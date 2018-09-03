===============================
pytest-pycharm
===============================

.. image:: https://badge.fury.io/py/pytest-pycharm.png
    :target: http://badge.fury.io/py/pytest-pycharm

Plugin for ``pytest`` to enter PyCharm debugger on uncaught exceptions

* Free software: BSD license

Features
--------

* Uncaught exceptions in ``pytest`` test cases will trigger the PyCharm
  debugger


Installation
------------

You can install the plugin by running

    pip install pytest-pycharm

Alternately check out the source code and run

    python setup.py install


Usage
-----

You are ready to go right after the plugin installation. Execute any test in
PyCharm by right-clicking on a test and selecting *Debug pytest in ...*. The
debugger will pause on a false assertion (see `test example`_).

The plugin also works with custom ``pytest`` Run Configurations:
*Run | Edit Configurations | Add New Configuration | Python tests | pytest*.

**Note:** make sure the Run Configuration uses the correct interpreter with
``pytest-pycharm`` installed.

.. _test example: test_dummy.py
