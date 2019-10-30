from odoo import models, fields, api
from odoo.addons.as_time.models import alsw
class TimeSlots(models.Model):
  _name = 'sccc.time_slots'
  _description = 'Time Slots'
  _rec_name = 'day_of_week'
  
  from_time = alsw.Time('From')
  to_time = alsw.Time('To')
  day_of_week = fields.Selection([('Saturday','Saturday'),('Sunday','Sunday'),('Monday','Monday'),
                                  ('Tuesday','Tuesday'),('Wednesday','Wednesday'),('Thursday','Thursday'),
                                  ('Friday','Friday')], 'Day of Week')

  # Relations
  files = fields.Many2many('sccc.file', 'time_slots_file_rel', string='Files')
  counselor = fields.Many2many('sccc.counselor', 'time_slots_counselor_rel', string='Availability (Time Slots)')