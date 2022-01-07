# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_certificate_config_details import CreateCertificateConfigDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCertificateIssuedByInternalCaConfigDetails(CreateCertificateConfigDetails):
    """
    The details of the configuration for creating an internally managed certificate which is issued by a private certificate authority (CA).
    """

    #: A constant which can be used with the certificate_profile_type property of a CreateCertificateIssuedByInternalCaConfigDetails.
    #: This constant has a value of "TLS_SERVER_OR_CLIENT"
    CERTIFICATE_PROFILE_TYPE_TLS_SERVER_OR_CLIENT = "TLS_SERVER_OR_CLIENT"

    #: A constant which can be used with the certificate_profile_type property of a CreateCertificateIssuedByInternalCaConfigDetails.
    #: This constant has a value of "TLS_SERVER"
    CERTIFICATE_PROFILE_TYPE_TLS_SERVER = "TLS_SERVER"

    #: A constant which can be used with the certificate_profile_type property of a CreateCertificateIssuedByInternalCaConfigDetails.
    #: This constant has a value of "TLS_CLIENT"
    CERTIFICATE_PROFILE_TYPE_TLS_CLIENT = "TLS_CLIENT"

    #: A constant which can be used with the certificate_profile_type property of a CreateCertificateIssuedByInternalCaConfigDetails.
    #: This constant has a value of "TLS_CODE_SIGN"
    CERTIFICATE_PROFILE_TYPE_TLS_CODE_SIGN = "TLS_CODE_SIGN"

    #: A constant which can be used with the key_algorithm property of a CreateCertificateIssuedByInternalCaConfigDetails.
    #: This constant has a value of "RSA2048"
    KEY_ALGORITHM_RSA2048 = "RSA2048"

    #: A constant which can be used with the key_algorithm property of a CreateCertificateIssuedByInternalCaConfigDetails.
    #: This constant has a value of "RSA4096"
    KEY_ALGORITHM_RSA4096 = "RSA4096"

    #: A constant which can be used with the key_algorithm property of a CreateCertificateIssuedByInternalCaConfigDetails.
    #: This constant has a value of "ECDSA_P256"
    KEY_ALGORITHM_ECDSA_P256 = "ECDSA_P256"

    #: A constant which can be used with the key_algorithm property of a CreateCertificateIssuedByInternalCaConfigDetails.
    #: This constant has a value of "ECDSA_P384"
    KEY_ALGORITHM_ECDSA_P384 = "ECDSA_P384"

    #: A constant which can be used with the signature_algorithm property of a CreateCertificateIssuedByInternalCaConfigDetails.
    #: This constant has a value of "SHA256_WITH_RSA"
    SIGNATURE_ALGORITHM_SHA256_WITH_RSA = "SHA256_WITH_RSA"

    #: A constant which can be used with the signature_algorithm property of a CreateCertificateIssuedByInternalCaConfigDetails.
    #: This constant has a value of "SHA384_WITH_RSA"
    SIGNATURE_ALGORITHM_SHA384_WITH_RSA = "SHA384_WITH_RSA"

    #: A constant which can be used with the signature_algorithm property of a CreateCertificateIssuedByInternalCaConfigDetails.
    #: This constant has a value of "SHA512_WITH_RSA"
    SIGNATURE_ALGORITHM_SHA512_WITH_RSA = "SHA512_WITH_RSA"

    #: A constant which can be used with the signature_algorithm property of a CreateCertificateIssuedByInternalCaConfigDetails.
    #: This constant has a value of "SHA256_WITH_ECDSA"
    SIGNATURE_ALGORITHM_SHA256_WITH_ECDSA = "SHA256_WITH_ECDSA"

    #: A constant which can be used with the signature_algorithm property of a CreateCertificateIssuedByInternalCaConfigDetails.
    #: This constant has a value of "SHA384_WITH_ECDSA"
    SIGNATURE_ALGORITHM_SHA384_WITH_ECDSA = "SHA384_WITH_ECDSA"

    #: A constant which can be used with the signature_algorithm property of a CreateCertificateIssuedByInternalCaConfigDetails.
    #: This constant has a value of "SHA512_WITH_ECDSA"
    SIGNATURE_ALGORITHM_SHA512_WITH_ECDSA = "SHA512_WITH_ECDSA"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCertificateIssuedByInternalCaConfigDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.certificates_management.models.CreateCertificateIssuedByInternalCaConfigDetails.config_type` attribute
        of this class is ``ISSUED_BY_INTERNAL_CA`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_type:
            The value to assign to the config_type property of this CreateCertificateIssuedByInternalCaConfigDetails.
            Allowed values for this property are: "ISSUED_BY_INTERNAL_CA", "MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA", "IMPORTED"
        :type config_type: str

        :param version_name:
            The value to assign to the version_name property of this CreateCertificateIssuedByInternalCaConfigDetails.
        :type version_name: str

        :param certificate_profile_type:
            The value to assign to the certificate_profile_type property of this CreateCertificateIssuedByInternalCaConfigDetails.
            Allowed values for this property are: "TLS_SERVER_OR_CLIENT", "TLS_SERVER", "TLS_CLIENT", "TLS_CODE_SIGN"
        :type certificate_profile_type: str

        :param issuer_certificate_authority_id:
            The value to assign to the issuer_certificate_authority_id property of this CreateCertificateIssuedByInternalCaConfigDetails.
        :type issuer_certificate_authority_id: str

        :param validity:
            The value to assign to the validity property of this CreateCertificateIssuedByInternalCaConfigDetails.
        :type validity: oci.certificates_management.models.Validity

        :param subject:
            The value to assign to the subject property of this CreateCertificateIssuedByInternalCaConfigDetails.
        :type subject: oci.certificates_management.models.CertificateSubject

        :param subject_alternative_names:
            The value to assign to the subject_alternative_names property of this CreateCertificateIssuedByInternalCaConfigDetails.
        :type subject_alternative_names: list[oci.certificates_management.models.CertificateSubjectAlternativeName]

        :param key_algorithm:
            The value to assign to the key_algorithm property of this CreateCertificateIssuedByInternalCaConfigDetails.
            Allowed values for this property are: "RSA2048", "RSA4096", "ECDSA_P256", "ECDSA_P384"
        :type key_algorithm: str

        :param signature_algorithm:
            The value to assign to the signature_algorithm property of this CreateCertificateIssuedByInternalCaConfigDetails.
            Allowed values for this property are: "SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA"
        :type signature_algorithm: str

        """
        self.swagger_types = {
            'config_type': 'str',
            'version_name': 'str',
            'certificate_profile_type': 'str',
            'issuer_certificate_authority_id': 'str',
            'validity': 'Validity',
            'subject': 'CertificateSubject',
            'subject_alternative_names': 'list[CertificateSubjectAlternativeName]',
            'key_algorithm': 'str',
            'signature_algorithm': 'str'
        }

        self.attribute_map = {
            'config_type': 'configType',
            'version_name': 'versionName',
            'certificate_profile_type': 'certificateProfileType',
            'issuer_certificate_authority_id': 'issuerCertificateAuthorityId',
            'validity': 'validity',
            'subject': 'subject',
            'subject_alternative_names': 'subjectAlternativeNames',
            'key_algorithm': 'keyAlgorithm',
            'signature_algorithm': 'signatureAlgorithm'
        }

        self._config_type = None
        self._version_name = None
        self._certificate_profile_type = None
        self._issuer_certificate_authority_id = None
        self._validity = None
        self._subject = None
        self._subject_alternative_names = None
        self._key_algorithm = None
        self._signature_algorithm = None
        self._config_type = 'ISSUED_BY_INTERNAL_CA'

    @property
    def certificate_profile_type(self):
        """
        **[Required]** Gets the certificate_profile_type of this CreateCertificateIssuedByInternalCaConfigDetails.
        The name of the profile used to create the certificate, which depends on the type of certificate you need.

        Allowed values for this property are: "TLS_SERVER_OR_CLIENT", "TLS_SERVER", "TLS_CLIENT", "TLS_CODE_SIGN"


        :return: The certificate_profile_type of this CreateCertificateIssuedByInternalCaConfigDetails.
        :rtype: str
        """
        return self._certificate_profile_type

    @certificate_profile_type.setter
    def certificate_profile_type(self, certificate_profile_type):
        """
        Sets the certificate_profile_type of this CreateCertificateIssuedByInternalCaConfigDetails.
        The name of the profile used to create the certificate, which depends on the type of certificate you need.


        :param certificate_profile_type: The certificate_profile_type of this CreateCertificateIssuedByInternalCaConfigDetails.
        :type: str
        """
        allowed_values = ["TLS_SERVER_OR_CLIENT", "TLS_SERVER", "TLS_CLIENT", "TLS_CODE_SIGN"]
        if not value_allowed_none_or_none_sentinel(certificate_profile_type, allowed_values):
            raise ValueError(
                "Invalid value for `certificate_profile_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._certificate_profile_type = certificate_profile_type

    @property
    def issuer_certificate_authority_id(self):
        """
        **[Required]** Gets the issuer_certificate_authority_id of this CreateCertificateIssuedByInternalCaConfigDetails.
        The OCID of the private CA.


        :return: The issuer_certificate_authority_id of this CreateCertificateIssuedByInternalCaConfigDetails.
        :rtype: str
        """
        return self._issuer_certificate_authority_id

    @issuer_certificate_authority_id.setter
    def issuer_certificate_authority_id(self, issuer_certificate_authority_id):
        """
        Sets the issuer_certificate_authority_id of this CreateCertificateIssuedByInternalCaConfigDetails.
        The OCID of the private CA.


        :param issuer_certificate_authority_id: The issuer_certificate_authority_id of this CreateCertificateIssuedByInternalCaConfigDetails.
        :type: str
        """
        self._issuer_certificate_authority_id = issuer_certificate_authority_id

    @property
    def validity(self):
        """
        Gets the validity of this CreateCertificateIssuedByInternalCaConfigDetails.

        :return: The validity of this CreateCertificateIssuedByInternalCaConfigDetails.
        :rtype: oci.certificates_management.models.Validity
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """
        Sets the validity of this CreateCertificateIssuedByInternalCaConfigDetails.

        :param validity: The validity of this CreateCertificateIssuedByInternalCaConfigDetails.
        :type: oci.certificates_management.models.Validity
        """
        self._validity = validity

    @property
    def subject(self):
        """
        **[Required]** Gets the subject of this CreateCertificateIssuedByInternalCaConfigDetails.

        :return: The subject of this CreateCertificateIssuedByInternalCaConfigDetails.
        :rtype: oci.certificates_management.models.CertificateSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this CreateCertificateIssuedByInternalCaConfigDetails.

        :param subject: The subject of this CreateCertificateIssuedByInternalCaConfigDetails.
        :type: oci.certificates_management.models.CertificateSubject
        """
        self._subject = subject

    @property
    def subject_alternative_names(self):
        """
        Gets the subject_alternative_names of this CreateCertificateIssuedByInternalCaConfigDetails.
        A list of subject alternative names.


        :return: The subject_alternative_names of this CreateCertificateIssuedByInternalCaConfigDetails.
        :rtype: list[oci.certificates_management.models.CertificateSubjectAlternativeName]
        """
        return self._subject_alternative_names

    @subject_alternative_names.setter
    def subject_alternative_names(self, subject_alternative_names):
        """
        Sets the subject_alternative_names of this CreateCertificateIssuedByInternalCaConfigDetails.
        A list of subject alternative names.


        :param subject_alternative_names: The subject_alternative_names of this CreateCertificateIssuedByInternalCaConfigDetails.
        :type: list[oci.certificates_management.models.CertificateSubjectAlternativeName]
        """
        self._subject_alternative_names = subject_alternative_names

    @property
    def key_algorithm(self):
        """
        Gets the key_algorithm of this CreateCertificateIssuedByInternalCaConfigDetails.
        The algorithm to use to create key pairs.

        Allowed values for this property are: "RSA2048", "RSA4096", "ECDSA_P256", "ECDSA_P384"


        :return: The key_algorithm of this CreateCertificateIssuedByInternalCaConfigDetails.
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        """
        Sets the key_algorithm of this CreateCertificateIssuedByInternalCaConfigDetails.
        The algorithm to use to create key pairs.


        :param key_algorithm: The key_algorithm of this CreateCertificateIssuedByInternalCaConfigDetails.
        :type: str
        """
        allowed_values = ["RSA2048", "RSA4096", "ECDSA_P256", "ECDSA_P384"]
        if not value_allowed_none_or_none_sentinel(key_algorithm, allowed_values):
            raise ValueError(
                "Invalid value for `key_algorithm`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._key_algorithm = key_algorithm

    @property
    def signature_algorithm(self):
        """
        Gets the signature_algorithm of this CreateCertificateIssuedByInternalCaConfigDetails.
        The algorithm to use to sign the public key certificate.

        Allowed values for this property are: "SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA"


        :return: The signature_algorithm of this CreateCertificateIssuedByInternalCaConfigDetails.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """
        Sets the signature_algorithm of this CreateCertificateIssuedByInternalCaConfigDetails.
        The algorithm to use to sign the public key certificate.


        :param signature_algorithm: The signature_algorithm of this CreateCertificateIssuedByInternalCaConfigDetails.
        :type: str
        """
        allowed_values = ["SHA256_WITH_RSA", "SHA384_WITH_RSA", "SHA512_WITH_RSA", "SHA256_WITH_ECDSA", "SHA384_WITH_ECDSA", "SHA512_WITH_ECDSA"]
        if not value_allowed_none_or_none_sentinel(signature_algorithm, allowed_values):
            raise ValueError(
                "Invalid value for `signature_algorithm`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._signature_algorithm = signature_algorithm

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
