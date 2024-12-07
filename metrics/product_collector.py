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
            'default_code': item.default_code,
            'name': item.name,
            'quantity_on_hand': item.qty_available,
            'cost_price': item.standard_price,
            'sale_price': item.list_price,
            'barcode': item.barcode,
            'taxes_id': item.taxes_id,
            'category': item.categ_id.name,
            'description_sale': item.description_sale,
            'barcode': item.barcode,
            'default_code': item.default_code,
            'weight': item.weight,
            'volume': item.volume,
            'type': item.type,
            'route_ids': item.route_ids,
            'tracking': item.tracking,
            'property_stock_production': item.property_stock_production,
            'property_stock_inventory': item.property_stock_inventory,
        }
        item_data.append(item_info)
    return item_data