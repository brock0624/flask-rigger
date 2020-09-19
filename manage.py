# -*- coding:utf-8 -*-
import os
from app import create_app
from flask_script import Manager, Server
from flask_migrate import MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

server = Server(host="127.0.0.1", port=5000)
manager.add_command("runserver", server)
manager.add_command('db',MigrateCommand)
# manager.add_option('-c', '--config', dest='config', required=False)

@manager.command
def hello():
    'hello world'
    print('hello world')

@manager.option('-n', '--name', dest='name', help='Your name', default='world')
@manager.option('-u', '--url', dest='url', default='zero.brock.fun')
def test(name, url):
    'hello world or hello <setting name>'
    print('hello', name)
    print(url)


if __name__ == '__main__':
    manager.run()
