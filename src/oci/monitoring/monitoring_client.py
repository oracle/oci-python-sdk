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
from oci.util import Sentinel
from .models import monitoring_type_mapping
missing = Sentinel("Missing")


class MonitoringClient(object):
    """
    Use the Monitoring API to manage metric queries and alarms for assessing the health, capacity, and performance of your cloud resources.
    Endpoints vary by operation. For PostMetric, use the `telemetry-ingestion` endpoints; for all other operations, use the `telemetry` endpoints.
    For information about monitoring, see [Monitoring Overview](/iaas/Content/Monitoring/Concepts/monitoringoverview.htm).
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
            'base_path': '/20180401',
            'service_endpoint_template': 'https://telemetry.{region}.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False)
        }
        self.base_client = BaseClient("monitoring", config, signer, monitoring_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')

    def change_alarm_compartment(self, alarm_id, change_alarm_compartment_details, **kwargs):
        """
        Moves an alarm into a different compartment within the same tenancy.

        For information about moving resources between compartments, see `Moving Resources Between Compartments`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str alarm_id: (required)
            The `OCID`__ of an alarm.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param ChangeAlarmCompartmentDetails change_alarm_compartment_details: (required)
            The configuration details for moving an alarm.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Customer part of the request identifier token. If you need to contact Oracle about a particular
            request, please provide the complete request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/alarms/{alarmId}/actions/changeCompartment"
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
                "change_alarm_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "alarmId": alarm_id
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
                body=change_alarm_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_alarm_compartment_details)

    def create_alarm(self, create_alarm_details, **kwargs):
        """
        Creates a new alarm in the specified compartment.
        For important limits information, see `Limits on Monitoring`__.

        This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations.
        Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests,
        or transactions, per second (TPS) for a given tenancy.

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Limits


        :param CreateAlarmDetails create_alarm_details: (required)
            Document for creating an alarm.

        :param str opc_request_id: (optional)
            Customer part of the request identifier token. If you need to contact Oracle about a particular
            request, please provide the complete request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations. For example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            might be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.monitoring.models.Alarm`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/alarms"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_alarm got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                header_params=header_params,
                body=create_alarm_details,
                response_type="Alarm")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_alarm_details,
                response_type="Alarm")

    def delete_alarm(self, alarm_id, **kwargs):
        """
        Deletes the specified alarm.
        For important limits information, see `Limits on Monitoring`__.

        This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations.
        Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests,
        or transactions, per second (TPS) for a given tenancy.

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Limits


        :param str alarm_id: (required)
            The `OCID`__ of an alarm.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Customer part of the request identifier token. If you need to contact Oracle about a particular
            request, please provide the complete request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/alarms/{alarmId}"
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
                "delete_alarm got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "alarmId": alarm_id
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

    def get_alarm(self, alarm_id, **kwargs):
        """
        Gets the specified alarm.
        For important limits information, see `Limits on Monitoring`__.

        This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations.
        Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests,
        or transactions, per second (TPS) for a given tenancy.

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Limits


        :param str alarm_id: (required)
            The `OCID`__ of an alarm.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Customer part of the request identifier token. If you need to contact Oracle about a particular
            request, please provide the complete request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.monitoring.models.Alarm`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/alarms/{alarmId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_alarm got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "alarmId": alarm_id
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
                response_type="Alarm")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Alarm")

    def get_alarm_history(self, alarm_id, **kwargs):
        """
        Get the history of the specified alarm.
        For important limits information, see `Limits on Monitoring`__.

        This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations.
        Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests,
        or transactions, per second (TPS) for a given tenancy.

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Limits


        :param str alarm_id: (required)
            The `OCID`__ of an alarm.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Customer part of the request identifier token. If you need to contact Oracle about a particular
            request, please provide the complete request ID.

        :param str alarm_historytype: (optional)
            The type of history entries to retrieve. State history (STATE_HISTORY) or state transition history (STATE_TRANSITION_HISTORY).
            If not specified, entries of both types are retrieved.

            Example: `STATE_HISTORY`

            Allowed values are: "STATE_HISTORY", "STATE_TRANSITION_HISTORY"

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            Default: 1000

            Example: 500

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param datetime timestamp_greater_than_or_equal_to: (optional)
            A filter to return only alarm history entries with timestamps occurring on or after the specified date and time. Format defined by RFC3339.

            Example: `2019-01-01T01:00:00.789Z`

        :param datetime timestamp_less_than: (optional)
            A filter to return only alarm history entries with timestamps occurring before the specified date and time. Format defined by RFC3339.

            Example: `2019-01-02T01:00:00.789Z`

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.monitoring.models.AlarmHistoryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/alarms/{alarmId}/history"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "alarm_historytype",
            "page",
            "limit",
            "timestamp_greater_than_or_equal_to",
            "timestamp_less_than"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_alarm_history got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "alarmId": alarm_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'alarm_historytype' in kwargs:
            alarm_historytype_allowed_values = ["STATE_HISTORY", "STATE_TRANSITION_HISTORY"]
            if kwargs['alarm_historytype'] not in alarm_historytype_allowed_values:
                raise ValueError(
                    "Invalid value for `alarm_historytype`, must be one of {0}".format(alarm_historytype_allowed_values)
                )

        query_params = {
            "alarmHistorytype": kwargs.get("alarm_historytype", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "timestampGreaterThanOrEqualTo": kwargs.get("timestamp_greater_than_or_equal_to", missing),
            "timestampLessThan": kwargs.get("timestamp_less_than", missing)
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
                response_type="AlarmHistoryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AlarmHistoryCollection")

    def list_alarms(self, compartment_id, **kwargs):
        """
        Lists the alarms for the specified compartment.
        For important limits information, see `Limits on Monitoring`__.

        This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations.
        Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests,
        or transactions, per second (TPS) for a given tenancy.

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Limits


        :param str compartment_id: (required)
            The `OCID`__ of the compartment containing the
            resources monitored by the metric that you are searching for. Use tenancyId to search in
            the root compartment.

            Example: `ocid1.compartment.oc1..exampleuniqueID`

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Customer part of the request identifier token. If you need to contact Oracle about a particular
            request, please provide the complete request ID.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            Default: 1000

            Example: 500

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.
            Use this filter to list an alarm by name. Alternatively, when you know the alarm OCID, use the GetAlarm operation.

        :param str lifecycle_state: (optional)
            A filter to return only alarms that match the given lifecycle state exactly. When not specified, only alarms in the ACTIVE lifecycle state are listed.

            Allowed values are: "ACTIVE", "DELETING", "DELETED"

        :param str sort_by: (optional)
            The field to use when sorting returned alarm definitions. Only one sorting level is provided.

            Example: `severity`

            Allowed values are: "displayName", "severity"

        :param str sort_order: (optional)
            The sort order to use when sorting returned alarm definitions. Ascending (ASC) or descending (DESC).

            Example: `ASC`

            Allowed values are: "ASC", "DESC"

        :param bool compartment_id_in_subtree: (optional)
            When true, returns resources from all compartments and subcompartments. The parameter can
            only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment).
            A true value requires the user to have tenancy-level permissions. If this requirement is not met,
            then the call is rejected. When false, returns resources from only the compartment specified in
            compartmentId. Default is false.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.monitoring.models.AlarmSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/alarms"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "page",
            "limit",
            "display_name",
            "lifecycle_state",
            "sort_by",
            "sort_order",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_alarms got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["ACTIVE", "DELETING", "DELETED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["displayName", "severity"]
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
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "displayName": kwargs.get("display_name", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
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
                response_type="list[AlarmSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AlarmSummary]")

    def list_alarms_status(self, compartment_id, **kwargs):
        """
        List the status of each alarm in the specified compartment.
        For important limits information, see `Limits on Monitoring`__.

        This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations.
        Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests,
        or transactions, per second (TPS) for a given tenancy.

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Limits


        :param str compartment_id: (required)
            The `OCID`__ of the compartment containing the
            resources monitored by the metric that you are searching for. Use tenancyId to search in
            the root compartment.

            Example: `ocid1.compartment.oc1..exampleuniqueID`

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Customer part of the request identifier token. If you need to contact Oracle about a particular
            request, please provide the complete request ID.

        :param bool compartment_id_in_subtree: (optional)
            When true, returns resources from all compartments and subcompartments. The parameter can
            only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment).
            A true value requires the user to have tenancy-level permissions. If this requirement is not met,
            then the call is rejected. When false, returns resources from only the compartment specified in
            compartmentId. Default is false.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            Default: 1000

            Example: 500

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.
            Use this filter to list an alarm by name. Alternatively, when you know the alarm OCID, use the GetAlarm operation.

        :param str sort_by: (optional)
            The field to use when sorting returned alarm definitions. Only one sorting level is provided.

            Example: `severity`

            Allowed values are: "displayName", "severity"

        :param str sort_order: (optional)
            The sort order to use when sorting returned alarm definitions. Ascending (ASC) or descending (DESC).

            Example: `ASC`

            Allowed values are: "ASC", "DESC"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.monitoring.models.AlarmStatusSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/alarms/status"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "compartment_id_in_subtree",
            "page",
            "limit",
            "display_name",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_alarms_status got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["displayName", "severity"]
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
            "compartmentId": compartment_id,
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "displayName": kwargs.get("display_name", missing),
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
                response_type="list[AlarmStatusSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AlarmStatusSummary]")

    def list_metrics(self, compartment_id, list_metrics_details, **kwargs):
        """
        Returns metric definitions that match the criteria specified in the request. Compartment OCID required.
        For information about metrics, see `Metrics Overview`__.
        For important limits information, see `Limits on Monitoring`__.

        Transactions Per Second (TPS) per-tenancy limit for this operation: 10.

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#MetricsOverview
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Limits


        :param str compartment_id: (required)
            The `OCID`__ of the compartment containing the
            resources monitored by the metric that you are searching for. Use tenancyId to search in
            the root compartment.

            Example: `ocid1.compartment.oc1..exampleuniqueID`

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param ListMetricsDetails list_metrics_details: (required)
            The dimensions used to filter metrics.

        :param str opc_request_id: (optional)
            Customer part of the request identifier token. If you need to contact Oracle about a particular
            request, please provide the complete request ID.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call.
            For important details about how pagination works, see `List Pagination`__.

            Default: 1000

            Example: 500

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param bool compartment_id_in_subtree: (optional)
            When true, returns resources from all compartments and subcompartments. The parameter can
            only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment).
            A true value requires the user to have tenancy-level permissions. If this requirement is not met,
            then the call is rejected. When false, returns resources from only the compartment specified in
            compartmentId. Default is false.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.monitoring.models.Metric`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/metrics/actions/listMetrics"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "page",
            "limit",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_metrics got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
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
                body=list_metrics_details,
                response_type="list[Metric]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=list_metrics_details,
                response_type="list[Metric]")

    def post_metric_data(self, post_metric_data_details, **kwargs):
        """
        Publishes raw metric data points to the Monitoring service.
        For more information about publishing metrics, see `Publishing Custom Metrics`__.
        For important limits information, see `Limits on Monitoring`__.

        Per-call limits information follows.

        * Dimensions per metric group*. Maximum: 20. Minimum: 1.
        * Unique metric streams*. Maximum: 50.
        * Transactions Per Second (TPS) per-tenancy limit for this operation: 50.

        *A metric group is the combination of a given metric, metric namespace, and tenancy for the purpose of determining limits.
        A dimension is a qualifier provided in a metric definition.
        A metric stream is an individual set of aggregated data for a metric, typically specific to a resource.
        For more information about metric-related concepts, see `Monitoring Concepts`__.

        The endpoints for this operation differ from other Monitoring operations. Replace the string `telemetry` with `telemetry-ingestion` in the endpoint, as in the following example:

        https://telemetry-ingestion.eu-frankfurt-1.oraclecloud.com

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Limits
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#concepts


        :param PostMetricDataDetails post_metric_data_details: (required)
            An array of metric objects containing raw metric data points to be posted to the Monitoring service.

        :param str opc_request_id: (optional)
            Customer part of the request identifier token. If you need to contact Oracle about a particular
            request, please provide the complete request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.monitoring.models.PostMetricDataResponseDetails`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/metrics"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "post_metric_data got unknown kwargs: {!r}".format(extra_kwargs))

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
                header_params=header_params,
                body=post_metric_data_details,
                response_type="PostMetricDataResponseDetails")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=post_metric_data_details,
                response_type="PostMetricDataResponseDetails")

    def remove_alarm_suppression(self, alarm_id, **kwargs):
        """
        Removes any existing suppression for the specified alarm.
        For important limits information, see `Limits on Monitoring`__.

        This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations.
        Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests,
        or transactions, per second (TPS) for a given tenancy.

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Limits


        :param str alarm_id: (required)
            The `OCID`__ of an alarm.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Customer part of the request identifier token. If you need to contact Oracle about a particular
            request, please provide the complete request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/alarms/{alarmId}/actions/removeSuppression"
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
                "remove_alarm_suppression got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "alarmId": alarm_id
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

    def summarize_metrics_data(self, compartment_id, summarize_metrics_data_details, **kwargs):
        """
        Returns aggregated data that match the criteria specified in the request. Compartment OCID required.
        For information on metric queries, see `Building Metric Queries`__.
        For important limits information, see `Limits on Monitoring`__.

        Transactions Per Second (TPS) per-tenancy limit for this operation: 10.

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Limits


        :param str compartment_id: (required)
            The `OCID`__ of the compartment containing the
            resources monitored by the metric that you are searching for. Use tenancyId to search in
            the root compartment.

            Example: `ocid1.compartment.oc1..exampleuniqueID`

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param SummarizeMetricsDataDetails summarize_metrics_data_details: (required)
            The dimensions used to filter for metrics.

        :param str opc_request_id: (optional)
            Customer part of the request identifier token. If you need to contact Oracle about a particular
            request, please provide the complete request ID.

        :param bool compartment_id_in_subtree: (optional)
            When true, returns resources from all compartments and subcompartments. The parameter can
            only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment).
            A true value requires the user to have tenancy-level permissions. If this requirement is not met,
            then the call is rejected. When false, returns resources from only the compartment specified in
            compartmentId. Default is false.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.monitoring.models.MetricData`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/metrics/actions/summarizeMetricsData"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_metrics_data got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
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
                body=summarize_metrics_data_details,
                response_type="list[MetricData]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=summarize_metrics_data_details,
                response_type="list[MetricData]")

    def update_alarm(self, alarm_id, update_alarm_details, **kwargs):
        """
        Updates the specified alarm.
        For important limits information, see `Limits on Monitoring`__.

        This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations.
        Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests,
        or transactions, per second (TPS) for a given tenancy.

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Limits


        :param str alarm_id: (required)
            The `OCID`__ of an alarm.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param UpdateAlarmDetails update_alarm_details: (required)
            Document for updating an alarm.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Customer part of the request identifier token. If you need to contact Oracle about a particular
            request, please provide the complete request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.monitoring.models.Alarm`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/alarms/{alarmId}"
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
                "update_alarm got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "alarmId": alarm_id
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
                body=update_alarm_details,
                response_type="Alarm")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_alarm_details,
                response_type="Alarm")
