Public Python SDK
^^^^^^^^^^^^^^^^^

- Run all tests with 'python -m unittest discover'
- Run a single test class with 'python -m unittest tests.<class name>'
- Build whl with build.sh.

Setting up the development environment
======================================

Virtual Environments And You
----------------------------

You should really be using pyenv_ with pyenv-virtualenv_.  If you don't think
you need a virtual environment and can skip all of this silliness, best of luck
:)

Before you start, see `common build problems`_ to grab the necessary dependencies based on your OS.

.. _pyenv: https://github.com/yyuu/pyenv#installation
.. _pyenv-virtualenv: https://github.com/yyuu/pyenv-virtualenv#installation
.. _common build problems: https://github.com/yyuu/pyenv/wiki/Common-build-problems

Make sure to set up auto completion for both pyenv and pyenv-virtualenv.

::

    # Run once to install the python versions we test against
    pyenv install 2.7.12
    pyenv install 3.5.1
    
    # Create new virtual environments for sdk-specific work:
    pyenv virtualenv 2.7.12 sdk-2
    pyenv virtualenv 3.5.1 sdk-3
    
    # Set pyenv to use these virtualenvs when you're running commands from
    # the project or any subdirectory
    pyenv local sdk-3 sdk-2
    
    # Update pip if necessary, in both pythons
    pip3 install -U pip
    pip2 install -U pip


Using ``pyenv local`` told pyenv that within this directory and subdirectories, only the sdk-2
and sdk-3 venvs should be exposed.  This will keep you from accidentally installing or mucking
around with the system-wide 2.7.12 and 3.5.1 environments.

To run commands with specifically the py2 or py3 venv, use ``pyenv shell`` as such::

    pyenv shell sdk-2

Now any script, such as ``py.test``, will pull from ``sdk-2``, even though
``sdk-3`` is listed first in ``.python-version``.

Dependencies
------------

You'll need to do this with both venvs.  Set the shell venv and run the
following commands, then swap the shell venv and run them again.  For
the venvs defined above, this would mean first using ``pyenv shell sdk-2``
and then after setting up dependencies, running ``pyenv shell sdk-3`` and
repeating those steps.

Tell pip that this is an editable package::

    pip install -e .

Install development-only dependencies::

    pip install -r requirements.txt

Running the tests
=================

To run the full suite of tests against all tox environments (currently
this is just Python 3.5.1 but will soon include Python 2.7.11)::

    tox

To run a single test with your local virtual environment (that is,
whatever environment is used by your interpreter, and not a tox env)::

    py.test tests/test_file.py::test_name

Building the SDK
================

Because we are (will be) using a shared codebase for 2.7 and 3.5+, you
can generate the wheel with either venv and ``setup.cfg`` ensures the
resulting wheel is marked as 2.7 and 3.5 compatible.

::

    python setup.py sdist bdist_wheel

Our release process doesn't use the internal pypi endpoint yet, so we
can't use the usual ``python setup.py ... upload`` but instead use a
maven-based process.

This will hopefully change in the near future.