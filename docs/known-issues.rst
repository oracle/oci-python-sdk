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