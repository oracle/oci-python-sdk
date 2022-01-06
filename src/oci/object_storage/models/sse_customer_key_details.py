# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SSECustomerKeyDetails(object):
    """
    Specifies the details of the customer-provided encryption key (SSE-C) associated with an object.
    """

    #: A constant which can be used with the algorithm property of a SSECustomerKeyDetails.
    #: This constant has a value of "AES256"
    ALGORITHM_AES256 = "AES256"

    def __init__(self, **kwargs):
        """
        Initializes a new SSECustomerKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param algorithm:
            The value to assign to the algorithm property of this SSECustomerKeyDetails.
            Allowed values for this property are: "AES256"
        :type algorithm: str

        :param key:
            The value to assign to the key property of this SSECustomerKeyDetails.
        :type key: str

        :param key_sha256:
            The value to assign to the key_sha256 property of this SSECustomerKeyDetails.
        :type key_sha256: str

        """
        self.swagger_types = {
            'algorithm': 'str',
            'key': 'str',
            'key_sha256': 'str'
        }

        self.attribute_map = {
            'algorithm': 'algorithm',
            'key': 'key',
            'key_sha256': 'keySha256'
        }

        self._algorithm = None
        self._key = None
        self._key_sha256 = None

    @property
    def algorithm(self):
        """
        **[Required]** Gets the algorithm of this SSECustomerKeyDetails.
        Specifies the encryption algorithm. The only supported value is \"AES256\".

        Allowed values for this property are: "AES256"


        :return: The algorithm of this SSECustomerKeyDetails.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """
        Sets the algorithm of this SSECustomerKeyDetails.
        Specifies the encryption algorithm. The only supported value is \"AES256\".


        :param algorithm: The algorithm of this SSECustomerKeyDetails.
        :type: str
        """
        allowed_values = ["AES256"]
        if not value_allowed_none_or_none_sentinel(algorithm, allowed_values):
            raise ValueError(
                "Invalid value for `algorithm`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._algorithm = algorithm

    @property
    def key(self):
        """
        **[Required]** Gets the key of this SSECustomerKeyDetails.
        Specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the object data.


        :return: The key of this SSECustomerKeyDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this SSECustomerKeyDetails.
        Specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the object data.


        :param key: The key of this SSECustomerKeyDetails.
        :type: str
        """
        self._key = key

    @property
    def key_sha256(self):
        """
        **[Required]** Gets the key_sha256 of this SSECustomerKeyDetails.
        Specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity
        of the encryption key.


        :return: The key_sha256 of this SSECustomerKeyDetails.
        :rtype: str
        """
        return self._key_sha256

    @key_sha256.setter
    def key_sha256(self, key_sha256):
        """
        Sets the key_sha256 of this SSECustomerKeyDetails.
        Specifies the base64-encoded SHA256 hash of the encryption key. This value is used to check the integrity
        of the encryption key.


        :param key_sha256: The key_sha256 of this SSECustomerKeyDetails.
        :type: str
        """
        self._key_sha256 = key_sha256

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
