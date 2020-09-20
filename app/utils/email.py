from threading import Thread
from app.extensions import mail
from flask import current_app, render_template
from flask_mail import Message


def async_send_mail(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except:
            current_app.logger.info("邮件： {subject},收件人: {user} 发送失败".format(subject=msg.subject, user=msg.recipients))
        else:
            current_app.logger.info("邮件： {subject},收件人: {user} 发送成功".format(subject=msg.subject, user=msg.recipients))


# 异步发送邮件
def send_mail(to, subject, template, **kwargs):
    # 通过current_app这个代理对象，获取真正的app对象
    app = current_app._get_current_object()
    msg = Message(subject=subject, recipients=to, sender=app.config['MAIL_USERNAME'])
    msg.html = render_template(template + '.html', **kwargs)
    msg.body = render_template(template + '.txt', **kwargs)

    thr = Thread(target=async_send_mail, args=[app, msg])
    # 启动线程
    thr.start()

# send_mail([user.email], '激活邮件', 'email/activate', username=user.username, token=token)
