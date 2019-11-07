from odoo import models, fields, api
class FeeSetting(models.Model):
  _name = 'sccc.fee_setting'
  _description = 'Fee Settings'
  _rec_name = 'combination'
  combination = fields.Char(string='Form Name', compute='_compute_fields_combination', store=True)

  form_upload = fields.Binary ('Upload Fee Form')
  today_date = fields.Date('Form Submission Date')
  currency_id = fields.Integer(compute='_get_currency', store=True)
  fee = fields.Float('Fee Set at')
  refered_to_fee = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Referred to Fee Review Committee?')
  currency = fields.Char('Currency')
  people_in = fields.Float('Total # people in household (including yourself)')
  client_employed = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Client Currently Employed?')
  monthly_gross = fields.Float('Client\'s total monthly gross income')

  source_of_salary = fields.Selection([ ('Full-time Employment', 'Full-time Employment'), 
                                        ('Part-Time Employment', 'Part-Time Employment'),
                                        ('Self-Employed','Self-Employed'), ('Other','Other') ], 'Source of salary/wages')
  other_specify = fields.Text('If other specify')
  public_assistance = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Receiving public assistance')
  monthly_income = fields.Float('If yes, what is client\'s monthly income from PA')

  source_of_pa_salary = fields.Selection([('General Relief', 'General Relief'), ('Social Security', 'Social Security'), 
                                          ('Unemployment Insurance', 'Unemployment Insurance'), ('Other', 'Other') ], 'Source of PA salary/wages')
  pa_source = fields.Text('If other, specify')

  source_of_client_income = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Does client have another source on income?')
  source_of_client = fields.Selection([ ('Savings', 'Savings'), ('Investments', 'Investments'),
                                        ('Allowances', 'Allowances'), ('Parents/Family/Friends', 'Parents/Family/Friends'),
                                        ('Partnew/Girlfriend/Boyfriend', 'Partnew/Girlfriend/Boyfriend'), ('Alimony/Child Support', 'Alimony/Child Support'),
                                        ('Other', 'Other') ], 'Client\'s other source of income')

  client_source = fields.Text('If other, specify')
  has_members = fields.Selection([ ('yes', 'Yes'), ('no', 'No') ], 'Are there any other members in client\'s family ')
  gross_monthly = fields.Float('What is gross monthly income of others')
  total_gross = fields.Float('Total Gross Monthly Income')
  
  # Relations
  file = fields.Many2one('sccc.file', string='File #', required=True)
  provider = fields.Many2one('sccc.provider', string='Provider')

  @api.depends('file') 
  def _compute_fields_combination(self):
    self.combination = str(self.file.file_number) + ' - ' + str(self.file.name) + ' Fee Setting Form'