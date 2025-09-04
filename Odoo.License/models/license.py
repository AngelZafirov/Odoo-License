from odoo import models, fields, api

class License(models.Model):
    _name = 'license.license'
    _description = 'Software License'
    _rec_name = 'license_key'

    license_key = fields.Char(required=True, index=True)
    _sql_constraints = [
        ('license_key_unique', 'unique(license_key)', 'License key must be unique.')
    ]

    partner_id = fields.Many2one('res.partner')
    product_id = fields.Many2one('product.product')
    start_date = fields.Date()
    end_date = fields.Date()
    status = fields.Selection([
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('revoked', 'Revoked')
    ], default='active')


    @api.model
    def cron_expire_license(self):
        today = fields.Date.today()
        expired = self.search([
            ('status', '=', 'active'),
            ('end_date', '<', today)
        ])
        expired.write({'status': 'expired'})
    