# -*- coding: utf-8 -*-
# @Time  : 2020/11/17 下午11:26
# @Author : 司云中
# @File : error.py
# @Software: Pycharm
from flask import render_template, Blueprint, jsonify
from flask_restful import Resource, abort



error = Blueprint('error', __name__, url_prefix='/error')

# 自定义异常404重定向的页面
@error.errorhandler(404)
def page_not_found(error):
    response = dict(status=0, message="404 Not Found")
    return jsonify(response), 404


class Error(Resource):
    def get(self):
        abort(404)