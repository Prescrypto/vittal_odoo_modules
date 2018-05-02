# -*- coding: utf-8 -*-
import _sae as sae
from functools import partial
from odoo import models, fields, api, _


class user_client(models.Model):
    _inherit = "res.partner"

    # exportación sae
    export_columns = [
        'client_export_id',
        'name',
        'rfc',
        'street',
        'street2',
        'cross_street',
        'crosses_with',
        'sat_colonia_id',
        'zip',
        'poblacion',
        'sat_municipio_id',
        'sat_estado_id',
        'sat_pais_id',
        'nacionalidad',
        'reference_id',
        'phone',
        'fax',
        'website',
        'curp',
        'invoice_email',
        'sat_uso_codigo',
        'sat_pagos_codigo',
        'zone',
    ]
    @api.multi
    def export(self):
        columns = self.export_columns
        format_clients = partial(sae.format, 'clients')
        return map(format_clients, self.export_data(columns).get('datas', []))

    def export_all(self):
        all_clients = self.env['res.partner']
        valid_clients = all_clients.search([['active', '=', True], ['customer', '=', True], ['parent_id', '=', False]])

        columns = self.export_columns
        format_clients = partial(sae.format, 'clients')

        return map(format_clients, valid_clients.export_data(columns).get('datas', []))

