from odoo import models, fields, api

class Calendar(models.Model):
    _name = 'sccc.calendar'

    name = fields.Char('Meeting Title')
    start_date = fields.Datetime('Start Date/Time')
    end_date = fields.Datetime('End Date/Time')
    duration = fields.Float('Duration')
    
    # Relations
    room = fields.Many2one('sccc.room', string='Room')
    files = fields.Many2many('sccc.file', 'meetings', string='Files')
    counselor = fields.Many2one('sccc.counselor', string='Counselor')