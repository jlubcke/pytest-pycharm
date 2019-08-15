#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

readme = open('README.rst').read()

requirements = [
    'pytest>=2.3' 
]

setup(
    name='pytest-pycharm',
    version='0.6.0',
    description='Plugin for py.test to enter PyCharm debugger on uncaught exceptions',
    long_description=readme + '\n',
    author='Johan Lübcke',
    author_email='johan@lubcke.se',
    url='https://github.com/jlubcke/pytest-pycharm',
    py_modules=['pytest_pycharm'],
    entry_points={'pytest11': ['pycharm = pytest_pycharm']},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='pytest,py.test,pycharm',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
