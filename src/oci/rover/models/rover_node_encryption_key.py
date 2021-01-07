# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RoverNodeEncryptionKey(object):
    """
    The response containing encryption key for a rover node.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RoverNodeEncryptionKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param encryption_key:
            The value to assign to the encryption_key property of this RoverNodeEncryptionKey.
        :type encryption_key: str

        """
        self.swagger_types = {
            'encryption_key': 'str'
        }

        self.attribute_map = {
            'encryption_key': 'encryptionKey'
        }

        self._encryption_key = None

    @property
    def encryption_key(self):
        """
        **[Required]** Gets the encryption_key of this RoverNodeEncryptionKey.
        The encryption key key for a rover node.


        :return: The encryption_key of this RoverNodeEncryptionKey.
        :rtype: str
        """
        return self._encryption_key

    @encryption_key.setter
    def encryption_key(self, encryption_key):
        """
        Sets the encryption_key of this RoverNodeEncryptionKey.
        The encryption key key for a rover node.


        :param encryption_key: The encryption_key of this RoverNodeEncryptionKey.
        :type: str
        """
        self._encryption_key = encryption_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
