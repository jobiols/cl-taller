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
    vehicle_brand = fields.Many2many(
        'storeroom_manager.vehicle.brand',
        ondelete='cascade',
        help="Vehicle brand",
        required=True
    )
    vehicle_model = fields.Many2one(
        'storeroom_manager.vehicle.model',
        ondelete='cascade',
        help="Vehicle model",
        required=True
    )
    product_brand = fields.Many2one(
        'storeroom_manager.product.brand',
        ondelete='cascade',
        help="Product Brand",
        required=True
    )

    type = fields.Selection(
        default='product'
    )

    replacement = fields.Boolean(
        default='False'
    )
