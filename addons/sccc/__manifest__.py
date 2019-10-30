# -*- coding: utf-8 -*-
{
    'name': "sccc",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account', 'payment', 'as_time'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/files_views.xml',
        'views/client_views.xml',
        'views/payment_views.xml',
        'views/calendar_views.xml',
        'views/account_move_views.xml',
        'views/account_payment_views.xml',
        'views/config_views/counselor_views.xml',
        'views/config_views/location_views.xml',
        'views/config_views/room_views.xml',
        'views/config_views/language_views.xml',
        'views/config_views/sessions_views.xml',
        'views/config_views/time_slots_views.xml',

        'views/form_views/individual_assessment_views.xml',
        'views/form_views/fam_assessment_views.xml',
        'views/form_views/fee_adjustment_views.xml',
        'views/form_views/fee_setting_views.xml',
        'views/form_views/progress_notes_views.xml'
    ],
    'css': [
        'static/src/css/custom_radio.css'
    ],
    'auto_install' : True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
