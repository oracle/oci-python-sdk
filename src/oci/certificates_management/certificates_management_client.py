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
from .models import certificates_management_type_mapping
missing = Sentinel("Missing")


class CertificatesManagementClient(object):
    """
    API for managing certificates.
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
            'base_path': '/20210224',
            'service_endpoint_template': 'https://certificatesmanagement.{region}.oci.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'circuit_breaker_strategy': kwargs.get('circuit_breaker_strategy', circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY)
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        if base_client_init_kwargs.get('circuit_breaker_strategy') is None:
            base_client_init_kwargs['circuit_breaker_strategy'] = circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY
        if 'allow_control_chars' in kwargs:
            base_client_init_kwargs['allow_control_chars'] = kwargs.get('allow_control_chars')
        self.base_client = BaseClient("certificates_management", config, signer, certificates_management_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

    def cancel_certificate_authority_deletion(self, certificate_authority_id, **kwargs):
        """
        Cancels the scheduled deletion of the specified certificate authority (CA).


        :param str certificate_authority_id: (required)
            The OCID of the certificate authority (CA).

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/cancel_certificate_authority_deletion.py.html>`__ to see an example of how to use cancel_certificate_authority_deletion API.
        """
        resource_path = "/certificateAuthorities/{certificateAuthorityId}/actions/cancelDeletion"
        method = "POST"
        operation_name = "cancel_certificate_authority_deletion"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateAuthority/CancelCertificateAuthorityDeletion"

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
                "cancel_certificate_authority_deletion got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateAuthorityId": certificate_authority_id
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

    def cancel_certificate_authority_version_deletion(self, certificate_authority_id, certificate_authority_version_number, **kwargs):
        """
        Cancels the scheduled deletion of the specified certificate authority (CA) version. Canceling
        a scheduled deletion restores the CA version's lifecycle state to what
        it was before its scheduled deletion.


        :param str certificate_authority_id: (required)
            The OCID of the certificate authority (CA).

        :param int certificate_authority_version_number: (required)
            The version number of the certificate authority (CA).

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/cancel_certificate_authority_version_deletion.py.html>`__ to see an example of how to use cancel_certificate_authority_version_deletion API.
        """
        resource_path = "/certificateAuthorities/{certificateAuthorityId}/version/{certificateAuthorityVersionNumber}/actions/cancelDeletion"
        method = "POST"
        operation_name = "cancel_certificate_authority_version_deletion"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateAuthorityVersion/CancelCertificateAuthorityVersionDeletion"

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
                "cancel_certificate_authority_version_deletion got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateAuthorityId": certificate_authority_id,
            "certificateAuthorityVersionNumber": certificate_authority_version_number
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

    def cancel_certificate_deletion(self, certificate_id, **kwargs):
        """
        Cancels the pending deletion of the specified certificate. Canceling
        a scheduled deletion restores the certificate's lifecycle state to what
        it was before you scheduled the certificate for deletion.


        :param str certificate_id: (required)
            The OCID of the certificate.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/cancel_certificate_deletion.py.html>`__ to see an example of how to use cancel_certificate_deletion API.
        """
        resource_path = "/certificates/{certificateId}/actions/cancelDeletion"
        method = "POST"
        operation_name = "cancel_certificate_deletion"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/Certificate/CancelCertificateDeletion"

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
                "cancel_certificate_deletion got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateId": certificate_id
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

    def cancel_certificate_version_deletion(self, certificate_id, certificate_version_number, **kwargs):
        """
        Cancels the scheduled deletion of the specified certificate version.


        :param str certificate_id: (required)
            The OCID of the certificate.

        :param int certificate_version_number: (required)
            The version number of the certificate.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/cancel_certificate_version_deletion.py.html>`__ to see an example of how to use cancel_certificate_version_deletion API.
        """
        resource_path = "/certificates/{certificateId}/version/{certificateVersionNumber}/actions/cancelDeletion"
        method = "POST"
        operation_name = "cancel_certificate_version_deletion"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateVersion/CancelCertificateVersionDeletion"

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
                "cancel_certificate_version_deletion got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateId": certificate_id,
            "certificateVersionNumber": certificate_version_number
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

    def change_ca_bundle_compartment(self, ca_bundle_id, change_ca_bundle_compartment_details, **kwargs):
        """
        Moves a CA bundle to a different compartment in the same tenancy. For information about
        moving resources between compartments, see `Moving Resources to a Different Compartment`__.

        When provided, if-match is checked against the ETag values of the secret.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str ca_bundle_id: (required)
            The OCID of the CA bundle.

        :param oci.certificates_management.models.ChangeCaBundleCompartmentDetails change_ca_bundle_compartment_details: (required)
            The updated compartment details.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original
            creation request may be rejected).

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/change_ca_bundle_compartment.py.html>`__ to see an example of how to use change_ca_bundle_compartment API.
        """
        resource_path = "/caBundles/{caBundleId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_ca_bundle_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CaBundle/ChangeCaBundleCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_ca_bundle_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "caBundleId": ca_bundle_id
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
                body=change_ca_bundle_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_ca_bundle_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def change_certificate_authority_compartment(self, certificate_authority_id, change_certificate_authority_compartment_details, **kwargs):
        """
        Moves a certificate authority (CA) to a different compartment within the same tenancy. For information about
        moving resources between compartments, see `Moving Resources to a Different Compartment`__.

        When provided, If-Match is checked against the ETag values of the source.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str certificate_authority_id: (required)
            The OCID of the certificate authority (CA).

        :param oci.certificates_management.models.ChangeCertificateAuthorityCompartmentDetails change_certificate_authority_compartment_details: (required)
            The updated compartment details

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original
            creation request may be rejected).

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/change_certificate_authority_compartment.py.html>`__ to see an example of how to use change_certificate_authority_compartment API.
        """
        resource_path = "/certificateAuthorities/{certificateAuthorityId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_certificate_authority_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateAuthority/ChangeCertificateAuthorityCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_certificate_authority_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateAuthorityId": certificate_authority_id
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
                body=change_certificate_authority_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_certificate_authority_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def change_certificate_compartment(self, certificate_id, change_certificate_compartment_details, **kwargs):
        """
        Moves a certificate to a different compartment within the same tenancy. For information about
        moving resources between compartments, see `Moving Resources to a Different Compartment`__.

        When provided, if-match is checked against the ETag values of the secret.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str certificate_id: (required)
            The OCID of the certificate.

        :param oci.certificates_management.models.ChangeCertificateCompartmentDetails change_certificate_compartment_details: (required)
            The updated compartment details.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original
            creation request may be rejected).

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/change_certificate_compartment.py.html>`__ to see an example of how to use change_certificate_compartment API.
        """
        resource_path = "/certificates/{certificateId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_certificate_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/Certificate/ChangeCertificateCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_certificate_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateId": certificate_id
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
                body=change_certificate_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_certificate_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_ca_bundle(self, create_ca_bundle_details, **kwargs):
        """
        Creates a new CA bundle according to the details of the request.


        :param oci.certificates_management.models.CreateCaBundleDetails create_ca_bundle_details: (required)
            The details of the request to create a new CA bundle.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original
            creation request may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.CaBundle`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/create_ca_bundle.py.html>`__ to see an example of how to use create_ca_bundle API.
        """
        resource_path = "/caBundles"
        method = "POST"
        operation_name = "create_ca_bundle"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CaBundle/CreateCaBundle"

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
                "create_ca_bundle got unknown kwargs: {!r}".format(extra_kwargs))

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
                header_params=header_params,
                body=create_ca_bundle_details,
                response_type="CaBundle",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_ca_bundle_details,
                response_type="CaBundle",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_certificate(self, create_certificate_details, **kwargs):
        """
        Creates a new certificate according to the details of the request.


        :param oci.certificates_management.models.CreateCertificateDetails create_certificate_details: (required)
            The details of the request to create a new certificate.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original
            creation request may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.Certificate`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/create_certificate.py.html>`__ to see an example of how to use create_certificate API.
        """
        resource_path = "/certificates"
        method = "POST"
        operation_name = "create_certificate"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/Certificate/CreateCertificate"

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
                "create_certificate got unknown kwargs: {!r}".format(extra_kwargs))

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
                header_params=header_params,
                body=create_certificate_details,
                response_type="Certificate",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_certificate_details,
                response_type="Certificate",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_certificate_authority(self, create_certificate_authority_details, **kwargs):
        """
        Creates a new certificate authority (CA) according to the details of the request.


        :param oci.certificates_management.models.CreateCertificateAuthorityDetails create_certificate_authority_details: (required)
            The details of the request to create a new CA.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original
            creation request may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.CertificateAuthority`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/create_certificate_authority.py.html>`__ to see an example of how to use create_certificate_authority API.
        """
        resource_path = "/certificateAuthorities"
        method = "POST"
        operation_name = "create_certificate_authority"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateAuthority/CreateCertificateAuthority"

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
                "create_certificate_authority got unknown kwargs: {!r}".format(extra_kwargs))

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
                header_params=header_params,
                body=create_certificate_authority_details,
                response_type="CertificateAuthority",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_certificate_authority_details,
                response_type="CertificateAuthority",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def delete_ca_bundle(self, ca_bundle_id, **kwargs):
        """
        Deletes the specified CA bundle.


        :param str ca_bundle_id: (required)
            The OCID of the CA bundle.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/delete_ca_bundle.py.html>`__ to see an example of how to use delete_ca_bundle API.
        """
        resource_path = "/caBundles/{caBundleId}"
        method = "DELETE"
        operation_name = "delete_ca_bundle"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CaBundle/DeleteCaBundle"

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
                "delete_ca_bundle got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "caBundleId": ca_bundle_id
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

    def get_association(self, association_id, **kwargs):
        """
        Gets details about the specified association.


        :param str association_id: (required)
            The OCID of an association between a certificate-related resource and another Oracle Cloud Infrastructure resource.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.Association`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/get_association.py.html>`__ to see an example of how to use get_association API.
        """
        resource_path = "/associations/{associationId}"
        method = "GET"
        operation_name = "get_association"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/Association/GetAssociation"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_association got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "associationId": association_id
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
                response_type="Association",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Association",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_ca_bundle(self, ca_bundle_id, **kwargs):
        """
        Gets details about the specified CA bundle.


        :param str ca_bundle_id: (required)
            The OCID of the CA bundle.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.CaBundle`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/get_ca_bundle.py.html>`__ to see an example of how to use get_ca_bundle API.
        """
        resource_path = "/caBundles/{caBundleId}"
        method = "GET"
        operation_name = "get_ca_bundle"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CaBundle/GetCaBundle"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_ca_bundle got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "caBundleId": ca_bundle_id
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
                response_type="CaBundle",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="CaBundle",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_certificate(self, certificate_id, **kwargs):
        """
        Gets details about the specified certificate.


        :param str certificate_id: (required)
            The OCID of the certificate.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.Certificate`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/get_certificate.py.html>`__ to see an example of how to use get_certificate API.
        """
        resource_path = "/certificates/{certificateId}"
        method = "GET"
        operation_name = "get_certificate"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/Certificate/GetCertificate"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_certificate got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateId": certificate_id
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
                response_type="Certificate",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Certificate",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_certificate_authority(self, certificate_authority_id, **kwargs):
        """
        Gets details about the specified certificate authority (CA).


        :param str certificate_authority_id: (required)
            The OCID of the certificate authority (CA).

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.CertificateAuthority`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/get_certificate_authority.py.html>`__ to see an example of how to use get_certificate_authority API.
        """
        resource_path = "/certificateAuthorities/{certificateAuthorityId}"
        method = "GET"
        operation_name = "get_certificate_authority"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateAuthority/GetCertificateAuthority"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_certificate_authority got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateAuthorityId": certificate_authority_id
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
                response_type="CertificateAuthority",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="CertificateAuthority",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_certificate_authority_version(self, certificate_authority_id, certificate_authority_version_number, **kwargs):
        """
        Gets details about the specified certificate authority (CA) version.


        :param str certificate_authority_id: (required)
            The OCID of the certificate authority (CA).

        :param int certificate_authority_version_number: (required)
            The version number of the certificate authority (CA).

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.CertificateAuthorityVersion`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/get_certificate_authority_version.py.html>`__ to see an example of how to use get_certificate_authority_version API.
        """
        resource_path = "/certificateAuthorities/{certificateAuthorityId}/version/{certificateAuthorityVersionNumber}"
        method = "GET"
        operation_name = "get_certificate_authority_version"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateAuthorityVersion/GetCertificateAuthorityVersion"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_certificate_authority_version got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateAuthorityId": certificate_authority_id,
            "certificateAuthorityVersionNumber": certificate_authority_version_number
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
                response_type="CertificateAuthorityVersion",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="CertificateAuthorityVersion",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_certificate_version(self, certificate_id, certificate_version_number, **kwargs):
        """
        Gets details about the specified version of a certificate.


        :param str certificate_id: (required)
            The OCID of the certificate.

        :param int certificate_version_number: (required)
            The version number of the certificate.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.CertificateVersion`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/get_certificate_version.py.html>`__ to see an example of how to use get_certificate_version API.
        """
        resource_path = "/certificates/{certificateId}/version/{certificateVersionNumber}"
        method = "GET"
        operation_name = "get_certificate_version"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateVersion/GetCertificateVersion"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_certificate_version got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateId": certificate_id,
            "certificateVersionNumber": certificate_version_number
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
                response_type="CertificateVersion",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="CertificateVersion",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_associations(self, **kwargs):
        """
        Lists all associations that match the query parameters.
        Optionally, you can use the parameter `FilterByAssociationIdQueryParam` to limit the result set to a single item that matches the specified association.


        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str compartment_id: (optional)
            A filter that returns only resources that match the given compartment OCID.

        :param str certificates_resource_id: (optional)
            A filter that returns only resources that match the given OCID of a certificate-related resource.

        :param str associated_resource_id: (optional)
            A filter that returns only resources that match the given OCID of an associated Oracle Cloud Infrastructure resource.

        :param str association_id: (optional)
            The OCID of the association. If the parameter is set to null, the service lists all associations.

        :param str name: (optional)
            A filter that returns only resources that match the specified name.

        :param str sort_by: (optional)
            The field to sort by. You can specify only one sort order. The default order for `TIMECREATED` is descending.
            The default order for `NAME` is ascending.

            Allowed values are: "NAME", "TIMECREATED"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param str page: (optional)
            The value of the `opc-next-page` response header
            from the previous \"List\" call.

        :param str association_type: (optional)
            Type of associations to list. If the parameter is set to null, the service lists all types of associations.

            Allowed values are: "CERTIFICATE", "CERTIFICATE_AUTHORITY", "CA_BUNDLE"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.AssociationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/list_associations.py.html>`__ to see an example of how to use list_associations API.
        """
        resource_path = "/associations"
        method = "GET"
        operation_name = "list_associations"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/AssociationSummary/ListAssociations"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "compartment_id",
            "certificates_resource_id",
            "associated_resource_id",
            "association_id",
            "name",
            "sort_by",
            "sort_order",
            "limit",
            "page",
            "association_type"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_associations got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["NAME", "TIMECREATED"]
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

        if 'association_type' in kwargs:
            association_type_allowed_values = ["CERTIFICATE", "CERTIFICATE_AUTHORITY", "CA_BUNDLE"]
            if kwargs['association_type'] not in association_type_allowed_values:
                raise ValueError(
                    "Invalid value for `association_type`, must be one of {0}".format(association_type_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "certificatesResourceId": kwargs.get("certificates_resource_id", missing),
            "associatedResourceId": kwargs.get("associated_resource_id", missing),
            "associationId": kwargs.get("association_id", missing),
            "name": kwargs.get("name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "associationType": kwargs.get("association_type", missing)
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
                query_params=query_params,
                header_params=header_params,
                response_type="AssociationCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="AssociationCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_ca_bundles(self, **kwargs):
        """
        Lists all CA bundles that match the query parameters.
        Optionally, you can use the parameter `FilterByCaBundleIdQueryParam` to limit the result set to a single item that matches the specified CA bundle.


        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str compartment_id: (optional)
            A filter that returns only resources that match the given compartment OCID.

        :param str lifecycle_state: (optional)
            A filter that returns only resources that match the given lifecycle state. The state value is case-insensitive.

            Allowed values are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"

        :param str name: (optional)
            A filter that returns only resources that match the specified name.

        :param str sort_by: (optional)
            The field to sort by. You can specify only one sort order. The default order for `TIMECREATED` is descending.
            The default order for `NAME` is ascending.

            Allowed values are: "NAME", "TIMECREATED"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param str page: (optional)
            The value of the `opc-next-page` response header
            from the previous \"List\" call.

        :param str ca_bundle_id: (optional)
            The OCID of the CA bundle.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.CaBundleCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/list_ca_bundles.py.html>`__ to see an example of how to use list_ca_bundles API.
        """
        resource_path = "/caBundles"
        method = "GET"
        operation_name = "list_ca_bundles"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CaBundleSummary/ListCaBundles"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "compartment_id",
            "lifecycle_state",
            "name",
            "sort_by",
            "sort_order",
            "limit",
            "page",
            "ca_bundle_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_ca_bundles got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["NAME", "TIMECREATED"]
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
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "name": kwargs.get("name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "caBundleId": kwargs.get("ca_bundle_id", missing)
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
                query_params=query_params,
                header_params=header_params,
                response_type="CaBundleCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="CaBundleCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_certificate_authorities(self, **kwargs):
        """
        Lists all certificate authorities (CAs) in the specified compartment.
        Optionally, you can use the parameter `FilterByCertificateAuthorityIdQueryParam` to limit the results to a single item that matches the specified CA.


        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str compartment_id: (optional)
            A filter that returns only resources that match the given compartment OCID.

        :param str lifecycle_state: (optional)
            A filter that returns only resources that match the given lifecycle state. The state value is case-insensitive.

            Allowed values are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"

        :param str name: (optional)
            A filter that returns only resources that match the specified name.

        :param str issuer_certificate_authority_id: (optional)
            The OCID of the certificate authority (CA). If the parameter is set to null, the service lists all CAs.

        :param str certificate_authority_id: (optional)
            The OCID of the certificate authority (CA). If the parameter is set to null, the service lists all CAs.

        :param str sort_by: (optional)
            The field to sort by. You can specify only one sort order. The default
            order for `EXPIRATIONDATE` and 'TIMECREATED' is descending. The default order for `NAME`
            is ascending.

            Allowed values are: "NAME", "EXPIRATIONDATE", "TIMECREATED"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param str page: (optional)
            The value of the `opc-next-page` response header
            from the previous \"List\" call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.CertificateAuthorityCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/list_certificate_authorities.py.html>`__ to see an example of how to use list_certificate_authorities API.
        """
        resource_path = "/certificateAuthorities"
        method = "GET"
        operation_name = "list_certificate_authorities"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateAuthoritySummary/ListCertificateAuthorities"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "compartment_id",
            "lifecycle_state",
            "name",
            "issuer_certificate_authority_id",
            "certificate_authority_id",
            "sort_by",
            "sort_order",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_certificate_authorities got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["NAME", "EXPIRATIONDATE", "TIMECREATED"]
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
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "name": kwargs.get("name", missing),
            "issuerCertificateAuthorityId": kwargs.get("issuer_certificate_authority_id", missing),
            "certificateAuthorityId": kwargs.get("certificate_authority_id", missing),
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
                response_type="CertificateAuthorityCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="CertificateAuthorityCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_certificate_authority_versions(self, certificate_authority_id, **kwargs):
        """
        Lists all versions for the specified certificate authority (CA).
        Optionally, you can use the parameter `FilterByVersionNumberQueryParam` to limit the results to a single item that matches the specified version number.


        :param str certificate_authority_id: (required)
            The OCID of the certificate authority (CA).

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param int version_number: (optional)
            A filter that returns only resources that match the specified version number. The default value is 0, which means that this filter is not applied.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param str page: (optional)
            The value of the `opc-next-page` response header
            from the previous \"List\" call.

        :param str sort_by: (optional)
            The field to sort by. You can specify only one sort order. The default order for 'VERSION_NUMBER' is ascending.

            Allowed values are: "VERSION_NUMBER"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.CertificateAuthorityVersionCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/list_certificate_authority_versions.py.html>`__ to see an example of how to use list_certificate_authority_versions API.
        """
        resource_path = "/certificateAuthorities/{certificateAuthorityId}/versions"
        method = "GET"
        operation_name = "list_certificate_authority_versions"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateAuthorityVersionSummary/ListCertificateAuthorityVersions"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "version_number",
            "limit",
            "page",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_certificate_authority_versions got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateAuthorityId": certificate_authority_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["VERSION_NUMBER"]
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
            "versionNumber": kwargs.get("version_number", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
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
                response_type="CertificateAuthorityVersionCollection",
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
                response_type="CertificateAuthorityVersionCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_certificate_versions(self, certificate_id, **kwargs):
        """
        Lists all certificate versions for the specified certificate.
        Optionally, you can use the parameter `FilterByVersionNumberQueryParam` to limit the result set to a single item that matches the specified version number.


        :param str certificate_id: (required)
            The OCID of the certificate.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param int version_number: (optional)
            A filter that returns only resources that match the specified version number. The default value is 0, which means that this filter is not applied.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param str page: (optional)
            The value of the `opc-next-page` response header
            from the previous \"List\" call.

        :param str sort_by: (optional)
            The field to sort by. You can specify only one sort order. The default order for 'VERSION_NUMBER' is ascending.

            Allowed values are: "VERSION_NUMBER"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.CertificateVersionCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/list_certificate_versions.py.html>`__ to see an example of how to use list_certificate_versions API.
        """
        resource_path = "/certificates/{certificateId}/versions"
        method = "GET"
        operation_name = "list_certificate_versions"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateVersionSummary/ListCertificateVersions"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "version_number",
            "limit",
            "page",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_certificate_versions got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateId": certificate_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["VERSION_NUMBER"]
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
            "versionNumber": kwargs.get("version_number", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
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
                response_type="CertificateVersionCollection",
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
                response_type="CertificateVersionCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_certificates(self, **kwargs):
        """
        Lists all certificates that match the query parameters.
        Optionally, you can use the parameter `FilterByCertificateIdQueryParam` to limit the result set to a single item that matches the specified certificate.


        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str compartment_id: (optional)
            A filter that returns only resources that match the given compartment OCID.

        :param str lifecycle_state: (optional)
            A filter that returns only resources that match the given lifecycle state. The state value is case-insensitive.

            Allowed values are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"

        :param str name: (optional)
            A filter that returns only resources that match the specified name.

        :param str sort_by: (optional)
            The field to sort by. You can specify only one sort order. The default
            order for `EXPIRATIONDATE` and 'TIMECREATED' is descending. The default order for `NAME`
            is ascending.

            Allowed values are: "NAME", "EXPIRATIONDATE", "TIMECREATED"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param str page: (optional)
            The value of the `opc-next-page` response header
            from the previous \"List\" call.

        :param str issuer_certificate_authority_id: (optional)
            The OCID of the certificate authority (CA). If the parameter is set to null, the service lists all CAs.

        :param str certificate_id: (optional)
            The OCID of the certificate. If the parameter is set to null, the service lists all certificates.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.CertificateCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/list_certificates.py.html>`__ to see an example of how to use list_certificates API.
        """
        resource_path = "/certificates"
        method = "GET"
        operation_name = "list_certificates"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateSummary/ListCertificates"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "compartment_id",
            "lifecycle_state",
            "name",
            "sort_by",
            "sort_order",
            "limit",
            "page",
            "issuer_certificate_authority_id",
            "certificate_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_certificates got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["NAME", "EXPIRATIONDATE", "TIMECREATED"]
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
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "name": kwargs.get("name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "issuerCertificateAuthorityId": kwargs.get("issuer_certificate_authority_id", missing),
            "certificateId": kwargs.get("certificate_id", missing)
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
                query_params=query_params,
                header_params=header_params,
                response_type="CertificateCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="CertificateCollection",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def revoke_certificate_authority_version(self, certificate_authority_id, certificate_authority_version_number, revoke_certificate_authority_version_details, **kwargs):
        """
        Revokes a certificate authority (CA) version.


        :param str certificate_authority_id: (required)
            The OCID of the certificate authority (CA).

        :param int certificate_authority_version_number: (required)
            The version number of the certificate authority (CA).

        :param oci.certificates_management.models.RevokeCertificateAuthorityVersionDetails revoke_certificate_authority_version_details: (required)
            The details of the request to revoke a CA version.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original
            creation request may be rejected).

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/revoke_certificate_authority_version.py.html>`__ to see an example of how to use revoke_certificate_authority_version API.
        """
        resource_path = "/certificateAuthorities/{certificateAuthorityId}/version/{certificateAuthorityVersionNumber}/actions/revoke"
        method = "POST"
        operation_name = "revoke_certificate_authority_version"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateAuthorityVersion/RevokeCertificateAuthorityVersion"

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
                "revoke_certificate_authority_version got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateAuthorityId": certificate_authority_id,
            "certificateAuthorityVersionNumber": certificate_authority_version_number
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
                body=revoke_certificate_authority_version_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=revoke_certificate_authority_version_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def revoke_certificate_version(self, certificate_id, certificate_version_number, revoke_certificate_version_details, **kwargs):
        """
        Revokes the specified certificate version.


        :param str certificate_id: (required)
            The OCID of the certificate.

        :param int certificate_version_number: (required)
            The version number of the certificate.

        :param oci.certificates_management.models.RevokeCertificateVersionDetails revoke_certificate_version_details: (required)
            The details of the request to revoke a certificate version.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (for example, if a resource has been
            deleted and purged from the system, then a retry of the original
            creation request may be rejected).

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/revoke_certificate_version.py.html>`__ to see an example of how to use revoke_certificate_version API.
        """
        resource_path = "/certificates/{certificateId}/version/{certificateVersionNumber}/actions/revoke"
        method = "POST"
        operation_name = "revoke_certificate_version"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateVersion/RevokeCertificateVersion"

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
                "revoke_certificate_version got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateId": certificate_id,
            "certificateVersionNumber": certificate_version_number
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
                body=revoke_certificate_version_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=revoke_certificate_version_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def schedule_certificate_authority_deletion(self, certificate_authority_id, schedule_certificate_authority_deletion_details, **kwargs):
        """
        Schedules the deletion of the specified certificate authority (CA). This sets the lifecycle state of the CA to `PENDING_DELETION` and then deletes it after the specified retention period ends. If needed, you can determine the status of the deletion by using `GetCertificateAuthority`.


        :param str certificate_authority_id: (required)
            The OCID of the certificate authority (CA).

        :param oci.certificates_management.models.ScheduleCertificateAuthorityDeletionDetails schedule_certificate_authority_deletion_details: (required)
            The details of the request to schedule the deletion of a CA.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/schedule_certificate_authority_deletion.py.html>`__ to see an example of how to use schedule_certificate_authority_deletion API.
        """
        resource_path = "/certificateAuthorities/{certificateAuthorityId}/actions/scheduleDeletion"
        method = "POST"
        operation_name = "schedule_certificate_authority_deletion"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateAuthority/ScheduleCertificateAuthorityDeletion"

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
                "schedule_certificate_authority_deletion got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateAuthorityId": certificate_authority_id
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
                header_params=header_params,
                body=schedule_certificate_authority_deletion_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=schedule_certificate_authority_deletion_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def schedule_certificate_authority_version_deletion(self, certificate_authority_id, certificate_authority_version_number, schedule_certificate_authority_version_deletion_details, **kwargs):
        """
        Schedules the deletion of the specified certificate authority (CA) version.
        This sets the lifecycle state of the CA version to `PENDING_DELETION`
        and then deletes it after the specified retention period ends. If needed, you can determine the status of the deletion by using `GetCertificateAuthorityVersion`.


        :param str certificate_authority_id: (required)
            The OCID of the certificate authority (CA).

        :param int certificate_authority_version_number: (required)
            The version number of the certificate authority (CA).

        :param oci.certificates_management.models.ScheduleCertificateAuthorityVersionDeletionDetails schedule_certificate_authority_version_deletion_details: (required)
            The details of the request to delete a CA version.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/schedule_certificate_authority_version_deletion.py.html>`__ to see an example of how to use schedule_certificate_authority_version_deletion API.
        """
        resource_path = "/certificateAuthorities/{certificateAuthorityId}/version/{certificateAuthorityVersionNumber}/actions/scheduleDeletion"
        method = "POST"
        operation_name = "schedule_certificate_authority_version_deletion"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateAuthorityVersion/ScheduleCertificateAuthorityVersionDeletion"

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
                "schedule_certificate_authority_version_deletion got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateAuthorityId": certificate_authority_id,
            "certificateAuthorityVersionNumber": certificate_authority_version_number
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
                header_params=header_params,
                body=schedule_certificate_authority_version_deletion_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=schedule_certificate_authority_version_deletion_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def schedule_certificate_deletion(self, certificate_id, schedule_certificate_deletion_details, **kwargs):
        """
        Schedules the deletion of the specified certificate. This sets the lifecycle state of the certificate
        to `PENDING_DELETION` and then deletes it after the specified retention period ends.
        You can subsequently use `GetCertificate` to determine the current deletion status.


        :param str certificate_id: (required)
            The OCID of the certificate.

        :param oci.certificates_management.models.ScheduleCertificateDeletionDetails schedule_certificate_deletion_details: (required)
            The details of the request to schedule a certificate deletion.
            This sets the lifecycle state of the certificate to `PENDING_DELETION` and then deletes it
            after the specified retention period ends.
            You can subsequently use `GetCertificate` to determine the current deletion status.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/schedule_certificate_deletion.py.html>`__ to see an example of how to use schedule_certificate_deletion API.
        """
        resource_path = "/certificates/{certificateId}/actions/scheduleDeletion"
        method = "POST"
        operation_name = "schedule_certificate_deletion"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/Certificate/ScheduleCertificateDeletion"

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
                "schedule_certificate_deletion got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateId": certificate_id
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
                header_params=header_params,
                body=schedule_certificate_deletion_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=schedule_certificate_deletion_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def schedule_certificate_version_deletion(self, certificate_id, certificate_version_number, schedule_certificate_version_deletion_details, **kwargs):
        """
        Schedules the deletion of the specified certificate version. This sets the lifecycle state of the certificate version to `PENDING_DELETION` and then deletes it after the specified retention period ends. You can only
        delete a certificate version if the certificate version rotation state is marked as `DEPRECATED`.

        You can subsequently use `GetCertificateVersion` to determine the current certificate version deletion status.


        :param str certificate_id: (required)
            The OCID of the certificate.

        :param int certificate_version_number: (required)
            The version number of the certificate.

        :param oci.certificates_management.models.ScheduleCertificateVersionDeletionDetails schedule_certificate_version_deletion_details: (required)
            The details of the request to delete a certificate version.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/schedule_certificate_version_deletion.py.html>`__ to see an example of how to use schedule_certificate_version_deletion API.
        """
        resource_path = "/certificates/{certificateId}/version/{certificateVersionNumber}/actions/scheduleDeletion"
        method = "POST"
        operation_name = "schedule_certificate_version_deletion"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateVersion/ScheduleCertificateVersionDeletion"

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
                "schedule_certificate_version_deletion got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateId": certificate_id,
            "certificateVersionNumber": certificate_version_number
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
                header_params=header_params,
                body=schedule_certificate_version_deletion_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=schedule_certificate_version_deletion_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_ca_bundle(self, ca_bundle_id, update_ca_bundle_details, **kwargs):
        """
        Updates the properties of a CA bundle.


        :param str ca_bundle_id: (required)
            The OCID of the CA bundle.

        :param oci.certificates_management.models.UpdateCaBundleDetails update_ca_bundle_details: (required)
            The details of the request to update a CA bundle.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.CaBundle`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/update_ca_bundle.py.html>`__ to see an example of how to use update_ca_bundle API.
        """
        resource_path = "/caBundles/{caBundleId}"
        method = "PUT"
        operation_name = "update_ca_bundle"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CaBundle/UpdateCaBundle"

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
                "update_ca_bundle got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "caBundleId": ca_bundle_id
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
                header_params=header_params,
                body=update_ca_bundle_details,
                response_type="CaBundle",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_ca_bundle_details,
                response_type="CaBundle",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_certificate(self, certificate_id, update_certificate_details, **kwargs):
        """
        Updates the properties of a certificate.


        :param str certificate_id: (required)
            The OCID of the certificate.

        :param oci.certificates_management.models.UpdateCertificateDetails update_certificate_details: (required)
            The details of the request to update a certificate.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.Certificate`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/update_certificate.py.html>`__ to see an example of how to use update_certificate API.
        """
        resource_path = "/certificates/{certificateId}"
        method = "PUT"
        operation_name = "update_certificate"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/Certificate/UpdateCertificate"

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
                "update_certificate got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateId": certificate_id
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
                header_params=header_params,
                body=update_certificate_details,
                response_type="Certificate",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_certificate_details,
                response_type="Certificate",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_certificate_authority(self, certificate_authority_id, update_certificate_authority_details, **kwargs):
        """
        Updates the properties of the specified certificate authority (CA).


        :param str certificate_authority_id: (required)
            The OCID of the certificate authority (CA).

        :param oci.certificates_management.models.UpdateCertificateAuthorityDetails update_certificate_authority_details: (required)
            The details of the request to update a CA.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.certificates_management.models.CertificateAuthority`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/certificatesmanagement/update_certificate_authority.py.html>`__ to see an example of how to use update_certificate_authority API.
        """
        resource_path = "/certificateAuthorities/{certificateAuthorityId}"
        method = "PUT"
        operation_name = "update_certificate_authority"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/certificatesmgmt/20210224/CertificateAuthority/UpdateCertificateAuthority"

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
                "update_certificate_authority got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateAuthorityId": certificate_authority_id
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
                header_params=header_params,
                body=update_certificate_authority_details,
                response_type="CertificateAuthority",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_certificate_authority_details,
                response_type="CertificateAuthority",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
