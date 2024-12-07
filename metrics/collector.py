from odoo import api, fields, models
from odoo.http import request
import json

def metrics_generator():
    # Optimize queries and consider caching
    active_users = request.env['res.users'].search_count([('active', '=', True)])
    inventory_items = request.env['product.product'].search_count([])

    # Build JSON data
    data = {
        "odoo_active_users": active_users,
        "odoo_inventory_items": inventory_items
    }

    # Convert to JSON string
    json_data = json.dumps(data)

    return json_data