.. _known-issues:

Known Issues
~~~~~~~~~~~~~~~~~~~~~~
These are the current known issues for the Python SDK.

UploadManager generates ssl3_write_pending error when a read timeout is set for the Object Storage client
=========================================================================================================
**Update:** With v2.18.0 we handle the object storage client with default timeout values (connect timeout = 10 secs and read timeout = 60 secs), by overwriting the timeout to `None` in the operations.

PLEASE NOTE that the operations are NOT thread-safe, and you should provide the UploadManager class with its own Object Storage client that isn't used elsewhere.

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


Potential data corruption with Python SDK on binary upload (versions 2.8.0 and below)
====================================================================================

**Details:** When using the Python SDK to perform binary upload operations you may encounter an issue with data corruption if retries are enabled or if you are using UploadManager.upload_file.

**Impacted Versions:** v2.8.0 and below

**Direct link to this issue:** `Potential data corruption with Python SDK on binary upload <https://github.com/oracle/oci-python-sdk/issues/203/>`_


Default timeout not getting set in the clients (versions 2.17.2 and below)
==========================================================================
The default timeout values (connect timeout = 10 secs and read timeout = 60 secs) we not getting set in the clients and remained None (infinite timeout). This has been fixed in v2.18.0.