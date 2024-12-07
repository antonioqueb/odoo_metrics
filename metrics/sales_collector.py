from odoo import api, models, fields
from dateutil.relativedelta import relativedelta

class SalesCollector(models.AbstractModel):
    _name = 'metrics.sales_collector'

    @api.model
    def collect_sales_data(self):
        # Fetching sales data, for example, total sales amount for the last 30 days
        today = fields.Date.today()
        start_date = today - relativedelta(days=30)
        sales = self.env['sale.order'].search([('date_order', '>=', start_date), ('state', 'in', ['sale', 'done'])])
        
        total_sales = sum(s.amount_total for s in sales)
        return {
            'total_sales_last_30_days': total_sales,
            'sales_count_last_30_days': len(sales),
        }