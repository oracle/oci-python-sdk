.. _configuration:

.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Configuration
~~~~~~~~~~~~~

oci uses a simple dict to build clients and other components.  You can build these manually, or oci can
parse and validate a config file.

Using the default configuration location ``~/.oci/config`` you can use
:func:`config.from_file() <oci.config.from_file>` to load any profile.  By default, the ``DEFAULT`` profile
is used:

.. code-block:: pycon

    >>> from oci.config import from_file
    >>> config = from_file()

    # Using a different profile from the default location
    >>> config = from_file(profile_name="integ-beta")

    # Using the default profile from a different file
    >>> config = from_file(file_location="~/.oci/config.prod")

Since ``config`` is a dict, you can also build it manually and check it with
:func:`config.validate_config() <oci.config.validate_config>`:

.. code-block:: python

    # Please check https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm
    # for help on how to generate a key-pair and calculate the key fingerprint.

    config = {
        "user": "<your_user_ocid>",
        "key_file": "<full_path_to_your_private_key>",
        "fingerprint": "<fingerprint_of_your_public_key>",
        "tenancy": "<your_tenancy_ocid>",
        "region": "<your_oci_region>"
    }

    from oci.config import validate_config
    validate_config(config)

If you want to use the private key which is not in the key file, key_content can be the backup of key_file:

.. code-block:: python

    # Please check https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm
    # for help on how to generate a key-pair and calculate the key fingerprint.

    config = {
        "user": "<your_user_ocid>",
        "key_content": "<content_of_the_private_key_not_in_key_file>",
        "fingerprint": "<fingerprint_of_your_public_key>",
        "tenancy": "<your_tenancy_ocid>",
        "region": "<your_oci_region>"
    }

    from oci.config import validate_config
    validate_config(config)

.. seealso::

    The `SDK and Tool Configuration`__ page has a full description of the required and supported options.
    These are supported across the OCI SDKs, so if you've already set this file up for any of the SDKs,
    you're all set.

    __ https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm