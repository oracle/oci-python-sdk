# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ByoipRangeVcnIpv6AllocationSummary(object):
    """
    A summary of IPv6 CIDR block subranges currently allocated to a VCN.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ByoipRangeVcnIpv6AllocationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param byoip_range_id:
            The value to assign to the byoip_range_id property of this ByoipRangeVcnIpv6AllocationSummary.
        :type byoip_range_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ByoipRangeVcnIpv6AllocationSummary.
        :type compartment_id: str

        :param ipv6_cidr_block:
            The value to assign to the ipv6_cidr_block property of this ByoipRangeVcnIpv6AllocationSummary.
        :type ipv6_cidr_block: str

        :param vcn_id:
            The value to assign to the vcn_id property of this ByoipRangeVcnIpv6AllocationSummary.
        :type vcn_id: str

        """
        self.swagger_types = {
            'byoip_range_id': 'str',
            'compartment_id': 'str',
            'ipv6_cidr_block': 'str',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'byoip_range_id': 'byoipRangeId',
            'compartment_id': 'compartmentId',
            'ipv6_cidr_block': 'ipv6CidrBlock',
            'vcn_id': 'vcnId'
        }

        self._byoip_range_id = None
        self._compartment_id = None
        self._ipv6_cidr_block = None
        self._vcn_id = None

    @property
    def byoip_range_id(self):
        """
        Gets the byoip_range_id of this ByoipRangeVcnIpv6AllocationSummary.
        The `OCID`__ of the `ByoipRange` resource to which the CIDR block belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The byoip_range_id of this ByoipRangeVcnIpv6AllocationSummary.
        :rtype: str
        """
        return self._byoip_range_id

    @byoip_range_id.setter
    def byoip_range_id(self, byoip_range_id):
        """
        Sets the byoip_range_id of this ByoipRangeVcnIpv6AllocationSummary.
        The `OCID`__ of the `ByoipRange` resource to which the CIDR block belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param byoip_range_id: The byoip_range_id of this ByoipRangeVcnIpv6AllocationSummary.
        :type: str
        """
        self._byoip_range_id = byoip_range_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this ByoipRangeVcnIpv6AllocationSummary.
        The `OCID`__ of the compartment containing the `ByoipRange`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ByoipRangeVcnIpv6AllocationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ByoipRangeVcnIpv6AllocationSummary.
        The `OCID`__ of the compartment containing the `ByoipRange`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ByoipRangeVcnIpv6AllocationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def ipv6_cidr_block(self):
        """
        Gets the ipv6_cidr_block of this ByoipRangeVcnIpv6AllocationSummary.
        The BYOIPv6 CIDR block range or subrange allocated to a VCN. This could be all or part of a BYOIPv6 CIDR block.
        Each VCN allocation must be /64 or larger.


        :return: The ipv6_cidr_block of this ByoipRangeVcnIpv6AllocationSummary.
        :rtype: str
        """
        return self._ipv6_cidr_block

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, ipv6_cidr_block):
        """
        Sets the ipv6_cidr_block of this ByoipRangeVcnIpv6AllocationSummary.
        The BYOIPv6 CIDR block range or subrange allocated to a VCN. This could be all or part of a BYOIPv6 CIDR block.
        Each VCN allocation must be /64 or larger.


        :param ipv6_cidr_block: The ipv6_cidr_block of this ByoipRangeVcnIpv6AllocationSummary.
        :type: str
        """
        self._ipv6_cidr_block = ipv6_cidr_block

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this ByoipRangeVcnIpv6AllocationSummary.
        The `OCID`__ of the `Vcn` resource to which the ByoipRange belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this ByoipRangeVcnIpv6AllocationSummary.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this ByoipRangeVcnIpv6AllocationSummary.
        The `OCID`__ of the `Vcn` resource to which the ByoipRange belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this ByoipRangeVcnIpv6AllocationSummary.
        :type: str
        """
        self._vcn_id = vcn_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
