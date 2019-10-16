from odoo import models, fields, api
from datetime import date, datetime
class FeeAdjustment(models.Model):
  _name = 'sccc.fee_adjustment'
  upload_fee = fields.Binary('Upload Fee Form')
  added_date = fields.Date('Date added to system')
  today_date = fields.Date('Today\'s date', compute='_get_today')
  currency = fields.Monetary('Currency')
  currency_fee = fields.Monetary('Currency Fee')
  requested_fee = fields.Monetary('Requested Fee')
  request_reason = fields.Text('Reason for request')
  people_inhouse = fields.Float('Total # people in household (including yourself)')
  ages = fields.Char('Ages (those you financially support in parentheses)')
  monthly_gross = fields.Monetary('Your total monthly gross income')
  income_source = fields.Char('Describe income source')
  monthly_net = fields.Monetary('Your total monthly net income')
  partener_monthly_net = fields.Monetary('Spouse/partner\'s total monthly net income')
  net_source = fields.Char('Describe income source')
  other_income = fields.Monetary('Any other monthly after-tax income')
  total_income = fields.Monetary('Total after-tax income')
  paystub = fields.Binary('Paystub, Tax Return, W-2 Upload')
  board_approval = fields.Selection([('true', 'True'), ('false', 'False')], 'Board Approval')
  fee = fields.Monetary('Fee')

  # Relations
  file = fields.Many2one('sccc.file', string='File')
  counselor = fields.Many2one('sccc.counselor', string='Counselor')

  def _get_today(self):
    self.today_date = date.today()