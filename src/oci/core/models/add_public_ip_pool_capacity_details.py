# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddPublicIpPoolCapacityDetails(object):
    """
    The information used to add capacity to an IP pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddPublicIpPoolCapacityDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param byoip_range_id:
            The value to assign to the byoip_range_id property of this AddPublicIpPoolCapacityDetails.
        :type byoip_range_id: str

        :param cidr_block:
            The value to assign to the cidr_block property of this AddPublicIpPoolCapacityDetails.
        :type cidr_block: str

        """
        self.swagger_types = {
            'byoip_range_id': 'str',
            'cidr_block': 'str'
        }

        self.attribute_map = {
            'byoip_range_id': 'byoipRangeId',
            'cidr_block': 'cidrBlock'
        }

        self._byoip_range_id = None
        self._cidr_block = None

    @property
    def byoip_range_id(self):
        """
        **[Required]** Gets the byoip_range_id of this AddPublicIpPoolCapacityDetails.
        The `OCID`__ of the `ByoipRange` resource to which the CIDR block belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The byoip_range_id of this AddPublicIpPoolCapacityDetails.
        :rtype: str
        """
        return self._byoip_range_id

    @byoip_range_id.setter
    def byoip_range_id(self, byoip_range_id):
        """
        Sets the byoip_range_id of this AddPublicIpPoolCapacityDetails.
        The `OCID`__ of the `ByoipRange` resource to which the CIDR block belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param byoip_range_id: The byoip_range_id of this AddPublicIpPoolCapacityDetails.
        :type: str
        """
        self._byoip_range_id = byoip_range_id

    @property
    def cidr_block(self):
        """
        **[Required]** Gets the cidr_block of this AddPublicIpPoolCapacityDetails.
        The CIDR block to add to the public IP pool. It could be all of the CIDR block identified in `byoipRangeId`, or a subrange.
        Example: `10.0.1.0/24`


        :return: The cidr_block of this AddPublicIpPoolCapacityDetails.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this AddPublicIpPoolCapacityDetails.
        The CIDR block to add to the public IP pool. It could be all of the CIDR block identified in `byoipRangeId`, or a subrange.
        Example: `10.0.1.0/24`


        :param cidr_block: The cidr_block of this AddPublicIpPoolCapacityDetails.
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
