.. _known-issues:

Known Issues
~~~~~~~~~~~~~~~~~~~~~~
These are the current known issues for the Python SDK.

UploadManager generates ssl3_write_pending error
================================================
Uploading small files with the upload_file method in UploadManager works, but uploading a large file generates an error.
