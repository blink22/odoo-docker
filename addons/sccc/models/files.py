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
    preferred_age = fields.Selection([ ('1', '21'), ('2', '22') ], 'Preferred Age')
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

    currency_id = fields.Integer(compute='_get_currency', store=True)
    fee = fields.Monetary('Fee')
    balance = fields.Monetary('Balance')
    hold = fields.Boolean('Hold')

    on_waitlist = fields.Boolean('On Waitlist?')
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
    payments = fields.Many2many('sccc.payment', 'payment_file_rel', string='Payments')
    individual_assessment = fields.Many2one('sccc.individual_assessment', string='Individual Assessment Form')
    fam_assessment = fields.Many2one('sccc.fam_assessment', string='FAM Assessment Form')
    availability = fields.Many2many('sccc.time_slots', 'time_slots_file_rel', string='Availability (Time Slots)')
    progress_notes = fields.Many2many('sccc.progress_notes', 'progress_notes_file_rel', string='Progress Notes')
    clients = fields.Many2many('sccc.client', 'client_file_rel', string='Clients')
    account_moves = fields.Many2many('account.move', 'account_file_rel', string='Account Moves')

    @api.model
    def create(self, form_object):
        form_object['file_number'] = randint(0,999999)
        return super(Files, self).create(form_object)

    def _get_currency(self):
        user_obj = self.pool.get('res.users')
        currency_obj = self.pool.get('res.currency')
        user = user_obj.browse(cr, uid, uid, context = context)
        if user.company_id:
            self.currency_id = user.company_id.currency_id.id
        else:
            self.currency_id = currency_obj.search(cr, uid, [('rate', '=', 1.0)])[0]