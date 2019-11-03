from odoo import models, fields, api

class account_payment(models.Model):
  _inherit="account.payment"
  
  # Relations
  files = fields.Many2many('sccc.file', 'account_payment_file_rel', string='File #')
  meetings = fields.Many2many('sccc.calendar', 'account_payment_calendar_rel', string='Meetings')

  def unlink(self):
    result = models.Model.unlink(self)
    return result

  @api.model
  def create(self, object):
    file_ids = self.env.context.get('file_ids')
    object['files'] = [[6, False, file_ids]]
    return super(account_payment, self).create(object)
    