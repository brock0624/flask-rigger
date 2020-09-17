# -*- coding: utf-8 -*-
from flask_restplus import Namespace, Resource, fields

# from app.models import Codes
# from app.code import custom_abord, generate_response, ResponseCode
# from app.utils.common import query_to_dict

# 定义命名空间
ns = Namespace('codes', description='Codes related operations')

code = ns.model('Code', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'code': fields.String(required=True, description='The code name'),
    'code_value': fields.String(required=True, description='The code value'),
    'type': fields.String(required=True, description='The code value'),
    'version': fields.Integer(required=True, description='The code value'),
    'active': fields.String(required=True, description='The code value'),
})

CODES = [
    {'id': 1, 'code': 'code1', 'code_value': 'value1', 'type': 'type1', 'version': 1},
    {'id': 2, 'code': 'code2', 'code_value': 'value2', 'type': 'type2', 'version': 1},
]


@ns.route('/')
class COdeList(Resource):
    @ns.doc('list_codes')
    @ns.marshal_list_with(code)
    def get(self):
        '''List all codes'''
        return CODES


@ns.route('/<int:id>')
@ns.param('id', 'The code identifier')
# @ns.response(404, 'Code not found')
class Code(Resource):
    @ns.doc('get_code')
    @ns.marshal_with(code)
    def get(self, id):
        '''获取单个code项，并允许删除操作'''
        for code in CODES:
            if code['id'] == id:
                return code
        # ns.abort(404)

# class StageCode(Resource):
#     def get(self):
#         codes = Codes.query.filter().all()
#         codedict = query_to_dict(codes)
#         code_dict = {}
#         for code in codedict:
#             code_dict[code.get('code')] = code.get('name')
#         return code_dict
