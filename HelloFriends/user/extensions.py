# -*- coding: utf-8 -*-
# @Time  : 2020/10/23 下午8:03
# @Author : 司云中
# @File : extensions.py
# @Software: Pycharm

from flask_login import LoginManager
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy


login_manager = LoginManager()
db = SQLAlchemy()
mongo = PyMongo()