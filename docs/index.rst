Oracle BMCS Python SDK
~~~~~~~~~~~~~~~~~~~~~~

This is the public Python SDK for Oracle Bare Metal Cloud Services.  Python 2.7+ and 3.5+ are supported.


.. code-block:: pycon

    >>> import oraclebmc
    >>> config = oraclebmc.config.from_file(
    ...     "~/.oraclebmc/config",
    ...     "integ-beta-profile")
    >>> identity = oraclebmc.identity.IdentityClient(config)
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


To get started, head over to the :ref:`installation instructions <install>` or see more examples in the
:ref:`quickstart <quickstart>` section.

.. toctree::
    :hidden:
    :maxdepth: 2

    installation
    configuration
    quickstart
    raw-requests
    api/index
    contributions
    notifications
    license
    feedback
