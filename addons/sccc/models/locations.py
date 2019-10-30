from odoo import models, fields, api

class Locations(models.Model):
    _name = 'sccc.location'
    _description = 'Locations'

    name = fields.Char('Location Name')
    location_id = fields.Integer(string='Location ID', required=True, copy=False, readonly=True, index=True, default= lambda self: self.env['ir.sequence'].next_by_code('sccc.location_id_generate'))
    created_on = fields.Datetime("Date")

    # Relations
    room = fields.One2many('sccc.room', 'location', string='Room')
    counselor = fields.Many2one('sccc.counselor', string='Counselor')
    meeting = fields.One2many('sccc.calendar', 'location', string='Meeting')