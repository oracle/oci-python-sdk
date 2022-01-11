# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateContainerImageSignatureDetails(object):
    """
    Upload container image signature request details.
    """

    #: A constant which can be used with the signing_algorithm property of a CreateContainerImageSignatureDetails.
    #: This constant has a value of "SHA_224_RSA_PKCS_PSS"
    SIGNING_ALGORITHM_SHA_224_RSA_PKCS_PSS = "SHA_224_RSA_PKCS_PSS"

    #: A constant which can be used with the signing_algorithm property of a CreateContainerImageSignatureDetails.
    #: This constant has a value of "SHA_256_RSA_PKCS_PSS"
    SIGNING_ALGORITHM_SHA_256_RSA_PKCS_PSS = "SHA_256_RSA_PKCS_PSS"

    #: A constant which can be used with the signing_algorithm property of a CreateContainerImageSignatureDetails.
    #: This constant has a value of "SHA_384_RSA_PKCS_PSS"
    SIGNING_ALGORITHM_SHA_384_RSA_PKCS_PSS = "SHA_384_RSA_PKCS_PSS"

    #: A constant which can be used with the signing_algorithm property of a CreateContainerImageSignatureDetails.
    #: This constant has a value of "SHA_512_RSA_PKCS_PSS"
    SIGNING_ALGORITHM_SHA_512_RSA_PKCS_PSS = "SHA_512_RSA_PKCS_PSS"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateContainerImageSignatureDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateContainerImageSignatureDetails.
        :type compartment_id: str

        :param image_id:
            The value to assign to the image_id property of this CreateContainerImageSignatureDetails.
        :type image_id: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this CreateContainerImageSignatureDetails.
        :type kms_key_id: str

        :param kms_key_version_id:
            The value to assign to the kms_key_version_id property of this CreateContainerImageSignatureDetails.
        :type kms_key_version_id: str

        :param message:
            The value to assign to the message property of this CreateContainerImageSignatureDetails.
        :type message: str

        :param signature:
            The value to assign to the signature property of this CreateContainerImageSignatureDetails.
        :type signature: str

        :param signing_algorithm:
            The value to assign to the signing_algorithm property of this CreateContainerImageSignatureDetails.
            Allowed values for this property are: "SHA_224_RSA_PKCS_PSS", "SHA_256_RSA_PKCS_PSS", "SHA_384_RSA_PKCS_PSS", "SHA_512_RSA_PKCS_PSS"
        :type signing_algorithm: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'image_id': 'str',
            'kms_key_id': 'str',
            'kms_key_version_id': 'str',
            'message': 'str',
            'signature': 'str',
            'signing_algorithm': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'image_id': 'imageId',
            'kms_key_id': 'kmsKeyId',
            'kms_key_version_id': 'kmsKeyVersionId',
            'message': 'message',
            'signature': 'signature',
            'signing_algorithm': 'signingAlgorithm'
        }

        self._compartment_id = None
        self._image_id = None
        self._kms_key_id = None
        self._kms_key_version_id = None
        self._message = None
        self._signature = None
        self._signing_algorithm = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateContainerImageSignatureDetails.
        The `OCID`__ of the compartment in which the container repository exists.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateContainerImageSignatureDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateContainerImageSignatureDetails.
        The `OCID`__ of the compartment in which the container repository exists.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateContainerImageSignatureDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def image_id(self):
        """
        **[Required]** Gets the image_id of this CreateContainerImageSignatureDetails.
        The `OCID`__ of the container image.

        Example: `ocid1.containerimage.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The image_id of this CreateContainerImageSignatureDetails.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this CreateContainerImageSignatureDetails.
        The `OCID`__ of the container image.

        Example: `ocid1.containerimage.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param image_id: The image_id of this CreateContainerImageSignatureDetails.
        :type: str
        """
        self._image_id = image_id

    @property
    def kms_key_id(self):
        """
        **[Required]** Gets the kms_key_id of this CreateContainerImageSignatureDetails.
        The `OCID`__ of the kmsKeyId used to sign the container image.

        Example: `ocid1.key.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The kms_key_id of this CreateContainerImageSignatureDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this CreateContainerImageSignatureDetails.
        The `OCID`__ of the kmsKeyId used to sign the container image.

        Example: `ocid1.key.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param kms_key_id: The kms_key_id of this CreateContainerImageSignatureDetails.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def kms_key_version_id(self):
        """
        **[Required]** Gets the kms_key_version_id of this CreateContainerImageSignatureDetails.
        The `OCID`__ of the kmsKeyVersionId used to sign the container image.

        Example: `ocid1.keyversion.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The kms_key_version_id of this CreateContainerImageSignatureDetails.
        :rtype: str
        """
        return self._kms_key_version_id

    @kms_key_version_id.setter
    def kms_key_version_id(self, kms_key_version_id):
        """
        Sets the kms_key_version_id of this CreateContainerImageSignatureDetails.
        The `OCID`__ of the kmsKeyVersionId used to sign the container image.

        Example: `ocid1.keyversion.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param kms_key_version_id: The kms_key_version_id of this CreateContainerImageSignatureDetails.
        :type: str
        """
        self._kms_key_version_id = kms_key_version_id

    @property
    def message(self):
        """
        **[Required]** Gets the message of this CreateContainerImageSignatureDetails.
        The base64 encoded signature payload that was signed.


        :return: The message of this CreateContainerImageSignatureDetails.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this CreateContainerImageSignatureDetails.
        The base64 encoded signature payload that was signed.


        :param message: The message of this CreateContainerImageSignatureDetails.
        :type: str
        """
        self._message = message

    @property
    def signature(self):
        """
        **[Required]** Gets the signature of this CreateContainerImageSignatureDetails.
        The signature of the message field using the kmsKeyId, the kmsKeyVersionId, and the signingAlgorithm.


        :return: The signature of this CreateContainerImageSignatureDetails.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """
        Sets the signature of this CreateContainerImageSignatureDetails.
        The signature of the message field using the kmsKeyId, the kmsKeyVersionId, and the signingAlgorithm.


        :param signature: The signature of this CreateContainerImageSignatureDetails.
        :type: str
        """
        self._signature = signature

    @property
    def signing_algorithm(self):
        """
        **[Required]** Gets the signing_algorithm of this CreateContainerImageSignatureDetails.
        The algorithm to be used for signing. These are the only supported signing algorithms for container images.

        Allowed values for this property are: "SHA_224_RSA_PKCS_PSS", "SHA_256_RSA_PKCS_PSS", "SHA_384_RSA_PKCS_PSS", "SHA_512_RSA_PKCS_PSS"


        :return: The signing_algorithm of this CreateContainerImageSignatureDetails.
        :rtype: str
        """
        return self._signing_algorithm

    @signing_algorithm.setter
    def signing_algorithm(self, signing_algorithm):
        """
        Sets the signing_algorithm of this CreateContainerImageSignatureDetails.
        The algorithm to be used for signing. These are the only supported signing algorithms for container images.


        :param signing_algorithm: The signing_algorithm of this CreateContainerImageSignatureDetails.
        :type: str
        """
        allowed_values = ["SHA_224_RSA_PKCS_PSS", "SHA_256_RSA_PKCS_PSS", "SHA_384_RSA_PKCS_PSS", "SHA_512_RSA_PKCS_PSS"]
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
