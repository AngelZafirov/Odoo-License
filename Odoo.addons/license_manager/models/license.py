from odoo import models, fields, api # type: ignore

class License(models.Model):
    _name = 'license.license'
    _description = 'Software License'
    _rec_name = 'license_key'

    license_key = fields.Char(string="License Key", required=True)

    _sql_constraints = [
        ('license_key_unique', 'unique(license_key)', 'License Key must be unique!')
    ]

    partner_id = fields.Many2one('res.partner')
    product_id = fields.Many2one('product.product')
    start_date = fields.Date()
    end_date = fields.Date()
    recurring = fields.Boolean()
    status = fields.Selection([
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('revoked', 'Revoked')
    ], default='active')

    @api.model
    def cron_expire_licenses(self):
        today = fields.Date.today()
        expired = self.search([
            ('status', '=', 'active'),
            ('end_date', '<', today)
        ])
        expired.write({'status': 'expired'})
