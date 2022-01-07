# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCertificateDetails(object):
    """
    The details of the certificate to create.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCertificateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateCertificateDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateCertificateDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCertificateDetails.
        :type compartment_id: str

        :param certificate_rules:
            The value to assign to the certificate_rules property of this CreateCertificateDetails.
        :type certificate_rules: list[oci.certificates_management.models.CertificateRule]

        :param certificate_config:
            The value to assign to the certificate_config property of this CreateCertificateDetails.
        :type certificate_config: oci.certificates_management.models.CreateCertificateConfigDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateCertificateDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateCertificateDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'certificate_rules': 'list[CertificateRule]',
            'certificate_config': 'CreateCertificateConfigDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'certificate_rules': 'certificateRules',
            'certificate_config': 'certificateConfig',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._name = None
        self._description = None
        self._compartment_id = None
        self._certificate_rules = None
        self._certificate_config = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateCertificateDetails.
        A user-friendly name for the certificate. Names are unique within a compartment. Avoid entering confidential information. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.


        :return: The name of this CreateCertificateDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateCertificateDetails.
        A user-friendly name for the certificate. Names are unique within a compartment. Avoid entering confidential information. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.


        :param name: The name of this CreateCertificateDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateCertificateDetails.
        A brief description of the certificate. Avoid entering confidential information.


        :return: The description of this CreateCertificateDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateCertificateDetails.
        A brief description of the certificate. Avoid entering confidential information.


        :param description: The description of this CreateCertificateDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateCertificateDetails.
        The OCID of the compartment where you want to create the certificate.


        :return: The compartment_id of this CreateCertificateDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCertificateDetails.
        The OCID of the compartment where you want to create the certificate.


        :param compartment_id: The compartment_id of this CreateCertificateDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def certificate_rules(self):
        """
        Gets the certificate_rules of this CreateCertificateDetails.
        An optional list of rules that control how the certificate is used and managed.


        :return: The certificate_rules of this CreateCertificateDetails.
        :rtype: list[oci.certificates_management.models.CertificateRule]
        """
        return self._certificate_rules

    @certificate_rules.setter
    def certificate_rules(self, certificate_rules):
        """
        Sets the certificate_rules of this CreateCertificateDetails.
        An optional list of rules that control how the certificate is used and managed.


        :param certificate_rules: The certificate_rules of this CreateCertificateDetails.
        :type: list[oci.certificates_management.models.CertificateRule]
        """
        self._certificate_rules = certificate_rules

    @property
    def certificate_config(self):
        """
        **[Required]** Gets the certificate_config of this CreateCertificateDetails.

        :return: The certificate_config of this CreateCertificateDetails.
        :rtype: oci.certificates_management.models.CreateCertificateConfigDetails
        """
        return self._certificate_config

    @certificate_config.setter
    def certificate_config(self, certificate_config):
        """
        Sets the certificate_config of this CreateCertificateDetails.

        :param certificate_config: The certificate_config of this CreateCertificateDetails.
        :type: oci.certificates_management.models.CreateCertificateConfigDetails
        """
        self._certificate_config = certificate_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateCertificateDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateCertificateDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateCertificateDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateCertificateDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateCertificateDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateCertificateDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateCertificateDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateCertificateDetails.
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
