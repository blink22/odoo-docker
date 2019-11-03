from odoo import models, fields, api, exceptions
from datetime import datetime
from dateutil.relativedelta import relativedelta
import json

class Calendar(models.Model):
    _name = 'sccc.calendar'
    _description = 'Meetings'
    _order = "start_date asc"

    name = fields.Char('Meeting Title', required=True)
    start_date = fields.Datetime('Start At', required=True)
    end_date = fields.Datetime('End At', required=True)
    
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
    
    files = fields.Many2many('sccc.file', 'calendar_file_rel', string='File', required=True)
    client_attend = fields.Many2many('sccc.file', 'calendar_attendance_file_rel', string='Did Client Attend?')
    
    provider = fields.Many2one('sccc.provider', string='Provider', required=True)
    user_ids = fields.Many2many('res.users', string='Attendees', track_visibility='onchange', readonly=True, 
                              states={'draft': [('readonly', False)]}, default=lambda self: self.env.user)
    progress_notes = fields.Many2many('sccc.progress_notes', 'progress_notes_calendar_rel', string='Progress Notes')
    
    account_moves = fields.Many2many('account.move', 'account_move_calendar_rel', string='Account Invoices')
    payments = fields.Many2many('account.payment', 'account_payment_calendar_rel', string='Payments')
            
    @api.model
    def create(self, form_object):
        # self.validate_object(form_object)
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
            
            
    # def validate_object(self, form_object):
    #     records = super(Calendar, self).search([['room', '=', form_object['room']]])
    #     for record in records:
    #         print('------------------------------')
    #         print('record koko- ', str(record.start_date))
    #         print('record - ', str(record.end_date))
    #         print('record - ', record.room.id)
    #         print('form_object - ', str(form_object['start_date']))
    #         print('form_object - ', str(form_object['end_date']))
    #         print('form_object - ', form_object['room'])
    #         if form_object['room'] == record.room:
    #             record_start_end_delta = relativedelta(record.start_date , record.end_date)
    #             print('start_end_delta', start_end_delta)
    #             form_start_to_start_delta
    #             form_start_to_start_delta
    #             form_start_to_start_delta
    #             if str(form_object['start_date']) <= str(record.end_date):
    #                 print('error')
    #             if str(form_object['start_date']) >= str(record.start_date) and str(form_object['start_date']) <= str(record.end_date):
    #                 print('error')
    #     records = super(Calendar, self).search([['room', '=', form_object['room'], 
    #                                             ['start_date', '>=', form_object['start_date'], 
    #                                             ['end_date', '>=', form_object['start_date']]]])
    #     count = len(records)
    #     print('count', count)
    #     if count > 0:
    #         raise exceptions.ValidationError('-Already has a meeting assigned ! \n-You may choose a different Room or Time.')

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