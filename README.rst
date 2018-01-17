===============================
pytest-pycharm
===============================

.. image:: https://badge.fury.io/py/pytest-pycharm.png
    :target: http://badge.fury.io/py/pytest-pycharm

Plugin for py.test to enter PyCharm debugger on uncaught exceptions

* Free software: BSD license

Features
--------

* Uncaught exceptions in py.test test cases will trigger the PyCharm debugger


Installation
------------

You can install the plugin by running

    pip install pytest-pycharm

Alternately check out the source code and run

    python setup.py install


Usage
-----

In pycharm choose ``run/edit configurations``. On the upper left corner, click
on the + and choose ``python``. Call it pycharm or anything you like.
As a script, choose the pytest executable (find its path using 
``which pytest``). Add script parameters if you use them.

Be sure to have the right python interpreter selected. Choose the working 
directory. Apply changes and close the window.

You can now select ``run/debug pytest`` and the debugger will stop on uncaught
exceptions.

As an example, on the command line I use the following

 .. code:: bash
 
    cd ~/project_folder
    source virtualenv/bin/activate
    # project_folder contains setup.py, the package folder and tests folder
    pytest --cov-report html --cov=my_package tests

As a consequence I put

- ``~/project_folder/virtualenv/bin/pytest`` for the script
- ``--cov-report html --cov=my_package tests`` for the parameters
- the python interpreter from the project virtual environment
- ``~/project_folder/`` for the working directory
