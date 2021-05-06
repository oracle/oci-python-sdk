# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry  # noqa: F401
from oci.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel, get_signer_from_authentication_type, AUTHENTICATION_TYPE_FIELD_NAME
from .models import opsi_type_mapping
missing = Sentinel("Missing")


class OperationsInsightsClient(object):
    """
    Use the Operations Insights API to perform data extraction operations to obtain database
    resource utilization, performance statistics, and reference information. For more information,
    see [About Oracle Cloud Infrastructure Operations Insights](https://docs.cloud.oracle.com/en-us/iaas/operations-insights/doc/operations-insights.html).
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
            'service_endpoint_template': 'https://operationsinsights.{region}.oci.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False)
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        self.base_client = BaseClient("operations_insights", config, signer, opsi_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')

    def change_database_insight_compartment(self, database_insight_id, change_database_insight_compartment_details, **kwargs):
        """
        Moves a DatabaseInsight resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.


        :param str database_insight_id: (required)
            Unique database insight identifier

        :param oci.opsi.models.ChangeDatabaseInsightCompartmentDetails change_database_insight_compartment_details: (required)
            The information to be updated.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/change_database_insight_compartment.py.html>`__ to see an example of how to use change_database_insight_compartment API.
        """
        resource_path = "/databaseInsights/{databaseInsightId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_database_insight_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseInsightId": database_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_database_insight_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_database_insight_compartment_details)

    def change_enterprise_manager_bridge_compartment(self, enterprise_manager_bridge_id, change_enterprise_manager_bridge_compartment_details, **kwargs):
        """
        Moves a EnterpriseManagerBridge resource from one compartment to another. When provided, If-Match is checked against ETag values of the resource.


        :param str enterprise_manager_bridge_id: (required)
            Unique Enterprise Manager bridge identifier

        :param oci.opsi.models.ChangeEnterpriseManagerBridgeCompartmentDetails change_enterprise_manager_bridge_compartment_details: (required)
            The information to be updated.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/change_enterprise_manager_bridge_compartment.py.html>`__ to see an example of how to use change_enterprise_manager_bridge_compartment API.
        """
        resource_path = "/enterpriseManagerBridges/{enterpriseManagerBridgeId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_enterprise_manager_bridge_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "enterpriseManagerBridgeId": enterprise_manager_bridge_id
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
                body=change_enterprise_manager_bridge_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_enterprise_manager_bridge_compartment_details)

    def change_host_insight_compartment(self, host_insight_id, change_host_insight_compartment_details, **kwargs):
        """
        Moves a HostInsight resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.


        :param str host_insight_id: (required)
            Unique host insight identifier

        :param oci.opsi.models.ChangeHostInsightCompartmentDetails change_host_insight_compartment_details: (required)
            The information to be updated.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/change_host_insight_compartment.py.html>`__ to see an example of how to use change_host_insight_compartment API.
        """
        resource_path = "/hostInsights/{hostInsightId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_host_insight_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "hostInsightId": host_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_host_insight_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_host_insight_compartment_details)

    def create_database_insight(self, create_database_insight_details, **kwargs):
        """
        Create a Database Insight resource for a database in Operations Insights. The database will be enabled in Operations Insights. Database metric collection and analysis will be started.


        :param oci.opsi.models.CreateDatabaseInsightDetails create_database_insight_details: (required)
            Details for the database for which a Database Insight resource will be created in Operations Insights.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.DatabaseInsight`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/create_database_insight.py.html>`__ to see an example of how to use create_database_insight API.
        """
        resource_path = "/databaseInsights"
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
                "create_database_insight got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_database_insight_details,
                response_type="DatabaseInsight")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_database_insight_details,
                response_type="DatabaseInsight")

    def create_enterprise_manager_bridge(self, create_enterprise_manager_bridge_details, **kwargs):
        """
        Create a Enterprise Manager bridge in Operations Insights.


        :param oci.opsi.models.CreateEnterpriseManagerBridgeDetails create_enterprise_manager_bridge_details: (required)
            Details for the Enterprise Manager bridge to be created in Operations Insights.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.EnterpriseManagerBridge`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/create_enterprise_manager_bridge.py.html>`__ to see an example of how to use create_enterprise_manager_bridge API.
        """
        resource_path = "/enterpriseManagerBridges"
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
                "create_enterprise_manager_bridge got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_enterprise_manager_bridge_details,
                response_type="EnterpriseManagerBridge")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_enterprise_manager_bridge_details,
                response_type="EnterpriseManagerBridge")

    def create_host_insight(self, create_host_insight_details, **kwargs):
        """
        Create a Host Insight resource for a host in Operations Insights. The host will be enabled in Operations Insights. Host metric collection and analysis will be started.


        :param oci.opsi.models.CreateHostInsightDetails create_host_insight_details: (required)
            Details for the host for which a Host Insight resource will be created in Operations Insights.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.HostInsight`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/create_host_insight.py.html>`__ to see an example of how to use create_host_insight API.
        """
        resource_path = "/hostInsights"
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
                "create_host_insight got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_host_insight_details,
                response_type="HostInsight")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_host_insight_details,
                response_type="HostInsight")

    def delete_database_insight(self, database_insight_id, **kwargs):
        """
        Deletes a database insight. The database insight will be deleted and cannot be enabled again.


        :param str database_insight_id: (required)
            Unique database insight identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/delete_database_insight.py.html>`__ to see an example of how to use delete_database_insight API.
        """
        resource_path = "/databaseInsights/{databaseInsightId}"
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
                "delete_database_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseInsightId": database_insight_id
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

    def delete_enterprise_manager_bridge(self, enterprise_manager_bridge_id, **kwargs):
        """
        Deletes an Operations Insights Enterprise Manager bridge. If any database insight is still referencing this bridge, the operation will fail.


        :param str enterprise_manager_bridge_id: (required)
            Unique Enterprise Manager bridge identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/delete_enterprise_manager_bridge.py.html>`__ to see an example of how to use delete_enterprise_manager_bridge API.
        """
        resource_path = "/enterpriseManagerBridges/{enterpriseManagerBridgeId}"
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
                "delete_enterprise_manager_bridge got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "enterpriseManagerBridgeId": enterprise_manager_bridge_id
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

    def delete_host_insight(self, host_insight_id, **kwargs):
        """
        Deletes a host insight. The host insight will be deleted and cannot be enabled again.


        :param str host_insight_id: (required)
            Unique host insight identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/delete_host_insight.py.html>`__ to see an example of how to use delete_host_insight API.
        """
        resource_path = "/hostInsights/{hostInsightId}"
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
                "delete_host_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "hostInsightId": host_insight_id
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

    def disable_database_insight(self, database_insight_id, **kwargs):
        """
        Disables a database in Operations Insights. Database metric collection and analysis will be stopped.


        :param str database_insight_id: (required)
            Unique database insight identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/disable_database_insight.py.html>`__ to see an example of how to use disable_database_insight API.
        """
        resource_path = "/databaseInsights/{databaseInsightId}/actions/disable"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "disable_database_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseInsightId": database_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
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

    def disable_host_insight(self, host_insight_id, **kwargs):
        """
        Disables a host in Operations Insights. Host metric collection and analysis will be stopped.


        :param str host_insight_id: (required)
            Unique host insight identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/disable_host_insight.py.html>`__ to see an example of how to use disable_host_insight API.
        """
        resource_path = "/hostInsights/{hostInsightId}/actions/disable"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "disable_host_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "hostInsightId": host_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
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

    def enable_database_insight(self, enable_database_insight_details, database_insight_id, **kwargs):
        """
        Enables a database in Operations Insights. Database metric collection and analysis will be started.


        :param oci.opsi.models.EnableDatabaseInsightDetails enable_database_insight_details: (required)
            Details for the database to be enabled in Operations Insights.

        :param str database_insight_id: (required)
            Unique database insight identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/enable_database_insight.py.html>`__ to see an example of how to use enable_database_insight API.
        """
        resource_path = "/databaseInsights/{databaseInsightId}/actions/enable"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "enable_database_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseInsightId": database_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=enable_database_insight_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=enable_database_insight_details)

    def enable_host_insight(self, enable_host_insight_details, host_insight_id, **kwargs):
        """
        Enables a host in Operations Insights. Host metric collection and analysis will be started.


        :param oci.opsi.models.EnableHostInsightDetails enable_host_insight_details: (required)
            Details for the host to be enabled in Operations Insights.

        :param str host_insight_id: (required)
            Unique host insight identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/enable_host_insight.py.html>`__ to see an example of how to use enable_host_insight API.
        """
        resource_path = "/hostInsights/{hostInsightId}/actions/enable"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "enable_host_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "hostInsightId": host_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=enable_host_insight_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=enable_host_insight_details)

    def get_database_insight(self, database_insight_id, **kwargs):
        """
        Gets details of a database insight.


        :param str database_insight_id: (required)
            Unique database insight identifier

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.DatabaseInsight`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/get_database_insight.py.html>`__ to see an example of how to use get_database_insight API.
        """
        resource_path = "/databaseInsights/{databaseInsightId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_database_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseInsightId": database_insight_id
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
                response_type="DatabaseInsight")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DatabaseInsight")

    def get_enterprise_manager_bridge(self, enterprise_manager_bridge_id, **kwargs):
        """
        Gets details of an Operations Insights Enterprise Manager bridge.


        :param str enterprise_manager_bridge_id: (required)
            Unique Enterprise Manager bridge identifier

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.EnterpriseManagerBridge`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/get_enterprise_manager_bridge.py.html>`__ to see an example of how to use get_enterprise_manager_bridge API.
        """
        resource_path = "/enterpriseManagerBridges/{enterpriseManagerBridgeId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_enterprise_manager_bridge got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "enterpriseManagerBridgeId": enterprise_manager_bridge_id
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
                response_type="EnterpriseManagerBridge")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="EnterpriseManagerBridge")

    def get_host_insight(self, host_insight_id, **kwargs):
        """
        Gets details of a host insight.


        :param str host_insight_id: (required)
            Unique host insight identifier

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.HostInsight`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/get_host_insight.py.html>`__ to see an example of how to use get_host_insight API.
        """
        resource_path = "/hostInsights/{hostInsightId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_host_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "hostInsightId": host_insight_id
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
                response_type="HostInsight")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="HostInsight")

    def get_work_request(self, work_request_id, **kwargs):
        """
        Gets the status of the work request with the given ID.


        :param str work_request_id: (required)
            The ID of the asynchronous request.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.WorkRequest`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/get_work_request.py.html>`__ to see an example of how to use get_work_request API.
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

    def ingest_database_configuration(self, ingest_database_configuration_details, **kwargs):
        """
        This is a generic ingest endpoint for all database configuration metrics.


        :param oci.opsi.models.IngestDatabaseConfigurationDetails ingest_database_configuration_details: (required)
            Payload for one or more database configuration metrics for a particular database.

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.IngestDatabaseConfigurationResponseDetails`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/ingest_database_configuration.py.html>`__ to see an example of how to use ingest_database_configuration API.
        """
        resource_path = "/databaseInsights/actions/ingestDatabaseConfiguration"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "database_id",
            "id",
            "opc_request_id",
            "if_match",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "ingest_database_configuration got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_database_configuration_details,
                response_type="IngestDatabaseConfigurationResponseDetails")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_database_configuration_details,
                response_type="IngestDatabaseConfigurationResponseDetails")

    def ingest_host_configuration(self, id, ingest_host_configuration_details, **kwargs):
        """
        This is a generic ingest endpoint for all the host configuration metrics


        :param str id: (required)
            Required `OCID`__ of the host insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.opsi.models.IngestHostConfigurationDetails ingest_host_configuration_details: (required)
            Payload for one or more host configuration metrics for a particular host.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.IngestHostConfigurationResponseDetails`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/ingest_host_configuration.py.html>`__ to see an example of how to use ingest_host_configuration API.
        """
        resource_path = "/hostInsights/actions/ingestHostConfiguration"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "if_match",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "ingest_host_configuration got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "id": id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_host_configuration_details,
                response_type="IngestHostConfigurationResponseDetails")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_host_configuration_details,
                response_type="IngestHostConfigurationResponseDetails")

    def ingest_host_metrics(self, id, ingest_host_metrics_details, **kwargs):
        """
        This is a generic ingest endpoint for all the host performance metrics


        :param str id: (required)
            Required `OCID`__ of the host insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.opsi.models.IngestHostMetricsDetails ingest_host_metrics_details: (required)
            Payload for one or more host performance metrics for a particular host.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.IngestHostMetricsResponseDetails`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/ingest_host_metrics.py.html>`__ to see an example of how to use ingest_host_metrics API.
        """
        resource_path = "/hostInsights/actions/ingestHostMetrics"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "if_match",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "ingest_host_metrics got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "id": id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_host_metrics_details,
                response_type="IngestHostMetricsResponseDetails")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_host_metrics_details,
                response_type="IngestHostMetricsResponseDetails")

    def ingest_sql_bucket(self, ingest_sql_bucket_details, **kwargs):
        """
        The sqlbucket endpoint takes in a JSON payload, persists it in Operations Insights ingest pipeline.
        Either databaseId or id must be specified.


        :param oci.opsi.models.IngestSqlBucketDetails ingest_sql_bucket_details: (required)
            Collection of SQL bucket objects for a particular database.

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.IngestSqlBucketResponseDetails`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/ingest_sql_bucket.py.html>`__ to see an example of how to use ingest_sql_bucket API.
        """
        resource_path = "/databaseInsights/actions/ingestSqlBucket"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "compartment_id",
            "database_id",
            "id",
            "opc_request_id",
            "if_match",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "ingest_sql_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_sql_bucket_details,
                response_type="IngestSqlBucketResponseDetails")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_sql_bucket_details,
                response_type="IngestSqlBucketResponseDetails")

    def ingest_sql_plan_lines(self, ingest_sql_plan_lines_details, **kwargs):
        """
        The SqlPlanLines endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline.
        Either databaseId or id must be specified.


        :param oci.opsi.models.IngestSqlPlanLinesDetails ingest_sql_plan_lines_details: (required)
            Collection of SQL plan line objects for a particular database.

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.IngestSqlPlanLinesResponseDetails`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/ingest_sql_plan_lines.py.html>`__ to see an example of how to use ingest_sql_plan_lines API.
        """
        resource_path = "/databaseInsights/actions/ingestSqlPlanLines"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "compartment_id",
            "database_id",
            "id",
            "opc_request_id",
            "if_match",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "ingest_sql_plan_lines got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_sql_plan_lines_details,
                response_type="IngestSqlPlanLinesResponseDetails")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_sql_plan_lines_details,
                response_type="IngestSqlPlanLinesResponseDetails")

    def ingest_sql_text(self, ingest_sql_text_details, **kwargs):
        """
        The SqlText endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline.
        Either databaseId or id must be specified.
        Disclaimer: SQL text being uploaded explicitly via APIs is not masked. Any sensitive literals contained in the sqlFullText column should be masked prior to ingestion.


        :param oci.opsi.models.IngestSqlTextDetails ingest_sql_text_details: (required)
            Collection of SQL text objects for a particular database.

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.IngestSqlTextResponseDetails`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/ingest_sql_text.py.html>`__ to see an example of how to use ingest_sql_text API.
        """
        resource_path = "/databaseInsights/actions/ingestSqlText"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "compartment_id",
            "database_id",
            "id",
            "opc_request_id",
            "if_match",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "ingest_sql_text got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_sql_text_details,
                response_type="IngestSqlTextResponseDetails")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_sql_text_details,
                response_type="IngestSqlTextResponseDetails")

    def list_database_insights(self, **kwargs):
        """
        Gets a list of database insights based on the query parameters specified. Either compartmentId or id query parameter must be specified.


        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str enterprise_manager_bridge_id: (optional)
            Unique Enterprise Manager bridge identifier

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] status: (optional)
            Resource Status

            Allowed values are: "DISABLED", "ENABLED", "TERMINATED"

        :param list[str] lifecycle_state: (optional)
            Lifecycle states

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] fields: (optional)
            Specifies the fields to return in a database summary response. By default all fields are returned if omitted.

            Allowed values are: "compartmentId", "databaseName", "databaseDisplayName", "databaseType", "databaseVersion", "databaseHostNames", "freeformTags", "definedTags"

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Database insight list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.

            Allowed values are: "databaseName", "databaseDisplayName", "databaseType"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.DatabaseInsightsCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_database_insights.py.html>`__ to see an example of how to use list_database_insights API.
        """
        resource_path = "/databaseInsights"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "compartment_id",
            "enterprise_manager_bridge_id",
            "id",
            "status",
            "lifecycle_state",
            "database_type",
            "database_id",
            "fields",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_database_insights got unknown kwargs: {!r}".format(extra_kwargs))

        if 'status' in kwargs:
            status_allowed_values = ["DISABLED", "ENABLED", "TERMINATED"]
            for status_item in kwargs['status']:
                if status_item not in status_allowed_values:
                    raise ValueError(
                        "Invalid value for `status`, must be one of {0}".format(status_allowed_values)
                    )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
            for lifecycle_state_item in kwargs['lifecycle_state']:
                if lifecycle_state_item not in lifecycle_state_allowed_values:
                    raise ValueError(
                        "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                    )

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        if 'fields' in kwargs:
            fields_allowed_values = ["compartmentId", "databaseName", "databaseDisplayName", "databaseType", "databaseVersion", "databaseHostNames", "freeformTags", "definedTags"]
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
            sort_by_allowed_values = ["databaseName", "databaseDisplayName", "databaseType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "enterpriseManagerBridgeId": kwargs.get("enterprise_manager_bridge_id", missing),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "status": self.base_client.generate_collection_format_param(kwargs.get("status", missing), 'multi'),
            "lifecycleState": self.base_client.generate_collection_format_param(kwargs.get("lifecycle_state", missing), 'multi'),
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
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
                response_type="DatabaseInsightsCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="DatabaseInsightsCollection")

    def list_enterprise_manager_bridges(self, **kwargs):
        """
        Gets a list of Operations Insights Enterprise Manager bridges. Either compartmentId or id must be specified.


        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str display_name: (optional)
            A filter to return only resources that match the entire display name.

        :param str id: (optional)
            Unique Enterprise Manager bridge identifier

        :param list[str] lifecycle_state: (optional)
            Lifecycle states

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

            Allowed values are: "timeCreated", "displayName"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.EnterpriseManagerBridgeCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_enterprise_manager_bridges.py.html>`__ to see an example of how to use list_enterprise_manager_bridges API.
        """
        resource_path = "/enterpriseManagerBridges"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "compartment_id",
            "display_name",
            "id",
            "lifecycle_state",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_enterprise_manager_bridges got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
            for lifecycle_state_item in kwargs['lifecycle_state']:
                if lifecycle_state_item not in lifecycle_state_allowed_values:
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
            "compartmentId": kwargs.get("compartment_id", missing),
            "displayName": kwargs.get("display_name", missing),
            "id": kwargs.get("id", missing),
            "lifecycleState": self.base_client.generate_collection_format_param(kwargs.get("lifecycle_state", missing), 'multi'),
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
                response_type="EnterpriseManagerBridgeCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="EnterpriseManagerBridgeCollection")

    def list_host_insights(self, **kwargs):
        """
        Gets a list of host insights based on the query parameters specified. Either compartmentId or id query parameter must be specified.


        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of host insight resource `OCIDs`__ of the host insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] status: (optional)
            Resource Status

            Allowed values are: "DISABLED", "ENABLED", "TERMINATED"

        :param list[str] lifecycle_state: (optional)
            Lifecycle states

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"

        :param list[str] host_type: (optional)
            Filter by one or more host types.
            Possible value is EXTERNAL-HOST.

        :param list[str] platform_type: (optional)
            Filter by one or more platform types.
            Possible value is LINUX.

            Allowed values are: "LINUX"

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Host insight list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.

            Allowed values are: "hostName", "hostType"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.HostInsightSummaryCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_host_insights.py.html>`__ to see an example of how to use list_host_insights API.
        """
        resource_path = "/hostInsights"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "compartment_id",
            "id",
            "status",
            "lifecycle_state",
            "host_type",
            "platform_type",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_host_insights got unknown kwargs: {!r}".format(extra_kwargs))

        if 'status' in kwargs:
            status_allowed_values = ["DISABLED", "ENABLED", "TERMINATED"]
            for status_item in kwargs['status']:
                if status_item not in status_allowed_values:
                    raise ValueError(
                        "Invalid value for `status`, must be one of {0}".format(status_allowed_values)
                    )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
            for lifecycle_state_item in kwargs['lifecycle_state']:
                if lifecycle_state_item not in lifecycle_state_allowed_values:
                    raise ValueError(
                        "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                    )

        if 'platform_type' in kwargs:
            platform_type_allowed_values = ["LINUX"]
            for platform_type_item in kwargs['platform_type']:
                if platform_type_item not in platform_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `platform_type`, must be one of {0}".format(platform_type_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["hostName", "hostType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "status": self.base_client.generate_collection_format_param(kwargs.get("status", missing), 'multi'),
            "lifecycleState": self.base_client.generate_collection_format_param(kwargs.get("lifecycle_state", missing), 'multi'),
            "hostType": self.base_client.generate_collection_format_param(kwargs.get("host_type", missing), 'multi'),
            "platformType": self.base_client.generate_collection_format_param(kwargs.get("platform_type", missing), 'multi'),
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
                response_type="HostInsightSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="HostInsightSummaryCollection")

    def list_hosted_entities(self, compartment_id, id, **kwargs):
        """
        Get a list of hosted entities details.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (required)
            Required `OCID`__ of the host insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] platform_type: (optional)
            Filter by one or more platform types.
            Possible value is LINUX.

            Allowed values are: "LINUX"

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Hosted entity list sort options.

            Allowed values are: "entityName", "entityType"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.HostedEntityCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_hosted_entities.py.html>`__ to see an example of how to use list_hosted_entities API.
        """
        resource_path = "/hostInsights/hostedEntities"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "platform_type",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_hosted_entities got unknown kwargs: {!r}".format(extra_kwargs))

        if 'platform_type' in kwargs:
            platform_type_allowed_values = ["LINUX"]
            for platform_type_item in kwargs['platform_type']:
                if platform_type_item not in platform_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `platform_type`, must be one of {0}".format(platform_type_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["entityName", "entityType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "platformType": self.base_client.generate_collection_format_param(kwargs.get("platform_type", missing), 'multi'),
            "id": id,
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
                response_type="HostedEntityCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="HostedEntityCollection")

    def list_importable_enterprise_manager_entities(self, enterprise_manager_bridge_id, **kwargs):
        """
        Gets a list of importable entities for an Operations Insights Enterprise Manager bridge that have not been imported before.


        :param str enterprise_manager_bridge_id: (required)
            Unique Enterprise Manager bridge identifier

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.ImportableEnterpriseManagerEntityCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_importable_enterprise_manager_entities.py.html>`__ to see an example of how to use list_importable_enterprise_manager_entities API.
        """
        resource_path = "/enterpriseManagerBridges/{enterpriseManagerBridgeId}/importableEnterpriseManagerEntities"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_importable_enterprise_manager_entities got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "enterpriseManagerBridgeId": enterprise_manager_bridge_id
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
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="ImportableEnterpriseManagerEntityCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ImportableEnterpriseManagerEntityCollection")

    def list_sql_plans(self, compartment_id, sql_identifier, plan_hash, **kwargs):
        """
        Query SQL Warehouse to list the plan xml for a given SQL execution plan. This returns a SqlPlanCollection object, but is currently limited to a single plan.
        Either databaseId or id must be specified.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str sql_identifier: (required)
            Unique SQL_ID for a SQL Statement.
            Example: `6rgjh9bjmy2s7`

        :param oci.opsi.models.list[int] plan_hash: (required)
            Unique plan hash for a SQL Plan of a particular SQL Statement.
            Example: `9820154385`

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlPlanCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_sql_plans.py.html>`__ to see an example of how to use list_sql_plans API.
        """
        resource_path = "/databaseInsights/sqlPlans"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "database_id",
            "id",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_sql_plans got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing),
            "sqlIdentifier": sql_identifier,
            "planHash": self.base_client.generate_collection_format_param(plan_hash, 'multi'),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="SqlPlanCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlPlanCollection")

    def list_sql_searches(self, compartment_id, sql_identifier, **kwargs):
        """
        Search SQL by SQL Identifier across databases and get the SQL Text and the details of the databases executing the SQL for a given time period.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str sql_identifier: (required)
            Unique SQL_ID for a SQL Statement.
            Example: `6rgjh9bjmy2s7`

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlSearchCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_sql_searches.py.html>`__ to see an example of how to use list_sql_searches API.
        """
        resource_path = "/databaseInsights/sqlSearches"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_sql_searches got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "sqlIdentifier": sql_identifier,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="SqlSearchCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlSearchCollection")

    def list_sql_texts(self, compartment_id, sql_identifier, **kwargs):
        """
        Query SQL Warehouse to get the full SQL Text for a SQL.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.opsi.models.list[str] sql_identifier: (required)
            One or more unique SQL_IDs for a SQL Statement.
            Example: `6rgjh9bjmy2s7`

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the assosicated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database `OCIDs`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlTextCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_sql_texts.py.html>`__ to see an example of how to use list_sql_texts API.
        """
        resource_path = "/databaseInsights/sqlTexts"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "database_id",
            "id",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_sql_texts got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "sqlIdentifier": self.base_client.generate_collection_format_param(sql_identifier, 'multi'),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="SqlTextCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlTextCollection")

    def list_work_request_errors(self, work_request_id, **kwargs):
        """
        Return a (paginated) list of errors for a given work request.


        :param str work_request_id: (required)
            The ID of the asynchronous request.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.WorkRequestErrorCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_work_request_errors.py.html>`__ to see an example of how to use list_work_request_errors API.
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
        Return a (paginated) list of logs for a given work request.


        :param str work_request_id: (required)
            The ID of the asynchronous request.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.WorkRequestLogEntryCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_work_request_logs.py.html>`__ to see an example of how to use list_work_request_logs API.
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
                response_type="WorkRequestLogEntryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="WorkRequestLogEntryCollection")

    def list_work_requests(self, compartment_id, **kwargs):
        """
        Lists the work requests in a compartment.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.WorkRequestCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_work_requests.py.html>`__ to see an example of how to use list_work_requests API.
        """
        resource_path = "/workRequests"
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
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="WorkRequestCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="WorkRequestCollection")

    def summarize_database_insight_resource_capacity_trend(self, compartment_id, resource_metric, **kwargs):
        """
        Returns response with time series data (endTimestamp, capacity, baseCapacity) for the time period specified.
        The maximum time range for analysis is 2 years, hence this is intentionally not paginated.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY and IO.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str utilization_level: (optional)
            Filter by utilization level by the following buckets:
              - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.
              - LOW_UTILIZATION: DBs with utilization lower than 25.
              - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.
              - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.

            Allowed values are: "HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sorts using end timestamp , capacity or baseCapacity

            Allowed values are: "endTimestamp", "capacity", "baseCapacity"

        :param str tablespace_name: (optional)
            Tablespace name for a database

        :param list[str] host_name: (optional)
            Filter by one or more hostname.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_database_insight_resource_capacity_trend.py.html>`__ to see an example of how to use summarize_database_insight_resource_capacity_trend API.
        """
        resource_path = "/databaseInsights/resourceCapacityTrend"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_type",
            "database_id",
            "id",
            "utilization_level",
            "page",
            "sort_order",
            "sort_by",
            "tablespace_name",
            "host_name",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_database_insight_resource_capacity_trend got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        if 'utilization_level' in kwargs:
            utilization_level_allowed_values = ["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]
            if kwargs['utilization_level'] not in utilization_level_allowed_values:
                raise ValueError(
                    "Invalid value for `utilization_level`, must be one of {0}".format(utilization_level_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["endTimestamp", "capacity", "baseCapacity"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "utilizationLevel": kwargs.get("utilization_level", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "tablespaceName": kwargs.get("tablespace_name", missing),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi')
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection")

    def summarize_database_insight_resource_forecast_trend(self, compartment_id, resource_metric, **kwargs):
        """
        Get Forecast predictions for CPU and Storage resources since a time in the past.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY and IO.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str statistic: (optional)
            Choose the type of statistic metric data to be used for forecasting.

            Allowed values are: "AVG", "MAX"

        :param int forecast_days: (optional)
            Number of days used for utilization forecast analysis.

        :param str forecast_model: (optional)
            Choose algorithm model for the forecasting.
            Possible values:
              - LINEAR: Uses linear regression algorithm for forecasting.
              - ML_AUTO: Automatically detects best algorithm to use for forecasting.
              - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm.

            Allowed values are: "LINEAR", "ML_AUTO", "ML_NO_AUTO"

        :param str utilization_level: (optional)
            Filter by utilization level by the following buckets:
              - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.
              - LOW_UTILIZATION: DBs with utilization lower than 25.
              - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.
              - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.

            Allowed values are: "HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"

        :param int confidence: (optional)
            This parameter is used to change data's confidence level, this data is ingested by the
            forecast algorithm.
            Confidence is the probability of an interval to contain the expected population parameter.
            Manipulation of this value will lead to different results.
            If not set, default confidence value is 95%.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param list[str] host_name: (optional)
            Filter by one or more hostname.

        :param str tablespace_name: (optional)
            Tablespace name for a database

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceForecastTrendAggregation`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_database_insight_resource_forecast_trend.py.html>`__ to see an example of how to use summarize_database_insight_resource_forecast_trend API.
        """
        resource_path = "/databaseInsights/resourceForecastTrend"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_type",
            "database_id",
            "id",
            "statistic",
            "forecast_days",
            "forecast_model",
            "utilization_level",
            "confidence",
            "page",
            "host_name",
            "tablespace_name",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_database_insight_resource_forecast_trend got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        if 'statistic' in kwargs:
            statistic_allowed_values = ["AVG", "MAX"]
            if kwargs['statistic'] not in statistic_allowed_values:
                raise ValueError(
                    "Invalid value for `statistic`, must be one of {0}".format(statistic_allowed_values)
                )

        if 'forecast_model' in kwargs:
            forecast_model_allowed_values = ["LINEAR", "ML_AUTO", "ML_NO_AUTO"]
            if kwargs['forecast_model'] not in forecast_model_allowed_values:
                raise ValueError(
                    "Invalid value for `forecast_model`, must be one of {0}".format(forecast_model_allowed_values)
                )

        if 'utilization_level' in kwargs:
            utilization_level_allowed_values = ["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]
            if kwargs['utilization_level'] not in utilization_level_allowed_values:
                raise ValueError(
                    "Invalid value for `utilization_level`, must be one of {0}".format(utilization_level_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "statistic": kwargs.get("statistic", missing),
            "forecastDays": kwargs.get("forecast_days", missing),
            "forecastModel": kwargs.get("forecast_model", missing),
            "utilizationLevel": kwargs.get("utilization_level", missing),
            "confidence": kwargs.get("confidence", missing),
            "page": kwargs.get("page", missing),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "tablespaceName": kwargs.get("tablespace_name", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="SummarizeDatabaseInsightResourceForecastTrendAggregation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceForecastTrendAggregation")

    def summarize_database_insight_resource_statistics(self, compartment_id, resource_metric, **kwargs):
        """
        Lists the Resource statistics (usage,capacity, usage change percent, utilization percent, base capacity, isAutoScalingEnabled) for each database filtered by utilization level


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY and IO.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param int percentile: (optional)
            Percentile values of daily usage to be used for computing the aggregate resource usage.

        :param str insight_by: (optional)
            Return data of a specific insight
            Possible values are High Utilization, Low Utilization, Any ,High Utilization Forecast,
            Low Utilization Forecast

        :param int forecast_days: (optional)
            Number of days used for utilization forecast analysis.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The order in which resource statistics records are listed

            Allowed values are: "utilizationPercent", "usage", "usageChangePercent", "databaseName", "databaseType"

        :param list[str] host_name: (optional)
            Filter by one or more hostname.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceStatisticsAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_database_insight_resource_statistics.py.html>`__ to see an example of how to use summarize_database_insight_resource_statistics API.
        """
        resource_path = "/databaseInsights/resourceStatistics"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_type",
            "database_id",
            "id",
            "percentile",
            "insight_by",
            "forecast_days",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "host_name",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_database_insight_resource_statistics got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["utilizationPercent", "usage", "usageChangePercent", "databaseName", "databaseType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "percentile": kwargs.get("percentile", missing),
            "insightBy": kwargs.get("insight_by", missing),
            "forecastDays": kwargs.get("forecast_days", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi')
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="SummarizeDatabaseInsightResourceStatisticsAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceStatisticsAggregationCollection")

    def summarize_database_insight_resource_usage(self, compartment_id, resource_metric, **kwargs):
        """
        A cumulative distribution function is used to rank the usage data points per database within the specified time period.
        For each database, the minimum data point with a ranking > the percentile value is included in the summation.
        Linear regression functions are used to calculate the usage change percentage.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY and IO.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param int percentile: (optional)
            Percentile values of daily usage to be used for computing the aggregate resource usage.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceUsageAggregation`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_database_insight_resource_usage.py.html>`__ to see an example of how to use summarize_database_insight_resource_usage API.
        """
        resource_path = "/databaseInsights/resourceUsageSummary"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_type",
            "database_id",
            "id",
            "page",
            "percentile",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_database_insight_resource_usage got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "page": kwargs.get("page", missing),
            "percentile": kwargs.get("percentile", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="SummarizeDatabaseInsightResourceUsageAggregation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceUsageAggregation")

    def summarize_database_insight_resource_usage_trend(self, compartment_id, resource_metric, **kwargs):
        """
        Returns response with time series data (endTimestamp, usage, capacity) for the time period specified.
        The maximum time range for analysis is 2 years, hence this is intentionally not paginated.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY and IO.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sorts using end timestamp, usage or capacity

            Allowed values are: "endTimestamp", "usage", "capacity"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceUsageTrendAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_database_insight_resource_usage_trend.py.html>`__ to see an example of how to use summarize_database_insight_resource_usage_trend API.
        """
        resource_path = "/databaseInsights/resourceUsageTrend"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_type",
            "database_id",
            "id",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_database_insight_resource_usage_trend got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["endTimestamp", "usage", "capacity"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
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
                response_type="SummarizeDatabaseInsightResourceUsageTrendAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceUsageTrendAggregationCollection")

    def summarize_database_insight_resource_utilization_insight(self, compartment_id, resource_metric, **kwargs):
        """
        Gets resources with current utilization (high and low) and projected utilization (high and low) for a resource type over specified time period.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY and IO.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param int forecast_days: (optional)
            Number of days used for utilization forecast analysis.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceUtilizationInsightAggregation`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_database_insight_resource_utilization_insight.py.html>`__ to see an example of how to use summarize_database_insight_resource_utilization_insight API.
        """
        resource_path = "/databaseInsights/resourceUtilizationInsight"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_type",
            "database_id",
            "id",
            "forecast_days",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_database_insight_resource_utilization_insight got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "forecastDays": kwargs.get("forecast_days", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="SummarizeDatabaseInsightResourceUtilizationInsightAggregation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceUtilizationInsightAggregation")

    def summarize_database_insight_tablespace_usage_trend(self, compartment_id, **kwargs):
        """
        Returns response with usage time series data (endTimestamp, usage, capacity) with breakdown by tablespaceName for the time period specified.
        The maximum time range for analysis is 2 years, hence this is intentionally not paginated.
        Either databaseId or id must be specified.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_database_insight_tablespace_usage_trend.py.html>`__ to see an example of how to use summarize_database_insight_tablespace_usage_trend API.
        """
        resource_path = "/databaseInsights/tablespaceUsageTrend"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_id",
            "id",
            "page",
            "limit",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_database_insight_tablespace_usage_trend got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "databaseId": kwargs.get("database_id", missing),
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
                response_type="SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection")

    def summarize_host_insight_resource_capacity_trend(self, compartment_id, resource_metric, **kwargs):
        """
        Returns response with time series data (endTimestamp, capacity) for the time period specified.
        The maximum time range for analysis is 2 years, hence this is intentionally not paginated.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by host resource metric.
            Supported values are CPU, MEMORY, and LOGICAL_MEMORY.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] platform_type: (optional)
            Filter by one or more platform types.
            Possible value is LINUX.

            Allowed values are: "LINUX"

        :param list[str] id: (optional)
            Optional list of host insight resource `OCIDs`__ of the host insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str utilization_level: (optional)
            Filter by utilization level by the following buckets:
              - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.
              - LOW_UTILIZATION: DBs with utilization lower than 25.
              - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.
              - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.

            Allowed values are: "HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sorts using end timestamp or capacity

            Allowed values are: "endTimestamp", "capacity"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeHostInsightResourceCapacityTrendAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_host_insight_resource_capacity_trend.py.html>`__ to see an example of how to use summarize_host_insight_resource_capacity_trend API.
        """
        resource_path = "/hostInsights/resourceCapacityTrend"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "platform_type",
            "id",
            "utilization_level",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_host_insight_resource_capacity_trend got unknown kwargs: {!r}".format(extra_kwargs))

        if 'platform_type' in kwargs:
            platform_type_allowed_values = ["LINUX"]
            for platform_type_item in kwargs['platform_type']:
                if platform_type_item not in platform_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `platform_type`, must be one of {0}".format(platform_type_allowed_values)
                    )

        if 'utilization_level' in kwargs:
            utilization_level_allowed_values = ["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]
            if kwargs['utilization_level'] not in utilization_level_allowed_values:
                raise ValueError(
                    "Invalid value for `utilization_level`, must be one of {0}".format(utilization_level_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["endTimestamp", "capacity"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "platformType": self.base_client.generate_collection_format_param(kwargs.get("platform_type", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "utilizationLevel": kwargs.get("utilization_level", missing),
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
                response_type="SummarizeHostInsightResourceCapacityTrendAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceCapacityTrendAggregationCollection")

    def summarize_host_insight_resource_forecast_trend(self, compartment_id, resource_metric, **kwargs):
        """
        Get Forecast predictions for CPU or memory resources since a time in the past.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by host resource metric.
            Supported values are CPU, MEMORY, and LOGICAL_MEMORY.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] platform_type: (optional)
            Filter by one or more platform types.
            Possible value is LINUX.

            Allowed values are: "LINUX"

        :param list[str] id: (optional)
            Optional list of host insight resource `OCIDs`__ of the host insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str statistic: (optional)
            Choose the type of statistic metric data to be used for forecasting.

            Allowed values are: "AVG", "MAX"

        :param int forecast_days: (optional)
            Number of days used for utilization forecast analysis.

        :param str forecast_model: (optional)
            Choose algorithm model for the forecasting.
            Possible values:
              - LINEAR: Uses linear regression algorithm for forecasting.
              - ML_AUTO: Automatically detects best algorithm to use for forecasting.
              - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm.

            Allowed values are: "LINEAR", "ML_AUTO", "ML_NO_AUTO"

        :param str utilization_level: (optional)
            Filter by utilization level by the following buckets:
              - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.
              - LOW_UTILIZATION: DBs with utilization lower than 25.
              - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.
              - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.

            Allowed values are: "HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"

        :param int confidence: (optional)
            This parameter is used to change data's confidence level, this data is ingested by the
            forecast algorithm.
            Confidence is the probability of an interval to contain the expected population parameter.
            Manipulation of this value will lead to different results.
            If not set, default confidence value is 95%.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeHostInsightResourceForecastTrendAggregation`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_host_insight_resource_forecast_trend.py.html>`__ to see an example of how to use summarize_host_insight_resource_forecast_trend API.
        """
        resource_path = "/hostInsights/resourceForecastTrend"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "platform_type",
            "id",
            "statistic",
            "forecast_days",
            "forecast_model",
            "utilization_level",
            "confidence",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_host_insight_resource_forecast_trend got unknown kwargs: {!r}".format(extra_kwargs))

        if 'platform_type' in kwargs:
            platform_type_allowed_values = ["LINUX"]
            for platform_type_item in kwargs['platform_type']:
                if platform_type_item not in platform_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `platform_type`, must be one of {0}".format(platform_type_allowed_values)
                    )

        if 'statistic' in kwargs:
            statistic_allowed_values = ["AVG", "MAX"]
            if kwargs['statistic'] not in statistic_allowed_values:
                raise ValueError(
                    "Invalid value for `statistic`, must be one of {0}".format(statistic_allowed_values)
                )

        if 'forecast_model' in kwargs:
            forecast_model_allowed_values = ["LINEAR", "ML_AUTO", "ML_NO_AUTO"]
            if kwargs['forecast_model'] not in forecast_model_allowed_values:
                raise ValueError(
                    "Invalid value for `forecast_model`, must be one of {0}".format(forecast_model_allowed_values)
                )

        if 'utilization_level' in kwargs:
            utilization_level_allowed_values = ["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]
            if kwargs['utilization_level'] not in utilization_level_allowed_values:
                raise ValueError(
                    "Invalid value for `utilization_level`, must be one of {0}".format(utilization_level_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "platformType": self.base_client.generate_collection_format_param(kwargs.get("platform_type", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "statistic": kwargs.get("statistic", missing),
            "forecastDays": kwargs.get("forecast_days", missing),
            "forecastModel": kwargs.get("forecast_model", missing),
            "utilizationLevel": kwargs.get("utilization_level", missing),
            "confidence": kwargs.get("confidence", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="SummarizeHostInsightResourceForecastTrendAggregation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceForecastTrendAggregation")

    def summarize_host_insight_resource_statistics(self, compartment_id, resource_metric, **kwargs):
        """
        Lists the resource statistics (usage, capacity, usage change percent, utilization percent, load) for each host filtered
        by utilization level.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by host resource metric.
            Supported values are CPU, MEMORY, and LOGICAL_MEMORY.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] platform_type: (optional)
            Filter by one or more platform types.
            Possible value is LINUX.

            Allowed values are: "LINUX"

        :param list[str] id: (optional)
            Optional list of host insight resource `OCIDs`__ of the host insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param int percentile: (optional)
            Percentile values of daily usage to be used for computing the aggregate resource usage.

        :param str insight_by: (optional)
            Return data of a specific insight
            Possible values are High Utilization, Low Utilization, Any ,High Utilization Forecast,
            Low Utilization Forecast

        :param int forecast_days: (optional)
            Number of days used for utilization forecast analysis.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The order in which resource statistics records are listed.

            Allowed values are: "utilizationPercent", "usage", "usageChangePercent", "hostName", "platformType"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeHostInsightResourceStatisticsAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_host_insight_resource_statistics.py.html>`__ to see an example of how to use summarize_host_insight_resource_statistics API.
        """
        resource_path = "/hostInsights/resourceStatistics"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "platform_type",
            "id",
            "percentile",
            "insight_by",
            "forecast_days",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_host_insight_resource_statistics got unknown kwargs: {!r}".format(extra_kwargs))

        if 'platform_type' in kwargs:
            platform_type_allowed_values = ["LINUX"]
            for platform_type_item in kwargs['platform_type']:
                if platform_type_item not in platform_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `platform_type`, must be one of {0}".format(platform_type_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["utilizationPercent", "usage", "usageChangePercent", "hostName", "platformType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "platformType": self.base_client.generate_collection_format_param(kwargs.get("platform_type", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "percentile": kwargs.get("percentile", missing),
            "insightBy": kwargs.get("insight_by", missing),
            "forecastDays": kwargs.get("forecast_days", missing),
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
                response_type="SummarizeHostInsightResourceStatisticsAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceStatisticsAggregationCollection")

    def summarize_host_insight_resource_usage(self, compartment_id, resource_metric, **kwargs):
        """
        A cumulative distribution function is used to rank the usage data points per host within the specified time period.
        For each host, the minimum data point with a ranking > the percentile value is included in the summation.
        Linear regression functions are used to calculate the usage change percentage.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by host resource metric.
            Supported values are CPU, MEMORY, and LOGICAL_MEMORY.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] platform_type: (optional)
            Filter by one or more platform types.
            Possible value is LINUX.

            Allowed values are: "LINUX"

        :param list[str] id: (optional)
            Optional list of host insight resource `OCIDs`__ of the host insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param int percentile: (optional)
            Percentile values of daily usage to be used for computing the aggregate resource usage.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeHostInsightResourceUsageAggregation`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_host_insight_resource_usage.py.html>`__ to see an example of how to use summarize_host_insight_resource_usage API.
        """
        resource_path = "/hostInsights/resourceUsageSummary"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "platform_type",
            "id",
            "page",
            "percentile",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_host_insight_resource_usage got unknown kwargs: {!r}".format(extra_kwargs))

        if 'platform_type' in kwargs:
            platform_type_allowed_values = ["LINUX"]
            for platform_type_item in kwargs['platform_type']:
                if platform_type_item not in platform_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `platform_type`, must be one of {0}".format(platform_type_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "platformType": self.base_client.generate_collection_format_param(kwargs.get("platform_type", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "page": kwargs.get("page", missing),
            "percentile": kwargs.get("percentile", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="SummarizeHostInsightResourceUsageAggregation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceUsageAggregation")

    def summarize_host_insight_resource_usage_trend(self, compartment_id, resource_metric, **kwargs):
        """
        Returns response with time series data (endTimestamp, usage, capacity) for the time period specified.
        The maximum time range for analysis is 2 years, hence this is intentionally not paginated.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by host resource metric.
            Supported values are CPU, MEMORY, and LOGICAL_MEMORY.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] platform_type: (optional)
            Filter by one or more platform types.
            Possible value is LINUX.

            Allowed values are: "LINUX"

        :param list[str] id: (optional)
            Optional list of host insight resource `OCIDs`__ of the host insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sorts using end timestamp, usage or capacity

            Allowed values are: "endTimestamp", "usage", "capacity"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeHostInsightResourceUsageTrendAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_host_insight_resource_usage_trend.py.html>`__ to see an example of how to use summarize_host_insight_resource_usage_trend API.
        """
        resource_path = "/hostInsights/resourceUsageTrend"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "platform_type",
            "id",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_host_insight_resource_usage_trend got unknown kwargs: {!r}".format(extra_kwargs))

        if 'platform_type' in kwargs:
            platform_type_allowed_values = ["LINUX"]
            for platform_type_item in kwargs['platform_type']:
                if platform_type_item not in platform_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `platform_type`, must be one of {0}".format(platform_type_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["endTimestamp", "usage", "capacity"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "platformType": self.base_client.generate_collection_format_param(kwargs.get("platform_type", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
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
                response_type="SummarizeHostInsightResourceUsageTrendAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceUsageTrendAggregationCollection")

    def summarize_host_insight_resource_utilization_insight(self, compartment_id, resource_metric, **kwargs):
        """
        Gets resources with current utilization (high and low) and projected utilization (high and low) for a resource type over specified time period.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by host resource metric.
            Supported values are CPU, MEMORY, and LOGICAL_MEMORY.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] platform_type: (optional)
            Filter by one or more platform types.
            Possible value is LINUX.

            Allowed values are: "LINUX"

        :param list[str] id: (optional)
            Optional list of host insight resource `OCIDs`__ of the host insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param int forecast_days: (optional)
            Number of days used for utilization forecast analysis.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeHostInsightResourceUtilizationInsightAggregation`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_host_insight_resource_utilization_insight.py.html>`__ to see an example of how to use summarize_host_insight_resource_utilization_insight API.
        """
        resource_path = "/hostInsights/resourceUtilizationInsight"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "platform_type",
            "id",
            "forecast_days",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_host_insight_resource_utilization_insight got unknown kwargs: {!r}".format(extra_kwargs))

        if 'platform_type' in kwargs:
            platform_type_allowed_values = ["LINUX"]
            for platform_type_item in kwargs['platform_type']:
                if platform_type_item not in platform_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `platform_type`, must be one of {0}".format(platform_type_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "platformType": self.base_client.generate_collection_format_param(kwargs.get("platform_type", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "forecastDays": kwargs.get("forecast_days", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="SummarizeHostInsightResourceUtilizationInsightAggregation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceUtilizationInsightAggregation")

    def summarize_sql_insights(self, compartment_id, **kwargs):
        """
        Query SQL Warehouse to get the performance insights for SQLs taking greater than X% database time for a given time period across the given databases or database types.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param float database_time_pct_greater_than: (optional)
            Filter sqls by percentage of db time.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlInsightAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_sql_insights.py.html>`__ to see an example of how to use summarize_sql_insights API.
        """
        resource_path = "/databaseInsights/sqlInsights"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "database_type",
            "database_id",
            "id",
            "database_time_pct_greater_than",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_sql_insights got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "databaseTimePctGreaterThan": kwargs.get("database_time_pct_greater_than", missing),
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="SqlInsightAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlInsightAggregationCollection")

    def summarize_sql_plan_insights(self, compartment_id, sql_identifier, **kwargs):
        """
        Query SQL Warehouse to get the performance insights on the execution plans for a given SQL for a given time period.
        Either databaseId or id must be specified.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str sql_identifier: (required)
            Unique SQL_ID for a SQL Statement.
            Example: `6rgjh9bjmy2s7`

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlPlanInsightAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_sql_plan_insights.py.html>`__ to see an example of how to use summarize_sql_plan_insights API.
        """
        resource_path = "/databaseInsights/sqlPlanInsights"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "database_id",
            "id",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_sql_plan_insights got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing),
            "sqlIdentifier": sql_identifier,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="SqlPlanInsightAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlPlanInsightAggregationCollection")

    def summarize_sql_response_time_distributions(self, compartment_id, sql_identifier, **kwargs):
        """
        Query SQL Warehouse to summarize the response time distribution of query executions for a given SQL for a given time period.
        Either databaseId or id must be specified.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str sql_identifier: (required)
            Unique SQL_ID for a SQL Statement.
            Example: `6rgjh9bjmy2s7`

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlResponseTimeDistributionAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_sql_response_time_distributions.py.html>`__ to see an example of how to use summarize_sql_response_time_distributions API.
        """
        resource_path = "/databaseInsights/sqlResponseTimeDistributions"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "database_id",
            "id",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_sql_response_time_distributions got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing),
            "sqlIdentifier": sql_identifier,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="SqlResponseTimeDistributionAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlResponseTimeDistributionAggregationCollection")

    def summarize_sql_statistics(self, compartment_id, **kwargs):
        """
        Query SQL Warehouse to get the performance statistics for SQLs taking greater than X% database time for a given time period across the given databases or database types.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param float database_time_pct_greater_than: (optional)
            Filter sqls by percentage of db time.

        :param list[str] sql_identifier: (optional)
            One or more unique SQL_IDs for a SQL Statement.
            Example: `6rgjh9bjmy2s7`

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to use when sorting SQL statistics.
            Example: databaseTimeInSec

            Allowed values are: "databaseTimeInSec", "executionsPerHour", "executionsCount", "cpuTimeInSec", "ioTimeInSec", "inefficientWaitTimeInSec", "responseTimeInSec", "planCount", "variability", "averageActiveSessions", "databaseTimePct", "inefficiencyInPct", "changeInCpuTimeInPct", "changeInIoTimeInPct", "changeInInefficientWaitTimeInPct", "changeInResponseTimeInPct", "changeInAverageActiveSessionsInPct", "changeInExecutionsPerHourInPct", "changeInInefficiencyInPct"

        :param list[str] category: (optional)
            Filter sqls by one or more performance categories.

            Allowed values are: "DEGRADING", "VARIANT", "INEFFICIENT", "CHANGING_PLANS", "IMPROVING", "DEGRADING_VARIANT", "DEGRADING_INEFFICIENT", "DEGRADING_CHANGING_PLANS", "DEGRADING_INCREASING_IO", "DEGRADING_INCREASING_CPU", "DEGRADING_INCREASING_INEFFICIENT_WAIT", "DEGRADING_CHANGING_PLANS_AND_INCREASING_IO", "DEGRADING_CHANGING_PLANS_AND_INCREASING_CPU", "DEGRADING_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT", "VARIANT_INEFFICIENT", "VARIANT_CHANGING_PLANS", "VARIANT_INCREASING_IO", "VARIANT_INCREASING_CPU", "VARIANT_INCREASING_INEFFICIENT_WAIT", "VARIANT_CHANGING_PLANS_AND_INCREASING_IO", "VARIANT_CHANGING_PLANS_AND_INCREASING_CPU", "VARIANT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT", "INEFFICIENT_CHANGING_PLANS", "INEFFICIENT_INCREASING_INEFFICIENT_WAIT", "INEFFICIENT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlStatisticAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_sql_statistics.py.html>`__ to see an example of how to use summarize_sql_statistics API.
        """
        resource_path = "/databaseInsights/sqlStatistics"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "database_type",
            "database_id",
            "id",
            "database_time_pct_greater_than",
            "sql_identifier",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "limit",
            "page",
            "opc_request_id",
            "sort_order",
            "sort_by",
            "category"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_sql_statistics got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["databaseTimeInSec", "executionsPerHour", "executionsCount", "cpuTimeInSec", "ioTimeInSec", "inefficientWaitTimeInSec", "responseTimeInSec", "planCount", "variability", "averageActiveSessions", "databaseTimePct", "inefficiencyInPct", "changeInCpuTimeInPct", "changeInIoTimeInPct", "changeInInefficientWaitTimeInPct", "changeInResponseTimeInPct", "changeInAverageActiveSessionsInPct", "changeInExecutionsPerHourInPct", "changeInInefficiencyInPct"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'category' in kwargs:
            category_allowed_values = ["DEGRADING", "VARIANT", "INEFFICIENT", "CHANGING_PLANS", "IMPROVING", "DEGRADING_VARIANT", "DEGRADING_INEFFICIENT", "DEGRADING_CHANGING_PLANS", "DEGRADING_INCREASING_IO", "DEGRADING_INCREASING_CPU", "DEGRADING_INCREASING_INEFFICIENT_WAIT", "DEGRADING_CHANGING_PLANS_AND_INCREASING_IO", "DEGRADING_CHANGING_PLANS_AND_INCREASING_CPU", "DEGRADING_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT", "VARIANT_INEFFICIENT", "VARIANT_CHANGING_PLANS", "VARIANT_INCREASING_IO", "VARIANT_INCREASING_CPU", "VARIANT_INCREASING_INEFFICIENT_WAIT", "VARIANT_CHANGING_PLANS_AND_INCREASING_IO", "VARIANT_CHANGING_PLANS_AND_INCREASING_CPU", "VARIANT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT", "INEFFICIENT_CHANGING_PLANS", "INEFFICIENT_INCREASING_INEFFICIENT_WAIT", "INEFFICIENT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT"]
            for category_item in kwargs['category']:
                if category_item not in category_allowed_values:
                    raise ValueError(
                        "Invalid value for `category`, must be one of {0}".format(category_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "databaseTimePctGreaterThan": kwargs.get("database_time_pct_greater_than", missing),
            "sqlIdentifier": self.base_client.generate_collection_format_param(kwargs.get("sql_identifier", missing), 'multi'),
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "category": self.base_client.generate_collection_format_param(kwargs.get("category", missing), 'multi')
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="SqlStatisticAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlStatisticAggregationCollection")

    def summarize_sql_statistics_time_series(self, compartment_id, sql_identifier, **kwargs):
        """
        Query SQL Warehouse to get the performance statistics time series for a given SQL across given databases for a given time period.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str sql_identifier: (required)
            Unique SQL_ID for a SQL Statement.
            Example: `6rgjh9bjmy2s7`

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database `OCIDs`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlStatisticsTimeSeriesAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_sql_statistics_time_series.py.html>`__ to see an example of how to use summarize_sql_statistics_time_series API.
        """
        resource_path = "/databaseInsights/sqlStatisticsTimeSeries"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "database_id",
            "id",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_sql_statistics_time_series got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "sqlIdentifier": sql_identifier,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="SqlStatisticsTimeSeriesAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlStatisticsTimeSeriesAggregationCollection")

    def summarize_sql_statistics_time_series_by_plan(self, compartment_id, sql_identifier, **kwargs):
        """
        Query SQL Warehouse to get the performance statistics time series for a given SQL by execution plans for a given time period.
        Either databaseId or id must be specified.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str sql_identifier: (required)
            Unique SQL_ID for a SQL Statement.
            Example: `6rgjh9bjmy2s7`

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlStatisticsTimeSeriesByPlanAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_sql_statistics_time_series_by_plan.py.html>`__ to see an example of how to use summarize_sql_statistics_time_series_by_plan API.
        """
        resource_path = "/databaseInsights/sqlStatisticsTimeSeriesByPlan"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "database_id",
            "id",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_sql_statistics_time_series_by_plan got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing),
            "sqlIdentifier": sql_identifier,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="SqlStatisticsTimeSeriesByPlanAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlStatisticsTimeSeriesByPlanAggregationCollection")

    def update_database_insight(self, database_insight_id, update_database_insight_details, **kwargs):
        """
        Updates configuration of a database insight.


        :param str database_insight_id: (required)
            Unique database insight identifier

        :param oci.opsi.models.UpdateDatabaseInsightDetails update_database_insight_details: (required)
            The configuration to be updated.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/update_database_insight.py.html>`__ to see an example of how to use update_database_insight API.
        """
        resource_path = "/databaseInsights/{databaseInsightId}"
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
                "update_database_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseInsightId": database_insight_id
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
                body=update_database_insight_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_database_insight_details)

    def update_enterprise_manager_bridge(self, enterprise_manager_bridge_id, update_enterprise_manager_bridge_details, **kwargs):
        """
        Updates configuration of an Operations Insights Enterprise Manager bridge.


        :param str enterprise_manager_bridge_id: (required)
            Unique Enterprise Manager bridge identifier

        :param oci.opsi.models.UpdateEnterpriseManagerBridgeDetails update_enterprise_manager_bridge_details: (required)
            The configuration to be updated.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/update_enterprise_manager_bridge.py.html>`__ to see an example of how to use update_enterprise_manager_bridge API.
        """
        resource_path = "/enterpriseManagerBridges/{enterpriseManagerBridgeId}"
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
                "update_enterprise_manager_bridge got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "enterpriseManagerBridgeId": enterprise_manager_bridge_id
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
                body=update_enterprise_manager_bridge_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_enterprise_manager_bridge_details)

    def update_host_insight(self, host_insight_id, update_host_insight_details, **kwargs):
        """
        Updates configuration of a host insight.


        :param str host_insight_id: (required)
            Unique host insight identifier

        :param oci.opsi.models.UpdateHostInsightDetails update_host_insight_details: (required)
            The configuration to be updated.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/update_host_insight.py.html>`__ to see an example of how to use update_host_insight API.
        """
        resource_path = "/hostInsights/{hostInsightId}"
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
                "update_host_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "hostInsightId": host_insight_id
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
                body=update_host_insight_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_host_insight_details)
