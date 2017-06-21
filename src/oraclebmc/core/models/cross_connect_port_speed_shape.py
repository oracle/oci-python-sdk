# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CrossConnectPortSpeedShape(object):

    def __init__(self):

        self.swagger_types = {
            'name': 'str',
            'port_speed_in_gbps': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'port_speed_in_gbps': 'portSpeedInGbps'
        }

        self._name = None
        self._port_speed_in_gbps = None

    @property
    def name(self):
        """
        Gets the name of this CrossConnectPortSpeedShape.
        The name of the port speed shape.

        Example: `10 Gbps`


        :return: The name of this CrossConnectPortSpeedShape.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CrossConnectPortSpeedShape.
        The name of the port speed shape.

        Example: `10 Gbps`


        :param name: The name of this CrossConnectPortSpeedShape.
        :type: str
        """
        self._name = name

    @property
    def port_speed_in_gbps(self):
        """
        Gets the port_speed_in_gbps of this CrossConnectPortSpeedShape.
        The port speed in Gbps.

        Example: `10`


        :return: The port_speed_in_gbps of this CrossConnectPortSpeedShape.
        :rtype: int
        """
        return self._port_speed_in_gbps

    @port_speed_in_gbps.setter
    def port_speed_in_gbps(self, port_speed_in_gbps):
        """
        Sets the port_speed_in_gbps of this CrossConnectPortSpeedShape.
        The port speed in Gbps.

        Example: `10`


        :param port_speed_in_gbps: The port_speed_in_gbps of this CrossConnectPortSpeedShape.
        :type: int
        """
        self._port_speed_in_gbps = port_speed_in_gbps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
