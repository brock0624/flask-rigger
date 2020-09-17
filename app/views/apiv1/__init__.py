# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restplus import Api

# from .users import UsersView, UsersList
# from .codes import StageCode
from .codes import ns as codes

# 创建蓝本对象
blueprint = Blueprint('api', __name__)
flask_api = Api(blueprint,
                title='flask_rigger apis',
                version='1.0',
                description='这是注释', )

# flask_api.add_resource(UsersView, '/users/<int:id>')
# flask_api.add_resource(UsersList, '/userslist')
# flask_api.add_resource(StageCode, '/codes')
flask_api.add_namespace(codes)
