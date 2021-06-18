Oracle Cloud Infrastructure Python SDK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

=====
About
=====

This is the Python SDK for Oracle Cloud Infrastructure. Python 3.6, 3.7, 3.8 and 3.9 are supported.

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

__ https://docs.oracle.com/en-us/iaas/tools/python/latest/index.html

============
Installation
============

It is highly recommended that a Python virtual environment be used when installing oci.

Please consult the `Installing packages using pip and virtualenv`__ guide from the Python Software Foundation for more information about virtual environments.

__ https://packaging.python.org/guides/installing-using-pip-and-virtualenv/

See `the installation guide`__ for installation troubleshooting and alternative install methods.

__ https://docs.oracle.com/en-us/iaas/tools/python/latest/installation.html

Once your virtual environment is active, oci can be installed using pip.

::

    pip install oci


============
Development
============

See the `development readme`__ for information on how to make changes, run tests and build the documentation and wheel for the Python SDK.

__ https://github.com/oracle/oci-python-sdk/blob/master/README-development.rst

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

__ https://docs.oracle.com/en-us/iaas/tools/python/latest/index.html
__ https://docs.oracle.com/en-us/iaas/tools/python/latest/api/landing.html

A downloadable version of the documentation is include with in the release zip, which can be found `here`__.

__ https://github.com/oracle/oci-python-sdk/releases

====
Help
====

See the “Questions or Feedback” section `here`__.

__ https://docs.oracle.com/en-us/iaas/tools/python/latest/feedback.html

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

__ https://docs.cloud.oracle.com/Content/knownissues.htm
__ https://github.com/oracle/oci-python-sdk

=======
Survey
=======

Are you a Developer using the OCI SDK? If so, please fill out our survey to help us make the OCI SDK better for you.
Click `here`__ for the survey page.

__ https://oracle.questionpro.com/t/APeMlZka26?custom3=pypi

=======
License
=======

Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

See `LICENSE`__ for more details.

__ https://github.com/oracle/oci-python-sdk/blob/master/LICENSE.txt
