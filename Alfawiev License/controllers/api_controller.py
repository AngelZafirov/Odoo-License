from odoo import http
from odoo.http import request

class LicenseAPI(http.Controller):

    @http.route('/license/validate', type='json', auth='none', methods=['POST'])
    def validate(self, **kwargs):
        key = kwargs.get('key')
        license = request.env['license.license'].sudo().search([('name','=',key)], limit=1)
        if not license or not license.active:
            return {'status': 'invalid'}
        return {'status': 'valid', 'product': license.product_id.name}
