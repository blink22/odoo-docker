from odoo import models, fields, api
from random import randint

class Files(models.Model):
    _name = 'sccc.file'
    _description = 'Files'
    _rec_name = 'combination'
    combination = fields.Char (string='File', compute='_compute_fields_combination', store=True)

    file_number = fields.Char('File #', readonly=True)
    name = fields.Char('File Name', readonly=True)
    out_reach = fields.Boolean('Outreach?')
    preferred_gender = fields.Selection([ ('m', 'Male'), ('f', 'Female') ], 'Preferred Gender')
    preferred_age = fields.Selection([ ('Below', 'Below'), ('Similar', 'Similar'), ('Above', 'Above')], 'Preferred Age')

    if_group = fields.Selection([ ('1', 'Pesonal & Relational Support'), 
                                  ('2', 'Healing From Betrayal'), 
                                  ('3', 'Community Mindfulness & Compassion'),
                                  ('4', 'Best Practice Parenting'),
                                  ('5', 'Rage Resolution & Stress Navigation'),
                                  ('6', 'Teen')], 'If Group:')
    
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

    active_client = fields.Boolean('Active Client?')
    last_true_attendance = fields.Integer('True Attend')
    attended_session = fields.Boolean('Attended Session?')
    late = fields.Boolean('Late (NC)')
    left_early = fields.Boolean('Left Early (NC)')
    absent = fields.Boolean('Absent')
    terminated = fields.Boolean('Terminated?')
    
    lgbtq_provider = fields.Boolean('Would like LGBTQ Counselor?')
    other_considerations = fields.Text('Other Considerations?')
    additional_notes = fields.Char('Additional Notes')

    # Relations
    provider = fields.Many2many('sccc.provider', 'provider_file_rel', string='Provider')
    meetings = fields.Many2many('sccc.calendar', 'calendar_file_rel', string='Meetings')
    sessions = fields.Many2many('sccc.sessions', 'sessions_file_rel', string='Sessions')

    fee_adjustment = fields.One2many('sccc.fee_adjustment', 'file', string='Fee Adjustment Form')
    individual_assessment = fields.One2many('sccc.individual_assessment', 'file', string='Individual Assessment Form')
    fam_assessment = fields.One2many('sccc.fam_assessment', 'file', string='FAM Assessment Form')
    fee_setting = fields.One2many('sccc.fee_setting', 'file', string='Fee Setting Form')

    availability = fields.Many2many('sccc.time_slots', 'time_slots_file_rel', string='Availability (Time Slots)')
    progress_notes = fields.Many2many('sccc.progress_notes', 'progress_notes_file_rel', string='Progress Notes')
    clients = fields.Many2many('sccc.client', 'client_file_rel', string='Clients', required=True)
    account_moves = fields.Many2many('account.move', 'account_move_file_rel', string='Account Invoices')
    payments = fields.Many2many('account.payment', 'account_payment_file_rel', string='Payments')

    @api.onchange('attended_session')
    def handle_attendance1(self):
        if self.attended_session:
            self.late = False
            self.left_early = False
            self.absent = False

    @api.onchange('late')
    def handle_attendance2(self):
        if self.late:
            self.attended_session = False
            self.left_early = False
            self.absent = False

    @api.onchange('left_early')
    def handle_attendance3(self):
        if self.left_early:
            self.late = False
            self.attended_session = False
            self.absent = False

    @api.onchange('absent')
    def handle_attendance4(self):
        if self.absent:
            self.late = False
            self.left_early = False
            self.attended_session = False

    @api.depends('file_number', 'name') 
    def _compute_fields_combination(self):
        for file in self:
            file.combination = str(file.file_number) + ' - ' + str(file.name)

    @api.model
    def create(self, form_object):
        form_object['file_number'] = randint(0,999999)
        name = ''
        i = 0
        clients = self.env['sccc.client'].search([('id', 'in', form_object['clients'][0][2])])
        while i < len(clients):
            name += clients[i].name
            if i < len(clients)-1:
                name += ', '
            i += 1
        
        form_object['name'] = name
        return super(Files, self).create(form_object)