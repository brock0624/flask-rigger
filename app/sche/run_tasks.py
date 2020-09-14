# -*- coding: utf-8 -*-
from datetime import datetime
from flask import current_app


def task_func(task_id):
    """业务逻辑"""
    # 发邮件、写诗、画画 -> 爱干啥干啥
    print('task_func')


def task_date(task_id, task_type):
    msg = "{task_id}-{task_type}-{date}".format(task_id=task_id, task_type=task_type,
                                                date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(msg)


def task_interval(task_id, task_type):
    msg = "{task_id}-{task_type}-{date}".format(task_id=task_id, task_type=task_type,
                                                date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(msg)


def task_cron(task_id, task_type):
    msg = "{task_id}-{task_type}-{date}".format(task_id=task_id, task_type=task_type,
                                                date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(msg)
