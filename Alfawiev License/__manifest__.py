{
    'name': 'alfaview_license',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'License management for software products',
    'depends': ['base', 'contacts', 'sale'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/license_views.xml',
        'views/customer_views.xml',
        'wizards/license_wizard.xml',
    ],
    'installable': True,
    'application': True,
}

