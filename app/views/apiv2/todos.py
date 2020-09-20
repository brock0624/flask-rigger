# -*- coding: utf-8 -*-
from flask_restplus import Namespace, Resource, fields, marshal

# 定义命名空间
from app.utils.code import generate_response, ResponseCode

ns = Namespace('todos', description='TODO operations')

todo = ns.model('Todo', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})


class TodoDAO(object):
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                return todo
        ns.abort(404, "Todo {} doesn't exist".format(id))

    def create(self, data):
        todo = data
        todo['id'] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self, id):
        todo = self.get(id)
        self.todos.remove(todo)


DAO = TodoDAO()
DAO.create({'task': 'Build an API'})
DAO.create({'task': '?????'})
DAO.create({'task': 'profit!'})


@ns.route('/')
class TodoList(Resource):
    '''获取所有todos元素，并允许通过POST来添加新的task'''

    @ns.doc('list_todos')
    def get(self, resource_fields=todo):
        '''返回所有task'''
        dic = marshal(DAO.todos, resource_fields)
        return generate_response(data=dic, code=ResponseCode.CODE_SUCCESS)

    @ns.doc('create_todo')
    @ns.expect(todo)
    def post(self, resource_fields=todo):
        '''创建一个新的task'''
        dic = marshal(DAO.create(ns.payload), resource_fields)
        return generate_response(data=dic, code=ResponseCode.CODE_CREATED), 201


@ns.route('/<int:id>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
class Todo(Resource):
    '''获取单个todo项，并允许删除操作'''

    @ns.doc('get_todo')
    def get(self, id):
        '''获取id指定的todo项'''
        dic = marshal(DAO.todos, todo)
        return generate_response(data=DAO.get(id), code=ResponseCode.CODE_SUCCESS)

    @ns.doc('delete_todo')
    # @ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''根据id删除对应的task'''
        DAO.delete(id)
        return generate_response(code=ResponseCode.CODE_DELETED), 204

    @ns.expect(todo)
    @ns.marshal_with(todo)
    def put(self, id):
        '''更新id指定的task'''
        return DAO.update(id, ns.payload)
