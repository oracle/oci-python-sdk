# coding: utf-8
# Copyright (c) 2016 Oracle and/or its affiliates. All rights reserved.


from ..util import formatted_flat_dict


class UdpOptions(object):

    def __init__(self):

        self.swagger_types = {
            'destination_port_range': 'PortRange'
        }

        self.attribute_map = {
            'destination_port_range': 'destinationPortRange'
        }

        self._destination_port_range = None

    @property
    def destination_port_range(self):
        """
        Gets the destination_port_range of this UdpOptions.
        A single destination port or a range.

        :return: The destination_port_range of this UdpOptions.
        :rtype: PortRange
        """
        return self._destination_port_range

    @destination_port_range.setter
    def destination_port_range(self, destination_port_range):
        """
        Sets the destination_port_range of this UdpOptions.
        A single destination port or a range.

        :param destination_port_range: The destination_port_range of this UdpOptions.
        :type: PortRange
        """
        self._destination_port_range = destination_port_range

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
