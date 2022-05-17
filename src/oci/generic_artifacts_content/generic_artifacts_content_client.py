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
from .models import generic_artifacts_content_type_mapping
missing = Sentinel("Missing")


class GenericArtifactsContentClient(object):
    """
    API covering the Generic Artifacts Service content
    Use this API to put and get generic artifact content.
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
            'base_path': '/20160918',
            'service_endpoint_template': 'https://generic.artifacts.{region}.oci.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'circuit_breaker_strategy': kwargs.get('circuit_breaker_strategy', circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY)
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        if base_client_init_kwargs.get('circuit_breaker_strategy') is None:
            base_client_init_kwargs['circuit_breaker_strategy'] = circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY
        if 'allow_control_chars' in kwargs:
            base_client_init_kwargs['allow_control_chars'] = kwargs.get('allow_control_chars')
        self.base_client = BaseClient("generic_artifacts_content", config, signer, generic_artifacts_content_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

    def get_generic_artifact_content(self, artifact_id, **kwargs):
        """
        Gets the specified artifact's content.


        :param str artifact_id: (required)
            The `OCID`__ of the artifact.

            Example: `ocid1.genericartifact.oc1..exampleuniqueID`

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned `request ID`__

            Example: `bxxxxxxx-fxxx-4xxx-9xxx-bxxxxxxxxxxx`
            If you contact Oracle about a request, provide this request ID.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/genericartifactscontent/get_generic_artifact_content.py.html>`__ to see an example of how to use get_generic_artifact_content API.
        """
        resource_path = "/generic/artifacts/{artifactId}/content"
        method = "GET"
        operation_name = "get_generic_artifact_content"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/generic/20160918/GenericArtifact/GetGenericArtifactContent"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_generic_artifact_content got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "artifactId": artifact_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/octet-stream",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

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
                response_type="stream",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_generic_artifact_content_by_path(self, repository_id, artifact_path, version, **kwargs):
        """
        Gets the content of an artifact with a specified `artifactPath` and `version`.


        :param str repository_id: (required)
            The `OCID`__ of the repository.

            Example: `ocid1.repository.oc1..exampleuniqueID`

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str artifact_path: (required)
            A user-defined path to describe the location of an artifact. You can use slashes to organize the repository, but slashes do not create a directory structure. An artifact path does not include an artifact version.

            Example: `project01/my-web-app/artifact-abc`

        :param str version: (required)
            A user-defined string to describe the artifact version.

            Example: `1.1.2` or `1.2-beta-2`

        :param str opc_request_id: (optional)
            Unique Oracle-assigned `request ID`__

            Example: `bxxxxxxx-fxxx-4xxx-9xxx-bxxxxxxxxxxx`
            If you contact Oracle about a request, provide this request ID.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/genericartifactscontent/get_generic_artifact_content_by_path.py.html>`__ to see an example of how to use get_generic_artifact_content_by_path API.
        """
        resource_path = "/generic/repositories/{repositoryId}/artifactPaths/{artifactPath}/versions/{version}/content"
        method = "GET"
        operation_name = "get_generic_artifact_content_by_path"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/generic/20160918/GenericArtifact/GetGenericArtifactContentByPath"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_generic_artifact_content_by_path got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "repositoryId": repository_id,
            "artifactPath": artifact_path,
            "version": version
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/octet-stream",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

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
                response_type="stream",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def put_generic_artifact_content_by_path(self, repository_id, artifact_path, version, generic_artifact_content_body, **kwargs):
        """
        Uploads an artifact. Provide `artifactPath`, `version` and content. Avoid entering confidential information when you define the path and version.


        :param str repository_id: (required)
            The `OCID`__ of the repository.

            Example: `ocid1.repository.oc1..exampleuniqueID`

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str artifact_path: (required)
            A user-defined path to describe the location of an artifact. You can use slashes to organize the repository, but slashes do not create a directory structure. An artifact path does not include an artifact version.

            Example: `project01/my-web-app/artifact-abc`

        :param str version: (required)
            A user-defined string to describe the artifact version.

            Example: `1.1.2` or `1.2-beta-2`

        :param stream generic_artifact_content_body: (required)
            Uploads an artifact. Provide artifact path, version and content. Avoid entering confidential information when you define the path and version.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned `request ID`__

            Example: `bxxxxxxx-fxxx-4xxx-9xxx-bxxxxxxxxxxx`
            If you contact Oracle about a request, provide this request ID.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.generic_artifacts_content.models.GenericArtifact`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/genericartifactscontent/put_generic_artifact_content_by_path.py.html>`__ to see an example of how to use put_generic_artifact_content_by_path API.
        """
        resource_path = "/generic/repositories/{repositoryId}/artifactPaths/{artifactPath}/versions/{version}/content"
        method = "PUT"
        operation_name = "put_generic_artifact_content_by_path"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/generic/20160918/GenericArtifact/PutGenericArtifactContentByPath"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "buffer_limit",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "put_generic_artifact_content_by_path got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "repositoryId": repository_id,
            "artifactPath": artifact_path,
            "version": version
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        # If the body parameter is optional we need to assign it to a variable so additional type checking can be performed.
        try:
            generic_artifact_content_body
        except NameError:
            generic_artifact_content_body = kwargs.get("generic_artifact_content_body", missing)

        if generic_artifact_content_body is not missing and generic_artifact_content_body is not None:
            if (not isinstance(generic_artifact_content_body, (six.binary_type, six.string_types)) and
                    not hasattr(generic_artifact_content_body, "read")):
                raise TypeError('The body must be a string, bytes, or provide a read() method.')

            if hasattr(generic_artifact_content_body, 'fileno') and hasattr(generic_artifact_content_body, 'name') and generic_artifact_content_body.name != '<stdin>':
                if requests.utils.super_len(generic_artifact_content_body) == 0:
                    header_params['Content-Length'] = '0'

            # If content length is not given and stream object have no 'fileno' and is not a string or bytes, try to calculate content length
            elif 'Content-Length' not in header_params and not is_content_length_calculable_by_req_util(generic_artifact_content_body):
                calculated_obj = back_up_body_calculate_stream_content_length(generic_artifact_content_body, kwargs.get("buffer_limit"))
                header_params['Content-Length'] = calculated_obj["content_length"]
                generic_artifact_content_body = calculated_obj["byte_content"]

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

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
                body=generic_artifact_content_body,
                response_type="GenericArtifact",
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
                body=generic_artifact_content_body,
                response_type="GenericArtifact",
                enforce_content_headers=False,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
