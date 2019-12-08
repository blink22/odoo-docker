from odoo import models, fields, api
class MeetingStatus(models.Model):
  _name = 'sccc.meeting_status'
  _description = 'Status'

  name = fields.Char('Status')
  color = fields.Char('Color')

  # Relations
  meetings  = fields.One2many('sccc.calendar', 'meeting_status', string='Meetings')