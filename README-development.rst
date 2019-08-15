============
Development
============

The target audience for this README is developers wanting to contribute to the
SDK.  If you wish to use the SDK with your own programs, please see
README.rst

Getting Started
===============
Assuming that you have Python and `virtualenv` installed, set up your environment and install the required dependencies like this:

.. code-block:: sh

    git clone https://github.com/oracle/oci-python-sdk.git
    cd oci-python-sdk
    virtualenv oci-python-sdk-env
    . oci-python-sdk-env/bin/activate
    pip install -r requirements.txt
    pip install -e .

You should also set up your configuration files as described `here`__

__ https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/sdkconfig.htm

Running Tests
=============
The SDK uses `pytest` as its test framework. You can run tests against Python 2.7, Python 3.5 and Python 3.6 using the `tox` command. Note that this requires that you have those versions of Python installed,
otherwise you must pass `-e` or run tests directly:

.. code-block:: sh

    # This will run tests against all configured Pythons in tox.ini (currently 2.7, 3.5 and 3.6). You need to have those versions installed
    tox

    # This will run tests against a specific Python versions
    tox -e py27

If you wish to run an individual test then you can run:

.. code-block:: sh

    py.test -s tests/integ/test_launch_instance_tutorial.py

Specifying a config file
------------------------

By default, the tests will look for a config file, 'config' in 'tests/resources'.
If 'tests/resources' does not exist, the tests will try attempt to use
'tests/configuration/config'.
The default profile is ``DEFAULT``.  You can change this with the
``--config-file`` and ``--config-profile`` options.

.. code-block:: sh

    # Use a different config file, still using the DEFAULT profile
    tox -- --config-file ~/.oci/config

    # Using a different profile in the default config file
    tox -- --config-profile IAD_PROFILE

A sample config file is provided 'tests/configuration/config.sample'

Specifying environment variables
--------------------------------
In addition to a valid config file for your tenancy, the tests also require the following environment
variables to be set:

    * ``OCI_PYSDK_PUBLIC_SSH_KEY_FILE``: path to a public SSH key (.pub file) that will be given access to the instance launched in ``test_launch_instance_tutorial.py``.


Checking Style
==============
The Python SDK adheres to PEP8 style guilds and uses Flake8 to validate style.  There are some exceptions and they can
be viewed in the ``setup.cfg`` file.

If you run tox with no environment specified Flake8 will be run.  You can also run flake8 with no arguments to check
the style consistency for the whole project.  If you want to check a single file you can run flake8 with a path to the
file to check.

.. code-block:: sh
    flake8 path/to/python_file_to_check.py

If flake8 is not found, make sure you have ``requirements.txt`` installed into your virtualenv.  See the
"Getting Started" section.


Generating Documentation
========================
Sphinx is used for documentation. You can generate HTML locally with the following:

.. code-block:: sh

    pip install -r requirements.txt
    cd docs
    make html

Generating the wheel
====================
The SDK is packaged as a wheel. In order to generate the wheel you can run:

.. code-block:: sh

    python setup.py sdist bdist_wheel

This wheel can then be installed via `pip`.