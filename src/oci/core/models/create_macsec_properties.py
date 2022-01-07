# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMacsecProperties(object):
    """
    Properties used to configure MACsec (if capable).
    """

    #: A constant which can be used with the state property of a CreateMacsecProperties.
    #: This constant has a value of "ENABLED"
    STATE_ENABLED = "ENABLED"

    #: A constant which can be used with the state property of a CreateMacsecProperties.
    #: This constant has a value of "DISABLED"
    STATE_DISABLED = "DISABLED"

    #: A constant which can be used with the encryption_cipher property of a CreateMacsecProperties.
    #: This constant has a value of "AES128_GCM"
    ENCRYPTION_CIPHER_AES128_GCM = "AES128_GCM"

    #: A constant which can be used with the encryption_cipher property of a CreateMacsecProperties.
    #: This constant has a value of "AES128_GCM_XPN"
    ENCRYPTION_CIPHER_AES128_GCM_XPN = "AES128_GCM_XPN"

    #: A constant which can be used with the encryption_cipher property of a CreateMacsecProperties.
    #: This constant has a value of "AES256_GCM"
    ENCRYPTION_CIPHER_AES256_GCM = "AES256_GCM"

    #: A constant which can be used with the encryption_cipher property of a CreateMacsecProperties.
    #: This constant has a value of "AES256_GCM_XPN"
    ENCRYPTION_CIPHER_AES256_GCM_XPN = "AES256_GCM_XPN"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMacsecProperties object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param state:
            The value to assign to the state property of this CreateMacsecProperties.
            Allowed values for this property are: "ENABLED", "DISABLED"
        :type state: str

        :param primary_key:
            The value to assign to the primary_key property of this CreateMacsecProperties.
        :type primary_key: oci.core.models.CreateMacsecKey

        :param encryption_cipher:
            The value to assign to the encryption_cipher property of this CreateMacsecProperties.
            Allowed values for this property are: "AES128_GCM", "AES128_GCM_XPN", "AES256_GCM", "AES256_GCM_XPN"
        :type encryption_cipher: str

        """
        self.swagger_types = {
            'state': 'str',
            'primary_key': 'CreateMacsecKey',
            'encryption_cipher': 'str'
        }

        self.attribute_map = {
            'state': 'state',
            'primary_key': 'primaryKey',
            'encryption_cipher': 'encryptionCipher'
        }

        self._state = None
        self._primary_key = None
        self._encryption_cipher = None

    @property
    def state(self):
        """
        **[Required]** Gets the state of this CreateMacsecProperties.
        Indicates whether or not MACsec is enabled.

        Allowed values for this property are: "ENABLED", "DISABLED"


        :return: The state of this CreateMacsecProperties.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this CreateMacsecProperties.
        Indicates whether or not MACsec is enabled.


        :param state: The state of this CreateMacsecProperties.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(state, allowed_values):
            raise ValueError(
                "Invalid value for `state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._state = state

    @property
    def primary_key(self):
        """
        Gets the primary_key of this CreateMacsecProperties.

        :return: The primary_key of this CreateMacsecProperties.
        :rtype: oci.core.models.CreateMacsecKey
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        """
        Sets the primary_key of this CreateMacsecProperties.

        :param primary_key: The primary_key of this CreateMacsecProperties.
        :type: oci.core.models.CreateMacsecKey
        """
        self._primary_key = primary_key

    @property
    def encryption_cipher(self):
        """
        Gets the encryption_cipher of this CreateMacsecProperties.
        Type of encryption cipher suite to use for the MACsec connection.

        Allowed values for this property are: "AES128_GCM", "AES128_GCM_XPN", "AES256_GCM", "AES256_GCM_XPN"


        :return: The encryption_cipher of this CreateMacsecProperties.
        :rtype: str
        """
        return self._encryption_cipher

    @encryption_cipher.setter
    def encryption_cipher(self, encryption_cipher):
        """
        Sets the encryption_cipher of this CreateMacsecProperties.
        Type of encryption cipher suite to use for the MACsec connection.


        :param encryption_cipher: The encryption_cipher of this CreateMacsecProperties.
        :type: str
        """
        allowed_values = ["AES128_GCM", "AES128_GCM_XPN", "AES256_GCM", "AES256_GCM_XPN"]
        if not value_allowed_none_or_none_sentinel(encryption_cipher, allowed_values):
            raise ValueError(
                "Invalid value for `encryption_cipher`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._encryption_cipher = encryption_cipher

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
