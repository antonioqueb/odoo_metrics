from odoo import api, fields, models
from odoo.http import request
import json

def metrics_generator():
    # Active Users with Last Activity (if mail module is installed)
    active_users = request.env['res.users'].search([('active', '=', True)])
    user_data = []
    for user in active_users:
        # Check for mail module and access last_activity_date
        if request.env.modules.get('mail'):
            last_activity = user.sudo().last_activity_date
        else:
            last_activity = None  # Set to None if mail module is not installed

        user_info = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'last_activity': last_activity,
            # Add more fields as needed: groups, roles, etc.
        }
        user_data.append(user_info)

    # Inventory Items
    inventory_items = request.env['product.product'].search([])
    item_data = []
    for item in inventory_items:
        item_info = {
            'id': item.id,
            'name': item.name,
            'quantity_on_hand': item.qty_available,
            'cost_price': item.standard_price,
            'sale_price': item.list_price,
            # Add more fields as needed: categories, suppliers, etc.
        }
        item_data.append(item_info)

    # Build JSON data
    data = {
        "odoo_active_users": user_data,
        "odoo_inventory_items": item_data
    }

    # Convert to JSON string
    json_data = json.dumps(data)

    return json_data