Flask DbShell
===================

The extension provides facilites for implementing Django-like ```./manage.py dbshell``` command

Installation
------------

Install the extension with one of the following commands:


```bash
$ easy_install flask-dbshell
```

or alternatively if you have pip installed:

```bash
$ pip install flask-dbshell
```

How to use
----------

Example of a simple script that runs mysql's shell

```python
from flask.ext.dbshell import DbShell


def main():
    dbshell = DbShell('mysql://scott:tiger@server/dbname')
    dbshell.run_shell()
    

if __name__ == '__main__':
    main()
```

Example of use with Flask-Script:

```python
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
```


Python versions supported
-------------------------

Tested with 2.6.x and 2.7.x
