# -*- coding: utf-8 -*-
from .main import main
from .users import users
from .apiv1 import blueprint as apiv1
from .apiv2 import blueprint as apiv2


DEFAULT_BLUEPRINT = (
    (main, ''),
    (main, '/main'),
    (users, '/users'),
    (apiv1, '/api/v1'),
    (apiv2, '/api/v2'),
)


# 封装配置蓝本的函数
def config_blueprint(app):
    # 循环读取元组中的蓝本
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)
