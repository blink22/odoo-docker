from odoo import models, fields, api
import urllib3
import json

class SquarePayment(models.Model):
  _name = 'sccc.square_payment'
  _rec_name = 'square_payment_id'
  square_payment_id = fields.Char('SquareID')
  square_created_at = fields.Char('Date')
  square_amount = fields.Float('Amount')
  square_amount_currency = fields.Char('Amount Currency')
  square_total = fields.Float('Total')
  square_total_currency = fields.Char('Total Currency')
  square_order_id = fields.Char('SquareOrderID')
  square_location_id = fields.Char('SquareLocationID')
  square_status = fields.Char('SquareStatus')
  square_source = fields.Char('SquareSource')

  # @api.model
  # def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
  #   http = urllib3.PoolManager()
  #   URL = 'https://connect.squareup.com/v2/payments'
  #   payments = http.request('GET', URL, 
  #       headers={
  #        'Square-Version': '2019-11-20',
  #        'Authorization': 'Bearer EAAAEIajyYnvAZdDg-UcJP-2c1hPxDrnte9MUKOh1-myR-zG4yOLGaaJrRmrnsmJ'
  #       }
  #   )
  #   payments = json.loads(payments.data.decode('utf-8'))
  #   records = []
  #   for payment in payments['payments']:
  #     records.append(self.map_values(payment))
  #   return records
  
  @api.model
  def create(self, form_object):
    return super(SquarePayment, self).create(form_object)

  # def map_values(self, payment):
  #   return {
  #     'square_payment_id': payment['id'],
  #     'square_created_at': payment['created_at'],
  #     'square_amount': payment['amount_money']['amount'],
  #     'square_amount_currency': payment['amount_money']['currency'],
  #     'square_total': payment['total_money']['amount'],
  #     'square_total_currency': payment['total_money']['currency'],
  #     'square_order_id': payment['order_id'],
  #     'square_location_id': payment['location_id'],
  #     'square_status': payment['status'],
  #     'square_source': payment['source_type']
  #   }
