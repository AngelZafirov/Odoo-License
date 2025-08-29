{
    'name': 'License Manager',
    'version': '1.0',
    'summary': 'Verwaltung und API für Software-Lizenzen',
    'author': 'Dein Name',
    'depends': ['base', 'product'],
    'data': ['data/cron.xml'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'test': ['tests/test_license.py']
}