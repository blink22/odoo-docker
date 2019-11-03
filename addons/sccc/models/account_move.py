from odoo import models, fields, api

class CustomAccountInvoice(models.Model):
    _inherit="account.move"
    
    # Relations
    files = fields.Many2many('sccc.file', 'account_move_file_rel', string='Files')
    meetings = fields.Many2many('sccc.calendar', 'account_move_calendar_rel', string='Meetings')

    def unlink(self):
        for move in self:
            # if move.name != '/' and not self._context.get('force_delete'):
            #     raise UserError(_("You cannot delete an entry which has been posted once."))
            move.line_ids.unlink()
        return models.Model.unlink(self)
    
    def action_invoice_register_payment(self):
        return self.env['account.payment']\
            .with_context(active_ids=self.ids, active_model='account.move', active_id=self.id, file_ids=self.files.ids)\
            .action_register_payment()