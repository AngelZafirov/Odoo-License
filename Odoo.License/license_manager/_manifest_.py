{
    'name': 'License Manager',
    'version': '1.0',
    'summary': 'Verwaltung von Software-Lizenzen',
    'sequence': 10,
    'description': """
License Manager Modul
=====================
Dieses Modul verwaltet Lizenzen, prüft ihre Gültigkeit und integriert externe APIs.
    """,
    'author': 'Dein Name oder Firma',
    'website': 'https://www.example.com',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/cron.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
