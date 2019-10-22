from odoo import models, fields, api
class ProgressNotes(models.Model):
  _name = 'sccc.progress_notes'

  name = fields.Char('Name')
  date = fields.Date('Date Of Session')
  synopsis = fields.Text('Synopsis: overview, themes, client concerns, mood')
  goals = fields.Text('Self-described goals/resources (recent changes?)')
  documentation = fields.Text('Documentation: Legal/ethical matters, safety concerns')
  follow_up = fields.Text('Intended follow-up: phone calls, consultatios, refferals')
  next_session = fields.Date('Next Session')
  created_on = fields.Datetime("Date")

  # Relations
  counselor = fields.Many2one('sccc.counselor', string='Counselor')
  files = fields.Many2many('sccc.file', 'progress_notes_file_rel', string='Files')
  meetings = fields.Many2many('sccc.calendar', 'progress_notes_calendar_rel', string='Meetings')