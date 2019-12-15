# -*- coding: utf-8 -*-
from odoo import http
import json
import requests

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
#     def object(self, obj0, **kw):
#         return http.request.render('sccc.object', {
#             'object': obj
#         })
class Sccc(http.Controller):
    # example request is
    # http://localhost:8069/square/payments/webhook/
    # body = {"params": {"data":"123"}}
    # headers = Content-Type:application/json
    @http.route('/square/payments/webhook', type='json', auth='public', methods=['POST'])
    def fun(self, **post):
        body = json.loads(http.request.httprequest.data)
        payment_id = body["json"]["entity_id"]
        url = 'https://explorer-gateway.squareup.com/v2/payments/' + payment_id
        headers = { 
            'Content-Type': 'application/json',
            'Square-Version': '2019-11-20',
            'Authorization': 'Bearer EAAAEIajyYnvAZdDg-UcJP-2c1hPxDrnte9MUKOh1-myR-zG4yOLGaaJrRmrnsmJ'
        }
        r = requests.get(url, headers=headers)
        payment = json.loads(r.content)["payment"]
        mapped_payment = self.map_values(payment)
        records = http.request.env['sccc.square_payment'].create(mapped_payment)
        return {"status_code": 200}

    def map_values(self, payment):
        return {
          'square_payment_id': payment['id'],
          'square_created_at': payment['created_at'],
          'square_amount': payment['amount_money']['amount'],
          'square_amount_currency': payment['amount_money']['currency'],
          'square_total': payment['total_money']['amount'],
          'square_total_currency': payment['total_money']['currency'],
          'square_order_id': payment['order_id'],
          'square_location_id': payment['location_id'],
          'square_status': payment['status'],
          'square_source': payment['source_type']
        }
