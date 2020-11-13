# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.
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
            'timeout': kwargs.get('timeout'),
            'base_path': '/20200630',
            'service_endpoint_template': 'https://operationsinsights.{region}.oci.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False)
        }
        self.base_client = BaseClient("operations_insights", config, signer, opsi_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')

    def ingest_sql_bucket(self, compartment_id, database_id, ingest_sql_bucket_details, **kwargs):
        """
        The sqlbucket endpoint takes in a JSON payload, persists it in Operations Insights ingest pipeline.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str database_id: (required)
            Required `OCID`__ of the database.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.opsi.models.IngestSqlBucketDetails ingest_sql_bucket_details: (required)
            Collection of SQL bucket objects for a particular database.

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
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.IngestSqlBucketResponseDetails`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databaseInsights/actions/ingestSqlBucket"
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
                "ingest_sql_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": database_id
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

    def ingest_sql_plan_lines(self, compartment_id, database_id, ingest_sql_plan_lines_details, **kwargs):
        """
        The SqlPlanLines endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str database_id: (required)
            Required `OCID`__ of the database.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.opsi.models.IngestSqlPlanLinesDetails ingest_sql_plan_lines_details: (required)
            Collection of SQL plan line objects for a particular database.

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
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.IngestSqlPlanLinesResponseDetails`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databaseInsights/actions/ingestSqlPlanLines"
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
                "ingest_sql_plan_lines got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": database_id
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

    def ingest_sql_text(self, compartment_id, database_id, ingest_sql_text_details, **kwargs):
        """
        The SqlText endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline.
        Disclaimer: SQL text being uploaded explicitly via APIs is not masked. Any sensitive literals contained in the sqlFullText column should be masked prior to ingestion.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str database_id: (required)
            Required `OCID`__ of the database.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.opsi.models.IngestSqlTextDetails ingest_sql_text_details: (required)
            Collection of SQL text objects for a particular database.

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
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.IngestSqlTextResponseDetails`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databaseInsights/actions/ingestSqlText"
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
                "ingest_sql_text got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": database_id
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

    def list_database_insights(self, compartment_id, **kwargs):
        """
        Lists database insight resources


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__.

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
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.DatabaseInsightsCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databaseInsights"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
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

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D"]
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
            "compartmentId": compartment_id,
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

    def list_sql_plans(self, compartment_id, database_id, sql_identifier, plan_hash, **kwargs):
        """
        Query SQL Warehouse to list the plan xml for a given SQL execution plan. This returns a SqlPlanCollection object, but is currently limited to a single plan.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str database_id: (required)
            Required `OCID`__ of the database.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str sql_identifier: (required)
            Unique SQL_ID for a SQL Statement.
            Example: `6rgjh9bjmy2s7`

        :param oci.opsi.models.list[int] plan_hash: (required)
            Unique plan hash for a SQL Plan of a particular SQL Statement.
            Example: `9820154385`

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
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlPlanCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databaseInsights/sqlPlans"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_sql_plans got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": database_id,
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
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlSearchCollection`
        :rtype: :class:`~oci.response.Response`
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
            Optional list of database `OCIDs`__.

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
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlTextCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databaseInsights/sqlTexts"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "database_id",
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

    def summarize_database_insight_resource_capacity_trend(self, compartment_id, resource_metric, **kwargs):
        """
        Returns response with time series data (endTimestamp, capacity, baseCapacity) for the time period specified.
        The maximum time range for analysis is 2 years, hence this is intentionally not paginated.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU and STORAGE.

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
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__.

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

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection`
        :rtype: :class:`~oci.response.Response`
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
            "utilization_level",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_database_insight_resource_capacity_trend got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D"]
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
            Supported values are CPU and STORAGE.

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
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__.

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
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceForecastTrendAggregation`
        :rtype: :class:`~oci.response.Response`
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
                "summarize_database_insight_resource_forecast_trend got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D"]
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
            Supported values are CPU and STORAGE.

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
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__.

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

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceStatisticsAggregationCollection`
        :rtype: :class:`~oci.response.Response`
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
                "summarize_database_insight_resource_statistics got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D"]
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
            Supported values are CPU and STORAGE.

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
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__.

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
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceUsageAggregation`
        :rtype: :class:`~oci.response.Response`
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
            "page",
            "percentile",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_database_insight_resource_usage got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D"]
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
            Supported values are CPU and STORAGE.

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
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__.

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
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceUsageTrendAggregationCollection`
        :rtype: :class:`~oci.response.Response`
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
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D"]
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
            Supported values are CPU and STORAGE.

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
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__.

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
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceUtilizationInsightAggregation`
        :rtype: :class:`~oci.response.Response`
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
            "forecast_days",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_database_insight_resource_utilization_insight got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D"]
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

    def summarize_sql_insights(self, compartment_id, **kwargs):
        """
        Query SQL Warehouse to get the performance insights for SQLs taking greater than X% database time for a given time period across the given databases or database types.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__.

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
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlInsightAggregationCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databaseInsights/sqlInsights"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "database_type",
            "database_id",
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
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
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

    def summarize_sql_plan_insights(self, compartment_id, database_id, sql_identifier, **kwargs):
        """
        Query SQL Warehouse to get the performance insights on the execution plans for a given SQL for a given time period.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str database_id: (required)
            Required `OCID`__ of the database.

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
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlPlanInsightAggregationCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databaseInsights/sqlPlanInsights"
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
                "summarize_sql_plan_insights got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": database_id,
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

    def summarize_sql_response_time_distributions(self, compartment_id, database_id, sql_identifier, **kwargs):
        """
        Query SQL Warehouse to summarize the response time distribution of query executions for a given SQL for a given time period.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str database_id: (required)
            Required `OCID`__ of the database.

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
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlResponseTimeDistributionAggregationCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databaseInsights/sqlResponseTimeDistributions"
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
                "summarize_sql_response_time_distributions got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": database_id,
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
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__.

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

            Allowed values are: "DEGRADING", "VARIANT", "INEFFICIENT", "CHANGING_PLANS", "DEGRADING_VARIANT", "DEGRADING_INEFFICIENT", "DEGRADING_CHANGING_PLANS", "DEGRADING_INCREASING_IO", "DEGRADING_INCREASING_CPU", "DEGRADING_INCREASING_INEFFICIENT_WAIT", "DEGRADING_CHANGING_PLANS_AND_INCREASING_IO", "DEGRADING_CHANGING_PLANS_AND_INCREASING_CPU", "DEGRADING_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT", "VARIANT_INEFFICIENT", "VARIANT_CHANGING_PLANS", "VARIANT_INCREASING_IO", "VARIANT_INCREASING_CPU", "VARIANT_INCREASING_INEFFICIENT_WAIT", "VARIANT_CHANGING_PLANS_AND_INCREASING_IO", "VARIANT_CHANGING_PLANS_AND_INCREASING_CPU", "VARIANT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT", "INEFFICIENT_CHANGING_PLANS", "INEFFICIENT_INCREASING_INEFFICIENT_WAIT", "INEFFICIENT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlStatisticAggregationCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databaseInsights/sqlStatistics"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "database_type",
            "database_id",
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
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D"]
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
            category_allowed_values = ["DEGRADING", "VARIANT", "INEFFICIENT", "CHANGING_PLANS", "DEGRADING_VARIANT", "DEGRADING_INEFFICIENT", "DEGRADING_CHANGING_PLANS", "DEGRADING_INCREASING_IO", "DEGRADING_INCREASING_CPU", "DEGRADING_INCREASING_INEFFICIENT_WAIT", "DEGRADING_CHANGING_PLANS_AND_INCREASING_IO", "DEGRADING_CHANGING_PLANS_AND_INCREASING_CPU", "DEGRADING_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT", "VARIANT_INEFFICIENT", "VARIANT_CHANGING_PLANS", "VARIANT_INCREASING_IO", "VARIANT_INCREASING_CPU", "VARIANT_INCREASING_INEFFICIENT_WAIT", "VARIANT_CHANGING_PLANS_AND_INCREASING_IO", "VARIANT_CHANGING_PLANS_AND_INCREASING_CPU", "VARIANT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT", "INEFFICIENT_CHANGING_PLANS", "INEFFICIENT_INCREASING_INEFFICIENT_WAIT", "INEFFICIENT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT"]
            for category_item in kwargs['category']:
                if category_item not in category_allowed_values:
                    raise ValueError(
                        "Invalid value for `category`, must be one of {0}".format(category_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
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
            Optional list of database `OCIDs`__.

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
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlStatisticsTimeSeriesAggregationCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databaseInsights/sqlStatisticsTimeSeries"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "database_id",
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

    def summarize_sql_statistics_time_series_by_plan(self, compartment_id, database_id, sql_identifier, **kwargs):
        """
        Query SQL Warehouse to get the performance statistics time series for a given SQL by execution plans for a given time period.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str database_id: (required)
            Required `OCID`__ of the database.

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
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlStatisticsTimeSeriesByPlanAggregationCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databaseInsights/sqlStatisticsTimeSeriesByPlan"
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
                "summarize_sql_statistics_time_series_by_plan got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": database_id,
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
