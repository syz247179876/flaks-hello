# -*- coding: utf-8 -*-
# @Time  : 2020/10/22 下午6:29
# @Author : 司云中
# @File : auth.py
# @Software: Pycharm


from flask import (
    Blueprint
)
from flask_restful import Resource

# 创建一个蓝图

bp = Blueprint('auth', __name__, url_prefix='/auth')


# @bp.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         print(request)
#     return Response()

class Register(Resource):
    """资源路由"""
    def get(self, ):
        pass

















