from odoo import models, fields, api
class Files(models.Model):
    _name = 'sccc.file'

    _rec_name = 'file_number'
    file_number = fields.Integer('File #')

    name = fields.Char('File Name')
    out_reach = fields.Boolean('Outreach?')
    preferred_gender = fields.Selection([ ('m', 'Male'), ('f', 'Female') ], 'Preferred Gender')
    preferred_age = fields.Selection([ ('1', '21'), ('2', '22') ], 'Preferred Age')
    intake_date = fields.Date('Intake Date')
    
    currency_id = fields.Integer(compute='_get_currency', store="True")
    fee = fields.Monetary('Fee')
    balance = fields.Monetary('Balance')
    double_fee = fields.Boolean('Double Fee Hold')

    created_on = fields.Date('Created On',)
    on_waitlist = fields.Boolean('On Waitlist?')
    attended_session = fields.Boolean('Has Attended Session?')
    terminated = fields.Boolean('Terminated?')
    
    lgbtq_counselor = fields.Boolean('Would like LGBTQ Counselor?')
    other_considerations = fields.Text('Other Considerations?')
    additional_notes = fields.Char('Additional Notes')

    # Relations
    counselor = fields.Many2many('sccc.counselor', 'files', string='Counselor')
    meetings = fields.Many2many('sccc.calendar', 'files', string='Meetings')
    sessions = fields.Many2many('sccc.sessions', 'files', string='Sessions')
    fee_setting = fields.Many2one('sccc.fee_setting', string='Fee Setting Form')
    fee_adjustment = fields.Many2many('sccc.fee_adjustment', 'files', string='Fee Adjustment Form')
    payments = fields.Many2many('sccc.payments', 'files', string='Payments')
    individual_assessment = fields.Many2one('sccc.individual_assessment', string='Individual Assessment Form')
    fam_assessment = fields.Many2one('sccc.fam_assessment', string='FAM Assessment Form')
    sccc_appointment_type = fields.Many2many('sccc.sccc_appointment_type', 'files', string='SCCC Appointment Type')
    availability = fields.Many2many('sccc.time_slots', 'files', string='Availability (Time Slots)')
    progress_notes = fields.Many2many('sccc.progress_notes', 'files', string='Progress Notes')
    clients = fields.Many2many('sccc.client', 'files', string='Clients')

    def _get_currency(self):
        user_obj = self.pool.get('res.users')
        currency_obj = self.pool.get('res.currency')
        user = user_obj.browse(cr, uid, uid, context = context)
        if user.company_id:
            self.currency_id = user.company_id.currency_id.id
        else:
            self.currency_id = currency_obj.search(cr, uid, [('rate', '=', 1.0)])[0]