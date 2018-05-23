# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import api, models, fields, _
from openerp.exceptions import except_orm
from openerp.exceptions import UserError


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
        import wdb;            wdb.set_trace()

        # forzar para que funcione aunque no haya stock
        if not pick.force_assign():
            raise except_orm(
                    _('Can not assign product for transfer. Unknown error'))

        if not pick.move_lines and not pick.pack_operation_ids:
            raise UserError(_(
                'Please create some Initial Demand or Mark as Todo and create some Operations. '))

        # In draft or with no pack operations edited yet, ask if we can just do everything
        if pick.state == 'draft' or all(
                [x.qty_done == 0.0 for x in pick.pack_operation_ids]):
            # If no lots when needed, raise error
            picking_type = pick.picking_type_id
            if (
                picking_type.use_create_lots or picking_type.use_existing_lots):
                for pack in pick.pack_operation_ids:
                    if pack.product_id and pack.product_id.tracking != 'none':
                        raise UserError(_(
                            'Some products require lots, so you need to specify those first!'))

        # If still in draft => confirm and assign
        if pick.state == 'draft':
            pick.action_confirm()
            if pick.state != 'assigned':
                pick.action_assign()
                if pick.state != 'assigned':
                    raise UserError(_(
                        "Could not reserve all requested products. Please use the \'Mark as Todo\' button to handle the reservation manually."))

        for pack in pick.pack_operation_ids:
            if pack.product_qty > 0:
                pack.write({'qty_done': pack.product_qty})
            else:
                pack.unlink()
        pick.do_transfer()

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
