# -*- coding: utf-8 -*-
# @Time  : 2020/9/27 下午2:01
# @Author : 司云中
# @File : models.py
# @Software: Pycharm
from user import db


class User(db.Model):
    """创建用户表"""
    id = db.Column(db.Integer(), primary_key=True)  # 整型主键
    username = db.Column(db.String(30))
    phone = db.Column(db.String(11), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    # 多对一关系,如果想要一对一,添加uselist=False
    # backref:反向引用,在QQOauth类型上声明一个新属性,用于QQOauth的实例通过该属性访问该模型实例
    # lazy决定了sqlalchemy何时从数据库中加载数据, dynamic懒加载,返回查询对象,可进一步过滤后hit数据库
    qq_auth = db.relationship('QQOauth', backref='user', lazy='dynamic')


    def __init__(self, username, phone, password):
        self.username = username
        self.phone = phone
        self.password  = password

    def __repr__(self):
        return f"<[User] username:{self.username}, phone: {self.phone}"


class QQOauth(db.Model):
    """创建QQ第三方登录"""

    # 添加外键约束
    id = db.Column(db.Integer, primary_key=True)
    # 创建外键,参照主表的id
    qq_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    openid = db.Column(db.String(128), nullable=False)
