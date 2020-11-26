# -*- coding: utf-8 -*-
# @Time  : 2020/9/27 下午2:04
# @Author : 司云中
# @File : manage.py.py
# @Software: Pycharm

# from user import create_app, db
from user import db, app
from flask_script import Manager, Server

from user.models import User

manager = Manager(app)

manager.add_command('runserver', Server)  # 使用python manage.py runserver就可以启动服务器了

# 创建在命令行里面的上下文环境,想到与在命令行中直接导入
@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)
# 命令行中可以使用db.create_all()来创建数据表

if __name__ == '__main__':
    # 启动flask服务
    manager.run()
    # app.run(host='127.0.0.1', port=5000)