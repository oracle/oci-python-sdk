# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_certificate_config_details import CreateCertificateConfigDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCertificateByImportingConfigDetails(CreateCertificateConfigDetails):
    """
    The details of the configuration for creating a certificate based on the keys from an imported certificate.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCertificateByImportingConfigDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.certificates_management.models.CreateCertificateByImportingConfigDetails.config_type` attribute
        of this class is ``IMPORTED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_type:
            The value to assign to the config_type property of this CreateCertificateByImportingConfigDetails.
            Allowed values for this property are: "ISSUED_BY_INTERNAL_CA", "MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA", "IMPORTED"
        :type config_type: str

        :param version_name:
            The value to assign to the version_name property of this CreateCertificateByImportingConfigDetails.
        :type version_name: str

        :param cert_chain_pem:
            The value to assign to the cert_chain_pem property of this CreateCertificateByImportingConfigDetails.
        :type cert_chain_pem: str

        :param private_key_pem:
            The value to assign to the private_key_pem property of this CreateCertificateByImportingConfigDetails.
        :type private_key_pem: str

        :param certificate_pem:
            The value to assign to the certificate_pem property of this CreateCertificateByImportingConfigDetails.
        :type certificate_pem: str

        :param private_key_pem_passphrase:
            The value to assign to the private_key_pem_passphrase property of this CreateCertificateByImportingConfigDetails.
        :type private_key_pem_passphrase: str

        """
        self.swagger_types = {
            'config_type': 'str',
            'version_name': 'str',
            'cert_chain_pem': 'str',
            'private_key_pem': 'str',
            'certificate_pem': 'str',
            'private_key_pem_passphrase': 'str'
        }

        self.attribute_map = {
            'config_type': 'configType',
            'version_name': 'versionName',
            'cert_chain_pem': 'certChainPem',
            'private_key_pem': 'privateKeyPem',
            'certificate_pem': 'certificatePem',
            'private_key_pem_passphrase': 'privateKeyPemPassphrase'
        }

        self._config_type = None
        self._version_name = None
        self._cert_chain_pem = None
        self._private_key_pem = None
        self._certificate_pem = None
        self._private_key_pem_passphrase = None
        self._config_type = 'IMPORTED'

    @property
    def cert_chain_pem(self):
        """
        **[Required]** Gets the cert_chain_pem of this CreateCertificateByImportingConfigDetails.
        The certificate chain (in PEM format) for the imported certificate.


        :return: The cert_chain_pem of this CreateCertificateByImportingConfigDetails.
        :rtype: str
        """
        return self._cert_chain_pem

    @cert_chain_pem.setter
    def cert_chain_pem(self, cert_chain_pem):
        """
        Sets the cert_chain_pem of this CreateCertificateByImportingConfigDetails.
        The certificate chain (in PEM format) for the imported certificate.


        :param cert_chain_pem: The cert_chain_pem of this CreateCertificateByImportingConfigDetails.
        :type: str
        """
        self._cert_chain_pem = cert_chain_pem

    @property
    def private_key_pem(self):
        """
        **[Required]** Gets the private_key_pem of this CreateCertificateByImportingConfigDetails.
        The private key (in PEM format) for the imported certificate.


        :return: The private_key_pem of this CreateCertificateByImportingConfigDetails.
        :rtype: str
        """
        return self._private_key_pem

    @private_key_pem.setter
    def private_key_pem(self, private_key_pem):
        """
        Sets the private_key_pem of this CreateCertificateByImportingConfigDetails.
        The private key (in PEM format) for the imported certificate.


        :param private_key_pem: The private_key_pem of this CreateCertificateByImportingConfigDetails.
        :type: str
        """
        self._private_key_pem = private_key_pem

    @property
    def certificate_pem(self):
        """
        **[Required]** Gets the certificate_pem of this CreateCertificateByImportingConfigDetails.
        The certificate (in PEM format) for the imported certificate.


        :return: The certificate_pem of this CreateCertificateByImportingConfigDetails.
        :rtype: str
        """
        return self._certificate_pem

    @certificate_pem.setter
    def certificate_pem(self, certificate_pem):
        """
        Sets the certificate_pem of this CreateCertificateByImportingConfigDetails.
        The certificate (in PEM format) for the imported certificate.


        :param certificate_pem: The certificate_pem of this CreateCertificateByImportingConfigDetails.
        :type: str
        """
        self._certificate_pem = certificate_pem

    @property
    def private_key_pem_passphrase(self):
        """
        Gets the private_key_pem_passphrase of this CreateCertificateByImportingConfigDetails.
        An optional passphrase for the private key.


        :return: The private_key_pem_passphrase of this CreateCertificateByImportingConfigDetails.
        :rtype: str
        """
        return self._private_key_pem_passphrase

    @private_key_pem_passphrase.setter
    def private_key_pem_passphrase(self, private_key_pem_passphrase):
        """
        Sets the private_key_pem_passphrase of this CreateCertificateByImportingConfigDetails.
        An optional passphrase for the private key.


        :param private_key_pem_passphrase: The private_key_pem_passphrase of this CreateCertificateByImportingConfigDetails.
        :type: str
        """
        self._private_key_pem_passphrase = private_key_pem_passphrase

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
