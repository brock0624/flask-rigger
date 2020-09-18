# -*- coding=utf-8 -*-
# 将pymysql得到的dic转换为可以正常转json的dic
import time
import datetime
import decimal


def kv_to_safe(k, v):
    # 判断v的数据类型,转换成可json的类型
    if type(v) == datetime.datetime:
        # 如果是datetime类型则转换为时间戳
        v = time.mktime(v.timetuple())
    if type(v) == decimal.Decimal:
        # 如果是decimal类型则转换为flaot
        v = float(v)
    if type(v) == bytes:
        # bytes类型转str(utf8)
        v = str(v, encoding='utf8')
    return k, v


def dict_to_safe(inf, code):
    # dict转可转json的dict
    if inf:
        if type(inf) == dict:
            info = {}
            for k, v in inf.items():
                k, v = kv_to_safe(k, v)
                info[k] = v
        elif type(inf) == list:
            info = []
            for i in inf:
                dic = {}
                for k, v in i.items():
                    k, v = kv_to_safe(k, v)
                    dic[k] = v
                info.append(dic)
    else:
        info = None
    dic = {
        'code': code,
        'data': info
    }
    return dic


def oneobj_to_safe(model):
    # 单一对象转dic
    dic = {}
    if model == None:
        return None
    for col in model._sa_class_manager.mapper.mapped_table.columns:
        dic[col.name] = getattr(model, col.name)
    return dic


def allobj_to_safe(model_list):
    # 多个对象转dic
    dic_list = []
    if model_list == None:
        return None
    for model in model_list:
        dic_list.append(oneobj_to_safe(model))
    return dic_list


def get_error_dic(code, message):
    # 生成错误json
    dic = {
        'code': code,
        'data': {
            'message': message
        }
    }
    return dic


def get_success_dic(dic):
    # 生成正确json,code默认200
    dic = {
        'code': 200,
        'data': dic
    }
    return dic
