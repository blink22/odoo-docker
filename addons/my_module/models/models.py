# -*- coding: utf-8 -*-

from odoo import models, fields, api

class my_module(models.Model):
    _name = 'my_module.my_module'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

    def open_to_form_view(self, cr, uid, ids, context=None):
    
        if not context:
            context = {}

        name = 'Edit'
        res_model = 'my_module.my_module' 
        view_name = '<view>' 
        
        document_id = self.browse(cr, uid, ids[0]).id

        view = models.get_object_reference(cr, uid, name, view)
        view_id = view and view[1] or False


        return {
            'name': (name),
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': [view_id],
            'res_model': res_model, 
            'type': 'ir.actions.act_window',
            'nodestroy': True,
            'target': 'current',
            'res_id': document_id,
        }