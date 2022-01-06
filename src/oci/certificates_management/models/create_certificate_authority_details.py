# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCertificateAuthorityDetails(object):
    """
    The details for creating a certificate authority (CA).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCertificateAuthorityDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateCertificateAuthorityDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateCertificateAuthorityDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCertificateAuthorityDetails.
        :type compartment_id: str

        :param certificate_authority_rules:
            The value to assign to the certificate_authority_rules property of this CreateCertificateAuthorityDetails.
        :type certificate_authority_rules: list[oci.certificates_management.models.CertificateAuthorityRule]

        :param certificate_authority_config:
            The value to assign to the certificate_authority_config property of this CreateCertificateAuthorityDetails.
        :type certificate_authority_config: oci.certificates_management.models.CreateCertificateAuthorityConfigDetails

        :param certificate_revocation_list_details:
            The value to assign to the certificate_revocation_list_details property of this CreateCertificateAuthorityDetails.
        :type certificate_revocation_list_details: oci.certificates_management.models.CertificateRevocationListDetails

        :param kms_key_id:
            The value to assign to the kms_key_id property of this CreateCertificateAuthorityDetails.
        :type kms_key_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateCertificateAuthorityDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateCertificateAuthorityDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'certificate_authority_rules': 'list[CertificateAuthorityRule]',
            'certificate_authority_config': 'CreateCertificateAuthorityConfigDetails',
            'certificate_revocation_list_details': 'CertificateRevocationListDetails',
            'kms_key_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'certificate_authority_rules': 'certificateAuthorityRules',
            'certificate_authority_config': 'certificateAuthorityConfig',
            'certificate_revocation_list_details': 'certificateRevocationListDetails',
            'kms_key_id': 'kmsKeyId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._name = None
        self._description = None
        self._compartment_id = None
        self._certificate_authority_rules = None
        self._certificate_authority_config = None
        self._certificate_revocation_list_details = None
        self._kms_key_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateCertificateAuthorityDetails.
        A user-friendly name for the CA. Names are unique within a compartment. Avoid entering confidential information. Valid characters include uppercase or lowercase letters, numbers, hyphens, underscores, and periods.


        :return: The name of this CreateCertificateAuthorityDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateCertificateAuthorityDetails.
        A user-friendly name for the CA. Names are unique within a compartment. Avoid entering confidential information. Valid characters include uppercase or lowercase letters, numbers, hyphens, underscores, and periods.


        :param name: The name of this CreateCertificateAuthorityDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateCertificateAuthorityDetails.
        A brief description of the CA.


        :return: The description of this CreateCertificateAuthorityDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateCertificateAuthorityDetails.
        A brief description of the CA.


        :param description: The description of this CreateCertificateAuthorityDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateCertificateAuthorityDetails.
        The compartment in which you want to create the CA.


        :return: The compartment_id of this CreateCertificateAuthorityDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCertificateAuthorityDetails.
        The compartment in which you want to create the CA.


        :param compartment_id: The compartment_id of this CreateCertificateAuthorityDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def certificate_authority_rules(self):
        """
        Gets the certificate_authority_rules of this CreateCertificateAuthorityDetails.
        A list of rules that control how the CA is used and managed.


        :return: The certificate_authority_rules of this CreateCertificateAuthorityDetails.
        :rtype: list[oci.certificates_management.models.CertificateAuthorityRule]
        """
        return self._certificate_authority_rules

    @certificate_authority_rules.setter
    def certificate_authority_rules(self, certificate_authority_rules):
        """
        Sets the certificate_authority_rules of this CreateCertificateAuthorityDetails.
        A list of rules that control how the CA is used and managed.


        :param certificate_authority_rules: The certificate_authority_rules of this CreateCertificateAuthorityDetails.
        :type: list[oci.certificates_management.models.CertificateAuthorityRule]
        """
        self._certificate_authority_rules = certificate_authority_rules

    @property
    def certificate_authority_config(self):
        """
        **[Required]** Gets the certificate_authority_config of this CreateCertificateAuthorityDetails.

        :return: The certificate_authority_config of this CreateCertificateAuthorityDetails.
        :rtype: oci.certificates_management.models.CreateCertificateAuthorityConfigDetails
        """
        return self._certificate_authority_config

    @certificate_authority_config.setter
    def certificate_authority_config(self, certificate_authority_config):
        """
        Sets the certificate_authority_config of this CreateCertificateAuthorityDetails.

        :param certificate_authority_config: The certificate_authority_config of this CreateCertificateAuthorityDetails.
        :type: oci.certificates_management.models.CreateCertificateAuthorityConfigDetails
        """
        self._certificate_authority_config = certificate_authority_config

    @property
    def certificate_revocation_list_details(self):
        """
        Gets the certificate_revocation_list_details of this CreateCertificateAuthorityDetails.

        :return: The certificate_revocation_list_details of this CreateCertificateAuthorityDetails.
        :rtype: oci.certificates_management.models.CertificateRevocationListDetails
        """
        return self._certificate_revocation_list_details

    @certificate_revocation_list_details.setter
    def certificate_revocation_list_details(self, certificate_revocation_list_details):
        """
        Sets the certificate_revocation_list_details of this CreateCertificateAuthorityDetails.

        :param certificate_revocation_list_details: The certificate_revocation_list_details of this CreateCertificateAuthorityDetails.
        :type: oci.certificates_management.models.CertificateRevocationListDetails
        """
        self._certificate_revocation_list_details = certificate_revocation_list_details

    @property
    def kms_key_id(self):
        """
        **[Required]** Gets the kms_key_id of this CreateCertificateAuthorityDetails.
        The OCID of the Oracle Cloud Infrastructure Vault key used to encrypt the CA.


        :return: The kms_key_id of this CreateCertificateAuthorityDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this CreateCertificateAuthorityDetails.
        The OCID of the Oracle Cloud Infrastructure Vault key used to encrypt the CA.


        :param kms_key_id: The kms_key_id of this CreateCertificateAuthorityDetails.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateCertificateAuthorityDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateCertificateAuthorityDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateCertificateAuthorityDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateCertificateAuthorityDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateCertificateAuthorityDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateCertificateAuthorityDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateCertificateAuthorityDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateCertificateAuthorityDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
