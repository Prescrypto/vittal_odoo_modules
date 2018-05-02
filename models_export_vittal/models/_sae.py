# -*- coding: utf-8 -*-

from re import findall, sub
from odoo import fields
import unicodedata


# formatea datos exportados de odoo a sae
def format(name, row):
    # format client data
    if name == 'clients':
        row = format_clients(row)
    elif name == 'products':
        row = format_products(row)
    # limpiar datos
    return sanitize(row)


# formatea datos de productos
def format_products(row):
    # extraer id numerico de string
    row[0] = extract_id(row[0])
    # agregar campos no exportados
    for index in range(2, 18):
        row.insert(index, "")
    # agregar campos no exportados
    for index in range(19, 26):
        row.insert(index, "")
    # agregar clave de esquema
    row.insert(26, "1")
    # agregar campos no exportados
    for index in range(27, 31):
        row.insert(index, "")
    row.insert(32, "A")
    # agregar campos no exportados
    for index in range(33, 37):
        row.insert(index, "")
    # agregar campos no exportados
    for index in range(40, 45):
        row.insert(index, "")
    return row


# formatea datos de cliente
def format_clients(row):
    # variable no mutadas
    street = row[3]
    # agregar estatus
    row.insert(1, "")
    # extraer id numerico de string
    row[0] = extract_id(row[0])
    # extraer nombre de calle
    row[3] = extract_street(row[3])
    # extraer interior de calle y agregar a lista
    row.insert(4, extract_interior(street))
    # agregar clasificación
    row.insert(18, "")
    # agregar campo no exportados
    row.insert(22, "")
    # agregar campo de imprimir
    row.insert(23, "N")
    # agregar campo de correo electronico
    row.insert(24, "S")
    # agregar campo no exportados
    row.insert(25, "")
    for index in range(27, 43):
        row.insert(index, "")
    # agregar campo de tipo de empresa
    row.insert(43, "M")
    for index in range(44, 69):
        row.insert(index, "")
    row.insert(70, "")
    row.insert(71, "")
    for index in range(73, 75):
        row.insert(index, "")
    for index in range(77, 79):
        row.insert(index, "")
    return row


# extraer id numerico
def extract_id(id):
    return id.split('.')[-1].split('_')[-1]


# extraer numero interior de campo calle
def extract_interior(street):
    interior = findall('\d+', street)
    return interior[0] if interior else ""


# extraer nombre de calle de campo de calle
def extract_street(street_with_interior):
    street = sub('(\d+)', "", street_with_interior).lstrip()
    return street if street else ""


# limpiar datos
def sanitize(row):
    # quitar comas para no romper csv
    clean_row = map(
        lambda r: r.replace(",", " ") if isinstance(r, basestring) else r, row)
    # Normaliza los campos, quita acentos y caracteres no soportados
    normalize_row = map(lambda r: unicodedata.normalize("NFKD", u'{}'.format(r) ).encode('ascii', "ignore"), clean_row)
    # regresar renglon corregido, removiendo valores falsos
    return map(lambda r: r if r else "", normalize_row)


# formatear fechas
def date_format(date_string):
    date = fields.Datetime.from_string(date_string)
    return date.strftime('%d/%m/%Y') if date else ""


# llenar campos de linea con orden relevante
def merge_order_line(orders, products, line):
    # obtener orden a la cual pertenece la linea
    order = orders.search([['name', '=', line[0]]], limit=1)
    # obtener producto que pertenece a la linea
    product = products.search([])
    # agregar id externo de usuario
    line.insert(1, order.partner_export_id)
    # formatear fecha
    line[2] = date_format(line[2])
    # agregar descuento financiero
    line.insert(3, "")
    # agregar clave de vendedor
    line.insert(5, 1)
    # agregar su pedido
    line.insert(6, 1)
    # agregar fecha de entrega
    line.insert(7, "")
    # agregar fecha de vencimiento
    line.insert(8, "")
    # agregar descuentos adicionales
    line.insert(11, 0)
    line.insert(12, 0)
    # agregar comision
    line.insert(13, "")
    # agregar clave de esquema de impuestos
    line.insert(14, 1)
    # agregar cantidad
    line.insert(16, 1)
    # agregar ivas
    line.insert(17, 0)
    line.insert(18, 0)
    line.insert(19, 0)
    line.insert(20, 16)
    # agregar nota de orden de venta
    line.insert(21, order.note if order.note else "")
    return line
