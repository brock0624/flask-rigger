# -*- coding: utf-8 -*-

from app.extensions import db


class Codes(db.Model):
    __tablename__ = 't_codes'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(660))
    type = db.Column(db.String(20))
    version = db.Column(db.Integer)
    active = db.Column(db.Boolean())

    def to_dict(self):
        dict = {c.name:getattr(self,c.name,None) for c in self.__table__.columns}
        return dict

