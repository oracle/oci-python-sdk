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
from oci.util import back_up_body_calculate_stream_content_length, is_content_length_calculable_by_req_util
from .models import key_management_type_mapping
missing = Sentinel("Missing")


class KmsVaultClient(object):
    """
    API for managing and performing operations with keys and vaults. (For the API for managing secrets, see the Vault Service
    Secret Management API. For the API for retrieving secrets, see the Vault Service Secret Retrieval API.)
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
            'base_path': '/',
            'service_endpoint_template': 'https://kms.{region}.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'circuit_breaker_strategy': kwargs.get('circuit_breaker_strategy', circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY)
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        if base_client_init_kwargs.get('circuit_breaker_strategy') is None:
            base_client_init_kwargs['circuit_breaker_strategy'] = circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY
        if 'allow_control_chars' in kwargs:
            base_client_init_kwargs['allow_control_chars'] = kwargs.get('allow_control_chars')
        self.base_client = BaseClient("kms_vault", config, signer, key_management_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

    def backup_vault(self, vault_id, **kwargs):
        """
        Backs up an encrypted file that contains all the metadata of a vault so that you can restore the vault later.
        You can backup a vault whether or not it contains keys. This operation only backs up the
        metadata of the vault, and does not include key metadata.


        :param str vault_id: (required)
            The OCID of the vault.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (e.g., if a resource has been
            deleted and purged from the system, then a retry of the original
            creation request may be rejected).

        :param oci.key_management.models.BackupVaultDetails backup_vault_details: (optional)
            BackupVaultDetails

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.key_management.models.Vault`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/keymanagement/backup_vault.py.html>`__ to see an example of how to use backup_vault API.
        """
        resource_path = "/20180608/vaults/{vaultId}/actions/backup"
        method = "POST"
        operation_name = "backup_vault"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token",
            "backup_vault_details"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "backup_vault got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vaultId": vault_id
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
                body=kwargs.get('backup_vault_details'),
                response_type="Vault",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=kwargs.get('backup_vault_details'),
                response_type="Vault",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def cancel_vault_deletion(self, vault_id, **kwargs):
        """
        Cancels the scheduled deletion of the specified vault. Canceling a scheduled deletion
        restores the vault and all keys in it to their respective states from before their
        scheduled deletion. All keys that were scheduled for deletion prior to vault
        deletion retain their lifecycle state and time of deletion.

        As a provisioning operation, this call is subject to a Key Management limit that applies to
        the total number of requests across all provisioning write operations. Key Management might
        throttle this call to reject an otherwise valid request when the total rate of provisioning
        write operations exceeds 10 requests per second for a given tenancy.


        :param str vault_id: (required)
            The OCID of the vault.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (e.g., if a resource has been
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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.key_management.models.Vault`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/keymanagement/cancel_vault_deletion.py.html>`__ to see an example of how to use cancel_vault_deletion API.
        """
        resource_path = "/20180608/vaults/{vaultId}/actions/cancelDeletion"
        method = "POST"
        operation_name = "cancel_vault_deletion"
        api_reference_link = ""

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
                "cancel_vault_deletion got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vaultId": vault_id
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
                response_type="Vault",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Vault",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def change_vault_compartment(self, vault_id, change_vault_compartment_details, **kwargs):
        """
        Moves a vault into a different compartment within the same tenancy. For information about
        moving resources between compartments, see `Moving Resources to a Different Compartment`__.

        When provided, if-match is checked against the ETag values of the resource.

        As a provisioning operation, this call is subject to a Key Management limit that applies to
        the total number of requests across all provisioning write operations. Key Management might
        throttle this call to reject an otherwise valid request when the total rate of provisioning
        write operations exceeds 10 requests per second for a given tenancy.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str vault_id: (required)
            The OCID of the vault.

        :param oci.key_management.models.ChangeVaultCompartmentDetails change_vault_compartment_details: (required)

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (e.g., if a resource has been
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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/keymanagement/change_vault_compartment.py.html>`__ to see an example of how to use change_vault_compartment API.
        """
        resource_path = "/20180608/vaults/{vaultId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_vault_compartment"
        api_reference_link = ""

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
                "change_vault_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vaultId": vault_id
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
                body=change_vault_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_vault_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_vault(self, create_vault_details, **kwargs):
        """
        Creates a new vault. The type of vault you create determines key placement, pricing, and
        available options. Options include storage isolation, a dedicated service endpoint instead
        of a shared service endpoint for API calls, and either a dedicated hardware security module
        (HSM) or a multitenant HSM.

        As a provisioning operation, this call is subject to a Key Management limit that applies to
        the total number of requests across all provisioning write operations. Key Management might
        throttle this call to reject an otherwise valid request when the total rate of provisioning
        write operations exceeds 10 requests per second for a given tenancy.


        :param oci.key_management.models.CreateVaultDetails create_vault_details: (required)
            CreateVaultDetails

        :param str opc_request_id: (optional)
            Unique identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (e.g., if a resource has been
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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.key_management.models.Vault`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/keymanagement/create_vault.py.html>`__ to see an example of how to use create_vault API.
        """
        resource_path = "/20180608/vaults"
        method = "POST"
        operation_name = "create_vault"
        api_reference_link = ""

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
                "create_vault got unknown kwargs: {!r}".format(extra_kwargs))

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
                body=create_vault_details,
                response_type="Vault",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_vault_details,
                response_type="Vault",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_vault_replica(self, vault_id, create_vault_replica_details, **kwargs):
        """
        Creates a replica for the vault in another region in the same realm

        The API is a no-op if called for same region that a vault is already replicated to.
        409 if called on a vault that is already replicated to a different region. Users need to delete
        existing replica first before calling it with a different region.

        As a provisioning operation, this call is subject to a Key Management limit that applies to
        the total number of requests across all provisioning write operations. Key Management might
        throttle this call to reject an otherwise valid request when the total rate of provisioning
        write operations exceeds 10 requests per second for a given tenancy.


        :param str vault_id: (required)
            The OCID of the vault.

        :param oci.key_management.models.CreateVaultReplicaDetails create_vault_replica_details: (required)
            CreateVaultReplicaDetails

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (e.g., if a resource has been
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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/keymanagement/create_vault_replica.py.html>`__ to see an example of how to use create_vault_replica API.
        """
        resource_path = "/20180608/vaults/{vaultId}/actions/createReplica"
        method = "POST"
        operation_name = "create_vault_replica"
        api_reference_link = ""

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
                "create_vault_replica got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vaultId": vault_id
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
                body=create_vault_replica_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_vault_replica_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def delete_vault_replica(self, vault_id, delete_vault_replica_details, **kwargs):
        """
        Deletes a vault replica

        As a provisioning operation, this call is subject to a Key Management limit that applies to
        the total number of requests across all provisioning write operations. Key Management might
        throttle this call to reject an otherwise valid request when the total rate of provisioning
        write operations exceeds 10 requests per second for a given tenancy.


        :param str vault_id: (required)
            The OCID of the vault.

        :param oci.key_management.models.DeleteVaultReplicaDetails delete_vault_replica_details: (required)
            DeleteVaultReplicaDetails

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (e.g., if a resource has been
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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/keymanagement/delete_vault_replica.py.html>`__ to see an example of how to use delete_vault_replica API.
        """
        resource_path = "/20180608/vaults/{vaultId}/actions/deleteReplica"
        method = "POST"
        operation_name = "delete_vault_replica"
        api_reference_link = ""

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
                "delete_vault_replica got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vaultId": vault_id
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
                body=delete_vault_replica_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=delete_vault_replica_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_vault(self, vault_id, **kwargs):
        """
        Gets the specified vault's configuration information.

        As a provisioning operation, this call is subject to a Key Management limit that applies to
        the total number of requests across all provisioning read operations. Key Management might
        throttle this call to reject an otherwise valid request when the total rate of provisioning
        read operations exceeds 10 requests per second for a given tenancy.


        :param str vault_id: (required)
            The OCID of the vault.

        :param str opc_request_id: (optional)
            Unique identifier for the request. If provided, the returned request ID
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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.key_management.models.Vault`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/keymanagement/get_vault.py.html>`__ to see an example of how to use get_vault API.
        """
        resource_path = "/20180608/vaults/{vaultId}"
        method = "GET"
        operation_name = "get_vault"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_vault got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vaultId": vault_id
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
                response_type="Vault",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Vault",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_vault_usage(self, vault_id, **kwargs):
        """
        Gets the count of keys and key versions in the specified vault to calculate usage against service limits.


        :param str vault_id: (required)
            The OCID of the vault.

        :param str opc_request_id: (optional)
            Unique identifier for the request. If provided, the returned request ID
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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.key_management.models.VaultUsage`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/keymanagement/get_vault_usage.py.html>`__ to see an example of how to use get_vault_usage API.
        """
        resource_path = "/20180608/vaults/{vaultId}/usage"
        method = "GET"
        operation_name = "get_vault_usage"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_vault_usage got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vaultId": vault_id
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
                response_type="VaultUsage",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="VaultUsage",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_vault_replicas(self, vault_id, **kwargs):
        """
        Lists the replicas for a vault

        As a provisioning operation, this call is subject to a Key Management limit that applies to
        the total number of requests across all provisioning write operations. Key Management might
        throttle this call to reject an otherwise valid request when the total rate of provisioning
        write operations exceeds 10 requests per second for a given tenancy.


        :param str vault_id: (required)
            The OCID of the vault.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param str page: (optional)
            The value of the `opc-next-page` response header
            from the previous \"List\" call.

        :param str opc_request_id: (optional)
            Unique identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (e.g., if a resource has been
            deleted and purged from the system, then a retry of the original
            creation request may be rejected).

        :param str sort_by: (optional)
            The field to sort by. You can specify only one sort order. The default
            order for `TIMECREATED` is descending. The default order for `DISPLAYNAME`
            is ascending.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

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

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.key_management.models.VaultReplicaSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/keymanagement/list_vault_replicas.py.html>`__ to see an example of how to use list_vault_replicas API.
        """
        resource_path = "/20180608/vaults/{vaultId}/actions/listReplicas"
        method = "GET"
        operation_name = "list_vault_replicas"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "limit",
            "page",
            "opc_request_id",
            "opc_retry_token",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_vault_replicas got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vaultId": vault_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

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
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
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
                query_params=query_params,
                header_params=header_params,
                response_type="list[VaultReplicaSummary]",
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
                response_type="list[VaultReplicaSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_vaults(self, compartment_id, **kwargs):
        """
        Lists the vaults in the specified compartment.

        As a provisioning operation, this call is subject to a Key Management limit that applies to
        the total number of requests across all provisioning read operations. Key Management might
        throttle this call to reject an otherwise valid request when the total rate of provisioning
        read operations exceeds 10 requests per second for a given tenancy.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param str page: (optional)
            The value of the `opc-next-page` response header
            from the previous \"List\" call.

        :param str opc_request_id: (optional)
            Unique identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str sort_by: (optional)
            The field to sort by. You can specify only one sort order. The default
            order for `TIMECREATED` is descending. The default order for `DISPLAYNAME`
            is ascending.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

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

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.key_management.models.VaultSummary`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/keymanagement/list_vaults.py.html>`__ to see an example of how to use list_vaults API.
        """
        resource_path = "/20180608/vaults"
        method = "GET"
        operation_name = "list_vaults"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "limit",
            "page",
            "opc_request_id",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_vaults got unknown kwargs: {!r}".format(extra_kwargs))

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
            "compartmentId": compartment_id,
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
                query_params=query_params,
                header_params=header_params,
                response_type="list[VaultSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VaultSummary]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def restore_vault_from_file(self, compartment_id, restore_vault_from_file_details, **kwargs):
        """
        Restores a vault from an encrypted backup file. If a vault
        with the same OCID already exists, this operation returns a response with a
        409 HTTP status error code.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param stream restore_vault_from_file_details: (required)
            The encrypted backup file to upload to restore the vault.

        :param int content_length: (optional)
            The content length of the body.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param str content_md5: (optional)
            The base64-encoded MD5 hash value of the body, as described in `RFC 2616`__, section 14.15.
            If the Content-MD5 header is present, Key Management performs an integrity check on the body of the HTTP request by computing the MD5
            hash for the body and comparing it to the MD5 hash supplied in the header. If the two hashes don't match, the object is rejected and
            a response with 400 Unmatched Content MD5 error is returned, along with the message: \"The computed MD5 of the request body (ACTUAL_MD5)
            does not match the Content-MD5 header (HEADER_MD5).\"

            __ https://tools.ietf.org/rfc/rfc2616

        :param str opc_request_id: (optional)
            Unique identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (e.g., if a resource has been
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
        :param int buffer_limit: (optional)
            A buffer limit for the stream to be buffered. buffer_limit is used to set the buffer size capacity. Streams will be read until the size of the buffer reaches the buffer_limit.
            If the stream size is greater than the buffer_limit, a BufferError exception will be thrown.

            The buffer_limit parameter is used when the stream object does not have a `seek`, `tell`, or `fileno` property for the Python Request library to calculate out the content length.
            If buffer_limit is not passed, then the buffer_limit will be defaulted to 100MB.
            Large streams can cause the process to freeze, consider passing in content-length for large streams instead.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.key_management.models.Vault`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/keymanagement/restore_vault_from_file.py.html>`__ to see an example of how to use restore_vault_from_file API.
        """
        resource_path = "/20180608/vaults/actions/restoreFromFile"
        method = "POST"
        operation_name = "restore_vault_from_file"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "buffer_limit",
            "content_length",
            "if_match",
            "content_md5",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "restore_vault_from_file got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-length": kwargs.get("content_length", missing),
            "if-match": kwargs.get("if_match", missing),
            "content-md5": kwargs.get("content_md5", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        # If the body parameter is optional we need to assign it to a variable so additional type checking can be performed.
        try:
            restore_vault_from_file_details
        except NameError:
            restore_vault_from_file_details = kwargs.get("restore_vault_from_file_details", missing)

        if restore_vault_from_file_details is not missing and restore_vault_from_file_details is not None:
            if (not isinstance(restore_vault_from_file_details, (six.binary_type, six.string_types)) and
                    not hasattr(restore_vault_from_file_details, "read")):
                raise TypeError('The body must be a string, bytes, or provide a read() method.')

            if hasattr(restore_vault_from_file_details, 'fileno') and hasattr(restore_vault_from_file_details, 'name') and restore_vault_from_file_details.name != '<stdin>':
                if requests.utils.super_len(restore_vault_from_file_details) == 0:
                    header_params['Content-Length'] = '0'

            # If content length is not given and stream object have no 'fileno' and is not a string or bytes, try to calculate content length
            elif 'Content-Length' not in header_params and not is_content_length_calculable_by_req_util(restore_vault_from_file_details):
                calculated_obj = back_up_body_calculate_stream_content_length(restore_vault_from_file_details, kwargs.get("buffer_limit"))
                header_params['Content-Length'] = calculated_obj["content_length"]
                restore_vault_from_file_details = calculated_obj["byte_content"]

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
                query_params=query_params,
                header_params=header_params,
                body=restore_vault_from_file_details,
                response_type="Vault",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=restore_vault_from_file_details,
                response_type="Vault",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def restore_vault_from_object_store(self, compartment_id, **kwargs):
        """
        Restores a vault from an encrypted backup file stored in Oracle Cloud Infrastructure Object
        Storage. If a vault with the same OCID already exists, this operation returns
        a response with a 409 HTTP status error code.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (e.g., if a resource has been
            deleted and purged from the system, then a retry of the original
            creation request may be rejected).

        :param oci.key_management.models.RestoreVaultFromObjectStoreDetails restore_vault_from_object_store_details: (optional)
            RestoreVaultFromObjectStoreDetails

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.key_management.models.Vault`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/keymanagement/restore_vault_from_object_store.py.html>`__ to see an example of how to use restore_vault_from_object_store API.
        """
        resource_path = "/20180608/vaults/actions/restoreFromObjectStore"
        method = "POST"
        operation_name = "restore_vault_from_object_store"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token",
            "restore_vault_from_object_store_details"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "restore_vault_from_object_store got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id
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
                query_params=query_params,
                header_params=header_params,
                body=kwargs.get('restore_vault_from_object_store_details'),
                response_type="Vault",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=kwargs.get('restore_vault_from_object_store_details'),
                response_type="Vault",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def schedule_vault_deletion(self, vault_id, schedule_vault_deletion_details, **kwargs):
        """
        Schedules the deletion of the specified vault. This sets the lifecycle state of the vault and all keys in it
        that are not already scheduled for deletion to `PENDING_DELETION` and then deletes them after the
        retention period ends. The lifecycle state and time of deletion for keys already scheduled for deletion won't
        change. If any keys in the vault are scheduled to be deleted after the specified time of
        deletion for the vault, the call is rejected with the error code 409.

        As a provisioning operation, this call is subject to a Key Management limit that applies to
        the total number of requests across all provisioning write operations. Key Management might
        throttle this call to reject an otherwise valid request when the total rate of provisioning
        write operations exceeds 10 requests per second for a given tenancy.


        :param str vault_id: (required)
            The OCID of the vault.

        :param oci.key_management.models.ScheduleVaultDeletionDetails schedule_vault_deletion_details: (required)
            ScheduleVaultDeletionDetails

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case
            of a timeout or server error without risk of executing that same action
            again. Retry tokens expire after 24 hours, but can be invalidated
            before then due to conflicting operations (e.g., if a resource has been
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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.key_management.models.Vault`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/keymanagement/schedule_vault_deletion.py.html>`__ to see an example of how to use schedule_vault_deletion API.
        """
        resource_path = "/20180608/vaults/{vaultId}/actions/scheduleDeletion"
        method = "POST"
        operation_name = "schedule_vault_deletion"
        api_reference_link = ""

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
                "schedule_vault_deletion got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vaultId": vault_id
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
                body=schedule_vault_deletion_details,
                response_type="Vault",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=schedule_vault_deletion_details,
                response_type="Vault",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_vault(self, vault_id, update_vault_details, **kwargs):
        """
        Updates the properties of a vault. Specifically, you can update the
        `displayName`, `freeformTags`, and `definedTags` properties. Furthermore,
        the vault must be in an ACTIVE or CREATING state to be updated.

        As a provisioning operation, this call is subject to a Key Management limit that applies to
        the total number of requests across all provisioning write operations. Key Management might
        throttle this call to reject an otherwise valid request when the total rate of provisioning
        write operations exceeds 10 requests per second for a given tenancy.


        :param str vault_id: (required)
            The OCID of the vault.

        :param oci.key_management.models.UpdateVaultDetails update_vault_details: (required)
            UpdateVaultDetails

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a
            resource, set the `if-match` parameter to the value of the etag from a
            previous GET or POST response for that resource. The resource will be
            updated or deleted only if the etag you provide matches the resource's
            current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request. If provided, the returned request ID
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

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.key_management.models.Vault`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/keymanagement/update_vault.py.html>`__ to see an example of how to use update_vault API.
        """
        resource_path = "/20180608/vaults/{vaultId}"
        method = "PUT"
        operation_name = "update_vault"
        api_reference_link = ""

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
                "update_vault got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vaultId": vault_id
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
                body=update_vault_details,
                response_type="Vault",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_vault_details,
                response_type="Vault",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
