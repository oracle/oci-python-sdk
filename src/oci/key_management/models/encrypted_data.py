# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EncryptedData(object):
    """
    EncryptedData model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EncryptedData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ciphertext:
            The value to assign to the ciphertext property of this EncryptedData.
        :type ciphertext: str

        """
        self.swagger_types = {
            'ciphertext': 'str'
        }

        self.attribute_map = {
            'ciphertext': 'ciphertext'
        }

        self._ciphertext = None

    @property
    def ciphertext(self):
        """
        **[Required]** Gets the ciphertext of this EncryptedData.
        The encrypted data.


        :return: The ciphertext of this EncryptedData.
        :rtype: str
        """
        return self._ciphertext

    @ciphertext.setter
    def ciphertext(self, ciphertext):
        """
        Sets the ciphertext of this EncryptedData.
        The encrypted data.


        :param ciphertext: The ciphertext of this EncryptedData.
        :type: str
        """
        self._ciphertext = ciphertext

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
