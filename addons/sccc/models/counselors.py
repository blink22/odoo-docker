from odoo import models, fields, api

class Counselors(models.Model):
    _name = 'sccc.counselor'

    name = fields.Char('Name')
    in_crawl = fields.Boolean('In Crawl')
    availability = fields.Char('Availability')

    # Relations
    files = fields.Many2many('sccc.file', string='Case Load')