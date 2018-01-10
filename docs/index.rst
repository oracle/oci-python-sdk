.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Oracle Cloud Infrastructure Python SDK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the public Python SDK for Oracle Cloud Infrastructure.  Python 2.7+ and 3.5+ are supported.


.. code-block:: pycon

    >>> import oci
    >>> config = oci.config.from_file(
    ...     "~/.oci/config",
    ...     "integ-beta-profile")
    >>> identity = oci.identity.IdentityClient(config)
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

**Note**: The ``oraclebmc`` package is deprecated and will no longer be maintained starting March 2018. Please check the :ref:`Backward Compatibility <backward-compatibility>` section if you are using ``oraclebmc``.

.. toctree::
    :hidden:
    :maxdepth: 2

    installation
    configuration
    forward-compatibility
    backward-compatibility
    quickstart
    logging
    parallel-ops
    pass-explicit-null
    upload-manager
    raw-requests
    waiters
    pagination
    api/index
    contributions
    notifications
    license
    feedback
