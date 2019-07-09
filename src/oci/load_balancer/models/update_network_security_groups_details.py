# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateNetworkSecurityGroupsDetails(object):
    """
    An object representing an updated list of NSGs that overwrites the existing list of NSGs. In particular, if the load balancer had no prior NSGs configured, these with be the new NSGs to be used by the load balancer. If the load balancer used to have a list of NSGs configured, and this list contains no entries, then the load balancer will contain no NSGs after this call completes.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateNetworkSecurityGroupsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param network_security_group_ids:
            The value to assign to the network_security_group_ids property of this UpdateNetworkSecurityGroupsDetails.
        :type network_security_group_ids: list[str]

        """
        self.swagger_types = {
            'network_security_group_ids': 'list[str]'
        }

        self.attribute_map = {
            'network_security_group_ids': 'networkSecurityGroupIds'
        }

        self._network_security_group_ids = None

    @property
    def network_security_group_ids(self):
        """
        Gets the network_security_group_ids of this UpdateNetworkSecurityGroupsDetails.
        The array of NSG `OCIDs`__ to be used by this Load Balancer.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The network_security_group_ids of this UpdateNetworkSecurityGroupsDetails.
        :rtype: list[str]
        """
        return self._network_security_group_ids

    @network_security_group_ids.setter
    def network_security_group_ids(self, network_security_group_ids):
        """
        Sets the network_security_group_ids of this UpdateNetworkSecurityGroupsDetails.
        The array of NSG `OCIDs`__ to be used by this Load Balancer.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param network_security_group_ids: The network_security_group_ids of this UpdateNetworkSecurityGroupsDetails.
        :type: list[str]
        """
        self._network_security_group_ids = network_security_group_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
