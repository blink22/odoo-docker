from odoo import models, fields, api
class User(models.Model):
  _inherit = 'res.users'

  file = fields.Many2one('sccc.file', string='File #')