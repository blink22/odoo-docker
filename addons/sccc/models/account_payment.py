from odoo import models, fields, api

class account_payment(models.Model):
    _inherit="account.payment"
    
    def unlink(self):
      return models.Model.unlink(self)