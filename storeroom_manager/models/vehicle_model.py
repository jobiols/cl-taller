# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import models, fields


class VehicleModel(models.Model):
    _name = "storeroom_manager.vehicle.model"
    _description = 'Miscelaneous table Vehicle Model'

    name = fields.Char(

    )

    _sql_constraints = [
        ('uniq_vehicle_model', 'unique(name)',
         "This vehicle model already exists, it must be unique !"),
    ]
