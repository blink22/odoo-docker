from odoo import models, fields, api
class ProgressNotes(models.Model):
  _name = 'sccc.progress_notes'

  date = fields.Date('Date')
  synopsis = fields.Text('Synopsis')
  goals = fields.Text('Self-Described Goals')
  documentation = fields.Text('Documentation')
  follow_up = fields.Text('Intended Follow Up')
  next_session = fields.Date('Next Session')

  # Relations
  counselor = fields.Many2one('sccc.counselor', string='Counselor')
  files = fields.Many2many('sccc.file', 'progress_notes', string='Files')
  clients = fields.Many2one('sccc.client', string='Clients')