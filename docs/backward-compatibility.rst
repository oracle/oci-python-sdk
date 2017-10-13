.. _backward-compatibility:

.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Backward Compatibility
~~~~~~~~~~~~~~~~~~~~~~
The top level namespace / package name for the Python SDK has been changed from ``oraclebmc`` to ``oci``, so all of the documentation now references ``oci``. If you are using the ``oraclebmc`` package you should continue to reference ``oraclebmc`` in your code and when interpreting the documentation you should replace ``oci`` with ``oraclebmc`` (i.e. if there is a class defined in the docs as ``oci.base_client.BaseClient`` in the oraclebmc package this class will be called ``oraclebmc.base_client.BaseClient``).

**Note**: The ``oraclebmc`` package is deprecated and will no longer be maintained starting March 2018. Please upgrade to the ``oci`` package to avoid interruption at that time.