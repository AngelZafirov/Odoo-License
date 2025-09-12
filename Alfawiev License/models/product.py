from odoo import models, fields

class LicenseProduct(models.Model):
    _name = 'license.product'
    _description = 'Software Product'

    name = fields.Char(required=True)
    version = fields.Char()
    features = fields.Text()
    license_types = fields.Selection([
        ('standard','Standard'),
        ('professional','Professional'),
        ('enterprise','Enterprise'),
    ], default='standard')
