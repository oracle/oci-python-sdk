# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UdpOptions(object):
    """
    Optional and valid only for UDP. Use to specify particular destination ports for UDP rules.
    If you specify UDP as the protocol but omit this object, then all destination ports are allowed.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UdpOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param destination_port_range:
            The value to assign to the destination_port_range property of this UdpOptions.
        :type destination_port_range: oci.core.models.PortRange

        :param source_port_range:
            The value to assign to the source_port_range property of this UdpOptions.
        :type source_port_range: oci.core.models.PortRange

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
        Gets the destination_port_range of this UdpOptions.

        :return: The destination_port_range of this UdpOptions.
        :rtype: oci.core.models.PortRange
        """
        return self._destination_port_range

    @destination_port_range.setter
    def destination_port_range(self, destination_port_range):
        """
        Sets the destination_port_range of this UdpOptions.

        :param destination_port_range: The destination_port_range of this UdpOptions.
        :type: oci.core.models.PortRange
        """
        self._destination_port_range = destination_port_range

    @property
    def source_port_range(self):
        """
        Gets the source_port_range of this UdpOptions.

        :return: The source_port_range of this UdpOptions.
        :rtype: oci.core.models.PortRange
        """
        return self._source_port_range

    @source_port_range.setter
    def source_port_range(self, source_port_range):
        """
        Sets the source_port_range of this UdpOptions.

        :param source_port_range: The source_port_range of this UdpOptions.
        :type: oci.core.models.PortRange
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
