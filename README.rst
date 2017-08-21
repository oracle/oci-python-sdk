Oracle Cloud Infrastructure Python SDK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

=====
About
=====

This is the Python SDK for Oracle Cloud Infrastructure. Python 2.7+ and 3.5+ are supported.

.. code-block:: pycon

    >>> import oci
    # Set up config
    >>> config = oci.config.from_file(
    ...     "~/.oci/config",
    ...     "DEFAULT")
    # Create a service client
    >>> identity = oci.identity.IdentityClient(config)
    # Get the current user
    >>> user = identity.get_user(config["user"]).data
    >>> print(user)
    {
      "compartment_id": "ocid1.tenancy.oc1...",
      "description": "Test user",
      "id": "ocid1.user.oc1...",
      "inactive_status": null,
      "lifecycle_state": "ACTIVE",
      "name": "test-user@corp.com",
      "time_created": "2016-08-30T23:46:44.680000+00:00"
    }

The project is open source and maintained by Oracle Corp. The home page for the project is `here`__.

__ https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/index.html

============
Installation
============

::

    pip install oci


See `the installation guide`__ for installation troubleshooting and alternative install methods.

__ https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/installation.html

============
Development
============

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
The SDK uses `pytest` as its test framework. You can run tests against Python 2.7 Python 3.5 using the `tox` command. Note that this requires that you have those versions of Python installed, 
otherwise you must pass `-e` or run tests directly:

.. code-block:: sh

    # This will run tests against all configured Pythons in tox.ini (currently 2.7 and 3.5). You need to have those versions installed
    tox

    # This will run tests against a specific Python versions
    tox -e py27

If you wish to run an individual test then you can run:

.. code-block:: sh

    py.test -s tests/integ/test_launch_instance_tutorial.py

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

========
Examples
========

Examples can be found `here`__.

__ https://github.com/oracle/oci-python-sdk/blob/master/examples/

=============
Documentation
=============

Full documentation, including prerequisites and installation and configuration instructions, can be found `here`__.

API reference can be found `here`__.

__ https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/index.html
__ https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/api/index.html

====
Help
====

See the “Questions or Feedback” section `here`__.

__ https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/feedback.html

=======
Changes
=======

See `CHANGELOG`__.

__ https://github.com/oracle/oci-python-sdk/blob/master/CHANGELOG.rst

============
Contributing
============

oci-python-sdk is an open source project. See `CONTRIBUTING`__ for details.

Oracle gratefully acknowledges the contributions to oci-python-sdk that have been made by the community.

__ https://github.com/oracle/oci-python-sdk/blob/master/CONTRIBUTING.rst

============
Known Issues
============

You can find information on any known issues with the SDK `here`__ and under the “Issues” tab of this
project's `GitHub repository`__.

__ https://docs.us-phoenix-1.oraclecloud.com/Content/knownissues.htm
__ https://github.com/oracle/oci-python-sdk

=======
License
=======

Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

This SDK and sample is dual licensed under the Universal Permissive License 1.0 and the Apache License 2.0.

See `LICENSE`__ for more details.

__ https://github.com/oracle/oci-python-sdk/blob/master/LICENSE.txt
