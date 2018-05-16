# -*- coding: utf-8 -*-
{
    'name': "Exportar Catalogos layout SAE",

    'summary': """Exportar Catalogos compatibles SAE.""",

    'description': """
        Exporta en csv Catalogos de Contactos y Facturas,
        compatibles para importar en SAE.
    """,

    'author': "Prescrypto",
    'website': "http://www.prescrypto.com",

    'category': 'Specific Industry Applications',
    'version': '10.0.1',

    'depends': [
        'base','campos_clientes_vittal','account',
    ],

    # always loaded
    'data': [
        'views/sale_order_filter.xml',
        'views/static_assets.xml',
    ],
    
    # scripts
    'js': [
        'static/src/js/export.js'
    ],
    # templates
    'qweb': [
        'static/src/xml/export_button.xml',
        'static/src/xml/export_all_button.xml',
    ],
    
    # a module
    'application': False,
}
