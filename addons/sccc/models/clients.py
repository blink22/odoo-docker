from odoo import models, fields, api
from datetime import date, datetime 
from dateutil.relativedelta import relativedelta

class Clients(models.Model):
  _name = 'sccc.client'
  _description = 'Clients'
  
  name = fields.Char('Name', compute='_set_name', store=True, readonly=True)
  last_name = fields.Char('Last Name')
  first_name = fields.Char('First Name')
  out_reach = fields.Boolean('Outreach?')
  gender = fields.Selection([ ('m', 'Male'), ('f', 'Female') ], 'Gender')
  gender_pronouns = fields.Selection([('She/Her/Hers', 'She/Her/Hers'), ('He/Him/His', 'He/Him/His'), 
                                      ('They/Them/Theirs', 'They/Them/Theirs'), ('Not Listed', 'Not Listed')], 'Gender Pronouns')

  ethnicity = fields.Selection([('American Indian/Native American/Alaskan Native', 'American Indian/Native American/Alaskan Native'),
                                ('Asian', 'Asian'), ('Black', 'Black'), ('Latina/o/x', 'Latina/o/x'),
                                ('Middle Eastern or North African','Middle Eastern or North African'), ('Mixed','Mixed'), 
                                ('Native Hawaiian or Pacific Islander','Native Hawaiian or Pacific Islander'), 
                                ('White','White'), ('Other','Other'), ('Declines to Specify','Declines to Specify')], 'Ethnicity')
  
  date_of_birth = fields.Date('Date of Birth')
  age = fields.Integer('Age', compute='_calculate_age', store=True, readonly=True)
  email = fields.Char('Email')
  cell_phone = fields.Char('Cell #')

  found_us = fields.Selection([('Friend', 'Friend'), ('Advertisement', 'Advertisement'),
                               ('Family member','Family member'), ('Mandated','Mandated'), ('Guidance counselor','Guidance counselor'), 
                               ('Outreach','Outreach'), ('Website','Website'), ('Other','Other'), ('Google, etc.','Google, etc.')], 'How did client find out about us?')
  street = fields.Char('Street')
  apt_no = fields.Char('Apt/Suite No')
  city = fields.Char('City')
  zip_code = fields.Char('Zip')
  other = fields.Char('Other #')
  brought_him = fields.Text('What brings you to the center?')
  first_visit = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Is this your first visit?')
  when_first_visit = fields.Text('If no, when was it?')
  have_children = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Have children?')
  in_counseling = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Are you now in counseling?')
  in_counseling_with = fields.Text('If yes, with whom')

  counseling_type = fields.Selection([('Individual', 'Individual'), ('Family', 'Family'),
                                      ('Couple', 'Couple'), ('Group', 'Group')], 'What kind of counseling do you want?')
  interset = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Interested in online psychotherapy?')
  identify_center = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'When calling your cell phone, may we identify the center?')
  voicemail = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Is there a working voicemail that you check at this #?')
  client_language = fields.Char('Language')
  created_on = fields.Datetime("Date")
  
  # Relations
  files = fields.Many2many('sccc.file', 'client_file_rel', string='Files')

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

  @api.onchange('email')
  def validate_mail(self):
    if self.email:
      match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
      if match == None:
        raise ValidationError('Not a valid E-mail ID')