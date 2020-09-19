# -*- coding: utf-8 -*-
import datetime

from sqlalchemy import UniqueConstraint

from app.extensions import db


class Codes(db.Model):
    __tablename__ = 't_codes'
    id = db.Column(db.Integer, primary_key=True, comment="主键id")
    code = db.Column(db.String(64), comment="代码")
    code_value = db.Column(db.String(660), comment="代码值")
    type = db.Column(db.String(20), comment="代码类型")
    revision = db.Column(db.Integer, comment="乐观锁")
    active = db.Column(db.Boolean(), comment="状态")
    created_by = db.Column(db.String(20), server_default="sys", comment="创建人")
    created_time = db.Column(db.DateTime, default=datetime.datetime.now, comment="创建时间")
    updated_by = db.Column(db.String(20), server_default="sys", comment="更新人")
    updated_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment="更新时间")
    memo = db.Column(db.String(20), comment="备注")

    # 索引
    __table_args__ = (
        UniqueConstraint("code", "type", name="code_code_type"),
    )

    def to_dict(self):
        dict = {c.code_value: getattr(self, c.code_value, None) for c in self.__table__.columns}
        return dict
