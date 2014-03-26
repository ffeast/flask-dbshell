"""Flask-DbShell-------------
Django-like dbshell
"""
from setuptools import setup


setup(
    name='Flask-DbShell',
    version='1.0',
    url='http://github.com/ffeast/flask-dbshell/',
    license='BSD',
    author='ffeast',
    author_email='ffeast@gmail.com',
    description='Django-like dbshell',
    long_description=__doc__,
    py_modules=['flask_sqlite3'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'mock'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
