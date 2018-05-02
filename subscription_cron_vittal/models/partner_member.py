# -*- coding: utf-8 -*-

import odoo
import logging
from datetime import date, datetime
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class FamilyMember(models.Model):
    _inherit = "family.member"

    # comenzar suscripción
    @api.multi
    def start_reg(self):
        for record in self:
            record.start_date = fields.Datetime.to_string(datetime.now())
            record.end_date = ""
            record.user_active = True

    # terminar suscripción
    @api.multi
    def end_reg(self):
        for record in self:
            record.end_date = fields.Datetime.to_string(datetime.now())
            record.auto_end_date = ""
            record.user_active = False


class CompanyMember(models.Model):
    _inherit = "company.member"

    # comenzar suscripción
    @api.multi
    def start_reg(self):
        for record in self:
            record.start_date = fields.Datetime.to_string(datetime.now())
            record.end_date = ""
            record.user_active = True

    # terminar suscripción
    @api.multi
    def end_reg(self):
        for record in self:
            record.end_date = fields.Datetime.to_string(datetime.now())
            record.auto_end_date = ""
            record.user_active = False
