# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateCrossConnectDetails(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'cross_connect_group_id': 'str',
            'display_name': 'str',
            'far_cross_connect_or_cross_connect_group_id': 'str',
            'location_name': 'str',
            'near_cross_connect_or_cross_connect_group_id': 'str',
            'port_speed_shape_name': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'cross_connect_group_id': 'crossConnectGroupId',
            'display_name': 'displayName',
            'far_cross_connect_or_cross_connect_group_id': 'farCrossConnectOrCrossConnectGroupId',
            'location_name': 'locationName',
            'near_cross_connect_or_cross_connect_group_id': 'nearCrossConnectOrCrossConnectGroupId',
            'port_speed_shape_name': 'portSpeedShapeName'
        }

        self._compartment_id = None
        self._cross_connect_group_id = None
        self._display_name = None
        self._far_cross_connect_or_cross_connect_group_id = None
        self._location_name = None
        self._near_cross_connect_or_cross_connect_group_id = None
        self._port_speed_shape_name = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateCrossConnectDetails.
        The OCID of the compartment to contain the cross-connect.


        :return: The compartment_id of this CreateCrossConnectDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCrossConnectDetails.
        The OCID of the compartment to contain the cross-connect.


        :param compartment_id: The compartment_id of this CreateCrossConnectDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cross_connect_group_id(self):
        """
        Gets the cross_connect_group_id of this CreateCrossConnectDetails.
        The OCID of the cross-connect group to put this cross-connect in.


        :return: The cross_connect_group_id of this CreateCrossConnectDetails.
        :rtype: str
        """
        return self._cross_connect_group_id

    @cross_connect_group_id.setter
    def cross_connect_group_id(self, cross_connect_group_id):
        """
        Sets the cross_connect_group_id of this CreateCrossConnectDetails.
        The OCID of the cross-connect group to put this cross-connect in.


        :param cross_connect_group_id: The cross_connect_group_id of this CreateCrossConnectDetails.
        :type: str
        """
        self._cross_connect_group_id = cross_connect_group_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateCrossConnectDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this CreateCrossConnectDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateCrossConnectDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this CreateCrossConnectDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def far_cross_connect_or_cross_connect_group_id(self):
        """
        Gets the far_cross_connect_or_cross_connect_group_id of this CreateCrossConnectDetails.
        If you already have an existing cross-connect or cross-connect group at this FastConnect
        location, and you want this new cross-connect to be on a different router (for the
        purposes of redundancy), provide the OCID of that existing cross-connect or
        cross-connect group.


        :return: The far_cross_connect_or_cross_connect_group_id of this CreateCrossConnectDetails.
        :rtype: str
        """
        return self._far_cross_connect_or_cross_connect_group_id

    @far_cross_connect_or_cross_connect_group_id.setter
    def far_cross_connect_or_cross_connect_group_id(self, far_cross_connect_or_cross_connect_group_id):
        """
        Sets the far_cross_connect_or_cross_connect_group_id of this CreateCrossConnectDetails.
        If you already have an existing cross-connect or cross-connect group at this FastConnect
        location, and you want this new cross-connect to be on a different router (for the
        purposes of redundancy), provide the OCID of that existing cross-connect or
        cross-connect group.


        :param far_cross_connect_or_cross_connect_group_id: The far_cross_connect_or_cross_connect_group_id of this CreateCrossConnectDetails.
        :type: str
        """
        self._far_cross_connect_or_cross_connect_group_id = far_cross_connect_or_cross_connect_group_id

    @property
    def location_name(self):
        """
        Gets the location_name of this CreateCrossConnectDetails.
        The name of the FastConnect location where this cross-connect will be installed.
        To get a list of the available locations, see
        :func:`list_cross_connect_locations`.

        Example: `CyrusOne, Chandler, AZ`


        :return: The location_name of this CreateCrossConnectDetails.
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """
        Sets the location_name of this CreateCrossConnectDetails.
        The name of the FastConnect location where this cross-connect will be installed.
        To get a list of the available locations, see
        :func:`list_cross_connect_locations`.

        Example: `CyrusOne, Chandler, AZ`


        :param location_name: The location_name of this CreateCrossConnectDetails.
        :type: str
        """
        self._location_name = location_name

    @property
    def near_cross_connect_or_cross_connect_group_id(self):
        """
        Gets the near_cross_connect_or_cross_connect_group_id of this CreateCrossConnectDetails.
        If you already have an existing cross-connect or cross-connect group at this FastConnect
        location, and you want this new cross-connect to be on the same router, provide the
        OCID of that existing cross-connect or cross-connect group.


        :return: The near_cross_connect_or_cross_connect_group_id of this CreateCrossConnectDetails.
        :rtype: str
        """
        return self._near_cross_connect_or_cross_connect_group_id

    @near_cross_connect_or_cross_connect_group_id.setter
    def near_cross_connect_or_cross_connect_group_id(self, near_cross_connect_or_cross_connect_group_id):
        """
        Sets the near_cross_connect_or_cross_connect_group_id of this CreateCrossConnectDetails.
        If you already have an existing cross-connect or cross-connect group at this FastConnect
        location, and you want this new cross-connect to be on the same router, provide the
        OCID of that existing cross-connect or cross-connect group.


        :param near_cross_connect_or_cross_connect_group_id: The near_cross_connect_or_cross_connect_group_id of this CreateCrossConnectDetails.
        :type: str
        """
        self._near_cross_connect_or_cross_connect_group_id = near_cross_connect_or_cross_connect_group_id

    @property
    def port_speed_shape_name(self):
        """
        Gets the port_speed_shape_name of this CreateCrossConnectDetails.
        The port speed for this cross-connect. To get a list of the available port speeds, see
        :func:`list_crossconnect_port_speed_shapes`.

        Example: `10 Gbps`


        :return: The port_speed_shape_name of this CreateCrossConnectDetails.
        :rtype: str
        """
        return self._port_speed_shape_name

    @port_speed_shape_name.setter
    def port_speed_shape_name(self, port_speed_shape_name):
        """
        Sets the port_speed_shape_name of this CreateCrossConnectDetails.
        The port speed for this cross-connect. To get a list of the available port speeds, see
        :func:`list_crossconnect_port_speed_shapes`.

        Example: `10 Gbps`


        :param port_speed_shape_name: The port_speed_shape_name of this CreateCrossConnectDetails.
        :type: str
        """
        self._port_speed_shape_name = port_speed_shape_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
