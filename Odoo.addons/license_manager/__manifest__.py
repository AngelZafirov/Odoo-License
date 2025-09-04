{
    'name': 'License Manager',
    'version': '1.0',
    'summary': 'Verwaltung und API für Software-Lizenzen',
    'author': 'Dein Name',
    'license': 'LGPL-3',   
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/cron.xml',
    ],
    'installable': True,
    'application': True,
}
