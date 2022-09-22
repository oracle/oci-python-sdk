# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResizeVmClusterNetworkDetails(object):
    """
    Details of Db server network nodes to extend or shrink the VM cluster network. Applies to Exadata Cloud@Customer
    instances only.
    """

    #: A constant which can be used with the action property of a ResizeVmClusterNetworkDetails.
    #: This constant has a value of "ADD_DBSERVER_NETWORK"
    ACTION_ADD_DBSERVER_NETWORK = "ADD_DBSERVER_NETWORK"

    #: A constant which can be used with the action property of a ResizeVmClusterNetworkDetails.
    #: This constant has a value of "REMOVE_DBSERVER_NETWORK"
    ACTION_REMOVE_DBSERVER_NETWORK = "REMOVE_DBSERVER_NETWORK"

    def __init__(self, **kwargs):
        """
        Initializes a new ResizeVmClusterNetworkDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this ResizeVmClusterNetworkDetails.
            Allowed values for this property are: "ADD_DBSERVER_NETWORK", "REMOVE_DBSERVER_NETWORK"
        :type action: str

        :param vm_networks:
            The value to assign to the vm_networks property of this ResizeVmClusterNetworkDetails.
        :type vm_networks: list[oci.database.models.VmNetworkDetails]

        """
        self.swagger_types = {
            'action': 'str',
            'vm_networks': 'list[VmNetworkDetails]'
        }

        self.attribute_map = {
            'action': 'action',
            'vm_networks': 'vmNetworks'
        }

        self._action = None
        self._vm_networks = None

    @property
    def action(self):
        """
        **[Required]** Gets the action of this ResizeVmClusterNetworkDetails.
        Actions that can be performed on the VM cluster network.
        ADD_DBSERVER_NETWORK - Provide Db server network details of network nodes to be added to the VM cluster network.
        REMOVE_DBSERVER_NETWORK - Provide Db server network details of network nodes to be removed from the VM cluster network.

        Allowed values for this property are: "ADD_DBSERVER_NETWORK", "REMOVE_DBSERVER_NETWORK"


        :return: The action of this ResizeVmClusterNetworkDetails.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ResizeVmClusterNetworkDetails.
        Actions that can be performed on the VM cluster network.
        ADD_DBSERVER_NETWORK - Provide Db server network details of network nodes to be added to the VM cluster network.
        REMOVE_DBSERVER_NETWORK - Provide Db server network details of network nodes to be removed from the VM cluster network.


        :param action: The action of this ResizeVmClusterNetworkDetails.
        :type: str
        """
        allowed_values = ["ADD_DBSERVER_NETWORK", "REMOVE_DBSERVER_NETWORK"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            raise ValueError(
                "Invalid value for `action`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._action = action

    @property
    def vm_networks(self):
        """
        **[Required]** Gets the vm_networks of this ResizeVmClusterNetworkDetails.
        Details of the client and backup networks.


        :return: The vm_networks of this ResizeVmClusterNetworkDetails.
        :rtype: list[oci.database.models.VmNetworkDetails]
        """
        return self._vm_networks

    @vm_networks.setter
    def vm_networks(self, vm_networks):
        """
        Sets the vm_networks of this ResizeVmClusterNetworkDetails.
        Details of the client and backup networks.


        :param vm_networks: The vm_networks of this ResizeVmClusterNetworkDetails.
        :type: list[oci.database.models.VmNetworkDetails]
        """
        self._vm_networks = vm_networks

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
