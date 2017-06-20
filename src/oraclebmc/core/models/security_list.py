# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class SecurityList(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'egress_security_rules': 'list[EgressSecurityRule]',
            'id': 'str',
            'ingress_security_rules': 'list[IngressSecurityRule]',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'egress_security_rules': 'egressSecurityRules',
            'id': 'id',
            'ingress_security_rules': 'ingressSecurityRules',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._display_name = None
        self._egress_security_rules = None
        self._id = None
        self._ingress_security_rules = None
        self._lifecycle_state = None
        self._time_created = None
        self._vcn_id = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this SecurityList.
        The OCID of the compartment containing the security list.


        :return: The compartment_id of this SecurityList.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SecurityList.
        The OCID of the compartment containing the security list.


        :param compartment_id: The compartment_id of this SecurityList.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this SecurityList.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this SecurityList.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SecurityList.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this SecurityList.
        :type: str
        """
        self._display_name = display_name

    @property
    def egress_security_rules(self):
        """
        Gets the egress_security_rules of this SecurityList.
        Rules for allowing egress IP packets.


        :return: The egress_security_rules of this SecurityList.
        :rtype: list[EgressSecurityRule]
        """
        return self._egress_security_rules

    @egress_security_rules.setter
    def egress_security_rules(self, egress_security_rules):
        """
        Sets the egress_security_rules of this SecurityList.
        Rules for allowing egress IP packets.


        :param egress_security_rules: The egress_security_rules of this SecurityList.
        :type: list[EgressSecurityRule]
        """
        self._egress_security_rules = egress_security_rules

    @property
    def id(self):
        """
        Gets the id of this SecurityList.
        The security list's Oracle Cloud ID (OCID).


        :return: The id of this SecurityList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SecurityList.
        The security list's Oracle Cloud ID (OCID).


        :param id: The id of this SecurityList.
        :type: str
        """
        self._id = id

    @property
    def ingress_security_rules(self):
        """
        Gets the ingress_security_rules of this SecurityList.
        Rules for allowing ingress IP packets.


        :return: The ingress_security_rules of this SecurityList.
        :rtype: list[IngressSecurityRule]
        """
        return self._ingress_security_rules

    @ingress_security_rules.setter
    def ingress_security_rules(self, ingress_security_rules):
        """
        Sets the ingress_security_rules of this SecurityList.
        Rules for allowing ingress IP packets.


        :param ingress_security_rules: The ingress_security_rules of this SecurityList.
        :type: list[IngressSecurityRule]
        """
        self._ingress_security_rules = ingress_security_rules

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SecurityList.
        The security list's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SecurityList.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SecurityList.
        The security list's current state.


        :param lifecycle_state: The lifecycle_state of this SecurityList.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this SecurityList.
        The date and time the security list was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this SecurityList.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SecurityList.
        The date and time the security list was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this SecurityList.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this SecurityList.
        The OCID of the VCN the security list belongs to.


        :return: The vcn_id of this SecurityList.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this SecurityList.
        The OCID of the VCN the security list belongs to.


        :param vcn_id: The vcn_id of this SecurityList.
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
