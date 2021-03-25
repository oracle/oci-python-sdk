# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EncryptedData(object):
    """
    EncryptedData model.
    """

    #: A constant which can be used with the encryption_algorithm property of a EncryptedData.
    #: This constant has a value of "AES_256_GCM"
    ENCRYPTION_ALGORITHM_AES_256_GCM = "AES_256_GCM"

    #: A constant which can be used with the encryption_algorithm property of a EncryptedData.
    #: This constant has a value of "RSA_OAEP_SHA_1"
    ENCRYPTION_ALGORITHM_RSA_OAEP_SHA_1 = "RSA_OAEP_SHA_1"

    #: A constant which can be used with the encryption_algorithm property of a EncryptedData.
    #: This constant has a value of "RSA_OAEP_SHA_256"
    ENCRYPTION_ALGORITHM_RSA_OAEP_SHA_256 = "RSA_OAEP_SHA_256"

    def __init__(self, **kwargs):
        """
        Initializes a new EncryptedData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ciphertext:
            The value to assign to the ciphertext property of this EncryptedData.
        :type ciphertext: str

        :param key_id:
            The value to assign to the key_id property of this EncryptedData.
        :type key_id: str

        :param key_version_id:
            The value to assign to the key_version_id property of this EncryptedData.
        :type key_version_id: str

        :param encryption_algorithm:
            The value to assign to the encryption_algorithm property of this EncryptedData.
            Allowed values for this property are: "AES_256_GCM", "RSA_OAEP_SHA_1", "RSA_OAEP_SHA_256", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type encryption_algorithm: str

        """
        self.swagger_types = {
            'ciphertext': 'str',
            'key_id': 'str',
            'key_version_id': 'str',
            'encryption_algorithm': 'str'
        }

        self.attribute_map = {
            'ciphertext': 'ciphertext',
            'key_id': 'keyId',
            'key_version_id': 'keyVersionId',
            'encryption_algorithm': 'encryptionAlgorithm'
        }

        self._ciphertext = None
        self._key_id = None
        self._key_version_id = None
        self._encryption_algorithm = None

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

    @property
    def key_id(self):
        """
        Gets the key_id of this EncryptedData.
        The OCID of the key used to encrypt the ciphertext.


        :return: The key_id of this EncryptedData.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this EncryptedData.
        The OCID of the key used to encrypt the ciphertext.


        :param key_id: The key_id of this EncryptedData.
        :type: str
        """
        self._key_id = key_id

    @property
    def key_version_id(self):
        """
        Gets the key_version_id of this EncryptedData.
        The OCID of the key version used to encrypt the ciphertext.


        :return: The key_version_id of this EncryptedData.
        :rtype: str
        """
        return self._key_version_id

    @key_version_id.setter
    def key_version_id(self, key_version_id):
        """
        Sets the key_version_id of this EncryptedData.
        The OCID of the key version used to encrypt the ciphertext.


        :param key_version_id: The key_version_id of this EncryptedData.
        :type: str
        """
        self._key_version_id = key_version_id

    @property
    def encryption_algorithm(self):
        """
        Gets the encryption_algorithm of this EncryptedData.
        The encryption algorithm to use to encrypt and decrypt data with a customer-managed key.
        `AES_256_GCM` indicates that the key is a symmetric key that uses the Advanced Encryption Standard (AES) algorithm and
        that the mode of encryption is the Galois/Counter Mode (GCM). `RSA_OAEP_SHA_1` indicates that the
        key is an asymmetric key that uses the RSA encryption algorithm and uses Optimal Asymmetric Encryption Padding (OAEP).
        `RSA_OAEP_SHA_256` indicates that the key is an asymmetric key that uses the RSA encryption algorithm with a SHA-256 hash
        and uses OAEP.

        Allowed values for this property are: "AES_256_GCM", "RSA_OAEP_SHA_1", "RSA_OAEP_SHA_256", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The encryption_algorithm of this EncryptedData.
        :rtype: str
        """
        return self._encryption_algorithm

    @encryption_algorithm.setter
    def encryption_algorithm(self, encryption_algorithm):
        """
        Sets the encryption_algorithm of this EncryptedData.
        The encryption algorithm to use to encrypt and decrypt data with a customer-managed key.
        `AES_256_GCM` indicates that the key is a symmetric key that uses the Advanced Encryption Standard (AES) algorithm and
        that the mode of encryption is the Galois/Counter Mode (GCM). `RSA_OAEP_SHA_1` indicates that the
        key is an asymmetric key that uses the RSA encryption algorithm and uses Optimal Asymmetric Encryption Padding (OAEP).
        `RSA_OAEP_SHA_256` indicates that the key is an asymmetric key that uses the RSA encryption algorithm with a SHA-256 hash
        and uses OAEP.


        :param encryption_algorithm: The encryption_algorithm of this EncryptedData.
        :type: str
        """
        allowed_values = ["AES_256_GCM", "RSA_OAEP_SHA_1", "RSA_OAEP_SHA_256"]
        if not value_allowed_none_or_none_sentinel(encryption_algorithm, allowed_values):
            encryption_algorithm = 'UNKNOWN_ENUM_VALUE'
        self._encryption_algorithm = encryption_algorithm

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
