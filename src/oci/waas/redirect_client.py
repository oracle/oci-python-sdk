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
from .models import waas_type_mapping
missing = Sentinel("Missing")


class RedirectClient(object):
    """
    OCI Web Application Acceleration and Security Services
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
            'base_path': '/20181116',
            'service_endpoint_template': 'https://waas.{region}.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False)
        }
        self.base_client = BaseClient("redirect", config, signer, waas_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')

    def change_http_redirect_compartment(self, http_redirect_id, change_http_redirect_compartment_details, **kwargs):
        """
        Moves HTTP Redirect into a different compartment. When provided, If-Match is checked against ETag values of the WAAS policy.


        :param str http_redirect_id: (required)
            The `OCID`__ of the HTTP Redirect.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ChangeHttpRedirectCompartmentDetails change_http_redirect_compartment_details: (required)

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/httpRedirects/{httpRedirectId}/actions/changeCompartment"
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
                "change_http_redirect_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "httpRedirectId": http_redirect_id
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
                body=change_http_redirect_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_http_redirect_compartment_details)

    def create_http_redirect(self, create_http_redirect_details, **kwargs):
        """
        Creates a new HTTP Redirect on the WAF edge.


        :param CreateHttpRedirectDetails create_http_redirect_details: (required)
            The details of the HTTP Redirect.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/httpRedirects"
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
                "create_http_redirect got unknown kwargs: {!r}".format(extra_kwargs))

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
                body=create_http_redirect_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_http_redirect_details)

    def delete_http_redirect(self, http_redirect_id, **kwargs):
        """
        Deletes a redirect.


        :param str http_redirect_id: (required)
            The `OCID`__ of the HTTP Redirect.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/httpRedirects/{httpRedirectId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_http_redirect got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "httpRedirectId": http_redirect_id
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

    def get_http_redirect(self, http_redirect_id, **kwargs):
        """
        Gets the details of a HTTP Redirect.


        :param str http_redirect_id: (required)
            The `OCID`__ of the HTTP Redirect.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.HttpRedirect`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/httpRedirects/{httpRedirectId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_http_redirect got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "httpRedirectId": http_redirect_id
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
                response_type="HttpRedirect")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="HttpRedirect")

    def list_http_redirects(self, compartment_id, **kwargs):
        """
        Gets a list of HTTP Redirects.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment. This number is generated when the compartment is created.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param str sort_order: (optional)
            The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort the results of the List query.

            Allowed values are: "id", "domain", "target", "displayName"

        :param list[str] id: (optional)
            Filter redirects using a list of redirect OCIDs.

        :param list[str] display_name: (optional)
            Filter redirects using a display name.

        :param list[str] lifecycle_state: (optional)
            Filter redirects using a list of lifecycle states.

            Allowed values are: "CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"

        :param datetime time_created_greater_than_or_equal_to: (optional)
            A filter that matches redirects created on or after the specified date and time.

        :param datetime time_created_less_than: (optional)
            A filter that matches redirects created before the specified date-time. Default to 1 day before now.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.HttpRedirectSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/httpRedirects"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "id",
            "display_name",
            "lifecycle_state",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_http_redirects got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["id", "domain", "target", "displayName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]
            for lifecycle_state_item in kwargs['lifecycle_state']:
                if lifecycle_state_item not in lifecycle_state_allowed_values:
                    raise ValueError(
                        "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "displayName": self.base_client.generate_collection_format_param(kwargs.get("display_name", missing), 'multi'),
            "lifecycleState": self.base_client.generate_collection_format_param(kwargs.get("lifecycle_state", missing), 'multi'),
            "timeCreatedGreaterThanOrEqualTo": kwargs.get("time_created_greater_than_or_equal_to", missing),
            "timeCreatedLessThan": kwargs.get("time_created_less_than", missing)
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
                response_type="list[HttpRedirectSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[HttpRedirectSummary]")

    def update_http_redirect(self, http_redirect_id, update_http_redirect_details, **kwargs):
        """
        Updates the details of a HTTP Redirect, including target and tags. Only the fields specified in the request body will be updated; all other properties will remain unchanged.


        :param str http_redirect_id: (required)
            The `OCID`__ of the HTTP Redirect.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateHttpRedirectDetails update_http_redirect_details: (required)
            The details of the HTTP Redirect to update.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/httpRedirects/{httpRedirectId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_http_redirect got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "httpRedirectId": http_redirect_id
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
                body=update_http_redirect_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_http_redirect_details)
