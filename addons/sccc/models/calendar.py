from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta
import json

class Calendar(models.Model):
    _name = 'sccc.calendar'
    _description = 'Meetings'

    name = fields.Char('Meeting Title')
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
    mon = fields.Boolean('Mon')
    tue = fields.Boolean('Tue')
    wed = fields.Boolean('Wed')
    thu = fields.Boolean('Thu')
    fri = fields.Boolean('Fri')
    sat = fields.Boolean('Sat')
    sun = fields.Boolean('Sun')

    client_attend = fields.Boolean('Did Client Attend?')

    created_on = fields.Datetime("Date")

    # Relations
    location = fields.Many2one('sccc.location', string='Location')
    room = fields.Many2one('sccc.room', string='Room')
    files = fields.Many2many('sccc.file', 'calendar_file_rel', string='File')
    counselor = fields.Many2one('sccc.counselor', string='Counselor')
    user_ids = fields.Many2many('res.users', string='Attendees', track_visibility='onchange', readonly=True, 
                              states={'draft': [('readonly', False)]}, default=lambda self: self.env.user)
    progress_notes = fields.Many2many('sccc.progress_notes', 'progress_notes_calendar_rel', string='Progress Notes')
    payment = fields.Many2many('sccc.payment', 'payment_calendar_rel', string='Payment')

    @api.model
    def create(self, form_object):
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

            

