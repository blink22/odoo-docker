from odoo import models, fields, api, exceptions
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.addons.as_time.models import alsw
import json

class Calendar(models.Model):
    _name = 'sccc.calendar'
    _description = 'Meetings'
    _order = "start_date asc"

    _rec_name = 'combination'
    combination = fields.Char('Details', compute='_compute_fields_combination', store=True)

    name = fields.Char('Meeting Title', required=True)

    date = fields.Date('Date', required=True)
    start_time = alsw.Time('Start Time', required=True)
    end_time = alsw.Time('End Time', required=True)
    start_date = fields.Datetime('Start At')
    end_date = fields.Datetime('End At')
    
    status = fields.Selection([('Hold', 'Hold'), ('Match', 'Match'),
                                    ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], 'Status')

    appointment_type = fields.Selection([('Individual Counseling', 'Individual Counseling'), ('Psychiatry', 'Psychiatry'),
                                    ('TAPP-Individual', 'TAPP-Individual'), ('TAPP-Group', 'TAPP-Group'),
                                    ('Intake', 'Intake'), ('Group Counseling', 'Group Counseling'),
                                    ('Couples/Family Counseling', 'Couples/Family Counseling'), ('Other', 'Other'),
                                    ('Fee Adjustment', 'Fee Adjustment')], 'Appointment Type')

    non_transferrable = fields.Boolean('Non-transferrable')

    recurrent = fields.Boolean('Recurrent')
    privacy = fields.Selection([('Everyone', 'Everyone')], 'Privacy')
    show_time_as = fields.Selection([('Busy', 'Busy')], 'Show Time As')
    repeat_every = fields.Selection([('Day(s)', 'Day(s)'), ('Week(s)', 'Week(s)'), ('Month(s)', 'Month(s)'), ('Year(s)', 'Year(s)')], 'Unit')
    repeat_every_count = fields.Integer('Repeat Every')
    until_count = fields.Integer('Number of repetitions')

    created_on = fields.Datetime("Date")

    # Relations
    location = fields.Many2one('sccc.location', string='Location', required=True)
    room = fields.Many2one('sccc.room', string='Room', required=True)
    
    files = fields.Many2many('sccc.file', 'calendar_file_rel', string='File')
    client_attend = fields.Many2many('sccc.file', 'calendar_attendance_file_rel', string='Did Client Attend?')
    
    provider = fields.Many2one('sccc.provider', string='Provider')
    user_ids = fields.Many2many('res.users', string='Attendees', track_visibility='onchange', readonly=True, 
                              states={'draft': [('readonly', False)]}, default=lambda self: self.env.user)
    progress_notes = fields.Many2many('sccc.progress_notes', 'progress_notes_calendar_rel', string='Progress Notes')
    
    account_moves = fields.Many2many('account.move', 'account_move_calendar_rel', string='Account Invoices')
    payments = fields.Many2many('account.payment', 'account_payment_calendar_rel', string='Payments')

    @api.depends('provider') 
    def _compute_fields_combination(self):
        for meeting in self:
            meeting.combination = meeting.name
            if meeting.provider:
                meeting.combination += '\n'
                meeting.combination += ' ( ' + meeting.provider.name + ' )'
            for file in meeting.files:
                meeting.combination += '\n'
                meeting.combination += '( ' + file.file_number + ' - ' + file.name + ' )'

    @api.model
    def create(self, form_object):
        start_date = form_object['date'] + ' ' + form_object['start_time']
        end_date = form_object['date'] + ' ' + form_object['end_time']
        form_object['start_date'] = datetime.strptime(start_date, "%Y-%m-%d %I:%M%p")
        form_object['end_date'] = datetime.strptime(end_date, "%Y-%m-%d %I:%M%p")

        record = super(Calendar, self).create(form_object)
        self.check_repeat(form_object, record.until_count)
        return record

    @api.onchange('location')
    def selected_location(self):
        self.room = False
        res = {}
        if self.location:
            res['domain']={'room':[('location.location_id', '=', self.location.location_id)]}
        else:
            res['domain']={'room':[('id', '=', -1)]}
        return res

    def get_moves(self):
        moves = []
        self.account_moves = False
        if self.files:
            for file in self.files:
                for move in file.account_moves:
                    moves.append(move.id)
        self.account_moves = [(6, 0, moves)]

    def get_payments(self):
        payments = []
        if self.files:
            for file in self.files:
                for payment in file.payments:
                    payments.append(payment.id)
        self.payments = [(6, 0, payments)]

    @api.onchange('files')
    def selected_files(self):
        self.client_attend = False
        self.account_moves = False
        self.payments = False
        if self.files:
            self.client_attend = self.files
            self.get_moves()
            self.get_payments()
            
    def check_repeat(self, form_object, limit):
        if form_object['recurrent']:
            if limit > 0 and form_object['start_date'] and form_object['end_date']:
                amount = 0
                if form_object['repeat_every'] == 'Day(s)':
                    amount = relativedelta(days=form_object['repeat_every_count'])
                if form_object['repeat_every'] == 'Week(s)':
                    amount = relativedelta(weeks=form_object['repeat_every_count'])
                if form_object['repeat_every'] == 'Month(s)':
                    amount = relativedelta(months=form_object['repeat_every_count'])
                if form_object['repeat_every'] == 'Year(s)':
                    amount = relativedelta(years=form_object['repeat_every_count'])
                
                form_object['start_date'] = fields.Datetime.to_string(fields.Datetime.from_string(form_object['start_date']) + amount)
                form_object['end_date'] = fields.Datetime.to_string(fields.Datetime.from_string(form_object['end_date']) + amount)

                new_record = super(Calendar, self).create(form_object)
                self.check_repeat(form_object, limit-1)