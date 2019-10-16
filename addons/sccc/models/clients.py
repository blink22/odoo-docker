from odoo import models, fields, api
from datetime import date, datetime 
from dateutil.relativedelta import relativedelta

class Clients(models.Model):
  _name = 'sccc.client'

  name = fields.Char('Name', compute='_set_name')
  last_name = fields.Char('Last Name')
  first_name = fields.Char('First Name')
  out_reach = fields.Boolean('Outreach?')
  gender = fields.Selection([ ('m', 'Male'), ('f', 'Female') ], 'Gender')
  gender_pronouns = fields.Selection([('HE/SHE', 'HE/SHE'), ('HIM/HER', 'HIM/HER'), ('HIS/HER', 'HIS/HER'), ('HIS/HERS', 'HIS/HERS'), ('HIMSELF/HERSELF', 'HIMSELF/HERSELF')], 'Gender Pronouns')
  date_of_birth = fields.Date('Date of Birth')
  age = fields.Integer('Age', compute='_calculate_age')
  email = fields.Char('Email')
  cell_phone = fields.Char('Cell #')
  found_us = fields.Selection([('friend', 'Friend'), ('ads', 'Ads')], 'How did client find out about us?')
  street = fields.Char('Street')
  apt_no = fields.Char('Apt/Suite No')
  city = fields.Char('City')
  zip_code = fields.Char('Zip')
  other = fields.Char('Other #')
  brought_him = fields.Text('What brings you to the center?')
  first_visit = fields.Selection([('true', 'Yes'), ('false', 'No')], 'Is this your first visit?')
  when_first_visit = fields.Text('If no, when was it?')
  have_children = fields.Selection([('true', 'Yes'), ('false', 'No')], 'Have children?')
  in_counseling = fields.Selection([('true', 'Yes'), ('false', 'No')], 'Are you now in counseling?')
  in_counseling_with = fields.Text('If yes, with whom')
  counseling_type = fields.Selection([('a', 'A'), ('b', 'B')], 'What kind of counseling do you want?')
  interset = fields.Selection([('a', 'A'), ('b', 'B')], 'Interset in online psychotherapy')

  # Relations
  files = fields.Many2many('sccc.file', string='Files')
  ethnicity = fields.Many2one('sccc.ethnicity', string='Ethnicity')
  language = fields.Many2one('sccc.language', string='Language')

  @api.depends('last_name', 'first_name')
  def _set_name(self):
    last_name = ""
    if self.last_name:
      last_name = str(self.last_name)
    
    first_name = ""
    if self.first_name:
      first_name = str(self.first_name)

    self.name = last_name + ", " + first_name

  @api.depends('date_of_birth') 
  def _calculate_age(self):
    if self.date_of_birth: 
      years = relativedelta(date.today() , self.date_of_birth).years
      self.age = int(years)
    else:
      self.age = 0