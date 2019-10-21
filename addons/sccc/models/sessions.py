from odoo import models, fields, api
class Sessions(models.Model):
  _name = 'sccc.sessions'
  session_name = fields.Char('Session Name')
  created_on = fields.Datetime("Date")

  # Relations
  files = fields.Many2many('sccc.file', 'sessions_file_rel', string='Files')