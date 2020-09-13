# -*- coding: utf-8 -*- 
from flask import Blueprint
from flask_restful import Api, Resource
from .users import UsersView, UsersList
from .codes import StageCode

# 创建蓝本对象
api_bp = Blueprint('api_1_0', __name__)
flask_api = Api(api_bp)

flask_api.add_resource(UsersView, '/users/<int:id>')
flask_api.add_resource(UsersList, '/userslist')
flask_api.add_resource(StageCode, '/codes')
