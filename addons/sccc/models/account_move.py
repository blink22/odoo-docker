from odoo import models, fields, api

class CustomAccountInvoice(models.Model):
    _inherit="account.move"
    
    # Relations
    files = fields.Many2many('sccc.file', 'account_move_file_rel', string='Files')