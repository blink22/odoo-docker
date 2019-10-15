# -*- coding: utf-8 -*-
from odoo import http

# class Sccc(http.Controller):
#     @http.route('/sccc/sccc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sccc/sccc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sccc.listing', {
#             'root': '/sccc/sccc',
#             'objects': http.request.env['sccc.sccc'].search([]),
#         })

#     @http.route('/sccc/sccc/objects/<model("sccc.sccc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sccc.object', {
#             'object': obj
#         })