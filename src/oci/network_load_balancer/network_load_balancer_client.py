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
from .models import network_load_balancer_type_mapping
missing = Sentinel("Missing")


class NetworkLoadBalancerClient(object):
    """
    This describes the network load balancer API.
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
            'base_path': '/20200501',
            'service_endpoint_template': 'https://network-load-balancer-api.{region}.oci.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'circuit_breaker_strategy': kwargs.get('circuit_breaker_strategy', circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY)
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        if base_client_init_kwargs.get('circuit_breaker_strategy') is None:
            base_client_init_kwargs['circuit_breaker_strategy'] = circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY
        if 'allow_control_chars' in kwargs:
            base_client_init_kwargs['allow_control_chars'] = kwargs.get('allow_control_chars')
        self.base_client = BaseClient("network_load_balancer", config, signer, network_load_balancer_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

    def change_network_load_balancer_compartment(self, network_load_balancer_id, change_network_load_balancer_compartment_details, **kwargs):
        """
        Moves a network load balancer into a different compartment within the same tenancy. For information about moving resources
        between compartments, see `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.ChangeNetworkLoadBalancerCompartmentDetails change_network_load_balancer_compartment_details: (required)
            The configuration details for moving a network load balancer to a different compartment.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that it can be retried in case of a timeout or
            server error without risk of rerunning that same action. Retry tokens expire after 24
            hours but they can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the current etag value of the resource.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/change_network_load_balancer_compartment.py.html>`__ to see an example of how to use change_network_load_balancer_compartment API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_network_load_balancer_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/NetworkLoadBalancer/ChangeNetworkLoadBalancerCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_network_load_balancer_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_network_load_balancer_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_network_load_balancer_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_backend(self, network_load_balancer_id, create_backend_details, backend_set_name, **kwargs):
        """
        Adds a backend server to a backend set.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.CreateBackendDetails create_backend_details: (required)
            The details to add a backend server to a backend set.

        :param str backend_set_name: (required)
            The name of the backend set to which to add the backend server.

            Example: `example_backend_set`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that it can be retried in case of a timeout or
            server error without risk of rerunning that same action. Retry tokens expire after 24
            hours but they can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the current etag value of the resource.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/create_backend.py.html>`__ to see an example of how to use create_backend API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/backendSets/{backendSetName}/backends"
        method = "POST"
        operation_name = "create_backend"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/Backend/CreateBackend"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_backend got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id,
            "backendSetName": backend_set_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_backend_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_backend_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_backend_set(self, network_load_balancer_id, create_backend_set_details, **kwargs):
        """
        Adds a backend set to a network load balancer.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.CreateBackendSetDetails create_backend_set_details: (required)
            The details for adding a backend set.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that it can be retried in case of a timeout or
            server error without risk of rerunning that same action. Retry tokens expire after 24
            hours but they can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the current etag value of the resource.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/create_backend_set.py.html>`__ to see an example of how to use create_backend_set API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/backendSets"
        method = "POST"
        operation_name = "create_backend_set"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/BackendSet/CreateBackendSet"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_backend_set got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_backend_set_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_backend_set_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_listener(self, network_load_balancer_id, create_listener_details, **kwargs):
        """
        Adds a listener to a network load balancer.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.CreateListenerDetails create_listener_details: (required)
            Details to add a listener.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that it can be retried in case of a timeout or
            server error without risk of rerunning that same action. Retry tokens expire after 24
            hours but they can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the current etag value of the resource.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/create_listener.py.html>`__ to see an example of how to use create_listener API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/listeners"
        method = "POST"
        operation_name = "create_listener"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/Listener/CreateListener"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_listener got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_listener_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_listener_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_network_load_balancer(self, create_network_load_balancer_details, **kwargs):
        """
        Creates a network load balancer.


        :param oci.network_load_balancer.models.CreateNetworkLoadBalancerDetails create_network_load_balancer_details: (required)
            Details for the new network load balancer.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that it can be retried in case of a timeout or
            server error without risk of rerunning that same action. Retry tokens expire after 24
            hours but they can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.NetworkLoadBalancer`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/create_network_load_balancer.py.html>`__ to see an example of how to use create_network_load_balancer API.
        """
        resource_path = "/networkLoadBalancers"
        method = "POST"
        operation_name = "create_network_load_balancer"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/NetworkLoadBalancer/CreateNetworkLoadBalancer"

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
                "create_network_load_balancer got unknown kwargs: {!r}".format(extra_kwargs))

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

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_network_load_balancer_details,
                response_type="NetworkLoadBalancer",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_network_load_balancer_details,
                response_type="NetworkLoadBalancer",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def delete_backend(self, network_load_balancer_id, backend_set_name, backend_name, **kwargs):
        """
        Removes a backend server from a given network load balancer and backend set.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set associated with the backend server.

            Example: `example_backend_set`

        :param str backend_name: (required)
            The name of the backend server to remove.
            If the backend was created with an explicitly specified name, that name should be used here.
            If the backend was created without explicitly specifying the name, but was created using ipAddress, this is specified as <ipAddress>:<port>.
            If the backend was created without explicitly specifying the name, but was created using targetId, this is specified as <targetId>:<port>.

            Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:8080`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the current etag value of the resource.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/delete_backend.py.html>`__ to see an example of how to use delete_backend API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/backendSets/{backendSetName}/backends/{backendName}"
        method = "DELETE"
        operation_name = "delete_backend"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/Backend/DeleteBackend"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_backend got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id,
            "backendSetName": backend_set_name,
            "backendName": backend_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
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

    def delete_backend_set(self, network_load_balancer_id, backend_set_name, **kwargs):
        """
        Deletes the specified backend set. Note that deleting a backend set removes its backend servers from the network load balancer.

        Before you can delete a backend set, you must remove it from any active listeners.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set to delete.

            Example: `example_backend_set`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the current etag value of the resource.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/delete_backend_set.py.html>`__ to see an example of how to use delete_backend_set API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/backendSets/{backendSetName}"
        method = "DELETE"
        operation_name = "delete_backend_set"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/BackendSet/DeleteBackendSet"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_backend_set got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id,
            "backendSetName": backend_set_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
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

    def delete_listener(self, network_load_balancer_id, listener_name, **kwargs):
        """
        Deletes a listener from a network load balancer.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str listener_name: (required)
            The name of the listener to delete.

            Example: `example_listener`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the current etag value of the resource.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/delete_listener.py.html>`__ to see an example of how to use delete_listener API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/listeners/{listenerName}"
        method = "DELETE"
        operation_name = "delete_listener"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/Listener/DeleteListener"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_listener got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id,
            "listenerName": listener_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
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

    def delete_network_load_balancer(self, network_load_balancer_id, **kwargs):
        """
        Deletes a network load balancer resource by identifier.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the current etag value of the resource.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/delete_network_load_balancer.py.html>`__ to see an example of how to use delete_network_load_balancer API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}"
        method = "DELETE"
        operation_name = "delete_network_load_balancer"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/NetworkLoadBalancer/DeleteNetworkLoadBalancer"

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
                "delete_network_load_balancer got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

    def get_backend(self, network_load_balancer_id, backend_set_name, backend_name, **kwargs):
        """
        Retrieves the configuration information for the specified backend server.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set that includes the backend server.

            Example: `example_backend_set`

        :param str backend_name: (required)
            The name of the backend server to retrieve.
            If the backend was created with an explicitly specified name, that name should be used here.
            If the backend was created without explicitly specifying the name, but was created using ipAddress, this is specified as <ipAddress>:<port>.
            If the backend was created without explicitly specifying the name, but was created using targetId, this is specified as <targetId>:<port>.

            Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:8080`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str if_none_match: (optional)
            The system returns the requested resource, with a 200 status, only if the resource has no etag
            matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the
            HTTP status code `304 (Not Modified)`.

            Example: `example-etag`

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.Backend`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/get_backend.py.html>`__ to see an example of how to use get_backend API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/backendSets/{backendSetName}/backends/{backendName}"
        method = "GET"
        operation_name = "get_backend"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/Backend/GetBackend"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "if_none_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_backend got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id,
            "backendSetName": backend_set_name,
            "backendName": backend_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-none-match": kwargs.get("if_none_match", missing)
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
                response_type="Backend",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Backend",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_backend_health(self, network_load_balancer_id, backend_set_name, backend_name, **kwargs):
        """
        Retrieves the current health status of the specified backend server.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set associated with the backend server for which to retrieve the health status.

            Example: `example_backend_set`

        :param str backend_name: (required)
            The name of the backend server to retrieve health status for.
            If the backend was created with an explicitly specified name, that name should be used here.
            If the backend was created without explicitly specifying the name, but was created using ipAddress, this is specified as <ipAddress>:<port>.
            If the backend was created without explicitly specifying the name, but was created using targetId, this is specified as <targetId>:<port>.

            Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:8080`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.BackendHealth`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/get_backend_health.py.html>`__ to see an example of how to use get_backend_health API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/backendSets/{backendSetName}/backends/{backendName}/health"
        method = "GET"
        operation_name = "get_backend_health"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/BackendHealth/GetBackendHealth"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_backend_health got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id,
            "backendSetName": backend_set_name,
            "backendName": backend_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
                response_type="BackendHealth",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="BackendHealth",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_backend_set(self, network_load_balancer_id, backend_set_name, **kwargs):
        """
        Retrieves the configuration information for the specified backend set.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set to retrieve.

            Example: `example_backend_set`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str if_none_match: (optional)
            The system returns the requested resource, with a 200 status, only if the resource has no etag
            matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the
            HTTP status code `304 (Not Modified)`.

            Example: `example-etag`

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.BackendSet`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/get_backend_set.py.html>`__ to see an example of how to use get_backend_set API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/backendSets/{backendSetName}"
        method = "GET"
        operation_name = "get_backend_set"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/BackendSet/GetBackendSet"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "if_none_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_backend_set got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id,
            "backendSetName": backend_set_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-none-match": kwargs.get("if_none_match", missing)
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
                response_type="BackendSet",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="BackendSet",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_backend_set_health(self, network_load_balancer_id, backend_set_name, **kwargs):
        """
        Retrieves the health status for the specified backend set.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set for which to retrieve the health status.

            Example: `example_backend_set`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.BackendSetHealth`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/get_backend_set_health.py.html>`__ to see an example of how to use get_backend_set_health API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/backendSets/{backendSetName}/health"
        method = "GET"
        operation_name = "get_backend_set_health"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/BackendSetHealth/GetBackendSetHealth"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_backend_set_health got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id,
            "backendSetName": backend_set_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
                response_type="BackendSetHealth",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="BackendSetHealth",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_health_checker(self, network_load_balancer_id, backend_set_name, **kwargs):
        """
        Retrieves the health check policy information for a given network load balancer and backend set.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set associated with the health check policy to be retrieved.

            Example: `example_backend_set`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that it can be retried in case of a timeout or
            server error without risk of rerunning that same action. Retry tokens expire after 24
            hours but they can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str if_none_match: (optional)
            The system returns the requested resource, with a 200 status, only if the resource has no etag
            matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the
            HTTP status code `304 (Not Modified)`.

            Example: `example-etag`

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.HealthChecker`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/get_health_checker.py.html>`__ to see an example of how to use get_health_checker API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/backendSets/{backendSetName}/healthChecker"
        method = "GET"
        operation_name = "get_health_checker"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/HealthChecker/GetHealthChecker"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_none_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_health_checker got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id,
            "backendSetName": backend_set_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-none-match": kwargs.get("if_none_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="HealthChecker",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="HealthChecker",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_listener(self, network_load_balancer_id, listener_name, **kwargs):
        """
        Retrieves listener properties associated with a given network load balancer and listener name.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str listener_name: (required)
            The name of the listener to get.

            Example: `example_listener`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str if_none_match: (optional)
            The system returns the requested resource, with a 200 status, only if the resource has no etag
            matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the
            HTTP status code `304 (Not Modified)`.

            Example: `example-etag`

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.Listener`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/get_listener.py.html>`__ to see an example of how to use get_listener API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/listeners/{listenerName}"
        method = "GET"
        operation_name = "get_listener"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/Listener/GetListener"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "if_none_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_listener got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id,
            "listenerName": listener_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-none-match": kwargs.get("if_none_match", missing)
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
                response_type="Listener",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Listener",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_network_load_balancer(self, network_load_balancer_id, **kwargs):
        """
        Retrieves network load balancer configuration information by identifier.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_none_match: (optional)
            The system returns the requested resource, with a 200 status, only if the resource has no etag
            matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the
            HTTP status code `304 (Not Modified)`.

            Example: `example-etag`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.NetworkLoadBalancer`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/get_network_load_balancer.py.html>`__ to see an example of how to use get_network_load_balancer API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}"
        method = "GET"
        operation_name = "get_network_load_balancer"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/NetworkLoadBalancer/GetNetworkLoadBalancer"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_none_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_network_load_balancer got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-none-match": kwargs.get("if_none_match", missing),
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
                response_type="NetworkLoadBalancer",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="NetworkLoadBalancer",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_network_load_balancer_health(self, network_load_balancer_id, **kwargs):
        """
        Retrieves the health status for the specified network load balancer.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.NetworkLoadBalancerHealth`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/get_network_load_balancer_health.py.html>`__ to see an example of how to use get_network_load_balancer_health API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/health"
        method = "GET"
        operation_name = "get_network_load_balancer_health"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/NetworkLoadBalancerHealth/GetNetworkLoadBalancerHealth"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_network_load_balancer_health got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
                response_type="NetworkLoadBalancerHealth",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="NetworkLoadBalancerHealth",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_work_request(self, work_request_id, **kwargs):
        """
        Retrieves the details of the work request with the given identifier.


        :param str work_request_id: (required)
            The identifier of the asynchronous request.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.WorkRequest`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/get_work_request.py.html>`__ to see an example of how to use get_work_request API.
        """
        resource_path = "/workRequests/{workRequestId}"
        method = "GET"
        operation_name = "get_work_request"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/WorkRequest/GetWorkRequest"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
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

    def list_backend_sets(self, network_load_balancer_id, **kwargs):
        """
        Lists all backend sets associated with a given network load balancer.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str if_none_match: (optional)
            The system returns the requested resource, with a 200 status, only if the resource has no etag
            matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the
            HTTP status code `304 (Not Modified)`.

            Example: `example-etag`

        :param int limit: (optional)
            For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            The page token representing the page from which to start retrieving results.
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either 'asc' (ascending) or 'desc' (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending.
            The default order for displayName is ascending. If no value is specified, then timeCreated is the default.

            Allowed values are: "timeCreated", "displayName"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.BackendSetCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/list_backend_sets.py.html>`__ to see an example of how to use list_backend_sets API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/backendSets"
        method = "GET"
        operation_name = "list_backend_sets"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/BackendSetSummary/ListBackendSets"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "if_none_match",
            "limit",
            "page",
            "sort_order",
            "sort_by"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_backend_sets got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "displayName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-none-match": kwargs.get("if_none_match", missing)
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
                query_params=query_params,
                header_params=header_params,
                response_type="BackendSetCollection",
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
                response_type="BackendSetCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_backends(self, network_load_balancer_id, backend_set_name, **kwargs):
        """
        Lists the backend servers for a given network load balancer and backend set.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str backend_set_name: (required)
            The name of the backend set associated with the backend servers.

            Example: `example_backend_set`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str if_none_match: (optional)
            The system returns the requested resource, with a 200 status, only if the resource has no etag
            matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the
            HTTP status code `304 (Not Modified)`.

            Example: `example-etag`

        :param int limit: (optional)
            For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            The page token representing the page from which to start retrieving results.
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either 'asc' (ascending) or 'desc' (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending.
            The default order for displayName is ascending. If no value is specified, then timeCreated is the default.

            Allowed values are: "timeCreated", "displayName"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.BackendCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/list_backends.py.html>`__ to see an example of how to use list_backends API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/backendSets/{backendSetName}/backends"
        method = "GET"
        operation_name = "list_backends"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/BackendSummary/ListBackends"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "if_none_match",
            "limit",
            "page",
            "sort_order",
            "sort_by"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_backends got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id,
            "backendSetName": backend_set_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "displayName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-none-match": kwargs.get("if_none_match", missing)
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
                query_params=query_params,
                header_params=header_params,
                response_type="BackendCollection",
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
                response_type="BackendCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_listeners(self, network_load_balancer_id, **kwargs):
        """
        Lists all listeners associated with a given network load balancer.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str if_none_match: (optional)
            The system returns the requested resource, with a 200 status, only if the resource has no etag
            matching the one specified. If the condition fails for the GET and HEAD methods, then the system returns the
            HTTP status code `304 (Not Modified)`.

            Example: `example-etag`

        :param int limit: (optional)
            For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            The page token representing the page from which to start retrieving results.
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either 'asc' (ascending) or 'desc' (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending.
            The default order for displayName is ascending. If no value is specified, then timeCreated is the default.

            Allowed values are: "timeCreated", "displayName"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.ListenerCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/list_listeners.py.html>`__ to see an example of how to use list_listeners API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/listeners"
        method = "GET"
        operation_name = "list_listeners"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/ListenerSummary/ListListeners"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "if_none_match",
            "limit",
            "page",
            "sort_order",
            "sort_by"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_listeners got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "displayName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-none-match": kwargs.get("if_none_match", missing)
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
                query_params=query_params,
                header_params=header_params,
                response_type="ListenerCollection",
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
                response_type="ListenerCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_network_load_balancer_healths(self, compartment_id, **kwargs):
        """
        Lists the summary health statuses for all network load balancers in the specified compartment.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment containing the network load balancers to list.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str sort_order: (optional)
            The sort order to use, either 'asc' (ascending) or 'desc' (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending.
            The default order for displayName is ascending. If no value is specified, then timeCreated is the default.

            Allowed values are: "timeCreated", "displayName"

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            The page token representing the page from which to start retrieving results.
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.NetworkLoadBalancerHealthCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/list_network_load_balancer_healths.py.html>`__ to see an example of how to use list_network_load_balancer_healths API.
        """
        resource_path = "/networkLoadBalancers/health"
        method = "GET"
        operation_name = "list_network_load_balancer_healths"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/NetworkLoadBalancerHealth/ListNetworkLoadBalancerHealths"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "sort_order",
            "sort_by",
            "opc_request_id",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_network_load_balancer_healths got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "displayName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
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
                response_type="NetworkLoadBalancerHealthCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="NetworkLoadBalancerHealthCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_network_load_balancers(self, compartment_id, **kwargs):
        """
        Returns a list of network load balancers.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment containing the network load balancers to list.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the given lifecycle state.

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"

        :param str display_name: (optional)
            A filter to return only resources that match the entire display name given.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            The page token representing the page from which to start retrieving results.
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either 'asc' (ascending) or 'desc' (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending.
            The default order for displayName is ascending. If no value is specified, then timeCreated is the default.

            Allowed values are: "timeCreated", "displayName"

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.NetworkLoadBalancerCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/list_network_load_balancers.py.html>`__ to see an example of how to use list_network_load_balancers API.
        """
        resource_path = "/networkLoadBalancers"
        method = "GET"
        operation_name = "list_network_load_balancers"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/NetworkLoadBalancer/ListNetworkLoadBalancers"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "lifecycle_state",
            "display_name",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_network_load_balancers got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "displayName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "displayName": kwargs.get("display_name", missing),
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
                response_type="NetworkLoadBalancerCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="NetworkLoadBalancerCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_network_load_balancers_policies(self, **kwargs):
        """
        Lists the available network load balancer policies.


        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            The page token representing the page from which to start retrieving results.
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either 'asc' (ascending) or 'desc' (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending.
            The default order for displayName is ascending. If no value is specified, then timeCreated is the default.

            Allowed values are: "timeCreated", "displayName"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.NetworkLoadBalancersPolicyCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/list_network_load_balancers_policies.py.html>`__ to see an example of how to use list_network_load_balancers_policies API.
        """
        resource_path = "/networkLoadBalancersPolicies"
        method = "GET"
        operation_name = "list_network_load_balancers_policies"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/NetworkLoadBalancingPolicy/ListNetworkLoadBalancersPolicies"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "sort_order",
            "sort_by"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_network_load_balancers_policies got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "displayName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
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
                response_type="NetworkLoadBalancersPolicyCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="NetworkLoadBalancersPolicyCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_network_load_balancers_protocols(self, **kwargs):
        """
        This API has been deprecated so it won't return the updated list of supported protocls.
        Lists all supported traffic protocols.


        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            The page token representing the page from which to start retrieving results.
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either 'asc' (ascending) or 'desc' (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Only one sort order can be provided. The default order for timeCreated is descending.
            The default order for displayName is ascending. If no value is specified, then timeCreated is the default.

            Allowed values are: "timeCreated", "displayName"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.NetworkLoadBalancersProtocolCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/list_network_load_balancers_protocols.py.html>`__ to see an example of how to use list_network_load_balancers_protocols API.
        """
        resource_path = "/networkLoadBalancersProtocols"
        method = "GET"
        operation_name = "list_network_load_balancers_protocols"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/ListenerProtocols/ListNetworkLoadBalancersProtocols"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "sort_order",
            "sort_by"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_network_load_balancers_protocols got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "displayName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
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
                response_type="NetworkLoadBalancersProtocolCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="NetworkLoadBalancersProtocolCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_work_request_errors(self, work_request_id, compartment_id, **kwargs):
        """
        Return a (paginated) list of errors for a given work request.


        :param str work_request_id: (required)
            The identifier of the asynchronous request.

        :param str compartment_id: (required)
            The `OCID`__ of the compartment containing the network load balancers to list.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str page: (optional)
            The page token representing the page from which to start retrieving results.
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.WorkRequestErrorCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/list_work_request_errors.py.html>`__ to see an example of how to use list_work_request_errors API.
        """
        resource_path = "/workRequests/{workRequestId}/errors"
        method = "GET"
        operation_name = "list_work_request_errors"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/WorkRequestError/ListWorkRequestErrors"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "page",
            "limit"
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
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
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
                response_type="WorkRequestErrorCollection",
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
                response_type="WorkRequestErrorCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_work_request_logs(self, work_request_id, compartment_id, **kwargs):
        """
        Returns a (paginated) list of logs for a given work request.


        :param str work_request_id: (required)
            The identifier of the asynchronous request.

        :param str compartment_id: (required)
            The `OCID`__ of the compartment containing the network load balancers to list.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str page: (optional)
            The page token representing the page from which to start retrieving results.
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.WorkRequestLogEntryCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/list_work_request_logs.py.html>`__ to see an example of how to use list_work_request_logs API.
        """
        resource_path = "/workRequests/{workRequestId}/logs"
        method = "GET"
        operation_name = "list_work_request_logs"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/WorkRequestLogEntry/ListWorkRequestLogs"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "page",
            "limit"
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
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
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
                response_type="WorkRequestLogEntryCollection",
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
                response_type="WorkRequestLogEntryCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_work_requests(self, compartment_id, **kwargs):
        """
        Lists all work requests.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment containing the network load balancers to list.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page or items to return, in a paginated \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            The page token representing the page from which to start retrieving results.
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.network_load_balancer.models.WorkRequestCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/list_work_requests.py.html>`__ to see an example of how to use list_work_requests API.
        """
        resource_path = "/workRequests"
        method = "GET"
        operation_name = "list_work_requests"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/WorkRequest/ListWorkRequests"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_work_requests got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
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
                response_type="WorkRequestCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="WorkRequestCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_backend(self, network_load_balancer_id, update_backend_details, backend_set_name, backend_name, **kwargs):
        """
        Updates the configuration of a backend server within the specified backend set.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.UpdateBackendDetails update_backend_details: (required)
            Details for updating a backend server.

        :param str backend_set_name: (required)
            The name of the backend set associated with the backend server.

            Example: `example_backend_set`

        :param str backend_name: (required)
            The name of the backend server to update.
            If the backend was created with an explicitly specified name, that name should be used here.
            If the backend was created without explicitly specifying the name, but was created using ipAddress, this is specified as <ipAddress>:<port>.
            If the backend was created without explicitly specifying the name, but was created using targetId, this is specified as <targetId>:<port>.

            Example: `10.0.0.3:8080` or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:8080`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that it can be retried in case of a timeout or
            server error without risk of rerunning that same action. Retry tokens expire after 24
            hours but they can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the current etag value of the resource.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/update_backend.py.html>`__ to see an example of how to use update_backend API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/backendSets/{backendSetName}/backends/{backendName}"
        method = "PUT"
        operation_name = "update_backend"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/Backend/UpdateBackend"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_backend got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id,
            "backendSetName": backend_set_name,
            "backendName": backend_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_backend_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_backend_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_backend_set(self, network_load_balancer_id, update_backend_set_details, backend_set_name, **kwargs):
        """
        Updates a backend set.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.UpdateBackendSetDetails update_backend_set_details: (required)
            The details to update a backend set.

        :param str backend_set_name: (required)
            The name of the backend set to update.

            Example: `example_backend_set`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that it can be retried in case of a timeout or
            server error without risk of rerunning that same action. Retry tokens expire after 24
            hours but they can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the current etag value of the resource.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/update_backend_set.py.html>`__ to see an example of how to use update_backend_set API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/backendSets/{backendSetName}"
        method = "PUT"
        operation_name = "update_backend_set"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/BackendSet/UpdateBackendSet"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_backend_set got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id,
            "backendSetName": backend_set_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_backend_set_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_backend_set_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_health_checker(self, network_load_balancer_id, update_health_checker_details, backend_set_name, **kwargs):
        """
        Updates the health check policy for a given network load balancer and backend set.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.UpdateHealthCheckerDetails update_health_checker_details: (required)
            The health check policy configuration details.

        :param str backend_set_name: (required)
            The name of the backend set associated with the health check policy to be retrieved.

            Example: `example_backend_set`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that it can be retried in case of a timeout or
            server error without risk of rerunning that same action. Retry tokens expire after 24
            hours but they can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the current etag value of the resource.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/update_health_checker.py.html>`__ to see an example of how to use update_health_checker API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/backendSets/{backendSetName}/healthChecker"
        method = "PUT"
        operation_name = "update_health_checker"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/HealthChecker/UpdateHealthChecker"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_health_checker got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id,
            "backendSetName": backend_set_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_health_checker_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_health_checker_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_listener(self, network_load_balancer_id, update_listener_details, listener_name, **kwargs):
        """
        Updates a listener for a given network load balancer.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.UpdateListenerDetails update_listener_details: (required)
            Details to update a listener.

        :param str listener_name: (required)
            The name of the listener to update.

            Example: `example_listener`

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that it can be retried in case of a timeout or
            server error without risk of rerunning that same action. Retry tokens expire after 24
            hours but they can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the current etag value of the resource.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/update_listener.py.html>`__ to see an example of how to use update_listener API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/listeners/{listenerName}"
        method = "PUT"
        operation_name = "update_listener"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/Listener/UpdateListener"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_listener got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id,
            "listenerName": listener_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_listener_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_listener_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_network_load_balancer(self, network_load_balancer_id, update_network_load_balancer_details, **kwargs):
        """
        Updates the network load balancer


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.UpdateNetworkLoadBalancerDetails update_network_load_balancer_details: (required)
            The information to be updated.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the current etag value of the resource.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/update_network_load_balancer.py.html>`__ to see an example of how to use update_network_load_balancer API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}"
        method = "PUT"
        operation_name = "update_network_load_balancer"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/NetworkLoadBalancer/UpdateNetworkLoadBalancer"

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
                "update_network_load_balancer got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
                body=update_network_load_balancer_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_network_load_balancer_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_network_security_groups(self, network_load_balancer_id, update_network_security_groups_details, **kwargs):
        """
        Updates the network security groups associated with the specified network load balancer.


        :param str network_load_balancer_id: (required)
            The `OCID`__ of the network load balancer to update.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.network_load_balancer.models.UpdateNetworkSecurityGroupsDetails update_network_security_groups_details: (required)
            The details for updating the network security groups associated with the specified network load balancer.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you must contact Oracle about a
            particular request, then provide the request identifier.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so that it can be retried in case of a timeout or
            server error without risk of rerunning that same action. Retry tokens expire after 24
            hours but they can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the etag you
            provide matches the current etag value of the resource.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/networkloadbalancer/update_network_security_groups.py.html>`__ to see an example of how to use update_network_security_groups API.
        """
        resource_path = "/networkLoadBalancers/{networkLoadBalancerId}/networkSecurityGroups"
        method = "PUT"
        operation_name = "update_network_security_groups"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/NetworkLoadBalancer/UpdateNetworkSecurityGroups"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_network_security_groups got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "networkLoadBalancerId": network_load_balancer_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_network_security_groups_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_network_security_groups_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
