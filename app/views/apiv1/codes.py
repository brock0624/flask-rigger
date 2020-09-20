# -*- coding: utf-8 -*-
from flask_restplus import Namespace, Resource, fields
from app.extensions import db
from app.models import Codes
# from app.code import custom_abord, generate_response, ResponseCode
# from app.utils.common import query_to_dict

# 定义命名空间
ns = Namespace('codes', description='Codes related operations')

code = ns.model('Code', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'code': fields.String(required=True, description='The code name'),
    'code_value': fields.String(required=True, description='The code value'),
    'type': fields.String(required=True, description='The code value'),
    'version': fields.Integer(required=True, description='The code value',attribute='revision'),
    'active': fields.Boolean(required=True, description='The code value'),
})


class CodeDAO(object):
    def __init__(self):
        self.counter = 0
        self.codes = []

    def get(self, id):
        obj = Codes.query.filter_by(id=id).first()
        if obj:
            return obj
        ns.abort(404, "code {} doesn't exist".format(id))

    def get_all(self):
        obj = Codes.query.filter().all()
        if obj:
            return obj
        else:
            return []

    def get_active(self):
        obj = Codes.query.filter_by(active=True).all()
        if obj:
            return obj
        else:
            return []

    def get_by_code(self, code):
        obj = Codes.query.filter_by(code=code).first()
        if obj:
            return obj
        ns.abort(404, "code {} doesn't exist".format(code))

    def create(self, data):
        code = Codes(id=data.get("id"), code=data.get("code"), code_value=data.get("code_value"), type=data.get("type"),
                     revision=data.get("version"), active=data.get("active"))
        db.session.add(code)
        db.session.commit()
        return code

    def update(self, id, data):
        code = self.get(id)
        code.active = data.get("active")
        db.session.add(code)
        # code.update("active",data.get("active"))
        return code

    def delete(self, id):
        code = self.get(id)
        db.session.delete(code)
        db.session.commit()


DAO = CodeDAO()


@ns.route('/')
class CodeList(Resource):
    @ns.doc('list_codes')
    @ns.marshal_list_with(code)
    def get(self):
        '''List all codes'''
        return DAO.get_all()

    @ns.doc('create_todo')
    @ns.expect(code)
    @ns.marshal_with(code, code=201)
    def post(self):
        '''创建一个新的task'''
        return DAO.create(ns.payload), 201


@ns.route('/active')
class CodeActiveList(Resource):
    @ns.doc('list_active_codes')
    @ns.marshal_list_with(code)
    def get(self):
        '''List active codes'''
        return DAO.get_active()


@ns.route('/<int:id>')
@ns.param('id', 'The code identifier')
@ns.response(404, 'Code not found')
class Code(Resource):
    '''获取单个code项，并允许删除操作'''

    @ns.doc('get_code')
    @ns.marshal_with(code)
    def get(self, id):
        '''获取id指定的code项'''
        return DAO.get(id)

    @ns.doc('delete_todo')
    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''根据id删除对应的task'''
        DAO.delete(id)
        return '', 204

    @ns.expect(code)
    @ns.marshal_with(code)
    def put(self, id):
        '''更新id指定的task'''
        return DAO.update(id, ns.payload)

@ns.route('/<string:code>')
@ns.param('code', 'The code identifier')
@ns.response(404, 'Code not found')
class Code(Resource):
    '''获取单个code项，并允许删除操作'''

    @ns.doc('get_code')
    @ns.marshal_with(code)
    def get(self, code):
        '''获取code指定的code项'''
        return DAO.get_by_code(code)