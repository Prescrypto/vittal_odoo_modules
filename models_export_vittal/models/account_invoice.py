# -*- coding: utf-8 -*-

import simple_export as se
from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = "account.invoice"
    
    exported = fields.Boolean(readonly=True, default=False, copy=False,
        help="It indicates that the invoice has been export.")
    
    # exportación sae
    def export(self):
        orders = self.env['account.invoice'].search(
            [('exported', '=', False), ('state', 'in', ('open', 'paid'))]
        )
        export_lines = ""
        for o in orders:
            export_lines = export_lines + se.gen_csv(o.invoice_line_ids, header=False)
        header = se.gen_csv(self.env['account.invoice.line'])
        orders.write({'exported': True})
        self.env.cr.commit()
        return header + export_lines


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    product_id = fields.Many2one('product.product', required=True)

    export_map = [
        'id',
        'invoice_id.partner_id.group_code',
        'invoice_id.date_invoice',
        None,
        None,
        None,
        None,
        'invoice_id.comment',
        'invoice_id.user_id.id',
        'invoice_id.id',
        None,
        'invoice_id.date_due',
        'price_unit',
        'const:0',
        'const:0',
        'const:0',
        'const:0',
        None,
        'product_id.clave_sat',
        'quantity',
        None,
        None,
        None,
        'const:16',
        None,
        'name',
        'invoice_id.sat_metodo_pago',
        'invoice_id.sat_pagos_id.codigo_forma',
        'invoice_id.sat_uso_id.codigo_uso'
    ]

    header_map = [
        'Clave',
        'Cliente',
        'Fecha de elaboración',
        'Descuento financiero',
        'Numero de almacen cabecera',
        'Numero de Moneda',
        'Tipo de Cambio',
        'Observaciones',
        'Clave de vendedor',
        'Su pedido',
        'Fecha de entrega',
        'Fecha de vencimiento',
        'Precio',
        'Desc. 1',
        'Desc. 2',
        'Desc. 3',
        'Comisión',
        'Clave de esquema de impuestos',
        'Clave del artículo',
        'Cantidad',
        'I.E.P.S.',
        'Ret. ISR',
        'Ret. IVA',
        'I.V.A.',
        'Numero de almacen Partidas',
        'Observaciones de partida',
        'Metodo de Pago',
        'Forma de Pago Sat',
        'Uso CFDI'
    ]