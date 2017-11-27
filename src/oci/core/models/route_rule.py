# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RouteRule(object):

    def __init__(self, **kwargs):
        """
        Initializes a new RouteRule object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cidr_block:
            The value to assign to the cidr_block property of this RouteRule.
        :type cidr_block: str

        :param network_entity_id:
            The value to assign to the network_entity_id property of this RouteRule.
        :type network_entity_id: str

        """
        self.swagger_types = {
            'cidr_block': 'str',
            'network_entity_id': 'str'
        }

        self.attribute_map = {
            'cidr_block': 'cidrBlock',
            'network_entity_id': 'networkEntityId'
        }

        self._cidr_block = None
        self._network_entity_id = None

    @property
    def cidr_block(self):
        """
        Gets the cidr_block of this RouteRule.
        A destination IP address range in CIDR notation. Matching packets will
        be routed to the indicated network entity (the target).

        Example: `0.0.0.0/0`


        :return: The cidr_block of this RouteRule.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this RouteRule.
        A destination IP address range in CIDR notation. Matching packets will
        be routed to the indicated network entity (the target).

        Example: `0.0.0.0/0`


        :param cidr_block: The cidr_block of this RouteRule.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def network_entity_id(self):
        """
        Gets the network_entity_id of this RouteRule.
        The OCID for the route rule's target. For information about the type of
        targets you can specify, see
        `Route Tables`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingroutetables.htm


        :return: The network_entity_id of this RouteRule.
        :rtype: str
        """
        return self._network_entity_id

    @network_entity_id.setter
    def network_entity_id(self, network_entity_id):
        """
        Sets the network_entity_id of this RouteRule.
        The OCID for the route rule's target. For information about the type of
        targets you can specify, see
        `Route Tables`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingroutetables.htm


        :param network_entity_id: The network_entity_id of this RouteRule.
        :type: str
        """
        self._network_entity_id = network_entity_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
