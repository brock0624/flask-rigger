# -*- coding: utf-8 -*-
from flask import current_app
from .user import User
from .role import Role
from .codes import Codes

from app.extensions import db

# Define models
roles_users = db.Table(
    's_roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('s_user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('s_role.id'))
)


def init_db():
    """Clear existing data and create new tables."""
    # with current_app.open_resource("schema.sql") as f:
    #     db.executescript(f.read().decode("utf8"))
    print("初始化数据库脚本文件！！！")
