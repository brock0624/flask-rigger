# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restplus import Api

# from .users import UsersView, UsersList
# from .codes import StageCode
from .codes import ns as codes
from .todos import ns as todos

# 创建蓝本对象
blueprint = Blueprint('apiv1', __name__)
flask_api = Api(blueprint,
                title='flask_rigger apis',
                version='1.0',
                description='这是注释', )

flask_api.add_namespace(codes)
flask_api.add_namespace(todos)
