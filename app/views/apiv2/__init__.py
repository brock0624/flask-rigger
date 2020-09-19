# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restplus import Api

from .todos import ns as todos

# 创建蓝本对象
blueprint = Blueprint('apiv2', __name__)
flask_api = Api(blueprint,
                title='flask_rigger apis',
                version='2.0',
                description='这是注释', )
flask_api.add_namespace(todos)
