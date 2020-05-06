# For copyright and license notices, see __manifest__.py file in module root

from openerp import models, api


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def action_cancel(self):
        """ Esto es un fix porque con lo que habia no podia cancelar facturas.

            busca con un filtered que el invoice tenga un pay_now_journal_id
            para despues ponerlo en False. Asi que le pongo cualquiera y luego
            se da el gusto de borrarlo.
        """
        aj_obj = self.env['account.journal']
        self.pay_now_journal_id = aj_obj.search([], limit=1)
        return super(AccountInvoice, self).action_cancel()
