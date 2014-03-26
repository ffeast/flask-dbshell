"""Flask-DbShell-------------
Django-like dbshell
"""
from setuptools import setup, find_packages


setup(
    name='Flask-DbShell',
    version='1.0',
    url='http://github.com/ffeast/flask-dbshell/',
    license='BSD',
    author='ffeast',
    author_email='ffeast@gmail.com',
    description='Django-like dbshell',
    long_description=__doc__,
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
    ],
    tests_require=[
        'mock>=1.0.1'
    ],
    test_suite='tests',
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
