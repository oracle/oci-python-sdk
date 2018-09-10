# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DecryptedData(object):
    """
    DecryptedData model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DecryptedData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param plaintext:
            The value to assign to the plaintext property of this DecryptedData.
        :type plaintext: str

        :param plaintext_checksum:
            The value to assign to the plaintext_checksum property of this DecryptedData.
        :type plaintext_checksum: str

        """
        self.swagger_types = {
            'plaintext': 'str',
            'plaintext_checksum': 'str'
        }

        self.attribute_map = {
            'plaintext': 'plaintext',
            'plaintext_checksum': 'plaintextChecksum'
        }

        self._plaintext = None
        self._plaintext_checksum = None

    @property
    def plaintext(self):
        """
        **[Required]** Gets the plaintext of this DecryptedData.
        The decrypted data, in the form of a base64-encoded value.


        :return: The plaintext of this DecryptedData.
        :rtype: str
        """
        return self._plaintext

    @plaintext.setter
    def plaintext(self, plaintext):
        """
        Sets the plaintext of this DecryptedData.
        The decrypted data, in the form of a base64-encoded value.


        :param plaintext: The plaintext of this DecryptedData.
        :type: str
        """
        self._plaintext = plaintext

    @property
    def plaintext_checksum(self):
        """
        **[Required]** Gets the plaintext_checksum of this DecryptedData.
        Checksum of the decrypted data.


        :return: The plaintext_checksum of this DecryptedData.
        :rtype: str
        """
        return self._plaintext_checksum

    @plaintext_checksum.setter
    def plaintext_checksum(self, plaintext_checksum):
        """
        Sets the plaintext_checksum of this DecryptedData.
        Checksum of the decrypted data.


        :param plaintext_checksum: The plaintext_checksum of this DecryptedData.
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
