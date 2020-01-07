.. _known-issues:

Known Issues
~~~~~~~~~~~~~~~~~~~~~~
These are the current known issues for the Python SDK.

UploadManager generates ssl3_write_pending error when a read timeout is set for the Object Storage client
=========================================================================================================
**Details:** UploadManager generates the following error when a read timeout is set for the Object Storage client.

.. code-block:: python

    OpenSSL.SSL.Error: [('SSL routines', 'ssl3_write_pending', 'bad write retry')]

**Workaround:** Do not set the read timeout for the Object Storage client. There are a two ways to do so:

- Create an Object Storage client without setting a timeout. 
- Clear the timeout on an already initialized Object Storage client by setting the timeout of the base_client to ``None``.

.. code-block:: python

    client.base_client.timeout = None

If you need to retain the connection timeout while clearing the read timeout, you can do so by setting the timeout to a tuple. The first item in the tuple is the connection timeout and the second is the read timeout. In the following example, the connection timeout is set to 90.0 seconds and the read timeout is set to infinite, or no timeout.

.. code-block:: python

    client.base_client.timeout = (90.0, None)


Potential data corruption with Python SDK on binary upload
==========================================================

**Details:** When using the Python SDK to perform binary upload operations you may encounter an issue with data corruption if retries are enabled or if you are using UploadManager.upload_file.

**Workaround:** We are aware of the issue and working on a resolution. For more information about this issue and workarounds, see `Potential data corruption issue for PythonSDK retry on binary data upload <https://github.com/oracle/oci-python-sdk/issues/203/>`_.

**Direct link to this issue:** `Potential data corruption with Python SDK on binary upload <https://preview.oci.oraclecorp.com/iaas/Content/knownissues.htm?bundle=joPythonKnownIssue#pythonDataCorrupt>`_.