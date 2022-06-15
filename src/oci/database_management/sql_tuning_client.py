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


class SqlTuningClient(object):
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
        self.base_client = BaseClient("sql_tuning", config, signer, database_management_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

    def clone_sql_tuning_task(self, managed_database_id, clone_sql_tuning_task_details, **kwargs):
        """
        Clones and runs a SQL tuning task in the database.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_management.models.CloneSqlTuningTaskDetails clone_sql_tuning_task_details: (required)
            The detailed inputs required to clone a SQL tuning task.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.SqlTuningTaskReturn`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/clone_sql_tuning_task.py.html>`__ to see an example of how to use clone_sql_tuning_task API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/actions/cloneSqlTuningTask"
        method = "POST"
        operation_name = "clone_sql_tuning_task"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/database-management/20201101/ManagedDatabase/CloneSqlTuningTask"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "clone_sql_tuning_task got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
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
                header_params=header_params,
                body=clone_sql_tuning_task_details,
                response_type="SqlTuningTaskReturn",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=clone_sql_tuning_task_details,
                response_type="SqlTuningTaskReturn",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def drop_sql_tuning_task(self, managed_database_id, drop_sql_tuning_task_details, **kwargs):
        """
        Drops a SQL tuning task and its related results from the database.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_management.models.DropSqlTuningTaskDetails drop_sql_tuning_task_details: (required)
            The detailed inputs required to drop a SQL tuning task.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
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

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/drop_sql_tuning_task.py.html>`__ to see an example of how to use drop_sql_tuning_task API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/actions/dropSqlTuningTask"
        method = "POST"
        operation_name = "drop_sql_tuning_task"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/database-management/20201101/ManagedDatabase/DropSqlTuningTask"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "drop_sql_tuning_task got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
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
                header_params=header_params,
                body=drop_sql_tuning_task_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=drop_sql_tuning_task_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_execution_plan_stats_comparision(self, managed_database_id, sql_tuning_advisor_task_id, sql_object_id, execution_id, **kwargs):
        """
        Retrieves a comparison of the existing SQL execution plan and a new plan.
        A SQL tuning task may suggest a new execution plan for a SQL,
        and this API retrieves the comparison report of the statistics of the two plans.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int sql_tuning_advisor_task_id: (required)
            The SQL tuning task identifier. This is not the `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int sql_object_id: (required)
            The SQL object ID for the SQL tuning task. This is not the `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int execution_id: (required)
            The execution ID for an execution of a SQL tuning task. This is not the `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.ExecutionPlanStatsComparision`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/get_execution_plan_stats_comparision.py.html>`__ to see an example of how to use get_execution_plan_stats_comparision API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/sqlTuningAdvisorTasks/{sqlTuningAdvisorTaskId}/executionPlanStatsComparision"
        method = "GET"
        operation_name = "get_execution_plan_stats_comparision"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/database-management/20201101/ManagedDatabase/GetExecutionPlanStatsComparision"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_execution_plan_stats_comparision got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id,
            "sqlTuningAdvisorTaskId": sql_tuning_advisor_task_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "sqlObjectId": sql_object_id,
            "executionId": execution_id
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
                response_type="ExecutionPlanStatsComparision",
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
                response_type="ExecutionPlanStatsComparision",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_sql_execution_plan(self, managed_database_id, sql_tuning_advisor_task_id, sql_object_id, attribute, **kwargs):
        """
        Retrieves a SQL execution plan for the SQL being tuned.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int sql_tuning_advisor_task_id: (required)
            The SQL tuning task identifier. This is not the `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int sql_object_id: (required)
            The SQL object ID for the SQL tuning task. This is not the `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str attribute: (required)
            The attribute of the SQL execution plan.

            Allowed values are: "ORIGINAL", "ORIGINAL_WITH_ADJUSTED_COST", "USING_SQL_PROFILE", "USING_NEW_INDICES", "USING_PARALLEL_EXECUTION"

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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.SqlTuningAdvisorTaskSqlExecutionPlan`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/get_sql_execution_plan.py.html>`__ to see an example of how to use get_sql_execution_plan API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/sqlTuningAdvisorTasks/{sqlTuningAdvisorTaskId}/sqlExecutionPlan"
        method = "GET"
        operation_name = "get_sql_execution_plan"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/database-management/20201101/ManagedDatabase/GetSqlExecutionPlan"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_sql_execution_plan got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id,
            "sqlTuningAdvisorTaskId": sql_tuning_advisor_task_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        attribute_allowed_values = ["ORIGINAL", "ORIGINAL_WITH_ADJUSTED_COST", "USING_SQL_PROFILE", "USING_NEW_INDICES", "USING_PARALLEL_EXECUTION"]
        if attribute not in attribute_allowed_values:
            raise ValueError(
                "Invalid value for `attribute`, must be one of {0}".format(attribute_allowed_values)
            )

        query_params = {
            "sqlObjectId": sql_object_id,
            "attribute": attribute
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
                response_type="SqlTuningAdvisorTaskSqlExecutionPlan",
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
                response_type="SqlTuningAdvisorTaskSqlExecutionPlan",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_sql_tuning_advisor_task_summary_report(self, managed_database_id, sql_tuning_advisor_task_id, **kwargs):
        """
        Gets the summary report for the specified SQL Tuning Advisor task.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int sql_tuning_advisor_task_id: (required)
            The SQL tuning task identifier. This is not the `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str search_period: (optional)
            How far back the API will search for begin and end exec id. Unused if neither exec ids nor time filter query params are supplied. This is applicable only for Auto SQL Tuning tasks.

            Allowed values are: "LAST_24HR", "LAST_7DAY", "LAST_31DAY", "SINCE_LAST", "ALL"

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to query parameter to filter the timestamp. This is applicable only for Auto SQL Tuning tasks.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the timestamp. This is applicable only for Auto SQL Tuning tasks.

        :param int begin_exec_id_greater_than_or_equal_to: (optional)
            The optional greater than or equal to filter on the execution ID related to a specific SQL Tuning Advisor task. This is applicable only for Auto SQL Tuning tasks.

        :param int end_exec_id_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter on the execution ID related to a specific SQL Tuning Advisor task. This is applicable only for Auto SQL Tuning tasks.

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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.SqlTuningAdvisorTaskSummaryReport`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/get_sql_tuning_advisor_task_summary_report.py.html>`__ to see an example of how to use get_sql_tuning_advisor_task_summary_report API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/sqlTuningAdvisorTasks/{sqlTuningAdvisorTaskId}/summaryReport"
        method = "GET"
        operation_name = "get_sql_tuning_advisor_task_summary_report"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/database-management/20201101/ManagedDatabase/GetSqlTuningAdvisorTaskSummaryReport"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "search_period",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "begin_exec_id_greater_than_or_equal_to",
            "end_exec_id_less_than_or_equal_to",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_sql_tuning_advisor_task_summary_report got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id,
            "sqlTuningAdvisorTaskId": sql_tuning_advisor_task_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'search_period' in kwargs:
            search_period_allowed_values = ["LAST_24HR", "LAST_7DAY", "LAST_31DAY", "SINCE_LAST", "ALL"]
            if kwargs['search_period'] not in search_period_allowed_values:
                raise ValueError(
                    "Invalid value for `search_period`, must be one of {0}".format(search_period_allowed_values)
                )

        query_params = {
            "searchPeriod": kwargs.get("search_period", missing),
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "beginExecIdGreaterThanOrEqualTo": kwargs.get("begin_exec_id_greater_than_or_equal_to", missing),
            "endExecIdLessThanOrEqualTo": kwargs.get("end_exec_id_less_than_or_equal_to", missing)
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
                response_type="SqlTuningAdvisorTaskSummaryReport",
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
                response_type="SqlTuningAdvisorTaskSummaryReport",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_sql_tuning_advisor_task_findings(self, managed_database_id, sql_tuning_advisor_task_id, **kwargs):
        """
        Gets an array of the details of the findings that match specific filters.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int sql_tuning_advisor_task_id: (required)
            The SQL tuning task identifier. This is not the `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int begin_exec_id: (optional)
            The optional greater than or equal to filter on the execution ID related to a specific SQL Tuning Advisor task.

        :param int end_exec_id: (optional)
            The optional less than or equal to query parameter to filter on the execution ID related to a specific SQL Tuning Advisor task.

        :param str search_period: (optional)
            The search period during which the API will search for begin and end exec id, if not supplied.
            Unused if beginExecId and endExecId optional query params are both supplied.

            Allowed values are: "LAST_24HR", "LAST_7DAY", "LAST_31DAY", "SINCE_LAST", "ALL"

        :param str finding_filter: (optional)
            The filter used to display specific findings in the report.

            Allowed values are: "none", "FINDINGS", "NOFINDINGS", "ERRORS", "PROFILES", "INDICES", "STATS", "RESTRUCTURE", "ALTERNATIVE", "AUTO_PROFILES", "OTHER_PROFILES"

        :param str stats_hash_filter: (optional)
            The hash value of the object for the statistic finding search.

        :param str index_hash_filter: (optional)
            The hash value of the index table name.

        :param str sort_by: (optional)
            The possible sortBy values of an object's recommendations.

            Allowed values are: "DBTIME_BENEFIT", "PARSING_SCHEMA", "SQL_ID", "STATS", "PROFILES", "SQL_BENEFIT", "DATE", "INDICES", "RESTRUCTURE", "ALTERNATIVE", "MISC", "ERROR", "TIMEOUTS"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the default order.

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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.SqlTuningAdvisorTaskFindingCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/list_sql_tuning_advisor_task_findings.py.html>`__ to see an example of how to use list_sql_tuning_advisor_task_findings API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/sqlTuningAdvisorTasks/{sqlTuningAdvisorTaskId}/findings"
        method = "GET"
        operation_name = "list_sql_tuning_advisor_task_findings"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/database-management/20201101/ManagedDatabase/ListSqlTuningAdvisorTaskFindings"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "begin_exec_id",
            "end_exec_id",
            "search_period",
            "finding_filter",
            "stats_hash_filter",
            "index_hash_filter",
            "sort_by",
            "sort_order",
            "page",
            "limit",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_sql_tuning_advisor_task_findings got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id,
            "sqlTuningAdvisorTaskId": sql_tuning_advisor_task_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'search_period' in kwargs:
            search_period_allowed_values = ["LAST_24HR", "LAST_7DAY", "LAST_31DAY", "SINCE_LAST", "ALL"]
            if kwargs['search_period'] not in search_period_allowed_values:
                raise ValueError(
                    "Invalid value for `search_period`, must be one of {0}".format(search_period_allowed_values)
                )

        if 'finding_filter' in kwargs:
            finding_filter_allowed_values = ["none", "FINDINGS", "NOFINDINGS", "ERRORS", "PROFILES", "INDICES", "STATS", "RESTRUCTURE", "ALTERNATIVE", "AUTO_PROFILES", "OTHER_PROFILES"]
            if kwargs['finding_filter'] not in finding_filter_allowed_values:
                raise ValueError(
                    "Invalid value for `finding_filter`, must be one of {0}".format(finding_filter_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["DBTIME_BENEFIT", "PARSING_SCHEMA", "SQL_ID", "STATS", "PROFILES", "SQL_BENEFIT", "DATE", "INDICES", "RESTRUCTURE", "ALTERNATIVE", "MISC", "ERROR", "TIMEOUTS"]
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
            "beginExecId": kwargs.get("begin_exec_id", missing),
            "endExecId": kwargs.get("end_exec_id", missing),
            "searchPeriod": kwargs.get("search_period", missing),
            "findingFilter": kwargs.get("finding_filter", missing),
            "statsHashFilter": kwargs.get("stats_hash_filter", missing),
            "indexHashFilter": kwargs.get("index_hash_filter", missing),
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
                response_type="SqlTuningAdvisorTaskFindingCollection",
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
                response_type="SqlTuningAdvisorTaskFindingCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_sql_tuning_advisor_task_recommendations(self, managed_database_id, sql_tuning_advisor_task_id, sql_object_id, execution_id, **kwargs):
        """
        Gets the findings and possible actions for a given object in a SQL tuning task.
        The task ID and object ID are used to retrieve the findings and recommendations.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int sql_tuning_advisor_task_id: (required)
            The SQL tuning task identifier. This is not the `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int sql_object_id: (required)
            The SQL object ID for the SQL tuning task. This is not the `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int execution_id: (required)
            The execution ID for an execution of a SQL tuning task. This is not the `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str sort_by: (optional)
            The possible sortBy values of an object's recommendations.

            Allowed values are: "RECOMMENDATION_TYPE", "BENEFIT"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the default order.

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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.SqlTuningAdvisorTaskRecommendationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/list_sql_tuning_advisor_task_recommendations.py.html>`__ to see an example of how to use list_sql_tuning_advisor_task_recommendations API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/sqlTuningAdvisorTasks/{sqlTuningAdvisorTaskId}/recommendations"
        method = "GET"
        operation_name = "list_sql_tuning_advisor_task_recommendations"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/database-management/20201101/ManagedDatabase/ListSqlTuningAdvisorTaskRecommendations"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "sort_by",
            "sort_order",
            "page",
            "limit",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_sql_tuning_advisor_task_recommendations got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id,
            "sqlTuningAdvisorTaskId": sql_tuning_advisor_task_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["RECOMMENDATION_TYPE", "BENEFIT"]
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
            "sqlObjectId": sql_object_id,
            "executionId": execution_id,
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
                response_type="SqlTuningAdvisorTaskRecommendationCollection",
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
                response_type="SqlTuningAdvisorTaskRecommendationCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_sql_tuning_advisor_tasks(self, managed_database_id, **kwargs):
        """
        Lists the SQL Tuning Advisor tasks for the specified Managed Database.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str name: (optional)
            The optional query parameter to filter the SQL Tuning Advisor task list by name.

        :param str status: (optional)
            The optional query parameter to filter the SQL Tuning Advisor task list by status.

            Allowed values are: "INITIAL", "EXECUTING", "INTERRUPTED", "COMPLETED", "ERROR"

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to query parameter to filter the timestamp.

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the timestamp.

        :param str page: (optional)
            The page token representing the page from where the next set of paginated results
            are retrieved. This is usually retrieved from a previous list call.

        :param int limit: (optional)
            The maximum number of records returned in the paginated response.

        :param str sort_by: (optional)
            The option to sort the SQL Tuning Advisor task summary data.

            Allowed values are: "NAME", "START_TIME"

        :param str sort_order: (optional)
            The option to sort information in ascending (\u2018ASC\u2019) or descending (\u2018DESC\u2019) order. Descending order is the default order.

            Allowed values are: "ASC", "DESC"

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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.SqlTuningAdvisorTaskCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/list_sql_tuning_advisor_tasks.py.html>`__ to see an example of how to use list_sql_tuning_advisor_tasks API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/sqlTuningAdvisorTasks"
        method = "GET"
        operation_name = "list_sql_tuning_advisor_tasks"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/database-management/20201101/ManagedDatabase/ListSqlTuningAdvisorTasks"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "name",
            "status",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "page",
            "limit",
            "sort_by",
            "sort_order",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_sql_tuning_advisor_tasks got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'status' in kwargs:
            status_allowed_values = ["INITIAL", "EXECUTING", "INTERRUPTED", "COMPLETED", "ERROR"]
            if kwargs['status'] not in status_allowed_values:
                raise ValueError(
                    "Invalid value for `status`, must be one of {0}".format(status_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["NAME", "START_TIME"]
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
            "name": kwargs.get("name", missing),
            "status": kwargs.get("status", missing),
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
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
                response_type="SqlTuningAdvisorTaskCollection",
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
                response_type="SqlTuningAdvisorTaskCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_sql_tuning_sets(self, managed_database_id, **kwargs):
        """
        Lists the SQL tuning sets for the specified Managed Database.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str owner: (optional)
            The owner of the SQL tuning set.

        :param str name_contains: (optional)
            Allow searching the name of the SQL tuning set by partial matching. The search is case insensitive.

        :param str sort_by: (optional)
            The option to sort the SQL tuning set summary data.

            Allowed values are: "NAME"

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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.SqlTuningSetCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/list_sql_tuning_sets.py.html>`__ to see an example of how to use list_sql_tuning_sets API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/sqlTuningSets"
        method = "GET"
        operation_name = "list_sql_tuning_sets"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/database-management/20201101/ManagedDatabase/ListSqlTuningSets"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "owner",
            "name_contains",
            "sort_by",
            "sort_order",
            "page",
            "limit",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_sql_tuning_sets got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["NAME"]
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
            "owner": kwargs.get("owner", missing),
            "nameContains": kwargs.get("name_contains", missing),
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
                response_type="SqlTuningSetCollection",
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
                response_type="SqlTuningSetCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def start_sql_tuning_task(self, managed_database_id, start_sql_tuning_task_details, **kwargs):
        """
        Starts a SQL tuning task for a given set of SQL statements from the active session history top SQL statements.


        :param str managed_database_id: (required)
            The `OCID`__ of the Managed Database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.database_management.models.StartSqlTuningTaskDetails start_sql_tuning_task_details: (required)
            The detailed inputs required to start a SQL tuning task.

        :param str opc_request_id: (optional)
            The client request ID for tracing.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database_management.models.SqlTuningTaskReturn`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/databasemanagement/start_sql_tuning_task.py.html>`__ to see an example of how to use start_sql_tuning_task API.
        """
        resource_path = "/managedDatabases/{managedDatabaseId}/actions/startSqlTuningTask"
        method = "POST"
        operation_name = "start_sql_tuning_task"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/database-management/20201101/ManagedDatabase/StartSqlTuningTask"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "start_sql_tuning_task got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "managedDatabaseId": managed_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
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
                header_params=header_params,
                body=start_sql_tuning_task_details,
                response_type="SqlTuningTaskReturn",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=start_sql_tuning_task_details,
                response_type="SqlTuningTaskReturn",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
