# -*- coding: utf-8 -*- 
from flask_restplus import abort
import datetime


class ResponseCode:
    CODE_SUCCESS = 200  # 凡是成功都用
    CODE_CREATED = 201  # 已创建
    CODE_DELETED = 204  # 已删除
    CODE_NO_PARAM = 400  # 参数错误
    CODE_NOT_LOGIN = 401  # 未认证
    CODE_FORBIDDEN = 403  # 没权限
    CODE_NOTFOUND = 404  # 资源不存在
    CODE_SERVER_ERROE = 500  # 服务器错误

    msg = {
        CODE_SUCCESS: "success",
        CODE_CREATED: "create success",
        CODE_DELETED: "delete success",
        CODE_NO_PARAM: "params error",
        CODE_NOT_LOGIN: "not auth",
        CODE_FORBIDDEN: "permission denied",
        CODE_NOTFOUND: "source not found",
        CODE_SERVER_ERROE: "sorry,server is error"
    }


def generate_response(data=None, message=None, code=ResponseCode.CODE_SUCCESS):
    if message is None:
        message = ResponseCode.msg[code]
    return {
        'message': message,
        'code': code,
        'data': data,
        # 'ctime' : datetime.datetime.now()
    }


# 增加一个type,方便控制 data的[],{},""格式和有数据一样，避免前端报错
def custom_abord(http_status_code, *args, **kwargs):
    if http_status_code == 400:
        # 重定义400返回参数
        abort(400, **generate_response(message=ResponseCode.msg[http_status_code], code=http_status_code))
    abort(http_status_code)
