# -*- coding: utf-8 -*-
# @Time  : 2020/10/22 下午6:29
# @Author : 司云中
# @File : auth.py
# @Software: Pycharm

from flask import (
    Blueprint, request
)
from flask_restful import Resource

# 创建一个蓝图

bp = Blueprint('auth', __name__, url_prefix='/auth')

class Register(Resource):
    """资源路由"""
    def get(self, request):
        pass



















