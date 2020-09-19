# -*- coding: utf-8 -*-
from flask import current_app, flash
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from flask_security import UserMixin

from app.extensions import db


class User(db.Model, UserMixin):
    __tablename__ = 's_user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary='s_roles_users',
                            backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return self.username

    # # 密码字段保护
    # @property
    # def password(self):
    #     raise AttributeError('密码是不可读属性')
    #
    # # 设置密码，加密存储
    # @password.setter
    # def password(self, password):
    #     # 相当于执行  user.password_hash=password
    #     self.password_hash = generate_password_hash(password)
    #
    #     # 生成激活的token
    #     def generate_activate_token(self):
    #         # 创建用于生成token的类，需要传递秘钥和有效期expires_in默认=3600,expires_in=60
    #         s = Serializer(current_app.config['SECRET_KEY'])
    #         # 生成包含有效信息(必须是字典数据)的token字符串
    #         return s.dumps({'id': self.id})
    #
    # # 生成任意的token
    # @staticmethod
    # def generate_token(dict):
    #     s = Serializer(current_app.config['SECRET_KEY'])
    #     # 生成包含有效信息(必须是字典数据)的token字符串
    #     return s.dumps(dict)
    #
    # # 检查任意token是否有效,返回真实词典数据
    # @staticmethod
    # def check_token(token):
    #     s = Serializer(current_app.config['SECRET_KEY'])
    #     try:
    #         data = s.loads(token)
    #     except SignatureExpired:
    #         flash('邮件已过期')
    #         return False
    #     except BadSignature:
    #         flash('无效的验证邮箱')
    #         return False
    #     return data
    #
    # # 账户激活，因为激活时还不知道是哪个用户
    # @staticmethod
    # def check_activate_token(token):
    #     s = Serializer(current_app.config['SECRET_KEY'])
    #     try:
    #         data = s.loads(token)
    #         print(data)
    #     except SignatureExpired:
    #         flash('激活邮件已过期')
    #         return False
    #     except BadSignature:
    #         flash('无效的激活')
    #         return False
    #     user = User.query.get(data.get('id'))
    #     print(user)
    #     if not user:
    #         flash('激活的账户不存在')
    #         return False
    #     if not user.confirm:  # 没有激活才需要激活
    #         user.confirm = True
    #         db.session.add(user)
    #     return True
    #
    # # 密码的校验
    # def verify_password(self, password):
    #     return check_password_hash(self.password_hash, password)
