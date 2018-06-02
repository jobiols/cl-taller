# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import models, fields


class VehicleBrand(models.Model):
    _name = "storeroom_manager.vehicle.brand"
    _description = 'Miscelaneous table Vehicle Brand'

    name = fields.Char(

    )

    _sql_constraints = [
        ('uniq_vehicle_brand', 'unique(name)',
         "This vehicle brand already exists, it must be unique !"),
    ]
