Public Python SDK
^^^^^^^^^^^^^^^^^

- Run all tests with ``tox``
- Run a single test file with ``py.test tests/unit/<test_file>.py``
- Run a single test with ``py.test tests/unit/<test_file>.py::<test_function_name>``

Required Test Files
===================

To ensure we're resolving ``~`` to the home folder correctly, the tests expect ~/.ssh/id_rsa.pem to exist.

If you don't have a key pair setup, see _How to Generate an API Signing Key: https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm#How for more details

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
    pyenv install 3.6.5

    # Ensure you're using a newer virtualenv, packaged with
    # recent versions of python, pip (3.5+, 9.0+)
    pyenv shell 3.5.1
    pip install -U pip

    # Create new virtual environments for sdk-specific work:
    pyenv virtualenv --copies 3.6.5 sdk-36
    pyenv virtualenv --copies 3.5.1 sdk-3
    pyenv virtualenv --always-copy 2.7.12 sdk-2

    # Check to see that pyenv recognizes the new virtualenvs
    # You should  something like this:
    #    2.7.12/envs/sdk-2 (created from ~/.pyenv/versions/2.7.12)
    #    3.5.1/envs/sdk-3 (created from ~/.pyenv/versions/3.5.1)
    #    3.6.5/envs/sdk-36 (created from ~/.pyenv/versions/3.6.5)
    #    sdk-2 (created from ~/.pyenv/versions/2.7.12)
    #    sdk-3 (created from ~/.pyenv/versions/3.5.1)
    #    sdk-36 (created from ~/.pyenv/versions/3.6.5)
    pyenv virtualenvs

    # Drop the shell venv
    pyenv shell --unset

    # Set pyenv to use these virtualenvs when you're running commands from
    # the project or any subdirectory
    pyenv local sdk-36 sdk-3 sdk-2

    # Update pip if necessary, in all pythons
    pip3 install -U pip
    pip2 install -U pip

    # Verify sdk-3 installed correctly
    tox -e flake8


Using ``pyenv local`` told pyenv that within this directory and subdirectories, only the sdk-2, sdk-3
and sdk-36 venvs should be exposed.  This will keep you from accidentally installing or mucking
around with the system-wide 2.7.x, 3.5.x and 3.6.x environments.

To run commands with specifically the py2 or py3 venv, use ``pyenv shell`` as such::

    pyenv shell sdk-2

Now any script, such as ``py.test``, will pull from ``sdk-2``, even though
``sdk-3`` is listed first in ``.python-version``.

Dependencies
------------

You'll need to do this with all venvs.  Set the shell venv and run the
following commands, then swap the shell venv and run them again.  For
the venvs defined above, this would mean first using ``pyenv shell sdk-2``
and then after setting up dependencies, repeating those steps in other venvs
(e.g. ``pyenv shell sdk-3`` and ``pyenv shell sdk-36``)

Tell pip that this is an editable package::

    pip install -e .

Install development-only dependencies::

    pip install -r requirements.txt
    pip install -r requirements-internal.txt


Running the tests
=================

Prerequisites::

    - Set the pass phrase for the private key (ask the SDK team for the correct pass phrase)::

        export PYTHON_TESTS_ADMIN_PASS_PHRASE='<TODO: enter pass phrase>'

    - Make sure to unset virtual environment using 'pyenv shell --unset'

Some of the tests require environment variables which can be set by running the following command::

    'source internal_resources/test_setup.sh'

If you need the environment variables for the internalbriangustafson tenant, then can can be set
by running the following command::

    `source internal_resources/test_setup_internalbriangustafson.sh`.

To run the full suite of tests against all tox environments::

    tox

To run a single test with your local virtual environment (that is,
whatever environment is used by your interpreter, and not a tox env)::

    py.test tests/test_file.py::test_name

Some tests are marked as slow. These will be run by default, but can
be skipped by specifying '--fast' when running py.test. Also,
it is recommended to run tests with the '-s' option so that stdout
from the tests is shown. Example run::

    py.test --fast -s


