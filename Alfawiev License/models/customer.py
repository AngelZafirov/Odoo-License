from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    license_ids = fields.One2many('license.license', 'customer_id', string="Licenses")
