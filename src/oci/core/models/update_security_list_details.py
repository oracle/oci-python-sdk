# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSecurityListDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSecurityListDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateSecurityListDetails.
        :type display_name: str

        :param egress_security_rules:
            The value to assign to the egress_security_rules property of this UpdateSecurityListDetails.
        :type egress_security_rules: list[EgressSecurityRule]

        :param ingress_security_rules:
            The value to assign to the ingress_security_rules property of this UpdateSecurityListDetails.
        :type ingress_security_rules: list[IngressSecurityRule]

        """
        self.swagger_types = {
            'display_name': 'str',
            'egress_security_rules': 'list[EgressSecurityRule]',
            'ingress_security_rules': 'list[IngressSecurityRule]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'egress_security_rules': 'egressSecurityRules',
            'ingress_security_rules': 'ingressSecurityRules'
        }

        self._display_name = None
        self._egress_security_rules = None
        self._ingress_security_rules = None

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
        :rtype: list[EgressSecurityRule]
        """
        return self._egress_security_rules

    @egress_security_rules.setter
    def egress_security_rules(self, egress_security_rules):
        """
        Sets the egress_security_rules of this UpdateSecurityListDetails.
        Rules for allowing egress IP packets.


        :param egress_security_rules: The egress_security_rules of this UpdateSecurityListDetails.
        :type: list[EgressSecurityRule]
        """
        self._egress_security_rules = egress_security_rules

    @property
    def ingress_security_rules(self):
        """
        Gets the ingress_security_rules of this UpdateSecurityListDetails.
        Rules for allowing ingress IP packets.


        :return: The ingress_security_rules of this UpdateSecurityListDetails.
        :rtype: list[IngressSecurityRule]
        """
        return self._ingress_security_rules

    @ingress_security_rules.setter
    def ingress_security_rules(self, ingress_security_rules):
        """
        Sets the ingress_security_rules of this UpdateSecurityListDetails.
        Rules for allowing ingress IP packets.


        :param ingress_security_rules: The ingress_security_rules of this UpdateSecurityListDetails.
        :type: list[IngressSecurityRule]
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
