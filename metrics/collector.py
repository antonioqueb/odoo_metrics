from prometheus_client import CollectorRegistry, Gauge, generate_latest
from odoo import api, fields, models
from odoo.http import request

def metrics_generator():
    registry = CollectorRegistry()

    # Número de usuarios activos
    active_users = Gauge('odoo_active_users', 'Number of active Odoo users', registry=registry)
    active_users.set(len(request.env['res.users'].search([('active', '=', True)])))

    # Número de órdenes de venta recientes (último día)
    recent_sales = Gauge('odoo_recent_sales', 'Number of recent sales orders', registry=registry)
    recent_sales.set(len(request.env['sale.order'].search([('date_order', '>', (fields.Datetime.now() - fields.Datetime.delta(days=1)).strftime('%Y-%m-%d %H:%M:%S'))])))

    # Ejemplo de métrica adicional: Número de productos en inventario
    inventory_items = Gauge('odoo_inventory_items', 'Number of products in inventory', registry=registry)
    inventory_items.set(len(request.env['product.product'].search([])))

    # Aquí puedes añadir más métricas según tus necesidades

    return generate_latest(registry)