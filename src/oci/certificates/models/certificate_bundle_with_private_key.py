# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .certificate_bundle import CertificateBundle
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificateBundleWithPrivateKey(CertificateBundle):
    """
    A certificate bundle, including the private key.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CertificateBundleWithPrivateKey object with values from keyword arguments. The default value of the :py:attr:`~oci.certificates.models.CertificateBundleWithPrivateKey.certificate_bundle_type` attribute
        of this class is ``CERTIFICATE_CONTENT_WITH_PRIVATE_KEY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate_bundle_type:
            The value to assign to the certificate_bundle_type property of this CertificateBundleWithPrivateKey.
            Allowed values for this property are: "CERTIFICATE_CONTENT_PUBLIC_ONLY", "CERTIFICATE_CONTENT_WITH_PRIVATE_KEY"
        :type certificate_bundle_type: str

        :param certificate_id:
            The value to assign to the certificate_id property of this CertificateBundleWithPrivateKey.
        :type certificate_id: str

        :param certificate_name:
            The value to assign to the certificate_name property of this CertificateBundleWithPrivateKey.
        :type certificate_name: str

        :param version_number:
            The value to assign to the version_number property of this CertificateBundleWithPrivateKey.
        :type version_number: int

        :param serial_number:
            The value to assign to the serial_number property of this CertificateBundleWithPrivateKey.
        :type serial_number: str

        :param certificate_pem:
            The value to assign to the certificate_pem property of this CertificateBundleWithPrivateKey.
        :type certificate_pem: str

        :param cert_chain_pem:
            The value to assign to the cert_chain_pem property of this CertificateBundleWithPrivateKey.
        :type cert_chain_pem: str

        :param time_created:
            The value to assign to the time_created property of this CertificateBundleWithPrivateKey.
        :type time_created: datetime

        :param validity:
            The value to assign to the validity property of this CertificateBundleWithPrivateKey.
        :type validity: oci.certificates.models.Validity

        :param version_name:
            The value to assign to the version_name property of this CertificateBundleWithPrivateKey.
        :type version_name: str

        :param stages:
            The value to assign to the stages property of this CertificateBundleWithPrivateKey.
            Allowed values for items in this list are: "CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED", "FAILED"
        :type stages: list[str]

        :param revocation_status:
            The value to assign to the revocation_status property of this CertificateBundleWithPrivateKey.
        :type revocation_status: oci.certificates.models.RevocationStatus

        :param private_key_pem:
            The value to assign to the private_key_pem property of this CertificateBundleWithPrivateKey.
        :type private_key_pem: str

        :param private_key_pem_passphrase:
            The value to assign to the private_key_pem_passphrase property of this CertificateBundleWithPrivateKey.
        :type private_key_pem_passphrase: str

        """
        self.swagger_types = {
            'certificate_bundle_type': 'str',
            'certificate_id': 'str',
            'certificate_name': 'str',
            'version_number': 'int',
            'serial_number': 'str',
            'certificate_pem': 'str',
            'cert_chain_pem': 'str',
            'time_created': 'datetime',
            'validity': 'Validity',
            'version_name': 'str',
            'stages': 'list[str]',
            'revocation_status': 'RevocationStatus',
            'private_key_pem': 'str',
            'private_key_pem_passphrase': 'str'
        }

        self.attribute_map = {
            'certificate_bundle_type': 'certificateBundleType',
            'certificate_id': 'certificateId',
            'certificate_name': 'certificateName',
            'version_number': 'versionNumber',
            'serial_number': 'serialNumber',
            'certificate_pem': 'certificatePem',
            'cert_chain_pem': 'certChainPem',
            'time_created': 'timeCreated',
            'validity': 'validity',
            'version_name': 'versionName',
            'stages': 'stages',
            'revocation_status': 'revocationStatus',
            'private_key_pem': 'privateKeyPem',
            'private_key_pem_passphrase': 'privateKeyPemPassphrase'
        }

        self._certificate_bundle_type = None
        self._certificate_id = None
        self._certificate_name = None
        self._version_number = None
        self._serial_number = None
        self._certificate_pem = None
        self._cert_chain_pem = None
        self._time_created = None
        self._validity = None
        self._version_name = None
        self._stages = None
        self._revocation_status = None
        self._private_key_pem = None
        self._private_key_pem_passphrase = None
        self._certificate_bundle_type = 'CERTIFICATE_CONTENT_WITH_PRIVATE_KEY'

    @property
    def private_key_pem(self):
        """
        **[Required]** Gets the private_key_pem of this CertificateBundleWithPrivateKey.
        The private key (in PEM format) for the certificate.


        :return: The private_key_pem of this CertificateBundleWithPrivateKey.
        :rtype: str
        """
        return self._private_key_pem

    @private_key_pem.setter
    def private_key_pem(self, private_key_pem):
        """
        Sets the private_key_pem of this CertificateBundleWithPrivateKey.
        The private key (in PEM format) for the certificate.


        :param private_key_pem: The private_key_pem of this CertificateBundleWithPrivateKey.
        :type: str
        """
        self._private_key_pem = private_key_pem

    @property
    def private_key_pem_passphrase(self):
        """
        Gets the private_key_pem_passphrase of this CertificateBundleWithPrivateKey.
        An optional passphrase for the private key.


        :return: The private_key_pem_passphrase of this CertificateBundleWithPrivateKey.
        :rtype: str
        """
        return self._private_key_pem_passphrase

    @private_key_pem_passphrase.setter
    def private_key_pem_passphrase(self, private_key_pem_passphrase):
        """
        Sets the private_key_pem_passphrase of this CertificateBundleWithPrivateKey.
        An optional passphrase for the private key.


        :param private_key_pem_passphrase: The private_key_pem_passphrase of this CertificateBundleWithPrivateKey.
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
