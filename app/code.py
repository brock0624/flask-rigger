# -*- coding: utf-8 -*- 
from flask_restful import abort
import  datetime


class ResponseCode:
    code_success = 200  # 凡是成功都用
    CODE_NO_PARAM = 400  # 参数错误
    CODE_NOT_LOGIN = 401  # 未认证
    CODE_FORBIDDEN = 403  # 没权限
    CODE_NOTFOUND = 404  # 资源不存在
    CODE_SERVER_ERROE = 500  # 服务器错误

    msg = {
        code_success: "success",
        CODE_NO_PARAM: "params error",
        CODE_NOT_LOGIN: "not auth",
        CODE_FORBIDDEN: "permission denied",
        CODE_NOTFOUND: "source not found",
        CODE_SERVER_ERROE: "sorry,server is error"
    }


def generate_response(data=None, message=ResponseCode.msg[ResponseCode.code_success], code=ResponseCode.code_success):
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
