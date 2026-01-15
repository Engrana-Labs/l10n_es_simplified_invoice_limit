# -*- coding: utf-8 -*-
{
    'name': "Límite factura simplificada (ES) - Engrana Labs",

    'summary': "Módulo para establecer un límite personalizado en las facturas simplificadas en España",

    'description': """
Permite definir un límite personalizado para las facturas simplificadas en España, adaptándose a las necesidades específicas de cada empresa.
    """,

    'author': "Javier González Álvarez | Engrana Labs | javier@engranalabs.com",
    'website': "https://www.engranalabs.com",
    'support': 'info@engranalabs.com',
    'license': 'AGPL-3',
    'category': 'Accounting',
    'version': "18.0.1.0.0",
    'depends': ['base', 'l10n_es', 'account'],
    'data': [
        'views/spain_location_settings.xml',
    ],
    'images': ['static/description/banner.png']
}

