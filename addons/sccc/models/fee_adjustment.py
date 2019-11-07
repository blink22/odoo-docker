from odoo import models, fields, api
from datetime import date, datetime
class FeeAdjustment(models.Model):
  _name = 'sccc.fee_adjustment'
  _description = 'Fee Adjustments'
  _rec_name = 'combination'
  combination = fields.Char(string='Form Name', compute='_compute_fields_combination', store=True)

  upload_fee = fields.Binary('Upload Fee Form')
  added_date = fields.Date('Date added to system', required=True)
  today_date = fields.Date('Today\'s date')
  currency = fields.Char('Currency')
  current_fee = fields.Float('Current Fee')
  requested_fee = fields.Float('Requested Fee')
  request_reason = fields.Text('Reason for request')
  people_inhouse = fields.Float('Total # people in household (including yourself)')
  ages = fields.Char('Ages (those you financially support in parentheses)')
  monthly_gross = fields.Float('Your total monthly gross income')
  income_source = fields.Char('Describe income source')
  monthly_net = fields.Float('Your total monthly net income')
  partner_monthly_net = fields.Float('Spouse/partner\'s total monthly net income')
  net_source = fields.Char('Describe income source')
  other_income = fields.Float('Any other monthly after-tax income')
  total_income = fields.Float('Total after-tax income')
  paystub = fields.Binary('Paystub, Tax Return, W-2 Upload')
  board_approval = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Board Approval')
  created_on = fields.Datetime("Date")

  # Relations
  file = fields.Many2one('sccc.file', string='File #', required=True)
  provider = fields.Many2one('sccc.provider', string='Provider')

  @api.depends('file') 
  def _compute_fields_combination(self):
    self.combination = str(self.file.file_number) + ' - ' + str(self.file.name) + ' Fee Adjustment'