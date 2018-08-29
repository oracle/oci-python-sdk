# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KeyShape(object):
    """
    The cryptographic properties of a key.
    """

    #: A constant which can be used with the algorithm property of a KeyShape.
    #: This constant has a value of "AES"
    ALGORITHM_AES = "AES"

    def __init__(self, **kwargs):
        """
        Initializes a new KeyShape object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param algorithm:
            The value to assign to the algorithm property of this KeyShape.
            Allowed values for this property are: "AES", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type algorithm: str

        :param length:
            The value to assign to the length property of this KeyShape.
        :type length: int

        """
        self.swagger_types = {
            'algorithm': 'str',
            'length': 'int'
        }

        self.attribute_map = {
            'algorithm': 'algorithm',
            'length': 'length'
        }

        self._algorithm = None
        self._length = None

    @property
    def algorithm(self):
        """
        **[Required]** Gets the algorithm of this KeyShape.
        The algorithm used by a key's KeyVersions to encrypt or decrypt.

        Allowed values for this property are: "AES", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The algorithm of this KeyShape.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """
        Sets the algorithm of this KeyShape.
        The algorithm used by a key's KeyVersions to encrypt or decrypt.


        :param algorithm: The algorithm of this KeyShape.
        :type: str
        """
        allowed_values = ["AES"]
        if not value_allowed_none_or_none_sentinel(algorithm, allowed_values):
            algorithm = 'UNKNOWN_ENUM_VALUE'
        self._algorithm = algorithm

    @property
    def length(self):
        """
        **[Required]** Gets the length of this KeyShape.
        The length of the key, expressed as an integer. Values of 16, 24, or 32 are supported.


        :return: The length of this KeyShape.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Sets the length of this KeyShape.
        The length of the key, expressed as an integer. Values of 16, 24, or 32 are supported.


        :param length: The length of this KeyShape.
        :type: int
        """
        self._length = length

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
