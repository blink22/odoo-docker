from odoo import models, fields, api
class ProgressNotes(models.Model):
  _name = 'sccc.progress_notes'
  _description = 'Progress Notes'
  _rec_name = 'combination'
  combination = fields.Char(string='Form Name', compute='_compute_fields_combination', store=True)

  date = fields.Date('Date Of Session', required=True)
  synopsis = fields.Text('Synopsis: overview, themes, client concerns, mood')
  goals = fields.Text('Self-described goals/resources (recent changes?)')
  documentation = fields.Text('Documentation: Legal/ethical matters, safety concerns')
  follow_up = fields.Text('Intended follow-up: phone calls, consultatios, refferals')
  next_session = fields.Date('Next Session')
  created_on = fields.Datetime("Date")

  # Relations
  provider = fields.Many2one('sccc.provider', string='Provider')
  file = fields.Many2one('sccc.file', string='File #')
  meetings = fields.Many2many('sccc.calendar', 'progress_notes_calendar_rel', string='Meetings')

  @api.depends('file', 'date') 
  def _compute_fields_combination(self):
    for form in self:
      form.combination = str(form.file.file_number) + ' - ' + str(form.file.name) + ' Progress Note ' + str(form.date)