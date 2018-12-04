.. _known-issues:

Known Issues
~~~~~~~~~~~~~~~~~~~~~~
These are the current known issues for the Python SDK.

UploadManager generates ssl3_write_pending error
================================================
**Details:** Using :py:meth:`~oci.object_storage.UploadManager.upload_file` method to upload files larger than X generates a ``ssl3_write_pending`` error.

**Workaround:** If uploading files larger than X, do not use a timeout with the :py:class:`~oci.object_storage.UploadManager` class.