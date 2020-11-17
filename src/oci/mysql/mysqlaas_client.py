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
from .models import mysql_type_mapping
missing = Sentinel("Missing")


class MysqlaasClient(object):
    """
    The API for the MySQL Database Service
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
            'base_path': '/20190415',
            'service_endpoint_template': 'https://mysql.{region}.ocp.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False)
        }
        self.base_client = BaseClient("mysqlaas", config, signer, mysql_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')

    def create_configuration(self, create_configuration_details, **kwargs):
        """
        Creates a new Configuration.


        :param oci.mysql.models.CreateConfigurationDetails create_configuration_details: (required)
            Request to create a Configuration.

        :param str opc_request_id: (optional)
            Customer-defined unique identifier for the request. If you need to
            contact Oracle about a specific request, please provide the request
            ID that you supplied in this header with the request.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated before
            then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original
            creation request may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.mysql.models.Configuration`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/configurations"
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
                "create_configuration got unknown kwargs: {!r}".format(extra_kwargs))

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
                body=create_configuration_details,
                response_type="Configuration")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_configuration_details,
                response_type="Configuration")

    def delete_configuration(self, configuration_id, **kwargs):
        """
        Deletes a Configuration.
        The Configuration must not be in use by any DB Systems.


        :param str configuration_id: (required)
            The OCID of the Configuration.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `If-Match` header to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param str opc_request_id: (optional)
            Customer-defined unique identifier for the request. If you need to
            contact Oracle about a specific request, please provide the request
            ID that you supplied in this header with the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/configurations/{configurationId}"
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
                "delete_configuration got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "configurationId": configuration_id
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

    def get_configuration(self, configuration_id, **kwargs):
        """
        Get the full details of the specified Configuration, including the list of MySQL Variables and their values.


        :param str configuration_id: (required)
            The OCID of the Configuration.

        :param str opc_request_id: (optional)
            Customer-defined unique identifier for the request. If you need to
            contact Oracle about a specific request, please provide the request
            ID that you supplied in this header with the request.

        :param str if_none_match: (optional)
            For conditional requests. In the GET call for a resource, set the
            `If-None-Match` header to the value of the ETag from a previous GET (or
            POST or PUT) response for that resource. The server will return with
            either a 304 Not Modified response if the resource has not changed, or a
            200 OK response with the updated representation.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.mysql.models.Configuration`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/configurations/{configurationId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "if_none_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_configuration got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "configurationId": configuration_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-none-match": kwargs.get("if_none_match", missing)
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
                response_type="Configuration")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Configuration")

    def list_configurations(self, compartment_id, **kwargs):
        """
        Lists the Configurations available when creating a DB System.

        This may include DEFAULT configurations per Shape and CUSTOM configurations.

        The default sort order is a multi-part sort by:
          - shapeName, ascending
          - DEFAULT-before-CUSTOM
          - displayName ascending


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Customer-defined unique identifier for the request. If you need to
            contact Oracle about a specific request, please provide the request
            ID that you supplied in this header with the request.

        :param str configuration_id: (optional)
            The requested Configuration instance.

        :param str lifecycle_state: (optional)
            Configuration Lifecycle State

            Allowed values are: "ACTIVE", "DELETED"

        :param list[str] type: (optional)
            The requested Configuration types.

            Allowed values are: "DEFAULT", "CUSTOM"

        :param str display_name: (optional)
            A filter to return only the resource matching the given display name exactly.

        :param str shape_name: (optional)
            The requested Shape name.

        :param str sort_by: (optional)
            The field to sort by. Only one sort order may be provided. Time fields are default ordered as descending. Display name is default ordered as ascending.

            Allowed values are: "displayName", "shapeName", "timeCreated", "timeUpdated"

        :param str sort_order: (optional)
            The sort order to use (ASC or DESC).

            Allowed values are: "ASC", "DESC"

        :param int limit: (optional)
            The maximum number of items to return in a paginated list call. For information about pagination, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/#API/Concepts/usingapi.htm#List_Pagination

        :param str page: (optional)
            The value of the `opc-next-page` or `opc-prev-page` response header from
            the previous list call. For information about pagination, see `List
            Pagination`__.

            __ https://docs.cloud.oracle.com/#API/Concepts/usingapi.htm#List_Pagination

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.mysql.models.ConfigurationSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/configurations"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "configuration_id",
            "lifecycle_state",
            "type",
            "display_name",
            "shape_name",
            "sort_by",
            "sort_order",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_configurations got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["ACTIVE", "DELETED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'type' in kwargs:
            type_allowed_values = ["DEFAULT", "CUSTOM"]
            for type_item in kwargs['type']:
                if type_item not in type_allowed_values:
                    raise ValueError(
                        "Invalid value for `type`, must be one of {0}".format(type_allowed_values)
                    )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["displayName", "shapeName", "timeCreated", "timeUpdated"]
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
            "configurationId": kwargs.get("configuration_id", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "type": self.base_client.generate_collection_format_param(kwargs.get("type", missing), 'multi'),
            "displayName": kwargs.get("display_name", missing),
            "shapeName": kwargs.get("shape_name", missing),
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
                response_type="list[ConfigurationSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ConfigurationSummary]")

    def list_shapes(self, compartment_id, **kwargs):
        """
        Gets a list of the shapes you can use to create a new MySQL DB System.
        The shape determines the resources allocated to the DB System:
        CPU cores and memory for VM shapes; CPU cores, memory and
        storage for non-VM (or bare metal) shapes.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Customer-defined unique identifier for the request. If you need to
            contact Oracle about a specific request, please provide the request
            ID that you supplied in this header with the request.

        :param list[str] is_supported_for: (optional)
            Return shapes that are supported by the service feature.

            Allowed values are: "DBSYSTEM", "ANALYTICSCLUSTER"

        :param str availability_domain: (optional)
            The name of the Availability Domain.

        :param str name: (optional)
            Name

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.mysql.models.ShapeSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/shapes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "is_supported_for",
            "availability_domain",
            "name"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_shapes got unknown kwargs: {!r}".format(extra_kwargs))

        if 'is_supported_for' in kwargs:
            is_supported_for_allowed_values = ["DBSYSTEM", "ANALYTICSCLUSTER"]
            for is_supported_for_item in kwargs['is_supported_for']:
                if is_supported_for_item not in is_supported_for_allowed_values:
                    raise ValueError(
                        "Invalid value for `is_supported_for`, must be one of {0}".format(is_supported_for_allowed_values)
                    )

        query_params = {
            "isSupportedFor": self.base_client.generate_collection_format_param(kwargs.get("is_supported_for", missing), 'multi'),
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "compartmentId": compartment_id,
            "name": kwargs.get("name", missing)
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
                response_type="list[ShapeSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ShapeSummary]")

    def list_versions(self, compartment_id, **kwargs):
        """
        Get a list of supported and available MySQL database major versions.

        The list is sorted by version family.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Customer-defined unique identifier for the request. If you need to
            contact Oracle about a specific request, please provide the request
            ID that you supplied in this header with the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.mysql.models.VersionSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/versions"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_versions got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id
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
                response_type="list[VersionSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VersionSummary]")

    def update_configuration(self, configuration_id, update_configuration_details, **kwargs):
        """
        Updates the Configuration details.


        :param str configuration_id: (required)
            The OCID of the Configuration.

        :param oci.mysql.models.UpdateConfigurationDetails update_configuration_details: (required)
            Request to update a Configuration.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `If-Match` header to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param str opc_request_id: (optional)
            Customer-defined unique identifier for the request. If you need to
            contact Oracle about a specific request, please provide the request
            ID that you supplied in this header with the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.mysql.models.Configuration`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/configurations/{configurationId}"
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
                "update_configuration got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "configurationId": configuration_id
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
                body=update_configuration_details,
                response_type="Configuration")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_configuration_details,
                response_type="Configuration")
