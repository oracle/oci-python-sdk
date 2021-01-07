# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateNetworkSecurityGroupsDetails(object):
    """
    An object representing an updated list of network security groups (NSGs) that overwrites the existing list of NSGs.
    *  If the load balancer has no NSGs configured, it uses the NSGs in this list.
    *  If the load balancer has a list of NSGs configured, this list replaces the existing list.
    *  If the load balancer has a list of NSGs configured and this list is empty, the operation removes all of the load balancer's NSG associations.
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
        An array of NSG `OCIDs`__ associated with the load
        balancer.

        During the load balancer's creation, the service adds the new load balancer to the specified NSGs.

        The benefits of associating the load balancer with NSGs include:

        *  NSGs define network security rules to govern ingress and egress traffic for the load balancer.

        *  The network security rules of other resources can reference the NSGs associated with the load balancer
           to ensure access.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The network_security_group_ids of this UpdateNetworkSecurityGroupsDetails.
        :rtype: list[str]
        """
        return self._network_security_group_ids

    @network_security_group_ids.setter
    def network_security_group_ids(self, network_security_group_ids):
        """
        Sets the network_security_group_ids of this UpdateNetworkSecurityGroupsDetails.
        An array of NSG `OCIDs`__ associated with the load
        balancer.

        During the load balancer's creation, the service adds the new load balancer to the specified NSGs.

        The benefits of associating the load balancer with NSGs include:

        *  NSGs define network security rules to govern ingress and egress traffic for the load balancer.

        *  The network security rules of other resources can reference the NSGs associated with the load balancer
           to ensure access.

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
