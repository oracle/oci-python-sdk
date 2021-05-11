.. _known-issues:

Known Issues
~~~~~~~~~~~~~~~~~~~~~~
These are the current known issues for the Python SDK.

create_job_and_wait_for_state() fails with KeyError for ResourceManagerClientCompositeOperations (versions 2.20.0 and above)
============================================================================================================================
`ResourceManagerClientCompositeOperations.create_job_and_wait_for_state() <https://docs.cloud.oracle.com/en-us/iaas/tools/python/latest/api/resource_manager/client/oci.resource_manager.ResourceManagerClientCompositeOperations.html#oci.resource_manager.ResourceManagerClientCompositeOperations.create_stack_and_wait_for_state>`_ fails with KeyError: 'opc-work-request-id'.

**Workaround:** Use `create_stack() <https://docs.cloud.oracle.com/en-us/iaas/tools/python/latest/api/resource_manager/client/oci.resource_manager.ResourceManagerClient.html#oci.resource_manager.ResourceManagerClient.create_stack>`_ and then implement `waiters <https://docs.cloud.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html#oci.wait_until>`_. You can find an example to use waiters `here <https://github.com/oracle/oci-python-sdk/blob/master/examples/wait_for_resource_in_state.py>`_.

UploadManager.upload_stream() raises MultipartUploadError in oci v2.23.2
========================================================================
`UploadManager.upload_stream() <https://docs.cloud.oracle.com/en-us/iaas/tools/python/latest/api/upload_manager.html#oci.object_storage.UploadManager.upload_stream>`_ raises MultipartUploadError when a timeout is set on the underlying object storage client, and the operation takes more than the read timeout to complete. Prior to v2.23.2, we were overwriting the timeout to None in the operations (please see this `known issue <https://docs.cloud.oracle.com/en-us/iaas/tools/python/latest/known-issues.html#uploadmanager-generates-ssl3-write-pending-error-when-a-read-timeout-is-set-for-the-object-storage-client>`_). The default timeout is a read timeout of 60 seconds, hence this scenario will be triggered by default in v2.23.2 on any use of this operation where the operation takes 60 or more seconds to complete.
You can work around the issue by explicitly setting the timeout to None. For example,

.. code-block:: python

    client.base_client.timeout = None

This issue has been fixed in oci v2.23.3

UploadManager generates ssl3_write_pending error when a read timeout is set for the Object Storage client
=========================================================================================================
**Update:** This issue has partially been fixed in v2.23.2. This issue still may exist with using Python versions < 2.7.9. If you do encounter this issue, please consult the workaround mentioned below.

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

Some BlockStorage composite operations throw a 404/NotAuthorizedOrNotFound for Cross Region operations
======================================================================================================
**Details:** The copy_boot_volume_backup_and_wait_for_state() and copy_volume_backup_and_wait_for_state() from the BlockStorage Client Composite operations throw a 404/NotAuthorizedOrNotFound when copying a backup from one region to another even though the operation succeeds eventually.

**Impacted Versions:** All

**Workaround:** Instead of using the composite operations, use two different clients for this operation; one client in the Source Region to send the request for copying the backup from Region A to Region B, and a second client in Destination region to wait for the backup to become available. See `this <https://github.com/oracle/oci-python-sdk/blob/master/examples/copy_volume_backup_example.py>`_ for an example.

**Direct link to this issue:** `Some BlockStorage composite operations throw a 404/NotAuthorizedOrNotFound for Cross Region operations <https://github.com/oracle/oci-python-sdk/issues/344>`_