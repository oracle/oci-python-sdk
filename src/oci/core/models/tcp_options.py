# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TcpOptions(object):
    """
    Optional object to specify ports for a TCP rule. If you specify TCP as the
    protocol but omit this object, then all ports are allowed.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TcpOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param destination_port_range:
            The value to assign to the destination_port_range property of this TcpOptions.
        :type destination_port_range: PortRange

        :param source_port_range:
            The value to assign to the source_port_range property of this TcpOptions.
        :type source_port_range: PortRange

        """
        self.swagger_types = {
            'destination_port_range': 'PortRange',
            'source_port_range': 'PortRange'
        }

        self.attribute_map = {
            'destination_port_range': 'destinationPortRange',
            'source_port_range': 'sourcePortRange'
        }

        self._destination_port_range = None
        self._source_port_range = None

    @property
    def destination_port_range(self):
        """
        Gets the destination_port_range of this TcpOptions.
        An inclusive range of allowed destination ports. Use the same number for the min and max
        to indicate a single port. Defaults to all ports if not specified.


        :return: The destination_port_range of this TcpOptions.
        :rtype: PortRange
        """
        return self._destination_port_range

    @destination_port_range.setter
    def destination_port_range(self, destination_port_range):
        """
        Sets the destination_port_range of this TcpOptions.
        An inclusive range of allowed destination ports. Use the same number for the min and max
        to indicate a single port. Defaults to all ports if not specified.


        :param destination_port_range: The destination_port_range of this TcpOptions.
        :type: PortRange
        """
        self._destination_port_range = destination_port_range

    @property
    def source_port_range(self):
        """
        Gets the source_port_range of this TcpOptions.
        An inclusive range of allowed source ports. Use the same number for the min and max to
        indicate a single port. Defaults to all ports if not specified.


        :return: The source_port_range of this TcpOptions.
        :rtype: PortRange
        """
        return self._source_port_range

    @source_port_range.setter
    def source_port_range(self, source_port_range):
        """
        Sets the source_port_range of this TcpOptions.
        An inclusive range of allowed source ports. Use the same number for the min and max to
        indicate a single port. Defaults to all ports if not specified.


        :param source_port_range: The source_port_range of this TcpOptions.
        :type: PortRange
        """
        self._source_port_range = source_port_range

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
