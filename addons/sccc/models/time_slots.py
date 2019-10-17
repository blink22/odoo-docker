from odoo import models, fields, api
class TimeSlots(models.Model):
  _name = 'sccc.time_slots'
  name = fields.Char('Name')
  from_time = fields.Float('From')
  to_time = fields.Float('To')
  day_of_week = fields.Char('Day of Week')

  # Relations
  files = fields.Many2many('sccc.file', 'availability', string='Files')