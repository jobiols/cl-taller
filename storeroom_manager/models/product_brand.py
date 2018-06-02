# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import models, fields


class ProductBrand(models.Model):
    _name = "storeroom_manager.product.brand"
    _description = 'Miscelaneous table Product Brands'

    name = fields.Char(

    )

    _sql_constraints = [
        ('uniq_product_brand', 'unique(name)',
         "This product brand alerady exists, it must be unique !"),
    ]
