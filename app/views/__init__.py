# -*- coding: utf-8 -*-
from .main import main
from .users import users
from .apiv1 import blueprint as apiv1


DEFAULT_BLUEPRINT = (
    (main, ''),
    (main, '/main'),
    (users, '/users'),
    (apiv1, '/api/v1'),
    # (api_1_1, '/api/v11'),
)


# 封装配置蓝本的函数
def config_blueprint(app):
    # 循环读取元组中的蓝本
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)
