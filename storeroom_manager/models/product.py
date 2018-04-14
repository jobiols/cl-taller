# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import api, models, fields


class ProductProduct(models.Model):
    _inherit = "product.template"

    storeroom_location = fields.Char(
        help="Storeroom location Tower / Shelf"
    )
    warehouse_location = fields.Char(
        help="Warehouse location Tower / Shelf"
    )
    product_brand = fields.Char(
        help="Product Brand"
    )
    product_code = fields.Char(
        help="Product code"
    )
    vehicle_brand = fields.Char(
        help="Vehicle brand"
    )
    vehicle_model = fields.Char(
        help="Vehicle model"
    )

