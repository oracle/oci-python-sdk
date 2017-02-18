.. _configuration:

Configuration
~~~~~~~~~~~~~

oraclebmc uses a simple dict to build clients and other components.  You can build these manually, or oraclebmc can
parse and validate a config file.

Using the default configuration location ``~/.oraclebmc/config`` you can use
:func:`config.from_file() <oraclebmc.config.from_file>` to load any profile.  By default, the ``DEFAULT`` profile
is used:

.. code-block:: pycon

    >>> from oraclebmc.config import from_file
    >>> config = from_file()

    # Using a different profile from the default location
    >>> config = from_file(profile_name="integ-beta")

    # Using the default profile from a different file
    >>> config = from_file(file_location="~/.oraclebmc/config.prod")

Since ``config`` is a dict, you can also build it manually and check it with
:func:`config.validate_config() <oraclebmc.config.validate_config>`:

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

    from oraclebmc.config import validate_config
    validate_config(config)

.. seealso::

    The `SDK and Tool Configuration`__ page has a full description of the required and supported options.
    These are supported across the SDKs, so if you've already set this file up for the Ruby or Java SDKs,
    you're all set.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/sdkconfig.htm