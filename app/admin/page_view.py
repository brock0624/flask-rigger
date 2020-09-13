# -*- coding: utf-8 -*-

from wtforms import fields, widgets
from app.admin.admin_view import AdminModelView


# define a custom wtforms widget and field.
# see https://wtforms.readthedocs.io/en/latest/widgets.html#custom-widgets
class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        # add WYSIWYG class to existing classes
        existing_classes = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class'] = '{} {}'.format(existing_classes, "ckeditor")
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()


class PageView(AdminModelView):
    form_overrides = {
        'text': CKTextAreaField
    }
    create_template = 'admin/create_page.html'
    edit_template = 'admin/edit_page.html'
