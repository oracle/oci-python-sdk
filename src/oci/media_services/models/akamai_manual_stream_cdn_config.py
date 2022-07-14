# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .stream_cdn_config_section import StreamCdnConfigSection
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AkamaiManualStreamCdnConfig(StreamCdnConfigSection):
    """
    Configuration fields for manual Akamai configuration.
    """

    #: A constant which can be used with the origin_auth_sign_type property of a AkamaiManualStreamCdnConfig.
    #: This constant has a value of "ForwardURL"
    ORIGIN_AUTH_SIGN_TYPE_FORWARD_URL = "ForwardURL"

    #: A constant which can be used with the origin_auth_sign_encryption property of a AkamaiManualStreamCdnConfig.
    #: This constant has a value of "SHA256-HMAC"
    ORIGIN_AUTH_SIGN_ENCRYPTION_SHA256_HMAC = "SHA256-HMAC"

    def __init__(self, **kwargs):
        """
        Initializes a new AkamaiManualStreamCdnConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.media_services.models.AkamaiManualStreamCdnConfig.type` attribute
        of this class is ``AKAMAI_MANUAL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AkamaiManualStreamCdnConfig.
            Allowed values for this property are: "EDGE", "AKAMAI_MANUAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param origin_auth_sign_type:
            The value to assign to the origin_auth_sign_type property of this AkamaiManualStreamCdnConfig.
            Allowed values for this property are: "ForwardURL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type origin_auth_sign_type: str

        :param origin_auth_sign_encryption:
            The value to assign to the origin_auth_sign_encryption property of this AkamaiManualStreamCdnConfig.
            Allowed values for this property are: "SHA256-HMAC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type origin_auth_sign_encryption: str

        :param origin_auth_secret_key_a:
            The value to assign to the origin_auth_secret_key_a property of this AkamaiManualStreamCdnConfig.
        :type origin_auth_secret_key_a: str

        :param origin_auth_secret_key_nonce_a:
            The value to assign to the origin_auth_secret_key_nonce_a property of this AkamaiManualStreamCdnConfig.
        :type origin_auth_secret_key_nonce_a: str

        :param origin_auth_secret_key_b:
            The value to assign to the origin_auth_secret_key_b property of this AkamaiManualStreamCdnConfig.
        :type origin_auth_secret_key_b: str

        :param origin_auth_secret_key_nonce_b:
            The value to assign to the origin_auth_secret_key_nonce_b property of this AkamaiManualStreamCdnConfig.
        :type origin_auth_secret_key_nonce_b: str

        :param edge_hostname:
            The value to assign to the edge_hostname property of this AkamaiManualStreamCdnConfig.
        :type edge_hostname: str

        :param edge_path_prefix:
            The value to assign to the edge_path_prefix property of this AkamaiManualStreamCdnConfig.
        :type edge_path_prefix: str

        :param is_edge_token_auth:
            The value to assign to the is_edge_token_auth property of this AkamaiManualStreamCdnConfig.
        :type is_edge_token_auth: bool

        :param edge_token_key:
            The value to assign to the edge_token_key property of this AkamaiManualStreamCdnConfig.
        :type edge_token_key: str

        :param edge_token_salt:
            The value to assign to the edge_token_salt property of this AkamaiManualStreamCdnConfig.
        :type edge_token_salt: str

        """
        self.swagger_types = {
            'type': 'str',
            'origin_auth_sign_type': 'str',
            'origin_auth_sign_encryption': 'str',
            'origin_auth_secret_key_a': 'str',
            'origin_auth_secret_key_nonce_a': 'str',
            'origin_auth_secret_key_b': 'str',
            'origin_auth_secret_key_nonce_b': 'str',
            'edge_hostname': 'str',
            'edge_path_prefix': 'str',
            'is_edge_token_auth': 'bool',
            'edge_token_key': 'str',
            'edge_token_salt': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'origin_auth_sign_type': 'originAuthSignType',
            'origin_auth_sign_encryption': 'originAuthSignEncryption',
            'origin_auth_secret_key_a': 'originAuthSecretKeyA',
            'origin_auth_secret_key_nonce_a': 'originAuthSecretKeyNonceA',
            'origin_auth_secret_key_b': 'originAuthSecretKeyB',
            'origin_auth_secret_key_nonce_b': 'originAuthSecretKeyNonceB',
            'edge_hostname': 'edgeHostname',
            'edge_path_prefix': 'edgePathPrefix',
            'is_edge_token_auth': 'isEdgeTokenAuth',
            'edge_token_key': 'edgeTokenKey',
            'edge_token_salt': 'edgeTokenSalt'
        }

        self._type = None
        self._origin_auth_sign_type = None
        self._origin_auth_sign_encryption = None
        self._origin_auth_secret_key_a = None
        self._origin_auth_secret_key_nonce_a = None
        self._origin_auth_secret_key_b = None
        self._origin_auth_secret_key_nonce_b = None
        self._edge_hostname = None
        self._edge_path_prefix = None
        self._is_edge_token_auth = None
        self._edge_token_key = None
        self._edge_token_salt = None
        self._type = 'AKAMAI_MANUAL'

    @property
    def origin_auth_sign_type(self):
        """
        Gets the origin_auth_sign_type of this AkamaiManualStreamCdnConfig.
        The type of data used to compute the signature.

        Allowed values for this property are: "ForwardURL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The origin_auth_sign_type of this AkamaiManualStreamCdnConfig.
        :rtype: str
        """
        return self._origin_auth_sign_type

    @origin_auth_sign_type.setter
    def origin_auth_sign_type(self, origin_auth_sign_type):
        """
        Sets the origin_auth_sign_type of this AkamaiManualStreamCdnConfig.
        The type of data used to compute the signature.


        :param origin_auth_sign_type: The origin_auth_sign_type of this AkamaiManualStreamCdnConfig.
        :type: str
        """
        allowed_values = ["ForwardURL"]
        if not value_allowed_none_or_none_sentinel(origin_auth_sign_type, allowed_values):
            origin_auth_sign_type = 'UNKNOWN_ENUM_VALUE'
        self._origin_auth_sign_type = origin_auth_sign_type

    @property
    def origin_auth_sign_encryption(self):
        """
        Gets the origin_auth_sign_encryption of this AkamaiManualStreamCdnConfig.
        The type of encryption used to compute the signature.

        Allowed values for this property are: "SHA256-HMAC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The origin_auth_sign_encryption of this AkamaiManualStreamCdnConfig.
        :rtype: str
        """
        return self._origin_auth_sign_encryption

    @origin_auth_sign_encryption.setter
    def origin_auth_sign_encryption(self, origin_auth_sign_encryption):
        """
        Sets the origin_auth_sign_encryption of this AkamaiManualStreamCdnConfig.
        The type of encryption used to compute the signature.


        :param origin_auth_sign_encryption: The origin_auth_sign_encryption of this AkamaiManualStreamCdnConfig.
        :type: str
        """
        allowed_values = ["SHA256-HMAC"]
        if not value_allowed_none_or_none_sentinel(origin_auth_sign_encryption, allowed_values):
            origin_auth_sign_encryption = 'UNKNOWN_ENUM_VALUE'
        self._origin_auth_sign_encryption = origin_auth_sign_encryption

    @property
    def origin_auth_secret_key_a(self):
        """
        Gets the origin_auth_secret_key_a of this AkamaiManualStreamCdnConfig.
        The shared secret key A, two for errorless key rotation.


        :return: The origin_auth_secret_key_a of this AkamaiManualStreamCdnConfig.
        :rtype: str
        """
        return self._origin_auth_secret_key_a

    @origin_auth_secret_key_a.setter
    def origin_auth_secret_key_a(self, origin_auth_secret_key_a):
        """
        Sets the origin_auth_secret_key_a of this AkamaiManualStreamCdnConfig.
        The shared secret key A, two for errorless key rotation.


        :param origin_auth_secret_key_a: The origin_auth_secret_key_a of this AkamaiManualStreamCdnConfig.
        :type: str
        """
        self._origin_auth_secret_key_a = origin_auth_secret_key_a

    @property
    def origin_auth_secret_key_nonce_a(self):
        """
        Gets the origin_auth_secret_key_nonce_a of this AkamaiManualStreamCdnConfig.
        Nonce identifier for originAuthSecretKeyA (used to determine key used to sign).


        :return: The origin_auth_secret_key_nonce_a of this AkamaiManualStreamCdnConfig.
        :rtype: str
        """
        return self._origin_auth_secret_key_nonce_a

    @origin_auth_secret_key_nonce_a.setter
    def origin_auth_secret_key_nonce_a(self, origin_auth_secret_key_nonce_a):
        """
        Sets the origin_auth_secret_key_nonce_a of this AkamaiManualStreamCdnConfig.
        Nonce identifier for originAuthSecretKeyA (used to determine key used to sign).


        :param origin_auth_secret_key_nonce_a: The origin_auth_secret_key_nonce_a of this AkamaiManualStreamCdnConfig.
        :type: str
        """
        self._origin_auth_secret_key_nonce_a = origin_auth_secret_key_nonce_a

    @property
    def origin_auth_secret_key_b(self):
        """
        Gets the origin_auth_secret_key_b of this AkamaiManualStreamCdnConfig.
        The shared secret key B, two for errorless key rotation.


        :return: The origin_auth_secret_key_b of this AkamaiManualStreamCdnConfig.
        :rtype: str
        """
        return self._origin_auth_secret_key_b

    @origin_auth_secret_key_b.setter
    def origin_auth_secret_key_b(self, origin_auth_secret_key_b):
        """
        Sets the origin_auth_secret_key_b of this AkamaiManualStreamCdnConfig.
        The shared secret key B, two for errorless key rotation.


        :param origin_auth_secret_key_b: The origin_auth_secret_key_b of this AkamaiManualStreamCdnConfig.
        :type: str
        """
        self._origin_auth_secret_key_b = origin_auth_secret_key_b

    @property
    def origin_auth_secret_key_nonce_b(self):
        """
        Gets the origin_auth_secret_key_nonce_b of this AkamaiManualStreamCdnConfig.
        Nonce identifier for originAuthSecretKeyB (used to determine key used to sign).


        :return: The origin_auth_secret_key_nonce_b of this AkamaiManualStreamCdnConfig.
        :rtype: str
        """
        return self._origin_auth_secret_key_nonce_b

    @origin_auth_secret_key_nonce_b.setter
    def origin_auth_secret_key_nonce_b(self, origin_auth_secret_key_nonce_b):
        """
        Sets the origin_auth_secret_key_nonce_b of this AkamaiManualStreamCdnConfig.
        Nonce identifier for originAuthSecretKeyB (used to determine key used to sign).


        :param origin_auth_secret_key_nonce_b: The origin_auth_secret_key_nonce_b of this AkamaiManualStreamCdnConfig.
        :type: str
        """
        self._origin_auth_secret_key_nonce_b = origin_auth_secret_key_nonce_b

    @property
    def edge_hostname(self):
        """
        Gets the edge_hostname of this AkamaiManualStreamCdnConfig.
        The hostname of the CDN edge server to use when building CDN URLs.


        :return: The edge_hostname of this AkamaiManualStreamCdnConfig.
        :rtype: str
        """
        return self._edge_hostname

    @edge_hostname.setter
    def edge_hostname(self, edge_hostname):
        """
        Sets the edge_hostname of this AkamaiManualStreamCdnConfig.
        The hostname of the CDN edge server to use when building CDN URLs.


        :param edge_hostname: The edge_hostname of this AkamaiManualStreamCdnConfig.
        :type: str
        """
        self._edge_hostname = edge_hostname

    @property
    def edge_path_prefix(self):
        """
        Gets the edge_path_prefix of this AkamaiManualStreamCdnConfig.
        The path to prepend when building CDN URLs.


        :return: The edge_path_prefix of this AkamaiManualStreamCdnConfig.
        :rtype: str
        """
        return self._edge_path_prefix

    @edge_path_prefix.setter
    def edge_path_prefix(self, edge_path_prefix):
        """
        Sets the edge_path_prefix of this AkamaiManualStreamCdnConfig.
        The path to prepend when building CDN URLs.


        :param edge_path_prefix: The edge_path_prefix of this AkamaiManualStreamCdnConfig.
        :type: str
        """
        self._edge_path_prefix = edge_path_prefix

    @property
    def is_edge_token_auth(self):
        """
        Gets the is_edge_token_auth of this AkamaiManualStreamCdnConfig.
        Whether token authentication should be used at the CDN edge.


        :return: The is_edge_token_auth of this AkamaiManualStreamCdnConfig.
        :rtype: bool
        """
        return self._is_edge_token_auth

    @is_edge_token_auth.setter
    def is_edge_token_auth(self, is_edge_token_auth):
        """
        Sets the is_edge_token_auth of this AkamaiManualStreamCdnConfig.
        Whether token authentication should be used at the CDN edge.


        :param is_edge_token_auth: The is_edge_token_auth of this AkamaiManualStreamCdnConfig.
        :type: bool
        """
        self._is_edge_token_auth = is_edge_token_auth

    @property
    def edge_token_key(self):
        """
        Gets the edge_token_key of this AkamaiManualStreamCdnConfig.
        The encryption key to use for edge token authentication.


        :return: The edge_token_key of this AkamaiManualStreamCdnConfig.
        :rtype: str
        """
        return self._edge_token_key

    @edge_token_key.setter
    def edge_token_key(self, edge_token_key):
        """
        Sets the edge_token_key of this AkamaiManualStreamCdnConfig.
        The encryption key to use for edge token authentication.


        :param edge_token_key: The edge_token_key of this AkamaiManualStreamCdnConfig.
        :type: str
        """
        self._edge_token_key = edge_token_key

    @property
    def edge_token_salt(self):
        """
        Gets the edge_token_salt of this AkamaiManualStreamCdnConfig.
        Salt to use when encrypting authentication token.


        :return: The edge_token_salt of this AkamaiManualStreamCdnConfig.
        :rtype: str
        """
        return self._edge_token_salt

    @edge_token_salt.setter
    def edge_token_salt(self, edge_token_salt):
        """
        Sets the edge_token_salt of this AkamaiManualStreamCdnConfig.
        Salt to use when encrypting authentication token.


        :param edge_token_salt: The edge_token_salt of this AkamaiManualStreamCdnConfig.
        :type: str
        """
        self._edge_token_salt = edge_token_salt

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
