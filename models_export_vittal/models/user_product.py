# -*- coding: utf-8 -*-

import odoo
import _sae as sae
from functools import partial
from odoo import models, fields, api


class user_product(models.Model):
    _inherit = "product.template"

    # exportación sae
    export_columns = [
        "id",
        "description_sale",
        "tipo_elemento",
        "cuenta_contable",
        "codigo_sat",
        "clave_unidad",
        "clave_erste",
    ]

    def export(self):
        columns = self.export_columns
        format_products = partial(sae.format, "products")
        return map(format_products, self.export_data(columns).get("datas", []))

    def export_all(self):
        all_products = self.env['product.template']
        valid_products = all_products.search([])

        columns = self.export_columns
        format_products = partial(sae.format, "products")

        return map(format_products, valid_products.export_data(columns).get('datas', []))
