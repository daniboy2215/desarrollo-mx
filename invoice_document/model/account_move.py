# -*- coding: utf-8 -*-
# © 2022 Fixdoo Solutions (Daniel Diaz <daniel.diaz@fixdoo.mx>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class account_invoice(models.Model):
    _inherit = "account.move"

    paypal_chk = fields.Boolean("Paypal")
    paypal_id = fields.Char("Paypal Id")

    def invoice_print(self):
        """ Print the invoice and mark it as sent, so that we can see more
            easily the next step of the workflow
        """
        self.ensure_one()
        self.sent = True
        return self.env.ref('invoice_document.%s' % self.env.company.account_template).report_action(self)
