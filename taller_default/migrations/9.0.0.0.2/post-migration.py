# For copyright and license notices, see __manifest__.py file in module root
# Corregir problema de desaparicion del cliente Edenor

from openupgradelib import openupgrade
import logging

_logger = logging.getLogger(__name__)


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    """ Cambia el cliente de las facturas y las lineas de contabilidad por
        edenor.
    """
    ai_obj = env['account.invoice']
    partner_obj = env['res.partner']
    account_move_obj = env['account.move']
    account_move_line_obj = env['account.move.line']

    _logger.info('Migration -> Corregir facturas de Edenor')

    edn = partner_obj.search([('ref', '=', 'edenor')])

    # buscar las facturas
    facturas = ['0006-00000061', '0003-00000003']

    for factura in facturas:
        fa = ai_obj.search([('document_number', '=', factura),
                            ('document_letter_name', '=', 'A'),
                            ('type', '=', 'out_invoice')])
        _logger.info('Migration -> Corrigiendo factura %s' % factura)

        # corregir cliente de la factura
        fa.partner_id = edn.id

        if fa.move_id:
            # corregir cliente en el asiento
            fa.move_id.partner_id = edn.id
            # corregir cliente en las elementos del asiento
            for aml in fa.move_id.line_ids:
                aml.partner_id = edn.id

            # lineas de asiento
            amls = account_move_line_obj.search(
                [('move_id', '=', fa.move_id.id)])

            #            domain = [('document_number', '=', fa.document_number)]
            #            moves = account_move_obj.search(domain)
            for aml in amls:
                aml.partner_id = edn.id
