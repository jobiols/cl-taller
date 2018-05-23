# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import api, models, fields, _


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
        for order in self:

            stock_picking_obj = self.env['stock.picking']
            pick = stock_picking_obj.create({
                'partner_id': 6,
                'priority': '1',
                'picking_type_id': 7,
                'location_id': 29,
                'move_type': 'one',
                'min_date': '2018-01-01',
                'origin': u'PAÑOL',
                'location_dest_id': 26,
                'note': ''
            })

            for order_line in order.order_lines:
                pick.move_lines.create({
                    'picking_id': pick.id,
                    'product_id': order_line.product_id.id,
                    'product_uom_qty': order_line.qty,
                    'product_uom': 1,
                    'location_id': 29,
                    'name': 'nombre del producto',
                    'location_dest_id': 26,
                    'picking_type_id': 7,
                })

            self.do_transfer(pick)
            order.state = 'sent'

    @api.multi
    def reverse_order(self):
        for order in self:
            order.state = 'draft'

    @api.multi
    @api.depends('informe_nro', 'unidad')
    def _get_name(self):
        for rec in self:
            rec.name = u'Orden de entrega {} {}'.format(
                    rec.informe_nro, rec.unidad)

    @api.multi
    def do_transfer(self, pick):

        pick.action_confirm()   # marcar por realizar
        pick.force_assign()     # forzar disponibilidad

        # poner las cantidades a mover
        for pack in pick.pack_operation_product_ids:
            pack.qty_done = pack.product_qty

        pick.do_new_transfer()  # validar

        return True


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
            domain=[('replacement', '=', True)],
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
