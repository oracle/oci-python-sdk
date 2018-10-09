.. _sdk-with-proxy:

.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Using the SDK with a proxy server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Python SDK uses the `Requests <http://docs.python-requests.org/en/master/>`_ library to make calls to Oracle Cloud Infrastructure services. If your environment requires you to use a proxy server for outgoing HTTP requests 
then you can set this up in the following ways:

* Configuring environment variable as described `here <http://docs.python-requests.org/en/master/user/advanced/#proxies>`_
* Modifying the underlying Requests `Session <http://docs.python-requests.org/en/master/api/#request-sessions>`_ object for a service client

In order to modify the underlying Session object, you can do something similar to:

.. code-block:: python

    import oci

    config = oci.config.from_file()
    compute = oci.core.ComputeClient(config)

    compute.base_client.session.proxies = { 'https': 'proxy.example.org:80' }

The key parts are that the underlying Session object can be accessed via ``base_client.session`` and we can then modify the `proxies <http://docs.python-requests.org/en/master/api/#requests.Session.proxies>`_
dictionary to add any required proxies.

If your proxy uses HTTP Basic Auth, then when setting ``base_client.session.proxies`` you can use the *http://user:password@host/* syntax to provide the username and password. For example:

.. code-block:: python

    compute.base_client.session.proxies = { 'https': 'http://myuser:mypassword@proxy.example.org:80' }