from odoo.tests.common import TransactionCase
from datetime import date, timedelta

class TestLicenseManager(TransactionCase):

    def setUp(self):
        super().setUp()
        self.License = self.env['license.license']
        self.partner = self.env['res.partner'].create({'name': 'Test Partner'})
        self.product = self.env['product.product'].create({'name': 'Test Product'})

    def test_license_creation_and_unique_constraint(self):
        license = self.License.create({
            'license_key': 'TEST-1234',
            'partner_id': self.partner.id,
            'product_id': self.product.id,
            'status': 'active',
            'start_date': date.today(),
            'end_date': date.today() + timedelta(days=1)
        })
        self.assertEqual(license.license_key, 'TEST-1234')

        with self.assertRaises(Exception):
            self.License.create({'license_key': 'TEST-1234'})

    def test_cron_expire_licenses(self):
        expired_license = self.License.create({
            'license_key': 'EXPIRED-1',
            'status': 'active',
            'end_date': date.today() - timedelta(days=1)
        })
        self.License.cron_expire_licenses()
        expired_license.refresh()
        self.assertEqual(expired_license.status, 'expired')

    def test_api_validate_license(self):
        license = self.License.create({
            'license_key': 'API-1234',
            'status': 'active'
        })
        controller = self.env['ir.http'].sudo()._get_controller_class('license_manager.controllers.license_api.LicenseAPI')()
        result = controller.validate_license('API-1234')
        self.assertTrue(result['valid'])

        result_invalid = controller.validate_license('INVALID-KEY')
        self.assertFalse(result_invalid['valid'])
        self.assertEqual(result_invalid['reason'], 'not_found')
