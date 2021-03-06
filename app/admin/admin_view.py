# -*- coding: utf-8 -*-
from flask import abort, url_for, request, redirect
from flask_admin import BaseView, expose
from flask_admin.contrib import sqla
from flask_security import current_user


class AdminModelView(sqla.ModelView):
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('superuser')
                )

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))


class MyAdminView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')
