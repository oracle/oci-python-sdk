# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry, circuit_breaker  # noqa: F401
from oci.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel, get_signer_from_authentication_type, AUTHENTICATION_TYPE_FIELD_NAME
from .models import jms_type_mapping
missing = Sentinel("Missing")


class JavaManagementServiceClient(object):
    """
    API for the Java Management Service. Use this API to view, create, and manage Fleets.
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
            This client will not have circuit breakers enabled by default, users can use their own circuit breaker strategy or the convenient :py:data:`~oci.circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY` provided by the SDK to enable it.
            The specifics of circuit breaker strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/circuit_breakers.html>`__.

        :param function circuit_breaker_callback: (optional)
            Callback function to receive any exceptions triggerred by the circuit breaker.
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
            'base_path': '/20210610',
            'service_endpoint_template': 'https://javamanagement.{region}.oci.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'circuit_breaker_strategy': kwargs.get('circuit_breaker_strategy', circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY)
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        self.base_client = BaseClient("java_management_service", config, signer, jms_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

    def change_fleet_compartment(self, fleet_id, change_fleet_compartment_details, **kwargs):
        """
        Move a specified Fleet into the compartment identified in the POST form. When provided, If-Match is checked against ETag values of the resource.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.jms.models.ChangeFleetCompartmentDetails change_fleet_compartment_details: (required)
            Compartment identifier.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            ETag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the ETag you
            provide matches the resource's current ETag value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/change_fleet_compartment.py.html>`__ to see an example of how to use change_fleet_compartment API.
        """
        resource_path = "/fleets/{fleetId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_fleet_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
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
                path_params=path_params,
                header_params=header_params,
                body=change_fleet_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_fleet_compartment_details)

    def create_fleet(self, create_fleet_details, **kwargs):
        """
        Create a new Fleet using the information provided.


        :param oci.jms.models.CreateFleetDetails create_fleet_details: (required)
            Details for the new Fleet.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/create_fleet.py.html>`__ to see an example of how to use create_fleet API.
        """
        resource_path = "/fleets"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_fleet got unknown kwargs: {!r}".format(extra_kwargs))

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
                body=create_fleet_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_fleet_details)

    def delete_fleet(self, fleet_id, **kwargs):
        """
        Deletes the Fleet specified by an identifier.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            ETag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the ETag you
            provide matches the resource's current ETag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/delete_fleet.py.html>`__ to see an example of how to use delete_fleet API.
        """
        resource_path = "/fleets/{fleetId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_fleet got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
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
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def get_fleet(self, fleet_id, **kwargs):
        """
        Retrieve a Fleet with the specified identifier.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.Fleet`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/get_fleet.py.html>`__ to see an example of how to use get_fleet API.
        """
        resource_path = "/fleets/{fleetId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_fleet got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
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
                response_type="Fleet")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Fleet")

    def get_fleet_agent_configuration(self, fleet_id, **kwargs):
        """
        Retrieve a Fleet Agent Configuration for the specified Fleet.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.FleetAgentConfiguration`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/get_fleet_agent_configuration.py.html>`__ to see an example of how to use get_fleet_agent_configuration API.
        """
        resource_path = "/fleets/{fleetId}/agentConfiguration"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_fleet_agent_configuration got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
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
                response_type="FleetAgentConfiguration")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="FleetAgentConfiguration")

    def get_work_request(self, work_request_id, **kwargs):
        """
        Retrieve the details of a work request with the specified ID.


        :param str work_request_id: (required)
            The `OCID`__ of the asynchronous work request.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.WorkRequest`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/get_work_request.py.html>`__ to see an example of how to use get_work_request API.
        """
        resource_path = "/workRequests/{workRequestId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
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
                response_type="WorkRequest")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="WorkRequest")

    def list_fleets(self, **kwargs):
        """
        Returns a list of all the Fleets contained by a compartment.


        :param str compartment_id: (optional)
            The `OCID`__ of the compartment in which to list resources.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            The ID of the Fleet.

        :param str lifecycle_state: (optional)
            The state of the lifecycle.

            Allowed values are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"

        :param str display_name: (optional)
            The display name.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

        :param str sort_order: (optional)
            The sort order, either 'asc' or 'desc'.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort Fleets. Only one sort order may be provided.
            Default order for _timeCreated_, _approximateJreCount_, _approximateInstallationCount_,
            _approximateApplicationCount_ and _approximateManagedInstanceCount_  is **descending**.
            Default order for _displayName_ is **ascending**.
            If no value is specified _timeCreated_ is default.

            Allowed values are: "displayName", "timeCreated"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.FleetCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/list_fleets.py.html>`__ to see an example of how to use list_fleets API.
        """
        resource_path = "/fleets"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "compartment_id",
            "id",
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
                "list_fleets got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]
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
            sort_by_allowed_values = ["displayName", "timeCreated"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "id": kwargs.get("id", missing),
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
                response_type="FleetCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="FleetCollection")

    def list_work_request_errors(self, work_request_id, **kwargs):
        """
        Retrieve a (paginated) list of errors for a specified work request.


        :param str work_request_id: (required)
            The `OCID`__ of the asynchronous work request.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str page: (optional)
            The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of items to return.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.WorkRequestErrorCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/list_work_request_errors.py.html>`__ to see an example of how to use list_work_request_errors API.
        """
        resource_path = "/workRequests/{workRequestId}/errors"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
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
                response_type="WorkRequestErrorCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="WorkRequestErrorCollection")

    def list_work_request_logs(self, work_request_id, **kwargs):
        """
        Retrieve a (paginated) list of logs for a specified work request.


        :param str work_request_id: (required)
            The `OCID`__ of the asynchronous work request.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str page: (optional)
            The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of items to return.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.WorkRequestLogEntryCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/list_work_request_logs.py.html>`__ to see an example of how to use list_work_request_logs API.
        """
        resource_path = "/workRequests/{workRequestId}/logs"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
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
                response_type="WorkRequestLogEntryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="WorkRequestLogEntryCollection")

    def list_work_requests(self, **kwargs):
        """
        List the work requests in a compartment.


        :param str compartment_id: (optional)
            The `OCID`__ of the compartment in which to list resources.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            The ID of an asynchronous work request.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str page: (optional)
            The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of items to return.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.WorkRequestCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/list_work_requests.py.html>`__ to see an example of how to use list_work_requests API.
        """
        resource_path = "/workRequests"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "compartment_id",
            "id",
            "opc_request_id",
            "page",
            "limit"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_work_requests got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "id": kwargs.get("id", missing),
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
                query_params=query_params,
                header_params=header_params,
                response_type="WorkRequestCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="WorkRequestCollection")

    def summarize_application_usage(self, fleet_id, **kwargs):
        """
        List application usage in a Fleet filtered by query parameters.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str application_id: (optional)
            The Fleet-unique identifier of the application.

        :param str display_name: (optional)
            The display name.

        :param str application_type: (optional)
            The type of the application.

        :param str jre_vendor: (optional)
            The vendor of the related Java Runtime.

        :param str jre_distribution: (optional)
            The distribution of the related Java Runtime.

        :param str jre_version: (optional)
            The version of the related Java Runtime.

        :param str installation_path: (optional)
            The file system path of the installation.

        :param str managed_instance_id: (optional)
            The Fleet-unique identifier of the related managed instance.

        :param list[str] fields: (optional)
            Additional fields to include into the returned model on top of the required ones.
            This parameter can also include 'approximateJreCount', 'approximateInstallationCount' and 'approximateManagedInstanceCount'.
            For example 'approximateJreCount,approximateInstallationCount'.

            Allowed values are: "approximateJreCount", "approximateInstallationCount", "approximateManagedInstanceCount"

        :param datetime time_start: (optional)
            The start of the time period during which resources are searched (formatted according to `RFC3339`__).

            __ https://datatracker.ietf.org/doc/html/rfc3339

        :param datetime time_end: (optional)
            The end of the time period during which resources are searched (formatted according to `RFC3339`__).

            __ https://datatracker.ietf.org/doc/html/rfc3339

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

        :param str sort_order: (optional)
            The sort order, either 'asc' or 'desc'.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort application views. Only one sort order may be provided.
            Default order for _timeFirstSeen_, _timeLastSeen_, _approximateJreCount_, _approximateInstallationCount_
            and _approximateManagedInstanceCount_  is **descending**.
            Default order for _displayName_ and _osName_ is **ascending**.
            If no value is specified _timeLastSeen_ is default.

            Allowed values are: "timeFirstSeen", "timeLastSeen", "displayName", "approximateJreCount", "approximateInstallationCount", "approximateManagedInstanceCount", "osName"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param list[str] os_family: (optional)
            The operating system type.

            Allowed values are: "LINUX", "WINDOWS", "MACOS", "UNKNOWN"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.ApplicationUsageCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/summarize_application_usage.py.html>`__ to see an example of how to use summarize_application_usage API.
        """
        resource_path = "/fleets/{fleetId}/actions/summarizeApplicationUsage"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "application_id",
            "display_name",
            "application_type",
            "jre_vendor",
            "jre_distribution",
            "jre_version",
            "installation_path",
            "managed_instance_id",
            "fields",
            "time_start",
            "time_end",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id",
            "os_family"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_application_usage got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'fields' in kwargs:
            fields_allowed_values = ["approximateJreCount", "approximateInstallationCount", "approximateManagedInstanceCount"]
            for fields_item in kwargs['fields']:
                if fields_item not in fields_allowed_values:
                    raise ValueError(
                        "Invalid value for `fields`, must be one of {0}".format(fields_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeFirstSeen", "timeLastSeen", "displayName", "approximateJreCount", "approximateInstallationCount", "approximateManagedInstanceCount", "osName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'os_family' in kwargs:
            os_family_allowed_values = ["LINUX", "WINDOWS", "MACOS", "UNKNOWN"]
            for os_family_item in kwargs['os_family']:
                if os_family_item not in os_family_allowed_values:
                    raise ValueError(
                        "Invalid value for `os_family`, must be one of {0}".format(os_family_allowed_values)
                    )

        query_params = {
            "applicationId": kwargs.get("application_id", missing),
            "displayName": kwargs.get("display_name", missing),
            "applicationType": kwargs.get("application_type", missing),
            "jreVendor": kwargs.get("jre_vendor", missing),
            "jreDistribution": kwargs.get("jre_distribution", missing),
            "jreVersion": kwargs.get("jre_version", missing),
            "installationPath": kwargs.get("installation_path", missing),
            "managedInstanceId": kwargs.get("managed_instance_id", missing),
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
            "timeStart": kwargs.get("time_start", missing),
            "timeEnd": kwargs.get("time_end", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "osFamily": self.base_client.generate_collection_format_param(kwargs.get("os_family", missing), 'multi')
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
                response_type="ApplicationUsageCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ApplicationUsageCollection")

    def summarize_installation_usage(self, fleet_id, **kwargs):
        """
        List Java installation usage in a Fleet filtered by query parameters.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str jre_vendor: (optional)
            The vendor of the related Java Runtime.

        :param str jre_distribution: (optional)
            The distribution of the related Java Runtime.

        :param str jre_version: (optional)
            The version of the related Java Runtime.

        :param str installation_path: (optional)
            The file system path of the installation.

        :param str application_id: (optional)
            The Fleet-unique identifier of the related application.

        :param str managed_instance_id: (optional)
            The Fleet-unique identifier of the related managed instance.

        :param list[str] fields: (optional)
            Additional fields to include into the returned model on top of the required ones.
            This parameter can also include 'approximateApplicationCount' and 'approximateManagedInstanceCount'.
            For example 'approximateApplicationCount,approximateManagedInstanceCount'.

            Allowed values are: "approximateApplicationCount", "approximateManagedInstanceCount"

        :param datetime time_start: (optional)
            The start of the time period during which resources are searched (formatted according to `RFC3339`__).

            __ https://datatracker.ietf.org/doc/html/rfc3339

        :param datetime time_end: (optional)
            The end of the time period during which resources are searched (formatted according to `RFC3339`__).

            __ https://datatracker.ietf.org/doc/html/rfc3339

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

        :param str sort_order: (optional)
            The sort order, either 'asc' or 'desc'.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort installation views. Only one sort order may be provided.
            Default order for _timeFirstSeen_, _timeLastSeen_, and _jreVersion_, _approximateApplicationCount_
            and _approximateManagedInstanceCount_  is **descending**.
            Default order for _jreDistribution_ and _jreVendor_ is **ascending**. If no value is specified _timeLastSeen_ is default.

            Allowed values are: "jreDistribution", "jreVendor", "jreVersion", "path", "timeFirstSeen", "timeLastSeen", "approximateApplicationCount", "approximateManagedInstanceCount", "osName"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param list[str] os_family: (optional)
            The operating system type.

            Allowed values are: "LINUX", "WINDOWS", "MACOS", "UNKNOWN"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.InstallationUsageCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/summarize_installation_usage.py.html>`__ to see an example of how to use summarize_installation_usage API.
        """
        resource_path = "/fleets/{fleetId}/actions/summarizeInstallationUsage"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "jre_vendor",
            "jre_distribution",
            "jre_version",
            "installation_path",
            "application_id",
            "managed_instance_id",
            "fields",
            "time_start",
            "time_end",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id",
            "os_family"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_installation_usage got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'fields' in kwargs:
            fields_allowed_values = ["approximateApplicationCount", "approximateManagedInstanceCount"]
            for fields_item in kwargs['fields']:
                if fields_item not in fields_allowed_values:
                    raise ValueError(
                        "Invalid value for `fields`, must be one of {0}".format(fields_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["jreDistribution", "jreVendor", "jreVersion", "path", "timeFirstSeen", "timeLastSeen", "approximateApplicationCount", "approximateManagedInstanceCount", "osName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'os_family' in kwargs:
            os_family_allowed_values = ["LINUX", "WINDOWS", "MACOS", "UNKNOWN"]
            for os_family_item in kwargs['os_family']:
                if os_family_item not in os_family_allowed_values:
                    raise ValueError(
                        "Invalid value for `os_family`, must be one of {0}".format(os_family_allowed_values)
                    )

        query_params = {
            "jreVendor": kwargs.get("jre_vendor", missing),
            "jreDistribution": kwargs.get("jre_distribution", missing),
            "jreVersion": kwargs.get("jre_version", missing),
            "installationPath": kwargs.get("installation_path", missing),
            "applicationId": kwargs.get("application_id", missing),
            "managedInstanceId": kwargs.get("managed_instance_id", missing),
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
            "timeStart": kwargs.get("time_start", missing),
            "timeEnd": kwargs.get("time_end", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "osFamily": self.base_client.generate_collection_format_param(kwargs.get("os_family", missing), 'multi')
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
                response_type="InstallationUsageCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="InstallationUsageCollection")

    def summarize_jre_usage(self, fleet_id, **kwargs):
        """
        List Java Runtime usage in a specified Fleet filtered by query parameters.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str jre_vendor: (optional)
            The vendor of the Java Runtime.

        :param str jre_distribution: (optional)
            The distribution of the Java Runtime.

        :param str jre_version: (optional)
            The version of the Java Runtime.

        :param str application_id: (optional)
            The Fleet-unique identifier of the related application.

        :param str managed_instance_id: (optional)
            The Fleet-unique identifier of the related managed instance.

        :param list[str] fields: (optional)
            Additional fields to include into the returned model on top of the required ones.
            This parameter can also include 'approximateApplicationCount', 'approximateInstallationCount' and 'approximateManagedInstanceCount'.
            For example 'approximateApplicationCount,approximateManagedInstanceCount'.

            Allowed values are: "approximateInstallationCount", "approximateApplicationCount", "approximateManagedInstanceCount"

        :param datetime time_start: (optional)
            The start of the time period during which resources are searched (formatted according to `RFC3339`__).

            __ https://datatracker.ietf.org/doc/html/rfc3339

        :param datetime time_end: (optional)
            The end of the time period during which resources are searched (formatted according to `RFC3339`__).

            __ https://datatracker.ietf.org/doc/html/rfc3339

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

        :param str sort_order: (optional)
            The sort order, either 'asc' or 'desc'.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort JRE usages. Only one sort order may be provided.
            Default order for _timeFirstSeen_, _timeLastSeen_, and _version_ is **descending**.
            Default order for _timeFirstSeen_, _timeLastSeen_, _version_, _approximateInstallationCount_,
            _approximateApplicationCount_ and _approximateManagedInstanceCount_  is **descending**.
            Default order for _distribution_, _vendor_, and _osName_ is **ascending**.
            If no value is specified _timeLastSeen_ is default.

            Allowed values are: "distribution", "timeFirstSeen", "timeLastSeen", "vendor", "version", "approximateInstallationCount", "approximateApplicationCount", "approximateManagedInstanceCount", "osName"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param list[str] os_family: (optional)
            The operating system type.

            Allowed values are: "LINUX", "WINDOWS", "MACOS", "UNKNOWN"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.JreUsageCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/summarize_jre_usage.py.html>`__ to see an example of how to use summarize_jre_usage API.
        """
        resource_path = "/fleets/{fleetId}/actions/summarizeJreUsage"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "jre_vendor",
            "jre_distribution",
            "jre_version",
            "application_id",
            "managed_instance_id",
            "fields",
            "time_start",
            "time_end",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id",
            "os_family"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_jre_usage got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'fields' in kwargs:
            fields_allowed_values = ["approximateInstallationCount", "approximateApplicationCount", "approximateManagedInstanceCount"]
            for fields_item in kwargs['fields']:
                if fields_item not in fields_allowed_values:
                    raise ValueError(
                        "Invalid value for `fields`, must be one of {0}".format(fields_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["distribution", "timeFirstSeen", "timeLastSeen", "vendor", "version", "approximateInstallationCount", "approximateApplicationCount", "approximateManagedInstanceCount", "osName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'os_family' in kwargs:
            os_family_allowed_values = ["LINUX", "WINDOWS", "MACOS", "UNKNOWN"]
            for os_family_item in kwargs['os_family']:
                if os_family_item not in os_family_allowed_values:
                    raise ValueError(
                        "Invalid value for `os_family`, must be one of {0}".format(os_family_allowed_values)
                    )

        query_params = {
            "jreVendor": kwargs.get("jre_vendor", missing),
            "jreDistribution": kwargs.get("jre_distribution", missing),
            "jreVersion": kwargs.get("jre_version", missing),
            "applicationId": kwargs.get("application_id", missing),
            "managedInstanceId": kwargs.get("managed_instance_id", missing),
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
            "timeStart": kwargs.get("time_start", missing),
            "timeEnd": kwargs.get("time_end", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "osFamily": self.base_client.generate_collection_format_param(kwargs.get("os_family", missing), 'multi')
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
                response_type="JreUsageCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="JreUsageCollection")

    def summarize_managed_instance_usage(self, fleet_id, **kwargs):
        """
        List managed instance usage in a Fleet filtered by query parameters.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str managed_instance_id: (optional)
            The Fleet-unique identifier of the managed instance.

        :param str managed_instance_type: (optional)
            The type of the managed instance.

            Allowed values are: "ORACLE_MANAGEMENT_AGENT"

        :param str jre_vendor: (optional)
            The vendor of the related Java Runtime.

        :param str jre_distribution: (optional)
            The distribution of the related Java Runtime.

        :param str jre_version: (optional)
            The version of the related Java Runtime.

        :param str installation_path: (optional)
            The file system path of the installation.

        :param str application_id: (optional)
            The Fleet-unique identifier of the related application.

        :param list[str] fields: (optional)
            Additional fields to include into the returned model on top of the required ones.
            This parameter can also include 'approximateJreCount', 'approximateInstallationCount' and 'approximateApplicationCount'.
            For example 'approximateJreCount,approximateInstallationCount'.

            Allowed values are: "approximateJreCount", "approximateInstallationCount", "approximateApplicationCount"

        :param datetime time_start: (optional)
            The start of the time period during which resources are searched (formatted according to `RFC3339`__).

            __ https://datatracker.ietf.org/doc/html/rfc3339

        :param datetime time_end: (optional)
            The end of the time period during which resources are searched (formatted according to `RFC3339`__).

            __ https://datatracker.ietf.org/doc/html/rfc3339

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

        :param str sort_order: (optional)
            The sort order, either 'asc' or 'desc'.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort managed instance views. Only one sort order may be provided.
            Default order for _timeFirstSeen_, _timeLastSeen_, approximateJreCount_, _approximateInstallationCount_
            and _approximateApplicationCount_  is **descending**.
            Default order for _osName_ is **ascending**.
            If no value is specified _timeLastSeen_ is default.

            Allowed values are: "timeFirstSeen", "timeLastSeen", "approximateJreCount", "approximateInstallationCount", "approximateApplicationCount", "osName"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param list[str] os_family: (optional)
            The operating system type.

            Allowed values are: "LINUX", "WINDOWS", "MACOS", "UNKNOWN"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.ManagedInstanceUsageCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/summarize_managed_instance_usage.py.html>`__ to see an example of how to use summarize_managed_instance_usage API.
        """
        resource_path = "/fleets/{fleetId}/actions/summarizeManagedInstanceUsage"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "managed_instance_id",
            "managed_instance_type",
            "jre_vendor",
            "jre_distribution",
            "jre_version",
            "installation_path",
            "application_id",
            "fields",
            "time_start",
            "time_end",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id",
            "os_family"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_managed_instance_usage got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'managed_instance_type' in kwargs:
            managed_instance_type_allowed_values = ["ORACLE_MANAGEMENT_AGENT"]
            if kwargs['managed_instance_type'] not in managed_instance_type_allowed_values:
                raise ValueError(
                    "Invalid value for `managed_instance_type`, must be one of {0}".format(managed_instance_type_allowed_values)
                )

        if 'fields' in kwargs:
            fields_allowed_values = ["approximateJreCount", "approximateInstallationCount", "approximateApplicationCount"]
            for fields_item in kwargs['fields']:
                if fields_item not in fields_allowed_values:
                    raise ValueError(
                        "Invalid value for `fields`, must be one of {0}".format(fields_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeFirstSeen", "timeLastSeen", "approximateJreCount", "approximateInstallationCount", "approximateApplicationCount", "osName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'os_family' in kwargs:
            os_family_allowed_values = ["LINUX", "WINDOWS", "MACOS", "UNKNOWN"]
            for os_family_item in kwargs['os_family']:
                if os_family_item not in os_family_allowed_values:
                    raise ValueError(
                        "Invalid value for `os_family`, must be one of {0}".format(os_family_allowed_values)
                    )

        query_params = {
            "managedInstanceId": kwargs.get("managed_instance_id", missing),
            "managedInstanceType": kwargs.get("managed_instance_type", missing),
            "jreVendor": kwargs.get("jre_vendor", missing),
            "jreDistribution": kwargs.get("jre_distribution", missing),
            "jreVersion": kwargs.get("jre_version", missing),
            "installationPath": kwargs.get("installation_path", missing),
            "applicationId": kwargs.get("application_id", missing),
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
            "timeStart": kwargs.get("time_start", missing),
            "timeEnd": kwargs.get("time_end", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "osFamily": self.base_client.generate_collection_format_param(kwargs.get("os_family", missing), 'multi')
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
                response_type="ManagedInstanceUsageCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ManagedInstanceUsageCollection")

    def update_fleet(self, fleet_id, update_fleet_details, **kwargs):
        """
        Update the Fleet specified by an identifier.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.jms.models.UpdateFleetDetails update_fleet_details: (required)
            The new details for the Fleet.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            ETag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the ETag you
            provide matches the resource's current ETag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/update_fleet.py.html>`__ to see an example of how to use update_fleet API.
        """
        resource_path = "/fleets/{fleetId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_fleet got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
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
                body=update_fleet_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_fleet_details)

    def update_fleet_agent_configuration(self, fleet_id, update_fleet_agent_configuration_details, **kwargs):
        """
        Update the Fleet Agent Configuration for the specified Fleet.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.jms.models.UpdateFleetAgentConfigurationDetails update_fleet_agent_configuration_details: (required)
            The new details for the Fleet Agent Configuration.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            ETag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the ETag you
            provide matches the resource's current ETag value.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/update_fleet_agent_configuration.py.html>`__ to see an example of how to use update_fleet_agent_configuration API.
        """
        resource_path = "/fleets/{fleetId}/agentConfiguration"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_fleet_agent_configuration got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
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
                body=update_fleet_agent_configuration_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_fleet_agent_configuration_details)
