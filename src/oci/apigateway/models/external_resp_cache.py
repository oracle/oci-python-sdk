# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .response_cache_details import ResponseCacheDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalRespCache(ResponseCacheDetails):
    """
    Connection details for an external RESP based cache store for Response Caching.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalRespCache object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.ExternalRespCache.type` attribute
        of this class is ``EXTERNAL_RESP_CACHE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ExternalRespCache.
            Allowed values for this property are: "EXTERNAL_RESP_CACHE", "NONE"
        :type type: str

        :param servers:
            The value to assign to the servers property of this ExternalRespCache.
        :type servers: list[oci.apigateway.models.ResponseCacheRespServer]

        :param authentication_secret_id:
            The value to assign to the authentication_secret_id property of this ExternalRespCache.
        :type authentication_secret_id: str

        :param authentication_secret_version_number:
            The value to assign to the authentication_secret_version_number property of this ExternalRespCache.
        :type authentication_secret_version_number: int

        :param is_ssl_enabled:
            The value to assign to the is_ssl_enabled property of this ExternalRespCache.
        :type is_ssl_enabled: bool

        :param is_ssl_verify_disabled:
            The value to assign to the is_ssl_verify_disabled property of this ExternalRespCache.
        :type is_ssl_verify_disabled: bool

        :param connect_timeout_in_ms:
            The value to assign to the connect_timeout_in_ms property of this ExternalRespCache.
        :type connect_timeout_in_ms: int

        :param read_timeout_in_ms:
            The value to assign to the read_timeout_in_ms property of this ExternalRespCache.
        :type read_timeout_in_ms: int

        :param send_timeout_in_ms:
            The value to assign to the send_timeout_in_ms property of this ExternalRespCache.
        :type send_timeout_in_ms: int

        """
        self.swagger_types = {
            'type': 'str',
            'servers': 'list[ResponseCacheRespServer]',
            'authentication_secret_id': 'str',
            'authentication_secret_version_number': 'int',
            'is_ssl_enabled': 'bool',
            'is_ssl_verify_disabled': 'bool',
            'connect_timeout_in_ms': 'int',
            'read_timeout_in_ms': 'int',
            'send_timeout_in_ms': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'servers': 'servers',
            'authentication_secret_id': 'authenticationSecretId',
            'authentication_secret_version_number': 'authenticationSecretVersionNumber',
            'is_ssl_enabled': 'isSslEnabled',
            'is_ssl_verify_disabled': 'isSslVerifyDisabled',
            'connect_timeout_in_ms': 'connectTimeoutInMs',
            'read_timeout_in_ms': 'readTimeoutInMs',
            'send_timeout_in_ms': 'sendTimeoutInMs'
        }

        self._type = None
        self._servers = None
        self._authentication_secret_id = None
        self._authentication_secret_version_number = None
        self._is_ssl_enabled = None
        self._is_ssl_verify_disabled = None
        self._connect_timeout_in_ms = None
        self._read_timeout_in_ms = None
        self._send_timeout_in_ms = None
        self._type = 'EXTERNAL_RESP_CACHE'

    @property
    def servers(self):
        """
        **[Required]** Gets the servers of this ExternalRespCache.
        The set of cache store members to connect to. At present only a single server is supported.


        :return: The servers of this ExternalRespCache.
        :rtype: list[oci.apigateway.models.ResponseCacheRespServer]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """
        Sets the servers of this ExternalRespCache.
        The set of cache store members to connect to. At present only a single server is supported.


        :param servers: The servers of this ExternalRespCache.
        :type: list[oci.apigateway.models.ResponseCacheRespServer]
        """
        self._servers = servers

    @property
    def authentication_secret_id(self):
        """
        **[Required]** Gets the authentication_secret_id of this ExternalRespCache.
        The `OCID`__ of the Oracle Vault Service secret resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The authentication_secret_id of this ExternalRespCache.
        :rtype: str
        """
        return self._authentication_secret_id

    @authentication_secret_id.setter
    def authentication_secret_id(self, authentication_secret_id):
        """
        Sets the authentication_secret_id of this ExternalRespCache.
        The `OCID`__ of the Oracle Vault Service secret resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param authentication_secret_id: The authentication_secret_id of this ExternalRespCache.
        :type: str
        """
        self._authentication_secret_id = authentication_secret_id

    @property
    def authentication_secret_version_number(self):
        """
        **[Required]** Gets the authentication_secret_version_number of this ExternalRespCache.
        The version number of the authentication secret to use.


        :return: The authentication_secret_version_number of this ExternalRespCache.
        :rtype: int
        """
        return self._authentication_secret_version_number

    @authentication_secret_version_number.setter
    def authentication_secret_version_number(self, authentication_secret_version_number):
        """
        Sets the authentication_secret_version_number of this ExternalRespCache.
        The version number of the authentication secret to use.


        :param authentication_secret_version_number: The authentication_secret_version_number of this ExternalRespCache.
        :type: int
        """
        self._authentication_secret_version_number = authentication_secret_version_number

    @property
    def is_ssl_enabled(self):
        """
        Gets the is_ssl_enabled of this ExternalRespCache.
        Defines if the connection should be over SSL.


        :return: The is_ssl_enabled of this ExternalRespCache.
        :rtype: bool
        """
        return self._is_ssl_enabled

    @is_ssl_enabled.setter
    def is_ssl_enabled(self, is_ssl_enabled):
        """
        Sets the is_ssl_enabled of this ExternalRespCache.
        Defines if the connection should be over SSL.


        :param is_ssl_enabled: The is_ssl_enabled of this ExternalRespCache.
        :type: bool
        """
        self._is_ssl_enabled = is_ssl_enabled

    @property
    def is_ssl_verify_disabled(self):
        """
        Gets the is_ssl_verify_disabled of this ExternalRespCache.
        Defines whether or not to uphold SSL verification.


        :return: The is_ssl_verify_disabled of this ExternalRespCache.
        :rtype: bool
        """
        return self._is_ssl_verify_disabled

    @is_ssl_verify_disabled.setter
    def is_ssl_verify_disabled(self, is_ssl_verify_disabled):
        """
        Sets the is_ssl_verify_disabled of this ExternalRespCache.
        Defines whether or not to uphold SSL verification.


        :param is_ssl_verify_disabled: The is_ssl_verify_disabled of this ExternalRespCache.
        :type: bool
        """
        self._is_ssl_verify_disabled = is_ssl_verify_disabled

    @property
    def connect_timeout_in_ms(self):
        """
        Gets the connect_timeout_in_ms of this ExternalRespCache.
        Defines the timeout for establishing a connection with the Response Cache.


        :return: The connect_timeout_in_ms of this ExternalRespCache.
        :rtype: int
        """
        return self._connect_timeout_in_ms

    @connect_timeout_in_ms.setter
    def connect_timeout_in_ms(self, connect_timeout_in_ms):
        """
        Sets the connect_timeout_in_ms of this ExternalRespCache.
        Defines the timeout for establishing a connection with the Response Cache.


        :param connect_timeout_in_ms: The connect_timeout_in_ms of this ExternalRespCache.
        :type: int
        """
        self._connect_timeout_in_ms = connect_timeout_in_ms

    @property
    def read_timeout_in_ms(self):
        """
        Gets the read_timeout_in_ms of this ExternalRespCache.
        Defines the timeout for reading data from the Response Cache.


        :return: The read_timeout_in_ms of this ExternalRespCache.
        :rtype: int
        """
        return self._read_timeout_in_ms

    @read_timeout_in_ms.setter
    def read_timeout_in_ms(self, read_timeout_in_ms):
        """
        Sets the read_timeout_in_ms of this ExternalRespCache.
        Defines the timeout for reading data from the Response Cache.


        :param read_timeout_in_ms: The read_timeout_in_ms of this ExternalRespCache.
        :type: int
        """
        self._read_timeout_in_ms = read_timeout_in_ms

    @property
    def send_timeout_in_ms(self):
        """
        Gets the send_timeout_in_ms of this ExternalRespCache.
        Defines the timeout for transmitting data to the Response Cache.


        :return: The send_timeout_in_ms of this ExternalRespCache.
        :rtype: int
        """
        return self._send_timeout_in_ms

    @send_timeout_in_ms.setter
    def send_timeout_in_ms(self, send_timeout_in_ms):
        """
        Sets the send_timeout_in_ms of this ExternalRespCache.
        Defines the timeout for transmitting data to the Response Cache.


        :param send_timeout_in_ms: The send_timeout_in_ms of this ExternalRespCache.
        :type: int
        """
        self._send_timeout_in_ms = send_timeout_in_ms

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
