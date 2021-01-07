# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkConfig(object):
    """
    Additional configuration of customer's network.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_nat_gateway_required:
            The value to assign to the is_nat_gateway_required property of this NetworkConfig.
        :type is_nat_gateway_required: bool

        :param cidr_block:
            The value to assign to the cidr_block property of this NetworkConfig.
        :type cidr_block: str

        """
        self.swagger_types = {
            'is_nat_gateway_required': 'bool',
            'cidr_block': 'str'
        }

        self.attribute_map = {
            'is_nat_gateway_required': 'isNatGatewayRequired',
            'cidr_block': 'cidrBlock'
        }

        self._is_nat_gateway_required = None
        self._cidr_block = None

    @property
    def is_nat_gateway_required(self):
        """
        Gets the is_nat_gateway_required of this NetworkConfig.
        A boolean flag whether to configure a NAT gateway.


        :return: The is_nat_gateway_required of this NetworkConfig.
        :rtype: bool
        """
        return self._is_nat_gateway_required

    @is_nat_gateway_required.setter
    def is_nat_gateway_required(self, is_nat_gateway_required):
        """
        Sets the is_nat_gateway_required of this NetworkConfig.
        A boolean flag whether to configure a NAT gateway.


        :param is_nat_gateway_required: The is_nat_gateway_required of this NetworkConfig.
        :type: bool
        """
        self._is_nat_gateway_required = is_nat_gateway_required

    @property
    def cidr_block(self):
        """
        Gets the cidr_block of this NetworkConfig.
        The CIDR IP address block of the VCN.


        :return: The cidr_block of this NetworkConfig.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this NetworkConfig.
        The CIDR IP address block of the VCN.


        :param cidr_block: The cidr_block of this NetworkConfig.
        :type: str
        """
        self._cidr_block = cidr_block

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
