from odoo import models, fields, api
class IndividualAssessment(models.Model):
  _name = 'sccc.individual_assessment'
  _description = 'Individual Assessments'

  intake = fields.Binary('Upload Intake Form')
  date = fields.Date('Date & Time')
  goals = fields.Text('Self-Described Goals')
  ethnicity = fields.Selection([('American Indian/Native American/Alaskan Native', 'American Indian/Native American/Alaskan Native'),
                                ('Asian', 'Asian'), ('Black', 'Black'), ('Latina/o/x', 'Latina/o/x'),
                                ('Middle Eastern or North African','Middle Eastern or North African'), ('Mixed','Mixed'), 
                                ('Native Hawaiian or Pacific Islander','Native Hawaiian or Pacific Islander'), 
                                ('White','White'), ('Other','Other'), ('Declines to Specify','Declines to Specify')], 'Ethnicity')
                                
  relationship = fields.Selection([('married', 'Married'), ('single', 'Single'), ('divorced', 'Divorced')], 'Relationship Status')
  employed = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Currently Employed?')
  physical_health = fields.Text('How is client\'s physical health?')
  therapy = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Any prior Therapy?')
  therapy_reason = fields.Text('When? How long? why?')
  client_other_services = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Client Receiving other services here?')
  client_other_services_specify = fields.Text('If so, specify')
  client_services = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Client Received services in the past?')
  client_services_specify = fields.Text('If so, specify')
  psychiatric = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Any Psychiatric hospitalizations?')
  psychiatric_reason = fields.Text('When? How long? Why?')
  client_meds = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Is client taking meds?')
  client_meds_reason = fields.Text('What? How much? Reason?')
  client_attend_session = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Is client mandated to attend session?')
  anger_management = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Is client mandated to attend anger management?')
  anger_management_yes = fields.Text('If either Yes, please describe')
  social_service = fields.Text('Social Service System')
  criminal_justice = fields.Text('Criminal Justice System')
  homocidal_client = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Does client self report as HOMICIDAL?')
  person_threatened = fields.Char('If Yes, try to get the name of the person threatened')
  ind_suicidal_thoughts = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Indication of Suicidal thoughts')
  actively_suicidal = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Indication that Actively Suicidal')
  specific_means = fields.Text('Do they have specific means for Suicide?')
  means_access = fields.Text('Do they have access to those means?')
  plan_suicide = fields.Text('Do they have a plan for suicide?')
  immediate_intent = fields.Text('Do they have immediate intent?')
  attempted_suicide = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Have they attempted Suicide before?')
  long_ago = fields.Text('How long ago?')
  what_means = fields.Text('By what means?')
  suicidal_thoughts = fields.Text('What are the suicidal thoughts exactly?')
  occurence_often = fields.Text('How often do they occur?')
  help_stop_thoughts = fields.Text('Does anything help stop those thoughts?')
  additional_notes = fields.Text('Any Additional Notes')
  created_on = fields.Datetime("Date")

  # Relations
  file = fields.One2many('sccc.file', 'individual_assessment', string='File')
  counselor = fields.Many2one('sccc.counselor', string='Counselor')
  client = fields.Many2one('sccc.client', string='Client')