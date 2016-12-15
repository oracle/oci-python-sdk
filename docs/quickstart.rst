.. _quickstart:

Quickstart
~~~~~~~~~~

Clients only require a valid config object:

.. code-block:: pycon

    >>> from oraclebmc import clients
    >>> identity = clients.IdentityClient(config)
    >>> networking = clients.VirtualNetworkClient(config)

Next, head to the `User Guides`_ or jump right into the `API Reference`_ to explore the available operations for each
service, and their parameters.

.. code-block:: python

    # TODO: more samples here!

.. note::

    The Python SDK uses ``lowercase_with_underscores`` for operations and parameters.  For example, the
    `ListApiKeys`_ operation is called with ``IdentityClient.list_api_keys`` and its parameter
    ``userId`` is translated to ``user_id``.

    .. _ListApiKeys: https://docs.us-az-phoenix-1.oracleiaas.com/api/#/en/identity/20160918/ApiKey/ListApiKeys

.. _User Guides: https://docs.us-az-phoenix-1.oracleiaas.com/Content/services.htm
.. _API Reference: https://docs.us-az-phoenix-1.oracleiaas.com/api/
