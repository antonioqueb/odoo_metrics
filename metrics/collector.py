from odoo import api, fields, models
from odoo.http import request
import json

def metrics_generator():
  # Build JSON data
  data = {
    "odoo_active_users": len(request.env['res.users'].search([('active', '=', True)])),
    "odoo_inventory_items": len(request.env['product.product'].search([]))
  }

  # Convert to JSON string
  json_data = json.dumps(data)

  return json_data