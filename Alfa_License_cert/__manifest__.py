{
    'name': 'Alfaview License Certificate',
    'version': '1.0',
    'summary': 'Lizenzprüfung per Zertifikat (.lic Datei)',
    'description': """
        Modul zur Überprüfung von Software-Lizenzen anhand einer Zertifikatsdatei (.lic).
        - Upload von Lizenzdateien
        - Signaturprüfung mit Public Key
        - Ablauf- und Kundenprüfung
    """,
    'author': 'Deine Firma',
    'website': 'https://deine-website.com',
    'category': 'Tools',
    'license': 'OPL-1',
    'depends': ['base', 'alfawiev_license_order'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/license_certificate_views.xml',
    ],
    'installable': True,
    'application': True,
}
