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
from .models import core_type_mapping
missing = Sentinel("Missing")


class BlockstorageClient(object):
    """
    Use the Core Services API to manage resources such as virtual cloud networks (VCNs),
    compute instances, and block storage volumes. For more information, see the console
    documentation for the [Networking](/iaas/Content/Network/Concepts/overview.htm),
    [Compute](/iaas/Content/Compute/Concepts/computeoverview.htm), and
    [Block Volume](/iaas/Content/Block/Concepts/overview.htm) services.
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
            'base_path': '/20160918',
            'service_endpoint_template': 'https://iaas.{region}.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'circuit_breaker_strategy': kwargs.get('circuit_breaker_strategy', circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY)
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        if base_client_init_kwargs.get('circuit_breaker_strategy') is None:
            base_client_init_kwargs['circuit_breaker_strategy'] = circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY
        if 'allow_control_chars' in kwargs:
            base_client_init_kwargs['allow_control_chars'] = kwargs.get('allow_control_chars')
        self.base_client = BaseClient("blockstorage", config, signer, core_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')
        self._config = config
        self._kwargs = kwargs

    def change_boot_volume_backup_compartment(self, boot_volume_backup_id, change_boot_volume_backup_compartment_details, **kwargs):
        """
        Moves a boot volume backup into a different compartment within the same tenancy.
        For information about moving resources between compartments,
        see `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str boot_volume_backup_id: (required)
            The OCID of the boot volume backup.

        :param oci.core.models.ChangeBootVolumeBackupCompartmentDetails change_boot_volume_backup_compartment_details: (required)
            Request to change the compartment of given boot volume backup.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/change_boot_volume_backup_compartment.py.html>`__ to see an example of how to use change_boot_volume_backup_compartment API.
        """
        resource_path = "/bootVolumeBackups/{bootVolumeBackupId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_boot_volume_backup_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/BootVolumeBackup/ChangeBootVolumeBackupCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_boot_volume_backup_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "bootVolumeBackupId": boot_volume_backup_id
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
                body=change_boot_volume_backup_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_boot_volume_backup_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def change_boot_volume_compartment(self, boot_volume_id, change_boot_volume_compartment_details, **kwargs):
        """
        Moves a boot volume into a different compartment within the same tenancy.
        For information about moving resources between compartments,
        see `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str boot_volume_id: (required)
            The OCID of the boot volume.

        :param oci.core.models.ChangeBootVolumeCompartmentDetails change_boot_volume_compartment_details: (required)
            Request to change the compartment of given boot volume.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/change_boot_volume_compartment.py.html>`__ to see an example of how to use change_boot_volume_compartment API.
        """
        resource_path = "/bootVolumes/{bootVolumeId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_boot_volume_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/BootVolume/ChangeBootVolumeCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_boot_volume_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "bootVolumeId": boot_volume_id
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
                body=change_boot_volume_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_boot_volume_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def change_volume_backup_compartment(self, volume_backup_id, change_volume_backup_compartment_details, **kwargs):
        """
        Moves a volume backup into a different compartment within the same tenancy.
        For information about moving resources between compartments,
        see `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str volume_backup_id: (required)
            The OCID of the volume backup.

        :param oci.core.models.ChangeVolumeBackupCompartmentDetails change_volume_backup_compartment_details: (required)
            Request to change the compartment of given volume backup.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/change_volume_backup_compartment.py.html>`__ to see an example of how to use change_volume_backup_compartment API.
        """
        resource_path = "/volumeBackups/{volumeBackupId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_volume_backup_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeBackup/ChangeVolumeBackupCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_volume_backup_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeBackupId": volume_backup_id
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
                body=change_volume_backup_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_volume_backup_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def change_volume_compartment(self, volume_id, change_volume_compartment_details, **kwargs):
        """
        Moves a volume into a different compartment within the same tenancy.
        For information about moving resources between compartments,
        see `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str volume_id: (required)
            The OCID of the volume.

        :param oci.core.models.ChangeVolumeCompartmentDetails change_volume_compartment_details: (required)
            Request to change the compartment of given volume.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/change_volume_compartment.py.html>`__ to see an example of how to use change_volume_compartment API.
        """
        resource_path = "/volumes/{volumeId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_volume_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/Volume/ChangeVolumeCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_volume_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeId": volume_id
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
                body=change_volume_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_volume_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def change_volume_group_backup_compartment(self, volume_group_backup_id, change_volume_group_backup_compartment_details, **kwargs):
        """
        Moves a volume group backup into a different compartment within the same tenancy.
        For information about moving resources between compartments,
        see `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str volume_group_backup_id: (required)
            The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.

        :param oci.core.models.ChangeVolumeGroupBackupCompartmentDetails change_volume_group_backup_compartment_details: (required)
            Request to change the compartment of given volume group backup.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/change_volume_group_backup_compartment.py.html>`__ to see an example of how to use change_volume_group_backup_compartment API.
        """
        resource_path = "/volumeGroupBackups/{volumeGroupBackupId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_volume_group_backup_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeGroupBackup/ChangeVolumeGroupBackupCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_volume_group_backup_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeGroupBackupId": volume_group_backup_id
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
                body=change_volume_group_backup_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_volume_group_backup_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def change_volume_group_compartment(self, volume_group_id, change_volume_group_compartment_details, **kwargs):
        """
        Moves a volume group into a different compartment within the same tenancy.
        For information about moving resources between compartments,
        see `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str volume_group_id: (required)
            The Oracle Cloud ID (OCID) that uniquely identifies the volume group.

        :param oci.core.models.ChangeVolumeGroupCompartmentDetails change_volume_group_compartment_details: (required)
            Request to change the compartment of given volume group.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/change_volume_group_compartment.py.html>`__ to see an example of how to use change_volume_group_compartment API.
        """
        resource_path = "/volumeGroups/{volumeGroupId}/actions/changeCompartment"
        method = "POST"
        operation_name = "change_volume_group_compartment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeGroup/ChangeVolumeGroupCompartment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_volume_group_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeGroupId": volume_group_id
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
                body=change_volume_group_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_volume_group_compartment_details,
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def copy_boot_volume_backup(self, boot_volume_backup_id, copy_boot_volume_backup_details, **kwargs):
        """
        Creates a boot volume backup copy in specified region. For general information about volume backups,
        see `Overview of Boot Volume Backups`__

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/bootvolumebackups.htm


        :param str boot_volume_backup_id: (required)
            The OCID of the boot volume backup.

        :param oci.core.models.CopyBootVolumeBackupDetails copy_boot_volume_backup_details: (required)
            Request to create a cross-region copy of given boot volume backup.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.BootVolumeBackup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/copy_boot_volume_backup.py.html>`__ to see an example of how to use copy_boot_volume_backup API.
        """
        resource_path = "/bootVolumeBackups/{bootVolumeBackupId}/actions/copy"
        method = "POST"
        operation_name = "copy_boot_volume_backup"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/BootVolumeBackup/CopyBootVolumeBackup"

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
                "copy_boot_volume_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "bootVolumeBackupId": boot_volume_backup_id
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
                body=copy_boot_volume_backup_details,
                response_type="BootVolumeBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=copy_boot_volume_backup_details,
                response_type="BootVolumeBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def copy_volume_backup(self, volume_backup_id, copy_volume_backup_details, **kwargs):
        """
        Creates a volume backup copy in specified region. For general information about volume backups,
        see `Overview of Block Volume Service Backups`__

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumebackups.htm


        :param str volume_backup_id: (required)
            The OCID of the volume backup.

        :param oci.core.models.CopyVolumeBackupDetails copy_volume_backup_details: (required)
            Request to create a cross-region copy of given backup.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeBackup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/copy_volume_backup.py.html>`__ to see an example of how to use copy_volume_backup API.
        """
        resource_path = "/volumeBackups/{volumeBackupId}/actions/copy"
        method = "POST"
        operation_name = "copy_volume_backup"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeBackup/CopyVolumeBackup"

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
                "copy_volume_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeBackupId": volume_backup_id
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
                body=copy_volume_backup_details,
                response_type="VolumeBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=copy_volume_backup_details,
                response_type="VolumeBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def copy_volume_group_backup(self, volume_group_backup_id, copy_volume_group_backup_details, **kwargs):
        """
        Creates a volume group backup copy in specified region. For general information about volume group backups,
        see `Overview of Block Volume Backups`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumebackups.htm


        :param str volume_group_backup_id: (required)
            The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.

        :param oci.core.models.CopyVolumeGroupBackupDetails copy_volume_group_backup_details: (required)
            Request to create a cross-region copy of given volume group backup.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeGroupBackup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/copy_volume_group_backup.py.html>`__ to see an example of how to use copy_volume_group_backup API.
        """
        resource_path = "/volumeGroupBackups/{volumeGroupBackupId}/actions/copy"
        method = "POST"
        operation_name = "copy_volume_group_backup"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeGroupBackup/CopyVolumeGroupBackup"

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
                "copy_volume_group_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeGroupBackupId": volume_group_backup_id
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
                body=copy_volume_group_backup_details,
                response_type="VolumeGroupBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=copy_volume_group_backup_details,
                response_type="VolumeGroupBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_boot_volume(self, create_boot_volume_details, **kwargs):
        """
        Creates a new boot volume in the specified compartment from an existing boot volume or a boot volume backup.
        For general information about boot volumes, see `Boot Volumes`__.
        You may optionally specify a *display name* for the volume, which is simply a friendly name or
        description. It does not have to be unique, and you can change it. Avoid entering confidential information.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/bootvolumes.htm


        :param oci.core.models.CreateBootVolumeDetails create_boot_volume_details: (required)
            Request to create a new boot volume.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.BootVolume`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/create_boot_volume.py.html>`__ to see an example of how to use create_boot_volume API.
        """
        resource_path = "/bootVolumes"
        method = "POST"
        operation_name = "create_boot_volume"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/BootVolume/CreateBootVolume"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_boot_volume got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_boot_volume_details,
                response_type="BootVolume",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_boot_volume_details,
                response_type="BootVolume",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_boot_volume_backup(self, create_boot_volume_backup_details, **kwargs):
        """
        Creates a new boot volume backup of the specified boot volume. For general information about boot volume backups,
        see `Overview of Boot Volume Backups`__

        When the request is received, the backup object is in a REQUEST_RECEIVED state.
        When the data is imaged, it goes into a CREATING state.
        After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/bootvolumebackups.htm


        :param oci.core.models.CreateBootVolumeBackupDetails create_boot_volume_backup_details: (required)
            Request to create a new backup of given boot volume.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.BootVolumeBackup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/create_boot_volume_backup.py.html>`__ to see an example of how to use create_boot_volume_backup API.
        """
        resource_path = "/bootVolumeBackups"
        method = "POST"
        operation_name = "create_boot_volume_backup"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/BootVolumeBackup/CreateBootVolumeBackup"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_boot_volume_backup got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_boot_volume_backup_details,
                response_type="BootVolumeBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_boot_volume_backup_details,
                response_type="BootVolumeBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_volume(self, create_volume_details, **kwargs):
        """
        Creates a new volume in the specified compartment. Volumes can be created in sizes ranging from
        50 GB (51200 MB) to 32 TB (33554432 MB), in 1 GB (1024 MB) increments. By default, volumes are 1 TB (1048576 MB).
        For general information about block volumes, see
        `Overview of Block Volume Service`__.

        A volume and instance can be in separate compartments but must be in the same availability domain.
        For information about access control and compartments, see
        `Overview of the IAM Service`__. For information about
        availability domains, see `Regions and Availability Domains`__.
        To get a list of availability domains, use the `ListAvailabilityDomains` operation
        in the Identity and Access Management Service API.

        You may optionally specify a *display name* for the volume, which is simply a friendly name or
        description. It does not have to be unique, and you can change it. Avoid entering confidential information.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/overview.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm
        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm


        :param oci.core.models.CreateVolumeDetails create_volume_details: (required)
            Request to create a new volume.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Volume`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/create_volume.py.html>`__ to see an example of how to use create_volume API.
        """
        resource_path = "/volumes"
        method = "POST"
        operation_name = "create_volume"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/Volume/CreateVolume"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_volume got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_volume_details,
                response_type="Volume",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_volume_details,
                response_type="Volume",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_volume_backup(self, create_volume_backup_details, **kwargs):
        """
        Creates a new backup of the specified volume. For general information about volume backups,
        see `Overview of Block Volume Service Backups`__

        When the request is received, the backup object is in a REQUEST_RECEIVED state.
        When the data is imaged, it goes into a CREATING state.
        After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumebackups.htm


        :param oci.core.models.CreateVolumeBackupDetails create_volume_backup_details: (required)
            Request to create a new backup of given volume.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeBackup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/create_volume_backup.py.html>`__ to see an example of how to use create_volume_backup API.
        """
        resource_path = "/volumeBackups"
        method = "POST"
        operation_name = "create_volume_backup"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeBackup/CreateVolumeBackup"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_volume_backup got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_volume_backup_details,
                response_type="VolumeBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_volume_backup_details,
                response_type="VolumeBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_volume_backup_policy(self, create_volume_backup_policy_details, **kwargs):
        """
        Creates a new user defined backup policy.

        For more information about Oracle defined backup policies and user defined backup policies,
        see `Policy-Based Backups`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm


        :param oci.core.models.CreateVolumeBackupPolicyDetails create_volume_backup_policy_details: (required)
            Request to create a new scheduled backup policy.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeBackupPolicy`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/create_volume_backup_policy.py.html>`__ to see an example of how to use create_volume_backup_policy API.
        """
        resource_path = "/volumeBackupPolicies"
        method = "POST"
        operation_name = "create_volume_backup_policy"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeBackupPolicy/CreateVolumeBackupPolicy"

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
                "create_volume_backup_policy got unknown kwargs: {!r}".format(extra_kwargs))

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
                body=create_volume_backup_policy_details,
                response_type="VolumeBackupPolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_volume_backup_policy_details,
                response_type="VolumeBackupPolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_volume_backup_policy_assignment(self, create_volume_backup_policy_assignment_details, **kwargs):
        """
        Assigns a volume backup policy to the specified volume. Note that a given volume can
        only have one backup policy assigned to it. If this operation is used for a volume that already
        has a different backup policy assigned, the prior backup policy will be silently unassigned.


        :param oci.core.models.CreateVolumeBackupPolicyAssignmentDetails create_volume_backup_policy_assignment_details: (required)
            Request to assign a specified policy to a particular volume.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeBackupPolicyAssignment`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/create_volume_backup_policy_assignment.py.html>`__ to see an example of how to use create_volume_backup_policy_assignment API.
        """
        resource_path = "/volumeBackupPolicyAssignments"
        method = "POST"
        operation_name = "create_volume_backup_policy_assignment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeBackupPolicyAssignment/CreateVolumeBackupPolicyAssignment"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_volume_backup_policy_assignment got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                header_params=header_params,
                body=create_volume_backup_policy_assignment_details,
                response_type="VolumeBackupPolicyAssignment",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_volume_backup_policy_assignment_details,
                response_type="VolumeBackupPolicyAssignment",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_volume_group(self, create_volume_group_details, **kwargs):
        """
        Creates a new volume group in the specified compartment.
        A volume group is a collection of volumes and may be created from a list of volumes, cloning an existing
        volume group, or by restoring a volume group backup.
        You may optionally specify a *display name* for the volume group, which is simply a friendly name or
        description. It does not have to be unique, and you can change it. Avoid entering confidential information.

        For more information, see `Volume Groups`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm


        :param oci.core.models.CreateVolumeGroupDetails create_volume_group_details: (required)
            Request to create a new volume group.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeGroup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/create_volume_group.py.html>`__ to see an example of how to use create_volume_group API.
        """
        resource_path = "/volumeGroups"
        method = "POST"
        operation_name = "create_volume_group"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeGroup/CreateVolumeGroup"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_volume_group got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_volume_group_details,
                response_type="VolumeGroup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_volume_group_details,
                response_type="VolumeGroup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def create_volume_group_backup(self, create_volume_group_backup_details, **kwargs):
        """
        Creates a new backup volume group of the specified volume group.
        For more information, see `Volume Groups`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm


        :param oci.core.models.CreateVolumeGroupBackupDetails create_volume_group_backup_details: (required)
            Request to create a new backup group of given volume group.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeGroupBackup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/create_volume_group_backup.py.html>`__ to see an example of how to use create_volume_group_backup API.
        """
        resource_path = "/volumeGroupBackups"
        method = "POST"
        operation_name = "create_volume_group_backup"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeGroupBackup/CreateVolumeGroupBackup"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_volume_group_backup got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_volume_group_backup_details,
                response_type="VolumeGroupBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_volume_group_backup_details,
                response_type="VolumeGroupBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def delete_boot_volume(self, boot_volume_id, **kwargs):
        """
        Deletes the specified boot volume. The volume cannot have an active connection to an instance.
        To disconnect the boot volume from a connected instance, see
        `Disconnecting From a Boot Volume`__.
        **Warning:** All data on the boot volume will be permanently lost when the boot volume is deleted.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/deletingbootvolume.htm


        :param str boot_volume_id: (required)
            The OCID of the boot volume.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/delete_boot_volume.py.html>`__ to see an example of how to use delete_boot_volume API.
        """
        resource_path = "/bootVolumes/{bootVolumeId}"
        method = "DELETE"
        operation_name = "delete_boot_volume"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_boot_volume got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "bootVolumeId": boot_volume_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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

    def delete_boot_volume_backup(self, boot_volume_backup_id, **kwargs):
        """
        Deletes a boot volume backup.


        :param str boot_volume_backup_id: (required)
            The OCID of the boot volume backup.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/delete_boot_volume_backup.py.html>`__ to see an example of how to use delete_boot_volume_backup API.
        """
        resource_path = "/bootVolumeBackups/{bootVolumeBackupId}"
        method = "DELETE"
        operation_name = "delete_boot_volume_backup"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_boot_volume_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "bootVolumeBackupId": boot_volume_backup_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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

    def delete_boot_volume_kms_key(self, boot_volume_id, **kwargs):
        """
        Removes the specified boot volume's assigned Key Management encryption key.


        :param str boot_volume_id: (required)
            The OCID of the boot volume.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/delete_boot_volume_kms_key.py.html>`__ to see an example of how to use delete_boot_volume_kms_key API.
        """
        resource_path = "/bootVolumes/{bootVolumeId}/kmsKey"
        method = "DELETE"
        operation_name = "delete_boot_volume_kms_key"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_boot_volume_kms_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "bootVolumeId": boot_volume_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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

    def delete_volume(self, volume_id, **kwargs):
        """
        Deletes the specified volume. The volume cannot have an active connection to an instance.
        To disconnect the volume from a connected instance, see
        `Disconnecting From a Volume`__.
        **Warning:** All data on the volume will be permanently lost when the volume is deleted.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/disconnectingfromavolume.htm


        :param str volume_id: (required)
            The OCID of the volume.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/delete_volume.py.html>`__ to see an example of how to use delete_volume API.
        """
        resource_path = "/volumes/{volumeId}"
        method = "DELETE"
        operation_name = "delete_volume"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_volume got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeId": volume_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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

    def delete_volume_backup(self, volume_backup_id, **kwargs):
        """
        Deletes a volume backup.


        :param str volume_backup_id: (required)
            The OCID of the volume backup.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/delete_volume_backup.py.html>`__ to see an example of how to use delete_volume_backup API.
        """
        resource_path = "/volumeBackups/{volumeBackupId}"
        method = "DELETE"
        operation_name = "delete_volume_backup"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_volume_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeBackupId": volume_backup_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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

    def delete_volume_backup_policy(self, policy_id, **kwargs):
        """
        Deletes a user defined backup policy.
         For more information about user defined backup policies,
         see `Policy-Based Backups`__.

         Avoid entering confidential information.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#UserDefinedBackupPolicies


        :param str policy_id: (required)
            The OCID of the volume backup policy.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/delete_volume_backup_policy.py.html>`__ to see an example of how to use delete_volume_backup_policy API.
        """
        resource_path = "/volumeBackupPolicies/{policyId}"
        method = "DELETE"
        operation_name = "delete_volume_backup_policy"
        api_reference_link = ""

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
                "delete_volume_backup_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "policyId": policy_id
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

    def delete_volume_backup_policy_assignment(self, policy_assignment_id, **kwargs):
        """
        Deletes a volume backup policy assignment.


        :param str policy_assignment_id: (required)
            The OCID of the volume backup policy assignment.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/delete_volume_backup_policy_assignment.py.html>`__ to see an example of how to use delete_volume_backup_policy_assignment API.
        """
        resource_path = "/volumeBackupPolicyAssignments/{policyAssignmentId}"
        method = "DELETE"
        operation_name = "delete_volume_backup_policy_assignment"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_volume_backup_policy_assignment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "policyAssignmentId": policy_assignment_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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

    def delete_volume_group(self, volume_group_id, **kwargs):
        """
        Deletes the specified volume group. Individual volumes are not deleted, only the volume group is deleted.
        For more information, see `Volume Groups`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm


        :param str volume_group_id: (required)
            The Oracle Cloud ID (OCID) that uniquely identifies the volume group.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/delete_volume_group.py.html>`__ to see an example of how to use delete_volume_group API.
        """
        resource_path = "/volumeGroups/{volumeGroupId}"
        method = "DELETE"
        operation_name = "delete_volume_group"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_volume_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeGroupId": volume_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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

    def delete_volume_group_backup(self, volume_group_backup_id, **kwargs):
        """
        Deletes a volume group backup. This operation deletes all the backups in
        the volume group. For more information, see `Volume Groups`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm


        :param str volume_group_backup_id: (required)
            The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/delete_volume_group_backup.py.html>`__ to see an example of how to use delete_volume_group_backup API.
        """
        resource_path = "/volumeGroupBackups/{volumeGroupBackupId}"
        method = "DELETE"
        operation_name = "delete_volume_group_backup"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_volume_group_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeGroupBackupId": volume_group_backup_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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

    def delete_volume_kms_key(self, volume_id, **kwargs):
        """
        Removes the specified volume's assigned Key Management encryption key.


        :param str volume_id: (required)
            The OCID of the volume.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

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
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/delete_volume_kms_key.py.html>`__ to see an example of how to use delete_volume_kms_key API.
        """
        resource_path = "/volumes/{volumeId}/kmsKey"
        method = "DELETE"
        operation_name = "delete_volume_kms_key"
        api_reference_link = ""

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_volume_kms_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeId": volume_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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

    def get_block_volume_replica(self, block_volume_replica_id, **kwargs):
        """
        Gets information for the specified block volume replica.


        :param str block_volume_replica_id: (required)
            The OCID of the block volume replica.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.BlockVolumeReplica`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/get_block_volume_replica.py.html>`__ to see an example of how to use get_block_volume_replica API.
        """
        resource_path = "/blockVolumeReplicas/{blockVolumeReplicaId}"
        method = "GET"
        operation_name = "get_block_volume_replica"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/BlockVolumeReplica/GetBlockVolumeReplica"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_block_volume_replica got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "blockVolumeReplicaId": block_volume_replica_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="BlockVolumeReplica",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="BlockVolumeReplica",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_boot_volume(self, boot_volume_id, **kwargs):
        """
        Gets information for the specified boot volume.


        :param str boot_volume_id: (required)
            The OCID of the boot volume.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.BootVolume`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/get_boot_volume.py.html>`__ to see an example of how to use get_boot_volume API.
        """
        resource_path = "/bootVolumes/{bootVolumeId}"
        method = "GET"
        operation_name = "get_boot_volume"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/BootVolume/GetBootVolume"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_boot_volume got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "bootVolumeId": boot_volume_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="BootVolume",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="BootVolume",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_boot_volume_backup(self, boot_volume_backup_id, **kwargs):
        """
        Gets information for the specified boot volume backup.


        :param str boot_volume_backup_id: (required)
            The OCID of the boot volume backup.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.BootVolumeBackup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/get_boot_volume_backup.py.html>`__ to see an example of how to use get_boot_volume_backup API.
        """
        resource_path = "/bootVolumeBackups/{bootVolumeBackupId}"
        method = "GET"
        operation_name = "get_boot_volume_backup"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/BootVolumeBackup/GetBootVolumeBackup"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_boot_volume_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "bootVolumeBackupId": boot_volume_backup_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="BootVolumeBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="BootVolumeBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_boot_volume_kms_key(self, boot_volume_id, **kwargs):
        """
        Gets the Key Management encryption key assigned to the specified boot volume.


        :param str boot_volume_id: (required)
            The OCID of the boot volume.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.BootVolumeKmsKey`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/get_boot_volume_kms_key.py.html>`__ to see an example of how to use get_boot_volume_kms_key API.
        """
        resource_path = "/bootVolumes/{bootVolumeId}/kmsKey"
        method = "GET"
        operation_name = "get_boot_volume_kms_key"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/BootVolumeKmsKey/GetBootVolumeKmsKey"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_boot_volume_kms_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "bootVolumeId": boot_volume_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                response_type="BootVolumeKmsKey",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="BootVolumeKmsKey",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_boot_volume_replica(self, boot_volume_replica_id, **kwargs):
        """
        Gets information for the specified boot volume replica.


        :param str boot_volume_replica_id: (required)
            The OCID of the boot volume replica.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.BootVolumeReplica`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/get_boot_volume_replica.py.html>`__ to see an example of how to use get_boot_volume_replica API.
        """
        resource_path = "/bootVolumeReplicas/{bootVolumeReplicaId}"
        method = "GET"
        operation_name = "get_boot_volume_replica"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/BootVolumeReplica/GetBootVolumeReplica"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_boot_volume_replica got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "bootVolumeReplicaId": boot_volume_replica_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="BootVolumeReplica",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="BootVolumeReplica",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_volume(self, volume_id, **kwargs):
        """
        Gets information for the specified volume.


        :param str volume_id: (required)
            The OCID of the volume.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Volume`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/get_volume.py.html>`__ to see an example of how to use get_volume API.
        """
        resource_path = "/volumes/{volumeId}"
        method = "GET"
        operation_name = "get_volume"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/Volume/GetVolume"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_volume got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeId": volume_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="Volume",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Volume",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_volume_backup(self, volume_backup_id, **kwargs):
        """
        Gets information for the specified volume backup.


        :param str volume_backup_id: (required)
            The OCID of the volume backup.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeBackup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/get_volume_backup.py.html>`__ to see an example of how to use get_volume_backup API.
        """
        resource_path = "/volumeBackups/{volumeBackupId}"
        method = "GET"
        operation_name = "get_volume_backup"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeBackup/GetVolumeBackup"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_volume_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeBackupId": volume_backup_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="VolumeBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="VolumeBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_volume_backup_policy(self, policy_id, **kwargs):
        """
        Gets information for the specified volume backup policy.


        :param str policy_id: (required)
            The OCID of the volume backup policy.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeBackupPolicy`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/get_volume_backup_policy.py.html>`__ to see an example of how to use get_volume_backup_policy API.
        """
        resource_path = "/volumeBackupPolicies/{policyId}"
        method = "GET"
        operation_name = "get_volume_backup_policy"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeBackupPolicy/GetVolumeBackupPolicy"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_volume_backup_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "policyId": policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="VolumeBackupPolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="VolumeBackupPolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_volume_backup_policy_asset_assignment(self, asset_id, **kwargs):
        """
        Gets the volume backup policy assignment for the specified volume. The
        `assetId` query parameter is required, and the returned list will contain at most
        one item, since volume can only have one volume backup policy assigned at a time.


        :param str asset_id: (required)
            The OCID of an asset (e.g. a volume).

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.VolumeBackupPolicyAssignment`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/get_volume_backup_policy_asset_assignment.py.html>`__ to see an example of how to use get_volume_backup_policy_asset_assignment API.
        """
        resource_path = "/volumeBackupPolicyAssignments"
        method = "GET"
        operation_name = "get_volume_backup_policy_asset_assignment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeBackupPolicyAssignment/GetVolumeBackupPolicyAssetAssignment"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_volume_backup_policy_asset_assignment got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "assetId": asset_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="list[VolumeBackupPolicyAssignment]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VolumeBackupPolicyAssignment]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_volume_backup_policy_assignment(self, policy_assignment_id, **kwargs):
        """
        Gets information for the specified volume backup policy assignment.


        :param str policy_assignment_id: (required)
            The OCID of the volume backup policy assignment.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeBackupPolicyAssignment`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/get_volume_backup_policy_assignment.py.html>`__ to see an example of how to use get_volume_backup_policy_assignment API.
        """
        resource_path = "/volumeBackupPolicyAssignments/{policyAssignmentId}"
        method = "GET"
        operation_name = "get_volume_backup_policy_assignment"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeBackupPolicyAssignment/GetVolumeBackupPolicyAssignment"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_volume_backup_policy_assignment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "policyAssignmentId": policy_assignment_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="VolumeBackupPolicyAssignment",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="VolumeBackupPolicyAssignment",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_volume_group(self, volume_group_id, **kwargs):
        """
        Gets information for the specified volume group. For more information, see `Volume Groups`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm


        :param str volume_group_id: (required)
            The Oracle Cloud ID (OCID) that uniquely identifies the volume group.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeGroup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/get_volume_group.py.html>`__ to see an example of how to use get_volume_group API.
        """
        resource_path = "/volumeGroups/{volumeGroupId}"
        method = "GET"
        operation_name = "get_volume_group"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeGroup/GetVolumeGroup"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_volume_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeGroupId": volume_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="VolumeGroup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="VolumeGroup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_volume_group_backup(self, volume_group_backup_id, **kwargs):
        """
        Gets information for the specified volume group backup. For more information, see `Volume Groups`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm


        :param str volume_group_backup_id: (required)
            The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeGroupBackup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/get_volume_group_backup.py.html>`__ to see an example of how to use get_volume_group_backup API.
        """
        resource_path = "/volumeGroupBackups/{volumeGroupBackupId}"
        method = "GET"
        operation_name = "get_volume_group_backup"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeGroupBackup/GetVolumeGroupBackup"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_volume_group_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeGroupBackupId": volume_group_backup_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="VolumeGroupBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="VolumeGroupBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_volume_group_replica(self, volume_group_replica_id, **kwargs):
        """
        Gets information for the specified volume group replica.


        :param str volume_group_replica_id: (required)
            The OCID of the volume replica group.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeGroupReplica`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/get_volume_group_replica.py.html>`__ to see an example of how to use get_volume_group_replica API.
        """
        resource_path = "/volumeGroupReplicas/{volumeGroupReplicaId}"
        method = "GET"
        operation_name = "get_volume_group_replica"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeGroupReplica/GetVolumeGroupReplica"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_volume_group_replica got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeGroupReplicaId": volume_group_replica_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="VolumeGroupReplica",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="VolumeGroupReplica",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def get_volume_kms_key(self, volume_id, **kwargs):
        """
        Gets the Key Management encryption key assigned to the specified volume.


        :param str volume_id: (required)
            The OCID of the volume.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeKmsKey`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/get_volume_kms_key.py.html>`__ to see an example of how to use get_volume_kms_key API.
        """
        resource_path = "/volumes/{volumeId}/kmsKey"
        method = "GET"
        operation_name = "get_volume_kms_key"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeKmsKey/GetVolumeKmsKey"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_volume_kms_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeId": volume_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                response_type="VolumeKmsKey",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="VolumeKmsKey",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_block_volume_replicas(self, **kwargs):
        """
        Lists the block volume replicas in the specified compartment and availability domain.


        :param str availability_domain: (optional)
            The name of the availability domain.

            Example: `Uocm:PHX-AD-1`

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str volume_group_replica_id: (optional)
            The OCID of the volume group replica.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

            Allowed values are: "PROVISIONING", "AVAILABLE", "ACTIVATING", "TERMINATING", "TERMINATED", "FAULTY"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.BlockVolumeReplica`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/list_block_volume_replicas.py.html>`__ to see an example of how to use list_block_volume_replicas API.
        """
        resource_path = "/blockVolumeReplicas"
        method = "GET"
        operation_name = "list_block_volume_replicas"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/BlockVolumeReplica/ListBlockVolumeReplicas"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "availability_domain",
            "compartment_id",
            "volume_group_replica_id",
            "limit",
            "page",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_block_volume_replicas got unknown kwargs: {!r}".format(extra_kwargs))

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

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "ACTIVATING", "TERMINATING", "TERMINATED", "FAULTY"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "compartmentId": kwargs.get("compartment_id", missing),
            "volumeGroupReplicaId": kwargs.get("volume_group_replica_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="list[BlockVolumeReplica]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[BlockVolumeReplica]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_boot_volume_backups(self, compartment_id, **kwargs):
        """
        Lists the boot volume backups in the specified compartment. You can filter the results by boot volume.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str boot_volume_id: (optional)
            The OCID of the boot volume.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str source_boot_volume_backup_id: (optional)
            A filter to return only resources that originated from the given source boot volume backup.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle state. The state value is
            case-insensitive.

            Allowed values are: "CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.BootVolumeBackup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/list_boot_volume_backups.py.html>`__ to see an example of how to use list_boot_volume_backups API.
        """
        resource_path = "/bootVolumeBackups"
        method = "GET"
        operation_name = "list_boot_volume_backups"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/BootVolumeBackup/ListBootVolumeBackups"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "boot_volume_id",
            "limit",
            "page",
            "display_name",
            "source_boot_volume_backup_id",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_boot_volume_backups got unknown kwargs: {!r}".format(extra_kwargs))

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

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "bootVolumeId": kwargs.get("boot_volume_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
            "sourceBootVolumeBackupId": kwargs.get("source_boot_volume_backup_id", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="list[BootVolumeBackup]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[BootVolumeBackup]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_boot_volume_replicas(self, **kwargs):
        """
        Lists the boot volume replicas in the specified compartment and availability domain.


        :param str availability_domain: (optional)
            The name of the availability domain.

            Example: `Uocm:PHX-AD-1`

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str volume_group_replica_id: (optional)
            The OCID of the volume group replica.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

            Allowed values are: "PROVISIONING", "AVAILABLE", "ACTIVATING", "TERMINATING", "TERMINATED", "FAULTY"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.BootVolumeReplica`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/list_boot_volume_replicas.py.html>`__ to see an example of how to use list_boot_volume_replicas API.
        """
        resource_path = "/bootVolumeReplicas"
        method = "GET"
        operation_name = "list_boot_volume_replicas"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/BootVolumeReplica/ListBootVolumeReplicas"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "availability_domain",
            "compartment_id",
            "volume_group_replica_id",
            "limit",
            "page",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_boot_volume_replicas got unknown kwargs: {!r}".format(extra_kwargs))

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

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "ACTIVATING", "TERMINATING", "TERMINATED", "FAULTY"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "compartmentId": kwargs.get("compartment_id", missing),
            "volumeGroupReplicaId": kwargs.get("volume_group_replica_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="list[BootVolumeReplica]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[BootVolumeReplica]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_boot_volumes(self, **kwargs):
        """
        Lists the boot volumes in the specified compartment and availability domain.


        :param str availability_domain: (optional)
            The name of the availability domain.

            Example: `Uocm:PHX-AD-1`

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str volume_group_id: (optional)
            The OCID of the volume group.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.BootVolume`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/list_boot_volumes.py.html>`__ to see an example of how to use list_boot_volumes API.
        """
        resource_path = "/bootVolumes"
        method = "GET"
        operation_name = "list_boot_volumes"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/BootVolume/ListBootVolumes"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "availability_domain",
            "compartment_id",
            "limit",
            "page",
            "volume_group_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_boot_volumes got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "compartmentId": kwargs.get("compartment_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "volumeGroupId": kwargs.get("volume_group_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="list[BootVolume]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[BootVolume]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_volume_backup_policies(self, **kwargs):
        """
        Lists all the volume backup policies available in the specified compartment.

        For more information about Oracle defined backup policies and user defined backup policies,
        see `Policy-Based Backups`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm


        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str compartment_id: (optional)
            The OCID of the compartment.
            If no compartment is specified, the Oracle defined backup policies are listed.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.VolumeBackupPolicy`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/list_volume_backup_policies.py.html>`__ to see an example of how to use list_volume_backup_policies API.
        """
        resource_path = "/volumeBackupPolicies"
        method = "GET"
        operation_name = "list_volume_backup_policies"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeBackupPolicy/ListVolumeBackupPolicies"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "limit",
            "page",
            "compartment_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_volume_backup_policies got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="list[VolumeBackupPolicy]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VolumeBackupPolicy]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_volume_backups(self, compartment_id, **kwargs):
        """
        Lists the volume backups in the specified compartment. You can filter the results by volume.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str volume_id: (optional)
            The OCID of the volume.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str source_volume_backup_id: (optional)
            A filter to return only resources that originated from the given source volume backup.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle state. The state
            value is case-insensitive.

            Allowed values are: "CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.VolumeBackup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/list_volume_backups.py.html>`__ to see an example of how to use list_volume_backups API.
        """
        resource_path = "/volumeBackups"
        method = "GET"
        operation_name = "list_volume_backups"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeBackup/ListVolumeBackups"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "volume_id",
            "limit",
            "page",
            "display_name",
            "source_volume_backup_id",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_volume_backups got unknown kwargs: {!r}".format(extra_kwargs))

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

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "volumeId": kwargs.get("volume_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
            "sourceVolumeBackupId": kwargs.get("source_volume_backup_id", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="list[VolumeBackup]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VolumeBackup]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_volume_group_backups(self, compartment_id, **kwargs):
        """
        Lists the volume group backups in the specified compartment. You can filter the results by volume group.
        For more information, see `Volume Groups`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str volume_group_id: (optional)
            The OCID of the volume group.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.VolumeGroupBackup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/list_volume_group_backups.py.html>`__ to see an example of how to use list_volume_group_backups API.
        """
        resource_path = "/volumeGroupBackups"
        method = "GET"
        operation_name = "list_volume_group_backups"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeGroupBackup/ListVolumeGroupBackups"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "volume_group_id",
            "limit",
            "page",
            "display_name",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_volume_group_backups got unknown kwargs: {!r}".format(extra_kwargs))

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
            "volumeGroupId": kwargs.get("volume_group_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="list[VolumeGroupBackup]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VolumeGroupBackup]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_volume_group_replicas(self, availability_domain, compartment_id, **kwargs):
        """
        Lists the volume group replicas in the specified compartment. You can filter the results by volume group.
        For more information, see `Volume Group Replication`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroupreplication.htm


        :param str availability_domain: (required)
            The name of the availability domain.

            Example: `Uocm:PHX-AD-1`

        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.

            Allowed values are: "PROVISIONING", "AVAILABLE", "ACTIVATING", "TERMINATING", "TERMINATED", "FAULTY"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.VolumeGroupReplica`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/list_volume_group_replicas.py.html>`__ to see an example of how to use list_volume_group_replicas API.
        """
        resource_path = "/volumeGroupReplicas"
        method = "GET"
        operation_name = "list_volume_group_replicas"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeGroupReplica/ListVolumeGroupReplicas"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "limit",
            "page",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_volume_group_replicas got unknown kwargs: {!r}".format(extra_kwargs))

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

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "ACTIVATING", "TERMINATING", "TERMINATED", "FAULTY"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="list[VolumeGroupReplica]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VolumeGroupReplica]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_volume_groups(self, compartment_id, **kwargs):
        """
        Lists the volume groups in the specified compartment and availability domain.
        For more information, see `Volume Groups`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str availability_domain: (optional)
            The name of the availability domain.

            Example: `Uocm:PHX-AD-1`

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle
            state. The state value is case-insensitive.

            Allowed values are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "UPDATE_PENDING"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.VolumeGroup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/list_volume_groups.py.html>`__ to see an example of how to use list_volume_groups API.
        """
        resource_path = "/volumeGroups"
        method = "GET"
        operation_name = "list_volume_groups"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeGroup/ListVolumeGroups"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "availability_domain",
            "limit",
            "page",
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_volume_groups got unknown kwargs: {!r}".format(extra_kwargs))

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

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "UPDATE_PENDING"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="list[VolumeGroup]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VolumeGroup]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def list_volumes(self, **kwargs):
        """
        Lists the volumes in the specified compartment and availability domain.


        :param str availability_domain: (optional)
            The name of the availability domain.

            Example: `Uocm:PHX-AD-1`

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to return in a paginated
            \"List\" call. For important details about how pagination works, see
            `List Pagination`__.

            Example: `50`

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from the previous \"List\"
            call. For important details about how pagination works, see
            `List Pagination`__.

            __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine

        :param str display_name: (optional)
            A filter to return only resources that match the given display name exactly.

        :param str sort_by: (optional)
            The field to sort by. You can provide one sort order (`sortOrder`). Default order for
            TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
            sort order is case sensitive.

            **Note:** In general, some \"List\" operations (for example, `ListInstances`) let you
            optionally filter by availability domain if the scope of the resource type is within a
            single availability domain. If you call one of these \"List\" operations without specifying
            an availability domain, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
            is case sensitive.

            Allowed values are: "ASC", "DESC"

        :param str volume_group_id: (optional)
            The OCID of the volume group.

        :param str lifecycle_state: (optional)
            A filter to only return resources that match the given lifecycle state. The state
            value is case-insensitive.

            Allowed values are: "PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.core.models.Volume`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/list_volumes.py.html>`__ to see an example of how to use list_volumes API.
        """
        resource_path = "/volumes"
        method = "GET"
        operation_name = "list_volumes"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/Volume/ListVolumes"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "availability_domain",
            "compartment_id",
            "limit",
            "page",
            "display_name",
            "sort_by",
            "sort_order",
            "volume_group_id",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_volumes got unknown kwargs: {!r}".format(extra_kwargs))

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

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "compartmentId": kwargs.get("compartment_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "displayName": kwargs.get("display_name", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "volumeGroupId": kwargs.get("volume_group_id", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

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
                response_type="list[Volume]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Volume]",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_boot_volume(self, boot_volume_id, update_boot_volume_details, **kwargs):
        """
        Updates the specified boot volume's display name, defined tags, and free-form tags.


        :param str boot_volume_id: (required)
            The OCID of the boot volume.

        :param oci.core.models.UpdateBootVolumeDetails update_boot_volume_details: (required)
            Update boot volume's display name.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.BootVolume`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/update_boot_volume.py.html>`__ to see an example of how to use update_boot_volume API.
        """
        resource_path = "/bootVolumes/{bootVolumeId}"
        method = "PUT"
        operation_name = "update_boot_volume"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/BootVolume/UpdateBootVolume"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_boot_volume got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "bootVolumeId": boot_volume_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_boot_volume_details,
                response_type="BootVolume",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_boot_volume_details,
                response_type="BootVolume",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_boot_volume_backup(self, boot_volume_backup_id, update_boot_volume_backup_details, **kwargs):
        """
        Updates the display name for the specified boot volume backup.
        Avoid entering confidential information.


        :param str boot_volume_backup_id: (required)
            The OCID of the boot volume backup.

        :param oci.core.models.UpdateBootVolumeBackupDetails update_boot_volume_backup_details: (required)
            Update boot volume backup fields

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.BootVolumeBackup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/update_boot_volume_backup.py.html>`__ to see an example of how to use update_boot_volume_backup API.
        """
        resource_path = "/bootVolumeBackups/{bootVolumeBackupId}"
        method = "PUT"
        operation_name = "update_boot_volume_backup"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/BootVolumeBackup/UpdateBootVolumeBackup"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_boot_volume_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "bootVolumeBackupId": boot_volume_backup_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_boot_volume_backup_details,
                response_type="BootVolumeBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_boot_volume_backup_details,
                response_type="BootVolumeBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_boot_volume_kms_key(self, boot_volume_id, update_boot_volume_kms_key_details, **kwargs):
        """
        Updates the specified volume with a new Key Management master encryption key.


        :param str boot_volume_id: (required)
            The OCID of the boot volume.

        :param oci.core.models.UpdateBootVolumeKmsKeyDetails update_boot_volume_kms_key_details: (required)
            Updates the Key Management master encryption key assigned to the specified boot volume.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.BootVolumeKmsKey`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/update_boot_volume_kms_key.py.html>`__ to see an example of how to use update_boot_volume_kms_key API.
        """
        resource_path = "/bootVolumes/{bootVolumeId}/kmsKey"
        method = "PUT"
        operation_name = "update_boot_volume_kms_key"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/BootVolumeKmsKey/UpdateBootVolumeKmsKey"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_boot_volume_kms_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "bootVolumeId": boot_volume_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_boot_volume_kms_key_details,
                response_type="BootVolumeKmsKey",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_boot_volume_kms_key_details,
                response_type="BootVolumeKmsKey",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_volume(self, volume_id, update_volume_details, **kwargs):
        """
        Updates the specified volume's display name.
        Avoid entering confidential information.


        :param str volume_id: (required)
            The OCID of the volume.

        :param oci.core.models.UpdateVolumeDetails update_volume_details: (required)
            Update volume's display name. Avoid entering confidential information.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.Volume`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/update_volume.py.html>`__ to see an example of how to use update_volume API.
        """
        resource_path = "/volumes/{volumeId}"
        method = "PUT"
        operation_name = "update_volume"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/Volume/UpdateVolume"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_volume got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeId": volume_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_volume_details,
                response_type="Volume",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_volume_details,
                response_type="Volume",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_volume_backup(self, volume_backup_id, update_volume_backup_details, **kwargs):
        """
        Updates the display name for the specified volume backup.
        Avoid entering confidential information.


        :param str volume_backup_id: (required)
            The OCID of the volume backup.

        :param oci.core.models.UpdateVolumeBackupDetails update_volume_backup_details: (required)
            Update volume backup fields

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeBackup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/update_volume_backup.py.html>`__ to see an example of how to use update_volume_backup API.
        """
        resource_path = "/volumeBackups/{volumeBackupId}"
        method = "PUT"
        operation_name = "update_volume_backup"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeBackup/UpdateVolumeBackup"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_volume_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeBackupId": volume_backup_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_volume_backup_details,
                response_type="VolumeBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_volume_backup_details,
                response_type="VolumeBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_volume_backup_policy(self, policy_id, update_volume_backup_policy_details, **kwargs):
        """
        Updates a user defined backup policy.
         For more information about user defined backup policies,
         see `Policy-Based Backups`__.

         Avoid entering confidential information.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#UserDefinedBackupPolicies


        :param str policy_id: (required)
            The OCID of the volume backup policy.

        :param oci.core.models.UpdateVolumeBackupPolicyDetails update_volume_backup_policy_details: (required)
            Update volume backup policy fields

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeBackupPolicy`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/update_volume_backup_policy.py.html>`__ to see an example of how to use update_volume_backup_policy API.
        """
        resource_path = "/volumeBackupPolicies/{policyId}"
        method = "PUT"
        operation_name = "update_volume_backup_policy"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeBackupPolicy/UpdateVolumeBackupPolicy"

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
                "update_volume_backup_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "policyId": policy_id
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
                body=update_volume_backup_policy_details,
                response_type="VolumeBackupPolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_volume_backup_policy_details,
                response_type="VolumeBackupPolicy",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_volume_group(self, volume_group_id, update_volume_group_details, **kwargs):
        """
        Updates the set of volumes in a volume group along with the display name. Use this operation
        to add or remove volumes in a volume group. Specify the full list of volume IDs to include in the
        volume group. If the volume ID is not specified in the call, it will be removed from the volume group.
        Avoid entering confidential information.

        For more information, see `Volume Groups`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm


        :param str volume_group_id: (required)
            The Oracle Cloud ID (OCID) that uniquely identifies the volume group.

        :param oci.core.models.UpdateVolumeGroupDetails update_volume_group_details: (required)
            Update volume group's set of volumes and/or display name

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param bool preserve_volume_replica: (optional)
            Specifies whether to disable or preserve the individual volume replication when removing a volume from the
            replication enabled volume group. When set to `true`, the individual volume replica is preserved. The default
            value is `true`.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeGroup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/update_volume_group.py.html>`__ to see an example of how to use update_volume_group API.
        """
        resource_path = "/volumeGroups/{volumeGroupId}"
        method = "PUT"
        operation_name = "update_volume_group"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeGroup/UpdateVolumeGroup"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "preserve_volume_replica"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_volume_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeGroupId": volume_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "preserveVolumeReplica": kwargs.get("preserve_volume_replica", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                query_params=query_params,
                header_params=header_params,
                body=update_volume_group_details,
                response_type="VolumeGroup",
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
                body=update_volume_group_details,
                response_type="VolumeGroup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_volume_group_backup(self, volume_group_backup_id, update_volume_group_backup_details, **kwargs):
        """
        Updates the display name for the specified volume group backup. For more information, see `Volume Groups`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm


        :param str volume_group_backup_id: (required)
            The Oracle Cloud ID (OCID) that uniquely identifies the volume group backup.

        :param oci.core.models.UpdateVolumeGroupBackupDetails update_volume_group_backup_details: (required)
            Update volume group backup fields

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeGroupBackup`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/update_volume_group_backup.py.html>`__ to see an example of how to use update_volume_group_backup API.
        """
        resource_path = "/volumeGroupBackups/{volumeGroupBackupId}"
        method = "PUT"
        operation_name = "update_volume_group_backup"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeGroupBackup/UpdateVolumeGroupBackup"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_volume_group_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeGroupBackupId": volume_group_backup_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_volume_group_backup_details,
                response_type="VolumeGroupBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_volume_group_backup_details,
                response_type="VolumeGroupBackup",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)

    def update_volume_kms_key(self, volume_id, update_volume_kms_key_details, **kwargs):
        """
        Updates the specified volume with a new Key Management master encryption key.


        :param str volume_id: (required)
            The OCID of the volume.

        :param oci.core.models.UpdateVolumeKmsKeyDetails update_volume_kms_key_details: (required)
            Updates the Key Management master encryption key assigned to the specified volume.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource. The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.core.models.VolumeKmsKey`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/core/update_volume_kms_key.py.html>`__ to see an example of how to use update_volume_kms_key API.
        """
        resource_path = "/volumes/{volumeId}/kmsKey"
        method = "PUT"
        operation_name = "update_volume_kms_key"
        api_reference_link = "https://docs.oracle.com/iaas/api/#/en/iaas/20160918/VolumeKmsKey/UpdateVolumeKmsKey"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_volume_kms_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "volumeId": volume_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_volume_kms_key_details,
                response_type="VolumeKmsKey",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_volume_kms_key_details,
                response_type="VolumeKmsKey",
                allow_control_chars=kwargs.get('allow_control_chars'),
                operation_name=operation_name,
                api_reference_link=api_reference_link)
