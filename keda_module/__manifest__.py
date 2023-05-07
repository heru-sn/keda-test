# -*- coding: utf-8 -*-
# Copyright 2023 PT Citra Kreasi Teknologi Indonesia
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
# noinspection PyUnresolvedReferences,SpellCheckingInspection
{
    "name": """keDA - Tech Solution""",
    "summary": """Custom Module""",
    "category": "",
    "version": "0.1.1",
    "development_status": "Alpha",  # Options: Alpha|Beta|Production/Stable|Mature
    "auto_install": False,
    "installable": True,
    "application": False,
    "author": "PT Citra Kreasi Teknologi Indonesia",
    "support": "admin@keda-tech.com",
    "website": "https://keda-tech.com",
    "license": "OPL-1",
    "images": [
        'images/main_screenshot.png'
    ],

    # "price": 10.00,
    # "currency": "USD",

    "depends": [
        # odoo addons
        'base',
        'purchase',
        'sale',
        # third party addons

        # developed addons

    ],
    "data": [
        # group
        # 'security/res_groups.xml',

        # data

        # global action
        # 'views/action/action.xml',

        # wizard

        # view
        'views/common/master_material.xml',

        # report paperformat

        # report template
        # 'views/report/report_template_model_name.xml',

        # report action
        # 'views/action/action_report.xml',

        # assets
        # 'views/assets.xml',

        # onboarding action
        # 'views/action/action_onboarding.xml',

        # action menu
        # 'views/action/action_menu.xml',

        # action onboarding
        # 'views/action/action_onboarding.xml',

        # menu
        'views/menu.xml',

        # security
        'security/ir.model.access.csv',    

        # data
    ],
    "demo": [
        # 'demo/demo.xml',
    ],
    "qweb": [
        # "static/src/xml/{QWEBFILE1}.xml",
    ],

    "post_load": None,
    # "pre_init_hook": "pre_init_hook",
    # "post_init_hook": "post_init_hook",
    "uninstall_hook": None,

    "external_dependencies": {"python": [], "bin": []},
    # "live_test_url": "",
    # "demo_title": "{MODULE_NAME}",
    # "demo_addons": [
    # ],
    # "demo_addons_hidden": [
    # ],
    # "demo_url": "DEMO-URL",
    # "demo_summary": "{SHORT_DESCRIPTION_OF_THE_MODULE}",
    # "demo_images": [
    #    "images/MAIN_IMAGE",
    # ]
}
