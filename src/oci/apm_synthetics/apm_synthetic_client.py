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
from .models import apm_synthetics_type_mapping
missing = Sentinel("Missing")


class ApmSyntheticClient(object):
    """
    Use the Application Performance Monitoring Synthetic Monitoring API to query synthetic scripts and monitors. For more information, see [Application Performance Monitoring](https://docs.oracle.com/iaas/application-performance-monitoring/index.html).
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
            'base_path': '/20200630',
            'service_endpoint_template': 'https://apm-synthetic.{region}.oci.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'circuit_breaker_strategy': kwargs.get('circuit_breaker_strategy', circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY)
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        if base_client_init_kwargs.get('circuit_breaker_strategy') is None:
            base_client_init_kwargs['circuit_breaker_strategy'] = circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY
        if 'allow_control_chars' in kwargs:
            base_client_init_kwargs['allow_control_chars'] = kwargs.get('allow_control_chars')
        self.base_client = BaseClient("apm_synthetic", config, signer, apm_synthetics_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

    def create_dedicated_vantage_point(self, apm_domain_id, create_dedicated_vantage_point_details, **kwargs):
        """
        Registers a new dedicated vantage point.


        :param str apm_domain_id: (required)
            The APM domain ID the request is intended for.

        :param oci.apm_synthetics.models.CreateDedicatedVantagePointDetails create_dedicated_vantage_point_details: (required)
            The configuration details for registering a dedicated vantage point.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.apm_synthetics.models.DedicatedVantagePoint`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/apmsynthetics/create_dedicated_vantage_point.py.html>`__ to see an example of how to use create_dedicated_vantage_point API.
        """
        resource_path = "/dedicatedVantagePoints"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_dedicated_vantage_point got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "apmDomainId": apm_domain_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=create_dedicated_vantage_point_details,
                response_type="DedicatedVantagePoint")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=create_dedicated_vantage_point_details,
                response_type="DedicatedVantagePoint")

    def create_monitor(self, apm_domain_id, create_monitor_details, **kwargs):
        """
        Creates a new monitor.


        :param str apm_domain_id: (required)
            The APM domain ID the request is intended for.

        :param oci.apm_synthetics.models.CreateMonitorDetails create_monitor_details: (required)
            The configuration details for creating a monitor.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.apm_synthetics.models.Monitor`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/apmsynthetics/create_monitor.py.html>`__ to see an example of how to use create_monitor API.
        """
        resource_path = "/monitors"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_monitor got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "apmDomainId": apm_domain_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=create_monitor_details,
                response_type="Monitor")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=create_monitor_details,
                response_type="Monitor")

    def create_script(self, apm_domain_id, create_script_details, **kwargs):
        """
        Creates a new script.


        :param str apm_domain_id: (required)
            The APM domain ID the request is intended for.

        :param oci.apm_synthetics.models.CreateScriptDetails create_script_details: (required)
            The configuration details for creating a script.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.apm_synthetics.models.Script`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/apmsynthetics/create_script.py.html>`__ to see an example of how to use create_script API.
        """
        resource_path = "/scripts"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_script got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "apmDomainId": apm_domain_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=create_script_details,
                response_type="Script")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=create_script_details,
                response_type="Script")

    def delete_dedicated_vantage_point(self, apm_domain_id, dedicated_vantage_point_id, **kwargs):
        """
        Deregisters the specified dedicated vantage point.


        :param str apm_domain_id: (required)
            The APM domain ID the request is intended for.

        :param str dedicated_vantage_point_id: (required)
            The OCID of the dedicated vantage point.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/apmsynthetics/delete_dedicated_vantage_point.py.html>`__ to see an example of how to use delete_dedicated_vantage_point API.
        """
        resource_path = "/dedicatedVantagePoints/{dedicatedVantagePointId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_dedicated_vantage_point got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dedicatedVantagePointId": dedicated_vantage_point_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "apmDomainId": apm_domain_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)

    def delete_monitor(self, apm_domain_id, monitor_id, **kwargs):
        """
        Deletes the specified monitor.


        :param str apm_domain_id: (required)
            The APM domain ID the request is intended for.

        :param str monitor_id: (required)
            The OCID of the monitor.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/apmsynthetics/delete_monitor.py.html>`__ to see an example of how to use delete_monitor API.
        """
        resource_path = "/monitors/{monitorId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_monitor got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "monitorId": monitor_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "apmDomainId": apm_domain_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)

    def delete_script(self, apm_domain_id, script_id, **kwargs):
        """
        Deletes the specified script.


        :param str apm_domain_id: (required)
            The APM domain ID the request is intended for.

        :param str script_id: (required)
            The OCID of the script.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/apmsynthetics/delete_script.py.html>`__ to see an example of how to use delete_script API.
        """
        resource_path = "/scripts/{scriptId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_script got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "scriptId": script_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "apmDomainId": apm_domain_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)

    def get_dedicated_vantage_point(self, apm_domain_id, dedicated_vantage_point_id, **kwargs):
        """
        Gets the details of the dedicated vantage point identified by the OCID.


        :param str apm_domain_id: (required)
            The APM domain ID the request is intended for.

        :param str dedicated_vantage_point_id: (required)
            The OCID of the dedicated vantage point.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.apm_synthetics.models.DedicatedVantagePoint`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/apmsynthetics/get_dedicated_vantage_point.py.html>`__ to see an example of how to use get_dedicated_vantage_point API.
        """
        resource_path = "/dedicatedVantagePoints/{dedicatedVantagePointId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_dedicated_vantage_point got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dedicatedVantagePointId": dedicated_vantage_point_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "apmDomainId": apm_domain_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="DedicatedVantagePoint")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DedicatedVantagePoint")

    def get_monitor(self, apm_domain_id, monitor_id, **kwargs):
        """
        Gets the configuration of the monitor identified by the OCID.


        :param str apm_domain_id: (required)
            The APM domain ID the request is intended for.

        :param str monitor_id: (required)
            The OCID of the monitor.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.apm_synthetics.models.Monitor`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/apmsynthetics/get_monitor.py.html>`__ to see an example of how to use get_monitor API.
        """
        resource_path = "/monitors/{monitorId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_monitor got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "monitorId": monitor_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "apmDomainId": apm_domain_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="Monitor")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="Monitor")

    def get_monitor_result(self, apm_domain_id, monitor_id, vantage_point, result_type, result_content_type, execution_time, **kwargs):
        """
        Gets the results for a specific execution of a monitor identified by OCID. The results are in a HAR file, Screenshot, Console Log or Network details.


        :param str apm_domain_id: (required)
            The APM domain ID the request is intended for.

        :param str monitor_id: (required)
            The OCID of the monitor.

        :param str vantage_point: (required)
            The vantagePoint name.

        :param str result_type: (required)
            The result type: har, screenshot, log, or network.

        :param str result_content_type: (required)
            The result content type: zip or raw.

        :param str execution_time: (required)
            The time the object was posted.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.apm_synthetics.models.MonitorResult`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/apmsynthetics/get_monitor_result.py.html>`__ to see an example of how to use get_monitor_result API.
        """
        resource_path = "/monitors/{monitorId}/results/{executionTime}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_monitor_result got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "monitorId": monitor_id,
            "executionTime": execution_time
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "apmDomainId": apm_domain_id,
            "vantagePoint": vantage_point,
            "resultType": result_type,
            "resultContentType": result_content_type
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="MonitorResult")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="MonitorResult")

    def get_script(self, apm_domain_id, script_id, **kwargs):
        """
        Gets the configuration of the script identified by the OCID.


        :param str apm_domain_id: (required)
            The APM domain ID the request is intended for.

        :param str script_id: (required)
            The OCID of the script.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.apm_synthetics.models.Script`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/apmsynthetics/get_script.py.html>`__ to see an example of how to use get_script API.
        """
        resource_path = "/scripts/{scriptId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_script got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "scriptId": script_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "apmDomainId": apm_domain_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="Script")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="Script")

    def list_dedicated_vantage_points(self, apm_domain_id, **kwargs):
        """
        Returns a list of dedicated vantage points.


        :param str apm_domain_id: (required)
            The APM domain ID the request is intended for.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). Default sort order is ascending.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Only one sort order may be provided.
            Default order of displayName is ascending.
            Default order of timeCreated and timeUpdated is descending.
            The displayName sort by is case sensitive.

            Allowed values are: "displayName", "name", "timeCreated", "timeUpdated", "status"

        :param str display_name: (optional)
            A filter to return only the resources that match the entire display name.

        :param str name: (optional)
            A filter to return only the resources that match the entire name.

        :param str status: (optional)
            A filter to return only the dedicated vantage points that match a given status.

            Allowed values are: "ENABLED", "DISABLED"

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.apm_synthetics.models.DedicatedVantagePointCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/apmsynthetics/list_dedicated_vantage_points.py.html>`__ to see an example of how to use list_dedicated_vantage_points API.
        """
        resource_path = "/dedicatedVantagePoints"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "display_name",
            "name",
            "status",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_dedicated_vantage_points got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["displayName", "name", "timeCreated", "timeUpdated", "status"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'status' in kwargs:
            status_allowed_values = ["ENABLED", "DISABLED"]
            if kwargs['status'] not in status_allowed_values:
                raise ValueError(
                    "Invalid value for `status`, must be one of {0}".format(status_allowed_values)
                )

        query_params = {
            "apmDomainId": apm_domain_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "displayName": kwargs.get("display_name", missing),
            "name": kwargs.get("name", missing),
            "status": kwargs.get("status", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="DedicatedVantagePointCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="DedicatedVantagePointCollection")

    def list_monitors(self, apm_domain_id, **kwargs):
        """
        Returns a list of monitors.


        :param str apm_domain_id: (required)
            The APM domain ID the request is intended for.

        :param str display_name: (optional)
            A filter to return only the resources that match the entire display name.

        :param str script_id: (optional)
            A filter to return only monitors using scriptId.

        :param str vantage_point: (optional)
            The name of the public or dedicated vantage point.

        :param str monitor_type: (optional)
            A filter to return only monitors that match the given monitor type.
            Supported values are SCRIPTED_BROWSER, BROWSER, SCRIPTED_REST and REST.

        :param str status: (optional)
            A filter to return only monitors that match the status given.

            Allowed values are: "ENABLED", "DISABLED", "INVALID"

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). Default sort order is ascending.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Only one sort order may be provided.
            Default order of displayName is ascending.
            Default order of timeCreated and timeUpdated is descending.
            The displayName sort by is case insensitive.

            Allowed values are: "displayName", "timeCreated", "timeUpdated", "status", "monitorType"

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.apm_synthetics.models.MonitorCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/apmsynthetics/list_monitors.py.html>`__ to see an example of how to use list_monitors API.
        """
        resource_path = "/monitors"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "display_name",
            "script_id",
            "vantage_point",
            "monitor_type",
            "status",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_monitors got unknown kwargs: {!r}".format(extra_kwargs))

        if 'status' in kwargs:
            status_allowed_values = ["ENABLED", "DISABLED", "INVALID"]
            if kwargs['status'] not in status_allowed_values:
                raise ValueError(
                    "Invalid value for `status`, must be one of {0}".format(status_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["displayName", "timeCreated", "timeUpdated", "status", "monitorType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "apmDomainId": apm_domain_id,
            "displayName": kwargs.get("display_name", missing),
            "scriptId": kwargs.get("script_id", missing),
            "vantagePoint": kwargs.get("vantage_point", missing),
            "monitorType": kwargs.get("monitor_type", missing),
            "status": kwargs.get("status", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="MonitorCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="MonitorCollection")

    def list_public_vantage_points(self, apm_domain_id, **kwargs):
        """
        Returns a list of public vantage points.


        :param str apm_domain_id: (required)
            The APM domain ID the request is intended for.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). Default sort order is ascending.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort by (`sortBy`). Default order for displayName or name is ascending. The displayName or name
            sort by is case insensitive.

            Allowed values are: "name", "displayName"

        :param str display_name: (optional)
            A filter to return only the resources that match the entire display name.

        :param str name: (optional)
            A filter to return only the resources that match the entire name.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.apm_synthetics.models.PublicVantagePointCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/apmsynthetics/list_public_vantage_points.py.html>`__ to see an example of how to use list_public_vantage_points API.
        """
        resource_path = "/publicVantagePoints"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "display_name",
            "name",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_public_vantage_points got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["name", "displayName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "apmDomainId": apm_domain_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "displayName": kwargs.get("display_name", missing),
            "name": kwargs.get("name", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="PublicVantagePointCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="PublicVantagePointCollection")

    def list_scripts(self, apm_domain_id, **kwargs):
        """
        Returns a list of scripts.


        :param str apm_domain_id: (required)
            The APM domain ID the request is intended for.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str display_name: (optional)
            A filter to return only the resources that match the entire display name.

        :param str content_type: (optional)
            A filter to return only resources that match the content type given.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). Default sort order is ascending.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Only one sort order may be provided.
            Default order of displayName and contentType is ascending.
            Default order of timeCreated and timeUpdated is descending.
            The displayName sort by is case insensitive.

            Allowed values are: "displayName", "timeCreated", "timeUpdated", "contentType"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.apm_synthetics.models.ScriptCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/apmsynthetics/list_scripts.py.html>`__ to see an example of how to use list_scripts API.
        """
        resource_path = "/scripts"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "display_name",
            "content_type",
            "limit",
            "page",
            "sort_order",
            "sort_by"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_scripts got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["displayName", "timeCreated", "timeUpdated", "contentType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "apmDomainId": apm_domain_id,
            "displayName": kwargs.get("display_name", missing),
            "contentType": kwargs.get("content_type", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="ScriptCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ScriptCollection")

    def update_dedicated_vantage_point(self, apm_domain_id, dedicated_vantage_point_id, update_dedicated_vantage_point_details, **kwargs):
        """
        Updates the dedicated vantage point.


        :param str apm_domain_id: (required)
            The APM domain ID the request is intended for.

        :param str dedicated_vantage_point_id: (required)
            The OCID of the dedicated vantage point.

        :param oci.apm_synthetics.models.UpdateDedicatedVantagePointDetails update_dedicated_vantage_point_details: (required)
            The information to be updated.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.apm_synthetics.models.DedicatedVantagePoint`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/apmsynthetics/update_dedicated_vantage_point.py.html>`__ to see an example of how to use update_dedicated_vantage_point API.
        """
        resource_path = "/dedicatedVantagePoints/{dedicatedVantagePointId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_dedicated_vantage_point got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dedicatedVantagePointId": dedicated_vantage_point_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "apmDomainId": apm_domain_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                body=update_dedicated_vantage_point_details,
                response_type="DedicatedVantagePoint")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_dedicated_vantage_point_details,
                response_type="DedicatedVantagePoint")

    def update_monitor(self, apm_domain_id, monitor_id, update_monitor_details, **kwargs):
        """
        Updates the monitor.


        :param str apm_domain_id: (required)
            The APM domain ID the request is intended for.

        :param str monitor_id: (required)
            The OCID of the monitor.

        :param oci.apm_synthetics.models.UpdateMonitorDetails update_monitor_details: (required)
            The information to be updated.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.apm_synthetics.models.Monitor`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/apmsynthetics/update_monitor.py.html>`__ to see an example of how to use update_monitor API.
        """
        resource_path = "/monitors/{monitorId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_monitor got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "monitorId": monitor_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "apmDomainId": apm_domain_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                body=update_monitor_details,
                response_type="Monitor")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_monitor_details,
                response_type="Monitor")

    def update_script(self, apm_domain_id, script_id, update_script_details, **kwargs):
        """
        Updates the script.


        :param str apm_domain_id: (required)
            The APM domain ID the request is intended for.

        :param str script_id: (required)
            The OCID of the script.

        :param oci.apm_synthetics.models.UpdateScriptDetails update_script_details: (required)
            The information to be updated.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.apm_synthetics.models.Script`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/apmsynthetics/update_script.py.html>`__ to see an example of how to use update_script API.
        """
        resource_path = "/scripts/{scriptId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_script got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "scriptId": script_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "apmDomainId": apm_domain_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                body=update_script_details,
                response_type="Script")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_script_details,
                response_type="Script")
