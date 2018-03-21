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

* The Python SDK uses the `Requests <http://docs.python-requests.org/en/master/>`_ library to make calls to OCI services but it does not mask or wrap any of the errors originating from this library, so you should also account for these in your code. The exception reference for Requests can be found `here <http://docs.python-requests.org/en/master/_modules/requests/exceptions/>`__ and `here <http://docs.python-requests.org/en/master/api/#exceptions>`__