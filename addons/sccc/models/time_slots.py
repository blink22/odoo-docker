from odoo import models, fields, api
class TimeSlots(models.Model):
  _name = 'sccc.time_slots'
  name = fields.Char('Name')
  time = fields.Float('Name')
  day_of_week = fields.Char('Day of Week')