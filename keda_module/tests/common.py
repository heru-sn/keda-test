# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields
from odoo.tests.common import TransactionCase, HttpCase, tagged, Form

class KedaTestCommon(TransactionCase):

    @classmethod
    def safe_copy(cls, record):
        return record and record.copy()
