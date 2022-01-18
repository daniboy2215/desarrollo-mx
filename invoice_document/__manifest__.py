# -*- coding: utf-8 -*-
# © 2022 Fixdoo, (Daniel Diaz <daniel.diaz@fixdoo.mx>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Invoice Document",

    "summary": """
        Customized invoice printing module""",

    "description": """
        Customized invoice printing module
    """,

    "author": "Fixdoo Create by Daniel Diaz",
    "website": "http://www.fixdoo.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "accounting",
    "version": "14.0.1",

    # any module necessary for this one to work correctly
    "depends": ["base",
                "account",
                ],

    # always loaded
    "data": [
        # "views/account_move_report_data_view.xml",
        # "views/res_company_view.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        # "demo/demo.xml",
    ],
}
