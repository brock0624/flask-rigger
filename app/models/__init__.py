# -*- coding: utf-8 -*-
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
