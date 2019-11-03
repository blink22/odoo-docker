from odoo import models, fields, api
from random import randint

class Files(models.Model):
    _name = 'sccc.file'
    _description = 'Files'

    _rec_name = 'file_number'
    file_number = fields.Char('File #', readonly=True)

    name = fields.Char('File Name')
    out_reach = fields.Boolean('Outreach?')
    preferred_gender = fields.Selection([ ('m', 'Male'), ('f', 'Female') ], 'Preferred Gender')
    preferred_age = fields.Selection([ ('Below', 'Below'), ('Similar', 'Similar'), ('Above', 'Above')], 'Preferred Age')
    intake_date = fields.Date('Intake Date')
    
    # Appointment types
    type_1 = fields.Boolean('Individual Counseling')
    type_2 = fields.Boolean('Psychiatry')
    type_3 = fields.Boolean('TAPP - Individual')
    type_4 = fields.Boolean('TAPP - Group')
    type_5 = fields.Boolean('Intake')
    type_6 = fields.Boolean('Group Counseling')
    type_7 = fields.Boolean('Couples/Family Counseling')
    type_8 = fields.Boolean('WeCounsel')
    type_9 = fields.Boolean('Other')

    hold = fields.Boolean('Double Fee Hold')

    on_waitlist = fields.Boolean('Waitlist?')
    attended_session = fields.Boolean('Attended Session?')
    late = fields.Boolean('Late (NC)')
    left_early = fields.Boolean('Left Early (NC)')
    absent = fields.Boolean('Absent')
    terminated = fields.Boolean('Terminated?')
    
    lgbtq_counselor = fields.Boolean('Would like LGBTQ Counselor?')
    other_considerations = fields.Text('Other Considerations?')
    additional_notes = fields.Char('Additional Notes')
    created_on = fields.Datetime("Date")

    # Relations
    counselor = fields.Many2many('sccc.counselor', 'counselor_file_rel', string='Counselor')
    meetings = fields.Many2many('sccc.calendar', 'calendar_file_rel', string='Meetings')
    sessions = fields.Many2many('sccc.sessions', 'sessions_file_rel', string='Sessions')
    fee_setting = fields.Many2one('sccc.fee_setting', string='Fee Setting Form')
    fee_adjustment = fields.Many2many('sccc.fee_adjustment', 'fee_adjustment_file_rel', string='Fee Adjustment Form')
    individual_assessment = fields.Many2one('sccc.individual_assessment', string='Individual Assessment Form')
    fam_assessment = fields.Many2one('sccc.fam_assessment', string='FAM Assessment Form')
    availability = fields.Many2many('sccc.time_slots', 'time_slots_file_rel', string='Availability (Time Slots)')
    progress_notes = fields.Many2many('sccc.progress_notes', 'progress_notes_file_rel', string='Progress Notes')
    clients = fields.Many2many('sccc.client', 'client_file_rel', string='Clients')
    account_moves = fields.Many2many('account.move', 'account_move_file_rel', string='Account Invoices')
    payments = fields.Many2many('account.payment', 'account_payment_file_rel', string='Payments')

    # @api.onchange('account_moves')
    # def handle_account_moves(self):
    #     print('self', self.account_moves)
    #     for move in self.account_moves:
    #         print('move', move.display_name)
    #         print('journal', move.journal_id)
    #         print('journal', move.journal_id)
    #         for line2 in move.transaction_ids:
    #             print('line2', line2.display_name)
    #         for line in move.invoice_line_ids:
    #             print('line', line.name)

    @api.model
    def create(self, form_object):
        form_object['file_number'] = randint(0,999999)
        return super(Files, self).create(form_object)