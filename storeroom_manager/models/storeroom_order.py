# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import api, models, fields


class StoreroomOrder(models.Model):
    _name = "storeroom_manager.storeroom.order"
    _description = 'Storeroom delivery orders'
    _order = 'fecha_inicio desc, id desc'
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    name = fields.Char(
        compute="_get_name",
    )

    order_lines = fields.One2many(
        'storeroom_manager.order.line',
        'order_id',
        string='Order Lines',
    )

    informe_nro = fields.Char(

    )

    unidad = fields.Char(

    )

    patente = fields.Char(

    )

    fecha_inicio = fields.Date(

    )

    km_entrada = fields.Char(

    )

    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Delivered')],
        string='Status',
        readonly=True,
        copy=False,
        track_visibility='onchange',
        default='draft')

    @api.multi
    def transfer_order(self):
        self.do_transfer_order()

    @api.multi
    def reverse_order(self):
        self.do_reverse_order()

    @api.multi
    @api.depends('informe_nro', 'unidad')
    def _get_name(self):
        for rec in self:
            rec.name = u'Orden de entrega {} {}'.format(
                rec.informe_nro, rec.unidad)

    @api.multi
    def do_transfer_order(self):
        for order in self:
            order.state = 'sent'
            for line in order.order_lines:
                print line.name


    @api.multi
    def do_reverse_order(self):
        for order in self:
            order.state = 'draft'


class StoreroomOrderLine(models.Model):
    _name = 'storeroom_manager.order.line'
    _description = 'Storeroom Order Line'
    _order = 'order_id desc, sequence, id'

    name = fields.Char(
        default="Orden"
    )

    order_id = fields.Many2one(
        'storeroom_manager.storeroom.order',
        string='Order Reference',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False
    )

    product_id = fields.Many2one(
        'product.product',
        string='Product',
        change_default=True,
        ondelete='restrict',
        required=True)

    qty = fields.Integer(
        string='Quantity',
        required=True,
        default=1
    )

    sequence = fields.Integer(
        string='Sequence',
        default=10
    )

    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Delivered')],
        string='Status',
        readonly=True,
        copy=False,
        track_visibility='onchange',
        default='draft')
