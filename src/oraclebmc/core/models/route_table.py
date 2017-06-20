# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class RouteTable(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'route_rules': 'list[RouteRule]',
            'time_created': 'datetime',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'route_rules': 'routeRules',
            'time_created': 'timeCreated',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._lifecycle_state = None
        self._route_rules = None
        self._time_created = None
        self._vcn_id = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this RouteTable.
        The OCID of the compartment containing the route table.


        :return: The compartment_id of this RouteTable.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RouteTable.
        The OCID of the compartment containing the route table.


        :param compartment_id: The compartment_id of this RouteTable.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this RouteTable.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this RouteTable.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RouteTable.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this RouteTable.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this RouteTable.
        The route table's Oracle ID (OCID).


        :return: The id of this RouteTable.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RouteTable.
        The route table's Oracle ID (OCID).


        :param id: The id of this RouteTable.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this RouteTable.
        The route table's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this RouteTable.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RouteTable.
        The route table's current state.


        :param lifecycle_state: The lifecycle_state of this RouteTable.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def route_rules(self):
        """
        Gets the route_rules of this RouteTable.
        The collection of rules for routing destination IPs to network devices.


        :return: The route_rules of this RouteTable.
        :rtype: list[RouteRule]
        """
        return self._route_rules

    @route_rules.setter
    def route_rules(self, route_rules):
        """
        Sets the route_rules of this RouteTable.
        The collection of rules for routing destination IPs to network devices.


        :param route_rules: The route_rules of this RouteTable.
        :type: list[RouteRule]
        """
        self._route_rules = route_rules

    @property
    def time_created(self):
        """
        Gets the time_created of this RouteTable.
        The date and time the route table was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this RouteTable.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RouteTable.
        The date and time the route table was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this RouteTable.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this RouteTable.
        The OCID of the VCN the route table list belongs to.


        :return: The vcn_id of this RouteTable.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this RouteTable.
        The OCID of the VCN the route table list belongs to.


        :param vcn_id: The vcn_id of this RouteTable.
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
