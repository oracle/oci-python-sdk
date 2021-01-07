# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePeerDetails(object):
    """
    The Peer details to be added
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePeerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param role:
            The value to assign to the role property of this CreatePeerDetails.
        :type role: str

        :param alias:
            The value to assign to the alias property of this CreatePeerDetails.
        :type alias: str

        :param ocpu_allocation_param:
            The value to assign to the ocpu_allocation_param property of this CreatePeerDetails.
        :type ocpu_allocation_param: oci.blockchain.models.OcpuAllocationNumberParam

        :param ad:
            The value to assign to the ad property of this CreatePeerDetails.
        :type ad: str

        """
        self.swagger_types = {
            'role': 'str',
            'alias': 'str',
            'ocpu_allocation_param': 'OcpuAllocationNumberParam',
            'ad': 'str'
        }

        self.attribute_map = {
            'role': 'role',
            'alias': 'alias',
            'ocpu_allocation_param': 'ocpuAllocationParam',
            'ad': 'ad'
        }

        self._role = None
        self._alias = None
        self._ocpu_allocation_param = None
        self._ad = None

    @property
    def role(self):
        """
        **[Required]** Gets the role of this CreatePeerDetails.
        Peer role


        :return: The role of this CreatePeerDetails.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this CreatePeerDetails.
        Peer role


        :param role: The role of this CreatePeerDetails.
        :type: str
        """
        self._role = role

    @property
    def alias(self):
        """
        Gets the alias of this CreatePeerDetails.
        peer alias


        :return: The alias of this CreatePeerDetails.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """
        Sets the alias of this CreatePeerDetails.
        peer alias


        :param alias: The alias of this CreatePeerDetails.
        :type: str
        """
        self._alias = alias

    @property
    def ocpu_allocation_param(self):
        """
        **[Required]** Gets the ocpu_allocation_param of this CreatePeerDetails.

        :return: The ocpu_allocation_param of this CreatePeerDetails.
        :rtype: oci.blockchain.models.OcpuAllocationNumberParam
        """
        return self._ocpu_allocation_param

    @ocpu_allocation_param.setter
    def ocpu_allocation_param(self, ocpu_allocation_param):
        """
        Sets the ocpu_allocation_param of this CreatePeerDetails.

        :param ocpu_allocation_param: The ocpu_allocation_param of this CreatePeerDetails.
        :type: oci.blockchain.models.OcpuAllocationNumberParam
        """
        self._ocpu_allocation_param = ocpu_allocation_param

    @property
    def ad(self):
        """
        **[Required]** Gets the ad of this CreatePeerDetails.
        Availability Domain to place new peer


        :return: The ad of this CreatePeerDetails.
        :rtype: str
        """
        return self._ad

    @ad.setter
    def ad(self, ad):
        """
        Sets the ad of this CreatePeerDetails.
        Availability Domain to place new peer


        :param ad: The ad of this CreatePeerDetails.
        :type: str
        """
        self._ad = ad

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
