# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
#    Copyright (C) 2016  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------
{
    'name': 'Storeroom Manager',
    'version': '9.0.1.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Warehouse Management',
    'summary': 'Manejo del pañol',
    'author': 'jeo Software',
    'depends': [
        'product',
        'purchase'
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/storeroom_view.xml',
        'views/miscelaneous_view.xml',
        'report/order_report.xml'
    ],
    'demo': [
        'demo/demo_data.xml',
    ],

    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],
}
