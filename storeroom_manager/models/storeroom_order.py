# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import api, models, fields


class StoreroomOrder(models.Model):
    _name = "storeroom.order"
    _description = 'Storeroom delivery orders'

    informe_nro = fields.Char(

    )

    unidad = fields.Char(

    )

    patente = fields.Char(

    )

    fecha_inicio = fields.Date(

    )

    km_entrada = fields.Integer(

    )
