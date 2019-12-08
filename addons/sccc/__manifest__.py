# -*- coding: utf-8 -*-
{
    'name': "SCCC",

    'summary': """
        Southern California Counseling Center
        """,

    'description': """
        SCCC provides comprehensive counseling services at rates based on your ability to pay. 
        We believe everyone should get the care they need, at rates they can afford, 
        for as long as they need counseling.
    """,

    'author': "SCCC",
    'website': "https://sccc-la.org/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account', 'payment', 'backend_theme_v13', 'mass_mailing'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'data/meeting_status_seed.xml',
        'data/appointment_type_seed.xml',

        'views/assets.xml',
        'views/menu_views.xml',
        'views/files_views.xml',
        'views/client_views.xml',
        'views/calendar_views.xml',
        'views/account_move_views.xml',
        'views/account_payment_views.xml',
        'views/square_payments_views.xml',
        'views/config_views/provider_views.xml',
        'views/config_views/location_views.xml',
        'views/config_views/room_views.xml',
        'views/config_views/language_views.xml',
        'views/config_views/sessions_views.xml',
        'views/config_views/time_slots_views.xml',

        'views/form_views/individual_assessment_views.xml',
        'views/form_views/fam_assessment_views.xml',
        'views/form_views/fee_adjustment_views.xml',
        'views/form_views/fee_setting_views.xml',
        'views/form_views/tapp_intake_views.xml',
        'views/form_views/progress_notes_views.xml'
    ],
    'auto_install' : True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
