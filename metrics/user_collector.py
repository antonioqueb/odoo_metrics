# metrics/user_collector.py
from odoo import http
import json

def collect_user_data():
    """
    Collects data for active users.
    """
    active_users = http.request.env['res.users'].search([('active', '=', True)])
    user_data = []

    for user in active_users:
        try:
            if http.request.env.modules.get('mail'):
                last_activity = user.sudo().last_activity_date
            else:
                last_activity = None
        except (AttributeError, ModuleNotFoundError):
            last_activity = None
            print(f"Error accessing last_activity for user {user.name}. Mail module might be missing.")

        user_info = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'last_activity': last_activity,
            'company_name': user.company_id.name if user.company_id else None,
            'group_names': [group.name for group in user.groups_id],
            'can_access_frontend': user.has_group('base.group_user'),
            'lang': user.lang,
            'preferred_language': user.lang,
            'is_admin': user.has_group('base.group_system'),
            'active': user.active,
            'phone': user.phone,
            'mobile': user.mobile,
            'address': user.address_id.name if user.address_id else None,
            'department': user.department_id.name if user.department_id else None,
            'job_title': user.job_title,
            'signature': user.signature,
        }
        user_data.append(user_info)
    return user_data