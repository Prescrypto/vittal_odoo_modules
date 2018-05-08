# -*- coding: utf-8 -*-

import odoo
import logging
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from . import _sae as sae
from datetime import datetime
from functools import partial

_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
    _inherit = "account.invoice"
    
    exported = fields.Boolean(readonly=True, default=False, copy=False,
        help="It indicates that the invoice has been export.")
    
    # exportación sae
    def export(self):
        
        # lista de ventas
        orders = self.env['account.invoice'].search([('exported','=',False),('state','in',('open','paid'))])

        # lista de lineas sin facturar
        lines = self.env['account.invoice.line'].search(
            [('invoice_id','in',orders.ids)])

        # datos relevantes de lineas
        line_rows = lines.export_data([
            'invoice_id',
            'create_date',
            'name',
            'price_unit',
            'discount',
            'product_code',
            'id',
        ]).get('datas', [])

        
        # agregar datos de orden a lineas anteriores
        merge = partial(sae.merge_invoice_line, orders)
        rows = map(merge, line_rows)

        # actualizar fecha al e indicar que fueron exportados
        update = {
            #'create_date': fields.Datetime.to_string(datetime.now()),
            'exported': True,
        }
        #orders.write(update)
        #lines.write(update)

        # exportar
        return map(sae.sanitize, rows)

class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    # clave erste derivada de producto
    related_product_code = fields.Char(
        string="Product Code",
        related="product_id.clave_erste",
        readonly=True,
        company_dependent=True)

    product_code = fields.Char(
        "Product Code", compute="_get_product_code", store=True)

    @api.depends("related_product_code")
    def _get_product_code(self):
        for record in self:
            if record.related_product_code:
                record.product_code = record.related_product_code
