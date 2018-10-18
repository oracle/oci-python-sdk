.. _setting-custom-headers:

.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Setting custom headers
~~~~~~~~~~~~~~~~~~~~~~~
The Python SDK uses the `Requests <http://docs.python-requests.org/en/master/>`_ library to make calls to Oracle Cloud Infrastructure services. If you need to add custom headers to your calls, you can do so via modifying the underlying Requests `Session <http://docs.python-requests.org/en/master/api/#request-sessions>`_ object

.. code-block:: python

    import oci

    config = oci.config.from_file()
    compute = oci.core.ComputeClient(config)

    # Adds my-custom-header as a header in the request. This header will be included in ALL
    # subsequent calls made
    compute.base_client.session.headers['my-custom-header'] = 'my custom header value'

    # If you no longer want to send the header then remove it from the dictionary
    compute.base_client.session.headers.pop('my-custom-header')

