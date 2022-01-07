# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


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
