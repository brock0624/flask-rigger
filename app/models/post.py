from datetime import datetime
from app.extensions import db


class Post(db.Model):
    __tablename__ = 't_posts'
    id = db.Column(db.Integer, primary_key=True, comment="主键id")
    # 区别是评论还是微博
    rid = db.Column(db.Integer, index=True, nullable=False, default=0, comment="区别是评论还是正文")
    content = db.Column(db.Text, comment="正文")
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, comment="创建时间")
    # 添加关联外键 '表名.字段'
    users_id = db.Column(db.Integer, db.ForeignKey('s_user.id'), comment="创建人id")
    # 缩略图
    pic = db.Column(db.String(64), default='default.jpg', comment="缩略图")
    # 类别
    category = db.Column(db.String(64), default='科技', comment="类别")
    # 访问量
    visitors = db.Column(db.Integer, default=0, comment="访问量")

    def __repr__(self):
        return self.content[:20]
