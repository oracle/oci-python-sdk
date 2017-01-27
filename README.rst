Oracle BMCS Python SDK
~~~~~~~~~~~~~~~~~~~~~~

This is the Python SDK for Oracle Bare Metal Cloud Services (BMCS).  Python 2.7+ and 3.5+ are supported.


.. code-block:: pycon

    >>> import oraclebmc
    # Set up config
    >>> config = oraclebmc.config.from_file(
    ...     "~/.oraclebmc/config",
    ...     "integ-beta-profile")
    # Create a service client
    >>> identity = oraclebmc.identity.IdentityClient(config)
    # Get the current user
    >>> user = identity.get_user(config["user"]).data
    >>> print(user)
    {
      "compartment_id": "ocid1.tenancy.oc1...",
      "description": "Integration testing user [BETA]",
      "id": "ocid1.user.oc1...",
      "inactive_status": null,
      "lifecycle_state": "ACTIVE",
      "name": "testing+integ-beta@corp.com",
      "time_created": "2016-08-30T23:46:44.680000+00:00"
    }

==============
 Installation
==============

::

    pip install oraclebmc


Because Oracle Bare Metal Cloud uses modern security best practices including TLS 1.2, you may encounter issues when
installing or running the SDK.  Please see our full `Python Installation Guide`_ for details and troubleshooting.

.. _Python Installation Guide: https://docs.us-phoenix-1.oraclecloud.com/tools/python/latest/installation.html

===============
 Documentation
===============

You can read the full SDK documentation `here`_, which will eventually be available on ReadTheDocs.

.. _here: https://docs.us-phoenix-1.oraclecloud.com/tools/python/latest/index.html