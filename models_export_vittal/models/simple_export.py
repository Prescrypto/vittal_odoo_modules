# -*- coding: utf-8 -*-

import csv
import io


def get_field(obj, field):
    if field is None:
        return ''
    elif "const:" in field:
        return field.replace('const:', '').replace('"', '')
    else:
        value = None
        for n in field.split('.'):
            if value is None:
                value = getattr(obj, n)
            else:
                value = getattr(value, n)
        return value if value else ''


def get_row(obj):
    em = obj.export_map
    row = []
    for v in em:
        row.append(get_field(obj, v))
    return row


def get_data(objects):
    if not objects or len(objects) < 1:
        return []
    values = []
    for o in objects:
        values.append(get_row(o))
    return values


def gen_csv(objects, header=True):
    output = io.BytesIO()
    writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL)
    if header:
        writer.writerow(objects.header_map)
    values = get_data(objects)
    for v in values:
        writer.writerow(v)
    return output.getvalue()