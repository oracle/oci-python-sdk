.. _exception-handling:

Exception handling
~~~~~~~~~~~~~~~~~~~~~~
When using the Python SDK, you should be prepared to handle the following exceptions:

* Any response received by the SDK with a non-2xx HTTP status will be thrown as a :py:class:`~oci.exceptions.ServiceError`
* A ``ValueError`` will be thrown if you provide invalid parameters to a method call or when setting an attribute. For example:

  * When setting an attribute on a model and that attribute has a constrained set of values, such as :py:attr:`~oci.core.models.CreatePublicIpDetails.lifetime` on ``CreatePublicIpDetails``
  * When passing a blank string as the identifier for a ``get_`` operation, such as passing a nil ``instance_id`` to :py:meth:`~oci.core.compute_client.ComputeClient.get_instance`

* :py:class:`~oci.exceptions.ClientError` and its subclasses. These exceptions are raised when there is an error with your configuration file or when using the :py:meth:`~oci.wait_until` function
  
  * :py:class:`~oci.exceptions.ConfigFileNotFound`
  * :py:class:`~oci.exceptions.InvalidConfig`
  * :py:class:`~oci.exceptions.InvalidPrivateKey`
  * :py:class:`~oci.exceptions.MissingPrivateKeyPassphrase`
  * :py:class:`~oci.exceptions.ProfileNotFound`
  * :py:class:`~oci.exceptions.WaitUntilNotSupported`
  * :py:class:`~oci.exceptions.MaximumWaitTimeExceeded`

* If you use the :py:class:`~oci.object_storage.UploadManager` then you should also catch :py:class:`~oci.exceptions.MultipartUploadError`

* If you use any of the ``CompositeOperation`` classes in the SDK (e.g. :py:class:`~oci.core.ComputeClientCompositeOperations`) then you should also catch :py:class:`~oci.exceptions.CompositeOperationError`

* The Python SDK uses the `Requests <http://docs.python-requests.org/en/master/>`_ library to make calls to Oracle Cloud Infrastructure services but it does not mask or wrap any of the errors originating from this library, so you should also account for these in your code. The exception reference for Requests can be found `here <http://docs.python-requests.org/en/master/_modules/requests/exceptions/>`__ and `here <http://docs.python-requests.org/en/master/api/#exceptions>`__

Handling HTTP 3xx responses
============================
As a result of the SDK treating responses with a non-2xx HTTP status as a :py:class:`~oci.exceptions.ServiceError` the SDK will throw a :py:class:`~oci.exceptions.ServiceError` on 3xx responses. This can impact operations which support conditional GETs, such as :py:meth:`~oci.object_storage.object_storage_client.ObjectStorageClient.get_object` and :py:meth:`~oci.object_storage.object_storage_client.ObjectStorageClient.head_object` methods as these can return responses with a HTTP status code of 304 if passed an ``if_none_match`` which corresponds to the curent etag of the object or bucket.

In order to account for this, you should catch :py:class:`~oci.exceptions.ServiceError` and check its ``status`` attribute for the HTTP status code. For example: 

.. code-block:: python

    import oci
    
    config = oci.config.from_file()
    client = oci.object_storage.ObjectStorageClient(config)

    try:
        get_object_response = client.get_object('my_namespace', 'my_bucket', 'my_object', if_none_match='some_etag_value')
    except oci.exceptions.ServiceError as e:
        if e.status == 304:
            # Object exists but has not been modified (based on the etag value)
            pass
        else:
            raise
