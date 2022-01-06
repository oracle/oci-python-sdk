# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_certificate_authority_config_details import CreateCertificateAuthorityConfigDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRootCaByGeneratingInternallyConfigDetails(CreateCertificateAuthorityConfigDetails):
    """
    The details for creating a private root certificate authority (CA).
    """

    #: A constant which can be used with the signing_algorithm property of a CreateRootCaByGeneratingInternallyConfigDetails.
    #: This constant has a value of "SHA256_WITH_RSA"
    SIGNING_ALGORITHM_SHA256_WITH_RSA = "SHA256_WITH_RSA"

    #: A constant which can be used with the signing_algorithm property of a CreateRootCaByGeneratingInternallyConfigDetails.
    #: This constant has a value of "SHA384_WITH_RSA"
    SIGNING_ALGORITHM_SHA384_WITH_RSA = "SHA384_WITH_RSA"

    #: A constant which can be used with the signing_algorithm property of a CreateRootCaByGeneratingInternallyConfigDetails.
    #: This constant has a value of "SHA512_WITH_RSA"
    SIGNING_ALGORITHM_SHA512_WITH_RSA = "SHA512_WITH_RSA"

    #: A constant which can be used with the signing_algorithm property of a CreateRootCaByGeneratingInternallyConfigDetails.
    #: This constant has a value of "SHA256_WITH_ECDSA"
    SIGNING_ALGORITHM_SHA256_WITH_ECDSA = "SHA256_WITH_ECDSA"

    #: A constant which can be used with the signing_algorithm property of a CreateRootCaByGeneratingInternallyConfigDetails.
    #: This constant has a value of "SHA384_WITH_ECDSA"
    SIGNING_ALGORITHM_SHA384_WITH_ECDSA = "SHA384_WITH_ECDSA"

    #: A constant which can be used with the signing_algorithm property of a CreateRootCaByGeneratingInternallyConfigDetails.
    #: This constant has a value of "SHA512_WITH_ECDSA"
    SIGNING_ALGORITHM_SHA512_WITH_ECDSA = "SHA512_WITH_ECDSA"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRootCaByGeneratingInternallyConfigDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.certificates_management.models.CreateRootCaByGeneratingInternallyConfigDetails.config_type` attribute
        of this class is ``ROOT_CA_GENERATED_INTERNALLY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_type:
            The value to assign to the config_type property of this CreateRootCaByGeneratingInternallyConfigDetails.
            Allowed values for this property are: "ROOT_CA_GENERATED_INTERNALLY", "SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA"
        :type config_type: str

        :param version_name:
            The value to assign to the version_name property of this CreateRootCaByGeneratingInternallyConfigDetails.
        :type version_name: str

        :param validity:
            The value to assign to the validity property of this CreateRootCaByGeneratingInternallyConfigDetails.
        :type validity: oci.certificates_management.models.Validity

        :param signing_algorithm:
            The value to assign to the signing_algorithm property of this CreateRootCaByGeneratingInternallyConfigDetails.
            Allowed values for this property are: "SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA"
        :type signing_algorithm: str

        :param subject:
            The value to assign to the subject property of this CreateRootCaByGeneratingInternallyConfigDetails.
        :type subject: oci.certificates_management.models.CertificateSubject

        """
        self.swagger_types = {
            'config_type': 'str',
            'version_name': 'str',
            'validity': 'Validity',
            'signing_algorithm': 'str',
            'subject': 'CertificateSubject'
        }

        self.attribute_map = {
            'config_type': 'configType',
            'version_name': 'versionName',
            'validity': 'validity',
            'signing_algorithm': 'signingAlgorithm',
            'subject': 'subject'
        }

        self._config_type = None
        self._version_name = None
        self._validity = None
        self._signing_algorithm = None
        self._subject = None
        self._config_type = 'ROOT_CA_GENERATED_INTERNALLY'

    @property
    def validity(self):
        """
        Gets the validity of this CreateRootCaByGeneratingInternallyConfigDetails.

        :return: The validity of this CreateRootCaByGeneratingInternallyConfigDetails.
        :rtype: oci.certificates_management.models.Validity
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """
        Sets the validity of this CreateRootCaByGeneratingInternallyConfigDetails.

        :param validity: The validity of this CreateRootCaByGeneratingInternallyConfigDetails.
        :type: oci.certificates_management.models.Validity
        """
        self._validity = validity

    @property
    def signing_algorithm(self):
        """
        Gets the signing_algorithm of this CreateRootCaByGeneratingInternallyConfigDetails.
        The algorithm used to sign public key certificates that the CA issues.

        Allowed values for this property are: "SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA"


        :return: The signing_algorithm of this CreateRootCaByGeneratingInternallyConfigDetails.
        :rtype: str
        """
        return self._signing_algorithm

    @signing_algorithm.setter
    def signing_algorithm(self, signing_algorithm):
        """
        Sets the signing_algorithm of this CreateRootCaByGeneratingInternallyConfigDetails.
        The algorithm used to sign public key certificates that the CA issues.


        :param signing_algorithm: The signing_algorithm of this CreateRootCaByGeneratingInternallyConfigDetails.
        :type: str
        """
        allowed_values = ["SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA"]
        if not value_allowed_none_or_none_sentinel(signing_algorithm, allowed_values):
            raise ValueError(
                "Invalid value for `signing_algorithm`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._signing_algorithm = signing_algorithm

    @property
    def subject(self):
        """
        **[Required]** Gets the subject of this CreateRootCaByGeneratingInternallyConfigDetails.

        :return: The subject of this CreateRootCaByGeneratingInternallyConfigDetails.
        :rtype: oci.certificates_management.models.CertificateSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this CreateRootCaByGeneratingInternallyConfigDetails.

        :param subject: The subject of this CreateRootCaByGeneratingInternallyConfigDetails.
        :type: oci.certificates_management.models.CertificateSubject
        """
        self._subject = subject

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
