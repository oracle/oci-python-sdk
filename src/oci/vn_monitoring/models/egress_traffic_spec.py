# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EgressTrafficSpec(object):
    """
    Defines the traffic configuration that leaves the traffic node.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EgressTrafficSpec object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param protocol:
            The value to assign to the protocol property of this EgressTrafficSpec.
        :type protocol: int

        :param source_address:
            The value to assign to the source_address property of this EgressTrafficSpec.
        :type source_address: str

        :param destination_address:
            The value to assign to the destination_address property of this EgressTrafficSpec.
        :type destination_address: str

        :param traffic_protocol_parameters:
            The value to assign to the traffic_protocol_parameters property of this EgressTrafficSpec.
        :type traffic_protocol_parameters: oci.vn_monitoring.models.TrafficProtocolParameters

        """
        self.swagger_types = {
            'protocol': 'int',
            'source_address': 'str',
            'destination_address': 'str',
            'traffic_protocol_parameters': 'TrafficProtocolParameters'
        }

        self.attribute_map = {
            'protocol': 'protocol',
            'source_address': 'sourceAddress',
            'destination_address': 'destinationAddress',
            'traffic_protocol_parameters': 'trafficProtocolParameters'
        }

        self._protocol = None
        self._source_address = None
        self._destination_address = None
        self._traffic_protocol_parameters = None

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this EgressTrafficSpec.
        The IP protocol to use for the traffic path analysis.


        :return: The protocol of this EgressTrafficSpec.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this EgressTrafficSpec.
        The IP protocol to use for the traffic path analysis.


        :param protocol: The protocol of this EgressTrafficSpec.
        :type: int
        """
        self._protocol = protocol

    @property
    def source_address(self):
        """
        **[Required]** Gets the source_address of this EgressTrafficSpec.
        The IPv4 address of the source node.


        :return: The source_address of this EgressTrafficSpec.
        :rtype: str
        """
        return self._source_address

    @source_address.setter
    def source_address(self, source_address):
        """
        Sets the source_address of this EgressTrafficSpec.
        The IPv4 address of the source node.


        :param source_address: The source_address of this EgressTrafficSpec.
        :type: str
        """
        self._source_address = source_address

    @property
    def destination_address(self):
        """
        **[Required]** Gets the destination_address of this EgressTrafficSpec.
        The IPv4 address of the destination node.


        :return: The destination_address of this EgressTrafficSpec.
        :rtype: str
        """
        return self._destination_address

    @destination_address.setter
    def destination_address(self, destination_address):
        """
        Sets the destination_address of this EgressTrafficSpec.
        The IPv4 address of the destination node.


        :param destination_address: The destination_address of this EgressTrafficSpec.
        :type: str
        """
        self._destination_address = destination_address

    @property
    def traffic_protocol_parameters(self):
        """
        Gets the traffic_protocol_parameters of this EgressTrafficSpec.

        :return: The traffic_protocol_parameters of this EgressTrafficSpec.
        :rtype: oci.vn_monitoring.models.TrafficProtocolParameters
        """
        return self._traffic_protocol_parameters

    @traffic_protocol_parameters.setter
    def traffic_protocol_parameters(self, traffic_protocol_parameters):
        """
        Sets the traffic_protocol_parameters of this EgressTrafficSpec.

        :param traffic_protocol_parameters: The traffic_protocol_parameters of this EgressTrafficSpec.
        :type: oci.vn_monitoring.models.TrafficProtocolParameters
        """
        self._traffic_protocol_parameters = traffic_protocol_parameters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
