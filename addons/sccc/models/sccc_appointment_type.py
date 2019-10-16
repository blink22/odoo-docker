from odoo import models, fields, api
class SCCCAppointmentType(models.Model):
  _name = 'sccc.sccc_appointment_type'
  type_name = fields.Char('Type Name')