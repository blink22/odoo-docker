from odoo import models, fields, api

class Ethnicity(models.Model):
  _name = 'sccc.ethnicity'

  name = fields.Char('Ethnicity Name')

  # Relations
  clients = fields.One2many('sccc.client', 'client_ethnicity', string='Clients')