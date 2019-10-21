from odoo import models, fields, api
class AppointmentType(models.Model):
  _name = 'sccc.appointment_type'
  name = fields.Char('Name')
  
  created_on = fields.Datetime("Date")

  # Relations
  files = fields.Many2many('sccc.file', 'appointment_type_file_rel', string='Files')