from odoo import models, fields, api

class Rooms(models.Model):
    _name = 'sccc.room'

    name = fields.Char('Room Name')
    type = fields.Selection([ ('family', 'FAMILY'),('mirror', 'MIRROR'), ('individual','INDIVIDUAL') ], 'Type')
    created_on = fields.Datetime("Date")

    # Relations
    location = fields.Many2one('sccc.location', string='Location')