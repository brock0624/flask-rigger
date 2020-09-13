# -*- coding: utf-8 -*-
from .main import main
from .users import users
from .api_1_0 import api_bp as api_1_0
# from .api_1_1 import api as api_1_1

DEFAULT_BLUEPRINT = (
    (main, ''),
    (main, '/main'),
    (users, '/users'),
    (api_1_0, '/api/v10'),
    # (api_1_1, '/api/v11'),
)


# 封装配置蓝本的函数
def config_blueprint(app):
    # 循环读取元组中的蓝本
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)
