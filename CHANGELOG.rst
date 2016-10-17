0.1.6
^^^^^

Config Loading
==============

To simplify the work of setting up config at runtime, the config validation is
performed automatically as part of creating a client.  This means you no longer
need to call ``config.from_dict(your_config)`` before creating a client.

If your config object fails to validate, ``InvalidConfig`` is raised.

For example:

    >>> import oraclebmc
    >>> invalid_config = {"user": "malformed ocid"}
    >>> oraclebmc.clients.IdentityClient(invalid_config)
    Traceback (most recent call last):
      ...
    oraclebmc.exceptions.InvalidConfig: {'user': 'malformed', 'tenancy': 'missing', ...}

* removed ``config.from_dict``
* new exception ``InvalidConfig``

0.1.5
^^^^^

(Internal) using ``pytz`` to localize response datetimes to UTC when the timezone isn't provided.

0.1.4
^^^^^

Config Loading
==============

* client config is now a dict, instead of a class
* config_file_loader moved to config.from_file

Previously, to create a client:

.. code-block:: python

    import oraclebmc

    config = oraclebmc.config_file_loader.load_config(
        file_location="~/.oraclebmc/config",
        profile_name="DEFAULT"
    )
    identity = oraclebmc.clients.identity_client.IdentityClient(config)

Now, to create a client:

.. code-block:: python

    import oraclebmc

    config = oraclebmc.config.from_file(
        file_location="~/.oraclebmc/config",
        profile_name="DEFAULT"
    )
    identity = oraclebmc.clients.identity_client.IdentityClient(config)

* new ``config.from_dict`` function for creating config at runtime
* validation includes all config failures, not just the first

Previously, to create a Config object at runtime:

.. code-block:: python

    import oraclebmc

    config = oraclebmc.Config()
    config.tenancy = "tenancy ocid"
    config.user = "user ocid"
    config.fingerprint = "fingerprint"
    config.key_file = "~/.oraclebmc/config"

The config values were never validated, which meant errors could pop up
long after you created the config object.  Additionally, there was no way to
easily unpack an existing config object into another.

Because config is now simply a dict, you can construct config with:

.. code-block:: python

    base_config = {
        "tenancy": "tenancy ocid",
        "user": "user ocid",
        "fingerprint": "fingerprint",
        "key_file": "~/.oraclebmc/config",
        # -- region is now required --
        "region": "us-phoenix-1"
    }

You can easily validate your config, and create copies with:

.. code-block:: python

    config = oraclebmc.config.from_dict(base_config)

Additionally, any optional settings that you did not specify (such as ``additional_user_agent``)
will be set from their defaults in ``oraclebmc.config.DEFAULT_CONFIG``.

Regions and Endpoints
=====================

* region no longer has a default value
* endpoints are loaded by region, and stored in ``base_client.endpoints``

Previously, the "us-phoenix-1" region was used if you did not specify one.
A default is no longer assumed, and you must provide a region.  If you are
building config objects at runtime, this means adding one new key to your
existing config dict:

.. code-block:: python
    config["region"] = "us-phoenix-1"

While there is currently one region, we want config to be explicit
about where resources should be created.  With a default, you might find
your multi-region deployment was actually entirely within us-phoenix-1
because of a typo in the config file.

The region -> endpoint mapping is now provided by ``oraclebmc.regions``.
When you specify endpoints in the config file, they will override the
endpoints for services within that region.  The overrides are scoped to
config loaded from that file, and not applied to the default region endpoints.

To override the endpoint for a service after loading it from a file:

.. code-block:: python

    config = oraclebmc.config.from_file(...)
    config["endpoints"]["identity"] = "https://identity.us-phoenix-1.oraclecloud.com/20160918"

BaseClient
==========

* new init param ``service``
* no longer has an attr ``config``
* new attr ``endpoint``
* session, user agent are built once at ``__init__``
* ``call_api`` no longer takes ``endpoint`` param

Unless you directly manipulate the ``BaseClient``, you can skip
this section.  These are mostly housekeeping, such as computing the
endpoint, session, and user agent once when the client is created.

Because the service name is passed to the BaseClient at init, it's
no longer necessary for each service client to compute its endpoint
at runtime from the full config object.  If you want to use a different
endpoint for a service, you should change the config's endpoint before
creating the endpoint.

Before:

.. code-block:: python

    client = oraclebmc.clients.identity_client.IdentityClient(config)
    config.identity_endpoint = "new endpoint"
    # or
    client.base_client.config.identity_endpoint = "new endpoint"

 Now:

.. code-block:: python

    config["endpoints"]["identity"] = "new endpoint"
    client = oraclebmc.clients.identity_client.IdentityClient(config)
    # or
    client.endpoint = "new endpoint"

0.1.3
^^^^^

Python 2.7
==========

This is the first release with beta support for Python 2.7.
There are undoubtedly some str vs bytes bugs still lurking around;
please contact us if you see any unexpected ``Unicode`` or ``Type`` Errors.

Api -> Client
=============

As part of our cross-sdk consistency efforts, the per-service
classes have been renamed from ``*Api`` to ``*Client``.  This
also changes the sub-module that the service clients are loaded from.

If you previously created an api with:

.. code-block:: python

    import oraclebmc
    config = oraclebmc.config_file_loader.load_config(...)

    identity = oraclebmc.apis.identity_api.IdentityApi(config)

you would now use:

.. code-block:: python

    import oraclebmc
    config = oraclebmc.config_file_loader.load_config(...)

    identity = oraclebmc.clients.identity_client.IdentityClient(config)
