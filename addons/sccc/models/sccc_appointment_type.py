from odoo import models, fields, api
class SCCCAppointmentType(models.Model):
  _name = 'sccc.sccc_appointment_type'
  type_name = fields.Char('Type Name')

  # Relations
  files = fields.Many2many('sccc.file', 'sccc_appointment_type', string='Files')