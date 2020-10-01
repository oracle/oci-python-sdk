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
from .models import data_integration_type_mapping
missing = Sentinel("Missing")


class DataIntegrationClient(object):
    """
    Use the Data Integration Service APIs to perform common extract, load, and transform (ETL) tasks.
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
            'base_path': '/20200430',
            'service_endpoint_template': 'https://dataintegration.{region}.oci.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False)
        }
        self.base_client = BaseClient("data_integration", config, signer, data_integration_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')

    def change_compartment(self, workspace_id, change_compartment_details, **kwargs):
        """
        Moves a workspace to a specified compartment.


        :param str workspace_id: (required)
            The workspace ID.

        :param ChangeCompartmentDetails change_compartment_details: (required)
            The information needed to move a workspace to a specified compartment.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/actions/changeCompartment"
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
                "change_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
                body=change_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_compartment_details)

    def create_application(self, workspace_id, create_application_details, **kwargs):
        """
        Creates an application.


        :param str workspace_id: (required)
            The workspace ID.

        :param CreateApplicationDetails create_application_details: (required)
            The details needed to create an application.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Application`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications"
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
                "create_application got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
                body=create_application_details,
                response_type="Application")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_application_details,
                response_type="Application")

    def create_connection(self, workspace_id, create_connection_details, **kwargs):
        """
        Creates a connection under an existing data asset.


        :param str workspace_id: (required)
            The workspace ID.

        :param CreateConnectionDetails create_connection_details: (required)
            The information needed to create a connection.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Connection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/connections"
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
                "create_connection got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
                body=create_connection_details,
                response_type="Connection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_connection_details,
                response_type="Connection")

    def create_connection_validation(self, workspace_id, create_connection_validation_details, **kwargs):
        """
        Creates a connection validation.


        :param str workspace_id: (required)
            The workspace ID.

        :param CreateConnectionValidationDetails create_connection_validation_details: (required)
            The information needed to validate a connection.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.ConnectionValidation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/connectionValidations"
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
                "create_connection_validation got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
                body=create_connection_validation_details,
                response_type="ConnectionValidation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_connection_validation_details,
                response_type="ConnectionValidation")

    def create_data_asset(self, workspace_id, create_data_asset_details, **kwargs):
        """
        Creates a data asset with default connection.


        :param str workspace_id: (required)
            The workspace ID.

        :param CreateDataAssetDetails create_data_asset_details: (required)
            The information needed to create a data asset.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.DataAsset`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/dataAssets"
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
                "create_data_asset got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
                body=create_data_asset_details,
                response_type="DataAsset")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_data_asset_details,
                response_type="DataAsset")

    def create_data_flow(self, workspace_id, create_data_flow_details, **kwargs):
        """
        Creates a new data flow in a project or folder ready for performing data integrations.


        :param str workspace_id: (required)
            The workspace ID.

        :param CreateDataFlowDetails create_data_flow_details: (required)
            The details needed to create a new data flow.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.DataFlow`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/dataFlows"
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
                "create_data_flow got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
                body=create_data_flow_details,
                response_type="DataFlow")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_data_flow_details,
                response_type="DataFlow")

    def create_data_flow_validation(self, workspace_id, create_data_flow_validation_details, **kwargs):
        """
        Accepts the data flow definition in the request payload and creates a data flow validation.


        :param str workspace_id: (required)
            The workspace ID.

        :param CreateDataFlowValidationDetails create_data_flow_validation_details: (required)
            The information needed to create the data flow validation for the data flow object.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.DataFlowValidation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/dataFlowValidations"
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
                "create_data_flow_validation got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
                body=create_data_flow_validation_details,
                response_type="DataFlowValidation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_data_flow_validation_details,
                response_type="DataFlowValidation")

    def create_entity_shape(self, workspace_id, connection_key, schema_resource_name, create_entity_shape_details, **kwargs):
        """
        Creates the data entity shape using the shape from the data asset.


        :param str workspace_id: (required)
            The workspace ID.

        :param str connection_key: (required)
            The connection key.

        :param str schema_resource_name: (required)
            The schema resource name used for retrieving schemas.

        :param CreateEntityShapeDetails create_entity_shape_details: (required)
            The details needed to create the data entity shape.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.EntityShape`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/connections/{connectionKey}/schemas/{schemaResourceName}/entityShapes"
        method = "POST"

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
                "create_entity_shape got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "connectionKey": connection_key,
            "schemaResourceName": schema_resource_name
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
                body=create_entity_shape_details,
                response_type="EntityShape")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_entity_shape_details,
                response_type="EntityShape")

    def create_external_publication(self, workspace_id, task_key, create_external_publication_details, **kwargs):
        """
        Publish a DataFlow in a OCI DataFlow application.


        :param str workspace_id: (required)
            The workspace ID.

        :param str task_key: (required)
            The task key.

        :param CreateExternalPublicationDetails create_external_publication_details: (required)
            Details needed to publish a task to OCI DataFlow application.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.ExternalPublication`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/tasks/{taskKey}/externalPublications"
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
                "create_external_publication got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "taskKey": task_key
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
                body=create_external_publication_details,
                response_type="ExternalPublication")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_external_publication_details,
                response_type="ExternalPublication")

    def create_external_publication_validation(self, workspace_id, task_key, create_external_publication_validation_details, **kwargs):
        """
        Validates a specific task.


        :param str workspace_id: (required)
            The workspace ID.

        :param str task_key: (required)
            The task key.

        :param CreateExternalPublicationValidationDetails create_external_publication_validation_details: (required)
            The information needed to create a task validation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.ExternalPublicationValidation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/tasks/{taskKey}/externalPublicationValidations"
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
                "create_external_publication_validation got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "taskKey": task_key
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
                body=create_external_publication_validation_details,
                response_type="ExternalPublicationValidation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_external_publication_validation_details,
                response_type="ExternalPublicationValidation")

    def create_folder(self, workspace_id, create_folder_details, **kwargs):
        """
        Creates a folder in a project or in another folder, limited to two levels of folders. |
        Folders are used to organize your design-time resources, such as tasks or data flows.


        :param str workspace_id: (required)
            The workspace ID.

        :param CreateFolderDetails create_folder_details: (required)
            The details needed to create a folder.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Folder`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/folders"
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
                "create_folder got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
                body=create_folder_details,
                response_type="Folder")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_folder_details,
                response_type="Folder")

    def create_patch(self, workspace_id, application_key, create_patch_details, **kwargs):
        """
        Creates a patch in an application.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param CreatePatchDetails create_patch_details: (required)
            Detailed needed to create a patch in an application.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Patch`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/patches"
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
                "create_patch got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key
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
                body=create_patch_details,
                response_type="Patch")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_patch_details,
                response_type="Patch")

    def create_project(self, workspace_id, create_project_details, **kwargs):
        """
        Creates a project. Projects are organizational constructs within a workspace that you use to organize your design-time resources, such as tasks or data flows. Projects can be organized into folders.


        :param str workspace_id: (required)
            The workspace ID.

        :param CreateProjectDetails create_project_details: (required)
            The details needed to create a project in a workspace.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Project`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/projects"
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
                "create_project got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
                body=create_project_details,
                response_type="Project")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_project_details,
                response_type="Project")

    def create_task(self, workspace_id, create_task_details, **kwargs):
        """
        Creates a new task ready for performing data integrations. There are specialized types of tasks that include data loader and integration tasks.


        :param str workspace_id: (required)
            The workspace ID.

        :param CreateTaskDetails create_task_details: (required)
            The details needed to create a new task.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Task`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/tasks"
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
                "create_task got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
                body=create_task_details,
                response_type="Task")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_task_details,
                response_type="Task")

    def create_task_run(self, workspace_id, application_key, create_task_run_details, **kwargs):
        """
        Creates a data integration task run for the specified task.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param CreateTaskRunDetails create_task_run_details: (required)
            The details needed to create a task run.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.TaskRun`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/taskRuns"
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
                "create_task_run got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key
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
                body=create_task_run_details,
                response_type="TaskRun")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_task_run_details,
                response_type="TaskRun")

    def create_task_validation(self, workspace_id, create_task_validation_details, **kwargs):
        """
        Validates a specific task.


        :param str workspace_id: (required)
            The workspace ID.

        :param CreateTaskValidationDetails create_task_validation_details: (required)
            The information needed to create a task validation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.TaskValidation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/taskValidations"
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
                "create_task_validation got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
                body=create_task_validation_details,
                response_type="TaskValidation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_task_validation_details,
                response_type="TaskValidation")

    def create_workspace(self, create_workspace_details, **kwargs):
        """
        Creates a new Data Integration workspace ready for performing data integration tasks.


        :param CreateWorkspaceDetails create_workspace_details: (required)
            The information needed to create a new Data Integration workspace.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces"
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
                "create_workspace got unknown kwargs: {!r}".format(extra_kwargs))

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
                body=create_workspace_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_workspace_details)

    def delete_application(self, workspace_id, application_key, **kwargs):
        """
        Removes an application using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}"
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
                "delete_application got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key
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

    def delete_connection(self, workspace_id, connection_key, **kwargs):
        """
        Removes a connection using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str connection_key: (required)
            The connection key.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/connections/{connectionKey}"
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
                "delete_connection got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "connectionKey": connection_key
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

    def delete_connection_validation(self, workspace_id, connection_validation_key, **kwargs):
        """
        Deletes a connection validation.


        :param str workspace_id: (required)
            The workspace ID.

        :param str connection_validation_key: (required)
            The key of the connection validation.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/connectionValidations/{connectionValidationKey}"
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
                "delete_connection_validation got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "connectionValidationKey": connection_validation_key
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

    def delete_data_asset(self, workspace_id, data_asset_key, **kwargs):
        """
        Removes a data asset using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str data_asset_key: (required)
            The data asset key.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/dataAssets/{dataAssetKey}"
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
                "delete_data_asset got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "dataAssetKey": data_asset_key
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

    def delete_data_flow(self, workspace_id, data_flow_key, **kwargs):
        """
        Removes a data flow from a project or folder using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str data_flow_key: (required)
            The data flow key.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/dataFlows/{dataFlowKey}"
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
                "delete_data_flow got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "dataFlowKey": data_flow_key
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

    def delete_data_flow_validation(self, workspace_id, data_flow_validation_key, **kwargs):
        """
        Removes a data flow validation using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str data_flow_validation_key: (required)
            The key of the dataflow validation.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/dataFlowValidations/{dataFlowValidationKey}"
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
                "delete_data_flow_validation got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "dataFlowValidationKey": data_flow_validation_key
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

    def delete_external_publication(self, workspace_id, task_key, external_publications_key, **kwargs):
        """
        Removes a published object using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str task_key: (required)
            The task key.

        :param str external_publications_key: (required)
            The external published object key.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/tasks/{taskKey}/externalPublications/{externalPublicationsKey}"
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
                "delete_external_publication got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "taskKey": task_key,
            "externalPublicationsKey": external_publications_key
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

    def delete_external_publication_validation(self, workspace_id, task_key, external_publication_validation_key, **kwargs):
        """
        Removes a task validation using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str task_key: (required)
            The task key.

        :param str external_publication_validation_key: (required)
            The external published object key.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/tasks/{taskKey}/externalPublicationValidations/{externalPublicationValidationKey}"
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
                "delete_external_publication_validation got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "taskKey": task_key,
            "externalPublicationValidationKey": external_publication_validation_key
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

    def delete_folder(self, workspace_id, folder_key, **kwargs):
        """
        Removes a folder from a project using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str folder_key: (required)
            The folder key.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/folders/{folderKey}"
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
                "delete_folder got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "folderKey": folder_key
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

    def delete_patch(self, workspace_id, application_key, patch_key, **kwargs):
        """
        Removes a patch using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param str patch_key: (required)
            The patch key.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/patches/{patchKey}"
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
                "delete_patch got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key,
            "patchKey": patch_key
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

    def delete_project(self, workspace_id, project_key, **kwargs):
        """
        Removes a project from the workspace using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str project_key: (required)
            The project key.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/projects/{projectKey}"
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
                "delete_project got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "projectKey": project_key
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

    def delete_task(self, workspace_id, task_key, **kwargs):
        """
        Removes a task using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str task_key: (required)
            The task key.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/tasks/{taskKey}"
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
                "delete_task got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "taskKey": task_key
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

    def delete_task_run(self, workspace_id, application_key, task_run_key, **kwargs):
        """
        Deletes a task run using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param str task_run_key: (required)
            The task run key.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/taskRuns/{taskRunKey}"
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
                "delete_task_run got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key,
            "taskRunKey": task_run_key
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

    def delete_task_validation(self, workspace_id, task_validation_key, **kwargs):
        """
        Removes a task validation using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str task_validation_key: (required)
            The task validation key.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/taskValidations/{taskValidationKey}"
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
                "delete_task_validation got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "taskValidationKey": task_validation_key
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

    def delete_workspace(self, workspace_id, **kwargs):
        """
        Deletes a Data Integration workspace resource using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param int quiesce_timeout: (optional)
            Used to set the timeout for Data Integration to gracefully close down any running jobs before stopping the workspace.

        :param bool is_force_operation: (optional)
            Used to force close down the workspace.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "quiesce_timeout",
            "is_force_operation",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_workspace got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "quiesceTimeout": kwargs.get("quiesce_timeout", missing),
            "isForceOperation": kwargs.get("is_force_operation", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

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
                query_params=query_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)

    def get_application(self, workspace_id, application_key, **kwargs):
        """
        Retrieves an application using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Application`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_application got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key
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
                response_type="Application")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Application")

    def get_connection(self, workspace_id, connection_key, **kwargs):
        """
        Retrieves the connection details using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str connection_key: (required)
            The connection key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Connection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/connections/{connectionKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_connection got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "connectionKey": connection_key
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
                response_type="Connection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Connection")

    def get_connection_validation(self, workspace_id, connection_validation_key, **kwargs):
        """
        Retrieves a connection validation using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str connection_validation_key: (required)
            The key of the connection validation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.ConnectionValidation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/connectionValidations/{connectionValidationKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_connection_validation got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "connectionValidationKey": connection_validation_key
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
                response_type="ConnectionValidation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ConnectionValidation")

    def get_count_statistic(self, workspace_id, count_statistic_key, **kwargs):
        """
        Retrieves statistics on a workspace. It returns an object with an array of property values, such as the number of projects, |
               applications, data assets, and so on.


        :param str workspace_id: (required)
            The workspace ID.

        :param str count_statistic_key: (required)
            A unique key of the container object, such as workspace, project, and so on, to count statistics for. The statistics is fetched for the given key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.CountStatistic`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/countStatistics/{countStatisticKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_count_statistic got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "countStatisticKey": count_statistic_key
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
                response_type="CountStatistic")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="CountStatistic")

    def get_data_asset(self, workspace_id, data_asset_key, **kwargs):
        """
        Retrieves details of a data asset using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str data_asset_key: (required)
            The data asset key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.DataAsset`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/dataAssets/{dataAssetKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_data_asset got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "dataAssetKey": data_asset_key
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
                response_type="DataAsset")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DataAsset")

    def get_data_entity(self, workspace_id, connection_key, schema_resource_name, data_entity_key, **kwargs):
        """
        Retrieves the data entity details with the given name from live schema.


        :param str workspace_id: (required)
            The workspace ID.

        :param str connection_key: (required)
            The connection key.

        :param str schema_resource_name: (required)
            The schema resource name used for retrieving schemas.

        :param str data_entity_key: (required)
            The key of the data entity.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.DataEntity`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/connections/{connectionKey}/schemas/{schemaResourceName}/dataEntities/{dataEntityKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_data_entity got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "connectionKey": connection_key,
            "schemaResourceName": schema_resource_name,
            "dataEntityKey": data_entity_key
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
                response_type="DataEntity")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DataEntity")

    def get_data_flow(self, workspace_id, data_flow_key, **kwargs):
        """
        Retrieves a data flow using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str data_flow_key: (required)
            The data flow key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.DataFlow`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/dataFlows/{dataFlowKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_data_flow got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "dataFlowKey": data_flow_key
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
                response_type="DataFlow")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DataFlow")

    def get_data_flow_validation(self, workspace_id, data_flow_validation_key, **kwargs):
        """
        Retrieves a data flow validation using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str data_flow_validation_key: (required)
            The key of the dataflow validation.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.DataFlowValidation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/dataFlowValidations/{dataFlowValidationKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_data_flow_validation got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "dataFlowValidationKey": data_flow_validation_key
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
                response_type="DataFlowValidation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DataFlowValidation")

    def get_dependent_object(self, workspace_id, application_key, dependent_object_key, **kwargs):
        """
        Retrieves the details of a dependent object from an application.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param str dependent_object_key: (required)
            The dependent object key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.DependentObject`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/dependentObjects/{dependentObjectKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_dependent_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key,
            "dependentObjectKey": dependent_object_key
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
                response_type="DependentObject")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DependentObject")

    def get_external_publication(self, workspace_id, task_key, external_publications_key, **kwargs):
        """
        Retrieves a publshed object in an task using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str task_key: (required)
            The task key.

        :param str external_publications_key: (required)
            The external published object key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.ExternalPublication`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/tasks/{taskKey}/externalPublications/{externalPublicationsKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_external_publication got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "taskKey": task_key,
            "externalPublicationsKey": external_publications_key
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
                response_type="ExternalPublication")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ExternalPublication")

    def get_external_publication_validation(self, workspace_id, task_key, external_publication_validation_key, **kwargs):
        """
        Retrieves an external publication validation using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str task_key: (required)
            The task key.

        :param str external_publication_validation_key: (required)
            The external published object key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.ExternalPublicationValidation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/tasks/{taskKey}/externalPublicationValidations/{externalPublicationValidationKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_external_publication_validation got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "taskKey": task_key,
            "externalPublicationValidationKey": external_publication_validation_key
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
                response_type="ExternalPublicationValidation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ExternalPublicationValidation")

    def get_folder(self, workspace_id, folder_key, **kwargs):
        """
        Retrieves a folder using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str folder_key: (required)
            The folder key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Folder`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/folders/{folderKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_folder got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "folderKey": folder_key
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
                response_type="Folder")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Folder")

    def get_patch(self, workspace_id, application_key, patch_key, **kwargs):
        """
        Retrieves a patch in an application using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param str patch_key: (required)
            The patch key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Patch`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/patches/{patchKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_patch got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key,
            "patchKey": patch_key
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
                response_type="Patch")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Patch")

    def get_project(self, workspace_id, project_key, **kwargs):
        """
        Retrieves a project using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str project_key: (required)
            The project key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Project`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/projects/{projectKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_project got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "projectKey": project_key
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
                response_type="Project")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Project")

    def get_published_object(self, workspace_id, application_key, published_object_key, **kwargs):
        """
        Retrieves the details of a published object from an application.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param str published_object_key: (required)
            The published object key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str expand_references: (optional)
            Used to expand references of the object. If value is true, then all referenced objects are expanded. If value is false, then shallow objects are returned in place of references. Default is false. <br><br><B>Example:</B><br> <ul> <li><B>?expandReferences=true</B> returns all objects of type data loader task</li> </ul>

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.PublishedObject`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/publishedObjects/{publishedObjectKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "expand_references"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_published_object got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key,
            "publishedObjectKey": published_object_key
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "expandReferences": kwargs.get("expand_references", missing)
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
                response_type="PublishedObject")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="PublishedObject")

    def get_reference(self, workspace_id, application_key, reference_key, **kwargs):
        """
        Retrieves a reference in an application.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param str reference_key: (required)
            The reference key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Reference`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/references/{referenceKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_reference got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key,
            "referenceKey": reference_key
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
                response_type="Reference")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Reference")

    def get_schema(self, workspace_id, connection_key, schema_resource_name, **kwargs):
        """
        Retrieves a schema that can be accessed using the specified connection.


        :param str workspace_id: (required)
            The workspace ID.

        :param str connection_key: (required)
            The connection key.

        :param str schema_resource_name: (required)
            The schema resource name used for retrieving schemas.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Schema`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/connections/{connectionKey}/schemas/{schemaResourceName}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_schema got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "connectionKey": connection_key,
            "schemaResourceName": schema_resource_name
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
                response_type="Schema")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Schema")

    def get_task(self, workspace_id, task_key, **kwargs):
        """
        Retrieves a task using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str task_key: (required)
            The task key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Task`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/tasks/{taskKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_task got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "taskKey": task_key
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
                response_type="Task")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Task")

    def get_task_run(self, workspace_id, application_key, task_run_key, **kwargs):
        """
        Retrieves a task run using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param str task_run_key: (required)
            The task run key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.TaskRun`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/taskRuns/{taskRunKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_task_run got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key,
            "taskRunKey": task_run_key
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
                response_type="TaskRun")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="TaskRun")

    def get_task_validation(self, workspace_id, task_validation_key, **kwargs):
        """
        Retrieves a task validation using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str task_validation_key: (required)
            The task validation key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.TaskValidation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/taskValidations/{taskValidationKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_task_validation got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "taskValidationKey": task_validation_key
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
                response_type="TaskValidation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="TaskValidation")

    def get_work_request(self, work_request_id, **kwargs):
        """
        Retrieves the status of the work request with the given ID.


        :param str work_request_id: (required)
            The ID of the asynchronous work request to retrieve.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.WorkRequest`
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

    def get_workspace(self, workspace_id, **kwargs):
        """
        Retrieves a Data Integration workspace using the specified identifier.


        :param str workspace_id: (required)
            The workspace ID.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Workspace`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_workspace got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
                response_type="Workspace")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Workspace")

    def list_applications(self, workspace_id, **kwargs):
        """
        Retrieves a list of applications and provides options to filter the list.


        :param str workspace_id: (required)
            The workspace ID.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param list[str] identifier: (optional)
            Used to filter by the identifier of the published object.

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.ApplicationSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "name",
            "identifier",
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
                "list_applications got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "name": kwargs.get("name", missing),
            "identifier": self.base_client.generate_collection_format_param(kwargs.get("identifier", missing), 'multi'),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ApplicationSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ApplicationSummaryCollection")

    def list_connection_validations(self, workspace_id, **kwargs):
        """
        Retrieves a list of connection validations within the specified workspace.


        :param str workspace_id: (required)
            The workspace ID.

        :param str key: (optional)
            Used to filter by the key of the object.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param str identifier: (optional)
            Used to filter by the identifier of the object.

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.ConnectionValidationSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/connectionValidations"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "key",
            "name",
            "identifier",
            "fields",
            "page",
            "limit",
            "sort_by",
            "sort_order",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_connection_validations got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
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
            "key": kwargs.get("key", missing),
            "name": kwargs.get("name", missing),
            "identifier": kwargs.get("identifier", missing),
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
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
                response_type="ConnectionValidationSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ConnectionValidationSummaryCollection")

    def list_connections(self, workspace_id, data_asset_key, **kwargs):
        """
        Retrieves a list of all connections.


        :param str workspace_id: (required)
            The workspace ID.

        :param str data_asset_key: (required)
            Used to filter by the data asset key of the object.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param str type: (optional)
            Type of the object to filter the results with.

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.ConnectionSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/connections"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "name",
            "page",
            "limit",
            "fields",
            "type",
            "sort_by",
            "sort_order",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_connections got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
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
            "dataAssetKey": data_asset_key,
            "name": kwargs.get("name", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
            "type": kwargs.get("type", missing),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ConnectionSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ConnectionSummaryCollection")

    def list_data_assets(self, workspace_id, **kwargs):
        """
        Retrieves a list of all data asset summaries.


        :param str workspace_id: (required)
            The workspace ID.

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param str type: (optional)
            Type of the object to filter the results with.

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str name: (optional)
            Used to filter by the name of the object.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.DataAssetSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/dataAssets"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "page",
            "limit",
            "fields",
            "type",
            "sort_by",
            "sort_order",
            "name",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_data_assets got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
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
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
            "type": kwargs.get("type", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DataAssetSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DataAssetSummaryCollection")

    def list_data_entities(self, workspace_id, connection_key, schema_resource_name, **kwargs):
        """
        Lists a summary of data entities from the data asset using the specified connection.


        :param str workspace_id: (required)
            The workspace ID.

        :param str connection_key: (required)
            The connection key.

        :param str schema_resource_name: (required)
            The schema resource name used for retrieving schemas.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str type: (optional)
            Type of the object to filter the results with.

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.DataEntitySummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/connections/{connectionKey}/schemas/{schemaResourceName}/dataEntities"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "name",
            "page",
            "type",
            "limit",
            "fields",
            "sort_by",
            "sort_order",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_data_entities got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "connectionKey": connection_key,
            "schemaResourceName": schema_resource_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
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
            "page": kwargs.get("page", missing),
            "type": kwargs.get("type", missing),
            "limit": kwargs.get("limit", missing),
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DataEntitySummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DataEntitySummaryCollection")

    def list_data_flow_validations(self, workspace_id, **kwargs):
        """
        Retrieves a list of data flow validations within the specified workspace.


        :param str workspace_id: (required)
            The workspace ID.

        :param str key: (optional)
            Used to filter by the key of the object.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param str identifier: (optional)
            Used to filter by the identifier of the object.

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.DataFlowValidationSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/dataFlowValidations"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "key",
            "name",
            "identifier",
            "fields",
            "page",
            "limit",
            "sort_by",
            "sort_order",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_data_flow_validations got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
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
            "key": kwargs.get("key", missing),
            "name": kwargs.get("name", missing),
            "identifier": kwargs.get("identifier", missing),
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
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
                response_type="DataFlowValidationSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DataFlowValidationSummaryCollection")

    def list_data_flows(self, workspace_id, **kwargs):
        """
        Retrieves a list of data flows in a project or folder.


        :param str workspace_id: (required)
            The workspace ID.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str folder_id: (optional)
            Unique key of the folder.

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param list[str] identifier: (optional)
            Used to filter by the identifier of the object.

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.DataFlowSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/dataFlows"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "folder_id",
            "fields",
            "name",
            "identifier",
            "limit",
            "page",
            "sort_order",
            "sort_by"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_data_flows got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "folderId": kwargs.get("folder_id", missing),
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
            "name": kwargs.get("name", missing),
            "identifier": self.base_client.generate_collection_format_param(kwargs.get("identifier", missing), 'multi'),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DataFlowSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DataFlowSummaryCollection")

    def list_dependent_objects(self, workspace_id, application_key, **kwargs):
        """
        Retrieves a list of all dependent objects for a specific application.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param list[str] identifier: (optional)
            Used to filter by the identifier of the published object.

        :param list[str] type: (optional)
            Used to filter by the object type of the object.
            It can be suffixed with an optional filter operator InSubtree.
            For Data Integration APIs, a filter based on type Task is used.

        :param str type_in_subtree: (optional)
            Used in association with type parameter. If value is true,
            then type all sub types of the given type parameter is considered.
            If value is false, then sub types are not considered. Default is false.

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.DependentObjectSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/dependentObjects"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "fields",
            "name",
            "identifier",
            "type",
            "type_in_subtree",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_dependent_objects got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key
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
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
            "name": kwargs.get("name", missing),
            "identifier": self.base_client.generate_collection_format_param(kwargs.get("identifier", missing), 'multi'),
            "type": self.base_client.generate_collection_format_param(kwargs.get("type", missing), 'multi'),
            "typeInSubtree": kwargs.get("type_in_subtree", missing),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DependentObjectSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DependentObjectSummaryCollection")

    def list_external_publication_validations(self, workspace_id, task_key, **kwargs):
        """
        Retrieves a lists of external publication validations in a workspace and provides options to filter the list.


        :param str workspace_id: (required)
            The workspace ID.

        :param str task_key: (required)
            The task key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param list[str] identifier: (optional)
            Used to filter by the identifier of the object.

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.ExternalPublicationValidationSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/tasks/{taskKey}/externalPublicationValidations"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "fields",
            "name",
            "identifier",
            "page",
            "limit",
            "sort_order",
            "sort_by"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_external_publication_validations got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "taskKey": task_key
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
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
            "name": kwargs.get("name", missing),
            "identifier": self.base_client.generate_collection_format_param(kwargs.get("identifier", missing), 'multi'),
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
                response_type="ExternalPublicationValidationSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ExternalPublicationValidationSummaryCollection")

    def list_external_publications(self, workspace_id, task_key, **kwargs):
        """
        Retrieves a list of external publications in an application and provides options to filter the list.


        :param str workspace_id: (required)
            The workspace ID.

        :param str task_key: (required)
            The task key.

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.ExternalPublicationSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/tasks/{taskKey}/externalPublications"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "fields",
            "name",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_external_publications got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "taskKey": task_key
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
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
            "name": kwargs.get("name", missing),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ExternalPublicationSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ExternalPublicationSummaryCollection")

    def list_folders(self, workspace_id, **kwargs):
        """
        Retrieves a list of folders in a project and provides options to filter the list.


        :param str workspace_id: (required)
            The workspace ID.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str aggregator_key: (optional)
            Used to filter by the project or the folder object.

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param list[str] identifier: (optional)
            Used to filter by the identifier of the object.

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.FolderSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/folders"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "aggregator_key",
            "fields",
            "name",
            "identifier",
            "page",
            "limit",
            "sort_order",
            "sort_by"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_folders got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "aggregatorKey": kwargs.get("aggregator_key", missing),
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
            "name": kwargs.get("name", missing),
            "identifier": self.base_client.generate_collection_format_param(kwargs.get("identifier", missing), 'multi'),
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
                response_type="FolderSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="FolderSummaryCollection")

    def list_patch_changes(self, workspace_id, application_key, **kwargs):
        """
        Retrieves a list of patches in an application and provides options to filter the list.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param str since_patch: (optional)
            Specifies the patch key to query from.

        :param str to_patch: (optional)
            Specifies the patch key to query to.

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.PatchChangeSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/patchChanges"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "name",
            "since_patch",
            "to_patch",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_patch_changes got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key
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
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "name": kwargs.get("name", missing),
            "sincePatch": kwargs.get("since_patch", missing),
            "toPatch": kwargs.get("to_patch", missing),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="PatchChangeSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="PatchChangeSummaryCollection")

    def list_patches(self, workspace_id, application_key, **kwargs):
        """
        Retrieves a list of patches in an application and provides options to filter the list. For listing changes based on a period and logical objects changed, see ListPatchChanges API.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param list[str] identifier: (optional)
            Used to filter by the identifier of the published object.

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.PatchSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/patches"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "name",
            "identifier",
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
                "list_patches got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key
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
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "name": kwargs.get("name", missing),
            "identifier": self.base_client.generate_collection_format_param(kwargs.get("identifier", missing), 'multi'),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="PatchSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="PatchSummaryCollection")

    def list_projects(self, workspace_id, **kwargs):
        """
        Retrieves a lists of projects in a workspace and provides options to filter the list.


        :param str workspace_id: (required)
            The workspace ID.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param list[str] identifier: (optional)
            Used to filter by the identifier of the object.

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.ProjectSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/projects"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "fields",
            "name",
            "identifier",
            "page",
            "limit",
            "sort_order",
            "sort_by"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_projects got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
            "name": kwargs.get("name", missing),
            "identifier": self.base_client.generate_collection_format_param(kwargs.get("identifier", missing), 'multi'),
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
                response_type="ProjectSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ProjectSummaryCollection")

    def list_published_objects(self, workspace_id, application_key, **kwargs):
        """
        Retrieves a list of all the published objects for a specified application.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param list[str] identifier: (optional)
            Used to filter by the identifier of the published object.

        :param list[str] type: (optional)
            Used to filter by the object type of the object.
            It can be suffixed with an optional filter operator InSubtree.
            For Data Integration APIs, a filter based on type Task is used.

        :param str type_in_subtree: (optional)
            Used in association with type parameter. If value is true,
            then type all sub types of the given type parameter is considered.
            If value is false, then sub types are not considered. Default is false.

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.PublishedObjectSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/publishedObjects"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "fields",
            "name",
            "identifier",
            "type",
            "type_in_subtree",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_published_objects got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key
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
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
            "name": kwargs.get("name", missing),
            "identifier": self.base_client.generate_collection_format_param(kwargs.get("identifier", missing), 'multi'),
            "type": self.base_client.generate_collection_format_param(kwargs.get("type", missing), 'multi'),
            "typeInSubtree": kwargs.get("type_in_subtree", missing),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="PublishedObjectSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="PublishedObjectSummaryCollection")

    def list_references(self, workspace_id, application_key, **kwargs):
        """
        Retrieves a list of references in an application. Reference objects are created when dataflows and tasks use objects, such as data assets and connections.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str name: (optional)
            Used to filter by the name of the object.

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.ReferenceSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/references"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "name",
            "sort_order",
            "sort_by"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_references got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key
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
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "name": kwargs.get("name", missing),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ReferenceSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ReferenceSummaryCollection")

    def list_schemas(self, workspace_id, connection_key, schema_resource_name, **kwargs):
        """
        Retrieves a list of all the schemas that can be accessed using the specified connection.


        :param str workspace_id: (required)
            The workspace ID.

        :param str connection_key: (required)
            The connection key.

        :param str schema_resource_name: (required)
            Schema resource name used for retrieving schemas.

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str name: (optional)
            Used to filter by the name of the object.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.SchemaSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/connections/{connectionKey}/schemas"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "page",
            "limit",
            "fields",
            "sort_by",
            "sort_order",
            "name",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_schemas got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "connectionKey": connection_key
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
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
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "schemaResourceName": schema_resource_name,
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="SchemaSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="SchemaSummaryCollection")

    def list_task_run_logs(self, workspace_id, application_key, task_run_key, **kwargs):
        """
        Gets log entries for task runs using its key.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param str task_run_key: (required)
            The task run key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.data_integration.models.TaskRunLogSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/taskRuns/{taskRunKey}/logs"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
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
                "list_task_run_logs got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key,
            "taskRunKey": task_run_key
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
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
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
                response_type="list[TaskRunLogSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[TaskRunLogSummary]")

    def list_task_runs(self, workspace_id, application_key, **kwargs):
        """
        Retrieves a list of task runs and provides options to filter the list.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param list[str] identifier: (optional)
            Used to filter by the identifier of the object.

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.TaskRunSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/taskRuns"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "fields",
            "name",
            "identifier",
            "page",
            "limit",
            "sort_order",
            "sort_by"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_task_runs got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key
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
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
            "name": kwargs.get("name", missing),
            "identifier": self.base_client.generate_collection_format_param(kwargs.get("identifier", missing), 'multi'),
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
                response_type="TaskRunSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="TaskRunSummaryCollection")

    def list_task_validations(self, workspace_id, **kwargs):
        """
        Retrieves a list of task validations within the specified workspace.


        :param str workspace_id: (required)
            The workspace ID.

        :param str key: (optional)
            Used to filter by the key of the object.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param str identifier: (optional)
            Used to filter by the identifier of the object.

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.TaskValidationSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/taskValidations"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "key",
            "name",
            "identifier",
            "fields",
            "page",
            "limit",
            "sort_by",
            "sort_order",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_task_validations got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
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
            "key": kwargs.get("key", missing),
            "name": kwargs.get("name", missing),
            "identifier": kwargs.get("identifier", missing),
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
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
                response_type="TaskValidationSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="TaskValidationSummaryCollection")

    def list_tasks(self, workspace_id, **kwargs):
        """
        Retrieves a list of all tasks in a specified project or folder.


        :param str workspace_id: (required)
            The workspace ID.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str folder_id: (optional)
            Unique key of the folder.

        :param list[str] fields: (optional)
            Specifies the fields to get for an object.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param list[str] key: (optional)
            Used to filter by the key of the object.

        :param list[str] identifier: (optional)
            Used to filter by the identifier of the object.

        :param list[str] type: (optional)
            Used to filter by the object type of the object. It can be suffixed with an optional filter operator InSubtree. If this operator is not specified, then exact match is considered. <br><br><B>Examples:</B><br> <ul> <li><B>?type=DATA_LOADER_TASK&typeInSubtree=false</B> returns all objects of type data loader task</li> <li><B>?type=DATA_LOADER_TASK</B> returns all objects of type data loader task</li> <li><B>?type=DATA_LOADER_TASK&typeInSubtree=true</B> returns all objects of type data loader task</li> </ul>

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.TaskSummaryCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/tasks"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "folder_id",
            "fields",
            "name",
            "key",
            "identifier",
            "type",
            "limit",
            "page",
            "sort_order",
            "sort_by"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_tasks got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "folderId": kwargs.get("folder_id", missing),
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
            "name": kwargs.get("name", missing),
            "key": self.base_client.generate_collection_format_param(kwargs.get("key", missing), 'multi'),
            "identifier": self.base_client.generate_collection_format_param(kwargs.get("identifier", missing), 'multi'),
            "type": self.base_client.generate_collection_format_param(kwargs.get("type", missing), 'multi'),
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="TaskSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="TaskSummaryCollection")

    def list_work_request_errors(self, work_request_id, **kwargs):
        """
        Retrieves a paginated list of errors for a given work request.


        :param str work_request_id: (required)
            The ID of the asynchronous work request to retrieve.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.data_integration.models.WorkRequestError`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workRequests/{workRequestId}/workRequestErrors"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
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

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
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
        Retrieves a paginated list of logs for a given work request.


        :param str work_request_id: (required)
            The ID of the asynchronous work request to retrieve.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.data_integration.models.WorkRequestLogEntry`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workRequests/{workRequestId}/logs"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
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

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
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
        Lists the work requests in a compartment.


        :param str compartment_id: (required)
            The OCID of the compartment containing the resources you want to list.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str work_request_status: (optional)
            The work request status.

            Allowed values are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.data_integration.models.WorkRequestSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workRequests"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "work_request_status",
            "page",
            "limit",
            "sort_order",
            "sort_by"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_work_requests got unknown kwargs: {!r}".format(extra_kwargs))

        if 'work_request_status' in kwargs:
            work_request_status_allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
            if kwargs['work_request_status'] not in work_request_status_allowed_values:
                raise ValueError(
                    "Invalid value for `work_request_status`, must be one of {0}".format(work_request_status_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "workRequestStatus": kwargs.get("work_request_status", missing),
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

    def list_workspaces(self, compartment_id, **kwargs):
        """
        Retrieves a list of Data Integration workspaces.


        :param str compartment_id: (required)
            The OCID of the compartment containing the resources you want to list.

        :param str name: (optional)
            Used to filter by the name of the object.

        :param int limit: (optional)
            Sets the maximum number of results per page, or items to return in a paginated `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value for this parameter is the `opc-next-page` or the `opc-prev-page` response header from the previous `List` call. See `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str lifecycle_state: (optional)
            The lifecycle state of a resource. When specified, the operation only returns resources that match the given lifecycle state. When not specified, all lifecycle states are processed as a match.

            Allowed values are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "STARTING", "STOPPING", "STOPPED"

        :param str sort_order: (optional)
            Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).

            Allowed values are: "TIME_CREATED", "DISPLAY_NAME"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.data_integration.models.WorkspaceSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "name",
            "limit",
            "page",
            "lifecycle_state",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_workspaces got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "STARTING", "STOPPING", "STOPPED"]
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
            sort_by_allowed_values = ["TIME_CREATED", "DISPLAY_NAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "name": kwargs.get("name", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
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
                response_type="list[WorkspaceSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkspaceSummary]")

    def start_workspace(self, workspace_id, **kwargs):
        """
        Starts a workspace.


        :param str workspace_id: (required)
            The workspace ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/actions/start"
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
                "start_workspace got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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

    def stop_workspace(self, workspace_id, **kwargs):
        """
        Stops a workspace.


        :param str workspace_id: (required)
            The workspace ID.

        :param int quiesce_timeout: (optional)
            Used to set the timeout for Data Integration to gracefully close down any running jobs before stopping the workspace.

        :param bool is_force_operation: (optional)
            Used to force close down the workspace.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/actions/stop"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "quiesce_timeout",
            "is_force_operation",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "stop_workspace got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "quiesceTimeout": kwargs.get("quiesce_timeout", missing),
            "isForceOperation": kwargs.get("is_force_operation", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

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
                query_params=query_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)

    def update_application(self, workspace_id, application_key, update_application_details, **kwargs):
        """
        Updates an application.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param UpdateApplicationDetails update_application_details: (required)
            The details needed to update an application.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Application`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}"
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
                "update_application got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key
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
                body=update_application_details,
                response_type="Application")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_application_details,
                response_type="Application")

    def update_connection(self, workspace_id, connection_key, update_connection_details, **kwargs):
        """
        Updates a connection under a data asset.


        :param str workspace_id: (required)
            The workspace ID.

        :param str connection_key: (required)
            The connection key.

        :param UpdateConnectionDetails update_connection_details: (required)
            The information needed to update a connection.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Connection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/connections/{connectionKey}"
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
                "update_connection got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "connectionKey": connection_key
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
                body=update_connection_details,
                response_type="Connection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_connection_details,
                response_type="Connection")

    def update_data_asset(self, workspace_id, data_asset_key, update_data_asset_details, **kwargs):
        """
        Updates a specific data asset with default connection.


        :param str workspace_id: (required)
            The workspace ID.

        :param str data_asset_key: (required)
            The data asset key.

        :param UpdateDataAssetDetails update_data_asset_details: (required)
            The information needed to update a data asset.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.DataAsset`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/dataAssets/{dataAssetKey}"
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
                "update_data_asset got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "dataAssetKey": data_asset_key
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
                body=update_data_asset_details,
                response_type="DataAsset")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_data_asset_details,
                response_type="DataAsset")

    def update_data_flow(self, workspace_id, data_flow_key, update_data_flow_details, **kwargs):
        """
        Updates a specific data flow.


        :param str workspace_id: (required)
            The workspace ID.

        :param str data_flow_key: (required)
            The data flow key.

        :param UpdateDataFlowDetails update_data_flow_details: (required)
            The details needed to updated a data flow.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.DataFlow`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/dataFlows/{dataFlowKey}"
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
                "update_data_flow got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "dataFlowKey": data_flow_key
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
                body=update_data_flow_details,
                response_type="DataFlow")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_data_flow_details,
                response_type="DataFlow")

    def update_external_publication(self, workspace_id, task_key, external_publications_key, update_external_publication_details, **kwargs):
        """
        Updates the external publication object.


        :param str workspace_id: (required)
            The workspace ID.

        :param str task_key: (required)
            The task key.

        :param str external_publications_key: (required)
            The external published object key.

        :param UpdateExternalPublicationDetails update_external_publication_details: (required)
            The information to be updated.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.ExternalPublication`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/tasks/{taskKey}/externalPublications/{externalPublicationsKey}"
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
                "update_external_publication got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "taskKey": task_key,
            "externalPublicationsKey": external_publications_key
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
                body=update_external_publication_details,
                response_type="ExternalPublication")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_external_publication_details,
                response_type="ExternalPublication")

    def update_folder(self, workspace_id, folder_key, update_folder_details, **kwargs):
        """
        Updates a specific folder.


        :param str workspace_id: (required)
            The workspace ID.

        :param str folder_key: (required)
            The folder key.

        :param UpdateFolderDetails update_folder_details: (required)
            The details needed to update a folder.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Folder`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/folders/{folderKey}"
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
                "update_folder got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "folderKey": folder_key
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
                body=update_folder_details,
                response_type="Folder")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_folder_details,
                response_type="Folder")

    def update_project(self, workspace_id, project_key, update_project_details, **kwargs):
        """
        Updates a specific project.


        :param str workspace_id: (required)
            The workspace ID.

        :param str project_key: (required)
            The project key.

        :param UpdateProjectDetails update_project_details: (required)
            The details needed to update a project.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Project`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/projects/{projectKey}"
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
                "update_project got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "projectKey": project_key
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
                body=update_project_details,
                response_type="Project")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_project_details,
                response_type="Project")

    def update_reference(self, workspace_id, application_key, reference_key, update_reference_details, **kwargs):
        """
        Updates the application references. For example, to map a data asset to a different target object.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param str reference_key: (required)
            The reference key.

        :param UpdateReferenceDetails update_reference_details: (required)
            The details needed to update the references.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Reference`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/references/{referenceKey}"
        method = "PUT"

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
                "update_reference got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key,
            "referenceKey": reference_key
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
                path_params=path_params,
                header_params=header_params,
                body=update_reference_details,
                response_type="Reference")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_reference_details,
                response_type="Reference")

    def update_task(self, workspace_id, task_key, update_task_details, **kwargs):
        """
        Updates a specific task. For example, you can update the task description or move the task to a different folder by changing the `aggregatorKey` to a different folder in the registry.


        :param str workspace_id: (required)
            The workspace ID.

        :param str task_key: (required)
            The task key.

        :param UpdateTaskDetails update_task_details: (required)
            The details needed to update a task.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Task`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/tasks/{taskKey}"
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
                "update_task got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "taskKey": task_key
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
                body=update_task_details,
                response_type="Task")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_task_details,
                response_type="Task")

    def update_task_run(self, workspace_id, application_key, task_run_key, update_task_run_details, **kwargs):
        """
        Updates the status of the task run. For example, aborts a task run.


        :param str workspace_id: (required)
            The workspace ID.

        :param str application_key: (required)
            The application key.

        :param str task_run_key: (required)
            The task run key.

        :param UpdateTaskRunDetails update_task_run_details: (required)
            The details needed to update the status of a task run.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.TaskRunDetails`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}/applications/{applicationKey}/taskRuns/{taskRunKey}"
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
                "update_task_run got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id,
            "applicationKey": application_key,
            "taskRunKey": task_run_key
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
                body=update_task_run_details,
                response_type="TaskRunDetails")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_task_run_details,
                response_type="TaskRunDetails")

    def update_workspace(self, workspace_id, update_workspace_details, **kwargs):
        """
        Updates the specified Data Integration workspace.


        :param str workspace_id: (required)
            The workspace ID.

        :param UpdateWorkspaceDetails update_workspace_details: (required)
            The information needed to update the workspace.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.
            The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value.
            When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If
            you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.data_integration.models.Workspace`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workspaces/{workspaceId}"
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
                "update_workspace got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workspaceId": workspace_id
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
                body=update_workspace_details,
                response_type="Workspace")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_workspace_details,
                response_type="Workspace")
