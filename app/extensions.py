# -*- coding: utf-8 -*-
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_moment import Moment
from flask_security import Security
from flask_session import Session
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class
from flask_debugtoolbar import DebugToolbarExtension
from flask_ckeditor import CKEditor
# from flask_cache import Cache
from flask_apscheduler import APScheduler
from flask_admin import Admin
from flask_redis import FlaskRedis

# 创建对象
bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate(db=db)
mail = Mail()
moment = Moment()
security = Security()
session = Session()
scheduler = APScheduler()
# 上传
photos = UploadSet('photos', IMAGES)
# 调试工具
toolbar = DebugToolbarExtension()
# 富文本
ckeditor = CKEditor()

# 后台管理
admin = Admin(name='后台管理', template_mode='bootstrap3', base_template='base.html', )

# 缓存页面
# cache = Cache()
# redis
redis_client = FlaskRedis()


# 初始化
def config_extensions(app):
    bootstrap.init_app(app)
    session.init_app(app)
    # db.app = app
    db.init_app(app)
    migrate.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    # security.init_app(app)
    toolbar.init_app(app)
    # 注册APScheduler
    scheduler.init_app(app)
    redis_client.init_app(app)

    admin.init_app(app)

    # cache.init_app(app,config={'CACHE_TYPE':'simple'})

    # ckeditor.init_app(app)
    # 一些图片上传的配置
    # configure_uploads(app, photos)
    # 设置上传文件大小
    # patch_request_class(app, size=None)
