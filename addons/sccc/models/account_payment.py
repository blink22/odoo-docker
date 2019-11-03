from odoo import models, fields, api

class account_payment(models.Model):
  _inherit="account.payment"
  
  # Relations
  files = fields.Many2many('sccc.file', 'account_payment_file_rel', string='File #')
  meetings = fields.Many2many('sccc.calendar', 'account_payment_calendar_rel', string='Meetings')

  def unlink(self):
    result = models.Model.unlink(self)
    return result