# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class DhcpOptions(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'options': 'list[DhcpOption]',
            'time_created': 'datetime',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'options': 'options',
            'time_created': 'timeCreated',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._lifecycle_state = None
        self._options = None
        self._time_created = None
        self._vcn_id = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this DhcpOptions.
        The OCID of the compartment containing the set of DHCP options.


        :return: The compartment_id of this DhcpOptions.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DhcpOptions.
        The OCID of the compartment containing the set of DHCP options.


        :param compartment_id: The compartment_id of this DhcpOptions.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this DhcpOptions.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this DhcpOptions.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DhcpOptions.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this DhcpOptions.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this DhcpOptions.
        Oracle ID (OCID) for the set of DHCP options.


        :return: The id of this DhcpOptions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DhcpOptions.
        Oracle ID (OCID) for the set of DHCP options.


        :param id: The id of this DhcpOptions.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DhcpOptions.
        The current state of the set of DHCP options.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DhcpOptions.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DhcpOptions.
        The current state of the set of DHCP options.


        :param lifecycle_state: The lifecycle_state of this DhcpOptions.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def options(self):
        """
        Gets the options of this DhcpOptions.
        The collection of individual DHCP options.


        :return: The options of this DhcpOptions.
        :rtype: list[DhcpOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this DhcpOptions.
        The collection of individual DHCP options.


        :param options: The options of this DhcpOptions.
        :type: list[DhcpOption]
        """
        self._options = options

    @property
    def time_created(self):
        """
        Gets the time_created of this DhcpOptions.
        Date and time the set of DHCP options was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this DhcpOptions.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DhcpOptions.
        Date and time the set of DHCP options was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this DhcpOptions.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this DhcpOptions.
        The OCID of the VCN the set of DHCP options belongs to.


        :return: The vcn_id of this DhcpOptions.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this DhcpOptions.
        The OCID of the VCN the set of DHCP options belongs to.


        :param vcn_id: The vcn_id of this DhcpOptions.
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
