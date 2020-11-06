# -*- coding: utf-8 -*-
# @Time  : 2020/11/6 下午8:05
# @Author : 司云中
# @File : demo.py
# @Software: Pycharm
from flask_restful import Resource


class Todo1(Resource):
    def get(self):
        # Default to 200 OK
        return {'task': 'Hello world'}


class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'task': 'Hello world'}, 201


class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}


from flask_restful import fields, marshal_with

# 自定义字段
class UrgentItem(fields.Raw):
    def format(self, value):
        return "Urgent" if value & 0x01 else "Normal"

resource_fields = {
    'task': fields.String,
    'uri': fields.Url('todo'),  # 通过endpoint生成其对应的url路径,并由Response返回
    'full_name': fields.String(attribute='actual_name'), # 替代的别名
    'priority': UrgentItem(attribute='flags')
}


class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'


class Todo(Resource):
    @marshal_with(resource_fields)  # 类装饰器,将python对象序列化为dict
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')



# 将api与blueprint结合起来

