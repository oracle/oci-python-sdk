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
from .models import marketplace_type_mapping
missing = Sentinel("Missing")


class MarketplaceClient(object):
    """
    Use the Marketplace API to manage applications in Oracle Cloud Infrastructure Marketplace. For more information, see [Overview of Marketplace](/Content/Marketplace/Concepts/marketoverview.htm)
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
            'base_path': '/20181001',
            'service_endpoint_template': 'https://marketplace.{region}.oci.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'circuit_breaker_strategy': kwargs.get('circuit_breaker_strategy', circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY)
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        if base_client_init_kwargs.get('circuit_breaker_strategy') is None:
            base_client_init_kwargs['circuit_breaker_strategy'] = circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY
        if 'allow_control_chars' in kwargs:
            base_client_init_kwargs['allow_control_chars'] = kwargs.get('allow_control_chars')
        self.base_client = BaseClient("marketplace", config, signer, marketplace_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

    def change_publication_compartment(self, publication_id, change_publication_compartment_details, **kwargs):
        """
        Moves the specified publication from one compartment to another.


        :param str publication_id: (required)
            The unique identifier for the publication.

        :param oci.marketplace.models.ChangePublicationCompartmentDetails change_publication_compartment_details: (required)
            The details of the request to change the compartment of a given publication.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without
            risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before
            then due to conflicting operations (for example, if a resource has been deleted and purged from the system,
            then a retry of the original creation request might be rejected).

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to
            the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or
            deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/change_publication_compartment.py.html>`__ to see an example of how to use change_publication_compartment API.
        """
        resource_path = "/publications/{publicationId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_publication_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/Publication/ChangePublicationCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_publication_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "publicationId": publication_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

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
                body=change_publication_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_publication_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_accepted_agreement(self, create_accepted_agreement_details, **kwargs):
        """
        Accepts a terms of use agreement for a specific package version of a listing. You must accept all
        terms of use for a package before you can deploy the package.


        :param oci.marketplace.models.CreateAcceptedAgreementDetails create_accepted_agreement_details: (required)
            Details necessary to accept an agreement.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without
            risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before
            then due to conflicting operations (for example, if a resource has been deleted and purged from the system,
            then a retry of the original creation request might be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.marketplace.models.AcceptedAgreement`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/create_accepted_agreement.py.html>`__ to see an example of how to use create_accepted_agreement API.
        """
        resource_path = "/acceptedAgreements"
        method = "POST"
        operation_name = "create_accepted_agreement"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/AcceptedAgreement/CreateAcceptedAgreement"

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
                "create_accepted_agreement got unknown kwargs: {!r}".format(extra_kwargs))

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
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_accepted_agreement_details,
                response_type="AcceptedAgreement",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_accepted_agreement_details,
                response_type="AcceptedAgreement",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_publication(self, create_publication_details, **kwargs):
        """
        Creates a publication of the specified listing type with an optional default package.


        :param oci.marketplace.models.CreatePublicationDetails create_publication_details: (required)
            The details for creating the publication.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without
            risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before
            then due to conflicting operations (for example, if a resource has been deleted and purged from the system,
            then a retry of the original creation request might be rejected).

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.marketplace.models.Publication`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/create_publication.py.html>`__ to see an example of how to use create_publication API.
        """
        resource_path = "/publications"
        method = "POST"
        operation_name = "create_publication"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/Publication/CreatePublication"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_publication got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_publication_details,
                response_type="Publication",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_publication_details,
                response_type="Publication",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def delete_accepted_agreement(self, accepted_agreement_id, **kwargs):
        """
        Removes a previously accepted terms of use agreement from the list of agreements that Marketplace checks
        before initiating a deployment. Listings in Marketplace that require acceptance of the specified terms
        of use can no longer be deployed, but existing deployments aren't affected.


        :param str accepted_agreement_id: (required)
            The unique identifier for the accepted terms of use agreement.

        :param str signature: (optional)
            Previously, the signature generated for the listing package terms of use agreement, but now deprecated and ignored.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to
            the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or
            deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/delete_accepted_agreement.py.html>`__ to see an example of how to use delete_accepted_agreement API.
        """
        resource_path = "/acceptedAgreements/{acceptedAgreementId}"
        method = "DELETE"
        operation_name = "delete_accepted_agreement"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/AcceptedAgreement/DeleteAcceptedAgreement"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "signature",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_accepted_agreement got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "acceptedAgreementId": accepted_agreement_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "signature": kwargs.get("signature", missing)
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
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

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

    def delete_publication(self, publication_id, **kwargs):
        """
        Deletes a publication, which also removes the associated listing from anywhere it was published, such as Marketplace or Compute.


        :param str publication_id: (required)
            The unique identifier for the publication.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to
            the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or
            deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/delete_publication.py.html>`__ to see an example of how to use delete_publication API.
        """
        resource_path = "/publications/{publicationId}"
        method = "DELETE"
        operation_name = "delete_publication"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/Publication/DeletePublication"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_publication got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "publicationId": publication_id
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_accepted_agreement(self, accepted_agreement_id, **kwargs):
        """
        Gets the details of a specific, previously accepted terms of use agreement.


        :param str accepted_agreement_id: (required)
            The unique identifier for the accepted terms of use agreement.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.marketplace.models.AcceptedAgreement`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/get_accepted_agreement.py.html>`__ to see an example of how to use get_accepted_agreement API.
        """
        resource_path = "/acceptedAgreements/{acceptedAgreementId}"
        method = "GET"
        operation_name = "get_accepted_agreement"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/AcceptedAgreement/GetAcceptedAgreement"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_accepted_agreement got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "acceptedAgreementId": accepted_agreement_id
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AcceptedAgreement",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AcceptedAgreement",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_agreement(self, listing_id, package_version, agreement_id, **kwargs):
        """
        Returns a terms of use agreement for a package with a time-based signature that can be used to
        accept the agreement.


        :param str listing_id: (required)
            The unique identifier for the listing.

        :param str package_version: (required)
            The version of the package. Package versions are unique within a listing.

        :param str agreement_id: (required)
            The unique identifier for the agreement.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str compartment_id: (optional)
            The unique identifier for the compartment.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.marketplace.models.Agreement`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/get_agreement.py.html>`__ to see an example of how to use get_agreement API.
        """
        resource_path = "/listings/{listingId}/packages/{packageVersion}/agreements/{agreementId}"
        method = "GET"
        operation_name = "get_agreement"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/Agreement/GetAgreement"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_agreement got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "listingId": listing_id,
            "packageVersion": package_version,
            "agreementId": agreement_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

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
                response_type="Agreement",
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
                response_type="Agreement",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_listing(self, listing_id, **kwargs):
        """
        Gets detailed information about a listing, including the listing's name, version, description, and
        resources.

        If you plan to launch an instance from an image listing, you must first subscribe to the listing. When
        you launch the instance, you also need to provide the image ID of the listing resource version that you want.

        Subscribing to the listing requires you to first get a signature from the terms of use agreement for the
        listing resource version. To get the signature, issue a `GetAppCatalogListingAgreements`__ API call.
        The `AppCatalogListingResourceVersionAgreements`__ object, including
        its signature, is returned in the response. With the signature for the terms of use agreement for the desired
        listing resource version, create a subscription by issuing a
        `CreateAppCatalogSubscription`__ API call.

        To get the image ID to launch an instance, issue a `GetAppCatalogListingResourceVersion`__ API call.
        Lastly, to launch the instance, use the image ID of the listing resource version to issue a `LaunchInstance`__ API call.

        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements/GetAppCatalogListingAgreements
        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements
        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogSubscription/CreateAppCatalogSubscription
        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersion/GetAppCatalogListingResourceVersion
        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Instance/LaunchInstance


        :param str listing_id: (required)
            The unique identifier for the listing.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str compartment_id: (optional)
            The unique identifier for the compartment.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.marketplace.models.Listing`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/get_listing.py.html>`__ to see an example of how to use get_listing API.
        """
        resource_path = "/listings/{listingId}"
        method = "GET"
        operation_name = "get_listing"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/Listing/GetListing"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_listing got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "listingId": listing_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

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
                response_type="Listing",
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
                response_type="Listing",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_package(self, listing_id, package_version, **kwargs):
        """
        Get the details of the specified version of a package, including information needed to launch the package.

        If you plan to launch an instance from an image listing, you must first subscribe to the listing. When
        you launch the instance, you also need to provide the image ID of the listing resource version that you want.

        Subscribing to the listing requires you to first get a signature from the terms of use agreement for the
        listing resource version. To get the signature, issue a `GetAppCatalogListingAgreements`__ API call.
        The `AppCatalogListingResourceVersionAgreements`__ object, including
        its signature, is returned in the response. With the signature for the terms of use agreement for the desired
        listing resource version, create a subscription by issuing a
        `CreateAppCatalogSubscription`__ API call.

        To get the image ID to launch an instance, issue a `GetAppCatalogListingResourceVersion`__ API call.
        Lastly, to launch the instance, use the image ID of the listing resource version to issue a `LaunchInstance`__ API call.

        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements/GetAppCatalogListingAgreements
        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements
        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogSubscription/CreateAppCatalogSubscription
        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersion/GetAppCatalogListingResourceVersion
        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Instance/LaunchInstance


        :param str listing_id: (required)
            The unique identifier for the listing.

        :param str package_version: (required)
            The version of the package. Package versions are unique within a listing.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str compartment_id: (optional)
            The unique identifier for the compartment.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.marketplace.models.ListingPackage`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/get_package.py.html>`__ to see an example of how to use get_package API.
        """
        resource_path = "/listings/{listingId}/packages/{packageVersion}"
        method = "GET"
        operation_name = "get_package"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/ListingPackage/GetPackage"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_package got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "listingId": listing_id,
            "packageVersion": package_version
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

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
                response_type="ListingPackage",
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
                response_type="ListingPackage",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_publication(self, publication_id, **kwargs):
        """
        Gets the details of the specified publication.


        :param str publication_id: (required)
            The unique identifier for the publication.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.marketplace.models.Publication`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/get_publication.py.html>`__ to see an example of how to use get_publication API.
        """
        resource_path = "/publications/{publicationId}"
        method = "GET"
        operation_name = "get_publication"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/Publication/GetPublication"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_publication got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "publicationId": publication_id
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Publication",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Publication",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_publication_package(self, publication_id, package_version, **kwargs):
        """
        Gets the details of a specific package version within a given publication.


        :param str publication_id: (required)
            The unique identifier for the publication.

        :param str package_version: (required)
            The version of the package. Package versions are unique within a listing.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.marketplace.models.PublicationPackage`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/get_publication_package.py.html>`__ to see an example of how to use get_publication_package API.
        """
        resource_path = "/publications/{publicationId}/packages/{packageVersion}"
        method = "GET"
        operation_name = "get_publication_package"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/PublicationPackage/GetPublicationPackage"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_publication_package got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "publicationId": publication_id,
            "packageVersion": package_version
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="PublicationPackage",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="PublicationPackage",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_accepted_agreements(self, compartment_id, **kwargs):
        """
        Lists the terms of use agreements that have been accepted in the specified compartment.
        You can filter results by specifying query parameters.


        :param str compartment_id: (required)
            The unique identifier for the compartment.

        :param str display_name: (optional)
            The display name of the resource.

        :param str listing_id: (optional)
            The unique identifier for the listing.

        :param str package_version: (optional)
            The version of the package. Package versions are unique within a listing.

        :param str accepted_agreement_id: (optional)
            The unique identifier for the accepted terms of use agreement.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str sort_by: (optional)
            The field to use to sort listed results. You can only specify one field to sort by.
            `TIMEACCEPTED` displays results in descending order by default. You can change your
            preference by specifying a different sort order.

            Allowed values are: "TIMEACCEPTED"

        :param str sort_order: (optional)
            The sort order to use, either `ASC` or `DESC`.

            Allowed values are: "ASC", "DESC"

        :param int limit: (optional)
            How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.marketplace.models.AcceptedAgreementSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/list_accepted_agreements.py.html>`__ to see an example of how to use list_accepted_agreements API.
        """
        resource_path = "/acceptedAgreements"
        method = "GET"
        operation_name = "list_accepted_agreements"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/AcceptedAgreementSummary/ListAcceptedAgreements"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "display_name",
            "listing_id",
            "package_version",
            "accepted_agreement_id",
            "opc_request_id",
            "sort_by",
            "sort_order",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_accepted_agreements got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMEACCEPTED"]
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
            "displayName": kwargs.get("display_name", missing),
            "listingId": kwargs.get("listing_id", missing),
            "packageVersion": kwargs.get("package_version", missing),
            "acceptedAgreementId": kwargs.get("accepted_agreement_id", missing),
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AcceptedAgreementSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AcceptedAgreementSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_agreements(self, listing_id, package_version, **kwargs):
        """
        Returns the terms of use agreements that must be accepted before you can deploy the specified version of a package.


        :param str listing_id: (required)
            The unique identifier for the listing.

        :param str package_version: (required)
            The version of the package. Package versions are unique within a listing.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param int limit: (optional)
            How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str compartment_id: (optional)
            The unique identifier for the compartment.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.marketplace.models.AgreementSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/list_agreements.py.html>`__ to see an example of how to use list_agreements API.
        """
        resource_path = "/listings/{listingId}/packages/{packageVersion}/agreements"
        method = "GET"
        operation_name = "list_agreements"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/AgreementSummary/ListAgreements"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_agreements got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "listingId": listing_id,
            "packageVersion": package_version
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
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
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

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
                response_type="list[AgreementSummary]",
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
                response_type="list[AgreementSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_categories(self, **kwargs):
        """
        Gets the list of all the categories for listings published to Oracle Cloud Infrastructure Marketplace. Categories apply
        to the software product provided by the listing.


        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param int limit: (optional)
            How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str compartment_id: (optional)
            The unique identifier for the compartment.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.marketplace.models.CategorySummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/list_categories.py.html>`__ to see an example of how to use list_categories API.
        """
        resource_path = "/categories"
        method = "GET"
        operation_name = "list_categories"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/CategorySummary/ListCategories"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_categories got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
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
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[CategorySummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[CategorySummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_listings(self, **kwargs):
        """
        Gets a list of listings from Oracle Cloud Infrastructure Marketplace by searching keywords and
        filtering according to listing attributes.

        If you plan to launch an instance from an image listing, you must first subscribe to the listing. When
        you launch the instance, you also need to provide the image ID of the listing resource version that you want.

        Subscribing to the listing requires you to first get a signature from the terms of use agreement for the
        listing resource version. To get the signature, issue a `GetAppCatalogListingAgreements`__ API call.
        The `AppCatalogListingResourceVersionAgreements`__ object, including
        its signature, is returned in the response. With the signature for the terms of use agreement for the desired
        listing resource version, create a subscription by issuing a
        `CreateAppCatalogSubscription`__ API call.

        To get the image ID to launch an instance, issue a `GetAppCatalogListingResourceVersion`__ API call.
        Lastly, to launch the instance, use the image ID of the listing resource version to issue a `LaunchInstance`__ API call.

        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements/GetAppCatalogListingAgreements
        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements
        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogSubscription/CreateAppCatalogSubscription
        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersion/GetAppCatalogListingResourceVersion
        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Instance/LaunchInstance


        :param list[str] name: (optional)
            The name of the listing.

        :param str listing_id: (optional)
            The unique identifier for the listing.

        :param str image_id: (optional)
            The image identifier of the listing.

        :param str publisher_id: (optional)
            Limit results to just this publisher.

        :param str package_type: (optional)
            A filter to return only packages that match the given package type exactly.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param int limit: (optional)
            How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str sort_by: (optional)
            The field to use to sort listed results. You can only specify one field to sort by.
            `TIMERELEASED` displays results in descending order by default.
            You can change your preference by specifying a different sort order.

            Allowed values are: "TIMERELEASED"

        :param str sort_order: (optional)
            The sort order to use, either `ASC` or `DESC`.

            Allowed values are: "ASC", "DESC"

        :param list[str] category: (optional)
            Name of the product category or categories. If you specify multiple categories, then Marketplace returns any listing with
            one or more matching categories.

        :param list[str] pricing: (optional)
            Name of the pricing type. If multiple pricing types are provided, then any listing with
            one or more matching pricing models will be returned.

            Allowed values are: "FREE", "BYOL", "PAYGO"

        :param bool is_featured: (optional)
            Indicates whether to show only featured listings. If this is set to `false` or is omitted, then all listings will be returned.

        :param list[str] listing_types: (optional)
            The type of the listing.

            Allowed values are: "COMMUNITY", "PARTNER", "PRIVATE"

        :param list[str] operating_systems: (optional)
            The operating system of the listing.

        :param str compartment_id: (optional)
            The unique identifier for the compartment.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.marketplace.models.ListingSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/list_listings.py.html>`__ to see an example of how to use list_listings API.
        """
        resource_path = "/listings"
        method = "GET"
        operation_name = "list_listings"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/ListingSummary/ListListings"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "name",
            "listing_id",
            "image_id",
            "publisher_id",
            "package_type",
            "opc_request_id",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "category",
            "pricing",
            "is_featured",
            "listing_types",
            "operating_systems",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_listings got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMERELEASED"]
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

        if 'pricing' in kwargs:
            pricing_allowed_values = ["FREE", "BYOL", "PAYGO"]
            for pricing_item in kwargs['pricing']:
                if pricing_item not in pricing_allowed_values:
                    raise ValueError(
                        "Invalid value for `pricing`, must be one of {0}".format(pricing_allowed_values)
                    )

        if 'listing_types' in kwargs:
            listing_types_allowed_values = ["COMMUNITY", "PARTNER", "PRIVATE"]
            for listing_types_item in kwargs['listing_types']:
                if listing_types_item not in listing_types_allowed_values:
                    raise ValueError(
                        "Invalid value for `listing_types`, must be one of {0}".format(listing_types_allowed_values)
                    )

        query_params = {
            "name": self.base_client.generate_collection_format_param(kwargs.get("name", missing), 'multi'),
            "listingId": kwargs.get("listing_id", missing),
            "imageId": kwargs.get("image_id", missing),
            "publisherId": kwargs.get("publisher_id", missing),
            "packageType": kwargs.get("package_type", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "category": self.base_client.generate_collection_format_param(kwargs.get("category", missing), 'multi'),
            "pricing": self.base_client.generate_collection_format_param(kwargs.get("pricing", missing), 'multi'),
            "isFeatured": kwargs.get("is_featured", missing),
            "listingTypes": self.base_client.generate_collection_format_param(kwargs.get("listing_types", missing), 'multi'),
            "operatingSystems": self.base_client.generate_collection_format_param(kwargs.get("operating_systems", missing), 'multi'),
            "compartmentId": kwargs.get("compartment_id", missing)
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
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ListingSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ListingSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_packages(self, listing_id, **kwargs):
        """
        Gets the list of packages for a listing.

        If you plan to launch an instance from an image listing, you must first subscribe to the listing. When
        you launch the instance, you also need to provide the image ID of the listing resource version that you want.

        Subscribing to the listing requires you to first get a signature from the terms of use agreement for the
        listing resource version. To get the signature, issue a `GetAppCatalogListingAgreements`__ API call.
        The `AppCatalogListingResourceVersionAgreements`__ object, including
        its signature, is returned in the response. With the signature for the terms of use agreement for the desired
        listing resource version, create a subscription by issuing a
        `CreateAppCatalogSubscription`__ API call.

        To get the image ID to launch an instance, issue a `GetAppCatalogListingResourceVersion`__ API call.
        Lastly, to launch the instance, use the image ID of the listing resource version to issue a `LaunchInstance`__ API call.

        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements/GetAppCatalogListingAgreements
        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements
        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogSubscription/CreateAppCatalogSubscription
        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersion/GetAppCatalogListingResourceVersion
        __ https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Instance/LaunchInstance


        :param str listing_id: (required)
            The unique identifier for the listing.

        :param str package_version: (optional)
            The version of the package. Package versions are unique within a listing.

        :param str package_type: (optional)
            A filter to return only packages that match the given package type exactly.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param int limit: (optional)
            How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str sort_by: (optional)
            The field to use to sort listed results. You can only specify one field to sort by.
            `TIMERELEASED` displays results in descending order by default.
            You can change your preference by specifying a different sort order.

            Allowed values are: "TIMERELEASED"

        :param str sort_order: (optional)
            The sort order to use, either `ASC` or `DESC`.

            Allowed values are: "ASC", "DESC"

        :param str compartment_id: (optional)
            The unique identifier for the compartment.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.marketplace.models.ListingPackageSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/list_packages.py.html>`__ to see an example of how to use list_packages API.
        """
        resource_path = "/listings/{listingId}/packages"
        method = "GET"
        operation_name = "list_packages"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/ListingPackageSummary/ListPackages"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "package_version",
            "package_type",
            "opc_request_id",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_packages got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "listingId": listing_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMERELEASED"]
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
            "packageVersion": kwargs.get("package_version", missing),
            "packageType": kwargs.get("package_type", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
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
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

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
                response_type="list[ListingPackageSummary]",
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
                response_type="list[ListingPackageSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_publication_packages(self, publication_id, **kwargs):
        """
        Lists the packages in the specified publication.


        :param str publication_id: (required)
            The unique identifier for the publication.

        :param str package_version: (optional)
            The version of the package. Package versions are unique within a listing.

        :param str package_type: (optional)
            A filter to return only packages that match the given package type exactly.

        :param str sort_by: (optional)
            The field to use to sort listed results. You can only specify one field to sort by.
            `TIMERELEASED` displays results in descending order by default.
            You can change your preference by specifying a different sort order.

            Allowed values are: "TIMERELEASED"

        :param str sort_order: (optional)
            The sort order to use, either `ASC` or `DESC`.

            Allowed values are: "ASC", "DESC"

        :param int limit: (optional)
            How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.marketplace.models.PublicationPackageSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/list_publication_packages.py.html>`__ to see an example of how to use list_publication_packages API.
        """
        resource_path = "/publications/{publicationId}/packages"
        method = "GET"
        operation_name = "list_publication_packages"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/PublicationPackageSummary/ListPublicationPackages"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "package_version",
            "package_type",
            "sort_by",
            "sort_order",
            "limit",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_publication_packages got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "publicationId": publication_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMERELEASED"]
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
            "packageVersion": kwargs.get("package_version", missing),
            "packageType": kwargs.get("package_type", missing),
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

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
                response_type="list[PublicationPackageSummary]",
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
                response_type="list[PublicationPackageSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_publications(self, compartment_id, listing_type, **kwargs):
        """
        Lists the publications in the specified compartment.


        :param str compartment_id: (required)
            The unique identifier for the compartment.

        :param str listing_type: (required)
            The type of the listing.

            Allowed values are: "COMMUNITY", "PARTNER", "PRIVATE"

        :param list[str] name: (optional)
            The name of the publication.

        :param str publication_id: (optional)
            The unique identifier for the publication.

        :param list[str] operating_systems: (optional)
            The operating system of the listing.

        :param str sort_by: (optional)
            The field to use to sort listed results. You can only specify one field to sort by.
            `TIMERELEASED` displays results in descending order by default.
            You can change your preference by specifying a different sort order.

            Allowed values are: "TIMERELEASED"

        :param str sort_order: (optional)
            The sort order to use, either `ASC` or `DESC`.

            Allowed values are: "ASC", "DESC"

        :param int limit: (optional)
            How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.marketplace.models.PublicationSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/list_publications.py.html>`__ to see an example of how to use list_publications API.
        """
        resource_path = "/publications"
        method = "GET"
        operation_name = "list_publications"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/PublicationSummary/ListPublications"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "name",
            "publication_id",
            "operating_systems",
            "sort_by",
            "sort_order",
            "limit",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_publications got unknown kwargs: {!r}".format(extra_kwargs))

        listing_type_allowed_values = ["COMMUNITY", "PARTNER", "PRIVATE"]
        if listing_type not in listing_type_allowed_values:
            raise ValueError(
                "Invalid value for `listing_type`, must be one of {0}".format(listing_type_allowed_values)
            )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMERELEASED"]
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
            "name": self.base_client.generate_collection_format_param(kwargs.get("name", missing), 'multi'),
            "listingType": listing_type,
            "publicationId": kwargs.get("publication_id", missing),
            "operatingSystems": self.base_client.generate_collection_format_param(kwargs.get("operating_systems", missing), 'multi'),
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PublicationSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PublicationSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_publishers(self, **kwargs):
        """
        Gets the list of all the publishers of listings available in Oracle Cloud Infrastructure Marketplace.


        :param str publisher_id: (optional)
            Limit results to just this publisher.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param int limit: (optional)
            How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str compartment_id: (optional)
            The unique identifier for the compartment.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.marketplace.models.PublisherSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/list_publishers.py.html>`__ to see an example of how to use list_publishers API.
        """
        resource_path = "/publishers"
        method = "GET"
        operation_name = "list_publishers"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/PublisherSummary/ListPublishers"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "publisher_id",
            "opc_request_id",
            "limit",
            "page",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_publishers got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "publisherId": kwargs.get("publisher_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
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
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PublisherSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PublisherSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_report_types(self, compartment_id, **kwargs):
        """
        Lists available types of reports for the compartment.


        :param str compartment_id: (required)
            The unique identifier for the compartment.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.marketplace.models.ReportTypeCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/list_report_types.py.html>`__ to see an example of how to use list_report_types API.
        """
        resource_path = "/reportTypes"
        method = "GET"
        operation_name = "list_report_types"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/ReportTypeCollection/ListReportTypes"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_report_types got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing)
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
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ReportTypeCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ReportTypeCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_reports(self, report_type, date, compartment_id, **kwargs):
        """
        Lists reports in the compartment that match the specified report type and date.


        :param str report_type: (required)
            The type of the report.

        :param datetime date: (required)
            Date, expressed in `RFC 3339`__ timestamp format. The service only interprets the year, month, and day parts in the input value, and ignores the hour, minute, and second parts.

            __ https://tools.ietf.org/html/rfc3339

        :param str compartment_id: (required)
            The unique identifier for the compartment.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.marketplace.models.ReportCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/list_reports.py.html>`__ to see an example of how to use list_reports API.
        """
        resource_path = "/reports"
        method = "GET"
        operation_name = "list_reports"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/ReportCollection/ListReports"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_reports got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "reportType": report_type,
            "date": date,
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing)
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
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ReportCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ReportCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_taxes(self, listing_id, **kwargs):
        """
        Returns list of all tax implications that current tenant may be liable to once they launch the listing.


        :param str listing_id: (required)
            The unique identifier for the listing.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str compartment_id: (optional)
            The unique identifier for the compartment.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.marketplace.models.TaxSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/list_taxes.py.html>`__ to see an example of how to use list_taxes API.
        """
        resource_path = "/listings/{listingId}/taxes"
        method = "GET"
        operation_name = "list_taxes"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/TaxSummary/ListTaxes"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_taxes got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "listingId": listing_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

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
                response_type="list[TaxSummary]",
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
                response_type="list[TaxSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def search_listings(self, search_listings_details, **kwargs):
        """
        Queries all Marketplace Applications to find listings that match the specified criteria. To search
        for a listing, you can use a free text or structured search.


        :param oci.marketplace.models.SearchListingsDetails search_listings_details: (required)
            Details related to the search query

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param int limit: (optional)
            How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.marketplace.models.ListingSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/search_listings.py.html>`__ to see an example of how to use search_listings API.
        """
        resource_path = "/searchListings"
        method = "POST"
        operation_name = "search_listings"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/ListingSummary/SearchListings"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "page",
            "limit"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "search_listings got unknown kwargs: {!r}".format(extra_kwargs))

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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=search_listings_details,
                response_type="list[ListingSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=search_listings_details,
                response_type="list[ListingSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_accepted_agreement(self, accepted_agreement_id, update_accepted_agreement_details, **kwargs):
        """
        Updates the display name or tags associated with a listing's previously accepted terms of use agreement.


        :param str accepted_agreement_id: (required)
            The unique identifier for the accepted terms of use agreement.

        :param oci.marketplace.models.UpdateAcceptedAgreementDetails update_accepted_agreement_details: (required)
            Details to update for an accepted agreement.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without
            risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before
            then due to conflicting operations (for example, if a resource has been deleted and purged from the system,
            then a retry of the original creation request might be rejected).

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to
            the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or
            deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.marketplace.models.AcceptedAgreement`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/update_accepted_agreement.py.html>`__ to see an example of how to use update_accepted_agreement API.
        """
        resource_path = "/acceptedAgreements/{acceptedAgreementId}"
        method = "PUT"
        operation_name = "update_accepted_agreement"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/AcceptedAgreement/UpdateAcceptedAgreement"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_accepted_agreement got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "acceptedAgreementId": accepted_agreement_id
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

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
                body=update_accepted_agreement_details,
                response_type="AcceptedAgreement",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_accepted_agreement_details,
                response_type="AcceptedAgreement",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_publication(self, publication_id, update_publication_details, **kwargs):
        """
        Updates the details of an existing publication.


        :param str publication_id: (required)
            The unique identifier for the publication.

        :param oci.marketplace.models.UpdatePublicationDetails update_publication_details: (required)
            The details for updating the publication.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request,
            please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without
            risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before
            then due to conflicting operations (for example, if a resource has been deleted and purged from the system,
            then a retry of the original creation request might be rejected).

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to
            the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or
            deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.marketplace.models.Publication`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/marketplace/update_publication.py.html>`__ to see an example of how to use update_publication API.
        """
        resource_path = "/publications/{publicationId}"
        method = "PUT"
        operation_name = "update_publication"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/marketplace/20181001/Publication/UpdatePublication"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_publication got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "publicationId": publication_id
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

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )
        if retry_strategy is None:
            retry_strategy = retry.DEFAULT_RETRY_STRATEGY

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
                body=update_publication_details,
                response_type="Publication",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_publication_details,
                response_type="Publication",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
