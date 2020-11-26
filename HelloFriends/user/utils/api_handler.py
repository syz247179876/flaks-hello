# -*- coding: utf-8 -*-
# @Time  : 2020/11/26 上午11:02
# @Author : 司云中
# @File : api_handler.py
# @Software: Pycharm
import werkzeug

from manage import app
from user.utils.api_exceptions import QQServiceUnavailable, ApiException, QQ_AUTHENTICATION_ERROR


@app.errorhandler(QQServiceUnavailable)
def handler_error(e):
    # 判断异常是不是ApiException
    if isinstance(e, ApiException):
        return e
    if isinstance(e, werkzeug.exceptions.HTTPException):
        code = e.code
        description = e.description
        return ApiException(code=code, error_code=QQ_AUTHENTICATION_ERROR, msg=description)
    # else:
    #     # 其他异常
    #     if app.config['DEBUG']:
    #         # TODO:日志记录
    #         return e
    #     else:
    #         return e