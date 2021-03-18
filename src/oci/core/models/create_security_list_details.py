# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSecurityListDetails(object):
    """
    CreateSecurityListDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSecurityListDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSecurityListDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSecurityListDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateSecurityListDetails.
        :type display_name: str

        :param egress_security_rules:
            The value to assign to the egress_security_rules property of this CreateSecurityListDetails.
        :type egress_security_rules: list[oci.core.models.EgressSecurityRule]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSecurityListDetails.
        :type freeform_tags: dict(str, str)

        :param ingress_security_rules:
            The value to assign to the ingress_security_rules property of this CreateSecurityListDetails.
        :type ingress_security_rules: list[oci.core.models.IngressSecurityRule]

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateSecurityListDetails.
        :type vcn_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'egress_security_rules': 'list[EgressSecurityRule]',
            'freeform_tags': 'dict(str, str)',
            'ingress_security_rules': 'list[IngressSecurityRule]',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'egress_security_rules': 'egressSecurityRules',
            'freeform_tags': 'freeformTags',
            'ingress_security_rules': 'ingressSecurityRules',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._egress_security_rules = None
        self._freeform_tags = None
        self._ingress_security_rules = None
        self._vcn_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateSecurityListDetails.
        The OCID of the compartment to contain the security list.


        :return: The compartment_id of this CreateSecurityListDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSecurityListDetails.
        The OCID of the compartment to contain the security list.


        :param compartment_id: The compartment_id of this CreateSecurityListDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateSecurityListDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateSecurityListDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateSecurityListDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateSecurityListDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateSecurityListDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateSecurityListDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSecurityListDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateSecurityListDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def egress_security_rules(self):
        """
        **[Required]** Gets the egress_security_rules of this CreateSecurityListDetails.
        Rules for allowing egress IP packets.


        :return: The egress_security_rules of this CreateSecurityListDetails.
        :rtype: list[oci.core.models.EgressSecurityRule]
        """
        return self._egress_security_rules

    @egress_security_rules.setter
    def egress_security_rules(self, egress_security_rules):
        """
        Sets the egress_security_rules of this CreateSecurityListDetails.
        Rules for allowing egress IP packets.


        :param egress_security_rules: The egress_security_rules of this CreateSecurityListDetails.
        :type: list[oci.core.models.EgressSecurityRule]
        """
        self._egress_security_rules = egress_security_rules

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateSecurityListDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateSecurityListDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateSecurityListDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateSecurityListDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def ingress_security_rules(self):
        """
        **[Required]** Gets the ingress_security_rules of this CreateSecurityListDetails.
        Rules for allowing ingress IP packets.


        :return: The ingress_security_rules of this CreateSecurityListDetails.
        :rtype: list[oci.core.models.IngressSecurityRule]
        """
        return self._ingress_security_rules

    @ingress_security_rules.setter
    def ingress_security_rules(self, ingress_security_rules):
        """
        Sets the ingress_security_rules of this CreateSecurityListDetails.
        Rules for allowing ingress IP packets.


        :param ingress_security_rules: The ingress_security_rules of this CreateSecurityListDetails.
        :type: list[oci.core.models.IngressSecurityRule]
        """
        self._ingress_security_rules = ingress_security_rules

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this CreateSecurityListDetails.
        The OCID of the VCN the security list belongs to.


        :return: The vcn_id of this CreateSecurityListDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateSecurityListDetails.
        The OCID of the VCN the security list belongs to.


        :param vcn_id: The vcn_id of this CreateSecurityListDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
