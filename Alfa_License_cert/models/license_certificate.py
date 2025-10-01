from odoo import models, fields, api, _
import json, base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from datetime import date

class LicenseCertificate(models.Model):
    _name = "license.certificate"
    _description = "Software License Certificate"

    name = fields.Char("License Name")
    file = fields.Binary("License File (.lic)")
    valid = fields.Boolean("Valid", compute="_compute_valid", store=False)
    reason = fields.Char("Validation Reason", compute="_compute_valid", store=False)

    @api.depends("file")
    def _compute_valid(self):
        for rec in self:
            rec.valid = False
            rec.reason = _("No license file uploaded")
            if not rec.file:
                continue

            try:
                data = base64.b64decode(rec.file).decode()
                lic = json.loads(data)

                payload = lic.get("payload")
                signature_b64 = lic.get("signature")
                if not payload or not signature_b64:
                    rec.reason = _("Invalid license format")
                    continue

                # Public Key laden (aus Systemparameter)
                pub_pem = self.env["ir.config_parameter"].sudo().get_param("license.public_key_pem")
                if not pub_pem:
                    rec.reason = _("No public key configured")
                    continue
                public_key = serialization.load_pem_public_key(pub_pem.encode())

                # Payload canonical serialisieren
                payload_bytes = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
                signature = base64.b64decode(signature_b64)

                # Signatur prüfen
                public_key.verify(
                    signature,
                    payload_bytes,
                    padding.PSS(
                        mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.MAX_LENGTH,
                    ),
                    hashes.SHA256(),
                )

                # Ablauf prüfen
                today = date.today()
                if payload.get("end_date") and payload["end_date"] < str(today):
                    rec.reason = _("License expired")
                    continue

                rec.valid = True
                rec.reason = _("License valid")

            except Exception as e:
                rec.valid = False
                rec.reason = _("Verification failed: %s") % str(e)
