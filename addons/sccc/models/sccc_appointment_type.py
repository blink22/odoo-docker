from odoo import models, fields, api
class SCCCAppointmentType(models.Model):
  _name = 'sccc.sccc_appointment_type'
  type_name = fields.Char('Type Name')
  created_on = fields.Datetime("Date")

  # Relations
  files = fields.Many2many('sccc.file', 'sccc_appointment_type', string='Files')