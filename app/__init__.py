# -*- coding: utf-8 -*- 
import logging
from logging.config import fileConfig
from flask import Flask, render_template, url_for
from flask_admin import helpers as admin_helpers
from flask_security import SQLAlchemyUserDatastore
from redis import Redis

from app.admin.admin_view import AdminModelView
from app.admin.rediscli_view import RedisCliView
from app.admin.users_view import UserView
from app.conf.config import config
from app.extensions import config_extensions, scheduler, admin, db, redis_client, security
from app.models import User, Role
from app.models.codes import Codes
from app.views import config_blueprint

fileConfig('app/conf/log-app.conf')


def get_logger(name):
    return logging.getLogger(name)


def config_errorhandler(app):
    # 如果在蓝本定制，则只针对蓝本的错误有效。
    # 可以使用app_errorhandler定制全局有效的错误显示
    # 定制全局404错误页面
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error/404.html', e=e)


def config_scheduler(app):
    """Configure Scheduler"""
    # sche.init_app(app)
    scheduler.start()

    # 加载任务，选择了第一次请求flask后端时加载，可以选择别的方式...
    @app.before_first_request
    def load_tasks():
        # 开启任务
        from app.sche import run_tasks


def config_admin(app):
    admin.add_view(AdminModelView(User, db.session))
    admin.add_view(AdminModelView(Role, db.session))
    admin.add_view(AdminModelView(Codes, db.session))

    # redis
    redis_cli = RedisCliView(app.config.get('REDIS_CLI'))

    admin.add_view(redis_cli)

    @app.context_processor
    def security_context_processor():
        return dict(
            admin_base_template=admin.base_template,
            admin_view=admin.index_view,
            h=admin_helpers,
            get_url=url_for
        )


# 将创建app的动作封装成一个函数
def create_app(config_name):
    # 创建app实例对象
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(config.get(config_name) or 'default')
    # 执行额外的初始化
    config.get(config_name).init_app(app)

    # 设置debug=True,让toolbar生效
    # app.debug=True

    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    # 加载扩展
    config_extensions(app)

    # 加载admin
    config_admin(app)

    # 初始化调度器配置
    config_scheduler(app)

    # 配置蓝本
    config_blueprint(app)

    # 配置全局错误处理
    config_errorhandler(app)

    # 返回app实例对象
    return app
