{
    'name': 'Test',
    'version': '1.0',
    'category': 'Test',
    'sequence': 15,
    'summary': 'Test Module',
    'website': 'trescloud.com',
    'depends': [
        'sale_management',
        'account',
        'stock'
    ],
    'data': [
        # data
        # security
        'security/ir.model.access.csv',
        'security/delivery_detail_security.xml',
        # reports
        'reports/report_invoice_templates.xml',
        # wizard
        # views
        'views/account_move_views.xml',
        'views/delivery_detail_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
