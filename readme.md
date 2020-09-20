# flask-rigger
## 简介
flask-rigger是一个Python环境下的后台管理系统脚手架工具。

1. 使用flask-admin做简单后台管理
2. 使用flask-restplus作api框架
3. ORM框架使用SQLAlchemy
4. 集成Flask-APScheduler作为调度管理


## 第三方依赖
~~~
Flask==1.1.2
Flask-Admin==1.5.6
Flask-APScheduler==1.11.0
Flask-BabelEx==0.9.4
Flask-Cache==0.13.1
Flask-CKEditor==0.4.4.1
Flask-DebugToolbar==0.11.0
Flask-Login==0.5.0
Flask-Mail==0.9.1
Flask-Migrate==2.5.3
Flask-Moment==0.10.0
Flask-Principal==0.4.0
flask-redis==0.4.0
flask-restplus==0.13.0
Flask-Script==2.0.6
Flask-Security==3.0.0
Flask-Session==0.3.2
Flask-SQLAlchemy==2.4.4
Flask-Uploads==0.2.1
Flask-WTF==0.14.3
~~~




## 环境配置
### venv虚拟环境安装配置
```
sudo pip3 install virtualenv
virtualenv venv
. venv/bin/activate
```

### 第三方依赖安装
```
pip3 install -r requirements.txt
```
### 系统参数配置
1. 编辑`/app/conf/config.py`， 修改SECRET_KEY及MySQL数据库相关参数
```
SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pzl123456@localhost/test-database'
```

2. 编辑/app/log-app.conf，修改日志路径
```
args=('/applog/rains/flask-rigger.log','a','utf8')
```

### 数据库初始化

方法一：

​	直接运行docs/flask-rigger.sql 文件

方法二：

​	使用Flask-Migrate管理数据库

~~~
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
~~~

### 启动应用
```
nohup ./manage.py runserver 2>&1 &
或
./run_app_dev.py (仅限测试)
```

访问地址： http://127.0.0.1:5000/

账号密码：admin/admin123

## 项目目录结构

~~~
flask-rigger
├── app				# 工程主目录
│   ├── __init__.py				# 初始化
│   ├── admin				#
│   ├── conf				# 系统参数及日志配置
│   │   ├── config.py
│   │   └── log-app.conf
│   ├── extensions.py				# 扩展应用
│   ├── forms
│   ├── models				# 数据库模型
│   ├── sche				# 调度任务
│   ├── static				# JS、CSS等静态文件
│   ├── templates				# 页面模版
│   ├── utils				#工具模块
│   │   ├── common.py
│   │   ├── email.py
│   │   ├── code.py
│   │   └── env.py
│   └── views				#对外view
│       ├── apiv1
│       └── apiv2
├── docs				# 文档
│   └── flask-rigger.sql
├── make_requirement.py				# 生成依赖文件
├── manage.py				# 项目入口
├── migrations				# 数据库镜像，自动生成
├── packages				# 第三方依赖包
├── readme.md
├── requirements.txt			# 第三方依赖-
├── run_app_dev.py				# 测试入口
└── run_app_test.py				# 测试入口
~~~

