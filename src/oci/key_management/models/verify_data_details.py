# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VerifyDataDetails(object):
    """
    VerifyDataDetails model.
    """

    #: A constant which can be used with the message_type property of a VerifyDataDetails.
    #: This constant has a value of "RAW"
    MESSAGE_TYPE_RAW = "RAW"

    #: A constant which can be used with the message_type property of a VerifyDataDetails.
    #: This constant has a value of "DIGEST"
    MESSAGE_TYPE_DIGEST = "DIGEST"

    #: A constant which can be used with the signing_algorithm property of a VerifyDataDetails.
    #: This constant has a value of "SHA_224_RSA_PKCS_PSS"
    SIGNING_ALGORITHM_SHA_224_RSA_PKCS_PSS = "SHA_224_RSA_PKCS_PSS"

    #: A constant which can be used with the signing_algorithm property of a VerifyDataDetails.
    #: This constant has a value of "SHA_256_RSA_PKCS_PSS"
    SIGNING_ALGORITHM_SHA_256_RSA_PKCS_PSS = "SHA_256_RSA_PKCS_PSS"

    #: A constant which can be used with the signing_algorithm property of a VerifyDataDetails.
    #: This constant has a value of "SHA_384_RSA_PKCS_PSS"
    SIGNING_ALGORITHM_SHA_384_RSA_PKCS_PSS = "SHA_384_RSA_PKCS_PSS"

    #: A constant which can be used with the signing_algorithm property of a VerifyDataDetails.
    #: This constant has a value of "SHA_512_RSA_PKCS_PSS"
    SIGNING_ALGORITHM_SHA_512_RSA_PKCS_PSS = "SHA_512_RSA_PKCS_PSS"

    #: A constant which can be used with the signing_algorithm property of a VerifyDataDetails.
    #: This constant has a value of "SHA_224_RSA_PKCS1_V1_5"
    SIGNING_ALGORITHM_SHA_224_RSA_PKCS1_V1_5 = "SHA_224_RSA_PKCS1_V1_5"

    #: A constant which can be used with the signing_algorithm property of a VerifyDataDetails.
    #: This constant has a value of "SHA_256_RSA_PKCS1_V1_5"
    SIGNING_ALGORITHM_SHA_256_RSA_PKCS1_V1_5 = "SHA_256_RSA_PKCS1_V1_5"

    #: A constant which can be used with the signing_algorithm property of a VerifyDataDetails.
    #: This constant has a value of "SHA_384_RSA_PKCS1_V1_5"
    SIGNING_ALGORITHM_SHA_384_RSA_PKCS1_V1_5 = "SHA_384_RSA_PKCS1_V1_5"

    #: A constant which can be used with the signing_algorithm property of a VerifyDataDetails.
    #: This constant has a value of "SHA_512_RSA_PKCS1_V1_5"
    SIGNING_ALGORITHM_SHA_512_RSA_PKCS1_V1_5 = "SHA_512_RSA_PKCS1_V1_5"

    #: A constant which can be used with the signing_algorithm property of a VerifyDataDetails.
    #: This constant has a value of "ECDSA_SHA_256"
    SIGNING_ALGORITHM_ECDSA_SHA_256 = "ECDSA_SHA_256"

    #: A constant which can be used with the signing_algorithm property of a VerifyDataDetails.
    #: This constant has a value of "ECDSA_SHA_384"
    SIGNING_ALGORITHM_ECDSA_SHA_384 = "ECDSA_SHA_384"

    #: A constant which can be used with the signing_algorithm property of a VerifyDataDetails.
    #: This constant has a value of "ECDSA_SHA_512"
    SIGNING_ALGORITHM_ECDSA_SHA_512 = "ECDSA_SHA_512"

    def __init__(self, **kwargs):
        """
        Initializes a new VerifyDataDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key_id:
            The value to assign to the key_id property of this VerifyDataDetails.
        :type key_id: str

        :param key_version_id:
            The value to assign to the key_version_id property of this VerifyDataDetails.
        :type key_version_id: str

        :param signature:
            The value to assign to the signature property of this VerifyDataDetails.
        :type signature: str

        :param message_type:
            The value to assign to the message_type property of this VerifyDataDetails.
            Allowed values for this property are: "RAW", "DIGEST"
        :type message_type: str

        :param message:
            The value to assign to the message property of this VerifyDataDetails.
        :type message: str

        :param signing_algorithm:
            The value to assign to the signing_algorithm property of this VerifyDataDetails.
            Allowed values for this property are: "SHA_224_RSA_PKCS_PSS", "SHA_256_RSA_PKCS_PSS", "SHA_384_RSA_PKCS_PSS", "SHA_512_RSA_PKCS_PSS", "SHA_224_RSA_PKCS1_V1_5", "SHA_256_RSA_PKCS1_V1_5", "SHA_384_RSA_PKCS1_V1_5", "SHA_512_RSA_PKCS1_V1_5", "ECDSA_SHA_256", "ECDSA_SHA_384", "ECDSA_SHA_512"
        :type signing_algorithm: str

        """
        self.swagger_types = {
            'key_id': 'str',
            'key_version_id': 'str',
            'signature': 'str',
            'message_type': 'str',
            'message': 'str',
            'signing_algorithm': 'str'
        }

        self.attribute_map = {
            'key_id': 'keyId',
            'key_version_id': 'keyVersionId',
            'signature': 'signature',
            'message_type': 'messageType',
            'message': 'message',
            'signing_algorithm': 'signingAlgorithm'
        }

        self._key_id = None
        self._key_version_id = None
        self._signature = None
        self._message_type = None
        self._message = None
        self._signing_algorithm = None

    @property
    def key_id(self):
        """
        **[Required]** Gets the key_id of this VerifyDataDetails.
        The OCID of the key used to sign the message.


        :return: The key_id of this VerifyDataDetails.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this VerifyDataDetails.
        The OCID of the key used to sign the message.


        :param key_id: The key_id of this VerifyDataDetails.
        :type: str
        """
        self._key_id = key_id

    @property
    def key_version_id(self):
        """
        **[Required]** Gets the key_version_id of this VerifyDataDetails.
        The OCID of the key version used to sign the message.


        :return: The key_version_id of this VerifyDataDetails.
        :rtype: str
        """
        return self._key_version_id

    @key_version_id.setter
    def key_version_id(self, key_version_id):
        """
        Sets the key_version_id of this VerifyDataDetails.
        The OCID of the key version used to sign the message.


        :param key_version_id: The key_version_id of this VerifyDataDetails.
        :type: str
        """
        self._key_version_id = key_version_id

    @property
    def signature(self):
        """
        **[Required]** Gets the signature of this VerifyDataDetails.
        The base64-encoded binary data object denoting the cryptographic signature generated for the message.


        :return: The signature of this VerifyDataDetails.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """
        Sets the signature of this VerifyDataDetails.
        The base64-encoded binary data object denoting the cryptographic signature generated for the message.


        :param signature: The signature of this VerifyDataDetails.
        :type: str
        """
        self._signature = signature

    @property
    def message_type(self):
        """
        Gets the message_type of this VerifyDataDetails.
        Denotes whether the value of the message parameter is a raw message or a message digest.
        The default value, `RAW`, indicates a message. To indicate a message digest, use `DIGEST`.

        Allowed values for this property are: "RAW", "DIGEST"


        :return: The message_type of this VerifyDataDetails.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """
        Sets the message_type of this VerifyDataDetails.
        Denotes whether the value of the message parameter is a raw message or a message digest.
        The default value, `RAW`, indicates a message. To indicate a message digest, use `DIGEST`.


        :param message_type: The message_type of this VerifyDataDetails.
        :type: str
        """
        allowed_values = ["RAW", "DIGEST"]
        if not value_allowed_none_or_none_sentinel(message_type, allowed_values):
            raise ValueError(
                "Invalid value for `message_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._message_type = message_type

    @property
    def message(self):
        """
        **[Required]** Gets the message of this VerifyDataDetails.
        The base64-encoded binary data object denoting the message or message digest to sign. You can have a message up to 4096 bytes in size. To sign a larger message, provide the message digest.


        :return: The message of this VerifyDataDetails.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this VerifyDataDetails.
        The base64-encoded binary data object denoting the message or message digest to sign. You can have a message up to 4096 bytes in size. To sign a larger message, provide the message digest.


        :param message: The message of this VerifyDataDetails.
        :type: str
        """
        self._message = message

    @property
    def signing_algorithm(self):
        """
        **[Required]** Gets the signing_algorithm of this VerifyDataDetails.
        The algorithm to use to sign the message or message digest.
        For RSA keys, supported signature schemes include PKCS #1 and RSASSA-PSS, along with
        different hashing algorithms.
        For ECDSA keys, ECDSA is the supported signature scheme with different hashing algorithms.
        When you pass a message digest for signing, ensure that you specify the same hashing algorithm
        as used when creating the message digest.

        Allowed values for this property are: "SHA_224_RSA_PKCS_PSS", "SHA_256_RSA_PKCS_PSS", "SHA_384_RSA_PKCS_PSS", "SHA_512_RSA_PKCS_PSS", "SHA_224_RSA_PKCS1_V1_5", "SHA_256_RSA_PKCS1_V1_5", "SHA_384_RSA_PKCS1_V1_5", "SHA_512_RSA_PKCS1_V1_5", "ECDSA_SHA_256", "ECDSA_SHA_384", "ECDSA_SHA_512"


        :return: The signing_algorithm of this VerifyDataDetails.
        :rtype: str
        """
        return self._signing_algorithm

    @signing_algorithm.setter
    def signing_algorithm(self, signing_algorithm):
        """
        Sets the signing_algorithm of this VerifyDataDetails.
        The algorithm to use to sign the message or message digest.
        For RSA keys, supported signature schemes include PKCS #1 and RSASSA-PSS, along with
        different hashing algorithms.
        For ECDSA keys, ECDSA is the supported signature scheme with different hashing algorithms.
        When you pass a message digest for signing, ensure that you specify the same hashing algorithm
        as used when creating the message digest.


        :param signing_algorithm: The signing_algorithm of this VerifyDataDetails.
        :type: str
        """
        allowed_values = ["SHA_224_RSA_PKCS_PSS", "SHA_256_RSA_PKCS_PSS", "SHA_384_RSA_PKCS_PSS", "SHA_512_RSA_PKCS_PSS", "SHA_224_RSA_PKCS1_V1_5", "SHA_256_RSA_PKCS1_V1_5", "SHA_384_RSA_PKCS1_V1_5", "SHA_512_RSA_PKCS1_V1_5", "ECDSA_SHA_256", "ECDSA_SHA_384", "ECDSA_SHA_512"]
        if not value_allowed_none_or_none_sentinel(signing_algorithm, allowed_values):
            raise ValueError(
                "Invalid value for `signing_algorithm`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._signing_algorithm = signing_algorithm

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
