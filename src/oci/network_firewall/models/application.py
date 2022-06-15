# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Application(object):
    """
    A protocol identifier (such as TCP, UDP, or ICMP)
    and protocol-specific parameters (such as a port range).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Application object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.network_firewall.models.IcmpApplication`
        * :class:`~oci.network_firewall.models.UdpApplication`
        * :class:`~oci.network_firewall.models.TcpApplication`
        * :class:`~oci.network_firewall.models.Icmp6Application`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this Application.
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'ICMP':
            return 'IcmpApplication'

        if type == 'UDP':
            return 'UdpApplication'

        if type == 'TCP':
            return 'TcpApplication'

        if type == 'ICMP6':
            return 'Icmp6Application'
        else:
            return 'Application'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Application.
        Describes the type of Application.


        :return: The type of this Application.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Application.
        Describes the type of Application.


        :param type: The type of this Application.
        :type: str
        """
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
