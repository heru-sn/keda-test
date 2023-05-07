# # -*- coding: utf-8 -*-

import werkzeug.wrappers
import json

from odoo import http
from odoo.http import request

def valid_response(data, status=200):
    """Valid Response
    This will be return when the http request was successfully processed."""
    data = {"count": len(data), "data": data}
    return werkzeug.wrappers.Response(
        status=status,
        content_type="application/json; charset=utf-8",
        response=json.dumps(data),
    )

def invalid_response(typ, message=None, status=401):
    """Invalid Response
    This will be the return value whenever the server runs into an error
    either from the client or the server."""
    # return json.dumps({})
    return werkzeug.wrappers.Response(
        status=status,
        content_type="application/json; charset=utf-8",
        response=json.dumps(
            {
                "type": typ,
                "message": str(message)
                if str(message)
                else "wrong arguments (missing validation)",
            }
        ),
    )

class KedaRestApi(http.Controller):
    @http.route('/api/material/getmateriallist', auth='public', type="http", csrf=False, methods=['GET'])
    def get_material_list(self, **kwargs):
        result = {}
        data_material = request.env['master.material'].sudo().search([])
        list_cot = []

        try:
            for x in data_material:
                cot_list = {
                    'name': x.name,
                    'code': x.code,
                    'type_material': x.type_material,
                    'buy_price': x.buy_price,
                    'partner_id': x.partner_id.id,
                }
                list_cot.append(cot_list)

            result['result'] = list_cot
            result['code'] = 200
            result['message'] = "success"
            return valid_response(result)
        
        except Exception as e:
            return invalid_response("exception", e, 503)
                        