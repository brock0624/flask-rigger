# -*- coding: utf-8 -*-
from .tasks import task_func
from apscheduler.triggers.cron import CronTrigger  # 可以很友好的支持添加一个crontab表达式
from flask import current_app


def run_task():
    # 从数据库中初始化定时任务
    # TODO 从数据库中初始化定时任务
    current_app.logger.info("从数据库中初始化定时任务,TODO")
    pass


# 最重要的，这样当__init__.py创建app时加载这个文件，就会执行添加历史任务啦！
run_task()
