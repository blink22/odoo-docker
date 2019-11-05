from odoo import models, fields, api
from odoo.addons.as_time.models import alsw
class TimeSlots(models.Model):
  _name = 'sccc.time_slots'
  _description = 'Time Slots'
  _rec_name = 'combination'
  combination = fields.Char(string='Availability', compute='_compute_fields_combination', store=True)
  
  from_time = alsw.Time('From')
  to_time = alsw.Time('To')
  day_of_week = fields.Selection([('Saturday','Saturday'),('Sunday','Sunday'),('Monday','Monday'),
                                  ('Tuesday','Tuesday'),('Wednesday','Wednesday'),('Thursday','Thursday'),
                                  ('Friday','Friday')], 'Day of Week', required=True)

  # Relations
  files = fields.Many2many('sccc.file', 'time_slots_file_rel', string='Files')
  provider = fields.Many2many('sccc.provider', 'time_slots_provider_rel', string='Availability (Time Slots)')

  @api.model
  def create(self, form_object):
    if form_object['from_time'] == False:
      form_object['from_time'] = '11:59:59 AM'

    if form_object['to_time'] == False:
      form_object['to_time'] = '11:59:59 AM'

    return super(TimeSlots, self).create(form_object)

  @api.depends('from_time', 'to_time', 'day_of_week') 
  def _compute_fields_combination(self):
    for slot in self:
      slot.combination = slot.day_of_week + ' ' + str(slot.from_time) + ' - ' + str(slot.to_time)