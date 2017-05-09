# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CrossConnect(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'cross_connect_group_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'location_name': 'str',
            'port_name': 'str',
            'port_speed_shape_name': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'cross_connect_group_id': 'crossConnectGroupId',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'location_name': 'locationName',
            'port_name': 'portName',
            'port_speed_shape_name': 'portSpeedShapeName',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._cross_connect_group_id = None
        self._display_name = None
        self._id = None
        self._lifecycle_state = None
        self._location_name = None
        self._port_name = None
        self._port_speed_shape_name = None
        self._time_created = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CrossConnect.
        The OCID of the compartment containing the cross-connect group.


        :return: The compartment_id of this CrossConnect.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CrossConnect.
        The OCID of the compartment containing the cross-connect group.


        :param compartment_id: The compartment_id of this CrossConnect.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cross_connect_group_id(self):
        """
        Gets the cross_connect_group_id of this CrossConnect.
        The OCID of the cross-connect group this cross-connect belongs to (if any).


        :return: The cross_connect_group_id of this CrossConnect.
        :rtype: str
        """
        return self._cross_connect_group_id

    @cross_connect_group_id.setter
    def cross_connect_group_id(self, cross_connect_group_id):
        """
        Sets the cross_connect_group_id of this CrossConnect.
        The OCID of the cross-connect group this cross-connect belongs to (if any).


        :param cross_connect_group_id: The cross_connect_group_id of this CrossConnect.
        :type: str
        """
        self._cross_connect_group_id = cross_connect_group_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CrossConnect.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this CrossConnect.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CrossConnect.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this CrossConnect.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this CrossConnect.
        The cross-connect's Oracle ID (OCID).


        :return: The id of this CrossConnect.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CrossConnect.
        The cross-connect's Oracle ID (OCID).


        :param id: The id of this CrossConnect.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this CrossConnect.
        The cross-connect's current state.

        Allowed values for this property are: "PENDING_CUSTOMER", "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this CrossConnect.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CrossConnect.
        The cross-connect's current state.


        :param lifecycle_state: The lifecycle_state of this CrossConnect.
        :type: str
        """
        allowed_values = ["PENDING_CUSTOMER", "PROVISIONING", "PROVISIONED", "INACTIVE", "TERMINATING", "TERMINATED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def location_name(self):
        """
        Gets the location_name of this CrossConnect.
        The name of the FastConnect location where this cross-connect is installed.


        :return: The location_name of this CrossConnect.
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """
        Sets the location_name of this CrossConnect.
        The name of the FastConnect location where this cross-connect is installed.


        :param location_name: The location_name of this CrossConnect.
        :type: str
        """
        self._location_name = location_name

    @property
    def port_name(self):
        """
        Gets the port_name of this CrossConnect.
        A string identifying the meet-me room port for this cross-connect.


        :return: The port_name of this CrossConnect.
        :rtype: str
        """
        return self._port_name

    @port_name.setter
    def port_name(self, port_name):
        """
        Sets the port_name of this CrossConnect.
        A string identifying the meet-me room port for this cross-connect.


        :param port_name: The port_name of this CrossConnect.
        :type: str
        """
        self._port_name = port_name

    @property
    def port_speed_shape_name(self):
        """
        Gets the port_speed_shape_name of this CrossConnect.
        The port speed for this cross-connect.

        Example: `10 Gbps`


        :return: The port_speed_shape_name of this CrossConnect.
        :rtype: str
        """
        return self._port_speed_shape_name

    @port_speed_shape_name.setter
    def port_speed_shape_name(self, port_speed_shape_name):
        """
        Sets the port_speed_shape_name of this CrossConnect.
        The port speed for this cross-connect.

        Example: `10 Gbps`


        :param port_speed_shape_name: The port_speed_shape_name of this CrossConnect.
        :type: str
        """
        self._port_speed_shape_name = port_speed_shape_name

    @property
    def time_created(self):
        """
        Gets the time_created of this CrossConnect.
        The date and time the cross-connect was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this CrossConnect.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CrossConnect.
        The date and time the cross-connect was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this CrossConnect.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
