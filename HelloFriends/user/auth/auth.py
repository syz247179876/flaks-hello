# -*- coding: utf-8 -*-
# @Time  : 2020/10/22 下午6:29
# @Author : 司云中
# @File : auth.py
# @Software: Pycharm

import functools


from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


# 创建一个蓝图
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register',methods=('GET','POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']





