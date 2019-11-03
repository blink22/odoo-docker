from odoo import models, fields, api

class Payments(models.Model):
    _name = 'sccc.payment'
    _description = 'Payments'

    name = fields.Char('Fee Title')
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
                                         ('provider_no_show','Provider No Show') ], 'Description Tag')
    date = fields.Date('Date')
    amount_due = fields.Float('Amount Due')
    amount_paid = fields.Float('Amount Paid')
    payment_method = fields.Selection([ ('cash', 'Cash'),
                                        ('credit_card', 'Credit Card'),
                                        ('other','Other') ], 'Payment Method')
    created_on = fields.Datetime("Created On")

    # Relations
    files = fields.Many2many('sccc.file', 'payment_file_rel', string='Files')
    provider = fields.Many2one('sccc.provider', string='Provider')
    meetings = fields.Many2many('sccc.calendar', 'payment_calendar_rel', string='Meetings')