Specifying a config file
------------------------

By default, the tests will use the ``DEFAULT`` profile from the config file
at 'tests/resources/config'.  You can change this with the ``--config-file``
and ``--config-profile`` options::

    # Use a different config file, still using the DEFAULT profile
    tox -- --config-file ~/.oci/r2config

    # Using a different profile in the default config file
    tox -- --config-profile R2Testing

These are dynamically added by py.test when it collects tests; you can
view them with ``py.test --help`` or ``tox -- --help``.


Recording test traffic
----------------------------
The tests are intended to record traffic for later replay, so that subsequent test runs use the pre-recorded traffic
rather than hitting services each time. We use `VCR.py <http://vcrpy.readthedocs.io/en/latest/index.html>`_ in order to
do this.

Of the `recording modes <http://vcrpy.readthedocs.io/en/latest/usage.html#record-modes>`_ offered by VCR, we use ``once``
by default. 

When doing builds, since we assume the previously recorded traffic to be good, we use the ``none`` record mode.

If you need to re-record traffic then you can do by deleting the cassettes and using the ``once`` mode. You should
re-record traffic when:

* You add new tests
* You modify an existing test to make additional service calls
* An existing model changes (e.g. new fields are added to the Instance model) since this impacts the data which can get sent over the wire and how we serialise/deserialise it

**Note:** We have a Team City job which re-records tests.  It doesn't update the pre-recorded traffic in source control yet so that has to be done manually.

If you need to pass a record mode when running py.test, use the ``--vcr-record-mode`` option. For example::

    py.test -s --vcr-record-mode=once

If you need to do it under tox, then this becomes::

    tox -e py35 -- --vcr-record-mode=once

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

Running Tests Against IAD
==========================

By default the tests will run against PHX.  In order to run the tests against IAD you have to change a few
parameters as well as some values that are hardcoded in the tests.

To run the tests using the 'IAD' profile in tests/resources/config, you can use the '--config-profile' parameter.
For example:

::

    tox -- --config-profile IAD


You must also update the following locations in code where we are hardcoded for PHX:

* tests/integ/util.py, change the target_region to 'us-ashburn-1'
* tests/integ/test_object_storage.py, update namespace_name from 'dex-us-phoenix-1' to 'bmcs-dex-us-ashburn-1'

Running the Code Generator
===========================

You run the code generator by executing::

    mvn clean install


Note that at this time, it will execute the ``merge_and_validate_spec.py`` script, which is part of the ``coreservices-api-spec`` artifact, and execute it. As long as you are running in a virtual environment which was previously set up for the SDK you should be fine, but you may need to install the following dependencies: 

::

    pip install -r requirments-internal.txt

Adding support for new services
================================
The ``scripts/add_or_update_spec.py`` script can be used to add a new service to the SDK. An example of running this script is: 

::

  python scripts/add_or_update_spec.py --artifact-id kms-api-spec \
    --group-id com.oracle.pic.kms \
    --spec-name key_management \
    --relative-spec-path kms-api-spec-20180201.yaml \
    --endpoint https://keymanagement.{domain}/20180201 \
    --version 0.0.40 \
    --spec-generation-type PREVIEW \
    --non-regional-client \
    --regional-sub-service-overrides kms_provisioning


The script can be run as ``python scripts/add_or_update_spec.py --help`` to see a description of each option.

After you've added the service, you can run the code generator using the steps from the "Running the Code Generator" section of this readme.

Updating existing service spec versions
=========================================
Click must be installed to run add_or_update_spec.py.  Click is part of the requirements-internal.txt and will be installed with::

    pip install -r requirements-internal.txt

The ``scripts/add_or_update_spec.py`` script can be used to update the spec version of an existing service. An example of running this script is:

::

  python scripts/add_or_update_spec.py --artifact-id coreservices-api-spec --version 0.1.137


Note that we just need to provide the ``--artifact-id`` and the ``--version``
