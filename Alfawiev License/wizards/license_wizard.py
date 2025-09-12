from odoo import models, fields
from datetime import timedelta

class LicenseRenewWizard(models.TransientModel):
    _name = 'license.renew.wizard'
    _description = 'Renew License Wizard'

    license_id = fields.Many2one('license.license', required=True)
    extra_days = fields.Integer(default=365)

    def renew_license(self):
        if self.license_id.end_date:
            self.license_id.end_date += timedelta(days=self.extra_days)
        else:
            self.license_id.end_date = fields.Date.today() + timedelta(days=self.extra_days)
