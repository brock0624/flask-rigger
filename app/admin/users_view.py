# -*- coding: utf-8 -*-
from flask_admin.form import rules
from app.admin.admin_view import AdminModelView


class UserView(AdminModelView):
    """
    This class demonstrates the use of 'rules' for controlling the rendering of forms.
    """
    form_create_rules = [
        # Header and four fields. Email field will go above phone field.
        rules.FieldSet(('username', 'email', 'password'), 'Personal'),
        # Separate header and few fields
        rules.FieldSet(('last_login_at', 'current_login_at', 'last_login_ip', 'current_login_ip', 'login_count'),
                       'login'),
        rules.Field('active'),
        rules.Field('confirmed_at'),
        rules.Field('roles'),

        # String is resolved to form field, so there's no need to explicitly use `rules.Field`
        # Show macro that's included in the templates
        # rules.Container('rule_demo.wrap', rules.Field('notes'))
    ]

    # Use same rule set for edit page
    form_edit_rules = form_create_rules

    create_template = 'admin/create_user.html'
    edit_template = 'admin/edit_user.html'
