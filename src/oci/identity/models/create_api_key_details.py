# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateApiKeyDetails(object):
    """
    CreateApiKeyDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateApiKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CreateApiKeyDetails.
        :type key: str

        """
        self.swagger_types = {
            'key': 'str'
        }

        self.attribute_map = {
            'key': 'key'
        }

        self._key = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this CreateApiKeyDetails.
        The public key.  Must be an RSA key in PEM format.


        :return: The key of this CreateApiKeyDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreateApiKeyDetails.
        The public key.  Must be an RSA key in PEM format.


        :param key: The key of this CreateApiKeyDetails.
        :type: str
        """
        self._key = key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
