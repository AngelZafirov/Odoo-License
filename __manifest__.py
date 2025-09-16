{
    'name': 'Alfaview License',
    'version': '1.0',
    'summary': 'License management for software products',
    'description': """
        Manage software licenses linked to products and customers.
        - Create license products
        - Assign licenses to customers
        - Track validity and expiration
    """,
    'author': 'Dein Name / Deine Firma',
    'website': 'https://deine-website.com',
    'category': 'Sales',
    'license': 'OPL-1',     # wichtig: zeigt es als Third-party App
    'price': 100.0,         # Preis
    'currency': 'EUR',      # Währung
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
    'auto_install': False,
}
