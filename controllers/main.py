from odoo import http
from odoo.http import request, Response
import json
from ..metrics import user_collector, product_collector, sales_collector
from odoo import fields
from dateutil.relativedelta import relativedelta

class MetricsAPI(http.Controller):
    @http.route('/metrics/users', auth='public', type='http', methods=['GET'])
    def get_users(self, **kwargs):
        user_data = user_collector.UserCollector().collect_user_data()
        json_data = json.dumps(user_data, default=str)
        return Response(json_data, content_type='application/json; charset=utf-8')

    @http.route('/metrics/products', auth='public', type='http', methods=['GET'])
    def get_products(self, **kwargs):
        product_data = product_collector.ProductCollector().collect_product_data()
        json_data = json.dumps(product_data, default=str)
        return Response(json_data, content_type='application/json; charset=utf-8')

    @http.route('/metrics/sales', auth='public', type='http', methods=['GET'])
    def get_sales(self, **kwargs):
        sales_data = sales_collector.SalesCollector().collect_sales_data()
        json_data = json.dumps(sales_data, default=str)
        return Response(json_data, content_type='application/json; charset=utf-8')

    @http.route('/metrics', auth='public', type='http', methods=['GET'])
    def get_metrics(self, **kwargs):
        user_data = user_collector.UserCollector().collect_user_data()
        product_data = product_collector.ProductCollector().collect_product_data()
        sales_data = sales_collector.SalesCollector().collect_sales_data()

        data = {
            "odoo_active_users": user_data,
            "odoo_inventory_items": product_data,
            "odoo_sales_metrics": sales_data,
        }
        
        json_data = json.dumps(data, default=str)
        return Response(json_data, content_type='application/json; charset=utf-8')