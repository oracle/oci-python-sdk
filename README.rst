Oracle Bare Metal Cloud Services Python SDK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

=====
About
=====

This is the Python SDK for Oracle Bare Metal Cloud Services. Python 2.7+ and 3.5+ are supported.

.. code-block:: pycon

    >>> import oraclebmc
    # Set up config
    >>> config = oraclebmc.config.from_file(
    ...     "~/.oraclebmc/config",
    ...     "DEFAULT")
    # Create a service client
    >>> identity = oraclebmc.identity.IdentityClient(config)
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

The project is open source and maintained by Oracle Corp. The home page for the project is `here <https://docs.us-phoenix-1.oraclecloud.com/tools/python/latest/index.html>`__.

============
Installation
============

::

    pip install oraclebmc


See `the installation guide <https://docs.us-phoenix-1.oraclecloud.com/tools/python/latest/installation.html>`_ for installation troubleshooting and alternative install methods.

========
Examples
========

Examples can be found `here <https://github.com/oracle/bmcs-python-sdk/blob/master/examples/>`__.

=============
Documentation
=============

Full documentation, including prerequisites and installation and configuration instructions, can be found `here <https://docs.us-phoenix-1.oraclecloud.com/tools/python/latest/index.html>`__.

API reference can be found `here <https://docs.us-phoenix-1.oraclecloud.com/tools/python/latest/api/index.html>`__.

====
Help
====

See the “Questions or Feedback?” section `here <https://docs.us-phoenix-1.oraclecloud.com/tools/python/latest/installation.html>`_.

=======
Changes
=======

See `CHANGELOG <https://github.com/oracle/bmcs-python-sdk/blob/master/CHANGELOG.rst>`_.

============
Contributing
============

bmcs-python-sdk is an open source project. See `CONTRIBUTING <https://github.com/oracle/bmcs-python-sdk/blob/master/CONTRIBUTING.rst>`_ for details.

Oracle gratefully acknowledges the contributions to bmcs-python-sdk that have been made by the community.

============
Known Issues
============

You can find information on any known issues with the SDK `here <https://docs.us-phoenix-1.oraclecloud.com/Content/knownissues.htm>`__ and under the “Issues” tab of this project's `GitHub repository <https://github.com/oracle/bmcs-python-sdk>`_.

=======
License
=======

Copyright (c) 2016, Oracle and/or its affiliates. All rights reserved.

This SDK and sample is dual licensed under the Universal Permissive License 1.0 and the Apache License 2.0.

See `LICENSE <https://github.com/oracle/bmcs-python-sdk/blob/master/LICENSE.txt>`_ for more details.