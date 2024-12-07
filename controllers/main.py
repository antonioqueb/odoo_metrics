# controllers/main.py
from odoo import http
from odoo.http import request, Response  # Importa Response
import json
from ..metrics.collector import metrics_generator

class MetricsAPI(http.Controller):

    @http.route('/metrics', auth='public', type='http', methods=['GET'])
    def get_metrics(self, **kwargs):
        json_data = metrics_generator()
        return Response(json_data, content_type='application/json; charset=utf-8') # Usa Response