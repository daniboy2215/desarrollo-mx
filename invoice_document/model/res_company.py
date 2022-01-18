# -*- coding: utf-8 -*-
# © 2022 Fixdoo Solutions (Daniel Diaz <daniel.diaz@fixdoo.mx>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class res_company(models.Model):
    _inherit = "res.company"

    account_template = fields.Selection([
        #('fency', 'Fency'),
        #('classic', 'Classic'),
        #('modern', 'Modern'),
        ('None', ' '),
        ('odoo_standard', 'Odoo Standard'),
    ], string='Template Invoice')
