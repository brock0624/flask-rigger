# -*- coding: utf-8 -*-
import random

from flask_restplus import Namespace, Resource, fields, marshal, reqparse

# 定义命名空间
from json2html import json2html

from app.utils.code import generate_response, ResponseCode
from app.utils.email import send_mail

ns = Namespace('todos', description='TODO operations')

todo = ns.model('Todo', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details'),

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
    @ns.marshal_list_with(todo)
    def get(self):
        '''返回所有task'''
        return DAO.todos

    @ns.doc('create_todo')
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        '''创建一个新的task'''
        return DAO.create(ns.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
class Todo(Resource):
    '''获取单个todo项，并允许删除操作'''

    @ns.doc('get_todo')
    @ns.marshal_with(todo)
    def get(self, id):
        '''获取id指定的todo项'''
        return DAO.get(id)

    @ns.doc('delete_todo')
    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''根据id删除对应的task'''
        DAO.delete(id)
        return '', 204

    @ns.expect(todo)
    @ns.marshal_with(todo)
    def put(self, id):
        '''更新id指定的task'''
        return DAO.update(id, ns.payload)


@ns.route('/sendmail')
class TodoListSendMail(Resource):
    '''获取所有todos元素，并进行邮件提醒'''

    @ns.doc('send_mail_todos')
    @ns.param('usermail', '收件人邮箱,多人以","分隔')
    def post(self, resource_fields=todo):
        '''获取所有todos元素，并进行邮件提醒'''
        parser = reqparse.RequestParser()
        parser.add_argument('usermail', required=True, help='收件人邮箱不能为空')
        args = parser.parse_args()
        usermail = args["usermail"]
        dic = marshal(DAO.todos, resource_fields)
        todos = json2html.convert(json=dic)
        send_mail(usermail.split(","), "Today's Todos!", "email/todos", todos=todos)
        return generate_response(data=dic, code=ResponseCode.CODE_SUCCESS)
