# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SignedData(object):
    """
    SignedData model.
    """

    #: A constant which can be used with the signing_algorithm property of a SignedData.
    #: This constant has a value of "SHA_224_RSA_PKCS_PSS"
    SIGNING_ALGORITHM_SHA_224_RSA_PKCS_PSS = "SHA_224_RSA_PKCS_PSS"

    #: A constant which can be used with the signing_algorithm property of a SignedData.
    #: This constant has a value of "SHA_256_RSA_PKCS_PSS"
    SIGNING_ALGORITHM_SHA_256_RSA_PKCS_PSS = "SHA_256_RSA_PKCS_PSS"

    #: A constant which can be used with the signing_algorithm property of a SignedData.
    #: This constant has a value of "SHA_384_RSA_PKCS_PSS"
    SIGNING_ALGORITHM_SHA_384_RSA_PKCS_PSS = "SHA_384_RSA_PKCS_PSS"

    #: A constant which can be used with the signing_algorithm property of a SignedData.
    #: This constant has a value of "SHA_512_RSA_PKCS_PSS"
    SIGNING_ALGORITHM_SHA_512_RSA_PKCS_PSS = "SHA_512_RSA_PKCS_PSS"

    #: A constant which can be used with the signing_algorithm property of a SignedData.
    #: This constant has a value of "SHA_224_RSA_PKCS1_V1_5"
    SIGNING_ALGORITHM_SHA_224_RSA_PKCS1_V1_5 = "SHA_224_RSA_PKCS1_V1_5"

    #: A constant which can be used with the signing_algorithm property of a SignedData.
    #: This constant has a value of "SHA_256_RSA_PKCS1_V1_5"
    SIGNING_ALGORITHM_SHA_256_RSA_PKCS1_V1_5 = "SHA_256_RSA_PKCS1_V1_5"

    #: A constant which can be used with the signing_algorithm property of a SignedData.
    #: This constant has a value of "SHA_384_RSA_PKCS1_V1_5"
    SIGNING_ALGORITHM_SHA_384_RSA_PKCS1_V1_5 = "SHA_384_RSA_PKCS1_V1_5"

    #: A constant which can be used with the signing_algorithm property of a SignedData.
    #: This constant has a value of "SHA_512_RSA_PKCS1_V1_5"
    SIGNING_ALGORITHM_SHA_512_RSA_PKCS1_V1_5 = "SHA_512_RSA_PKCS1_V1_5"

    #: A constant which can be used with the signing_algorithm property of a SignedData.
    #: This constant has a value of "ECDSA_SHA_256"
    SIGNING_ALGORITHM_ECDSA_SHA_256 = "ECDSA_SHA_256"

    #: A constant which can be used with the signing_algorithm property of a SignedData.
    #: This constant has a value of "ECDSA_SHA_384"
    SIGNING_ALGORITHM_ECDSA_SHA_384 = "ECDSA_SHA_384"

    #: A constant which can be used with the signing_algorithm property of a SignedData.
    #: This constant has a value of "ECDSA_SHA_512"
    SIGNING_ALGORITHM_ECDSA_SHA_512 = "ECDSA_SHA_512"

    def __init__(self, **kwargs):
        """
        Initializes a new SignedData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key_id:
            The value to assign to the key_id property of this SignedData.
        :type key_id: str

        :param key_version_id:
            The value to assign to the key_version_id property of this SignedData.
        :type key_version_id: str

        :param signature:
            The value to assign to the signature property of this SignedData.
        :type signature: str

        :param signing_algorithm:
            The value to assign to the signing_algorithm property of this SignedData.
            Allowed values for this property are: "SHA_224_RSA_PKCS_PSS", "SHA_256_RSA_PKCS_PSS", "SHA_384_RSA_PKCS_PSS", "SHA_512_RSA_PKCS_PSS", "SHA_224_RSA_PKCS1_V1_5", "SHA_256_RSA_PKCS1_V1_5", "SHA_384_RSA_PKCS1_V1_5", "SHA_512_RSA_PKCS1_V1_5", "ECDSA_SHA_256", "ECDSA_SHA_384", "ECDSA_SHA_512", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type signing_algorithm: str

        """
        self.swagger_types = {
            'key_id': 'str',
            'key_version_id': 'str',
            'signature': 'str',
            'signing_algorithm': 'str'
        }

        self.attribute_map = {
            'key_id': 'keyId',
            'key_version_id': 'keyVersionId',
            'signature': 'signature',
            'signing_algorithm': 'signingAlgorithm'
        }

        self._key_id = None
        self._key_version_id = None
        self._signature = None
        self._signing_algorithm = None

    @property
    def key_id(self):
        """
        **[Required]** Gets the key_id of this SignedData.
        The OCID of the key used to sign the message


        :return: The key_id of this SignedData.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this SignedData.
        The OCID of the key used to sign the message


        :param key_id: The key_id of this SignedData.
        :type: str
        """
        self._key_id = key_id

    @property
    def key_version_id(self):
        """
        **[Required]** Gets the key_version_id of this SignedData.
        The OCID of the keyVersion used to sign the message


        :return: The key_version_id of this SignedData.
        :rtype: str
        """
        return self._key_version_id

    @key_version_id.setter
    def key_version_id(self, key_version_id):
        """
        Sets the key_version_id of this SignedData.
        The OCID of the keyVersion used to sign the message


        :param key_version_id: The key_version_id of this SignedData.
        :type: str
        """
        self._key_version_id = key_version_id

    @property
    def signature(self):
        """
        **[Required]** Gets the signature of this SignedData.
        The Base64-encoded binary data object denoting the cryptographic signature that was generated for the message or message digest.


        :return: The signature of this SignedData.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """
        Sets the signature of this SignedData.
        The Base64-encoded binary data object denoting the cryptographic signature that was generated for the message or message digest.


        :param signature: The signature of this SignedData.
        :type: str
        """
        self._signature = signature

    @property
    def signing_algorithm(self):
        """
        **[Required]** Gets the signing_algorithm of this SignedData.
        The algorithm to be used for signing the message or message digest
        For RSA keys, there are two supported Signature Schemes: PKCS1 and PSS along with
        different Hashing algorithms.
        For ECDSA keys, ECDSA is the supported signature scheme with different hashing algorithms.
        In case of passing digest for signing, make sure the same hashing algorithm is
        specified as used for created for digest.

        Allowed values for this property are: "SHA_224_RSA_PKCS_PSS", "SHA_256_RSA_PKCS_PSS", "SHA_384_RSA_PKCS_PSS", "SHA_512_RSA_PKCS_PSS", "SHA_224_RSA_PKCS1_V1_5", "SHA_256_RSA_PKCS1_V1_5", "SHA_384_RSA_PKCS1_V1_5", "SHA_512_RSA_PKCS1_V1_5", "ECDSA_SHA_256", "ECDSA_SHA_384", "ECDSA_SHA_512", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The signing_algorithm of this SignedData.
        :rtype: str
        """
        return self._signing_algorithm

    @signing_algorithm.setter
    def signing_algorithm(self, signing_algorithm):
        """
        Sets the signing_algorithm of this SignedData.
        The algorithm to be used for signing the message or message digest
        For RSA keys, there are two supported Signature Schemes: PKCS1 and PSS along with
        different Hashing algorithms.
        For ECDSA keys, ECDSA is the supported signature scheme with different hashing algorithms.
        In case of passing digest for signing, make sure the same hashing algorithm is
        specified as used for created for digest.


        :param signing_algorithm: The signing_algorithm of this SignedData.
        :type: str
        """
        allowed_values = ["SHA_224_RSA_PKCS_PSS", "SHA_256_RSA_PKCS_PSS", "SHA_384_RSA_PKCS_PSS", "SHA_512_RSA_PKCS_PSS", "SHA_224_RSA_PKCS1_V1_5", "SHA_256_RSA_PKCS1_V1_5", "SHA_384_RSA_PKCS1_V1_5", "SHA_512_RSA_PKCS1_V1_5", "ECDSA_SHA_256", "ECDSA_SHA_384", "ECDSA_SHA_512"]
        if not value_allowed_none_or_none_sentinel(signing_algorithm, allowed_values):
            signing_algorithm = 'UNKNOWN_ENUM_VALUE'
        self._signing_algorithm = signing_algorithm

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
