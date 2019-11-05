from odoo import models, fields, api
class FeeSetting(models.Model):
  _name = 'sccc.fee_setting'
  _description = 'Fee Settings'
  _rec_name = 'combination'
  combination = fields.Char(string='Form Name', compute='_compute_fields_combination', store=True)

  form_upload = fields.Binary ('Upload Fee Form')
  added_date = fields.Date('Date added to system', required=True)
  today_date = fields.Date('Today\'s date')
  currency_id = fields.Integer(compute='_get_currency', store=True)
  fee = fields.Float('Fee Set at')
  refered_to_fee = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Referred to Fee Review Committee?')
  currency = fields.Char('Currency')
  people_in = fields.Float('Total # people in household (including yourself)')
  client_employed = fields.Selection([('a', 'A'), ('b', 'B')], 'Client Currently Employed?')
  monthly_gross = fields.Float('Client\'s total monthly gross income')
  source_of_salary = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Source of salary/wages')
  other_specify = fields.Text('If other specify')
  public_assistance = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Receiving public assistance')
  monthly_income = fields.Float('If yes, what is client\'s monthly income from PA')
  source_of_pa_salary = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Source of PA salary/wages')
  pa_source = fields.Text('If other, specify')
  source_of_client_income = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Does client have another source on income?')
  source_of_client = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Client\'s other source of income')
  client_source = fields.Text('If other, specify')
  has_members = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Are there any other members in client\'s family ')
  gross_monthly = fields.Float('What is gross monthly income of others')
  total_gross = fields.Float('Total Gross Monthly Income')
  created_on = fields.Datetime("Date")
  
  # Relations
  file = fields.Many2one('sccc.file', string='File #', required=True)
  provider = fields.Many2one('sccc.provider', string='Provider')

  @api.depends('file', 'added_date') 
  def _compute_fields_combination(self):
    for form in self:
      form.combination = str(form.file.file_number) + ' - ' + str(form.file.name) + ' Fee Adjustment ' + str(form.added_date)