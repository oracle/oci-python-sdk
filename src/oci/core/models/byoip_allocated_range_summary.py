# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ByoipAllocatedRangeSummary(object):
    """
    A summary of CIDR block subranges that are currently allocated to an IP pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ByoipAllocatedRangeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cidr_block:
            The value to assign to the cidr_block property of this ByoipAllocatedRangeSummary.
        :type cidr_block: str

        :param public_ip_pool_id:
            The value to assign to the public_ip_pool_id property of this ByoipAllocatedRangeSummary.
        :type public_ip_pool_id: str

        """
        self.swagger_types = {
            'cidr_block': 'str',
            'public_ip_pool_id': 'str'
        }

        self.attribute_map = {
            'cidr_block': 'cidrBlock',
            'public_ip_pool_id': 'publicIpPoolId'
        }

        self._cidr_block = None
        self._public_ip_pool_id = None

    @property
    def cidr_block(self):
        """
        Gets the cidr_block of this ByoipAllocatedRangeSummary.
        The BYOIP CIDR block range or subrange allocated to an IP pool. This could be all or part of a BYOIP CIDR block.


        :return: The cidr_block of this ByoipAllocatedRangeSummary.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this ByoipAllocatedRangeSummary.
        The BYOIP CIDR block range or subrange allocated to an IP pool. This could be all or part of a BYOIP CIDR block.


        :param cidr_block: The cidr_block of this ByoipAllocatedRangeSummary.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def public_ip_pool_id(self):
        """
        Gets the public_ip_pool_id of this ByoipAllocatedRangeSummary.
        The `OCID`__ of the IP pool containing the CIDR block.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The public_ip_pool_id of this ByoipAllocatedRangeSummary.
        :rtype: str
        """
        return self._public_ip_pool_id

    @public_ip_pool_id.setter
    def public_ip_pool_id(self, public_ip_pool_id):
        """
        Sets the public_ip_pool_id of this ByoipAllocatedRangeSummary.
        The `OCID`__ of the IP pool containing the CIDR block.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param public_ip_pool_id: The public_ip_pool_id of this ByoipAllocatedRangeSummary.
        :type: str
        """
        self._public_ip_pool_id = public_ip_pool_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
