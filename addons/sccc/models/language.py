from odoo import models, fields, api

class Language(models.Model):
  _name = 'sccc.language'

  name = fields.Char('Language Name')
  local = fields.Char('Language local')
  code = fields.Char('Language Code')

  # Relations
  clients = fields.One2many('sccc.client', 'client_language', string='Clients')