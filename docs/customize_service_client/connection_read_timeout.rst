.. _read-connection-timeout:

.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Setting connection and read timeouts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Python SDK uses the `Requests <http://docs.python-requests.org/en/master/>`_ library to make calls to Oracle Cloud Infrastructure services. The SDK uses the Requests `definition <http://docs.python-requests.org/en/master/user/advanced/#timeouts>`_ for connection and read timeouts.

By default, calls made to services have no connection or read timeout associated with them (i.e. it is possible to wait forever for a response). If you wish to override this default behaviour and set a timeout, you can do something similar to:

.. code-block:: python

    import oci

    config = oci.config.from_file()
    compute = oci.core.ComputeClient(config)
    
    # This will set a value of 5 seconds to the connection and read timeout
    compute.base_client.timeout = 5

    # This will set the connection timeout to 2 seconds and the read timeout to 25 seconds
    compute.base_client.timeout = (2, 25)


You can modify the ``timeout`` attribute of the ``base_client`` to customize our connection and read timeouts. This attribute takes input in the same format as `Requests <http://docs.python-requests.org/en/master/>`_ does, namely:

* A single value will be applied to both the connection and read timeouts
* If a tuple is provided then the first value is used as the connection timeout and the second as the read timeout