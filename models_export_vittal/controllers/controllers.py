# -*- coding: utf-8 -*-
from odoo import http

# class CamposClientesVittal(http.Controller):
#     @http.route('/campos_clientes_vittal/campos_clientes_vittal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/campos_clientes_vittal/campos_clientes_vittal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('campos_clientes_vittal.listing', {
#             'root': '/campos_clientes_vittal/campos_clientes_vittal',
#             'objects': http.request.env['campos_clientes_vittal.campos_clientes_vittal'].search([]),
#         })

#     @http.route('/campos_clientes_vittal/campos_clientes_vittal/objects/<model("campos_clientes_vittal.campos_clientes_vittal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('campos_clientes_vittal.object', {
#             'object': obj
#         })