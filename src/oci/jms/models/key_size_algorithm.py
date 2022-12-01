# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KeySizeAlgorithm(object):
    """
    The algorithm object with name and key size properties.
    """

    #: A constant which can be used with the name property of a KeySizeAlgorithm.
    #: This constant has a value of "RSA"
    NAME_RSA = "RSA"

    #: A constant which can be used with the name property of a KeySizeAlgorithm.
    #: This constant has a value of "DSA"
    NAME_DSA = "DSA"

    #: A constant which can be used with the name property of a KeySizeAlgorithm.
    #: This constant has a value of "EC"
    NAME_EC = "EC"

    #: A constant which can be used with the name property of a KeySizeAlgorithm.
    #: This constant has a value of "DH"
    NAME_DH = "DH"

    def __init__(self, **kwargs):
        """
        Initializes a new KeySizeAlgorithm object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this KeySizeAlgorithm.
            Allowed values for this property are: "RSA", "DSA", "EC", "DH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type name: str

        :param key_size:
            The value to assign to the key_size property of this KeySizeAlgorithm.
        :type key_size: int

        """
        self.swagger_types = {
            'name': 'str',
            'key_size': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'key_size': 'keySize'
        }

        self._name = None
        self._key_size = None

    @property
    def name(self):
        """
        Gets the name of this KeySizeAlgorithm.
        The algorithm name.

        Allowed values for this property are: "RSA", "DSA", "EC", "DH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The name of this KeySizeAlgorithm.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this KeySizeAlgorithm.
        The algorithm name.


        :param name: The name of this KeySizeAlgorithm.
        :type: str
        """
        allowed_values = ["RSA", "DSA", "EC", "DH"]
        if not value_allowed_none_or_none_sentinel(name, allowed_values):
            name = 'UNKNOWN_ENUM_VALUE'
        self._name = name

    @property
    def key_size(self):
        """
        Gets the key_size of this KeySizeAlgorithm.
        Key size for the encryption algorithm.
        Allowed values: 256 for EC, 2048 for DH/DSA/RSA


        :return: The key_size of this KeySizeAlgorithm.
        :rtype: int
        """
        return self._key_size

    @key_size.setter
    def key_size(self, key_size):
        """
        Sets the key_size of this KeySizeAlgorithm.
        Key size for the encryption algorithm.
        Allowed values: 256 for EC, 2048 for DH/DSA/RSA


        :param key_size: The key_size of this KeySizeAlgorithm.
        :type: int
        """
        self._key_size = key_size

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
