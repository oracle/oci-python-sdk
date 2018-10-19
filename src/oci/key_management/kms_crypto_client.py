# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry  # noqa: F401
from oci.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel
from .models import key_management_type_mapping
missing = Sentinel("Missing")


class KmsCryptoClient(object):
    """
    API for managing and performing operations with keys and vaults.
    """

    def __init__(self, config, **kwargs):
        """
        Creates a new service client

        :param dict config:
            Configuration keys and values as per `SDK and Tool Configuration <https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/sdkconfig.htm>`__.
            The :py:meth:`~oci.config.from_file` method can be used to load configuration from a file. Alternatively, a ``dict`` can be passed. You can validate_config
            the dict using :py:meth:`~oci.config.validate_config`

        :param str service_endpoint: (optional)
            The endpoint of the service to call using this client. For example ``https://iaas.us-ashburn-1.oraclecloud.com``. If this keyword argument is
            not provided then it will be derived using the region in the config parameter. You should only provide this keyword argument if you have an explicit
            need to specify a service endpoint.

        :param timeout: (optional)
            The connection and read timeouts for the client. The default is that the client never times out. This keyword argument can be provided
            as a single float, in which case the value provided is used for both the read and connection timeouts, or as a tuple of two floats. If
            a tuple is provided then the first value is used as the connection timeout and the second value as the read timeout.
        :type timeout: float or tuple(float, float)

        :param signer: (optional)
            The signer to use when signing requests made by the service client. The default is to use a :py:class:`~oci.signer.Signer` based on the values
            provided in the config parameter.

            One use case for this parameter is for `Instance Principals authentication <https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Tasks/callingservicesfrominstances.htm>`__
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
            'regional_client': False,
            'service_endpoint': kwargs.get('service_endpoint'),
            'timeout': kwargs.get('timeout'),
            'base_path': '/20180608',
            'skip_deserialization': kwargs.get('skip_deserialization', False)
        }
        self.base_client = BaseClient("kms_crypto", config, signer, key_management_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')

    def decrypt(self, decrypt_data_details, **kwargs):
        """
        Decrypt
        Decrypts data using the given DecryptDataDetails resource.


        :param DecryptDataDetails decrypt_data_details: (required)
            DecryptDataDetails

        :param str opc_request_id: (optional)
            Unique identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.key_management.models.DecryptedData`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/decrypt"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "decrypt got unknown kwargs: {!r}".format(extra_kwargs))

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
                body=decrypt_data_details,
                response_type="DecryptedData")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=decrypt_data_details,
                response_type="DecryptedData")

    def encrypt(self, encrypt_data_details, **kwargs):
        """
        Encrypt
        Encrypts data using the given EncryptDataDetails resource.
        Plaintext included in the example request is a base64-encoded value
        of a UTF-8 string.


        :param EncryptDataDetails encrypt_data_details: (required)
            EncryptDataDetails

        :param str opc_request_id: (optional)
            Unique identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.key_management.models.EncryptedData`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/encrypt"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "encrypt got unknown kwargs: {!r}".format(extra_kwargs))

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
                body=encrypt_data_details,
                response_type="EncryptedData")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=encrypt_data_details,
                response_type="EncryptedData")

    def generate_data_encryption_key(self, generate_key_details, **kwargs):
        """
        GenerateDataEncryptionKey
        Generates a key that you can use to encrypt or decrypt data.


        :param GenerateKeyDetails generate_key_details: (required)
            GenerateKeyDetails

        :param str opc_request_id: (optional)
            Unique identifier for the request. If provided, the returned request ID
            will include this value. Otherwise, a random request ID will be
            generated by the service.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.key_management.models.GeneratedKey`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/generateDataEncryptionKey"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "generate_data_encryption_key got unknown kwargs: {!r}".format(extra_kwargs))

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
                body=generate_key_details,
                response_type="GeneratedKey")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=generate_key_details,
                response_type="GeneratedKey")
