# manage.py

from flask import Flask
from flask.ext.script import Manager
from flask.ext.dbshell import DbShell


class DevConfig(object):
    DATABASE_URI = 'sqlite:///demo.sqlite'


app = Flask(__name__)
app.config.from_object(DevConfig)
manager = Manager(app)


@manager.command
def dbshell():
    shell = DbShell(url=app.config['DATABASE_URI'])
    shell.run_shell()


if __name__ == "__main__":
    manager.run()
