# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateSecurityListDetails(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'egress_security_rules': 'list[EgressSecurityRule]',
            'ingress_security_rules': 'list[IngressSecurityRule]',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'egress_security_rules': 'egressSecurityRules',
            'ingress_security_rules': 'ingressSecurityRules',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._display_name = None
        self._egress_security_rules = None
        self._ingress_security_rules = None
        self._vcn_id = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateSecurityListDetails.
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
    def display_name(self):
        """
        Gets the display_name of this CreateSecurityListDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this CreateSecurityListDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSecurityListDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this CreateSecurityListDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def egress_security_rules(self):
        """
        Gets the egress_security_rules of this CreateSecurityListDetails.
        Rules for allowing egress IP packets.


        :return: The egress_security_rules of this CreateSecurityListDetails.
        :rtype: list[EgressSecurityRule]
        """
        return self._egress_security_rules

    @egress_security_rules.setter
    def egress_security_rules(self, egress_security_rules):
        """
        Sets the egress_security_rules of this CreateSecurityListDetails.
        Rules for allowing egress IP packets.


        :param egress_security_rules: The egress_security_rules of this CreateSecurityListDetails.
        :type: list[EgressSecurityRule]
        """
        self._egress_security_rules = egress_security_rules

    @property
    def ingress_security_rules(self):
        """
        Gets the ingress_security_rules of this CreateSecurityListDetails.
        Rules for allowing ingress IP packets.


        :return: The ingress_security_rules of this CreateSecurityListDetails.
        :rtype: list[IngressSecurityRule]
        """
        return self._ingress_security_rules

    @ingress_security_rules.setter
    def ingress_security_rules(self, ingress_security_rules):
        """
        Sets the ingress_security_rules of this CreateSecurityListDetails.
        Rules for allowing ingress IP packets.


        :param ingress_security_rules: The ingress_security_rules of this CreateSecurityListDetails.
        :type: list[IngressSecurityRule]
        """
        self._ingress_security_rules = ingress_security_rules

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this CreateSecurityListDetails.
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
