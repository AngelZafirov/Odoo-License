from odoo import models, fields, api
import uuid
from datetime import datetime, timedelta

class SoftwareLicense(models.Model):
    _name = 'license.license'
    _description = 'Software License'

    name = fields.Char(default=lambda self: str(uuid.uuid4()), readonly=True)
    product_id = fields.Many2one('license.product', required=True)
    customer_id = fields.Many2one('res.partner', required=True)
    license_type = fields.Selection(related='product_id.license_types', store=True)
    active = fields.Boolean(default=True)
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date()
    max_users = fields.Integer(default=1)
