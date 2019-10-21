from odoo import models, fields, api

class Calendar(models.Model):
    _name = 'sccc.calendar'

    name = fields.Char('Meeting Title')
    start_date = fields.Datetime('Start Date/Time')
    end_date = fields.Datetime('End Date/Time')
    duration = fields.Float('Duration')
    created_on = fields.Datetime("Date")
    
    # Relations
    room = fields.Many2one('sccc.room', string='Room')
    files = fields.Many2many('sccc.file', 'calendar_file_rel', string='Files')
    counselor = fields.Many2one('sccc.counselor', string='Counselor')