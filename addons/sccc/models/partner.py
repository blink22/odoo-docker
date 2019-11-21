from odoo import models, fields
class Partner(models.Model):
  _inherit = 'res.partner'

  file = fields.Many2one('sccc.file', string='File #')