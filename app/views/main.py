# -*- coding: utf-8 -*-
from flask_security import login_required
from flask import Blueprint, render_template, current_app, redirect, url_for, flash, request, render_template_string

# 创建蓝本对象
main = Blueprint('main', __name__)


@main.route('/')
@login_required
def admin():
    # return '<a href="/admin/">Click me to get to Admin!</a>'
    return render_template('index.html')


@main.route('/base')
def base():
    return render_template('base/base.html')


@main.route('/view_plan1/')
@login_required
def view_plan1():
    return render_template('main/plan.html', name1='测试name1的渲染', name2='name2渲染')
