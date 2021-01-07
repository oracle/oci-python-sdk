# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificatePublicKeyInfo(object):
    """
    Information about the public key and the algorithm used by the public key.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CertificatePublicKeyInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param algorithm:
            The value to assign to the algorithm property of this CertificatePublicKeyInfo.
        :type algorithm: str

        :param exponent:
            The value to assign to the exponent property of this CertificatePublicKeyInfo.
        :type exponent: int

        :param key_size:
            The value to assign to the key_size property of this CertificatePublicKeyInfo.
        :type key_size: int

        """
        self.swagger_types = {
            'algorithm': 'str',
            'exponent': 'int',
            'key_size': 'int'
        }

        self.attribute_map = {
            'algorithm': 'algorithm',
            'exponent': 'exponent',
            'key_size': 'keySize'
        }

        self._algorithm = None
        self._exponent = None
        self._key_size = None

    @property
    def algorithm(self):
        """
        Gets the algorithm of this CertificatePublicKeyInfo.
        The algorithm identifier and parameters for the public key.


        :return: The algorithm of this CertificatePublicKeyInfo.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """
        Sets the algorithm of this CertificatePublicKeyInfo.
        The algorithm identifier and parameters for the public key.


        :param algorithm: The algorithm of this CertificatePublicKeyInfo.
        :type: str
        """
        self._algorithm = algorithm

    @property
    def exponent(self):
        """
        Gets the exponent of this CertificatePublicKeyInfo.
        The private key exponent.


        :return: The exponent of this CertificatePublicKeyInfo.
        :rtype: int
        """
        return self._exponent

    @exponent.setter
    def exponent(self, exponent):
        """
        Sets the exponent of this CertificatePublicKeyInfo.
        The private key exponent.


        :param exponent: The exponent of this CertificatePublicKeyInfo.
        :type: int
        """
        self._exponent = exponent

    @property
    def key_size(self):
        """
        Gets the key_size of this CertificatePublicKeyInfo.
        The number of bits in a key used by a cryptographic algorithm.


        :return: The key_size of this CertificatePublicKeyInfo.
        :rtype: int
        """
        return self._key_size

    @key_size.setter
    def key_size(self, key_size):
        """
        Sets the key_size of this CertificatePublicKeyInfo.
        The number of bits in a key used by a cryptographic algorithm.


        :param key_size: The key_size of this CertificatePublicKeyInfo.
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
