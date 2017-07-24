.. _upload-manager:

Uploading Large Objects
~~~~~~~~~~~~~~~~~~~~~~~~

The Object Storage service supports multipart uploads to make large object uploads easier by splitting the large object into parts. The Python SDK supports multipart upload operations for advanced use cases, as well as a higher level upload class that uses the multipart upload APIs. `Managing Multipart Uploads <https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingmultipartuploads.htm>`_ provides links to the APIs used for multipart upload operations. Higher level multipart uploads are implemented using the UploadManager, which will: split a large object into parts for you, upload the parts in parallel, and then recombine and commit the parts as a single object in storage.

The `UploadObject <https://github.com/oracle/bmcs-python-sdk/blob/master/examples/multipart_object_upload.py>`_ example shows how the UploadManager can be used to upload files to object storage. 