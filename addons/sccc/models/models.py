# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Locations(models.Model):
    _name = 'sccc.location'

    name = fields.Char('Location Name')
    location_id = fields.Integer(string='Location ID', required=True, copy=False, readonly=True, index=True, default= lambda self: self.env['ir.sequence'].next_by_code('sccc.location_id_generate'))
    room = fields.One2many('sccc.room', 'location', string='Room')

class Rooms(models.Model):
    _name = 'sccc.room'

    name = fields.Char('Room Name')
    location = fields.Many2one('sccc.location', string='Location')
    type = fields.Selection([ ('family', 'FAMILY'),('mirror', 'MIRROR'), ('individual','INDIVIDUAL') ], 'Type')

class Counselors(models.Model):
    _name = 'sccc.counselor'

    name = fields.Char('Name')
    in_crawl = fields.Boolean('In Crawl')
    availability = fields.Char('Availability')
    files =fields.Many2many('sccc.file', string='Case Load')

class Files(models.Model):
    _name = 'sccc.file'

    _rec_name='file_number'

    counselor = fields.Many2many('sccc.counselor', 'files', string='Counselor')
    meetings = fields.Many2many('sccc.calendar', 'files', string='Meetings')
    file_number = fields.Integer('File#')
    name = fields.Char('Name')
    clients = fields.Many2many('sccc.client', string='Clients')
    intake_date = fields.Date('Intake Date')
    availability = fields.Char('Availability')
    waitlist = fields.Boolean('Waitlist')
    double_fee = fields.Boolean('Double Fee')
    lgbtq_counselor = fields.Boolean('LGBTQ Counselor')
    other_considerations = fields.Char('Other Considerations')
    additional_notes = fields.Char('Additional Notes')

class Clients(models.Model):
    _name = 'sccc.client'

    name = fields.Char('Name')
    first_name = fields.Char('First Name')
    last_name = fields.Char('First Name')
    date_of_birth = fields.Date('Date of Birth')
    email = fields.Char('Email')
    cell_phone = fields.Char('Cell')
    counseling_type = fields.Char('Counseling Type')
    files = fields.Many2many('sccc.file', string='Files')

class Payments(models.Model):
    _name = 'sccc.payment'

    name = fields.Char('Fee Title')
    file = fields.Many2one('sccc.file', string='File #')
    counselor = fields.Many2one('sccc.counselor', 'Counselor')
    description_tag = fields.Selection([ ('session', 'Session'),
                                         ('wecounsel', 'WeCounsel'),
                                         ('client_cancellation', 'Client Cancellation'),
                                         ('late_cancellation', 'Late Cancellation (Fee)'),
                                         ('client_no_show', 'Client No Show (Fee)'),
                                         ('intake', 'Intake'),
                                         ('assessment', 'Assessment'),
                                         ('payment', 'Payment'),
                                         ('correction', 'Correction'),
                                         ('phone_session', 'Phone Session'),
                                         ('group', 'Group'),
                                         ('counselor_no_show','Counselor No Show') ], 'Description Tag')
    date = fields.Date('Date')
    amount_due = fields.Float('Amount Due')
    amount_paid = fields.Float('Amount Paid')
    payment_method = fields.Selection([ ('cash', 'Cash'),
                                        ('credit_card', 'Credit Card'),
                                        ('other','Other') ], 'Payment Method')

class Calendar(models.Model):
    _name = 'sccc.calendar'

    name = fields.Char('Meeting Title')
    files = fields.Many2many('sccc.file', 'meetings', string='Files')
    counselor = fields.Many2one('sccc.counselor', string='Counselor')
    start_date = fields.Datetime('Start Date/Time')
    end_date = fields.Datetime('End Date/Time')
    duration = fields.Float('Duration')
    room = fields.Many2one('sccc.room', 'Room')
