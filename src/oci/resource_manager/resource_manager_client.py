# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry  # noqa: F401
from oci.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel
from .models import resource_manager_type_mapping
missing = Sentinel("Missing")


class ResourceManagerClient(object):
    """
    API for the Resource Manager service. Use this API to install, configure, and manage resources via the "infrastructure-as-code" model. For more information, see [Overview of Resource Manager](/iaas/Content/ResourceManager/Concepts/resourcemanager.htm).
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
            'base_path': '/20180917',
            'service_endpoint_template': 'https://resourcemanager.{region}.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False)
        }
        self.base_client = BaseClient("resource_manager", config, signer, resource_manager_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')

    def cancel_job(self, job_id, **kwargs):
        """
        Cancel a Job
        Indicates the intention to cancel the specified job.
        Cancellation of the job is not immediate, and may be delayed,
        or may not happen at all.


        :param str job_id: (required)
            The `OCID`__ of the job.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match`
            parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/jobs/{jobId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "cancel_job got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "jobId": job_id
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

    def change_stack_compartment(self, stack_id, change_stack_compartment_details, **kwargs):
        """
        Moves a Stack and it's associated Jobs into a different compartment. When provided, If-Match is checked against ETag values of the Stack.
        Moves a Stack and it's associated Jobs into a different compartment.


        :param str stack_id: (required)
            The `OCID`__ of the stack.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param ChangeStackCompartmentDetails change_stack_compartment_details: (required)
            Defines the properties of changeStackCompartment operation.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match`
            parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of retrying the same action. Retry tokens expire after
            24 hours, but can be invalidated before then due to conflicting operations. For example,
            if a resource has been deleted and purged from the system, then a retry of the original
            creation request may be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/stacks/{stackId}/actions/changeCompartment"
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
                "change_stack_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "stackId": stack_id
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
                body=change_stack_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_stack_compartment_details)

    def create_job(self, create_job_details, **kwargs):
        """
        Create a Job.
        Creates a job.


        :param CreateJobDetails create_job_details: (required)
            The properties for a request to create a job.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of retrying the same action. Retry tokens expire after
            24 hours, but can be invalidated before then due to conflicting operations. For example,
            if a resource has been deleted and purged from the system, then a retry of the original
            creation request may be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.resource_manager.models.Job`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/jobs"
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
                "create_job got unknown kwargs: {!r}".format(extra_kwargs))

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
                body=create_job_details,
                response_type="Job")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_job_details,
                response_type="Job")

    def create_stack(self, create_stack_details, **kwargs):
        """
        Creates a Stack.
        Creates a stack in the specified comparment.
        Specify the compartment using the compartment ID.
        For more information, see `Create a Stack`__.

        __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Tasks/usingconsole.htm#CreateStack


        :param CreateStackDetails create_stack_details: (required)
            The properties for creating a stack.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of retrying the same action. Retry tokens expire after
            24 hours, but can be invalidated before then due to conflicting operations. For example,
            if a resource has been deleted and purged from the system, then a retry of the original
            creation request may be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.resource_manager.models.Stack`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/stacks"
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
                "create_stack got unknown kwargs: {!r}".format(extra_kwargs))

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
                body=create_stack_details,
                response_type="Stack")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_stack_details,
                response_type="Stack")

    def delete_stack(self, stack_id, **kwargs):
        """
        Deletes a stack
        Deletes the specified stack object.


        :param str stack_id: (required)
            The `OCID`__ of the stack.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match`
            parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/stacks/{stackId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_stack got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "stackId": stack_id
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

    def get_job(self, job_id, **kwargs):
        """
        Get details of a specific job.
        Returns the specified job along with the job details.


        :param str job_id: (required)
            The `OCID`__ of the job.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.resource_manager.models.Job`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/jobs/{jobId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_job got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "jobId": job_id
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
                response_type="Job")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Job")

    def get_job_logs(self, job_id, **kwargs):
        """
        Gets log entries for a job
        Returns log entries for the specified job in JSON format.


        :param str job_id: (required)
            The `OCID`__ of the job.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param list[LogEntryType] type: (optional)
            A filter that returns only logs of a specified type.

        :param str level_greater_than_or_equal_to: (optional)
            A filter that returns only log entries that match a given severity level or greater.

            Allowed values are: "TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"

        :param str sort_order: (optional)
            The sort order, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param int limit: (optional)
            The number of items returned in a paginated `List` call. For information about pagination, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            The value of the `opc-next-page` response header from the preceding `List` call.
            For information about pagination, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param datetime timestamp_greater_than_or_equal_to: (optional)
            Time stamp specifying the lower time limit for which logs are returned in a query.

        :param datetime timestamp_less_than_or_equal_to: (optional)
            Time stamp specifying the upper time limit for which logs are returned in a query.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.resource_manager.models.LogEntry`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/jobs/{jobId}/logs"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "type",
            "level_greater_than_or_equal_to",
            "sort_order",
            "limit",
            "page",
            "timestamp_greater_than_or_equal_to",
            "timestamp_less_than_or_equal_to"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_job_logs got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "jobId": job_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'level_greater_than_or_equal_to' in kwargs:
            level_greater_than_or_equal_to_allowed_values = ["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"]
            if kwargs['level_greater_than_or_equal_to'] not in level_greater_than_or_equal_to_allowed_values:
                raise ValueError(
                    "Invalid value for `level_greater_than_or_equal_to`, must be one of {0}".format(level_greater_than_or_equal_to_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "type": self.base_client.generate_collection_format_param(kwargs.get("type", missing), 'multi'),
            "levelGreaterThanOrEqualTo": kwargs.get("level_greater_than_or_equal_to", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "timestampGreaterThanOrEqualTo": kwargs.get("timestamp_greater_than_or_equal_to", missing),
            "timestampLessThanOrEqualTo": kwargs.get("timestamp_less_than_or_equal_to", missing)
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
                response_type="list[LogEntry]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[LogEntry]")

    def get_job_logs_content(self, job_id, **kwargs):
        """
        Gets the raw logs for a job.
        Returns raw log file for the specified job in text format.
        Returns a maximum of 100,000 log entries.


        :param str job_id: (required)
            The `OCID`__ of the job.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type str
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/jobs/{jobId}/logs/content"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_job_logs_content got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "jobId": job_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "text/plain; charset=utf-8",
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
                response_type="str")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="str")

    def get_job_tf_config(self, job_id, **kwargs):
        """
        Get zipped Terraform configuration used for a specific job.
        Returns the Terraform configuration file for the specified job in .zip format.
        Returns an error if no zip file is found.


        :param str job_id: (required)
            The `OCID`__ of the job.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/jobs/{jobId}/tfConfig"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_job_tf_config got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "jobId": job_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/zip",
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
                response_type="stream")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream")

    def get_job_tf_state(self, job_id, **kwargs):
        """
        Get Terraform state output from a specified job.
        Returns the Terraform state for the specified job.


        :param str job_id: (required)
            The `OCID`__ of the job.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/jobs/{jobId}/tfState"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_job_tf_state got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "jobId": job_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/octet-stream",
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
                response_type="stream")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream")

    def get_stack(self, stack_id, **kwargs):
        """
        Gets a stack by ID.
        Gets a stack using the stack ID.


        :param str stack_id: (required)
            The `OCID`__ of the stack.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.resource_manager.models.Stack`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/stacks/{stackId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_stack got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "stackId": stack_id
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
                response_type="Stack")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Stack")

    def get_stack_tf_config(self, stack_id, **kwargs):
        """
        Gets the stack's zipped Terraform configuration
        Returns the Terraform configuration file in .zip format for the specified stack.
        Returns an error if no zip file is found.


        :param str stack_id: (required)
            The `OCID`__ of the stack.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/stacks/{stackId}/tfConfig"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_stack_tf_config got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "stackId": stack_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/zip",
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
                response_type="stream")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream")

    def get_stack_tf_state(self, stack_id, **kwargs):
        """
        Get Terraform state of the specified stack.
        Returns the Terraform state for the specified stack.


        :param str stack_id: (required)
            The `OCID`__ of the stack.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/stacks/{stackId}/tfState"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_stack_tf_state got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "stackId": stack_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/octet-stream",
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
                response_type="stream")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream")

    def get_work_request(self, work_request_id, **kwargs):
        """
        Get Work Request
        Return the given work request.


        :param str work_request_id: (required)
            The `OCID`__ of the work request.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.resource_manager.models.WorkRequest`
        :rtype: :class:`~oci.response.Response`
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

    def list_jobs(self, **kwargs):
        """
        List all jobs related to a stack or compartment. By default, the list is ordered by time created.\nYou can alter the ordering by using `SortByQueryParam` and `SortOrderQueryParam`.\n
        Returns a list of jobs in a stack or compartment, ordered by time created.

        - To list all jobs in a stack, provide the stack `OCID`__.
        - To list all jobs in a compartment, provide the compartment `OCID`__.
        - To return a specific job, provide the job `OCID`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str compartment_id: (optional)
            The compartment `OCID`__ on which to filter.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str stack_id: (optional)
            The stack `OCID`__ on which to filter.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            The `OCID`__ on which to query for jobs.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str lifecycle_state: (optional)
            A filter that returns all resources that match the specified lifecycle state.
            The state value is case-insensitive.

            Allowable values:
            - ACCEPTED
            - IN_PROGRESS
            - FAILED
            - SUCCEEDED
            - CANCELING
            - CANCELED

            Allowed values are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"

        :param str display_name: (optional)
            Display name on which to query.

        :param str sort_by: (optional)
            Specifies the field on which to sort.
            By default, `TIMECREATED` is ordered descending.
            By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param int limit: (optional)
            The number of items returned in a paginated `List` call. For information about pagination, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            The value of the `opc-next-page` response header from the preceding `List` call.
            For information about pagination, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.resource_manager.models.JobSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/jobs"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "compartment_id",
            "stack_id",
            "id",
            "lifecycle_state",
            "display_name",
            "sort_by",
            "sort_order",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_jobs got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
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
            "compartmentId": kwargs.get("compartment_id", missing),
            "stackId": kwargs.get("stack_id", missing),
            "id": kwargs.get("id", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
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
                query_params=query_params,
                header_params=header_params,
                response_type="list[JobSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[JobSummary]")

    def list_stacks(self, **kwargs):
        """
        Returns a stack or list of stacks.
        Returns a list of stacks.
        - If called using the compartment ID, returns all stacks in the specified compartment.
        - If called using the stack ID, returns the specified stack.


        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str compartment_id: (optional)
            The compartment `OCID`__ on which to filter.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            The `OCID`__ on which to query for a stack.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str lifecycle_state: (optional)
            A filter that returns only those resources that match the specified
            lifecycle state. The state value is case-insensitive.

            Allowable values:
            - CREATING
            - ACTIVE
            - DELETING
            - DELETED

            Allowed values are: "CREATING", "ACTIVE", "DELETING", "DELETED"

        :param str display_name: (optional)
            Display name on which to query.

        :param str sort_by: (optional)
            Specifies the field on which to sort.
            By default, `TIMECREATED` is ordered descending.
            By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param int limit: (optional)
            The number of items returned in a paginated `List` call. For information about pagination, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            The value of the `opc-next-page` response header from the preceding `List` call.
            For information about pagination, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.resource_manager.models.StackSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/stacks"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "compartment_id",
            "id",
            "lifecycle_state",
            "display_name",
            "sort_by",
            "sort_order",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_stacks got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
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
            "compartmentId": kwargs.get("compartment_id", missing),
            "id": kwargs.get("id", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
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
                query_params=query_params,
                header_params=header_params,
                response_type="list[StackSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[StackSummary]")

    def list_terraform_versions(self, **kwargs):
        """
        Lists supported Terraform versions.
        Returns a list of supported Terraform versions for use with stacks.


        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str compartment_id: (optional)
            The compartment `OCID`__ on which to filter.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.resource_manager.models.TerraformVersionCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/terraformVersions"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_terraform_versions got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing)
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
                response_type="TerraformVersionCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="TerraformVersionCollection")

    def list_work_request_errors(self, work_request_id, **kwargs):
        """
        Lists work request errors
        Return a (paginated) list of errors for a given work request.


        :param str work_request_id: (required)
            The `OCID`__ of the work request.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str compartment_id: (optional)
            The compartment `OCID`__ on which to filter.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The number of items returned in a paginated `List` call. For information about pagination, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            The value of the `opc-next-page` response header from the preceding `List` call.
            For information about pagination, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.resource_manager.models.WorkRequestError`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workRequests/{workRequestId}/errors"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "compartment_id",
            "limit",
            "page",
            "sort_order",
            "opc_request_id"
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

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestError]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestError]")

    def list_work_request_logs(self, work_request_id, **kwargs):
        """
        Lists work request logs
        Return a (paginated) list of logs for a given work request.


        :param str work_request_id: (required)
            The `OCID`__ of the work request.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str compartment_id: (optional)
            The compartment `OCID`__ on which to filter.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The number of items returned in a paginated `List` call. For information about pagination, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            The value of the `opc-next-page` response header from the preceding `List` call.
            For information about pagination, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.resource_manager.models.WorkRequestLogEntry`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workRequests/{workRequestId}/logs"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "compartment_id",
            "limit",
            "page",
            "sort_order",
            "opc_request_id"
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

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestLogEntry]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestLogEntry]")

    def list_work_requests(self, compartment_id, **kwargs):
        """
        Lists work requests
        Lists the work requests in a given compartment or for a given resource.


        :param str compartment_id: (required)
            The compartment `OCID`__ on which to filter.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_id: (optional)
            The `OCID`__ of the resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The number of items returned in a paginated `List` call. For information about pagination, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            The value of the `opc-next-page` response header from the preceding `List` call.
            For information about pagination, see `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.resource_manager.models.WorkRequestSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workRequests"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "resource_id",
            "limit",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_work_requests got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "resourceId": kwargs.get("resource_id", missing),
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
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestSummary]")

    def update_job(self, job_id, update_job_details, **kwargs):
        """
        Update a Job.
        Updates the specified job.


        :param str job_id: (required)
            The `OCID`__ of the job.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param UpdateJobDetails update_job_details: (required)
            Updates properties for the specified job.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match`
            parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.resource_manager.models.Job`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/jobs/{jobId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_job got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "jobId": job_id
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
                body=update_job_details,
                response_type="Job")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_job_details,
                response_type="Job")

    def update_stack(self, stack_id, update_stack_details, **kwargs):
        """
        Updates a stack
        Updates the specified stack object.
        Use `UpdateStack` when you update your Terraform configuration
        and want your changes to be reflected in the execution plan.
        For more information, see `Update a Stack`__ and
        `Edit or Delete a Stack`__.

        __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Tasks/usingconsole.htm#UpdateStack
        __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Tasks/usingconsole.htm#EditStack


        :param str stack_id: (required)
            The `OCID`__ of the stack.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param UpdateStackDetails update_stack_details: (required)
            Updated information provided for the stack.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a
            particular request, please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match`
            parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.resource_manager.models.Stack`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/stacks/{stackId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_stack got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "stackId": stack_id
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
                body=update_stack_details,
                response_type="Stack")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_stack_details,
                response_type="Stack")
