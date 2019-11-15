from odoo import models, fields, api

# If Mandated, attach documents here : many2many
# If so, who were they assigned to? : many2one
class FamAssessment(models.Model):
  _name = 'sccc.fam_assessment'
  _description = 'Family Assessments'
  _rec_name = 'combination'
  combination = fields.Char(string='Form Name', compute='_compute_fields_combination', store=True)

  intake = fields.Binary('Upload Intake Form')
  date = fields.Date('Intake Date', required=True)
  therapy_type = fields.Selection([('Family', 'Family'), ('Couple', 'Couple'), ('Child','Child')], 'Therapy Type')
  language_needs = fields.Text('Does family/couple have any language needs?')
  
  outstanding_balance = fields.Float('Any outstanding balance? (Must be $0 for assignment)')
  mandated_therapy = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Is client mandated to attend therapy?')
  mandated_therapy_agency = fields.Text('If yes, which agency?')
  # Is this right?
  mandated_attachments = fields.Binary('If Mandated, attach documents here')
  #
  bringing_reason = fields.Text('What is your sense of what is bringing this couple/family in?')
  concerns = fields.Text('Please document your concerns')
  referral = fields.Text('Any other referrals made to this couple/family?')
  able_assign = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Were you able to assign this couple/family?')
  # Is this right?
  
  #
  appointment_date = fields.Datetime('Date/time of appointment')
  fee = fields.Float('Fee')
  additional_notes = fields.Text('Additional notes')
  created_on = fields.Datetime("Date")

  # Relations
  file = fields.Many2one('sccc.file', string='File')
  clients = fields.Many2many('sccc.client', 'fam_assessment_clients_rel', string='Family/Couple members received individual counseling?')
  provider = fields.Many2one('sccc.provider', string='Intake Provider')
  # assigned_to = fields.Many2many('sccc.provider', string='If so, who were they assigned to?')

  @api.depends('file', 'date') 
  def _compute_fields_combination(self):
    for form in self:
      form.combination = str(form.file.file_number) + ' - ' + str(form.file.name) + ' Family Assessment ' + str(form.date)