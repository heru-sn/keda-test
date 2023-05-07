# -*- coding: utf-8 -*-
from unittest.mock import patch
from odoo.addons.keda_module.tests.common import KedaTestCommon

from odoo.tests import tagged

@tagged('post_install', '-at_install')
class TestKedaModule(KedaTestCommon):
    def test_create_master_material(self):
        test_material = self.env['master.material'].create({
            'code': 'MM-0001',
            'name': 'Material Cotton-0001',
            'type_material': 'cotton',
            'buy_price': 9000,
        })

        self.assertEqual(test_material.name, 'Material Cotton-0001')
        print('Your test was succesfull!')