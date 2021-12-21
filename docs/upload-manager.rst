.. _upload-manager:

.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Uploading Large Objects
~~~~~~~~~~~~~~~~~~~~~~~~

The Object Storage service supports multipart uploads to make large object uploads easier by splitting the large object into parts. The Python SDK supports raw multipart upload operations for advanced use cases, as well as a higher-level upload class that uses the multipart upload APIs. `Using Multipart Uploads <https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/usingmultipartuploads.htm>`_ provides links to the APIs used for raw multipart upload operations. Higher-level uploads can be performed using the :py:class:`~oci.object_storage.UploadManager`. The :py:class:`~oci.object_storage.UploadManager` will: split a large object into parts for you, upload the parts in parallel, and then recombine and commit the parts as a single object in Object Storage.

The `UploadObject <https://github.com/oracle/oci-python-sdk/blob/master/examples/multipart_object_upload.py>`_ example shows how :py:class:`~oci.object_storage.UploadManager` can be used to upload files to object storage.

.. warning::
    Potential data corruption with Python SDK on UploadManager.upload_stream() in FIPS mode and Cloud Shell (versions 2.53.0 and below), for more information please see :ref:`Known Issues<known-issues>` section.

.. warning::
    Potential data corruption with Python SDK on binary upload in versions 2.8.0 and below, for more information please see :ref:`Known Issues<known-issues>` section.