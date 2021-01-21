# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RemovePublicIpPoolCapacityDetails(object):
    """
    The information needed to remove capacity from a public IP pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RemovePublicIpPoolCapacityDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cidr_block:
            The value to assign to the cidr_block property of this RemovePublicIpPoolCapacityDetails.
        :type cidr_block: str

        """
        self.swagger_types = {
            'cidr_block': 'str'
        }

        self.attribute_map = {
            'cidr_block': 'cidrBlock'
        }

        self._cidr_block = None

    @property
    def cidr_block(self):
        """
        **[Required]** Gets the cidr_block of this RemovePublicIpPoolCapacityDetails.
        The CIDR block to remove from the  public IP pool.
        Example: `10.0.1.0/24`


        :return: The cidr_block of this RemovePublicIpPoolCapacityDetails.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this RemovePublicIpPoolCapacityDetails.
        The CIDR block to remove from the  public IP pool.
        Example: `10.0.1.0/24`


        :param cidr_block: The cidr_block of this RemovePublicIpPoolCapacityDetails.
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
