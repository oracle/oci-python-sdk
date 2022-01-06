# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkConfiguration(object):
    """
    Details of the network configuration.
    """

    #: A constant which can be used with the protocol property of a NetworkConfiguration.
    #: This constant has a value of "ICMP"
    PROTOCOL_ICMP = "ICMP"

    #: A constant which can be used with the protocol property of a NetworkConfiguration.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    #: A constant which can be used with the probe_mode property of a NetworkConfiguration.
    #: This constant has a value of "SACK"
    PROBE_MODE_SACK = "SACK"

    #: A constant which can be used with the probe_mode property of a NetworkConfiguration.
    #: This constant has a value of "SYN"
    PROBE_MODE_SYN = "SYN"

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param number_of_hops:
            The value to assign to the number_of_hops property of this NetworkConfiguration.
        :type number_of_hops: int

        :param probe_per_hop:
            The value to assign to the probe_per_hop property of this NetworkConfiguration.
        :type probe_per_hop: int

        :param transmission_rate:
            The value to assign to the transmission_rate property of this NetworkConfiguration.
        :type transmission_rate: int

        :param protocol:
            The value to assign to the protocol property of this NetworkConfiguration.
            Allowed values for this property are: "ICMP", "TCP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protocol: str

        :param probe_mode:
            The value to assign to the probe_mode property of this NetworkConfiguration.
            Allowed values for this property are: "SACK", "SYN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type probe_mode: str

        """
        self.swagger_types = {
            'number_of_hops': 'int',
            'probe_per_hop': 'int',
            'transmission_rate': 'int',
            'protocol': 'str',
            'probe_mode': 'str'
        }

        self.attribute_map = {
            'number_of_hops': 'numberOfHops',
            'probe_per_hop': 'probePerHop',
            'transmission_rate': 'transmissionRate',
            'protocol': 'protocol',
            'probe_mode': 'probeMode'
        }

        self._number_of_hops = None
        self._probe_per_hop = None
        self._transmission_rate = None
        self._protocol = None
        self._probe_mode = None

    @property
    def number_of_hops(self):
        """
        Gets the number_of_hops of this NetworkConfiguration.
        Number of hops.


        :return: The number_of_hops of this NetworkConfiguration.
        :rtype: int
        """
        return self._number_of_hops

    @number_of_hops.setter
    def number_of_hops(self, number_of_hops):
        """
        Sets the number_of_hops of this NetworkConfiguration.
        Number of hops.


        :param number_of_hops: The number_of_hops of this NetworkConfiguration.
        :type: int
        """
        self._number_of_hops = number_of_hops

    @property
    def probe_per_hop(self):
        """
        Gets the probe_per_hop of this NetworkConfiguration.
        Number of probes per hop.


        :return: The probe_per_hop of this NetworkConfiguration.
        :rtype: int
        """
        return self._probe_per_hop

    @probe_per_hop.setter
    def probe_per_hop(self, probe_per_hop):
        """
        Sets the probe_per_hop of this NetworkConfiguration.
        Number of probes per hop.


        :param probe_per_hop: The probe_per_hop of this NetworkConfiguration.
        :type: int
        """
        self._probe_per_hop = probe_per_hop

    @property
    def transmission_rate(self):
        """
        Gets the transmission_rate of this NetworkConfiguration.
        Number of probe packets sent out simultaneously.


        :return: The transmission_rate of this NetworkConfiguration.
        :rtype: int
        """
        return self._transmission_rate

    @transmission_rate.setter
    def transmission_rate(self, transmission_rate):
        """
        Sets the transmission_rate of this NetworkConfiguration.
        Number of probe packets sent out simultaneously.


        :param transmission_rate: The transmission_rate of this NetworkConfiguration.
        :type: int
        """
        self._transmission_rate = transmission_rate

    @property
    def protocol(self):
        """
        Gets the protocol of this NetworkConfiguration.
        Type of protocol.

        Allowed values for this property are: "ICMP", "TCP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protocol of this NetworkConfiguration.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this NetworkConfiguration.
        Type of protocol.


        :param protocol: The protocol of this NetworkConfiguration.
        :type: str
        """
        allowed_values = ["ICMP", "TCP"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            protocol = 'UNKNOWN_ENUM_VALUE'
        self._protocol = protocol

    @property
    def probe_mode(self):
        """
        Gets the probe_mode of this NetworkConfiguration.
        Type of probe mode when TCP protocol is selected.

        Allowed values for this property are: "SACK", "SYN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The probe_mode of this NetworkConfiguration.
        :rtype: str
        """
        return self._probe_mode

    @probe_mode.setter
    def probe_mode(self, probe_mode):
        """
        Sets the probe_mode of this NetworkConfiguration.
        Type of probe mode when TCP protocol is selected.


        :param probe_mode: The probe_mode of this NetworkConfiguration.
        :type: str
        """
        allowed_values = ["SACK", "SYN"]
        if not value_allowed_none_or_none_sentinel(probe_mode, allowed_values):
            probe_mode = 'UNKNOWN_ENUM_VALUE'
        self._probe_mode = probe_mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
