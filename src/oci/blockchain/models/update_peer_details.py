# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdatePeerDetails(object):
    """
    peer to modify ocpu allocation
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdatePeerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ocpu_allocation_param:
            The value to assign to the ocpu_allocation_param property of this UpdatePeerDetails.
        :type ocpu_allocation_param: oci.blockchain.models.OcpuAllocationNumberParam

        """
        self.swagger_types = {
            'ocpu_allocation_param': 'OcpuAllocationNumberParam'
        }

        self.attribute_map = {
            'ocpu_allocation_param': 'ocpuAllocationParam'
        }

        self._ocpu_allocation_param = None

    @property
    def ocpu_allocation_param(self):
        """
        **[Required]** Gets the ocpu_allocation_param of this UpdatePeerDetails.

        :return: The ocpu_allocation_param of this UpdatePeerDetails.
        :rtype: oci.blockchain.models.OcpuAllocationNumberParam
        """
        return self._ocpu_allocation_param

    @ocpu_allocation_param.setter
    def ocpu_allocation_param(self, ocpu_allocation_param):
        """
        Sets the ocpu_allocation_param of this UpdatePeerDetails.

        :param ocpu_allocation_param: The ocpu_allocation_param of this UpdatePeerDetails.
        :type: oci.blockchain.models.OcpuAllocationNumberParam
        """
        self._ocpu_allocation_param = ocpu_allocation_param

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
