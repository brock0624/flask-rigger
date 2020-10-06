# -*- coding: utf-8 -*-
from PIL import Image
from flask import Blueprint, render_template, current_app, redirect, url_for, flash, request, render_template_string, \
    session
from flask_security import logout_user, login_user, current_user



users = Blueprint('users', __name__)


@users.route('/')
def show():
    return session.get('key', 'not set') + '设置' + session.get('user', 'not set')


# 展示用户个人信息
@users.route('/profile/')
def profile():
    return render_template('users/profile.html')


@users.route('/test/')
def test():
    session['key'] = 'test'
    return 'ok'


@users.route('/clear/')
def clear():
    session.clear()
    return session.get('key', 'not set')
