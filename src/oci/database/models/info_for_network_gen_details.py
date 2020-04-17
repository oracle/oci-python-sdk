# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InfoForNetworkGenDetails(object):
    """
    Parameters for generation of the client or backup network in a VM cluster network.
    """

    #: A constant which can be used with the network_type property of a InfoForNetworkGenDetails.
    #: This constant has a value of "CLIENT"
    NETWORK_TYPE_CLIENT = "CLIENT"

    #: A constant which can be used with the network_type property of a InfoForNetworkGenDetails.
    #: This constant has a value of "BACKUP"
    NETWORK_TYPE_BACKUP = "BACKUP"

    def __init__(self, **kwargs):
        """
        Initializes a new InfoForNetworkGenDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param network_type:
            The value to assign to the network_type property of this InfoForNetworkGenDetails.
            Allowed values for this property are: "CLIENT", "BACKUP"
        :type network_type: str

        :param vlan_id:
            The value to assign to the vlan_id property of this InfoForNetworkGenDetails.
        :type vlan_id: str

        :param cidr:
            The value to assign to the cidr property of this InfoForNetworkGenDetails.
        :type cidr: str

        :param gateway:
            The value to assign to the gateway property of this InfoForNetworkGenDetails.
        :type gateway: str

        :param netmask:
            The value to assign to the netmask property of this InfoForNetworkGenDetails.
        :type netmask: str

        :param domain:
            The value to assign to the domain property of this InfoForNetworkGenDetails.
        :type domain: str

        :param prefix:
            The value to assign to the prefix property of this InfoForNetworkGenDetails.
        :type prefix: str

        """
        self.swagger_types = {
            'network_type': 'str',
            'vlan_id': 'str',
            'cidr': 'str',
            'gateway': 'str',
            'netmask': 'str',
            'domain': 'str',
            'prefix': 'str'
        }

        self.attribute_map = {
            'network_type': 'networkType',
            'vlan_id': 'vlanId',
            'cidr': 'cidr',
            'gateway': 'gateway',
            'netmask': 'netmask',
            'domain': 'domain',
            'prefix': 'prefix'
        }

        self._network_type = None
        self._vlan_id = None
        self._cidr = None
        self._gateway = None
        self._netmask = None
        self._domain = None
        self._prefix = None

    @property
    def network_type(self):
        """
        **[Required]** Gets the network_type of this InfoForNetworkGenDetails.
        The network type.

        Allowed values for this property are: "CLIENT", "BACKUP"


        :return: The network_type of this InfoForNetworkGenDetails.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """
        Sets the network_type of this InfoForNetworkGenDetails.
        The network type.


        :param network_type: The network_type of this InfoForNetworkGenDetails.
        :type: str
        """
        allowed_values = ["CLIENT", "BACKUP"]
        if not value_allowed_none_or_none_sentinel(network_type, allowed_values):
            raise ValueError(
                "Invalid value for `network_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._network_type = network_type

    @property
    def vlan_id(self):
        """
        **[Required]** Gets the vlan_id of this InfoForNetworkGenDetails.
        The network VLAN ID.


        :return: The vlan_id of this InfoForNetworkGenDetails.
        :rtype: str
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """
        Sets the vlan_id of this InfoForNetworkGenDetails.
        The network VLAN ID.


        :param vlan_id: The vlan_id of this InfoForNetworkGenDetails.
        :type: str
        """
        self._vlan_id = vlan_id

    @property
    def cidr(self):
        """
        **[Required]** Gets the cidr of this InfoForNetworkGenDetails.
        The cidr for the network.


        :return: The cidr of this InfoForNetworkGenDetails.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """
        Sets the cidr of this InfoForNetworkGenDetails.
        The cidr for the network.


        :param cidr: The cidr of this InfoForNetworkGenDetails.
        :type: str
        """
        self._cidr = cidr

    @property
    def gateway(self):
        """
        **[Required]** Gets the gateway of this InfoForNetworkGenDetails.
        The network gateway.


        :return: The gateway of this InfoForNetworkGenDetails.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """
        Sets the gateway of this InfoForNetworkGenDetails.
        The network gateway.


        :param gateway: The gateway of this InfoForNetworkGenDetails.
        :type: str
        """
        self._gateway = gateway

    @property
    def netmask(self):
        """
        **[Required]** Gets the netmask of this InfoForNetworkGenDetails.
        The network netmask.


        :return: The netmask of this InfoForNetworkGenDetails.
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """
        Sets the netmask of this InfoForNetworkGenDetails.
        The network netmask.


        :param netmask: The netmask of this InfoForNetworkGenDetails.
        :type: str
        """
        self._netmask = netmask

    @property
    def domain(self):
        """
        **[Required]** Gets the domain of this InfoForNetworkGenDetails.
        The network domain name.


        :return: The domain of this InfoForNetworkGenDetails.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this InfoForNetworkGenDetails.
        The network domain name.


        :param domain: The domain of this InfoForNetworkGenDetails.
        :type: str
        """
        self._domain = domain

    @property
    def prefix(self):
        """
        **[Required]** Gets the prefix of this InfoForNetworkGenDetails.
        The network domain name.


        :return: The prefix of this InfoForNetworkGenDetails.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this InfoForNetworkGenDetails.
        The network domain name.


        :param prefix: The prefix of this InfoForNetworkGenDetails.
        :type: str
        """
        self._prefix = prefix

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
