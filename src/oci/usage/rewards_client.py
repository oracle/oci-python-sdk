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
from .models import usage_type_mapping
missing = Sentinel("Missing")


class RewardsClient(object):
    """
    Use the Usage Proxy API to list Oracle Support Rewards, view related detailed usage information, and manage users who redeem rewards. For more information, see [Oracle Support Rewards Overview](/iaas/Content/Billing/Concepts/supportrewardsoverview.htm).
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
            'base_path': '/20190111',
            'service_endpoint_template': 'https://identity.{region}.oci.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'circuit_breaker_strategy': kwargs.get('circuit_breaker_strategy', circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY)
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        if base_client_init_kwargs.get('circuit_breaker_strategy') is None:
            base_client_init_kwargs['circuit_breaker_strategy'] = circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY
        if 'allow_control_chars' in kwargs:
            base_client_init_kwargs['allow_control_chars'] = kwargs.get('allow_control_chars')
        self.base_client = BaseClient("rewards", config, signer, usage_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

    def create_redeemable_user(self, create_redeemable_user_details, tenancy_id, subscription_id, **kwargs):
        """
        Adds the list of redeemable user summary for a subscription ID.


        :param oci.usage.models.CreateRedeemableUserDetails create_redeemable_user_details: (required)
            CreateRedeemableUserDetails information.

        :param str tenancy_id: (required)
            The OCID of the tenancy.

        :param str subscription_id: (required)
            The subscription ID for which rewards information is requested for.

        :param str user_id: (optional)
            The user ID of the person to send a copy of an email.

        :param str opc_request_id: (optional)
            Unique, Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted, only if the etag you
            provide matches the resource's current etag value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error, without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.usage.models.RedeemableUserCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/usage/create_redeemable_user.py.html>`__ to see an example of how to use create_redeemable_user API.
        """
        resource_path = "/subscriptions/{subscriptionId}/redeemableUsers"
        method = "POST"
        operation_name = "create_redeemable_user"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/usage-proxy/20190111/RedeemableUser/CreateRedeemableUser"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "user_id",
            "opc_request_id",
            "if_match",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_redeemable_user got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "subscriptionId": subscription_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "tenancyId": tenancy_id,
            "userId": kwargs.get("user_id", missing)
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
                query_params=query_params,
                header_params=header_params,
                body=create_redeemable_user_details,
                response_type="RedeemableUserCollection",
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
                body=create_redeemable_user_details,
                response_type="RedeemableUserCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def delete_redeemable_user(self, email_id, tenancy_id, subscription_id, **kwargs):
        """
        Deletes the list of redeemable user email ID for a subscription ID.


        :param str email_id: (required)
            The email ID that needs to be deleted.

        :param str tenancy_id: (required)
            The OCID of the tenancy.

        :param str subscription_id: (required)
            The subscription ID for which rewards information is requested for.

        :param str opc_request_id: (optional)
            Unique, Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call
            for a resource, set the `if-match` parameter to the value of the
            etag from a previous GET or POST response for that resource.
            The resource will be updated or deleted, only if the etag you
            provide matches the resource's current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/usage/delete_redeemable_user.py.html>`__ to see an example of how to use delete_redeemable_user API.
        """
        resource_path = "/subscriptions/{subscriptionId}/redeemableUsers"
        method = "DELETE"
        operation_name = "delete_redeemable_user"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/usage-proxy/20190111/RedeemableUser/DeleteRedeemableUser"

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
                "delete_redeemable_user got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "subscriptionId": subscription_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "emailId": email_id,
            "tenancyId": tenancy_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

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

    def list_products(self, tenancy_id, subscription_id, usage_period_key, **kwargs):
        """
        Provides product information that is specific to a reward usage period and its usage details.


        :param str tenancy_id: (required)
            The OCID of the tenancy.

        :param str subscription_id: (required)
            The subscription ID for which rewards information is requested for.

        :param str usage_period_key: (required)
            The SPM Identifier for the usage period.

        :param str opc_request_id: (optional)
            Unique, Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str page: (optional)
            The value of the 'opc-next-page' response header from the previous call.

        :param int limit: (optional)
            The maximum number of items to return in the paginated response.

        :param str sort_order: (optional)
            The sort order to use, which can be ascending (ASC) or descending (DESC).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Supports one sort order.

            Allowed values are: "TIMECREATED", "TIMESTART"

        :param str producttype: (optional)
            The field to specify the type of product.

            Allowed values are: "ALL", "ELIGIBLE", "INELIGIBLE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.usage.models.ProductCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/usage/list_products.py.html>`__ to see an example of how to use list_products API.
        """
        resource_path = "/subscriptions/{subscriptionId}/products"
        method = "GET"
        operation_name = "list_products"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/usage-proxy/20190111/ProductSummary/ListProducts"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "page",
            "limit",
            "sort_order",
            "sort_by",
            "producttype"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_products got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "subscriptionId": subscription_id
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
            sort_by_allowed_values = ["TIMECREATED", "TIMESTART"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'producttype' in kwargs:
            producttype_allowed_values = ["ALL", "ELIGIBLE", "INELIGIBLE"]
            if kwargs['producttype'] not in producttype_allowed_values:
                raise ValueError(
                    "Invalid value for `producttype`, must be one of {0}".format(producttype_allowed_values)
                )

        query_params = {
            "tenancyId": tenancy_id,
            "usagePeriodKey": usage_period_key,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "producttype": kwargs.get("producttype", missing)
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
                response_type="ProductCollection",
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
                response_type="ProductCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_redeemable_users(self, tenancy_id, subscription_id, **kwargs):
        """
        Provides the list of user summary that can redeem rewards for the given subscription ID.


        :param str tenancy_id: (required)
            The OCID of the tenancy.

        :param str subscription_id: (required)
            The subscription ID for which rewards information is requested for.

        :param str opc_request_id: (optional)
            Unique, Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str page: (optional)
            The value of the 'opc-next-page' response header from the previous call.

        :param int limit: (optional)
            The maximum number of items to return in the paginated response.

        :param str sort_order: (optional)
            The sort order to use, which can be ascending (ASC) or descending (DESC).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Supports one sort order.

            Allowed values are: "TIMECREATED", "TIMESTART"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.usage.models.RedeemableUserCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/usage/list_redeemable_users.py.html>`__ to see an example of how to use list_redeemable_users API.
        """
        resource_path = "/subscriptions/{subscriptionId}/redeemableUsers"
        method = "GET"
        operation_name = "list_redeemable_users"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/usage-proxy/20190111/RedeemableUserSummary/ListRedeemableUsers"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "page",
            "limit",
            "sort_order",
            "sort_by"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_redeemable_users got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "subscriptionId": subscription_id
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
            sort_by_allowed_values = ["TIMECREATED", "TIMESTART"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "tenancyId": tenancy_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RedeemableUserCollection",
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
                response_type="RedeemableUserCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_redemptions(self, tenancy_id, subscription_id, **kwargs):
        """
        Returns the list of redemption for the subscription ID.


        :param str tenancy_id: (required)
            The OCID of the tenancy.

        :param str subscription_id: (required)
            The subscription ID for which rewards information is requested for.

        :param datetime time_redeemed_greater_than_or_equal_to: (optional)
            The starting redeemed date filter for the redemption history.

        :param datetime time_redeemed_less_than: (optional)
            The ending redeemed date filter for the redemption history.

        :param str opc_request_id: (optional)
            Unique, Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str page: (optional)
            The value of the 'opc-next-page' response header from the previous call.

        :param int limit: (optional)
            The maximum number of items to return in the paginated response.

        :param str sort_order: (optional)
            The sort order to use, which can be ascending (ASC) or descending (DESC).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to be used only for list redemptions API. Supports one sort order.

            Allowed values are: "TIMEREDEEMED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.usage.models.RedemptionCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/usage/list_redemptions.py.html>`__ to see an example of how to use list_redemptions API.
        """
        resource_path = "/subscriptions/{subscriptionId}/redemptions"
        method = "GET"
        operation_name = "list_redemptions"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/usage-proxy/20190111/RedemptionSummary/ListRedemptions"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "time_redeemed_greater_than_or_equal_to",
            "time_redeemed_less_than",
            "opc_request_id",
            "page",
            "limit",
            "sort_order",
            "sort_by"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_redemptions got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "subscriptionId": subscription_id
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
            sort_by_allowed_values = ["TIMEREDEEMED"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "tenancyId": tenancy_id,
            "timeRedeemedGreaterThanOrEqualTo": kwargs.get("time_redeemed_greater_than_or_equal_to", missing),
            "timeRedeemedLessThan": kwargs.get("time_redeemed_less_than", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RedemptionCollection",
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
                response_type="RedemptionCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_rewards(self, tenancy_id, subscription_id, **kwargs):
        """
        Returns the list of rewards for a subscription ID.


        :param str tenancy_id: (required)
            The OCID of the tenancy.

        :param str subscription_id: (required)
            The subscription ID for which rewards information is requested for.

        :param str opc_request_id: (optional)
            Unique, Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.usage.models.RewardCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/usage/list_rewards.py.html>`__ to see an example of how to use list_rewards API.
        """
        resource_path = "/subscriptions/{subscriptionId}/rewards"
        method = "GET"
        operation_name = "list_rewards"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/usage-proxy/20190111/MonthlyRewardSummary/ListRewards"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_rewards got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "subscriptionId": subscription_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "tenancyId": tenancy_id
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
                response_type="RewardCollection",
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
                response_type="RewardCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
