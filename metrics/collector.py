from odoo import api, fields, models
from odoo.http import request
import json

def metrics_generator():
  # Build JSON data
  data = {
    "odoo_active_users": len(request.env['res.users'].search([('active', '=', True)])),
    "odoo_recent_sales": len(request.env['sale.order'].search([('date_order', '>', (fields.Datetime.now() - fields.Datetime.delta(days=1)).strftime('%Y-%m-%d %H:%M:%S'))])),
    "odoo_inventory_items": len(request.env['product.product'].search([]))
  }

  # Convert to JSON string
  json_data = json.dumps(data)

  return json_data