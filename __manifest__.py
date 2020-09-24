# -*- coding: utf-8 -*-
{
    'name': 'Portal project',
    'version': '1.0',
    'sequence': 6,
    'author': 'sonod',
    'summary': "Portal project" ,
    'description': "Portal project",
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/views.xml',
    ],
    'installable': True,
    'application': False,
}
