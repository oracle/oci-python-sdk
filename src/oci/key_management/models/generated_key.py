# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GeneratedKey(object):
    """
    GeneratedKey model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GeneratedKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ciphertext:
            The value to assign to the ciphertext property of this GeneratedKey.
        :type ciphertext: str

        :param plaintext:
            The value to assign to the plaintext property of this GeneratedKey.
        :type plaintext: str

        :param plaintext_checksum:
            The value to assign to the plaintext_checksum property of this GeneratedKey.
        :type plaintext_checksum: str

        """
        self.swagger_types = {
            'ciphertext': 'str',
            'plaintext': 'str',
            'plaintext_checksum': 'str'
        }

        self.attribute_map = {
            'ciphertext': 'ciphertext',
            'plaintext': 'plaintext',
            'plaintext_checksum': 'plaintextChecksum'
        }

        self._ciphertext = None
        self._plaintext = None
        self._plaintext_checksum = None

    @property
    def ciphertext(self):
        """
        **[Required]** Gets the ciphertext of this GeneratedKey.
        The encrypted generated data encryption key.


        :return: The ciphertext of this GeneratedKey.
        :rtype: str
        """
        return self._ciphertext

    @ciphertext.setter
    def ciphertext(self, ciphertext):
        """
        Sets the ciphertext of this GeneratedKey.
        The encrypted generated data encryption key.


        :param ciphertext: The ciphertext of this GeneratedKey.
        :type: str
        """
        self._ciphertext = ciphertext

    @property
    def plaintext(self):
        """
        Gets the plaintext of this GeneratedKey.
        The plaintext generated data encryption key, a base64-encoded
        sequence of random bytes, which is included if the
        GenerateDataEncryptionKey request includes the \"includePlaintextKey\"
        parameter and sets its value to 'true'.


        :return: The plaintext of this GeneratedKey.
        :rtype: str
        """
        return self._plaintext

    @plaintext.setter
    def plaintext(self, plaintext):
        """
        Sets the plaintext of this GeneratedKey.
        The plaintext generated data encryption key, a base64-encoded
        sequence of random bytes, which is included if the
        GenerateDataEncryptionKey request includes the \"includePlaintextKey\"
        parameter and sets its value to 'true'.


        :param plaintext: The plaintext of this GeneratedKey.
        :type: str
        """
        self._plaintext = plaintext

    @property
    def plaintext_checksum(self):
        """
        Gets the plaintext_checksum of this GeneratedKey.
        The checksum of the plaintext generated data encryption key, which
        is included if the GenerateDataEncryptionKey request includes the
        \"includePlaintextKey parameter and sets its value to 'true'.


        :return: The plaintext_checksum of this GeneratedKey.
        :rtype: str
        """
        return self._plaintext_checksum

    @plaintext_checksum.setter
    def plaintext_checksum(self, plaintext_checksum):
        """
        Sets the plaintext_checksum of this GeneratedKey.
        The checksum of the plaintext generated data encryption key, which
        is included if the GenerateDataEncryptionKey request includes the
        \"includePlaintextKey parameter and sets its value to 'true'.


        :param plaintext_checksum: The plaintext_checksum of this GeneratedKey.
        :type: str
        """
        self._plaintext_checksum = plaintext_checksum

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
