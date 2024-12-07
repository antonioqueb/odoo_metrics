# metrics/product_collector.py
from odoo import http, api
import json

def collect_product_data():
    """
    Collects data for product items, including calculated fields.
    """
    inventory_items = http.request.env['product.product'].search([])
    item_data = []

    for item in inventory_items:
        # Calcula el valor del inventario
        inventory_value = item.qty_available * item.standard_price

        # Calcula el margen de beneficio
        profit_margin = (item.list_price - item.standard_price) / item.list_price if item.list_price else 0

        # Calcula las ventas totales (requiere el módulo sale_management)
        total_sales = 0
        if http.request.env.modules.get('sale_management'):
            sales_lines = http.request.env['sale.order.line'].search([('product_id', '=', item.id)])
            total_sales = sum(sales_lines.mapped('price_subtotal'))


        item_info = {
            'id': item.id,
            'default_code': item.default_code,
            'name': item.name,
            'quantity_on_hand': item.qty_available,
            'cost_price': item.standard_price,
            'sale_price': item.list_price,
            'barcode': item.barcode,
            'taxes_id': [{'id': tax.id, 'name': tax.name} for tax in item.taxes_id],
            'category': {'id': item.categ_id.id, 'name': item.categ_id.name} if item.categ_id else None,
            'description_sale': item.description_sale,
            'weight': item.weight,
            'volume': item.volume,
            'type': item.type,
            'route_ids': [{'id': route.id, 'name': route.name} for route in item.route_ids],
            'tracking': item.tracking,
            'property_stock_production': {'id': item.property_stock_production.id, 'name': item.property_stock_production.name} if item.property_stock_production else None,
            'property_stock_inventory': {'id': item.property_stock_inventory.id, 'name': item.property_stock_inventory.name} if item.property_stock_inventory else None,
            'purchase_ok': item.purchase_ok,
            'sale_ok': item.sale_ok,
            'inventory_value': inventory_value,
            'profit_margin': profit_margin,
            'total_sales': total_sales,
        }
        item_data.append(item_info)
    return item_data