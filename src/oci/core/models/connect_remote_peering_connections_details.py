# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectRemotePeeringConnectionsDetails(object):
    """
    Information about the other remote peering connection (RPC).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectRemotePeeringConnectionsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param peer_id:
            The value to assign to the peer_id property of this ConnectRemotePeeringConnectionsDetails.
        :type peer_id: str

        :param peer_region_name:
            The value to assign to the peer_region_name property of this ConnectRemotePeeringConnectionsDetails.
        :type peer_region_name: str

        """
        self.swagger_types = {
            'peer_id': 'str',
            'peer_region_name': 'str'
        }

        self.attribute_map = {
            'peer_id': 'peerId',
            'peer_region_name': 'peerRegionName'
        }

        self._peer_id = None
        self._peer_region_name = None

    @property
    def peer_id(self):
        """
        **[Required]** Gets the peer_id of this ConnectRemotePeeringConnectionsDetails.
        The OCID of the RPC you want to peer with.


        :return: The peer_id of this ConnectRemotePeeringConnectionsDetails.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """
        Sets the peer_id of this ConnectRemotePeeringConnectionsDetails.
        The OCID of the RPC you want to peer with.


        :param peer_id: The peer_id of this ConnectRemotePeeringConnectionsDetails.
        :type: str
        """
        self._peer_id = peer_id

    @property
    def peer_region_name(self):
        """
        **[Required]** Gets the peer_region_name of this ConnectRemotePeeringConnectionsDetails.
        The name of the region that contains the RPC you want to peer with.

        Example: `us-ashburn-1`


        :return: The peer_region_name of this ConnectRemotePeeringConnectionsDetails.
        :rtype: str
        """
        return self._peer_region_name

    @peer_region_name.setter
    def peer_region_name(self, peer_region_name):
        """
        Sets the peer_region_name of this ConnectRemotePeeringConnectionsDetails.
        The name of the region that contains the RPC you want to peer with.

        Example: `us-ashburn-1`


        :param peer_region_name: The peer_region_name of this ConnectRemotePeeringConnectionsDetails.
        :type: str
        """
        self._peer_region_name = peer_region_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
