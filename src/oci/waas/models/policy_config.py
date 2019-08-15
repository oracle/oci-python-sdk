# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PolicyConfig(object):
    """
    The configuration details for the WAAS policy.
    """

    #: A constant which can be used with the tls_protocols property of a PolicyConfig.
    #: This constant has a value of "TLS_V1"
    TLS_PROTOCOLS_TLS_V1 = "TLS_V1"

    #: A constant which can be used with the tls_protocols property of a PolicyConfig.
    #: This constant has a value of "TLS_V1_1"
    TLS_PROTOCOLS_TLS_V1_1 = "TLS_V1_1"

    #: A constant which can be used with the tls_protocols property of a PolicyConfig.
    #: This constant has a value of "TLS_V1_2"
    TLS_PROTOCOLS_TLS_V1_2 = "TLS_V1_2"

    #: A constant which can be used with the tls_protocols property of a PolicyConfig.
    #: This constant has a value of "TLS_V1_3"
    TLS_PROTOCOLS_TLS_V1_3 = "TLS_V1_3"

    #: A constant which can be used with the client_address_header property of a PolicyConfig.
    #: This constant has a value of "X_FORWARDED_FOR"
    CLIENT_ADDRESS_HEADER_X_FORWARDED_FOR = "X_FORWARDED_FOR"

    #: A constant which can be used with the client_address_header property of a PolicyConfig.
    #: This constant has a value of "X_CLIENT_IP"
    CLIENT_ADDRESS_HEADER_X_CLIENT_IP = "X_CLIENT_IP"

    #: A constant which can be used with the client_address_header property of a PolicyConfig.
    #: This constant has a value of "X_REAL_IP"
    CLIENT_ADDRESS_HEADER_X_REAL_IP = "X_REAL_IP"

    #: A constant which can be used with the client_address_header property of a PolicyConfig.
    #: This constant has a value of "CLIENT_IP"
    CLIENT_ADDRESS_HEADER_CLIENT_IP = "CLIENT_IP"

    #: A constant which can be used with the client_address_header property of a PolicyConfig.
    #: This constant has a value of "TRUE_CLIENT_IP"
    CLIENT_ADDRESS_HEADER_TRUE_CLIENT_IP = "TRUE_CLIENT_IP"

    #: A constant which can be used with the cipher_group property of a PolicyConfig.
    #: This constant has a value of "DEFAULT"
    CIPHER_GROUP_DEFAULT = "DEFAULT"

    def __init__(self, **kwargs):
        """
        Initializes a new PolicyConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate_id:
            The value to assign to the certificate_id property of this PolicyConfig.
        :type certificate_id: str

        :param is_https_enabled:
            The value to assign to the is_https_enabled property of this PolicyConfig.
        :type is_https_enabled: bool

        :param is_https_forced:
            The value to assign to the is_https_forced property of this PolicyConfig.
        :type is_https_forced: bool

        :param tls_protocols:
            The value to assign to the tls_protocols property of this PolicyConfig.
            Allowed values for items in this list are: "TLS_V1", "TLS_V1_1", "TLS_V1_2", "TLS_V1_3", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type tls_protocols: list[str]

        :param is_origin_compression_enabled:
            The value to assign to the is_origin_compression_enabled property of this PolicyConfig.
        :type is_origin_compression_enabled: bool

        :param is_behind_cdn:
            The value to assign to the is_behind_cdn property of this PolicyConfig.
        :type is_behind_cdn: bool

        :param client_address_header:
            The value to assign to the client_address_header property of this PolicyConfig.
            Allowed values for this property are: "X_FORWARDED_FOR", "X_CLIENT_IP", "X_REAL_IP", "CLIENT_IP", "TRUE_CLIENT_IP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type client_address_header: str

        :param is_cache_control_respected:
            The value to assign to the is_cache_control_respected property of this PolicyConfig.
        :type is_cache_control_respected: bool

        :param is_response_buffering_enabled:
            The value to assign to the is_response_buffering_enabled property of this PolicyConfig.
        :type is_response_buffering_enabled: bool

        :param cipher_group:
            The value to assign to the cipher_group property of this PolicyConfig.
            Allowed values for this property are: "DEFAULT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type cipher_group: str

        """
        self.swagger_types = {
            'certificate_id': 'str',
            'is_https_enabled': 'bool',
            'is_https_forced': 'bool',
            'tls_protocols': 'list[str]',
            'is_origin_compression_enabled': 'bool',
            'is_behind_cdn': 'bool',
            'client_address_header': 'str',
            'is_cache_control_respected': 'bool',
            'is_response_buffering_enabled': 'bool',
            'cipher_group': 'str'
        }

        self.attribute_map = {
            'certificate_id': 'certificateId',
            'is_https_enabled': 'isHttpsEnabled',
            'is_https_forced': 'isHttpsForced',
            'tls_protocols': 'tlsProtocols',
            'is_origin_compression_enabled': 'isOriginCompressionEnabled',
            'is_behind_cdn': 'isBehindCdn',
            'client_address_header': 'clientAddressHeader',
            'is_cache_control_respected': 'isCacheControlRespected',
            'is_response_buffering_enabled': 'isResponseBufferingEnabled',
            'cipher_group': 'cipherGroup'
        }

        self._certificate_id = None
        self._is_https_enabled = None
        self._is_https_forced = None
        self._tls_protocols = None
        self._is_origin_compression_enabled = None
        self._is_behind_cdn = None
        self._client_address_header = None
        self._is_cache_control_respected = None
        self._is_response_buffering_enabled = None
        self._cipher_group = None

    @property
    def certificate_id(self):
        """
        Gets the certificate_id of this PolicyConfig.
        The OCID of the SSL certificate to use if HTTPS is supported.


        :return: The certificate_id of this PolicyConfig.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """
        Sets the certificate_id of this PolicyConfig.
        The OCID of the SSL certificate to use if HTTPS is supported.


        :param certificate_id: The certificate_id of this PolicyConfig.
        :type: str
        """
        self._certificate_id = certificate_id

    @property
    def is_https_enabled(self):
        """
        Gets the is_https_enabled of this PolicyConfig.
        Enable or disable HTTPS support. If true, a `certificateId` is required. If unspecified, defaults to `false`.


        :return: The is_https_enabled of this PolicyConfig.
        :rtype: bool
        """
        return self._is_https_enabled

    @is_https_enabled.setter
    def is_https_enabled(self, is_https_enabled):
        """
        Sets the is_https_enabled of this PolicyConfig.
        Enable or disable HTTPS support. If true, a `certificateId` is required. If unspecified, defaults to `false`.


        :param is_https_enabled: The is_https_enabled of this PolicyConfig.
        :type: bool
        """
        self._is_https_enabled = is_https_enabled

    @property
    def is_https_forced(self):
        """
        Gets the is_https_forced of this PolicyConfig.
        Force HTTP to HTTPS redirection. If unspecified, defaults to `false`.


        :return: The is_https_forced of this PolicyConfig.
        :rtype: bool
        """
        return self._is_https_forced

    @is_https_forced.setter
    def is_https_forced(self, is_https_forced):
        """
        Sets the is_https_forced of this PolicyConfig.
        Force HTTP to HTTPS redirection. If unspecified, defaults to `false`.


        :param is_https_forced: The is_https_forced of this PolicyConfig.
        :type: bool
        """
        self._is_https_forced = is_https_forced

    @property
    def tls_protocols(self):
        """
        Gets the tls_protocols of this PolicyConfig.
        A list of allowed TLS protocols. Only applicable when HTTPS support is enabled. It affects client's connection to the edge nodes. The most secure TLS version will be chosen.
        - **TLS_V1:** corresponds to TLS 1.0 specification.

        - **TLS_V1_1:** corresponds to TLS 1.1 specification.

        - **TLS_V1_2:** corresponds to TLS 1.2 specification.

        - **TLS_V1_3:** corresponds to TLS 1.3 specification.

        Enabled TLS protocols must go in a row. For example if TLS_v1_1 and TLS_V1_3 are enabled, TLS_V1_2 must be enabled too.

        Allowed values for items in this list are: "TLS_V1", "TLS_V1_1", "TLS_V1_2", "TLS_V1_3", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The tls_protocols of this PolicyConfig.
        :rtype: list[str]
        """
        return self._tls_protocols

    @tls_protocols.setter
    def tls_protocols(self, tls_protocols):
        """
        Sets the tls_protocols of this PolicyConfig.
        A list of allowed TLS protocols. Only applicable when HTTPS support is enabled. It affects client's connection to the edge nodes. The most secure TLS version will be chosen.
        - **TLS_V1:** corresponds to TLS 1.0 specification.

        - **TLS_V1_1:** corresponds to TLS 1.1 specification.

        - **TLS_V1_2:** corresponds to TLS 1.2 specification.

        - **TLS_V1_3:** corresponds to TLS 1.3 specification.

        Enabled TLS protocols must go in a row. For example if TLS_v1_1 and TLS_V1_3 are enabled, TLS_V1_2 must be enabled too.


        :param tls_protocols: The tls_protocols of this PolicyConfig.
        :type: list[str]
        """
        allowed_values = ["TLS_V1", "TLS_V1_1", "TLS_V1_2", "TLS_V1_3"]
        if tls_protocols:
            tls_protocols[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in tls_protocols]
        self._tls_protocols = tls_protocols

    @property
    def is_origin_compression_enabled(self):
        """
        Gets the is_origin_compression_enabled of this PolicyConfig.
        Enable or disable GZIP compression of origin responses. If enabled, the header `Accept-Encoding: gzip` is sent to origin, otherwise - empty `Accept-Encoding:` header is used.


        :return: The is_origin_compression_enabled of this PolicyConfig.
        :rtype: bool
        """
        return self._is_origin_compression_enabled

    @is_origin_compression_enabled.setter
    def is_origin_compression_enabled(self, is_origin_compression_enabled):
        """
        Sets the is_origin_compression_enabled of this PolicyConfig.
        Enable or disable GZIP compression of origin responses. If enabled, the header `Accept-Encoding: gzip` is sent to origin, otherwise - empty `Accept-Encoding:` header is used.


        :param is_origin_compression_enabled: The is_origin_compression_enabled of this PolicyConfig.
        :type: bool
        """
        self._is_origin_compression_enabled = is_origin_compression_enabled

    @property
    def is_behind_cdn(self):
        """
        Gets the is_behind_cdn of this PolicyConfig.
        Enable or disable the use of CDN. It allows to specify true client IP address if clients do not connect directly to us.


        :return: The is_behind_cdn of this PolicyConfig.
        :rtype: bool
        """
        return self._is_behind_cdn

    @is_behind_cdn.setter
    def is_behind_cdn(self, is_behind_cdn):
        """
        Sets the is_behind_cdn of this PolicyConfig.
        Enable or disable the use of CDN. It allows to specify true client IP address if clients do not connect directly to us.


        :param is_behind_cdn: The is_behind_cdn of this PolicyConfig.
        :type: bool
        """
        self._is_behind_cdn = is_behind_cdn

    @property
    def client_address_header(self):
        """
        Gets the client_address_header of this PolicyConfig.
        The HTTP header used to pass the client IP address from the CDN if `isBehindCdn` is enabled. This feature consumes the header and its value as the true client IP address. It does not create the header. Using trusted chains (for example `X-Client-Ip: 11.1.1.1, 13.3.3.3`), the last IP address in the list will be used as true client IP address. In case of multiple headers with the same name, the first one will be used. If the header is not present it will use the connecting IP address as the true client IP address. It's assumed that CDN sets the correct client IP address and prevents spoofing.

        - **X_FORWARDED_FOR:** Corresponds to `X-Forwarded-For` header name.

        - **X_CLIENT_IP:** Corresponds to `X-Client-Ip` header name.

        - **X_REAL_IP:** Corresponds to `X-Real-Ip` header name.

        - **CLIENT_IP:** Corresponds to `Client-Ip` header name.

        - **TRUE_CLIENT_IP:** Corresponds to `True-Client-Ip` header name.

        Allowed values for this property are: "X_FORWARDED_FOR", "X_CLIENT_IP", "X_REAL_IP", "CLIENT_IP", "TRUE_CLIENT_IP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The client_address_header of this PolicyConfig.
        :rtype: str
        """
        return self._client_address_header

    @client_address_header.setter
    def client_address_header(self, client_address_header):
        """
        Sets the client_address_header of this PolicyConfig.
        The HTTP header used to pass the client IP address from the CDN if `isBehindCdn` is enabled. This feature consumes the header and its value as the true client IP address. It does not create the header. Using trusted chains (for example `X-Client-Ip: 11.1.1.1, 13.3.3.3`), the last IP address in the list will be used as true client IP address. In case of multiple headers with the same name, the first one will be used. If the header is not present it will use the connecting IP address as the true client IP address. It's assumed that CDN sets the correct client IP address and prevents spoofing.

        - **X_FORWARDED_FOR:** Corresponds to `X-Forwarded-For` header name.

        - **X_CLIENT_IP:** Corresponds to `X-Client-Ip` header name.

        - **X_REAL_IP:** Corresponds to `X-Real-Ip` header name.

        - **CLIENT_IP:** Corresponds to `Client-Ip` header name.

        - **TRUE_CLIENT_IP:** Corresponds to `True-Client-Ip` header name.


        :param client_address_header: The client_address_header of this PolicyConfig.
        :type: str
        """
        allowed_values = ["X_FORWARDED_FOR", "X_CLIENT_IP", "X_REAL_IP", "CLIENT_IP", "TRUE_CLIENT_IP"]
        if not value_allowed_none_or_none_sentinel(client_address_header, allowed_values):
            client_address_header = 'UNKNOWN_ENUM_VALUE'
        self._client_address_header = client_address_header

    @property
    def is_cache_control_respected(self):
        """
        Gets the is_cache_control_respected of this PolicyConfig.
        Enable or disable automatic content caching based on the response `cache-control` header. This feature enables the origin to act as a proxy cache. Caching policies are usually defined using `cache-control` header. For example `cache-control: max-age=120` means that the returned resource is valid for 120 seconds. Caching rules will overwrite this setting.


        :return: The is_cache_control_respected of this PolicyConfig.
        :rtype: bool
        """
        return self._is_cache_control_respected

    @is_cache_control_respected.setter
    def is_cache_control_respected(self, is_cache_control_respected):
        """
        Sets the is_cache_control_respected of this PolicyConfig.
        Enable or disable automatic content caching based on the response `cache-control` header. This feature enables the origin to act as a proxy cache. Caching policies are usually defined using `cache-control` header. For example `cache-control: max-age=120` means that the returned resource is valid for 120 seconds. Caching rules will overwrite this setting.


        :param is_cache_control_respected: The is_cache_control_respected of this PolicyConfig.
        :type: bool
        """
        self._is_cache_control_respected = is_cache_control_respected

    @property
    def is_response_buffering_enabled(self):
        """
        Gets the is_response_buffering_enabled of this PolicyConfig.
        Enable or disable buffering of responses from the origin. Buffering improves overall stability in case of network issues, but slightly increases Time To First Byte.


        :return: The is_response_buffering_enabled of this PolicyConfig.
        :rtype: bool
        """
        return self._is_response_buffering_enabled

    @is_response_buffering_enabled.setter
    def is_response_buffering_enabled(self, is_response_buffering_enabled):
        """
        Sets the is_response_buffering_enabled of this PolicyConfig.
        Enable or disable buffering of responses from the origin. Buffering improves overall stability in case of network issues, but slightly increases Time To First Byte.


        :param is_response_buffering_enabled: The is_response_buffering_enabled of this PolicyConfig.
        :type: bool
        """
        self._is_response_buffering_enabled = is_response_buffering_enabled

    @property
    def cipher_group(self):
        """
        Gets the cipher_group of this PolicyConfig.
        The cipher group
        - **DEFAULT:** Cipher group supports TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 protocols. It has the following ciphers enabled: `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:!DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA`

        Allowed values for this property are: "DEFAULT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The cipher_group of this PolicyConfig.
        :rtype: str
        """
        return self._cipher_group

    @cipher_group.setter
    def cipher_group(self, cipher_group):
        """
        Sets the cipher_group of this PolicyConfig.
        The cipher group
        - **DEFAULT:** Cipher group supports TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 protocols. It has the following ciphers enabled: `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:!DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA`


        :param cipher_group: The cipher_group of this PolicyConfig.
        :type: str
        """
        allowed_values = ["DEFAULT"]
        if not value_allowed_none_or_none_sentinel(cipher_group, allowed_values):
            cipher_group = 'UNKNOWN_ENUM_VALUE'
        self._cipher_group = cipher_group

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
