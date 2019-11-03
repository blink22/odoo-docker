from odoo import models, fields, api

class Providers(models.Model):
    _name = 'sccc.provider'
    _description = 'Providers'

    name = fields.Char('Name', compute='_set_name', store=True)
    last_name = fields.Char('Last Name')
    first_name = fields.Char('First Name')
    in_crawl = fields.Boolean('In Crawl')
    out_of_office = fields.Boolean('Out of Office')
    lgbtq = fields.Boolean('LGBTQ')

    gender = fields.Selection([ ('m', 'Male'), ('f', 'Female') ], 'Gender')
    gender_pronouns = fields.Selection([('She/Her/Hers', 'She/Her/Hers'), ('He/Him/His', 'He/Him/His'), 
                                      ('They/Them/Theirs', 'They/Them/Theirs'), ('Not Listed', 'Not Listed')], 'Gender Pronouns')

    date_of_birth = fields.Date('Date of Birth')
    age = fields.Integer('Age', compute='_calculate_age', store=True, readonly=True)
    street = fields.Char('Street')
    apt_no = fields.Char('Apt/Suite No')
    city = fields.Char('City')
    zip_code = fields.Char('Zip')
    email = fields.Char('Email')
    cell_phone = fields.Char('Cell #')
    other = fields.Char('Other #')

    trained_for = fields.Selection([('WeCounsel', 'WeCounsel'), ('Couples/Family', 'Couples/Family'),
                                    ('Group', 'Group'), ('Psychiatry', 'Psychiatry')], 'Trained For')

    departments = fields.Selection([('Administration', 'Administration'), ('Counselors', 'Counselors'),
                                    ('Directors', 'Directors'), ('Front Desk', 'Front Desk'),
                                    ('Psychiatry', 'Psychiatry'), ('Coordinators', 'Coordinators')], 'Department')

    ethnicity = fields.Selection([('American Indian/Native American/Alaskan Native', 'American Indian/Native American/Alaskan Native'),
                                ('Asian', 'Asian'), ('Black', 'Black'), ('Latina/o/x', 'Latina/o/x'),
                                ('Middle Eastern or North African','Middle Eastern or North African'), ('Mixed','Mixed'), 
                                ('Native Hawaiian or Pacific Islander','Native Hawaiian or Pacific Islander'), 
                                ('White','White'), ('Other','Other'), ('Declines to Specify','Declines to Specify')], 'Ethnicity')

    language = fields.Char('Language')
    created_on = fields.Datetime("Date")
    
    # Relations
    availability = fields.Many2many('sccc.time_slots', 'time_slots_provider_rel', string='Availability (Time Slots)')
    files = fields.Many2many('sccc.file', 'provider_file_rel', string='Case Load')
    fam_assessment = fields.One2many('sccc.fam_assessment', 'provider', string='Fam Assessment')
    location = fields.One2many('sccc.location', 'provider', string='Location')

    @api.depends('last_name', 'first_name')
    def _set_name(self):
        last_name = ""
        if self.last_name:
            last_name = str(self.last_name)
        
        first_name = ""
        if self.first_name:
            first_name = str(self.first_name)

        self.name = last_name + ", " + first_name

    @api.depends('date_of_birth') 
    def _calculate_age(self):
        if self.date_of_birth: 
            years = relativedelta(date.today() , self.date_of_birth).years
            self.age = int(years)
        else:
            self.age = 0

    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')