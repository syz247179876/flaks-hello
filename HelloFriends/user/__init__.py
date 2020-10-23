# -*- coding: utf-8 -*-
# @Time  : 2020/9/27 下午2:00
# @Author : 司云中
# @File : __init__.py.py
# @Software: Pycharm

from flask import Flask
from config import config_develop
from .auth import auth
from .extensions import db, login_manager, mongo
from log import setup_log


def create_app(test_config=None):
    """创建和配置应用实例"""

    # instance_relative_config, instance的文件夹位于flaskr程序包外部，可以保存不应提交给版本控制的本地数据，例如配置密钥和数据库文件

    app = Flask(__name__, instance_relative_config=True)  # 实例化flask应用

    app.secret_key = '4A8BF09E6732FDC682988A8SYZ666AB7CF53176D08631E'

    # config是一个字典
    app.config.from_object(config_develop)  # 导入类对象作为默认配置,如果包含property，则必须以实例的方式传入

    login_manager.init_app(app)      # 将flask_login注册到app中

    mongo.init_app(app)              # 将flask_mongo注册到app中

    app.register_blueprint(auth.bp)  # 导入蓝图数图

    setup_log(config_develop)

    return app
