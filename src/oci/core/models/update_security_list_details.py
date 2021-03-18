# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSecurityListDetails(object):
    """
    UpdateSecurityListDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSecurityListDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateSecurityListDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateSecurityListDetails.
        :type display_name: str

        :param egress_security_rules:
            The value to assign to the egress_security_rules property of this UpdateSecurityListDetails.
        :type egress_security_rules: list[oci.core.models.EgressSecurityRule]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateSecurityListDetails.
        :type freeform_tags: dict(str, str)

        :param ingress_security_rules:
            The value to assign to the ingress_security_rules property of this UpdateSecurityListDetails.
        :type ingress_security_rules: list[oci.core.models.IngressSecurityRule]

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'egress_security_rules': 'list[EgressSecurityRule]',
            'freeform_tags': 'dict(str, str)',
            'ingress_security_rules': 'list[IngressSecurityRule]'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'egress_security_rules': 'egressSecurityRules',
            'freeform_tags': 'freeformTags',
            'ingress_security_rules': 'ingressSecurityRules'
        }

        self._defined_tags = None
        self._display_name = None
        self._egress_security_rules = None
        self._freeform_tags = None
        self._ingress_security_rules = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateSecurityListDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateSecurityListDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateSecurityListDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateSecurityListDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateSecurityListDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateSecurityListDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateSecurityListDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateSecurityListDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def egress_security_rules(self):
        """
        Gets the egress_security_rules of this UpdateSecurityListDetails.
        Rules for allowing egress IP packets.


        :return: The egress_security_rules of this UpdateSecurityListDetails.
        :rtype: list[oci.core.models.EgressSecurityRule]
        """
        return self._egress_security_rules

    @egress_security_rules.setter
    def egress_security_rules(self, egress_security_rules):
        """
        Sets the egress_security_rules of this UpdateSecurityListDetails.
        Rules for allowing egress IP packets.


        :param egress_security_rules: The egress_security_rules of this UpdateSecurityListDetails.
        :type: list[oci.core.models.EgressSecurityRule]
        """
        self._egress_security_rules = egress_security_rules

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateSecurityListDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateSecurityListDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateSecurityListDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateSecurityListDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def ingress_security_rules(self):
        """
        Gets the ingress_security_rules of this UpdateSecurityListDetails.
        Rules for allowing ingress IP packets.


        :return: The ingress_security_rules of this UpdateSecurityListDetails.
        :rtype: list[oci.core.models.IngressSecurityRule]
        """
        return self._ingress_security_rules

    @ingress_security_rules.setter
    def ingress_security_rules(self, ingress_security_rules):
        """
        Sets the ingress_security_rules of this UpdateSecurityListDetails.
        Rules for allowing ingress IP packets.


        :param ingress_security_rules: The ingress_security_rules of this UpdateSecurityListDetails.
        :type: list[oci.core.models.IngressSecurityRule]
        """
        self._ingress_security_rules = ingress_security_rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
