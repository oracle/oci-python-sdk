# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry, circuit_breaker  # noqa: F401
from oci.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel, get_signer_from_authentication_type, AUTHENTICATION_TYPE_FIELD_NAME
from oci.util import back_up_body_calculate_stream_content_length, is_content_length_calculable_by_req_util
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
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

        :param obj circuit_breaker_strategy: (optional)
            A circuit breaker strategy to apply to all calls made by this service client (i.e. at the client level).
            This client uses :py:data:`~oci.circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY` as default if no circuit breaker strategy is provided.
            The specifics of circuit breaker strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/circuit_breakers.html>`__.

        :param function circuit_breaker_callback: (optional)
            Callback function to receive any exceptions triggerred by the circuit breaker.

        :param allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this client should allow control characters in the response object. By default, the client will not
            allow control characters to be in the response object.
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
            'base_path': '/',
            'service_endpoint_template': 'https://objectstorage.{region}.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'circuit_breaker_strategy': kwargs.get('circuit_breaker_strategy', circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY)
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        if base_client_init_kwargs.get('circuit_breaker_strategy') is None:
            base_client_init_kwargs['circuit_breaker_strategy'] = circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY
        if 'allow_control_chars' in kwargs:
            base_client_init_kwargs['allow_control_chars'] = kwargs.get('allow_control_chars')
        self.base_client = BaseClient("object_storage", config, signer, object_storage_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/abort_multipart_upload.py.html>`__ to see an example of how to use abort_multipart_upload API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u/{objectName}"
        method = "DELETE"
        operation_name = "abort_multipart_upload"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/MultipartUpload/AbortMultipartUpload"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def cancel_work_request(self, work_request_id, **kwargs):
        """
        Cancels a work request.


        :param str work_request_id: (required)
            The ID of the asynchronous request.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/cancel_work_request.py.html>`__ to see an example of how to use cancel_work_request API.
        """
        resource_path = "/workRequests/{workRequestId}"
        method = "DELETE"
        operation_name = "cancel_work_request"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/WorkRequest/CancelWorkRequest"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of
            the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload
            the resource.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should
            fail if the resource already exists.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/commit_multipart_upload.py.html>`__ to see an example of how to use commit_multipart_upload API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u/{objectName}"
        method = "POST"
        operation_name = "commit_multipart_upload"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/MultipartUpload/CommitMultipartUpload"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=commit_multipart_upload_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=commit_multipart_upload_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def copy_object(self, namespace_name, bucket_name, copy_object_details, **kwargs):
        """
        Creates a request to copy an object within a region or to another region.

        See `Object Names`__
        for object naming requirements.

        __ https://docs.cloud.oracle.com/Content/Object/Tasks/managingobjects.htm#namerequirements


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

        :param str opc_sse_kms_key_id: (optional)
            The `OCID`__ of a master encryption key used to call the Key
            Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/copy_object.py.html>`__ to see an example of how to use copy_object API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/actions/copyObject"
        method = "POST"
        operation_name = "copy_object"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Object/CopyObject"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_client_request_id",
            "opc_sse_customer_algorithm",
            "opc_sse_customer_key",
            "opc_sse_customer_key_sha256",
            "opc_source_sse_customer_algorithm",
            "opc_source_sse_customer_key",
            "opc_source_sse_customer_key_sha256",
            "opc_sse_kms_key_id"
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
            "opc-source-sse-customer-key-sha256": kwargs.get("opc_source_sse_customer_key_sha256", missing),
            "opc-sse-kms-key-id": kwargs.get("opc_sse_kms_key_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=copy_object_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=copy_object_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.Bucket`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/create_bucket.py.html>`__ to see an example of how to use create_bucket API.
        """
        resource_path = "/n/{namespaceName}/b"
        method = "POST"
        operation_name = "create_bucket"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Bucket/CreateBucket"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_bucket_details,
                response_type="Bucket",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_bucket_details,
                response_type="Bucket",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_multipart_upload(self, namespace_name, bucket_name, create_multipart_upload_details, **kwargs):
        """
        Starts a new multipart upload to a specific object in the given bucket in the given namespace.

        See `Object Names`__
        for object naming requirements.

        __ https://docs.cloud.oracle.com/Content/Object/Tasks/managingobjects.htm#namerequirements


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param oci.object_storage.models.CreateMultipartUploadDetails create_multipart_upload_details: (required)
            Request object for creating a multipart upload.

        :param str if_match: (optional)
            The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of
            the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload
            the resource.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should
            fail if the resource already exists.

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

        :param str opc_sse_kms_key_id: (optional)
            The `OCID`__ of a master encryption key used to call the Key
            Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.MultipartUpload`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/create_multipart_upload.py.html>`__ to see an example of how to use create_multipart_upload API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u"
        method = "POST"
        operation_name = "create_multipart_upload"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/MultipartUpload/CreateMultipartUpload"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "if_none_match",
            "opc_client_request_id",
            "opc_sse_customer_algorithm",
            "opc_sse_customer_key",
            "opc_sse_customer_key_sha256",
            "opc_sse_kms_key_id"
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
            "opc-sse-customer-key-sha256": kwargs.get("opc_sse_customer_key_sha256", missing),
            "opc-sse-kms-key-id": kwargs.get("opc_sse_kms_key_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_multipart_upload_details,
                response_type="MultipartUpload",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_multipart_upload_details,
                response_type="MultipartUpload",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.PreauthenticatedRequest`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/create_preauthenticated_request.py.html>`__ to see an example of how to use create_preauthenticated_request API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/p"
        method = "POST"
        operation_name = "create_preauthenticated_request"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/PreauthenticatedRequest/CreatePreauthenticatedRequest"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_preauthenticated_request_details,
                response_type="PreauthenticatedRequest",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_preauthenticated_request_details,
                response_type="PreauthenticatedRequest",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.ReplicationPolicy`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/create_replication_policy.py.html>`__ to see an example of how to use create_replication_policy API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/replicationPolicies"
        method = "POST"
        operation_name = "create_replication_policy"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Replication/CreateReplicationPolicy"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_replication_policy_details,
                response_type="ReplicationPolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_replication_policy_details,
                response_type="ReplicationPolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.RetentionRule`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/create_retention_rule.py.html>`__ to see an example of how to use create_retention_rule API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/retentionRules"
        method = "POST"
        operation_name = "create_retention_rule"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/RetentionRule/CreateRetentionRule"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_retention_rule_details,
                response_type="RetentionRule",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_retention_rule_details,
                response_type="RetentionRule",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of
            the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload
            the resource.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/delete_bucket.py.html>`__ to see an example of how to use delete_bucket API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}"
        method = "DELETE"
        operation_name = "delete_bucket"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Bucket/DeleteBucket"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of
            the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload
            the resource.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str version_id: (optional)
            VersionId used to identify a particular version of the object

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/delete_object.py.html>`__ to see an example of how to use delete_object API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/o/{objectName}"
        method = "DELETE"
        operation_name = "delete_object"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Object/DeleteObject"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of
            the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload
            the resource.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/delete_object_lifecycle_policy.py.html>`__ to see an example of how to use delete_object_lifecycle_policy API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/l"
        method = "DELETE"
        operation_name = "delete_object_lifecycle_policy"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/ObjectLifecyclePolicy/DeleteObjectLifecyclePolicy"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/delete_preauthenticated_request.py.html>`__ to see an example of how to use delete_preauthenticated_request API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/p/{parId}"
        method = "DELETE"
        operation_name = "delete_preauthenticated_request"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/PreauthenticatedRequest/DeletePreauthenticatedRequest"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/delete_replication_policy.py.html>`__ to see an example of how to use delete_replication_policy API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/replicationPolicies/{replicationId}"
        method = "DELETE"
        operation_name = "delete_replication_policy"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Replication/DeleteReplicationPolicy"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of
            the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload
            the resource.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/delete_retention_rule.py.html>`__ to see an example of how to use delete_retention_rule API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/retentionRules/{retentionRuleId}"
        method = "DELETE"
        operation_name = "delete_retention_rule"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/RetentionRule/DeleteRetentionRule"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_bucket(self, namespace_name, bucket_name, **kwargs):
        """
        Gets the current representation of the given bucket in the given Object Storage namespace.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str if_match: (optional)
            The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of
            the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload
            the resource.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. Wildcards ('*') are not allowed. If the specified ETag does not
            match the ETag of the existing resource, the request returns the expected response. If the ETag matches
            the ETag of the existing resource, the request returns an HTTP 304 status without a response body.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param list[str] fields: (optional)
            Bucket summary includes the 'namespace', 'name', 'compartmentId', 'createdBy', 'timeCreated',
            and 'etag' fields. This parameter can also include 'approximateCount' (approximate number of objects), 'approximateSize'
            (total approximate size in bytes of all objects) and 'autoTiering' (state of auto tiering on the bucket).
            For example 'approximateCount,approximateSize,autoTiering'.

            Allowed values are: "approximateCount", "approximateSize", "autoTiering"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.Bucket`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/get_bucket.py.html>`__ to see an example of how to use get_bucket API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}"
        method = "GET"
        operation_name = "get_bucket"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Bucket/GetBucket"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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
            fields_allowed_values = ["approximateCount", "approximateSize", "autoTiering"]
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="Bucket",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="Bucket",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type str
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/get_namespace.py.html>`__ to see an example of how to use get_namespace API.
        """
        resource_path = "/n"
        method = "GET"
        operation_name = "get_namespace"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Namespace/GetNamespace"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="str",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="str",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.NamespaceMetadata`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/get_namespace_metadata.py.html>`__ to see an example of how to use get_namespace_metadata API.
        """
        resource_path = "/n/{namespaceName}"
        method = "GET"
        operation_name = "get_namespace_metadata"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Namespace/GetNamespaceMetadata"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="NamespaceMetadata",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="NamespaceMetadata",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of
            the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload
            the resource.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. Wildcards ('*') are not allowed. If the specified ETag does not
            match the ETag of the existing resource, the request returns the expected response. If the ETag matches
            the ETag of the existing resource, the request returns an HTTP 304 status without a response body.

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
            Specify this query parameter to override the value of the Content-Disposition response header in the GetObject response.

        :param str http_response_cache_control: (optional)
            Specify this query parameter to override the Cache-Control response header in the GetObject response.

        :param str http_response_content_type: (optional)
            Specify this query parameter to override the Content-Type response header in the GetObject response.

        :param str http_response_content_language: (optional)
            Specify this query parameter to override the Content-Language response header in the GetObject response.

        :param str http_response_content_encoding: (optional)
            Specify this query parameter to override the Content-Encoding response header in the GetObject response.

        :param str http_response_expires: (optional)
            Specify this query parameter to override the Expires response header in the GetObject response.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/get_object.py.html>`__ to see an example of how to use get_object API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/o/{objectName}"
        method = "GET"
        operation_name = "get_object"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Object/GetObject"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="stream",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="stream",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.ObjectLifecyclePolicy`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/get_object_lifecycle_policy.py.html>`__ to see an example of how to use get_object_lifecycle_policy API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/l"
        method = "GET"
        operation_name = "get_object_lifecycle_policy"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/ObjectLifecyclePolicy/GetObjectLifecyclePolicy"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ObjectLifecyclePolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ObjectLifecyclePolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.PreauthenticatedRequestSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/get_preauthenticated_request.py.html>`__ to see an example of how to use get_preauthenticated_request API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/p/{parId}"
        method = "GET"
        operation_name = "get_preauthenticated_request"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/PreauthenticatedRequest/GetPreauthenticatedRequest"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="PreauthenticatedRequestSummary",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="PreauthenticatedRequestSummary",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.ReplicationPolicy`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/get_replication_policy.py.html>`__ to see an example of how to use get_replication_policy API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/replicationPolicies/{replicationId}"
        method = "GET"
        operation_name = "get_replication_policy"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Replication/GetReplicationPolicy"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ReplicationPolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ReplicationPolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.RetentionRule`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/get_retention_rule.py.html>`__ to see an example of how to use get_retention_rule API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/retentionRules/{retentionRuleId}"
        method = "GET"
        operation_name = "get_retention_rule"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/RetentionRule/GetRetentionRule"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="RetentionRule",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="RetentionRule",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_work_request(self, work_request_id, **kwargs):
        """
        Gets the status of the work request for the given ID.


        :param str work_request_id: (required)
            The ID of the asynchronous request.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.WorkRequest`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/get_work_request.py.html>`__ to see an example of how to use get_work_request API.
        """
        resource_path = "/workRequests/{workRequestId}"
        method = "GET"
        operation_name = "get_work_request"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/WorkRequest/GetWorkRequest"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="WorkRequest",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="WorkRequest",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def head_bucket(self, namespace_name, bucket_name, **kwargs):
        """
        Efficiently checks to see if a bucket exists and gets the current entity tag (ETag) for the bucket.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str if_match: (optional)
            The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of
            the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload
            the resource.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. Wildcards ('*') are not allowed. If the specified ETag does not
            match the ETag of the existing resource, the request returns the expected response. If the ETag matches
            the ETag of the existing resource, the request returns an HTTP 304 status without a response body.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/head_bucket.py.html>`__ to see an example of how to use head_bucket API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}"
        method = "HEAD"
        operation_name = "head_bucket"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Bucket/HeadBucket"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of
            the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload
            the resource.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. Wildcards ('*') are not allowed. If the specified ETag does not
            match the ETag of the existing resource, the request returns the expected response. If the ETag matches
            the ETag of the existing resource, the request returns an HTTP 304 status without a response body.

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/head_object.py.html>`__ to see an example of how to use head_object API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/o/{objectName}"
        method = "HEAD"
        operation_name = "head_object"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Object/HeadObject"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_buckets(self, namespace_name, compartment_id, **kwargs):
        """
        Gets a list of all BucketSummary items in a compartment. A BucketSummary contains only summary fields for the bucket
        and does not contain fields like the user-defined metadata.

        ListBuckets returns a BucketSummary containing at most 1000 buckets. To paginate through more buckets, use the returned
        `opc-next-page` value with the `page` request parameter.

        To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized,
        talk to an administrator. If you are an administrator who needs to write policies to give users access, see
        `Getting Started with Policies`__.

        __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str compartment_id: (required)
            The ID of the compartment in which to list buckets.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important
            details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param list[str] fields: (optional)
            Bucket summary in list of buckets includes the 'namespace', 'name', 'compartmentId', 'createdBy', 'timeCreated',
            and 'etag' fields. This parameter can also include 'tags' (freeformTags and definedTags). The only supported value of this parameter is 'tags' for now. Example 'tags'.

            Allowed values are: "tags"

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.BucketSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/list_buckets.py.html>`__ to see an example of how to use list_buckets API.
        """
        resource_path = "/n/{namespaceName}/b"
        method = "GET"
        operation_name = "list_buckets"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Bucket/ListBuckets"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[BucketSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[BucketSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important
            details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.MultipartUploadPartSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/list_multipart_upload_parts.py.html>`__ to see an example of how to use list_multipart_upload_parts API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u/{objectName}"
        method = "GET"
        operation_name = "list_multipart_upload_parts"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/MultipartUpload/ListMultipartUploadParts"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[MultipartUploadPartSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[MultipartUploadPartSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_multipart_uploads(self, namespace_name, bucket_name, **kwargs):
        """
        Lists all of the in-progress multipart uploads for the given bucket in the given Object Storage namespace.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important
            details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.MultipartUpload`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/list_multipart_uploads.py.html>`__ to see an example of how to use list_multipart_uploads API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u"
        method = "GET"
        operation_name = "list_multipart_uploads"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/MultipartUpload/ListMultipartUploads"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[MultipartUpload]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[MultipartUpload]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_object_versions(self, namespace_name, bucket_name, **kwargs):
        """
        Lists the object versions in a bucket.

        ListObjectVersions returns an ObjectVersionCollection containing at most 1000 object versions. To paginate through
        more object versions, use the returned `opc-next-page` value with the `page` request parameter.

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
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str delimiter: (optional)
            When this parameter is set, only objects whose names do not contain the delimiter character
            (after an optionally specified prefix) are returned in the objects key of the response body.
            Scanned objects whose names contain the delimiter have the part of their name up to the first
            occurrence of the delimiter (including the optional prefix) returned as a set of prefixes.
            Note that only '/' is a supported delimiter character at this time.

        :param str fields: (optional)
            Object summary by default includes only the 'name' field. Use this parameter to also
            include 'size' (object size in bytes), 'etag', 'md5', 'timeCreated' (object creation date and time),
            'timeModified' (object modification date and time), 'storageTier' and 'archivalState' fields.
            Specify the value of this parameter as a comma-separated, case-insensitive list of those field names.
            For example 'name,etag,timeCreated,md5,timeModified,storageTier,archivalState'.

            Allowed values are: "name", "size", "etag", "timeCreated", "md5", "timeModified", "storageTier", "archivalState"

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str start_after: (optional)
            Object names returned by a list query must be greater than this parameter.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important
            details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.ObjectVersionCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/list_object_versions.py.html>`__ to see an example of how to use list_object_versions API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/objectversions"
        method = "GET"
        operation_name = "list_object_versions"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Object/ListObjectVersions"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ObjectVersionCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ObjectVersionCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_objects(self, namespace_name, bucket_name, **kwargs):
        """
        Lists the objects in a bucket. By default, ListObjects returns object names only. See the `fields`
        parameter for other fields that you can optionally include in ListObjects response.

        ListObjects returns at most 1000 objects. To paginate through more objects, use the returned 'nextStartWith'
        value with the 'start' parameter. To filter which objects ListObjects returns, use the 'start' and 'end'
        parameters.

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
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str delimiter: (optional)
            When this parameter is set, only objects whose names do not contain the delimiter character
            (after an optionally specified prefix) are returned in the objects key of the response body.
            Scanned objects whose names contain the delimiter have the part of their name up to the first
            occurrence of the delimiter (including the optional prefix) returned as a set of prefixes.
            Note that only '/' is a supported delimiter character at this time.

        :param str fields: (optional)
            Object summary by default includes only the 'name' field. Use this parameter to also
            include 'size' (object size in bytes), 'etag', 'md5', 'timeCreated' (object creation date and time),
            'timeModified' (object modification date and time), 'storageTier' and 'archivalState' fields.
            Specify the value of this parameter as a comma-separated, case-insensitive list of those field names.
            For example 'name,etag,timeCreated,md5,timeModified,storageTier,archivalState'.

            Allowed values are: "name", "size", "etag", "timeCreated", "md5", "timeModified", "storageTier", "archivalState"

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str start_after: (optional)
            Object names returned by a list query must be greater than this parameter.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.ListObjects`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/list_objects.py.html>`__ to see an example of how to use list_objects API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/o"
        method = "GET"
        operation_name = "list_objects"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Object/ListObjects"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ListObjects",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ListObjects",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important
            details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.PreauthenticatedRequestSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/list_preauthenticated_requests.py.html>`__ to see an example of how to use list_preauthenticated_requests API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/p"
        method = "GET"
        operation_name = "list_preauthenticated_requests"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/PreauthenticatedRequest/ListPreauthenticatedRequests"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PreauthenticatedRequestSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PreauthenticatedRequestSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important
            details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.ReplicationPolicySummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/list_replication_policies.py.html>`__ to see an example of how to use list_replication_policies API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/replicationPolicies"
        method = "GET"
        operation_name = "list_replication_policies"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Replication/ListReplicationPolicies"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ReplicationPolicySummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ReplicationPolicySummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important
            details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.ReplicationSource`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/list_replication_sources.py.html>`__ to see an example of how to use list_replication_sources API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/replicationSources"
        method = "GET"
        operation_name = "list_replication_sources"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Replication/ListReplicationSources"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ReplicationSource]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ReplicationSource]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important
            details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.RetentionRuleCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/list_retention_rules.py.html>`__ to see an example of how to use list_retention_rules API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/retentionRules"
        method = "GET"
        operation_name = "list_retention_rules"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/RetentionRule/ListRetentionRules"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RetentionRuleCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RetentionRuleCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_work_request_errors(self, work_request_id, **kwargs):
        """
        Lists the errors of the work request with the given ID.


        :param str work_request_id: (required)
            The ID of the asynchronous request.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important
            details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.WorkRequestError`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/list_work_request_errors.py.html>`__ to see an example of how to use list_work_request_errors API.
        """
        resource_path = "/workRequests/{workRequestId}/errors"
        method = "GET"
        operation_name = "list_work_request_errors"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/WorkRequestError/ListWorkRequestErrors"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestError]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestError]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_work_request_logs(self, work_request_id, **kwargs):
        """
        Lists the logs of the work request with the given ID.


        :param str work_request_id: (required)
            The ID of the asynchronous request.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important
            details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.WorkRequestLogEntry`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/list_work_request_logs.py.html>`__ to see an example of how to use list_work_request_logs API.
        """
        resource_path = "/workRequests/{workRequestId}/logs"
        method = "GET"
        operation_name = "list_work_request_logs"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/WorkRequestLogEntry/ListWorkRequestLogs"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestLogEntry]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestLogEntry]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_work_requests(self, compartment_id, **kwargs):
        """
        Lists the work requests in a compartment.


        :param str compartment_id: (required)
            The ID of the compartment in which to list buckets.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important
            details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.object_storage.models.WorkRequestSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/list_work_requests.py.html>`__ to see an example of how to use list_work_requests API.
        """
        resource_path = "/workRequests"
        method = "GET"
        operation_name = "list_work_requests"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/WorkRequest/ListWorkRequests"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/make_bucket_writable.py.html>`__ to see an example of how to use make_bucket_writable API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/actions/makeBucketWritable"
        method = "POST"
        operation_name = "make_bucket_writable"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Replication/MakeBucketWritable"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of
            the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload
            the resource.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should
            fail if the resource already exists.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param str expect: (optional)
            A value of `100-continue` requests preliminary verification of the request method, path, and headers before the request body is sent.
            If no error results from such verification, the server will send a 100 (Continue) interim response to indicate readiness for the request body.
            The only allowed value for this parameter is \"100-Continue\" (case-insensitive).

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

        :param str opc_sse_kms_key_id: (optional)
            The `OCID`__ of a master encryption key used to call the Key
            Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str storage_tier: (optional)
            The storage tier that the object should be stored in. If not specified, the object will be stored in
            the same storage tier as the bucket.

            Allowed values are: "Standard", "InfrequentAccess", "Archive"

        :param dict(str, str) opc_meta: (optional)
            Optional user-defined metadata key and value.

            "opc-meta-" will be appended to each dict key before it is sent to the server.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings
        :param int buffer_limit: (optional)
            A buffer limit for the stream to be buffered. buffer_limit is used to set the buffer size capacity. Streams will be read until the size of the buffer reaches the buffer_limit.
            If the stream size is greater than the buffer_limit, a BufferError exception will be thrown.

            The buffer_limit parameter is used when the stream object does not have a `seek`, `tell`, or `fileno` property for the Python Request library to calculate out the content length.
            If buffer_limit is not passed, then the buffer_limit will be defaulted to 100MB.
            Large streams can cause the process to freeze, consider passing in content-length for large streams instead.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/put_object.py.html>`__ to see an example of how to use put_object API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/o/{objectName}"
        method = "PUT"
        operation_name = "put_object"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Object/PutObject"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "buffer_limit",
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
            "opc_sse_kms_key_id",
            "storage_tier",
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
            "opc-sse-kms-key-id": kwargs.get("opc_sse_kms_key_id", missing),
            "storage-tier": kwargs.get("storage_tier", missing),

        }
        for key, value in six.iteritems(kwargs.get("opc_meta", {})):
            header_params["opc-meta-" + key] = value
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}
        # Set default value for expect header if user has not overridden it
        lowercase_header_params_keys = [k.lower() for k in header_params]
        if "expect" not in lowercase_header_params_keys:
            header_params["expect"] = "100-continue"

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

            # If content length is not given and stream object have no 'fileno' and is not a string or bytes, try to calculate content length
            elif 'Content-Length' not in header_params and not is_content_length_calculable_by_req_util(put_object_body):
                calculated_obj = back_up_body_calculate_stream_content_length(put_object_body, kwargs.get("buffer_limit"))
                header_params['Content-Length'] = calculated_obj["content_length"]
                put_object_body = calculated_obj["byte_content"]

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=put_object_body,
                enforce_content_headers=False,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=put_object_body,
                enforce_content_headers=False,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of
            the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload
            the resource.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should
            fail if the resource already exists.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.ObjectLifecyclePolicy`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/put_object_lifecycle_policy.py.html>`__ to see an example of how to use put_object_lifecycle_policy API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/l"
        method = "PUT"
        operation_name = "put_object_lifecycle_policy"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/ObjectLifecyclePolicy/PutObjectLifecyclePolicy"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=put_object_lifecycle_policy_details,
                response_type="ObjectLifecyclePolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=put_object_lifecycle_policy_details,
                response_type="ObjectLifecyclePolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/reencrypt_bucket.py.html>`__ to see an example of how to use reencrypt_bucket API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/actions/reencrypt"
        method = "POST"
        operation_name = "reencrypt_bucket"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Bucket/ReencryptBucket"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/reencrypt_object.py.html>`__ to see an example of how to use reencrypt_object API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/actions/reencrypt/{objectName}"
        method = "POST"
        operation_name = "reencrypt_object"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Object/ReencryptObject"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=reencrypt_object_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=reencrypt_object_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            The sourceName and newName of rename operation. Avoid entering confidential information.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/rename_object.py.html>`__ to see an example of how to use rename_object API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/actions/renameObject"
        method = "POST"
        operation_name = "rename_object"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Object/RenameObject"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=rename_object_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=rename_object_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/restore_objects.py.html>`__ to see an example of how to use restore_objects API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/actions/restoreObjects"
        method = "POST"
        operation_name = "restore_objects"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Object/RestoreObjects"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=restore_objects_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=restore_objects_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of
            the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload
            the resource.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.Bucket`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/update_bucket.py.html>`__ to see an example of how to use update_bucket API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}"
        method = "POST"
        operation_name = "update_bucket"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Bucket/UpdateBucket"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_bucket_details,
                response_type="Bucket",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_bucket_details,
                response_type="Bucket",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.NamespaceMetadata`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/update_namespace_metadata.py.html>`__ to see an example of how to use update_namespace_metadata API.
        """
        resource_path = "/n/{namespaceName}"
        method = "PUT"
        operation_name = "update_namespace_metadata"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Namespace/UpdateNamespaceMetadata"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_namespace_metadata_details,
                response_type="NamespaceMetadata",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_namespace_metadata_details,
                response_type="NamespaceMetadata",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_object_storage_tier(self, namespace_name, bucket_name, update_object_storage_tier_details, **kwargs):
        """
        Changes the storage tier of the object specified by the objectName parameter.


        :param str namespace_name: (required)
            The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param oci.object_storage.models.UpdateObjectStorageTierDetails update_object_storage_tier_details: (required)
            The object name and the desired storage tier.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/update_object_storage_tier.py.html>`__ to see an example of how to use update_object_storage_tier API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/actions/updateObjectStorageTier"
        method = "POST"
        operation_name = "update_object_storage_tier"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/Object/UpdateObjectStorageTier"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_client_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_object_storage_tier got unknown kwargs: {!r}".format(extra_kwargs))

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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_object_storage_tier_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_object_storage_tier_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of
            the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload
            the resource.

        :param str opc_client_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.object_storage.models.RetentionRule`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/update_retention_rule.py.html>`__ to see an example of how to use update_retention_rule API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/retentionRules/{retentionRuleId}"
        method = "PUT"
        operation_name = "update_retention_rule"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/RetentionRule/UpdateRetentionRule"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_retention_rule_details,
                response_type="RetentionRule",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_retention_rule_details,
                response_type="RetentionRule",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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
            The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches the ETag of
            the existing resource, GET and HEAD requests will return the resource and PUT and POST requests will upload
            the resource.

        :param str if_none_match: (optional)
            The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should
            fail if the resource already exists.

        :param str expect: (optional)
            A value of `100-continue` requests preliminary verification of the request method, path, and headers before the request body is sent.
            If no error results from such verification, the server will send a 100 (Continue) interim response to indicate readiness for the request body.
            The only allowed value for this parameter is \"100-Continue\" (case-insensitive).

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

        :param str opc_sse_kms_key_id: (optional)
            The `OCID`__ of a master encryption key used to call the Key
            Management service to generate a data encryption key or to encrypt or decrypt a data encryption key.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings
        :param int buffer_limit: (optional)
            A buffer limit for the stream to be buffered. buffer_limit is used to set the buffer size capacity. Streams will be read until the size of the buffer reaches the buffer_limit.
            If the stream size is greater than the buffer_limit, a BufferError exception will be thrown.

            The buffer_limit parameter is used when the stream object does not have a `seek`, `tell`, or `fileno` property for the Python Request library to calculate out the content length.
            If buffer_limit is not passed, then the buffer_limit will be defaulted to 100MB.
            Large streams can cause the process to freeze, consider passing in content-length for large streams instead.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/objectstorage/upload_part.py.html>`__ to see an example of how to use upload_part API.
        """
        resource_path = "/n/{namespaceName}/b/{bucketName}/u/{objectName}"
        method = "PUT"
        operation_name = "upload_part"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/objectstorage/20160918/MultipartUpload/UploadPart"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "buffer_limit",
            "content_length",
            "opc_client_request_id",
            "if_match",
            "if_none_match",
            "expect",
            "content_md5",
            "opc_sse_customer_algorithm",
            "opc_sse_customer_key",
            "opc_sse_customer_key_sha256",
            "opc_sse_kms_key_id"
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
            "opc-sse-customer-key-sha256": kwargs.get("opc_sse_customer_key_sha256", missing),
            "opc-sse-kms-key-id": kwargs.get("opc_sse_kms_key_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}
        # Set default value for expect header if user has not overridden it
        lowercase_header_params_keys = [k.lower() for k in header_params]
        if "expect" not in lowercase_header_params_keys:
            header_params["expect"] = "100-continue"

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

            # If content length is not given and stream object have no 'fileno' and is not a string or bytes, try to calculate content length
            elif 'Content-Length' not in header_params and not is_content_length_calculable_by_req_util(upload_part_body):
                calculated_obj = back_up_body_calculate_stream_content_length(upload_part_body, kwargs.get("buffer_limit"))
                header_params['Content-Length'] = calculated_obj["content_length"]
                upload_part_body = calculated_obj["byte_content"]

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=upload_part_body,
                enforce_content_headers=False,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=upload_part_body,
                enforce_content_headers=False,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
