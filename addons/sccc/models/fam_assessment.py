from odoo import models, fields, api

# If Mandated, attach documents here : many2many
# If so, who were they assigned to? : many2one
class FamAssessment(models.Model):
  _name = 'sccc.fam_assessment'

  intake = fields.Binary('Upload Intake Form')
  date = fields.Date('Date & Time')
  therapy_type = fields.Selection([('a', 'A'), ('b', 'B')], 'What type of therapy is this?')
  language_needs = fields.Text('Does family/couple have any language needs?')
  individual_counseling = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Family/Couple members received individual counseling?')
  currency_id = fields.Integer(_computed='_get_currency')
  outstanding_balance = fields.Monetary('Any outstanding balance?')
  mandated_therapy = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Is client mandated to attend therapy?')
  mandated_therapy_agency = fields.Text('If yes, which agency?')
  # Is this right?
  mandated_attachments = fields.Binary('If Mandated, attach documents here')
  #
  bringing_reason = fields.Text('What is your sense of what is bringing this couple/family?')
  concerns = fields.Text('Please document your concerns')
  referral = fields.Text('Any other referrals made to this couple/family?')
  able_assign = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Were you able to assign this couple/family?')
  # Is this right?
  client = fields.Many2one('sccc.client', 'If so, who were they assigned to?')
  #
  appointment_date = fields.Date('Date/time of appointment')
  fee = fields.Monetary('Fee')
  additional_notes = fields.Text('Additional notes')

  # Relations
  file = fields.One2many('sccc.file', 'fam_assessment', string='File')
  counselor = fields.Many2one('sccc.counselor', string='Counselor')

  def _get_currency(self):
    user_obj = self.pool.get('res.users')
    currency_obj = self.pool.get('res.currency')
    user = user_obj.browse(cr, uid, uid, context = context)
    if user.company_id:
        self.currency_id = user.company_id.currency_id.id
    else:
        self.currency_id = currency_obj.search(cr, uid, [('rate', '=', 1.0)])[0]
