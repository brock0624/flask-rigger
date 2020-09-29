# -*- coding: utf-8 -*-
import os
from datetime import datetime, timedelta
from redis import Redis
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))


# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# 定义配置基类
class Config:
    # 秘钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'

    # 数据库公用配置
    # 无警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True
    # 调度
    # 调度器开关
    SCHEDULER_API_ENABLED = True
    SCHEDULER_API_PREFIX = '/schedule'
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    JOBS = [
        # date 一次性任务，当系统启动时，该任务执行一次
        {
            'id': 'job_date',
            'func': 'app.sche.tasks:task_date',
            'args': (1, 'job_date'),
            'next_run_time': datetime.now() + timedelta(seconds=10)
        },
        # interval 循环间隔任务
        {
            'id': 'job_interval',
            'func': 'app.sche.tasks:task_interval',
            'args': (2, 'job_interval'),
            'trigger': 'interval',
            'seconds': 50  # 每隔50秒执行一次
        },
        # cron 循环定时任务
        {
            'id': 'job_cron',
            'func': 'app.sche.tasks:task_cron',
            'args': (3, 'job_cron'),
            'trigger': {
                'type': 'cron',
                'second': '5'
            }
        }
    ]
    # 持久化配置
    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 20}
    }
    SCHEDULER_JOB_DEFAULTS = {
        'coalesce': True,
        'max_instances': 3,
        'misfire_grace_time': 3600
    }
    # 解决FLASK DEBUG模式定时任务执行两次
    WERKZEUG_RUN_MAIN = True

    # 邮件 公共配置
    MAIL_USE_SSL = True
    MAIL_SUPPRESS_SEND = False
    MAIL_PORT = 465
    MAIL_USE_TLS = False

    # ITEMS_PER_PAGE = 10
    # JWT_AUTH_URL_RULE = '/api/auth'

    # 文件上传的位置
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024
    UPLOADED_PHOTOS_DEST = os.path.join(BASE_DIR, 'app/static/uploads')

    # Flask - Security
    # 用户追踪
    SECURITY_TRACKABLE = True
    # Flask-Security config
    SECURITY_URL_PREFIX = "/"
    SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
    SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"

    # Flask-Security URLs, overridden because they don't put a / at the end
    SECURITY_LOGIN_URL = "/login/"
    SECURITY_LOGOUT_URL = "/logout/"
    SECURITY_REGISTER_URL = "/register/"
    SECURITY_UNAUTHORIZED_VIEW = "/unauth"

    SECURITY_POST_LOGIN_VIEW = "/"
    SECURITY_POST_LOGOUT_VIEW = "/"
    SECURITY_POST_REGISTER_VIEW = "/"

    # Flask-Security features
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # bootstrap
    BOOTSTRAP_USE_MINIFIED = True
    BOOTSTRAP_SERVE_LOCAL = True

    # session
    SESSION_TYPE = 'filesystem'
    # 是否长期有效
    SESSION_PERMANENT = False
    # 是否强制加盐
    SESSION_USE_SIGNER = True
    SESSION_FILE_THRESHOLD = 2

    # 额外的初始化操作
    @staticmethod
    def init_app(app):
        pass


# 开发环境配置
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:test123@localhost/scott?charset=utf8mb4'
    # SCHEDULER_JOBSTORES = {
    #     'default': SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URI)
    # }
    # 发邮件 配置
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USERNAME = 'test@qq.com'
    MAIL_PASSWORD = 'miborlqplwsibddf'

    # cache
    CACHE_REDIS_HOST = 'localhost'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_PASSWORD = 'test123'
    CACHE_REDIS_DB = 0
    CACHE_TYPE = 'redis'

    # Redis
    REDIS_URL = "redis://:{passwd}@{host}:{port}/{db}".format(passwd=CACHE_REDIS_PASSWORD, host=CACHE_REDIS_HOST,
                                                              port=CACHE_REDIS_PORT, db=CACHE_REDIS_DB)
    REDIS_CLI = Redis(host=CACHE_REDIS_HOST, port=CACHE_REDIS_PORT,
                      db=CACHE_REDIS_DB, password=CACHE_REDIS_PASSWORD)
    SESSION_TYPE = "redis"
    SESSION_REDIS = REDIS_CLI


# 测试环境配置
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:test123@localhost/test-database'


# 生产环境
class PrdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:test123@localhost/product-database'


# 生成一个字典，用来根据字符串找到对应的配置类。
config = {
    'dev': DevConfig,
    'testing': TestConfig,
    'prd': PrdConfig,
    'default': DevConfig
}
