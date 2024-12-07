# controllers/main.py
from odoo import http
from odoo.http import request, Response
import json
from ..metrics import user_collector
from ..metrics import product_collector


class MetricsAPI(http.Controller):

    @http.route('/metrics/users', auth='public', type='http', methods=['GET'])
    def get_users(self, **kwargs):
        user_data = user_collector.collect_user_data()
        json_data = json.dumps(user_data, default=str)
        return Response(json_data, content_type='application/json; charset=utf-8')

    @http.route('/metrics/products', auth='public', type='http', methods=['GET'])
    def get_products(self, **kwargs):
        product_data = product_collector.collect_product_data()
        json_data = json.dumps(product_data, default=str)
        return Response(json_data, content_type='application/json; charset=utf-8')

    @http.route('/metrics', auth='public', type='http', methods=['GET'])  # Ruta combinada (opcional)
    def get_metrics(self, **kwargs):
        user_data = user_collector.collect_user_data()
        product_data = product_collector.collect_product_data()

        data = {
            "odoo_active_users": user_data,
            "odoo_inventory_items": product_data,
        }

        json_data = json.dumps(data, default=str)
        return Response(json_data, content_type='application/json; charset=utf-8')