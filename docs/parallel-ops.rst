.. _parallel-ops:

.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Parallel Operations
~~~~~~~~~~~~~~~~~~~~~~
The Python SDK supports parallel requests to Oracle Cloud Infrastructure. For example, the `object storage upload <https://github.com/oracle/oci-python-sdk/blob/master/examples/parallel_upload_to_object_storage.py>`_ example shows how multiple processes can be used to upload files to object storage.