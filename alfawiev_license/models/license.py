from odoo import models, fields, api
import uuid

class SoftwareLicense(models.Model):
    _name = 'license.license'
    _description = 'Software License'

    # Generiere einen eindeutigen Lizenzschlüssel
    name = fields.Char(
        string="License Key",
        default=lambda self: str(uuid.uuid4()),
        readonly=True,
        required=True,
        copy=False
    )

    # Produktbezug
    product_id = fields.Many2one(
        'license.product',
        string="Product",
        required=True,
        ondelete="cascade"
    )

    # Kunde aus res.partner
    customer_id = fields.Many2one(
        'res.partner',
        string="Customer",
        required=True,
        ondelete="cascade"
    )

    # Lizenztyp aus Produkt
    license_type = fields.Selection(
        related='product_id.license_types',
        string="License Type",
        store=True,
        readonly=True
    )

    # Status
    active = fields.Boolean(default=True)

    # Laufzeit
    start_date = fields.Date(
        string="Start Date",
        default=fields.Date.today
    )
    end_date = fields.Date(string="End Date")

    # User-Limit
    max_users = fields.Integer(string="Max. Users", default=1)

    # Gültigkeit berechnen
    is_expired = fields.Boolean(
        string="Expired",
        compute="_compute_is_expired",
        store=True
    )

    @api.depends('end_date', 'active')
    def _compute_is_expired(self):
        today = fields.Date.today()
        for record in self:
            record.is_expired = (
                not record.active
                or (record.end_date and record.end_date < today)
            )
