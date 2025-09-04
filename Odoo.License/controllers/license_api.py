from odoo import http
from odoo.http import request

class LicenseAPI(http.Controller):
    @http.route('/api/license/validate', type='json', auth='user')
    def validate_license(self, license_key):
        license = request.env['license.license'].sudo().search([('license_key', '=', license_key)], limit=1)
        if not license:
            return {'valid': False, 'reason': 'not_found'}

        if license.status != 'active':
            return {'valid': False, 'reason': 'license.status'}

        return {
            'valid': True,
            'customer': license.partner_id.Name,
            'product': license.product_id.Name,
            'expires': str(license.end_date)
        }