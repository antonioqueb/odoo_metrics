from odoo import http
from odoo.http import request
from ..metrics.collector import metrics_generator

class MetricsAPI(http.Controller):

    @http.route('/metrics', auth='public', type='http', methods=['GET'])
    def get_metrics(self, **kwargs):
        return metrics_generator()