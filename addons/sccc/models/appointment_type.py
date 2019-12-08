from odoo import models, fields, api
class AppointmentType(models.Model):
  _name = 'sccc.appointment_type'
  _description = 'Appointment Type'

  name = fields.Char('Name')

  # Relations
  files = fields.Many2many('sccc.file', 'appointment_type_file_rel', string='Files')