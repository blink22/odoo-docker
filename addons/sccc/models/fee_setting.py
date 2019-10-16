from odoo import models, fields, api
class FeeSetting(models.Model):
  _name = 'sccc.fee_setting'

  form_upload = fields.Binary ('Upload Fee Form')
  added_date = fields.Date('Date added to system')
  today_date = fields.Date('Today\'s date')
  fee = fields.Monetary('Fee Set at')
  refered_to_fee = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Referred to Fee Review Committee?')
  currency = fields.Monetary('Currency')
  people_in = fields.Float('Total # people in household (including yourself)')
  client_employed = fields.Selection([('a', 'A'), ('b', 'B')], 'Client Currently Employed?')
  monthly_gross = fields.Monetary('Client\'s total monthly gross income')
  source_of_salary = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Source of salary/wages')
  other_specify = fields.Text('If other specify')
  public_assistance = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Receiving public assistance')
  monthly_income = fields.Monetary('If yes, what is client\'s monthly income from PA')
  source_of_pa_salary = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Source of PA salary/wages')
  pa_source = fields.Text('If other, specify')
  source_of_client_income = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Does client have another source on income?')
  source_of_client = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Client\'s other source of income')
  client_source = fields.Text('If other, specify')
  has_members = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Are there any other members in client\'s family ')
  gross_monthly = fields.Monetary('What is gross monthly income of others')
  total_gross = fields.Monetary('Total Gross Monthly Income')

  # Relations
  files = fields.Many2one('sccc.file', 'File')
  counselor = fields.Many2one('sccc.counselor', 'Counselor')