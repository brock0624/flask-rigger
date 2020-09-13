# -*- coding: utf-8 -*- 
import os
from flask_security import login_required
from flask import Blueprint, render_template, current_app, redirect, url_for, flash, request, render_template_string, \
    session

# 创建蓝本对象
from app.forms.users import login_form, register_form

users = Blueprint('users', __name__)


@users.route('/')
def show():
    return session.get('key', 'not set') + '设置' + session.get('user', 'not set')


@users.route('/register', methods=('GET', 'POST'))
def register():
    form = register_form()  # 初始化表单
    return render_template('users/register.html', form=form)


@users.route('/login', methods=('GET', 'POST'))
def login():
    form = login_form()  # 初始化表单
    # if form.validate_on_submit():  # 如果页面有提交数据，在此创建数据库条目
    #     login_user = db_session.query(Users).filter_by(username=form.username.data).first()  # 查找name=jack的
    #     print(login_user.username)
    #     print(form.password.data)
    #     if login_user.password == form.password.data:
    #         session['key'] = 'value'
    #         session['user'] = 'user'
    #         return redirect(url_for('user.show'))  #
    #     else:
    #         return '登录失败'
    return render_template('users/login.html', form=form)


@users.route('/logout')
def logout():
    return 'user.logout'


@users.route('/test/')
def test():
    session['key'] = 'test'
    return 'ok'


@users.route('/clear/')
def clear():
    session.clear()
    return session.get('key', 'not set')
