# -*- coding: utf-8 -*-
# @Time  : 2020/11/6 下午8:14
# @Author : 司云中
# @File : urls.py
# @Software: Pycharm

# 路由集合

from flask_restful import Api

from user.api.dependencies import bp_dependencies, TodoNext
from user.auth.auth import Register, bp
from user.api.demo import Todo1

api = Api(bp)  # 将api与blueprint结合
api_dependencies = Api(bp_dependencies)

api.add_resource(Todo1,'/todo1', endpoint='todo666') # 添加资源路由
api.add_resource(Todo1,'/todo/<todo_id>', endpoint='todwwwwo')
api.add_resource(Register, '/register', endpoint='register')

def dependencies():
    """依赖方法/类"""
    return 'i am dependencies'

api_dependencies.add_resource(TodoNext, '/todo-next', endpoint='todo-next', resource_class_kwargs={'dependencies':dependencies})  # 依赖注入实例