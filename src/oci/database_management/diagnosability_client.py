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
from .models import database_management_type_mapping
missing = Sentinel("Missing")


class DiagnosabilityClient(object):
    """
    Use the Database Management API to perform tasks such as obtaining performance and resource usage metrics
    for a fleet of Managed Databases or a specific Managed Database, creating Managed Database Groups, and
    running a SQL job on a Managed Database or Managed Database Group.
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
            'base_path': '/20201101',
            'service_endpoint_template': 'https://dbmgmt.{region}.oci.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'circuit_breaker_strategy': kwargs.get('circuit_breaker_strategy', circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY)
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        if base_client_init_kwargs.get('circuit_breaker_strategy') is None:
            base_client_init_kwargs['circuit_breaker_strategy'] = circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY
        if 'allow_control_chars' in kwargs:
            base_client_init_kwargs['allow_control_chars'] = kwargs.get('allow_control_chars')
        self.base_client = BaseClient("diagnosability", config, signer, database_management_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

    def list_alert_logs(self, managed_database_id, **kwargs):
        """
        Lists the alert logs for the specified Managed Database.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to timestamp to filter the logs.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to timestamp to filter the logs.

        :param str level_filter: (optional)
            The optional parameter to filter the alert logs by log level.

            Allowed values are: "CRITICAL", "SEVERE", "IMPORTANT", "NORMAL", "ALL"

        :param str type_filter: (optional)
            The optional parameter to filter the attention or alert logs by type.

            Allowed values are: "UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE", "ALL"

        :param str log_search_text: (optional)
            The optional query parameter to filter the attention or alert logs by search text.

        :param bool is_regular_expression: (optional)
            The flag to indicate whether the search text is regular expression or not.

        :param str sort_by: (optional)
            The possible sortBy values of attention logs.

            Allowed values are: "LEVEL", "TYPE", "MESSAGE", "TIMESTAMP"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.

            Allowed values are: "ASC", "DESC"

        :param str page: (optional)
            The page token representing the page from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in the paginated response.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.AlertLogCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/list_alert_logs.py.html>`__ to see an example of how to use list_alert_logs API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/alertLogs"
        method = "GET"
        operation_name = "list_alert_logs"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/database-management/20201101/ManagedDatabase/ListAlertLogs"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "level_filter",
            "type_filter",
            "log_search_text",
            "is_regular_expression",
            "sort_by",
            "sort_order",
            "page",
            "limit",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_alert_logs got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'level_filter' in kwargs:
            level_filter_allowed_values = ["CRITICAL", "SEVERE", "IMPORTANT", "NORMAL", "ALL"]
            if kwargs['level_filter'] not in level_filter_allowed_values:
                raise ValueError(
                    "Invalid value for `level_filter`, must be one of {0}".format(level_filter_allowed_values)
                )

        if 'type_filter' in kwargs:
            type_filter_allowed_values = ["UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE", "ALL"]
            if kwargs['type_filter'] not in type_filter_allowed_values:
                raise ValueError(
                    "Invalid value for `type_filter`, must be one of {0}".format(type_filter_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["LEVEL", "TYPE", "MESSAGE", "TIMESTAMP"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "levelFilter": kwargs.get("level_filter", missing),
            "typeFilter": kwargs.get("type_filter", missing),
            "logSearchText": kwargs.get("log_search_text", missing),
            "isRegularExpression": kwargs.get("is_regular_expression", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
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
                response_type="AlertLogCollection",
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
                response_type="AlertLogCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_attention_logs(self, managed_database_id, **kwargs):
        """
        Lists the attention logs for the specified Managed Database.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to timestamp to filter the logs.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to timestamp to filter the logs.

        :param str urgency_filter: (optional)
            The optional parameter to filter the attention logs by urgency.

            Allowed values are: "IMMEDIATE", "SOON", "DEFERRABLE", "INFO", "ALL"

        :param str type_filter: (optional)
            The optional parameter to filter the attention or alert logs by type.

            Allowed values are: "UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE", "ALL"

        :param str log_search_text: (optional)
            The optional query parameter to filter the attention or alert logs by search text.

        :param bool is_regular_expression: (optional)
            The flag to indicate whether the search text is regular expression or not.

        :param str sort_by: (optional)
            The possible sortBy values of attention logs.

            Allowed values are: "URGENCY", "TYPE", "MESSAGE", "TIMESTAMP", "SCOPE", "TARGET_USER"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Ascending order is the default order.

            Allowed values are: "ASC", "DESC"

        :param str page: (optional)
            The page token representing the page from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in the paginated response.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.AttentionLogCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/list_attention_logs.py.html>`__ to see an example of how to use list_attention_logs API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/attentionLogs"
        method = "GET"
        operation_name = "list_attention_logs"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/database-management/20201101/ManagedDatabase/ListAttentionLogs"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "urgency_filter",
            "type_filter",
            "log_search_text",
            "is_regular_expression",
            "sort_by",
            "sort_order",
            "page",
            "limit",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_attention_logs got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'urgency_filter' in kwargs:
            urgency_filter_allowed_values = ["IMMEDIATE", "SOON", "DEFERRABLE", "INFO", "ALL"]
            if kwargs['urgency_filter'] not in urgency_filter_allowed_values:
                raise ValueError(
                    "Invalid value for `urgency_filter`, must be one of {0}".format(urgency_filter_allowed_values)
                )

        if 'type_filter' in kwargs:
            type_filter_allowed_values = ["UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE", "ALL"]
            if kwargs['type_filter'] not in type_filter_allowed_values:
                raise ValueError(
                    "Invalid value for `type_filter`, must be one of {0}".format(type_filter_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["URGENCY", "TYPE", "MESSAGE", "TIMESTAMP", "SCOPE", "TARGET_USER"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "urgencyFilter": kwargs.get("urgency_filter", missing),
            "typeFilter": kwargs.get("type_filter", missing),
            "logSearchText": kwargs.get("log_search_text", missing),
            "isRegularExpression": kwargs.get("is_regular_expression", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
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
                response_type="AttentionLogCollection",
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
                response_type="AttentionLogCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def summarize_alert_log_counts(self, managed_database_id, **kwargs):
        """
        Get the counts of alert logs for the specified Managed Database.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to timestamp to filter the logs.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to timestamp to filter the logs.

        :param str level_filter: (optional)
            The optional parameter to filter the alert logs by log level.

            Allowed values are: "CRITICAL", "SEVERE", "IMPORTANT", "NORMAL", "ALL"

        :param str group_by: (optional)
            The optional parameter used to group different alert logs.

            Allowed values are: "LEVEL", "TYPE"

        :param str type_filter: (optional)
            The optional parameter to filter the attention or alert logs by type.

            Allowed values are: "UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE", "ALL"

        :param str log_search_text: (optional)
            The optional query parameter to filter the attention or alert logs by search text.

        :param bool is_regular_expression: (optional)
            The flag to indicate whether the search text is regular expression or not.

        :param str page: (optional)
            The page token representing the page from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in the paginated response.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.AlertLogCountsCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/summarize_alert_log_counts.py.html>`__ to see an example of how to use summarize_alert_log_counts API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/alertLogCounts"
        method = "GET"
        operation_name = "summarize_alert_log_counts"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/database-management/20201101/ManagedDatabase/SummarizeAlertLogCounts"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "level_filter",
            "group_by",
            "type_filter",
            "log_search_text",
            "is_regular_expression",
            "page",
            "limit",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_alert_log_counts got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'level_filter' in kwargs:
            level_filter_allowed_values = ["CRITICAL", "SEVERE", "IMPORTANT", "NORMAL", "ALL"]
            if kwargs['level_filter'] not in level_filter_allowed_values:
                raise ValueError(
                    "Invalid value for `level_filter`, must be one of {0}".format(level_filter_allowed_values)
                )

        if 'group_by' in kwargs:
            group_by_allowed_values = ["LEVEL", "TYPE"]
            if kwargs['group_by'] not in group_by_allowed_values:
                raise ValueError(
                    "Invalid value for `group_by`, must be one of {0}".format(group_by_allowed_values)
                )

        if 'type_filter' in kwargs:
            type_filter_allowed_values = ["UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE", "ALL"]
            if kwargs['type_filter'] not in type_filter_allowed_values:
                raise ValueError(
                    "Invalid value for `type_filter`, must be one of {0}".format(type_filter_allowed_values)
                )

        query_params = {
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "levelFilter": kwargs.get("level_filter", missing),
            "groupBy": kwargs.get("group_by", missing),
            "typeFilter": kwargs.get("type_filter", missing),
            "logSearchText": kwargs.get("log_search_text", missing),
            "isRegularExpression": kwargs.get("is_regular_expression", missing),
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
                response_type="AlertLogCountsCollection",
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
                response_type="AlertLogCountsCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def summarize_attention_log_counts(self, managed_database_id, **kwargs):
        """
        Get the counts of attention logs for the specified Managed Database.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to timestamp to filter the logs.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to timestamp to filter the logs.

        :param str urgency_filter: (optional)
            The optional parameter to filter the attention logs by urgency.

            Allowed values are: "IMMEDIATE", "SOON", "DEFERRABLE", "INFO", "ALL"

        :param str group_by: (optional)
            The optional parameter used to group different attention logs.

            Allowed values are: "URGENCY", "TYPE"

        :param str type_filter: (optional)
            The optional parameter to filter the attention or alert logs by type.

            Allowed values are: "UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE", "ALL"

        :param str log_search_text: (optional)
            The optional query parameter to filter the attention or alert logs by search text.

        :param bool is_regular_expression: (optional)
            The flag to indicate whether the search text is regular expression or not.

        :param str page: (optional)
            The page token representing the page from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in the paginated response.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.AttentionLogCountsCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/summarize_attention_log_counts.py.html>`__ to see an example of how to use summarize_attention_log_counts API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/attentionLogCounts"
        method = "GET"
        operation_name = "summarize_attention_log_counts"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/database-management/20201101/ManagedDatabase/SummarizeAttentionLogCounts"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "urgency_filter",
            "group_by",
            "type_filter",
            "log_search_text",
            "is_regular_expression",
            "page",
            "limit",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_attention_log_counts got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'urgency_filter' in kwargs:
            urgency_filter_allowed_values = ["IMMEDIATE", "SOON", "DEFERRABLE", "INFO", "ALL"]
            if kwargs['urgency_filter'] not in urgency_filter_allowed_values:
                raise ValueError(
                    "Invalid value for `urgency_filter`, must be one of {0}".format(urgency_filter_allowed_values)
                )

        if 'group_by' in kwargs:
            group_by_allowed_values = ["URGENCY", "TYPE"]
            if kwargs['group_by'] not in group_by_allowed_values:
                raise ValueError(
                    "Invalid value for `group_by`, must be one of {0}".format(group_by_allowed_values)
                )

        if 'type_filter' in kwargs:
            type_filter_allowed_values = ["UNKNOWN", "INCIDENT_ERROR", "ERROR", "WARNING", "NOTIFICATION", "TRACE", "ALL"]
            if kwargs['type_filter'] not in type_filter_allowed_values:
                raise ValueError(
                    "Invalid value for `type_filter`, must be one of {0}".format(type_filter_allowed_values)
                )

        query_params = {
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "urgencyFilter": kwargs.get("urgency_filter", missing),
            "groupBy": kwargs.get("group_by", missing),
            "typeFilter": kwargs.get("type_filter", missing),
            "logSearchText": kwargs.get("log_search_text", missing),
            "isRegularExpression": kwargs.get("is_regular_expression", missing),
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
                response_type="AttentionLogCountsCollection",
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
                response_type="AttentionLogCountsCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
