# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReachableIp(object):
    """
    The reachable, or alternative, IP address for a nonpublic IP address that is associated with the private endpoint.
    Resource Manager uses this IP address to connect to nonpublic resources through the associated private endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ReachableIp object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ip_address:
            The value to assign to the ip_address property of this ReachableIp.
        :type ip_address: str

        """
        self.swagger_types = {
            'ip_address': 'str'
        }

        self.attribute_map = {
            'ip_address': 'ipAddress'
        }

        self._ip_address = None

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this ReachableIp.
        Reachable IP address associated with the private endpoint.


        :return: The ip_address of this ReachableIp.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this ReachableIp.
        Reachable IP address associated with the private endpoint.


        :param ip_address: The ip_address of this ReachableIp.
        :type: str
        """
        self._ip_address = ip_address

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
