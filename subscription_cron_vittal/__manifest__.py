# -*- coding: utf-8 -*-
{
    'name': "Subscriptions (Cron Jobs)",

    'summary': """Subscription (Cron Jobs).""",

    'description': """
        Implementacion de Subscripciones
    """,

    'author': "Prescrypto",
    'website': "http://www.prescrypto.com",

    'category': 'Specific Industry Applications',
    'version': '10.0.1',

    'depends': [
        'base','sale','campos_clientes_vittal',
    ],

    # always loaded
    'data': [
        'data/cron_subscription.xml',
        'data/cron_renew_next_subscription.xml',
        'data/cron_user_member.xml',
        'views/sale_order_form.xml',
        'views/subscription_tree.xml',
        'views/subscription_action.xml',
        'views/subscription_filter.xml',
        'views/sales_menu.xml',
    ],
    
    # a module
    'application': False,
}
