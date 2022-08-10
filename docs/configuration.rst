.. _configuration:

.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-cloud-infrastructure-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
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

    import os
    from myproject import testrunner
    user_ocid = os.environ["USER_OCID"]
    key_file = key_for(user_ocid)

    config = {
        "user": user_ocid,
        "key_file": key_file,
        "fingerprint": calc_fingerprint(key_file),
        "tenancy": testrunner.tenancy,
        "region": testrunner.region
    }

    from oci.config import validate_config
    validate_config(config)

If you want to use the private key which is not in the key file, key_content can be the backup of key_file:

.. code-block:: python

    import os
    from myproject import testrunner
    user_ocid = os.environ["USER_OCID"]

    config = {
        "user": user_ocid,
        "key_content": testrunner.key_content,
        "fingerprint": calc_fingerprint(key_content),
        "tenancy": testrunner.tenancy,
        "region": testrunner.region
    }

    from oci.config import validate_config
    validate_config(config)

.. seealso::

    The `SDK and Tool Configuration`__ page has a full description of the required and supported options.
    These are supported across the SDKs, so if you've already set this file up for the Ruby or Java SDKs,
    you're all set.

    __ https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm
