# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry  # noqa: F401
from oci.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel, get_signer_from_authentication_type, AUTHENTICATION_TYPE_FIELD_NAME
from .models import object_storage_type_mapping
missing = Sentinel("Missing")


class ObjectStorageClient(object):
    """
    Common set of Object Storage and Archive Storage APIs for managing buckets, objects, and related resources.
    For more information, see [Overview of Object Storage](/Content/Object/Concepts/objectstorageoverview.htm) and
    [Overview of Archive Storage](/Content/Archive/Concepts/archivestorageoverview.htm).
    """

    def __init__(self, config, **kwargs):
        """
        Creates a new service client

        :param dict config:
            Configuration keys and values as per `SDK and Tool Configuration <https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm>`__.
            The :py:meth:`~oci.config.from_file` method can be used to load configuration from a file. Alternatively, a ``dict`` can be passed. You can validate_config
            the dict using :py:meth:`~oci.config.validate_config`

        :param str service_endpoint: (optional)
            The endpoint of the service to call using this client. For example ``https://iaas.us-ashburn-1.oraclecloud.com``. If this keyword argument is
            not provided then it will be derived using the region in the config parameter. You should only provide this keyword argument if you have an explicit
            need to specify a service endpoint.

        :param timeout: (optional)
            The connection and read timeouts for the client. The default values are connection timeout 10 seconds and read timeout 60 seconds. This keyword argument can be provided
            as a single float, in which case the value provided is used for both the read and connection timeouts, or as a tuple of two floats. If
            a tuple is provided then the first value is used as the connection timeout and the second value as the read timeout.
        :type timeout: float or tuple(float, float)

        :param signer: (optional)
            The signer to use when signing requests made by the service client. The default is to use a :py:class:`~oci.signer.Signer` based on the values
            provided in the config parameter.

            One use case for this parameter is for `Instance Principals authentication <https://docs.cloud.oracle.com/Content/Identity/Tasks/callingservicesfrominstances.htm>`__
            by passing an instance of :py:class:`~oci.auth.signers.InstancePrincipalsSecurityTokenSigner` as the value for this keyword argument
        :type signer: :py:class:`~oci.signer.AbstractBaseSigner`

        :param obj retry_strategy: (optional)
            A retry strategy to apply to all calls made by this service client (i.e. at the client level). There is no retry strategy applied by default.
            Retry strategies can also be applied at the operation level by passing a ``retry_strategy`` keyword argument as part of calling the operation.
            Any value provided at the operation level will override whatever is specified at the client level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.
        """
        validate_config(config, signer=kwargs.get('signer'))
        if 'signer' in kwargs:
            signer = kwargs['signer']

        elif AUTHENTICATION_TYPE_FIELD_NAME in config:
            signer = get_signer_from_authentication_type(config)

        else:
            signer = Signer(
                tenancy=config["tenancy"],
                user=config["user"],
                fingerprint=config["fingerprint"],
                private_key_file_location=config.get("key_file"),
                pass_phrase=get_config_value_or_default(config, "pass_phrase"),
                private_key_content=config.get("key_content")
            )

        base_client_init_kwargs = {
            'regional_client': True,
            'service_endpoint': kwargs.get('service_endpoint'),
            'timeout': kwargs.get('timeout'),
            'base_path': '/',
            'service_endpoint_template': 'https://objectstorage.{region}.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False)
        }
        self.base_client = BaseClient("object_storage", config, signer, object_storage_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')

    def abort_multipart_upload(self, namespace_name, bucket_name, object_name, upload_id, **kwargs):
        """
        Aborts an in-progress multipart upload and deletes all parts that have been uploaded.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param str upload_id: (required)
            The upload ID for a multipart upload.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u/{objectName}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "abort_multipart_upload got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "uploadId": upload_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)

    def cancel_work_request(self, work_request_id, **kwargs):
        """
        Cancels a work request.


        :param str work_request_id: (required)
            The ID of the asynchronous request.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workRequests/{workRequestId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "cancel_work_request got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workRequestId": work_request_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def commit_multipart_upload(self, namespace_name, bucket_name, object_name, upload_id, commit_multipart_upload_details, **kwargs):
        """
        Commits a multipart upload, which involves checking part numbers and entity tags (ETags) of the parts, to create an aggregate object.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param str upload_id: (required)
            The upload ID for a multipart upload.

        :param oci.object_storage.models.CommitMultipartUploadDetails commit_multipart_upload_details: (required)
            The part numbers and entity tags (ETags) for the parts you want to commit.

        :param str if_match: (optional)
            The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object
            already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a
            part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u/{objectName}"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "if_none_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "commit_multipart_upload got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "uploadId": upload_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=commit_multipart_upload_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=commit_multipart_upload_details)

    def copy_object(self, namespace_name, bucket_name, copy_object_details, **kwargs):
        """
        Creates a request to copy an object within a region or to another region.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param oci.object_storage.models.CopyObjectDetails copy_object_details: (required)
            The source and destination of the object to be copied.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str opc_sse_customer_algorithm: (optional)
            The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param str opc_sse_customer_key: (optional)
            The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or
            decrypt the data. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param str opc_sse_customer_key_sha256: (optional)
            The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This
            value is used to check the integrity of the encryption key. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param str opc_source_sse_customer_algorithm: (optional)
            The optional header that specifies \"AES256\" as the encryption algorithm to use to decrypt the source
            object. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param str opc_source_sse_customer_key: (optional)
            The optional header that specifies the base64-encoded 256-bit encryption key to use to decrypt
            the source object. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param str opc_source_sse_customer_key_sha256: (optional)
            The optional header that specifies the base64-encoded SHA256 hash of the encryption key used to
            decrypt the source object. This value is used to check the integrity of the encryption key. For
            more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/actions/copyObject"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id",
            "opc_sse_customer_algorithm",
            "opc_sse_customer_key",
            "opc_sse_customer_key_sha256",
            "opc_source_sse_customer_algorithm",
            "opc_source_sse_customer_key",
            "opc_source_sse_customer_key_sha256"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "copy_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing),
            "opc-sse-customer-algorithm": kwargs.get("opc_sse_customer_algorithm", missing),
            "opc-sse-customer-key": kwargs.get("opc_sse_customer_key", missing),
            "opc-sse-customer-key-sha256": kwargs.get("opc_sse_customer_key_sha256", missing),
            "opc-source-sse-customer-algorithm": kwargs.get("opc_source_sse_customer_algorithm", missing),
            "opc-source-sse-customer-key": kwargs.get("opc_source_sse_customer_key", missing),
            "opc-source-sse-customer-key-sha256": kwargs.get("opc_source_sse_customer_key_sha256", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=copy_object_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=copy_object_details)

    def create_bucket(self, namespace_name, create_bucket_details, **kwargs):
        """
        Creates a bucket in the given namespace with a bucket name and optional user-defined metadata. Avoid entering
        confidential information in bucket names.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param oci.object_storage.models.CreateBucketDetails create_bucket_details: (required)
            Request object for creating a bucket.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.Bucket`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_bucket_details,
                response_type="Bucket")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_bucket_details,
                response_type="Bucket")

    def create_multipart_upload(self, namespace_name, bucket_name, create_multipart_upload_details, **kwargs):
        """
        Starts a new multipart upload to a specific object in the given bucket in the given namespace.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param oci.object_storage.models.CreateMultipartUploadDetails create_multipart_upload_details: (required)
            Request object for creating a multipart upload.

        :param str if_match: (optional)
            The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object
            already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a
            part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str opc_sse_customer_algorithm: (optional)
            The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param str opc_sse_customer_key: (optional)
            The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or
            decrypt the data. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param str opc_sse_customer_key_sha256: (optional)
            The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This
            value is used to check the integrity of the encryption key. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.MultipartUpload`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "if_none_match",
            "opc_client_request_id",
            "opc_sse_customer_algorithm",
            "opc_sse_customer_key",
            "opc_sse_customer_key_sha256"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_multipart_upload got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing),
            "opc-sse-customer-algorithm": kwargs.get("opc_sse_customer_algorithm", missing),
            "opc-sse-customer-key": kwargs.get("opc_sse_customer_key", missing),
            "opc-sse-customer-key-sha256": kwargs.get("opc_sse_customer_key_sha256", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_multipart_upload_details,
                response_type="MultipartUpload")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_multipart_upload_details,
                response_type="MultipartUpload")

    def create_preauthenticated_request(self, namespace_name, bucket_name, create_preauthenticated_request_details, **kwargs):
        """
        Creates a pre-authenticated request specific to the bucket.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param oci.object_storage.models.CreatePreauthenticatedRequestDetails create_preauthenticated_request_details: (required)
            Information needed to create the pre-authenticated request.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.PreauthenticatedRequest`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/p"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_preauthenticated_request got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_preauthenticated_request_details,
                response_type="PreauthenticatedRequest")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_preauthenticated_request_details,
                response_type="PreauthenticatedRequest")

    def create_replication_policy(self, namespace_name, bucket_name, create_replication_policy_details, **kwargs):
        """
        Creates a replication policy for the specified bucket.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param oci.object_storage.models.CreateReplicationPolicyDetails create_replication_policy_details: (required)
            The replication policy.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.ReplicationPolicy`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/replicationPolicies"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_replication_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_replication_policy_details,
                response_type="ReplicationPolicy")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_replication_policy_details,
                response_type="ReplicationPolicy")

    def create_retention_rule(self, namespace_name, bucket_name, create_retention_rule_details, **kwargs):
        """
        Creates a new retention rule in the specified bucket. The new rule will take effect typically within 30 seconds.
        Note that a maximum of 100 rules are supported on a bucket.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param oci.object_storage.models.CreateRetentionRuleDetails create_retention_rule_details: (required)
            The retention rule to create for the bucket.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.RetentionRule`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/retentionRules"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_retention_rule got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_retention_rule_details,
                response_type="RetentionRule")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_retention_rule_details,
                response_type="RetentionRule")

    def delete_bucket(self, namespace_name, bucket_name, **kwargs):
        """
        Deletes a bucket if the bucket is already empty. If the bucket is not empty, use
        :func:`delete_object` first. In addition,
        you cannot delete a bucket that has a multipart upload in progress or a pre-authenticated
        request associated with that bucket.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str if_match: (optional)
            The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_object(self, namespace_name, bucket_name, object_name, **kwargs):
        """
        Deletes an object.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param str if_match: (optional)
            The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str version_id: (optional)
            VersionId used to identify a particular version of the object

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/o/{objectName}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_client_request_id",
            "version_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "versionId": kwargs.get("version_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)

    def delete_object_lifecycle_policy(self, namespace_name, bucket_name, **kwargs):
        """
        Deletes the object lifecycle policy for the bucket.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str if_match: (optional)
            The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/l"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_object_lifecycle_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_preauthenticated_request(self, namespace_name, bucket_name, par_id, **kwargs):
        """
        Deletes the pre-authenticated request for the bucket.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str par_id: (required)
            The unique identifier for the pre-authenticated request. This can be used to manage operations against
            the pre-authenticated request, such as GET or DELETE.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/p/{parId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_preauthenticated_request got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "parId": par_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_replication_policy(self, namespace_name, bucket_name, replication_id, **kwargs):
        """
        Deletes the replication policy associated with the source bucket.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str replication_id: (required)
            The ID of the replication policy.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/replicationPolicies/{replicationId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_replication_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "replicationId": replication_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_retention_rule(self, namespace_name, bucket_name, retention_rule_id, **kwargs):
        """
        Deletes the specified rule. The deletion takes effect typically within 30 seconds.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str retention_rule_id: (required)
            The ID of the retention rule.

        :param str if_match: (optional)
            The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/retentionRules/{retentionRuleId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_retention_rule got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "retentionRuleId": retention_rule_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def get_bucket(self, namespace_name, bucket_name, **kwargs):
        """
        Gets the current representation of the given bucket in the given Object Storage namespace.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str if_match: (optional)
            The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object
            already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a
            part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param list[str] fields: (optional)
            Bucket summary includes the 'namespace', 'name', 'compartmentId', 'createdBy', 'timeCreated',
            and 'etag' fields. This parameter can also include 'approximateCount' (approximate number of objects) and 'approximateSize'
            (total approximate size in bytes of all objects). For example 'approximateCount,approximateSize'.

            Allowed values are: "approximateCount", "approximateSize"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.Bucket`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "if_none_match",
            "opc_client_request_id",
            "fields"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'fields' in kwargs:
            fields_allowed_values = ["approximateCount", "approximateSize"]
            for fields_item in kwargs['fields']:
                if fields_item not in fields_allowed_values:
                    raise ValueError(
                        "Invalid value for `fields`, must be one of {0}".format(fields_allowed_values)
                    )

        query_params = {
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'csv')
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="Bucket")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="Bucket")

    def get_namespace(self, **kwargs):
        """
        Each Oracle Cloud Infrastructure tenant is assigned one unique and uneditable Object Storage namespace. The namespace
        is a system-generated string assigned during account creation. For some older tenancies, the namespace string may be
        the tenancy name in all lower-case letters. You cannot edit a namespace.

        GetNamespace returns the name of the Object Storage namespace for the user making the request.
        If an optional compartmentId query parameter is provided, GetNamespace returns the namespace name of the corresponding
        tenancy, provided the user has access to it.


        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str compartment_id: (optional)
            This is an optional field representing either the tenancy `OCID`__ or the compartment
            `OCID`__ within the tenancy whose Object Storage namespace is to be retrieved.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type str
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_namespace got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="str")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="str")

    def get_namespace_metadata(self, namespace_name, **kwargs):
        """
        Gets the metadata for the Object Storage namespace, which contains defaultS3CompartmentId and
        defaultSwiftCompartmentId.

        Any user with the OBJECTSTORAGE_NAMESPACE_READ permission will be able to see the current metadata. If you are
        not authorized, talk to an administrator. If you are an administrator who needs to write policies
        to give users access, see
        `Getting Started with Policies`__.

        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.NamespaceMetadata`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_namespace_metadata got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="NamespaceMetadata")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="NamespaceMetadata")

    def get_object(self, namespace_name, bucket_name, object_name, **kwargs):
        """
        Gets the metadata and body of an object.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param str version_id: (optional)
            VersionId used to identify a particular version of the object

        :param str if_match: (optional)
            The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object
            already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a
            part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str range: (optional)
            Optional byte range to fetch, as described in `RFC 7233`__.
            Note that only a single range of bytes is supported.

            __ https://tools.ietf.org/html/rfc7233#section-2.1

        :param str opc_sse_customer_algorithm: (optional)
            The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param str opc_sse_customer_key: (optional)
            The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or
            decrypt the data. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param str opc_sse_customer_key_sha256: (optional)
            The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This
            value is used to check the integrity of the encryption key. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param str http_response_content_disposition: (optional)
            This value will be used in Content-Disposition header of the response.

        :param str http_response_cache_control: (optional)
            This value will be used in Cache-Control header of the response.

        :param str http_response_content_type: (optional)
            This value will be used in Content-Type header of the response.

        :param str http_response_content_language: (optional)
            This value will be used in Content-Language header of the response.

        :param str http_response_content_encoding: (optional)
            This value will be used in Content-Encoding header of the response

        :param str http_response_expires: (optional)
            This value will be used in Expires header of the response

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/o/{objectName}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "version_id",
            "if_match",
            "if_none_match",
            "opc_client_request_id",
            "range",
            "opc_sse_customer_algorithm",
            "opc_sse_customer_key",
            "opc_sse_customer_key_sha256",
            "http_response_content_disposition",
            "http_response_cache_control",
            "http_response_content_type",
            "http_response_content_language",
            "http_response_content_encoding",
            "http_response_expires"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "versionId": kwargs.get("version_id", missing),
            "httpResponseContentDisposition": kwargs.get("http_response_content_disposition", missing),
            "httpResponseCacheControl": kwargs.get("http_response_cache_control", missing),
            "httpResponseContentType": kwargs.get("http_response_content_type", missing),
            "httpResponseContentLanguage": kwargs.get("http_response_content_language", missing),
            "httpResponseContentEncoding": kwargs.get("http_response_content_encoding", missing),
            "httpResponseExpires": kwargs.get("http_response_expires", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing),
            "range": kwargs.get("range", missing),
            "opc-sse-customer-algorithm": kwargs.get("opc_sse_customer_algorithm", missing),
            "opc-sse-customer-key": kwargs.get("opc_sse_customer_key", missing),
            "opc-sse-customer-key-sha256": kwargs.get("opc_sse_customer_key_sha256", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="stream")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="stream")

    def get_object_lifecycle_policy(self, namespace_name, bucket_name, **kwargs):
        """
        Gets the object lifecycle policy for the bucket.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.ObjectLifecyclePolicy`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/l"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_object_lifecycle_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ObjectLifecyclePolicy")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ObjectLifecyclePolicy")

    def get_preauthenticated_request(self, namespace_name, bucket_name, par_id, **kwargs):
        """
        Gets the pre-authenticated request for the bucket.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str par_id: (required)
            The unique identifier for the pre-authenticated request. This can be used to manage operations against
            the pre-authenticated request, such as GET or DELETE.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.PreauthenticatedRequestSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/p/{parId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_preauthenticated_request got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "parId": par_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="PreauthenticatedRequestSummary")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="PreauthenticatedRequestSummary")

    def get_replication_policy(self, namespace_name, bucket_name, replication_id, **kwargs):
        """
        Get the replication policy.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str replication_id: (required)
            The ID of the replication policy.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.ReplicationPolicy`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/replicationPolicies/{replicationId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_replication_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "replicationId": replication_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ReplicationPolicy")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ReplicationPolicy")

    def get_retention_rule(self, namespace_name, bucket_name, retention_rule_id, **kwargs):
        """
        Get the specified retention rule.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str retention_rule_id: (required)
            The ID of the retention rule.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.RetentionRule`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/retentionRules/{retentionRuleId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_retention_rule got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "retentionRuleId": retention_rule_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="RetentionRule")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="RetentionRule")

    def get_work_request(self, work_request_id, **kwargs):
        """
        Gets the status of the work request for the given ID.


        :param str work_request_id: (required)
            The ID of the asynchronous request.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.WorkRequest`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workRequests/{workRequestId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_work_request got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workRequestId": work_request_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="WorkRequest")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="WorkRequest")

    def head_bucket(self, namespace_name, bucket_name, **kwargs):
        """
        Efficiently checks to see if a bucket exists and gets the current entity tag (ETag) for the bucket.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str if_match: (optional)
            The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object
            already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a
            part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}"
        method = "HEAD"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "if_none_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "head_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def head_object(self, namespace_name, bucket_name, object_name, **kwargs):
        """
        Gets the user-defined metadata and entity tag (ETag) for an object.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param str version_id: (optional)
            VersionId used to identify a particular version of the object

        :param str if_match: (optional)
            The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object
            already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a
            part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str opc_sse_customer_algorithm: (optional)
            The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param str opc_sse_customer_key: (optional)
            The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or
            decrypt the data. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param str opc_sse_customer_key_sha256: (optional)
            The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This
            value is used to check the integrity of the encryption key. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/o/{objectName}"
        method = "HEAD"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "version_id",
            "if_match",
            "if_none_match",
            "opc_client_request_id",
            "opc_sse_customer_algorithm",
            "opc_sse_customer_key",
            "opc_sse_customer_key_sha256"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "head_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "versionId": kwargs.get("version_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing),
            "opc-sse-customer-algorithm": kwargs.get("opc_sse_customer_algorithm", missing),
            "opc-sse-customer-key": kwargs.get("opc_sse_customer_key", missing),
            "opc-sse-customer-key-sha256": kwargs.get("opc_sse_customer_key_sha256", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)

    def list_buckets(self, namespace_name, compartment_id, **kwargs):
        """
        Gets a list of all BucketSummary items in a compartment. A BucketSummary contains only summary fields for the bucket
        and does not contain fields like the user-defined metadata.

        To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized,
        talk to an administrator. If you are an administrator who needs to write policies to give users access, see
        `Getting Started with Policies`__.

        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str compartment_id: (required)
            The ID of the compartment in which to list buckets.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page at which to start retrieving results.

        :param list[str] fields: (optional)
            Bucket summary in list of buckets includes the 'namespace', 'name', 'compartmentId', 'createdBy', 'timeCreated',
            and 'etag' fields. This parameter can also include 'tags' (freeformTags and definedTags). The only supported value
            of this parameter is 'tags' for now. Example 'tags'.

            Allowed values are: "tags"

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.BucketSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "fields",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_buckets got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'fields' in kwargs:
            fields_allowed_values = ["tags"]
            for fields_item in kwargs['fields']:
                if fields_item not in fields_allowed_values:
                    raise ValueError(
                        "Invalid value for `fields`, must be one of {0}".format(fields_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'csv')
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[BucketSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[BucketSummary]")

    def list_multipart_upload_parts(self, namespace_name, bucket_name, object_name, upload_id, **kwargs):
        """
        Lists the parts of an in-progress multipart upload.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param str upload_id: (required)
            The upload ID for a multipart upload.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page at which to start retrieving results.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.MultipartUploadPartSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u/{objectName}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_multipart_upload_parts got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "uploadId": upload_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[MultipartUploadPartSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[MultipartUploadPartSummary]")

    def list_multipart_uploads(self, namespace_name, bucket_name, **kwargs):
        """
        Lists all of the in-progress multipart uploads for the given bucket in the given Object Storage namespace.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page at which to start retrieving results.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.MultipartUpload`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_multipart_uploads got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[MultipartUpload]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[MultipartUpload]")

    def list_object_versions(self, namespace_name, bucket_name, **kwargs):
        """
        Lists the object versions in a bucket.

        To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized,
        talk to an administrator. If you are an administrator who needs to write policies to give users access, see
        `Getting Started with Policies`__.

        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str prefix: (optional)
            The string to use for matching against the start of object names in a list query.

        :param str start: (optional)
            Object names returned by a list query must be greater or equal to this parameter.

        :param str end: (optional)
            Object names returned by a list query must be strictly less than this parameter.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str delimiter: (optional)
            When this parameter is set, only objects whose names do not contain the delimiter character
            (after an optionally specified prefix) are returned in the objects key of the response body.
            Scanned objects whose names contain the delimiter have the part of their name up to the first
            occurrence of the delimiter (including the optional prefix) returned as a set of prefixes.
            Note that only '/' is a supported delimiter character at this time.

        :param str fields: (optional)
            Object summary in list of objects includes the 'name' field. This parameter can also include 'size'
            (object size in bytes), 'etag', 'md5', 'timeCreated' (object creation date and time) and 'timeModified'
            (object modification date and time).
            Value of this parameter should be a comma-separated, case-insensitive list of those field names.
            For example 'name,etag,timeCreated,md5,timeModified'

            Allowed values are: "name", "size", "etag", "timeCreated", "md5", "timeModified"

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str start_after: (optional)
            Object names returned by a list query must be greater than this parameter.

        :param str page: (optional)
            The page at which to start retrieving results.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.ObjectVersionCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/objectversions"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "prefix",
            "start",
            "end",
            "limit",
            "delimiter",
            "fields",
            "opc_client_request_id",
            "start_after",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_object_versions got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "prefix": kwargs.get("prefix", missing),
            "start": kwargs.get("start", missing),
            "end": kwargs.get("end", missing),
            "limit": kwargs.get("limit", missing),
            "delimiter": kwargs.get("delimiter", missing),
            "fields": kwargs.get("fields", missing),
            "startAfter": kwargs.get("start_after", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ObjectVersionCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ObjectVersionCollection")

    def list_objects(self, namespace_name, bucket_name, **kwargs):
        """
        Lists the objects in a bucket.

        To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized,
        talk to an administrator. If you are an administrator who needs to write policies to give users access, see
        `Getting Started with Policies`__.

        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str prefix: (optional)
            The string to use for matching against the start of object names in a list query.

        :param str start: (optional)
            Object names returned by a list query must be greater or equal to this parameter.

        :param str end: (optional)
            Object names returned by a list query must be strictly less than this parameter.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str delimiter: (optional)
            When this parameter is set, only objects whose names do not contain the delimiter character
            (after an optionally specified prefix) are returned in the objects key of the response body.
            Scanned objects whose names contain the delimiter have the part of their name up to the first
            occurrence of the delimiter (including the optional prefix) returned as a set of prefixes.
            Note that only '/' is a supported delimiter character at this time.

        :param str fields: (optional)
            Object summary in list of objects includes the 'name' field. This parameter can also include 'size'
            (object size in bytes), 'etag', 'md5', 'timeCreated' (object creation date and time) and 'timeModified'
            (object modification date and time).
            Value of this parameter should be a comma-separated, case-insensitive list of those field names.
            For example 'name,etag,timeCreated,md5,timeModified'

            Allowed values are: "name", "size", "etag", "timeCreated", "md5", "timeModified"

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str start_after: (optional)
            Object names returned by a list query must be greater than this parameter.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.ListObjects`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/o"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "prefix",
            "start",
            "end",
            "limit",
            "delimiter",
            "fields",
            "opc_client_request_id",
            "start_after"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_objects got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "prefix": kwargs.get("prefix", missing),
            "start": kwargs.get("start", missing),
            "end": kwargs.get("end", missing),
            "limit": kwargs.get("limit", missing),
            "delimiter": kwargs.get("delimiter", missing),
            "fields": kwargs.get("fields", missing),
            "startAfter": kwargs.get("start_after", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ListObjects")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ListObjects")

    def list_preauthenticated_requests(self, namespace_name, bucket_name, **kwargs):
        """
        Lists pre-authenticated requests for the bucket.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name_prefix: (optional)
            User-specified object name prefixes can be used to query and return a list of pre-authenticated requests.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page at which to start retrieving results.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.PreauthenticatedRequestSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/p"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "object_name_prefix",
            "limit",
            "page",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_preauthenticated_requests got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "objectNamePrefix": kwargs.get("object_name_prefix", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PreauthenticatedRequestSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PreauthenticatedRequestSummary]")

    def list_replication_policies(self, namespace_name, bucket_name, **kwargs):
        """
        List the replication policies associated with a bucket.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str page: (optional)
            The page at which to start retrieving results.

        :param int limit: (optional)
            The maximum number of items to return.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.ReplicationPolicySummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/replicationPolicies"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id",
            "page",
            "limit"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_replication_policies got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ReplicationPolicySummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ReplicationPolicySummary]")

    def list_replication_sources(self, namespace_name, bucket_name, **kwargs):
        """
        List the replication sources of a destination bucket.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str page: (optional)
            The page at which to start retrieving results.

        :param int limit: (optional)
            The maximum number of items to return.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.ReplicationSource`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/replicationSources"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id",
            "page",
            "limit"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_replication_sources got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ReplicationSource]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ReplicationSource]")

    def list_retention_rules(self, namespace_name, bucket_name, **kwargs):
        """
        List the retention rules for a bucket. The retention rules are sorted based on creation time,
        with the most recently created retention rule returned first.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str page: (optional)
            The page at which to start retrieving results.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.RetentionRuleCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/retentionRules"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_retention_rules got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RetentionRuleCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RetentionRuleCollection")

    def list_work_request_errors(self, work_request_id, **kwargs):
        """
        Lists the errors of the work request with the given ID.


        :param str work_request_id: (required)
            The ID of the asynchronous request.

        :param str page: (optional)
            The page at which to start retrieving results.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.WorkRequestError`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workRequests/{workRequestId}/errors"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "page",
            "limit",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_work_request_errors got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workRequestId": work_request_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestError]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestError]")

    def list_work_request_logs(self, work_request_id, **kwargs):
        """
        Lists the logs of the work request with the given ID.


        :param str work_request_id: (required)
            The ID of the asynchronous request.

        :param str page: (optional)
            The page at which to start retrieving results.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.WorkRequestLogEntry`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workRequests/{workRequestId}/logs"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "page",
            "limit",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_work_request_logs got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workRequestId": work_request_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestLogEntry]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestLogEntry]")

    def list_work_requests(self, compartment_id, **kwargs):
        """
        Lists the work requests in a compartment.


        :param str compartment_id: (required)
            The ID of the compartment in which to list buckets.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str page: (optional)
            The page at which to start retrieving results.

        :param int limit: (optional)
            The maximum number of items to return.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.WorkRequestSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workRequests"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id",
            "page",
            "limit"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_work_requests got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestSummary]")

    def make_bucket_writable(self, namespace_name, bucket_name, **kwargs):
        """
        Stops replication to the destination bucket and removes the replication policy. When the replication
        policy was created, this destination bucket became read-only except for new and changed objects replicated
        automatically from the source bucket. MakeBucketWritable removes the replication policy. This bucket is no
        longer the target for replication and is now writable, allowing users to make changes to bucket contents.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/actions/makeBucketWritable"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "make_bucket_writable got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def put_object(self, namespace_name, bucket_name, object_name, put_object_body, **kwargs):
        """
        Creates a new object or overwrites an existing object with the same name. The maximum object size allowed by
        PutObject is 50 GiB.

        See `Object Names`__
        for object naming requirements.

        See `Special Instructions for Object Storage PUT`__
        for request signature requirements.

        __ https://docs.cloud.oracle.com/Content/Object/Tasks/managingobjects.htm#namerequirements
        __ https://docs.cloud.oracle.com/Content/API/Concepts/signingrequests.htm#ObjectStoragePut


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param stream put_object_body: (required)
            The object to upload to the object store.

        :param int content_length: (optional)
            The content length of the body.

        :param str if_match: (optional)
            The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object
            already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a
            part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str expect: (optional)
            100-continue

        :param str content_md5: (optional)
            The optional base-64 header that defines the encoded MD5 hash of the body. If the optional Content-MD5 header is present, Object
            Storage performs an integrity check on the body of the HTTP request by computing the MD5 hash for the body and comparing it to the
            MD5 hash supplied in the header. If the two hashes do not match, the object is rejected and an HTTP-400 Unmatched Content MD5 error
            is returned with the message:

            \"The computed MD5 of the request body (ACTUAL_MD5) does not match the Content-MD5 header (HEADER_MD5)\"

        :param str content_type: (optional)
            The optional Content-Type header that defines the standard MIME type format of the object. Content type defaults to
            'application/octet-stream' if not specified in the PutObject call. Specifying values for this header has no effect
            on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example,
            you could use this header to identify and perform special operations on text only objects.

        :param str content_language: (optional)
            The optional Content-Language header that defines the content language of the object to upload. Specifying
            values for this header has no effect on Object Storage behavior. Programs that read the object determine what
            to do based on the value provided. For example, you could use this header to identify and differentiate objects
            based on a particular language.

        :param str content_encoding: (optional)
            The optional Content-Encoding header that defines the content encodings that were applied to the object to
            upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the
            object determine what to do based on the value provided. For example, you could use this header to determine
            what decoding mechanisms need to be applied to obtain the media-type specified by the Content-Type header of
            the object.

        :param str content_disposition: (optional)
            The optional Content-Disposition header that defines presentational information for the object to be
            returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object
            Storage behavior. Programs that read the object determine what to do based on the value provided.
            For example, you could use this header to let users download objects with custom filenames in a browser.

        :param str cache_control: (optional)
            The optional Cache-Control header that defines the caching behavior value to be returned in GetObject and
            HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs
            that read the object determine what to do based on the value provided.
            For example, you could use this header to identify objects that require caching restrictions.

        :param str opc_sse_customer_algorithm: (optional)
            The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param str opc_sse_customer_key: (optional)
            The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or
            decrypt the data. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param str opc_sse_customer_key_sha256: (optional)
            The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This
            value is used to check the integrity of the encryption key. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param dict(str, str) opc_meta: (optional)
            Optional user-defined metadata key and value.

            "opc-meta-" will be appended to each dict key before it is sent to the server.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/o/{objectName}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "content_length",
            "if_match",
            "if_none_match",
            "opc_client_request_id",
            "expect",
            "content_md5",
            "content_type",
            "content_language",
            "content_encoding",
            "content_disposition",
            "cache_control",
            "opc_sse_customer_algorithm",
            "opc_sse_customer_key",
            "opc_sse_customer_key_sha256",
            "opc_meta"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "put_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "if-none-match": kwargs.get("if_none_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing),
            "Expect": kwargs.get("expect", missing),
            "Content-Length": kwargs.get("content_length", missing),
            "Content-MD5": kwargs.get("content_md5", missing),
            "Content-Type": kwargs.get("content_type", missing),
            "Content-Language": kwargs.get("content_language", missing),
            "Content-Encoding": kwargs.get("content_encoding", missing),
            "Content-Disposition": kwargs.get("content_disposition", missing),
            "Cache-Control": kwargs.get("cache_control", missing),
            "opc-sse-customer-algorithm": kwargs.get("opc_sse_customer_algorithm", missing),
            "opc-sse-customer-key": kwargs.get("opc_sse_customer_key", missing),
            "opc-sse-customer-key-sha256": kwargs.get("opc_sse_customer_key_sha256", missing),

        }
        for key, value in six.iteritems(kwargs.get("opc_meta", {})):
            header_params["opc-meta-" + key] = value
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        # If the body parameter is optional we need to assign it to a variable so additional type checking can be performed.
        try:
            put_object_body
        except NameError:
            put_object_body = kwargs.get("put_object_body", missing)

        if put_object_body is not missing and put_object_body is not None:
            if (not isinstance(put_object_body, (six.binary_type, six.string_types)) and
                    not hasattr(put_object_body, "read")):
                raise TypeError('The body must be a string, bytes, or provide a read() method.')

            if hasattr(put_object_body, 'fileno') and hasattr(put_object_body, 'name') and put_object_body.name != '<stdin>':
                if requests.utils.super_len(put_object_body) == 0:
                    header_params['Content-Length'] = '0'

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        # Disable the retry_strategy to work around data corruption issue temporarily
        if retry_strategy:
            retry_strategy = None
        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=put_object_body,
                enforce_content_headers=False)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=put_object_body,
                enforce_content_headers=False)

    def put_object_lifecycle_policy(self, namespace_name, bucket_name, put_object_lifecycle_policy_details, **kwargs):
        """
        Creates or replaces the object lifecycle policy for the bucket.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param oci.object_storage.models.PutObjectLifecyclePolicyDetails put_object_lifecycle_policy_details: (required)
            The lifecycle policy to apply to the bucket.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str if_match: (optional)
            The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object
            already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a
            part, this is the entity tag of the target part.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.ObjectLifecyclePolicy`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/l"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id",
            "if_match",
            "if_none_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "put_object_lifecycle_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing),
            "if-match": kwargs.get("if_match", missing),
            "if-none-match": kwargs.get("if_none_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=put_object_lifecycle_policy_details,
                response_type="ObjectLifecyclePolicy")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=put_object_lifecycle_policy_details,
                response_type="ObjectLifecyclePolicy")

    def reencrypt_bucket(self, namespace_name, bucket_name, **kwargs):
        """
        Re-encrypts the unique data encryption key that encrypts each object written to the bucket by using the most recent
        version of the master encryption key assigned to the bucket. (All data encryption keys are encrypted by a master
        encryption key. Master encryption keys are assigned to buckets and managed by Oracle by default, but you can assign
        a key that you created and control through the Oracle Cloud Infrastructure Key Management service.) The kmsKeyId property
        of the bucket determines which master encryption key is assigned to the bucket. If you assigned a different Key Management
        master encryption key to the bucket, you can call this API to re-encrypt all data encryption keys with the newly
        assigned key. Similarly, you might want to re-encrypt all data encryption keys if the assigned key has been rotated to
        a new key version since objects were last added to the bucket. If you call this API and there is no kmsKeyId associated
        with the bucket, the call will fail.

        Calling this API starts a work request task to re-encrypt the data encryption key of all objects in the bucket. Only
        objects created before the time of the API call will be re-encrypted. The call can take a long time, depending on how many
        objects are in the bucket and how big they are. This API returns a work request ID that you can use to retrieve the status
        of the work request task.
        All the versions of objects will be re-encrypted whether versioning is enabled or suspended at the bucket.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/actions/reencrypt"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "reencrypt_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def reencrypt_object(self, namespace_name, bucket_name, object_name, reencrypt_object_details, **kwargs):
        """
        Re-encrypts the data encryption keys that encrypt the object and its chunks. By default, when you create a bucket, the Object Storage
        service manages the master encryption key used to encrypt each object's data encryption keys. The encryption mechanism that you specify for
        the bucket applies to the objects it contains.

        You can alternatively employ one of these encryption strategies for an object:

        - You can assign a key that you created and control through the Oracle Cloud Infrastructure Vault service.

        - You can encrypt an object using your own encryption key. The key you supply is known as a customer-provided encryption key (SSE-C).


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param oci.object_storage.models.ReencryptObjectDetails reencrypt_object_details: (required)
            Request object for re-encrypting the data encryption key associated with an object.

        :param str version_id: (optional)
            VersionId used to identify a particular version of the object

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/actions/reencrypt/{objectName}"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "version_id",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "reencrypt_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "versionId": kwargs.get("version_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=reencrypt_object_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=reencrypt_object_details)

    def rename_object(self, namespace_name, bucket_name, rename_object_details, **kwargs):
        """
        Rename an object in the given Object Storage namespace.

        See `Object Names`__
        for object naming requirements.

        __ https://docs.cloud.oracle.com/Content/Object/Tasks/managingobjects.htm#namerequirements


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param oci.object_storage.models.RenameObjectDetails rename_object_details: (required)
            The sourceName and newName of rename operation.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/actions/renameObject"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "rename_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=rename_object_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=rename_object_details)

    def restore_objects(self, namespace_name, bucket_name, restore_objects_details, **kwargs):
        """
        Restores one or more objects specified by the objectName parameter.
        By default objects will be restored for 24 hours. Duration can be configured using the hours parameter.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param oci.object_storage.models.RestoreObjectsDetails restore_objects_details: (required)
            Request to restore objects.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/actions/restoreObjects"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "restore_objects got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=restore_objects_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=restore_objects_details)

    def update_bucket(self, namespace_name, bucket_name, update_bucket_details, **kwargs):
        """
        Performs a partial or full update of a bucket's user-defined metadata.

        Use UpdateBucket to move a bucket from one compartment to another within the same tenancy. Supply the compartmentID
        of the compartment that you want to move the bucket to. For more information about moving resources between compartments,
        see `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param oci.object_storage.models.UpdateBucketDetails update_bucket_details: (required)
            Request object for updating a bucket.

        :param str if_match: (optional)
            The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.Bucket`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_bucket_details,
                response_type="Bucket")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_bucket_details,
                response_type="Bucket")

    def update_namespace_metadata(self, namespace_name, update_namespace_metadata_details, **kwargs):
        """
        By default, buckets created using the Amazon S3 Compatibility API or the Swift API are created in the root
        compartment of the Oracle Cloud Infrastructure tenancy.

        You can change the default Swift/Amazon S3 compartmentId designation to a different compartmentId. All
        subsequent bucket creations will use the new default compartment, but no previously created
        buckets will be modified. A user must have OBJECTSTORAGE_NAMESPACE_UPDATE permission to make changes to the default
        compartments for Amazon S3 and Swift.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param oci.object_storage.models.UpdateNamespaceMetadataDetails update_namespace_metadata_details: (required)
            Request object for update NamespaceMetadata.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.NamespaceMetadata`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_namespace_metadata got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_namespace_metadata_details,
                response_type="NamespaceMetadata")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_namespace_metadata_details,
                response_type="NamespaceMetadata")

    def update_retention_rule(self, namespace_name, bucket_name, retention_rule_id, update_retention_rule_details, **kwargs):
        """
        Updates the specified retention rule. Rule changes take effect typically within 30 seconds.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str retention_rule_id: (required)
            The ID of the retention rule.

        :param oci.object_storage.models.UpdateRetentionRuleDetails update_retention_rule_details: (required)
            Request object for updating the retention rule.

        :param str if_match: (optional)
            The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.RetentionRule`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/retentionRules/{retentionRuleId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_retention_rule got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "retentionRuleId": retention_rule_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_retention_rule_details,
                response_type="RetentionRule")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_retention_rule_details,
                response_type="RetentionRule")

    def upload_part(self, namespace_name, bucket_name, object_name, upload_id, upload_part_num, upload_part_body, **kwargs):
        """
        Uploads a single part of a multipart upload.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param str upload_id: (required)
            The upload ID for a multipart upload.

        :param int upload_part_num: (required)
            The part number that identifies the object part currently being uploaded.

        :param stream upload_part_body: (required)
            The part being uploaded to the Object Storage service.

        :param int content_length: (optional)
            The content length of the body.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str if_match: (optional)
            The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object.
            For uploading a part, this is the entity tag of the target part.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object
            already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a
            part, this is the entity tag of the target part.

        :param str expect: (optional)
            100-continue

        :param str content_md5: (optional)
            The optional base-64 header that defines the encoded MD5 hash of the body. If the optional Content-MD5 header is present, Object
            Storage performs an integrity check on the body of the HTTP request by computing the MD5 hash for the body and comparing it to the
            MD5 hash supplied in the header. If the two hashes do not match, the object is rejected and an HTTP-400 Unmatched Content MD5 error
            is returned with the message:

            \"The computed MD5 of the request body (ACTUAL_MD5) does not match the Content-MD5 header (HEADER_MD5)\"

        :param str opc_sse_customer_algorithm: (optional)
            The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param str opc_sse_customer_key: (optional)
            The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or
            decrypt the data. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param str opc_sse_customer_key_sha256: (optional)
            The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This
            value is used to check the integrity of the encryption key. For more information, see
            `Using Your Own Keys for Server-Side Encryption`__.

            __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u/{objectName}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "content_length",
            "opc_client_request_id",
            "if_match",
            "if_none_match",
            "expect",
            "content_md5",
            "opc_sse_customer_algorithm",
            "opc_sse_customer_key",
            "opc_sse_customer_key_sha256"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "upload_part got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "namespaceName": namespace_name,
            "bucketName": bucket_name,
            "objectName": object_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "uploadId": upload_id,
            "uploadPartNum": upload_part_num
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "opc-client-request-id": kwargs.get("opc_client_request_id", missing),
            "if-match": kwargs.get("if_match", missing),
            "if-none-match": kwargs.get("if_none_match", missing),
            "Expect": kwargs.get("expect", missing),
            "Content-Length": kwargs.get("content_length", missing),
            "Content-MD5": kwargs.get("content_md5", missing),
            "opc-sse-customer-algorithm": kwargs.get("opc_sse_customer_algorithm", missing),
            "opc-sse-customer-key": kwargs.get("opc_sse_customer_key", missing),
            "opc-sse-customer-key-sha256": kwargs.get("opc_sse_customer_key_sha256", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        # If the body parameter is optional we need to assign it to a variable so additional type checking can be performed.
        try:
            upload_part_body
        except NameError:
            upload_part_body = kwargs.get("upload_part_body", missing)

        if upload_part_body is not missing and upload_part_body is not None:
            if (not isinstance(upload_part_body, (six.binary_type, six.string_types)) and
                    not hasattr(upload_part_body, "read")):
                raise TypeError('The body must be a string, bytes, or provide a read() method.')

            if hasattr(upload_part_body, 'fileno') and hasattr(upload_part_body, 'name') and upload_part_body.name != '<stdin>':
                if requests.utils.super_len(upload_part_body) == 0:
                    header_params['Content-Length'] = '0'

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        # Disable the retry_strategy to work around data corruption issue temporarily
        if retry_strategy:
            retry_strategy = None
        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=upload_part_body,
                enforce_content_headers=False)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=upload_part_body,
                enforce_content_headers=False)
