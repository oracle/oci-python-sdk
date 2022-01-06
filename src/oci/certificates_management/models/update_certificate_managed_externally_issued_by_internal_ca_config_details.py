# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_certificate_config_details import UpdateCertificateConfigDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails(UpdateCertificateConfigDetails):
    """
    The details for updating an externally managed certificate which is issued by a private certificate authority (CA).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.certificates_management.models.UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails.config_type` attribute
        of this class is ``MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_type:
            The value to assign to the config_type property of this UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails.
            Allowed values for this property are: "ISSUED_BY_INTERNAL_CA", "MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA", "IMPORTED"
        :type config_type: str

        :param version_name:
            The value to assign to the version_name property of this UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails.
        :type version_name: str

        :param stage:
            The value to assign to the stage property of this UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails.
            Allowed values for this property are: "CURRENT", "PENDING"
        :type stage: str

        :param csr_pem:
            The value to assign to the csr_pem property of this UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails.
        :type csr_pem: str

        :param validity:
            The value to assign to the validity property of this UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails.
        :type validity: oci.certificates_management.models.Validity

        """
        self.swagger_types = {
            'config_type': 'str',
            'version_name': 'str',
            'stage': 'str',
            'csr_pem': 'str',
            'validity': 'Validity'
        }

        self.attribute_map = {
            'config_type': 'configType',
            'version_name': 'versionName',
            'stage': 'stage',
            'csr_pem': 'csrPem',
            'validity': 'validity'
        }

        self._config_type = None
        self._version_name = None
        self._stage = None
        self._csr_pem = None
        self._validity = None
        self._config_type = 'MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA'

    @property
    def csr_pem(self):
        """
        **[Required]** Gets the csr_pem of this UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails.
        The certificate signing request (in PEM format).


        :return: The csr_pem of this UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails.
        :rtype: str
        """
        return self._csr_pem

    @csr_pem.setter
    def csr_pem(self, csr_pem):
        """
        Sets the csr_pem of this UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails.
        The certificate signing request (in PEM format).


        :param csr_pem: The csr_pem of this UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails.
        :type: str
        """
        self._csr_pem = csr_pem

    @property
    def validity(self):
        """
        Gets the validity of this UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails.

        :return: The validity of this UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails.
        :rtype: oci.certificates_management.models.Validity
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """
        Sets the validity of this UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails.

        :param validity: The validity of this UpdateCertificateManagedExternallyIssuedByInternalCaConfigDetails.
        :type: oci.certificates_management.models.Validity
        """
        self._validity = validity

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
