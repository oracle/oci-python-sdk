# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
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
            'base_path': '/20210610',
            'service_endpoint_template': 'https://javamanagement.{region}.oci.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'circuit_breaker_strategy': kwargs.get('circuit_breaker_strategy', circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY)
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        if base_client_init_kwargs.get('circuit_breaker_strategy') is None:
            base_client_init_kwargs['circuit_breaker_strategy'] = circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY
        if 'allow_control_chars' in kwargs:
            base_client_init_kwargs['allow_control_chars'] = kwargs.get('allow_control_chars')
        self.base_client = BaseClient("java_management_service", config, signer, jms_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

    def add_fleet_installation_sites(self, fleet_id, add_fleet_installation_sites_details, **kwargs):
        """
        Add Java installation sites in a Fleet.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.jms.models.AddFleetInstallationSitesDetails add_fleet_installation_sites_details: (required)
            List of installation sites to be added.

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/add_fleet_installation_sites.py.html>`__ to see an example of how to use add_fleet_installation_sites API.
        """
        resource_path = "/fleets/{fleetId}/actions/addInstallationSites"
        method = "POST"
        operation_name = "add_fleet_installation_sites"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/InstallationSiteSummary/AddFleetInstallationSites"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "add_fleet_installation_sites got unknown kwargs: {!r}".format(extra_kwargs))

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
                path_params=path_params,
                header_params=header_params,
                body=add_fleet_installation_sites_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=add_fleet_installation_sites_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def cancel_work_request(self, work_request_id, **kwargs):
        """
        Deletes the work request specified by an identifier.


        :param str work_request_id: (required)
            The `OCID`__ of the asynchronous work request.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            ETag from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the ETag you
            provide matches the resource's current ETag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/cancel_work_request.py.html>`__ to see an example of how to use cancel_work_request API.
        """
        resource_path = "/workRequests/{workRequestId}"
        method = "DELETE"
        operation_name = "cancel_work_request"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/WorkRequest/CancelWorkRequest"

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
            "opc-request-id": kwargs.get("opc_request_id", missing),
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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/change_fleet_compartment.py.html>`__ to see an example of how to use change_fleet_compartment API.
        """
        resource_path = "/fleets/{fleetId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_fleet_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/Fleet/ChangeFleetCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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
                path_params=path_params,
                header_params=header_params,
                body=change_fleet_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_fleet_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_blocklist(self, fleet_id, create_blocklist_details, **kwargs):
        """
        Add a new record to the fleet blocklist.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.jms.models.CreateBlocklistDetails create_blocklist_details: (required)
            Details for the new blocklist record.

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.Blocklist`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/create_blocklist.py.html>`__ to see an example of how to use create_blocklist API.
        """
        resource_path = "/fleets/{fleetId}/blocklists"
        method = "POST"
        operation_name = "create_blocklist"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/Blocklist/CreateBlocklist"

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
                "create_blocklist got unknown kwargs: {!r}".format(extra_kwargs))

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
                path_params=path_params,
                header_params=header_params,
                body=create_blocklist_details,
                response_type="Blocklist",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_blocklist_details,
                response_type="Blocklist",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_fleet(self, create_fleet_details, **kwargs):
        """
        Create a new Fleet using the information provided.

        `inventoryLog` is now a required parameter for CreateFleet API.
        Update existing applications using this API
        before July 15, 2022 to ensure the applications continue to work.
        See the `Service Change Notice`__ for more details.
        Migrate existing fleets using the `UpdateFleet` API to set the `inventoryLog` parameter.

        __ https://docs.oracle.com/en-us/iaas/Content/servicechanges.htm#JMS


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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/create_fleet.py.html>`__ to see an example of how to use create_fleet API.
        """
        resource_path = "/fleets"
        method = "POST"
        operation_name = "create_fleet"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/Fleet/CreateFleet"

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
                header_params=header_params,
                body=create_fleet_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_fleet_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def delete_blocklist(self, fleet_id, blocklist_key, **kwargs):
        """
        Deletes the blocklist record specified by an identifier.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str blocklist_key: (required)
            The unique identifier of the blocklist record.

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/delete_blocklist.py.html>`__ to see an example of how to use delete_blocklist API.
        """
        resource_path = "/fleets/{fleetId}/blocklists/{blocklistKey}"
        method = "DELETE"
        operation_name = "delete_blocklist"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/Blocklist/DeleteBlocklist"

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
                "delete_blocklist got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id,
            "blocklistKey": blocklist_key
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

    def delete_crypto_analysis_result(self, fleet_id, crypto_analysis_result_id, **kwargs):
        """
        Deletes only the metadata of the Crypto Event Analysis result, but the file remains in the object storage.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str crypto_analysis_result_id: (required)
            The OCID of the analysis result.

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/delete_crypto_analysis_result.py.html>`__ to see an example of how to use delete_crypto_analysis_result API.
        """
        resource_path = "/fleets/{fleetId}/cryptoAnalysisResults/{cryptoAnalysisResultId}"
        method = "DELETE"
        operation_name = "delete_crypto_analysis_result"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/CryptoAnalysisResult/DeleteCryptoAnalysisResult"

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
                "delete_crypto_analysis_result got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id,
            "cryptoAnalysisResultId": crypto_analysis_result_id
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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/delete_fleet.py.html>`__ to see an example of how to use delete_fleet API.
        """
        resource_path = "/fleets/{fleetId}"
        method = "DELETE"
        operation_name = "delete_fleet"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/Fleet/DeleteFleet"

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

    def generate_agent_deploy_script(self, fleet_id, generate_agent_deploy_script_details, **kwargs):
        """
        Generates Agent Deploy Script for Fleet using the information provided.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.jms.models.GenerateAgentDeployScriptDetails generate_agent_deploy_script_details: (required)
            Attributes to generate agent deploy script for a Fleet.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/generate_agent_deploy_script.py.html>`__ to see an example of how to use generate_agent_deploy_script API.
        """
        resource_path = "/fleets/{fleetId}/actions/generateAgentDeployScript"
        method = "POST"
        operation_name = "generate_agent_deploy_script"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/Fleet/GenerateAgentDeployScript"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "generate_agent_deploy_script got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "text/plain",
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
                header_params=header_params,
                body=generate_agent_deploy_script_details,
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
                body=generate_agent_deploy_script_details,
                response_type="stream",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_crypto_analysis_result(self, fleet_id, crypto_analysis_result_id, **kwargs):
        """
        Retrieve metadata of the Crypto Event Analysis result.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str crypto_analysis_result_id: (required)
            The OCID of the analysis result.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.CryptoAnalysisResult`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/get_crypto_analysis_result.py.html>`__ to see an example of how to use get_crypto_analysis_result API.
        """
        resource_path = "/fleets/{fleetId}/cryptoAnalysisResults/{cryptoAnalysisResultId}"
        method = "GET"
        operation_name = "get_crypto_analysis_result"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/CryptoAnalysisResult/GetCryptoAnalysisResult"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_crypto_analysis_result got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id,
            "cryptoAnalysisResultId": crypto_analysis_result_id
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
                response_type="CryptoAnalysisResult",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="CryptoAnalysisResult",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.Fleet`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/get_fleet.py.html>`__ to see an example of how to use get_fleet API.
        """
        resource_path = "/fleets/{fleetId}"
        method = "GET"
        operation_name = "get_fleet"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/Fleet/GetFleet"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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
                response_type="Fleet",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Fleet",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_fleet_advanced_feature_configuration(self, fleet_id, **kwargs):
        """
        Returns fleet level advanced feature configuration


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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.FleetAdvancedFeatureConfiguration`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/get_fleet_advanced_feature_configuration.py.html>`__ to see an example of how to use get_fleet_advanced_feature_configuration API.
        """
        resource_path = "/fleets/{fleetId}/advancedFeatureConfiguration"
        method = "GET"
        operation_name = "get_fleet_advanced_feature_configuration"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/FleetAdvancedFeatureConfiguration/GetFleetAdvancedFeatureConfiguration"

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
                "get_fleet_advanced_feature_configuration got unknown kwargs: {!r}".format(extra_kwargs))

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
                response_type="FleetAdvancedFeatureConfiguration",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="FleetAdvancedFeatureConfiguration",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.FleetAgentConfiguration`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/get_fleet_agent_configuration.py.html>`__ to see an example of how to use get_fleet_agent_configuration API.
        """
        resource_path = "/fleets/{fleetId}/agentConfiguration"
        method = "GET"
        operation_name = "get_fleet_agent_configuration"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/FleetAgentConfiguration/GetFleetAgentConfiguration"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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
                response_type="FleetAgentConfiguration",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="FleetAgentConfiguration",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_java_family(self, family_version, **kwargs):
        """
        Returns metadata associated with a specific Java release family.


        :param str family_version: (required)
            Unique Java family version identifier.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.JavaFamily`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/get_java_family.py.html>`__ to see an example of how to use get_java_family API.
        """
        resource_path = "/javaFamilies/{familyVersion}"
        method = "GET"
        operation_name = "get_java_family"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/JavaFamily/GetJavaFamily"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_java_family got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "familyVersion": family_version
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
                response_type="JavaFamily",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="JavaFamily",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_java_release(self, release_version, **kwargs):
        """
        Returns detail of a Java release.


        :param str release_version: (required)
            Unique Java release version identifier

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.JavaRelease`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/get_java_release.py.html>`__ to see an example of how to use get_java_release API.
        """
        resource_path = "/javaReleases/{releaseVersion}"
        method = "GET"
        operation_name = "get_java_release"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/JavaRelease/GetJavaRelease"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_java_release got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "releaseVersion": release_version
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
                response_type="JavaRelease",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="JavaRelease",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.WorkRequest`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/get_work_request.py.html>`__ to see an example of how to use get_work_request API.
        """
        resource_path = "/workRequests/{workRequestId}"
        method = "GET"
        operation_name = "get_work_request"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/WorkRequest/GetWorkRequest"

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

    def list_blocklists(self, fleet_id, **kwargs):
        """
        Returns a list of blocklist entities contained by a fleet.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str operation: (optional)
            The operation type.

            Allowed values are: "CREATE_FLEET", "DELETE_FLEET", "MOVE_FLEET", "UPDATE_FLEET", "UPDATE_FLEET_AGENT_CONFIGURATION", "DELETE_JAVA_INSTALLATION", "CREATE_JAVA_INSTALLATION", "COLLECT_JFR", "REQUEST_CRYPTO_EVENT_ANALYSIS", "SCAN_JAVA_SERVER_USAGE", "SCAN_LIBRARY_USAGE"

        :param str managed_instance_id: (optional)
            The Fleet-unique identifier of the related managed instance.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

        :param str sort_order: (optional)
            The sort order, either 'asc' or 'desc'.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort blocklist records. Only one sort order may be provided.
            Default order for _operation_ is **ascending**.
            If no value is specified _operation_ is default.

            Allowed values are: "operation"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.BlocklistCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/list_blocklists.py.html>`__ to see an example of how to use list_blocklists API.
        """
        resource_path = "/fleets/{fleetId}/blocklists"
        method = "GET"
        operation_name = "list_blocklists"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/Blocklist/ListBlocklists"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "operation",
            "managed_instance_id",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_blocklists got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'operation' in kwargs:
            operation_allowed_values = ["CREATE_FLEET", "DELETE_FLEET", "MOVE_FLEET", "UPDATE_FLEET", "UPDATE_FLEET_AGENT_CONFIGURATION", "DELETE_JAVA_INSTALLATION", "CREATE_JAVA_INSTALLATION", "COLLECT_JFR", "REQUEST_CRYPTO_EVENT_ANALYSIS", "SCAN_JAVA_SERVER_USAGE", "SCAN_LIBRARY_USAGE"]
            if kwargs['operation'] not in operation_allowed_values:
                raise ValueError(
                    "Invalid value for `operation`, must be one of {0}".format(operation_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["operation"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "operation": kwargs.get("operation", missing),
            "managedInstanceId": kwargs.get("managed_instance_id", missing),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="BlocklistCollection",
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
                response_type="BlocklistCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_crypto_analysis_results(self, fleet_id, **kwargs):
        """
        List Crypto Event Analysis results.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str aggregation_mode: (optional)
            The aggregation mode of the crypto event analysis result.

            Allowed values are: "JFR", "MANAGED_INSTANCE"

        :param str managed_instance_id: (optional)
            The Fleet-unique identifier of the related managed instance.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

        :param str sort_order: (optional)
            The sort order, either 'asc' or 'desc'.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort crypto event analysis results. Only one sort order may be provided.
            Default order for _timeCreated_, and _jreVersion_ is **descending**.
            Default order for _managedInstanceId_, _jreDistribution_, _jreVendor_ and _osName_ is **ascending**.
            If no value is specified _timeCreated_ is default.

            Allowed values are: "timeCreated", "managedInstanceId", "workRequestId"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param datetime time_start: (optional)
            The start of the time period during which resources are searched (formatted according to `RFC3339`__).

            __ https://datatracker.ietf.org/doc/html/rfc3339

        :param datetime time_end: (optional)
            The end of the time period during which resources are searched (formatted according to `RFC3339`__).

            __ https://datatracker.ietf.org/doc/html/rfc3339

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.CryptoAnalysisResultCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/list_crypto_analysis_results.py.html>`__ to see an example of how to use list_crypto_analysis_results API.
        """
        resource_path = "/fleets/{fleetId}/cryptoAnalysisResults"
        method = "GET"
        operation_name = "list_crypto_analysis_results"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/CryptoAnalysisResult/ListCryptoAnalysisResults"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "aggregation_mode",
            "managed_instance_id",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id",
            "time_start",
            "time_end"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_crypto_analysis_results got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'aggregation_mode' in kwargs:
            aggregation_mode_allowed_values = ["JFR", "MANAGED_INSTANCE"]
            if kwargs['aggregation_mode'] not in aggregation_mode_allowed_values:
                raise ValueError(
                    "Invalid value for `aggregation_mode`, must be one of {0}".format(aggregation_mode_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "managedInstanceId", "workRequestId"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "aggregationMode": kwargs.get("aggregation_mode", missing),
            "managedInstanceId": kwargs.get("managed_instance_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "timeStart": kwargs.get("time_start", missing),
            "timeEnd": kwargs.get("time_end", missing)
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
                response_type="CryptoAnalysisResultCollection",
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
                response_type="CryptoAnalysisResultCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_fleets(self, **kwargs):
        """
        Returns a list of all the Fleets contained by a compartment. The query parameter `compartmentId`
        is required unless the query parameter `id` is specified.


        :param str compartment_id: (optional)
            The `OCID`__ of the compartment in which to list resources.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            The ID of the Fleet.

        :param str lifecycle_state: (optional)
            The state of the lifecycle.

            Allowed values are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "NEEDS_ATTENTION", "UPDATING"

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

        :param str display_name_contains: (optional)
            Filter the list with displayName contains the given value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.FleetCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/list_fleets.py.html>`__ to see an example of how to use list_fleets API.
        """
        resource_path = "/fleets"
        method = "GET"
        operation_name = "list_fleets"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/Fleet/ListFleets"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "id",
            "lifecycle_state",
            "display_name",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id",
            "display_name_contains"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_fleets got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "NEEDS_ATTENTION", "UPDATING"]
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
            "sortBy": kwargs.get("sort_by", missing),
            "displayNameContains": kwargs.get("display_name_contains", missing)
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
                response_type="FleetCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="FleetCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_installation_sites(self, fleet_id, **kwargs):
        """
        List Java installation sites in a Fleet filtered by query parameters.


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

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

        :param str sort_order: (optional)
            The sort order, either 'asc' or 'desc'.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort installation sites. Only one sort order may be provided.
            Default order for _timeLastSeen_, and _jreVersion_, _approximateApplicationCount_ is **descending**.
            Default order for _managedInstanceId_, _jreDistribution_, _jreVendor_ and _osName_ is **ascending**.
            If no value is specified _managedInstanceId_ is default.

            Allowed values are: "managedInstanceId", "jreDistribution", "jreVendor", "jreVersion", "path", "approximateApplicationCount", "osName", "securityStatus"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param list[str] os_family: (optional)
            The operating system type.

            Allowed values are: "LINUX", "WINDOWS", "MACOS", "UNKNOWN"

        :param str jre_security_status: (optional)
            The security status of the Java Runtime.

            Allowed values are: "UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED"

        :param str path_contains: (optional)
            Filter the list with path contains the given value.

        :param datetime time_start: (optional)
            The start of the time period during which resources are searched (formatted according to `RFC3339`__).

            __ https://datatracker.ietf.org/doc/html/rfc3339

        :param datetime time_end: (optional)
            The end of the time period during which resources are searched (formatted according to `RFC3339`__).

            __ https://datatracker.ietf.org/doc/html/rfc3339

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.InstallationSiteCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/list_installation_sites.py.html>`__ to see an example of how to use list_installation_sites API.
        """
        resource_path = "/fleets/{fleetId}/installationSites"
        method = "GET"
        operation_name = "list_installation_sites"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/InstallationSiteSummary/ListInstallationSites"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "jre_vendor",
            "jre_distribution",
            "jre_version",
            "installation_path",
            "application_id",
            "managed_instance_id",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id",
            "os_family",
            "jre_security_status",
            "path_contains",
            "time_start",
            "time_end"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_installation_sites got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
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
            sort_by_allowed_values = ["managedInstanceId", "jreDistribution", "jreVendor", "jreVersion", "path", "approximateApplicationCount", "osName", "securityStatus"]
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

        if 'jre_security_status' in kwargs:
            jre_security_status_allowed_values = ["UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED"]
            if kwargs['jre_security_status'] not in jre_security_status_allowed_values:
                raise ValueError(
                    "Invalid value for `jre_security_status`, must be one of {0}".format(jre_security_status_allowed_values)
                )

        query_params = {
            "jreVendor": kwargs.get("jre_vendor", missing),
            "jreDistribution": kwargs.get("jre_distribution", missing),
            "jreVersion": kwargs.get("jre_version", missing),
            "installationPath": kwargs.get("installation_path", missing),
            "applicationId": kwargs.get("application_id", missing),
            "managedInstanceId": kwargs.get("managed_instance_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "osFamily": self.base_client.generate_collection_format_param(kwargs.get("os_family", missing), 'multi'),
            "jreSecurityStatus": kwargs.get("jre_security_status", missing),
            "pathContains": kwargs.get("path_contains", missing),
            "timeStart": kwargs.get("time_start", missing),
            "timeEnd": kwargs.get("time_end", missing)
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
                response_type="InstallationSiteCollection",
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
                response_type="InstallationSiteCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_java_families(self, **kwargs):
        """
        Returns a list of the Java release family information.
        A Java release family is typically a major version in the Java version identifier.


        :param str family_version: (optional)
            The version identifier for the Java family.

        :param str display_name: (optional)
            The display name for the Java family.

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

        :param str sort_order: (optional)
            The sort order, either 'asc' or 'desc'.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            If no value is specified _familyVersion_ is default.

            Allowed values are: "familyVersion", "endOfSupportLifeDate", "supportType"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.JavaFamilyCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/list_java_families.py.html>`__ to see an example of how to use list_java_families API.
        """
        resource_path = "/javaFamilies"
        method = "GET"
        operation_name = "list_java_families"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/JavaFamily/ListJavaFamilies"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "family_version",
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
                "list_java_families got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["familyVersion", "endOfSupportLifeDate", "supportType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "familyVersion": kwargs.get("family_version", missing),
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
                response_type="JavaFamilyCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="JavaFamilyCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_java_releases(self, **kwargs):
        """
        Returns a list of Java releases.


        :param str release_version: (optional)
            Unique Java release version identifier

        :param str family_version: (optional)
            The version identifier for the Java family.

        :param str release_type: (optional)
            Java release type.

            Allowed values are: "CPU", "FEATURE", "BPR", "PATCH_RELEASE"

        :param str jre_security_status: (optional)
            The security status of the Java Runtime.

            Allowed values are: "UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED"

        :param str license_type: (optional)
            Java license type.

            Allowed values are: "OTN", "NFTC", "RESTRICTED"

        :param int limit: (optional)
            The maximum number of items to return.

        :param str page: (optional)
            The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

        :param str sort_order: (optional)
            The sort order, either 'asc' or 'desc'.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            If no value is specified _releaseDate_ is default.

            Allowed values are: "releaseDate", "releaseVersion", "familyVersion", "licenseType"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.JavaReleaseCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/list_java_releases.py.html>`__ to see an example of how to use list_java_releases API.
        """
        resource_path = "/javaReleases"
        method = "GET"
        operation_name = "list_java_releases"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/JavaRelease/ListJavaReleases"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "release_version",
            "family_version",
            "release_type",
            "jre_security_status",
            "license_type",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_java_releases got unknown kwargs: {!r}".format(extra_kwargs))

        if 'release_type' in kwargs:
            release_type_allowed_values = ["CPU", "FEATURE", "BPR", "PATCH_RELEASE"]
            if kwargs['release_type'] not in release_type_allowed_values:
                raise ValueError(
                    "Invalid value for `release_type`, must be one of {0}".format(release_type_allowed_values)
                )

        if 'jre_security_status' in kwargs:
            jre_security_status_allowed_values = ["UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED"]
            if kwargs['jre_security_status'] not in jre_security_status_allowed_values:
                raise ValueError(
                    "Invalid value for `jre_security_status`, must be one of {0}".format(jre_security_status_allowed_values)
                )

        if 'license_type' in kwargs:
            license_type_allowed_values = ["OTN", "NFTC", "RESTRICTED"]
            if kwargs['license_type'] not in license_type_allowed_values:
                raise ValueError(
                    "Invalid value for `license_type`, must be one of {0}".format(license_type_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["releaseDate", "releaseVersion", "familyVersion", "licenseType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "releaseVersion": kwargs.get("release_version", missing),
            "familyVersion": kwargs.get("family_version", missing),
            "releaseType": kwargs.get("release_type", missing),
            "jreSecurityStatus": kwargs.get("jre_security_status", missing),
            "licenseType": kwargs.get("license_type", missing),
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
                response_type="JavaReleaseCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="JavaReleaseCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_jre_usage(self, **kwargs):
        """
        List Java Runtime usage in a specified host filtered by query parameters.


        :param str compartment_id: (optional)
            The `OCID`__ of the compartment in which to list resources.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str host_id: (optional)
            The host `OCID`__ of the managed instance.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str application_id: (optional)
            The Fleet-unique identifier of the application.

        :param str application_name: (optional)
            The name of the application.

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

            Allowed values are: "distribution", "timeFirstSeen", "timeLastSeen", "vendor", "version", "approximateInstallationCount", "approximateApplicationCount", "approximateManagedInstanceCount", "osName", "securityStatus"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.JreUsageCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/list_jre_usage.py.html>`__ to see an example of how to use list_jre_usage API.
        """
        resource_path = "/listJreUsage"
        method = "GET"
        operation_name = "list_jre_usage"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/JreUsage/ListJreUsage"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "host_id",
            "application_id",
            "application_name",
            "time_start",
            "time_end",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_jre_usage got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["distribution", "timeFirstSeen", "timeLastSeen", "vendor", "version", "approximateInstallationCount", "approximateApplicationCount", "approximateManagedInstanceCount", "osName", "securityStatus"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "hostId": kwargs.get("host_id", missing),
            "applicationId": kwargs.get("application_id", missing),
            "applicationName": kwargs.get("application_name", missing),
            "timeStart": kwargs.get("time_start", missing),
            "timeEnd": kwargs.get("time_end", missing),
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
                response_type="JreUsageCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="JreUsageCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_work_items(self, work_request_id, **kwargs):
        """
        Retrieve a (paginated) list of work items for a specified work request.


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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.WorkItemCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/list_work_items.py.html>`__ to see an example of how to use list_work_items API.
        """
        resource_path = "/workRequests/{workRequestId}/workItems"
        method = "GET"
        operation_name = "list_work_items"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/WorkItemSummary/ListWorkItems"

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
                "list_work_items got unknown kwargs: {!r}".format(extra_kwargs))

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
                response_type="WorkItemCollection",
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
                response_type="WorkItemCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.WorkRequestErrorCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/list_work_request_errors.py.html>`__ to see an example of how to use list_work_request_errors API.
        """
        resource_path = "/workRequests/{workRequestId}/errors"
        method = "GET"
        operation_name = "list_work_request_errors"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/WorkRequestError/ListWorkRequestErrors"

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.WorkRequestLogEntryCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/list_work_request_logs.py.html>`__ to see an example of how to use list_work_request_logs API.
        """
        resource_path = "/workRequests/{workRequestId}/logs"
        method = "GET"
        operation_name = "list_work_request_logs"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/WorkRequestLogEntry/ListWorkRequestLogs"

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

    def list_work_requests(self, **kwargs):
        """
        List the work requests in a compartment. The query parameter `compartmentId` is required unless the query parameter `id` or `fleetId` is specified.


        :param str compartment_id: (optional)
            The `OCID`__ of the compartment in which to list resources.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            The ID of an asynchronous work request.

        :param str fleet_id: (optional)
            The `OCID`__ of the fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str page: (optional)
            The page token representing the page at which to start retrieving results. The token is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of items to return.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.WorkRequestCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/list_work_requests.py.html>`__ to see an example of how to use list_work_requests API.
        """
        resource_path = "/workRequests"
        method = "GET"
        operation_name = "list_work_requests"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/WorkRequest/ListWorkRequests"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "id",
            "fleet_id",
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
            "fleetId": kwargs.get("fleet_id", missing),
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

    def remove_fleet_installation_sites(self, fleet_id, remove_fleet_installation_sites_details, **kwargs):
        """
        Remove Java installation sites in a Fleet.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.jms.models.RemoveFleetInstallationSitesDetails remove_fleet_installation_sites_details: (required)
            List of installation sites to be deleted.

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/remove_fleet_installation_sites.py.html>`__ to see an example of how to use remove_fleet_installation_sites API.
        """
        resource_path = "/fleets/{fleetId}/actions/removeInstallationSites"
        method = "POST"
        operation_name = "remove_fleet_installation_sites"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/InstallationSiteSummary/RemoveFleetInstallationSites"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "remove_fleet_installation_sites got unknown kwargs: {!r}".format(extra_kwargs))

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
                path_params=path_params,
                header_params=header_params,
                body=remove_fleet_installation_sites_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=remove_fleet_installation_sites_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def request_crypto_analyses(self, fleet_id, request_crypto_analyses_details, **kwargs):
        """
        Request to perform crypto analyses. The result of crypto analysis will be uploaded to the
        object storage bucket desiginated when enable Crypto Event Analysis feature.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.jms.models.RequestCryptoAnalysesDetails request_crypto_analyses_details: (required)
            Detail information to start Crypto Analyses

        :param str opc_request_id: (optional)
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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/request_crypto_analyses.py.html>`__ to see an example of how to use request_crypto_analyses API.
        """
        resource_path = "/fleets/{fleetId}/actions/requestCryptoAnalyses"
        method = "POST"
        operation_name = "request_crypto_analyses"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/Fleet/RequestCryptoAnalyses"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "request_crypto_analyses got unknown kwargs: {!r}".format(extra_kwargs))

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
                body=request_crypto_analyses_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=request_crypto_analyses_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def request_jfr_recordings(self, fleet_id, request_jfr_recordings_details, **kwargs):
        """
        Request to collect the JFR recordings on the selected target. The JFR files are uploaded
        to the object storage bucket that you designated when you enabled the recording feature.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.jms.models.RequestJfrRecordingsDetails request_jfr_recordings_details: (required)
            Detail information to start JFR recordings.

        :param str opc_request_id: (optional)
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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/request_jfr_recordings.py.html>`__ to see an example of how to use request_jfr_recordings API.
        """
        resource_path = "/fleets/{fleetId}/actions/requestJfrRecordings"
        method = "POST"
        operation_name = "request_jfr_recordings"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/Fleet/RequestJfrRecordings"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "request_jfr_recordings got unknown kwargs: {!r}".format(extra_kwargs))

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
                body=request_jfr_recordings_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=request_jfr_recordings_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def scan_java_server_usage(self, fleet_id, scan_java_server_usage_details, **kwargs):
        """
        Scan Java server usage in a fleet.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.jms.models.ScanJavaServerUsageDetails scan_java_server_usage_details: (required)
            List of managed instances to be scanned.

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/scan_java_server_usage.py.html>`__ to see an example of how to use scan_java_server_usage API.
        """
        resource_path = "/fleets/{fleetId}/actions/scanJavaServerUsage"
        method = "POST"
        operation_name = "scan_java_server_usage"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/JavaServerUsage/ScanJavaServerUsage"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "scan_java_server_usage got unknown kwargs: {!r}".format(extra_kwargs))

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
                path_params=path_params,
                header_params=header_params,
                body=scan_java_server_usage_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=scan_java_server_usage_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def scan_library_usage(self, fleet_id, scan_library_usage_details, **kwargs):
        """
        Scan library usage in a fleet.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.jms.models.ScanLibraryUsageDetails scan_library_usage_details: (required)
            List of managed instances to be scanned.

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/scan_library_usage.py.html>`__ to see an example of how to use scan_library_usage API.
        """
        resource_path = "/fleets/{fleetId}/actions/scanLibraryUsage"
        method = "POST"
        operation_name = "scan_library_usage"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/LibraryUsage/ScanLibraryUsage"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "scan_library_usage got unknown kwargs: {!r}".format(extra_kwargs))

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
                path_params=path_params,
                header_params=header_params,
                body=scan_library_usage_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=scan_library_usage_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

        :param str display_name_contains: (optional)
            Filter the list with displayName contains the given value.

        :param str library_key: (optional)
            The library key.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.ApplicationUsageCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/summarize_application_usage.py.html>`__ to see an example of how to use summarize_application_usage API.
        """
        resource_path = "/fleets/{fleetId}/actions/summarizeApplicationUsage"
        method = "GET"
        operation_name = "summarize_application_usage"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/ApplicationUsage/SummarizeApplicationUsage"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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
            "os_family",
            "display_name_contains",
            "library_key"
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
            "osFamily": self.base_client.generate_collection_format_param(kwargs.get("os_family", missing), 'multi'),
            "displayNameContains": kwargs.get("display_name_contains", missing),
            "libraryKey": kwargs.get("library_key", missing)
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
                response_type="ApplicationUsageCollection",
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
                response_type="ApplicationUsageCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def summarize_deployed_application_usage(self, fleet_id, **kwargs):
        """
        List deployed applications in a fleet filtered by query parameters.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str server_key: (optional)
            The server key.

        :param str server_instance_key: (optional)
            The Java server instance key.

        :param str managed_instance_id: (optional)
            The Fleet-unique identifier of the managed instance.

        :param str library_key: (optional)
            The library key.

        :param str application_key: (optional)
            The deployed application key.

        :param str application_name_contains: (optional)
            Filter the list with deployed application name contains the given value.

        :param str application_name: (optional)
            The deployed application name.

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
            The field to sort deployed applications.  Only one sort order may be provided.
            If no value is specified _timeLastSeen_ is default.

            Allowed values are: "applicationName", "applicationType", "isClustered", "javaServerInstanceCount", "timeFirstSeen", "timeLastSeen"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.DeployedApplicationUsageCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/summarize_deployed_application_usage.py.html>`__ to see an example of how to use summarize_deployed_application_usage API.
        """
        resource_path = "/fleets/{fleetId}/actions/summarizeDeployedApplicationUsage"
        method = "GET"
        operation_name = "summarize_deployed_application_usage"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/DeployedApplicationUsage/SummarizeDeployedApplicationUsage"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "server_key",
            "server_instance_key",
            "managed_instance_id",
            "library_key",
            "application_key",
            "application_name_contains",
            "application_name",
            "time_start",
            "time_end",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_deployed_application_usage got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
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
            sort_by_allowed_values = ["applicationName", "applicationType", "isClustered", "javaServerInstanceCount", "timeFirstSeen", "timeLastSeen"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "serverKey": kwargs.get("server_key", missing),
            "serverInstanceKey": kwargs.get("server_instance_key", missing),
            "managedInstanceId": kwargs.get("managed_instance_id", missing),
            "libraryKey": kwargs.get("library_key", missing),
            "applicationKey": kwargs.get("application_key", missing),
            "applicationNameContains": kwargs.get("application_name_contains", missing),
            "applicationName": kwargs.get("application_name", missing),
            "timeStart": kwargs.get("time_start", missing),
            "timeEnd": kwargs.get("time_end", missing),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DeployedApplicationUsageCollection",
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
                response_type="DeployedApplicationUsageCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

        :param str path_contains: (optional)
            Filter the list with path contains the given value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.InstallationUsageCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/summarize_installation_usage.py.html>`__ to see an example of how to use summarize_installation_usage API.
        """
        resource_path = "/fleets/{fleetId}/actions/summarizeInstallationUsage"
        method = "GET"
        operation_name = "summarize_installation_usage"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/InstallationUsage/SummarizeInstallationUsage"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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
            "os_family",
            "path_contains"
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
            "osFamily": self.base_client.generate_collection_format_param(kwargs.get("os_family", missing), 'multi'),
            "pathContains": kwargs.get("path_contains", missing)
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
                response_type="InstallationUsageCollection",
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
                response_type="InstallationUsageCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def summarize_java_server_instance_usage(self, fleet_id, **kwargs):
        """
        List Java server instances in a fleet filtered by query parameters.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str server_key: (optional)
            The server key.

        :param str server_instance_key: (optional)
            The Java server instance key.

        :param str managed_instance_id: (optional)
            The Fleet-unique identifier of the managed instance.

        :param str application_key: (optional)
            The deployed application key.

        :param str library_key: (optional)
            The library key.

        :param str server_instance_name_contains: (optional)
            Filter the list with Java server instance name contains the given value.

        :param str server_instance_name: (optional)
            The Java server instance name.

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
            The field to sort Java server instances.  Only one sort order may be provided.
            If no value is specified _timeLastSeen_ is default.

            Allowed values are: "serverInstanceName", "managedInstanceName", "approximateDeployedApplicationCount", "timeFirstSeen", "timeLastSeen"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.JavaServerInstanceUsageCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/summarize_java_server_instance_usage.py.html>`__ to see an example of how to use summarize_java_server_instance_usage API.
        """
        resource_path = "/fleets/{fleetId}/actions/summarizeJavaServerInstanceUsage"
        method = "GET"
        operation_name = "summarize_java_server_instance_usage"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/JavaServerInstanceUsage/SummarizeJavaServerInstanceUsage"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "server_key",
            "server_instance_key",
            "managed_instance_id",
            "application_key",
            "library_key",
            "server_instance_name_contains",
            "server_instance_name",
            "time_start",
            "time_end",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_java_server_instance_usage got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
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
            sort_by_allowed_values = ["serverInstanceName", "managedInstanceName", "approximateDeployedApplicationCount", "timeFirstSeen", "timeLastSeen"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "serverKey": kwargs.get("server_key", missing),
            "serverInstanceKey": kwargs.get("server_instance_key", missing),
            "managedInstanceId": kwargs.get("managed_instance_id", missing),
            "applicationKey": kwargs.get("application_key", missing),
            "libraryKey": kwargs.get("library_key", missing),
            "serverInstanceNameContains": kwargs.get("server_instance_name_contains", missing),
            "serverInstanceName": kwargs.get("server_instance_name", missing),
            "timeStart": kwargs.get("time_start", missing),
            "timeEnd": kwargs.get("time_end", missing),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="JavaServerInstanceUsageCollection",
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
                response_type="JavaServerInstanceUsageCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def summarize_java_server_usage(self, fleet_id, **kwargs):
        """
        List Java servers in a fleet filtered by query parameters.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str server_key: (optional)
            The server key.

        :param str server_name_contains: (optional)
            Filter the list with server name contains the given value.

        :param str server_name: (optional)
            The server name.

        :param str server_version: (optional)
            The server version.

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
            The field to sort Java servers.  Only one sort order may be provided.
            If no value is specified _timeLastSeen_ is default.

            Allowed values are: "serverName", "serverVersion", "serverInstanceCount", "approximateDeployedApplicationCount", "timeFirstSeen", "timeLastSeen"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.JavaServerUsageCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/summarize_java_server_usage.py.html>`__ to see an example of how to use summarize_java_server_usage API.
        """
        resource_path = "/fleets/{fleetId}/actions/summarizeJavaServerUsage"
        method = "GET"
        operation_name = "summarize_java_server_usage"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/JavaServerUsage/SummarizeJavaServerUsage"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "server_key",
            "server_name_contains",
            "server_name",
            "server_version",
            "time_start",
            "time_end",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_java_server_usage got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
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
            sort_by_allowed_values = ["serverName", "serverVersion", "serverInstanceCount", "approximateDeployedApplicationCount", "timeFirstSeen", "timeLastSeen"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "serverKey": kwargs.get("server_key", missing),
            "serverNameContains": kwargs.get("server_name_contains", missing),
            "serverName": kwargs.get("server_name", missing),
            "serverVersion": kwargs.get("server_version", missing),
            "timeStart": kwargs.get("time_start", missing),
            "timeEnd": kwargs.get("time_end", missing),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="JavaServerUsageCollection",
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
                response_type="JavaServerUsageCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def summarize_jre_usage(self, fleet_id, **kwargs):
        """
        List Java Runtime usage in a specified Fleet filtered by query parameters.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str jre_id: (optional)
            The Fleet-unique identifier of the related Java Runtime.

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

            Allowed values are: "distribution", "timeFirstSeen", "timeLastSeen", "vendor", "version", "approximateInstallationCount", "approximateApplicationCount", "approximateManagedInstanceCount", "osName", "securityStatus"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param list[str] os_family: (optional)
            The operating system type.

            Allowed values are: "LINUX", "WINDOWS", "MACOS", "UNKNOWN"

        :param str jre_security_status: (optional)
            The security status of the Java Runtime.

            Allowed values are: "UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.JreUsageCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/summarize_jre_usage.py.html>`__ to see an example of how to use summarize_jre_usage API.
        """
        resource_path = "/fleets/{fleetId}/actions/summarizeJreUsage"
        method = "GET"
        operation_name = "summarize_jre_usage"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/JreUsage/SummarizeJreUsage"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "jre_id",
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
            "os_family",
            "jre_security_status"
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
            sort_by_allowed_values = ["distribution", "timeFirstSeen", "timeLastSeen", "vendor", "version", "approximateInstallationCount", "approximateApplicationCount", "approximateManagedInstanceCount", "osName", "securityStatus"]
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

        if 'jre_security_status' in kwargs:
            jre_security_status_allowed_values = ["UNKNOWN", "UP_TO_DATE", "UPDATE_REQUIRED", "UPGRADE_REQUIRED"]
            if kwargs['jre_security_status'] not in jre_security_status_allowed_values:
                raise ValueError(
                    "Invalid value for `jre_security_status`, must be one of {0}".format(jre_security_status_allowed_values)
                )

        query_params = {
            "jreId": kwargs.get("jre_id", missing),
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
            "osFamily": self.base_client.generate_collection_format_param(kwargs.get("os_family", missing), 'multi'),
            "jreSecurityStatus": kwargs.get("jre_security_status", missing)
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
                response_type="JreUsageCollection",
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
                response_type="JreUsageCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def summarize_library_usage(self, fleet_id, **kwargs):
        """
        List libraries in a fleet filtered by query parameters.


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str server_instance_key: (optional)
            The Java server instance key.

        :param str managed_instance_id: (optional)
            The Fleet-unique identifier of the managed instance.

        :param str application_key: (optional)
            The deployed application key.

        :param str library_key: (optional)
            The library key.

        :param str library_name_contains: (optional)
            Filter the list with library name contains the given value.

        :param str library_name: (optional)
            The library name.

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
            The field to sort libraries.  Only one sort order may be provided.
            If no value is specified _timeLastSeen_ is default.

            Allowed values are: "applicationCount", "javaServerInstanceCount", "cvssScore", "deployedApplicationCount", "libraryName", "libraryVersion", "managedInstanceCount", "timeFirstSeen", "timeLastSeen"

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.LibraryUsageCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/summarize_library_usage.py.html>`__ to see an example of how to use summarize_library_usage API.
        """
        resource_path = "/fleets/{fleetId}/actions/summarizeLibraryUsage"
        method = "GET"
        operation_name = "summarize_library_usage"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/LibraryUsage/SummarizeLibraryUsage"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "server_instance_key",
            "managed_instance_id",
            "application_key",
            "library_key",
            "library_name_contains",
            "library_name",
            "time_start",
            "time_end",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_library_usage got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "fleetId": fleet_id
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
            sort_by_allowed_values = ["applicationCount", "javaServerInstanceCount", "cvssScore", "deployedApplicationCount", "libraryName", "libraryVersion", "managedInstanceCount", "timeFirstSeen", "timeLastSeen"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "serverInstanceKey": kwargs.get("server_instance_key", missing),
            "managedInstanceId": kwargs.get("managed_instance_id", missing),
            "applicationKey": kwargs.get("application_key", missing),
            "libraryKey": kwargs.get("library_key", missing),
            "libraryNameContains": kwargs.get("library_name_contains", missing),
            "libraryName": kwargs.get("library_name", missing),
            "timeStart": kwargs.get("time_start", missing),
            "timeEnd": kwargs.get("time_end", missing),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="LibraryUsageCollection",
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
                response_type="LibraryUsageCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

        :param str hostname_contains: (optional)
            Filter the list with hostname contains the given value.

        :param str library_key: (optional)
            The library key.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.ManagedInstanceUsageCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/summarize_managed_instance_usage.py.html>`__ to see an example of how to use summarize_managed_instance_usage API.
        """
        resource_path = "/fleets/{fleetId}/actions/summarizeManagedInstanceUsage"
        method = "GET"
        operation_name = "summarize_managed_instance_usage"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/ManagedInstanceUsage/SummarizeManagedInstanceUsage"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
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
            "os_family",
            "hostname_contains",
            "library_key"
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
            "osFamily": self.base_client.generate_collection_format_param(kwargs.get("os_family", missing), 'multi'),
            "hostnameContains": kwargs.get("hostname_contains", missing),
            "libraryKey": kwargs.get("library_key", missing)
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
                response_type="ManagedInstanceUsageCollection",
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
                response_type="ManagedInstanceUsageCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def summarize_resource_inventory(self, **kwargs):
        """
        Retrieve the inventory of JMS resources in the specified compartment: a list of the number of _active_ fleets, managed instances, Java Runtimes, Java installations, and applications.


        :param str compartment_id: (optional)
            The `OCID`__ of the compartment in which to list resources.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param datetime time_start: (optional)
            The start of the time period during which resources are searched (formatted according to `RFC3339`__).

            __ https://datatracker.ietf.org/doc/html/rfc3339

        :param datetime time_end: (optional)
            The end of the time period during which resources are searched (formatted according to `RFC3339`__).

            __ https://datatracker.ietf.org/doc/html/rfc3339

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.ResourceInventory`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/summarize_resource_inventory.py.html>`__ to see an example of how to use summarize_resource_inventory API.
        """
        resource_path = "/summarizeResourceInventory"
        method = "GET"
        operation_name = "summarize_resource_inventory"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/Fleet/SummarizeResourceInventory"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "time_start",
            "time_end",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_resource_inventory got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "timeStart": kwargs.get("time_start", missing),
            "timeEnd": kwargs.get("time_end", missing)
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
                response_type="ResourceInventory",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ResourceInventory",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/update_fleet.py.html>`__ to see an example of how to use update_fleet API.
        """
        resource_path = "/fleets/{fleetId}"
        method = "PUT"
        operation_name = "update_fleet"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/Fleet/UpdateFleet"

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
                body=update_fleet_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_fleet_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_fleet_advanced_feature_configuration(self, fleet_id, update_fleet_advanced_feature_configuration_details, **kwargs):
        """
        Update advanced feature configurations for the fleet
        Ensure that the namespace and bucket storage are created prior to turning on the JfrRecording or CryptoEventAnalysis feature


        :param str fleet_id: (required)
            The `OCID`__ of the Fleet.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.jms.models.UpdateFleetAdvancedFeatureConfigurationDetails update_fleet_advanced_feature_configuration_details: (required)
            Update advanced feature configurations with new fields

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.jms.models.FleetAdvancedFeatureConfiguration`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/update_fleet_advanced_feature_configuration.py.html>`__ to see an example of how to use update_fleet_advanced_feature_configuration API.
        """
        resource_path = "/fleets/{fleetId}/advancedFeatureConfiguration"
        method = "PUT"
        operation_name = "update_fleet_advanced_feature_configuration"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/FleetAdvancedFeatureConfiguration/UpdateFleetAdvancedFeatureConfiguration"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_fleet_advanced_feature_configuration got unknown kwargs: {!r}".format(extra_kwargs))

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
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
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
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_fleet_advanced_feature_configuration_details,
                response_type="FleetAdvancedFeatureConfiguration",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_fleet_advanced_feature_configuration_details,
                response_type="FleetAdvancedFeatureConfiguration",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

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

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/jms/update_fleet_agent_configuration.py.html>`__ to see an example of how to use update_fleet_agent_configuration API.
        """
        resource_path = "/fleets/{fleetId}/agentConfiguration"
        method = "PUT"
        operation_name = "update_fleet_agent_configuration"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/jms/20210610/FleetAgentConfiguration/UpdateFleetAgentConfiguration"

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
                body=update_fleet_agent_configuration_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_fleet_agent_configuration_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
