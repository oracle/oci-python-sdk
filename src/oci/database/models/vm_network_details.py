# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VmNetworkDetails(object):
    """
    Details of the client or backup networks in an Exadata VM cluster network. Applies to Exadata Cloud@Customer instances only.
    """

    #: A constant which can be used with the network_type property of a VmNetworkDetails.
    #: This constant has a value of "CLIENT"
    NETWORK_TYPE_CLIENT = "CLIENT"

    #: A constant which can be used with the network_type property of a VmNetworkDetails.
    #: This constant has a value of "BACKUP"
    NETWORK_TYPE_BACKUP = "BACKUP"

    def __init__(self, **kwargs):
        """
        Initializes a new VmNetworkDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vlan_id:
            The value to assign to the vlan_id property of this VmNetworkDetails.
        :type vlan_id: str

        :param network_type:
            The value to assign to the network_type property of this VmNetworkDetails.
            Allowed values for this property are: "CLIENT", "BACKUP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type network_type: str

        :param netmask:
            The value to assign to the netmask property of this VmNetworkDetails.
        :type netmask: str

        :param gateway:
            The value to assign to the gateway property of this VmNetworkDetails.
        :type gateway: str

        :param domain_name:
            The value to assign to the domain_name property of this VmNetworkDetails.
        :type domain_name: str

        :param nodes:
            The value to assign to the nodes property of this VmNetworkDetails.
        :type nodes: list[oci.database.models.NodeDetails]

        """
        self.swagger_types = {
            'vlan_id': 'str',
            'network_type': 'str',
            'netmask': 'str',
            'gateway': 'str',
            'domain_name': 'str',
            'nodes': 'list[NodeDetails]'
        }

        self.attribute_map = {
            'vlan_id': 'vlanId',
            'network_type': 'networkType',
            'netmask': 'netmask',
            'gateway': 'gateway',
            'domain_name': 'domainName',
            'nodes': 'nodes'
        }

        self._vlan_id = None
        self._network_type = None
        self._netmask = None
        self._gateway = None
        self._domain_name = None
        self._nodes = None

    @property
    def vlan_id(self):
        """
        **[Required]** Gets the vlan_id of this VmNetworkDetails.
        The network VLAN ID.


        :return: The vlan_id of this VmNetworkDetails.
        :rtype: str
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """
        Sets the vlan_id of this VmNetworkDetails.
        The network VLAN ID.


        :param vlan_id: The vlan_id of this VmNetworkDetails.
        :type: str
        """
        self._vlan_id = vlan_id

    @property
    def network_type(self):
        """
        **[Required]** Gets the network_type of this VmNetworkDetails.
        The network type.

        Allowed values for this property are: "CLIENT", "BACKUP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The network_type of this VmNetworkDetails.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """
        Sets the network_type of this VmNetworkDetails.
        The network type.


        :param network_type: The network_type of this VmNetworkDetails.
        :type: str
        """
        allowed_values = ["CLIENT", "BACKUP"]
        if not value_allowed_none_or_none_sentinel(network_type, allowed_values):
            network_type = 'UNKNOWN_ENUM_VALUE'
        self._network_type = network_type

    @property
    def netmask(self):
        """
        **[Required]** Gets the netmask of this VmNetworkDetails.
        The network netmask.


        :return: The netmask of this VmNetworkDetails.
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """
        Sets the netmask of this VmNetworkDetails.
        The network netmask.


        :param netmask: The netmask of this VmNetworkDetails.
        :type: str
        """
        self._netmask = netmask

    @property
    def gateway(self):
        """
        **[Required]** Gets the gateway of this VmNetworkDetails.
        The network gateway.


        :return: The gateway of this VmNetworkDetails.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """
        Sets the gateway of this VmNetworkDetails.
        The network gateway.


        :param gateway: The gateway of this VmNetworkDetails.
        :type: str
        """
        self._gateway = gateway

    @property
    def domain_name(self):
        """
        **[Required]** Gets the domain_name of this VmNetworkDetails.
        The network domain name.


        :return: The domain_name of this VmNetworkDetails.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """
        Sets the domain_name of this VmNetworkDetails.
        The network domain name.


        :param domain_name: The domain_name of this VmNetworkDetails.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def nodes(self):
        """
        **[Required]** Gets the nodes of this VmNetworkDetails.
        The list of node details.


        :return: The nodes of this VmNetworkDetails.
        :rtype: list[oci.database.models.NodeDetails]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """
        Sets the nodes of this VmNetworkDetails.
        The list of node details.


        :param nodes: The nodes of this VmNetworkDetails.
        :type: list[oci.database.models.NodeDetails]
        """
        self._nodes = nodes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
