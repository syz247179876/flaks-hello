# -*- coding: utf-8 -*-
# @Time  : 2020/11/7 上午12:03
# @Author : 司云中
# @File : dependencies.py
# @Software: Pycharm

'''
依赖注入
'''
from flask import Blueprint
from flask_restful import Resource, abort

bp_dependencies = Blueprint('dependencies', __name__, url_prefix='/dependencies')

class TodoNext(Resource):
    def __init__(self, **kwargs): # kwargs中传进来黑盒依赖
        self.my_dependencies = kwargs['dependencies']

    def get(self):
        return self.my_dependencies()  # 调用依赖操作



