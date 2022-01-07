# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOsnDetails(object):
    """
    The Ordering Service Node details to be added
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOsnDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ad:
            The value to assign to the ad property of this CreateOsnDetails.
        :type ad: str

        :param ocpu_allocation_param:
            The value to assign to the ocpu_allocation_param property of this CreateOsnDetails.
        :type ocpu_allocation_param: oci.blockchain.models.OcpuAllocationNumberParam

        """
        self.swagger_types = {
            'ad': 'str',
            'ocpu_allocation_param': 'OcpuAllocationNumberParam'
        }

        self.attribute_map = {
            'ad': 'ad',
            'ocpu_allocation_param': 'ocpuAllocationParam'
        }

        self._ad = None
        self._ocpu_allocation_param = None

    @property
    def ad(self):
        """
        **[Required]** Gets the ad of this CreateOsnDetails.
        Availability Domain to place new OSN


        :return: The ad of this CreateOsnDetails.
        :rtype: str
        """
        return self._ad

    @ad.setter
    def ad(self, ad):
        """
        Sets the ad of this CreateOsnDetails.
        Availability Domain to place new OSN


        :param ad: The ad of this CreateOsnDetails.
        :type: str
        """
        self._ad = ad

    @property
    def ocpu_allocation_param(self):
        """
        Gets the ocpu_allocation_param of this CreateOsnDetails.

        :return: The ocpu_allocation_param of this CreateOsnDetails.
        :rtype: oci.blockchain.models.OcpuAllocationNumberParam
        """
        return self._ocpu_allocation_param

    @ocpu_allocation_param.setter
    def ocpu_allocation_param(self, ocpu_allocation_param):
        """
        Sets the ocpu_allocation_param of this CreateOsnDetails.

        :param ocpu_allocation_param: The ocpu_allocation_param of this CreateOsnDetails.
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
