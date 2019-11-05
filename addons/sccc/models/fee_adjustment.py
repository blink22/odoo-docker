from odoo import models, fields, api
from datetime import date, datetime
class FeeAdjustment(models.Model):
  _name = 'sccc.fee_adjustment'
  _description = 'Fee Adjustments'

  name = fields.Char('Form Name')
  upload_fee = fields.Binary('Upload Fee Form')
  added_date = fields.Date('Date added to system')
  today_date = fields.Date('Today\'s date', readonly=True)
  currency_id = fields.Integer(compute='_get_currency', store=True)
  currency = fields.Monetary('Currency')
  current_fee = fields.Monetary('Current Fee')
  requested_fee = fields.Monetary('Requested Fee')
  request_reason = fields.Text('Reason for request')
  people_inhouse = fields.Float('Total # people in household (including yourself)')
  ages = fields.Char('Ages (those you financially support in parentheses)')
  monthly_gross = fields.Monetary('Your total monthly gross income')
  income_source = fields.Char('Describe income source')
  monthly_net = fields.Monetary('Your total monthly net income')
  partner_monthly_net = fields.Monetary('Spouse/partner\'s total monthly net income')
  net_source = fields.Char('Describe income source')
  other_income = fields.Monetary('Any other monthly after-tax income')
  total_income = fields.Monetary('Total after-tax income')
  paystub = fields.Binary('Paystub, Tax Return, W-2 Upload')
  board_approval = fields.Selection([('true', 'True'), ('false', 'False')], 'Board Approval')
  created_on = fields.Datetime("Date")

  # Relations
  files = fields.Many2many('sccc.file', 'fee_adjustment_file_rel', string='Files')
  provider = fields.Many2one('sccc.provider', string='provider')

  def _get_currency(self):
    user_obj = self.pool.get('res.users')
    currency_obj = self.pool.get('res.currency')
    user = user_obj.browse(cr, uid, uid, context = context)
    if user.company_id:
        self.currency_id = user.company_id.currency_id.id
    else:
        self.currency_id = currency_obj.search(cr, uid, [('rate', '=', 1.0)])[0]