from odoo import http
from odoo.http import request
import json
from ..metrics.collector import metrics_generator

class MetricsAPI(http.Controller):

  # Consider using Odoo's authentication mechanisms for production
  @http.route('/metrics', auth='public', type='http', methods=['GET'])  # Adjust auth for production
  def get_metrics(self, **kwargs):
    json_data = metrics_generator()
    return json_data