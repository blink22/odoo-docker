from odoo import models, fields, api

class Counselors(models.Model):
    _name = 'sccc.counselor'

    name = fields.Char('Name', compute='_set_name', store=True)
    last_name = fields.Char('Last Name')
    first_name = fields.Char('First Name')
    in_crawl = fields.Boolean('In Crawl')
    availability = fields.Char('Availability')
    
    departments = fields.Selection([('Administration', 'Administration'), ('Counselors', 'Counselors'),
                                    ('Directors', 'Directors'), ('Front Desk', 'Front Desk'),
                                    ('Psychiatry', 'Psychiatry'), ('Coordinators', 'Coordinators')], 'Departments')

    ethnicity = fields.Selection([('American Indian/Native American/Alaskan Native', 'American Indian/Native American/Alaskan Native'),
                                ('Asian', 'Asian'), ('Black', 'Black'), ('Latina/o/x', 'Latina/o/x'),
                                ('Middle Eastern or North African','Middle Eastern or North African'), ('Mixed','Mixed'), 
                                ('Native Hawaiian or Pacific Islander','Native Hawaiian or Pacific Islander'), 
                                ('White','White'), ('Other','Other'), ('Declines to Specify','Declines to Specify')], 'Ethnicity')

    language = fields.Char('Language')
    created_on = fields.Datetime("Date")
    
    # Relations
    files = fields.Many2many('sccc.file', 'counselor_file_rel', string='Case Load')
    fam_assessment = fields.One2many('sccc.fam_assessment', 'counselor', string='Fam Assessment')
    location = fields.One2many('sccc.location', 'counselor', string='Location')

    @api.depends('last_name', 'first_name')
    def _set_name(self):
        last_name = ""
        if self.last_name:
            last_name = str(self.last_name)
        
        first_name = ""
        if self.first_name:
            first_name = str(self.first_name)

        self.name = last_name + ", " + first_name