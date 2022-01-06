# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCertificateAuthorityDetails(object):
    """
    The details for updating a certificate authority (CA).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCertificateAuthorityDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateCertificateAuthorityDetails.
        :type description: str

        :param current_version_number:
            The value to assign to the current_version_number property of this UpdateCertificateAuthorityDetails.
        :type current_version_number: int

        :param certificate_authority_config:
            The value to assign to the certificate_authority_config property of this UpdateCertificateAuthorityDetails.
        :type certificate_authority_config: oci.certificates_management.models.UpdateCertificateAuthorityConfigDetails

        :param certificate_revocation_list_details:
            The value to assign to the certificate_revocation_list_details property of this UpdateCertificateAuthorityDetails.
        :type certificate_revocation_list_details: oci.certificates_management.models.CertificateRevocationListDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateCertificateAuthorityDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateCertificateAuthorityDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param certificate_authority_rules:
            The value to assign to the certificate_authority_rules property of this UpdateCertificateAuthorityDetails.
        :type certificate_authority_rules: list[oci.certificates_management.models.CertificateAuthorityRule]

        """
        self.swagger_types = {
            'description': 'str',
            'current_version_number': 'int',
            'certificate_authority_config': 'UpdateCertificateAuthorityConfigDetails',
            'certificate_revocation_list_details': 'CertificateRevocationListDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'certificate_authority_rules': 'list[CertificateAuthorityRule]'
        }

        self.attribute_map = {
            'description': 'description',
            'current_version_number': 'currentVersionNumber',
            'certificate_authority_config': 'certificateAuthorityConfig',
            'certificate_revocation_list_details': 'certificateRevocationListDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'certificate_authority_rules': 'certificateAuthorityRules'
        }

        self._description = None
        self._current_version_number = None
        self._certificate_authority_config = None
        self._certificate_revocation_list_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._certificate_authority_rules = None

    @property
    def description(self):
        """
        Gets the description of this UpdateCertificateAuthorityDetails.
        A brief description of the CA.


        :return: The description of this UpdateCertificateAuthorityDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateCertificateAuthorityDetails.
        A brief description of the CA.


        :param description: The description of this UpdateCertificateAuthorityDetails.
        :type: str
        """
        self._description = description

    @property
    def current_version_number(self):
        """
        Gets the current_version_number of this UpdateCertificateAuthorityDetails.
        Makes this version the current version. This property cannot be updated in combination with any other properties.


        :return: The current_version_number of this UpdateCertificateAuthorityDetails.
        :rtype: int
        """
        return self._current_version_number

    @current_version_number.setter
    def current_version_number(self, current_version_number):
        """
        Sets the current_version_number of this UpdateCertificateAuthorityDetails.
        Makes this version the current version. This property cannot be updated in combination with any other properties.


        :param current_version_number: The current_version_number of this UpdateCertificateAuthorityDetails.
        :type: int
        """
        self._current_version_number = current_version_number

    @property
    def certificate_authority_config(self):
        """
        Gets the certificate_authority_config of this UpdateCertificateAuthorityDetails.

        :return: The certificate_authority_config of this UpdateCertificateAuthorityDetails.
        :rtype: oci.certificates_management.models.UpdateCertificateAuthorityConfigDetails
        """
        return self._certificate_authority_config

    @certificate_authority_config.setter
    def certificate_authority_config(self, certificate_authority_config):
        """
        Sets the certificate_authority_config of this UpdateCertificateAuthorityDetails.

        :param certificate_authority_config: The certificate_authority_config of this UpdateCertificateAuthorityDetails.
        :type: oci.certificates_management.models.UpdateCertificateAuthorityConfigDetails
        """
        self._certificate_authority_config = certificate_authority_config

    @property
    def certificate_revocation_list_details(self):
        """
        Gets the certificate_revocation_list_details of this UpdateCertificateAuthorityDetails.

        :return: The certificate_revocation_list_details of this UpdateCertificateAuthorityDetails.
        :rtype: oci.certificates_management.models.CertificateRevocationListDetails
        """
        return self._certificate_revocation_list_details

    @certificate_revocation_list_details.setter
    def certificate_revocation_list_details(self, certificate_revocation_list_details):
        """
        Sets the certificate_revocation_list_details of this UpdateCertificateAuthorityDetails.

        :param certificate_revocation_list_details: The certificate_revocation_list_details of this UpdateCertificateAuthorityDetails.
        :type: oci.certificates_management.models.CertificateRevocationListDetails
        """
        self._certificate_revocation_list_details = certificate_revocation_list_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateCertificateAuthorityDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateCertificateAuthorityDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateCertificateAuthorityDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateCertificateAuthorityDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateCertificateAuthorityDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateCertificateAuthorityDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateCertificateAuthorityDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateCertificateAuthorityDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def certificate_authority_rules(self):
        """
        Gets the certificate_authority_rules of this UpdateCertificateAuthorityDetails.
        A list of rules that control how the CA is used and managed.


        :return: The certificate_authority_rules of this UpdateCertificateAuthorityDetails.
        :rtype: list[oci.certificates_management.models.CertificateAuthorityRule]
        """
        return self._certificate_authority_rules

    @certificate_authority_rules.setter
    def certificate_authority_rules(self, certificate_authority_rules):
        """
        Sets the certificate_authority_rules of this UpdateCertificateAuthorityDetails.
        A list of rules that control how the CA is used and managed.


        :param certificate_authority_rules: The certificate_authority_rules of this UpdateCertificateAuthorityDetails.
        :type: list[oci.certificates_management.models.CertificateAuthorityRule]
        """
        self._certificate_authority_rules = certificate_authority_rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
