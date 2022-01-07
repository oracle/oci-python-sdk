# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_certificate_authority_config_details import UpdateCertificateAuthorityConfigDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSubordinateCaIssuedByInternalCaConfigDetails(UpdateCertificateAuthorityConfigDetails):
    """
    The details for updating a private subordinate certificate authority (CA) which is issued by a private CA.
    Note: This operation automatically rotates the private key.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSubordinateCaIssuedByInternalCaConfigDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.certificates_management.models.UpdateSubordinateCaIssuedByInternalCaConfigDetails.config_type` attribute
        of this class is ``SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_type:
            The value to assign to the config_type property of this UpdateSubordinateCaIssuedByInternalCaConfigDetails.
            Allowed values for this property are: "ROOT_CA_GENERATED_INTERNALLY", "SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA"
        :type config_type: str

        :param version_name:
            The value to assign to the version_name property of this UpdateSubordinateCaIssuedByInternalCaConfigDetails.
        :type version_name: str

        :param stage:
            The value to assign to the stage property of this UpdateSubordinateCaIssuedByInternalCaConfigDetails.
            Allowed values for this property are: "CURRENT", "PENDING"
        :type stage: str

        :param validity:
            The value to assign to the validity property of this UpdateSubordinateCaIssuedByInternalCaConfigDetails.
        :type validity: oci.certificates_management.models.Validity

        """
        self.swagger_types = {
            'config_type': 'str',
            'version_name': 'str',
            'stage': 'str',
            'validity': 'Validity'
        }

        self.attribute_map = {
            'config_type': 'configType',
            'version_name': 'versionName',
            'stage': 'stage',
            'validity': 'validity'
        }

        self._config_type = None
        self._version_name = None
        self._stage = None
        self._validity = None
        self._config_type = 'SUBORDINATE_CA_ISSUED_BY_INTERNAL_CA'

    @property
    def validity(self):
        """
        Gets the validity of this UpdateSubordinateCaIssuedByInternalCaConfigDetails.

        :return: The validity of this UpdateSubordinateCaIssuedByInternalCaConfigDetails.
        :rtype: oci.certificates_management.models.Validity
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """
        Sets the validity of this UpdateSubordinateCaIssuedByInternalCaConfigDetails.

        :param validity: The validity of this UpdateSubordinateCaIssuedByInternalCaConfigDetails.
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
