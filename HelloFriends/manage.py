# -*- coding: utf-8 -*-
# @Time  : 2020/9/27 下午2:04
# @Author : 司云中
# @File : manage.py.py
# @Software: Pycharm

from user import create_app

app = create_app()

if __name__ == '__main__':
    # 启动flask服务
    app.run(host='127.0.0.1', port=5000)