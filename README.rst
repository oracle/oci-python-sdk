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

The project is open source and maintained by Oracle Corp. The home page for the project is `here`__.

__ https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/index.html

============
Installation
============

::

    pip install oraclebmc


See `the installation guide`__ for installation troubleshooting and alternative install methods.

__ https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/installation.html

========
Examples
========

Examples can be found `here`__.

__ https://github.com/oracle/bmcs-python-sdk/blob/master/examples/

=============
Documentation
=============

Full documentation, including prerequisites and installation and configuration instructions, can be found `here`__.

API reference can be found `here`__.

__ https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/index.html
__ https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/api/index.html

====
Help
====

See the “Questions or Feedback” section `here`__.

__ https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/feedback.html

=======
Changes
=======

See `CHANGELOG`__.

__ https://github.com/oracle/bmcs-python-sdk/blob/master/CHANGELOG.rst

============
Contributing
============

bmcs-python-sdk is an open source project. See `CONTRIBUTING`__ for details.

Oracle gratefully acknowledges the contributions to bmcs-python-sdk that have been made by the community.

__ https://github.com/oracle/bmcs-python-sdk/blob/master/CONTRIBUTING.rst

============
Known Issues
============

You can find information on any known issues with the SDK `here`__ and under the “Issues” tab of this
project's `GitHub repository`__.

__ https://docs.us-phoenix-1.oraclecloud.com/Content/knownissues.htm
__ https://github.com/oracle/bmcs-python-sdk

=======
License
=======

Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

This SDK and sample is dual licensed under the Universal Permissive License 1.0 and the Apache License 2.0.

See `LICENSE`__ for more details.

__ https://github.com/oracle/bmcs-python-sdk/blob/master/LICENSE.txt
