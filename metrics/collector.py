from odoo import api, fields, models
from odoo.http import request
import json

def metrics_generator():
  registry = CollectorRegistry()

  # ... Your existing code for defining gauges ...

  # Build JSON data
  data = {
    "odoo_active_users": active_users.get(),
    "odoo_recent_sales": recent_sales.get(),
    "odoo_inventory_items": inventory_items.get(),
    # Add more metrics to the data dictionary
  }

  # Convert to JSON string
  json_data = json.dumps(data)

  return json_data