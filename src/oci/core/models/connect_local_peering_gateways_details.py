# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectLocalPeeringGatewaysDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectLocalPeeringGatewaysDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param peer_id:
            The value to assign to the peer_id property of this ConnectLocalPeeringGatewaysDetails.
        :type peer_id: str

        """
        self.swagger_types = {
            'peer_id': 'str'
        }

        self.attribute_map = {
            'peer_id': 'peerId'
        }

        self._peer_id = None

    @property
    def peer_id(self):
        """
        Gets the peer_id of this ConnectLocalPeeringGatewaysDetails.
        The OCID of the LPG you want to peer with.


        :return: The peer_id of this ConnectLocalPeeringGatewaysDetails.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """
        Sets the peer_id of this ConnectLocalPeeringGatewaysDetails.
        The OCID of the LPG you want to peer with.


        :param peer_id: The peer_id of this ConnectLocalPeeringGatewaysDetails.
        :type: str
        """
        self._peer_id = peer_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
