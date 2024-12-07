# metrics/product_collector.py
from odoo import http
import json

def collect_product_data():
    """
    Collects data for product items.
    """
    inventory_items = http.request.env['product.product'].search([])
    item_data = []

    for item in inventory_items:
        item_info = {
            'id': item.id,
            'name': item.name,
            'quantity_on_hand': item.qty_available,
            'cost_price': item.standard_price,
            'sale_price': item.list_price,
            'category': item.categ_id.name,
            'description_sale': item.description_sale,
            'barcode': item.barcode,
            'default_code': item.default_code,
            'weight': item.weight,
            'volume': item.volume,
            'type': item.type,
        }
        item_data.append(item_info)
    return item_data