# -*- coding: utf-8 -*-

import odoo
import logging
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
import _sae as sae
from datetime import datetime
from functools import partial

_logger = logging.getLogger(__name__)


class user_sales_order(models.Model):
    _inherit = "sale.order"

    # exportación sae
    def export(self):
        # lista de ventas
        orders = self.env['sale.order'].search([])

        # lista de productos
        products = self.env['product.template'].search([])

        # lista de lineas sin facturar
        lines = self.env['sale.order.line'].search(
            [['invoice_status', '=', 'to invoice'], ['state', '=', 'sale']])

        # datos relevantes de lineas
        line_rows = lines.export_data([
            'order_id',
            'create_date',
            'name',
            'price_unit',
            'discount',
            'product_code',
        ]).get('datas', [])

        # agregar datos de orden a lineas anteriores
        merge = partial(sae.merge_order_line, orders, products)
        rows = map(merge, line_rows)

        # actualizar fecha al e indicar que fueron exportados
        update = {
            'create_date': fields.Datetime.to_string(datetime.now()),
            'invoice_status': 'invoiced'
        }
        orders.write(update)
        lines.write(update)

        # exportar
        format_orders = partial(sae.format, "orders")
        return map(format_orders, rows)
