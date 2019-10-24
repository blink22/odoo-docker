from odoo import models, fields, api
class TimeSlots(models.Model):
  _name = 'sccc.time_slots'
  _description = 'Time Slots'

  name = fields.Char('Name')
  from_time = fields.Float('From')
  to_time = fields.Float('To')
  day_of_week = fields.Char('Day of Week')
  created_on = fields.Datetime("Date")

  # Relations
  files = fields.Many2many('sccc.file', 'time_slots_file_rel', string='Files')
  counselor = fields.Many2many('sccc.counselor', 'time_slots_counselor_rel', string='Availability (Time Slots)')