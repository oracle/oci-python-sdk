# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodeDetails(object):
    """
    Node details associated with a network.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NodeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hostname:
            The value to assign to the hostname property of this NodeDetails.
        :type hostname: str

        :param ip:
            The value to assign to the ip property of this NodeDetails.
        :type ip: str

        :param vip_hostname:
            The value to assign to the vip_hostname property of this NodeDetails.
        :type vip_hostname: str

        :param vip:
            The value to assign to the vip property of this NodeDetails.
        :type vip: str

        """
        self.swagger_types = {
            'hostname': 'str',
            'ip': 'str',
            'vip_hostname': 'str',
            'vip': 'str'
        }

        self.attribute_map = {
            'hostname': 'hostname',
            'ip': 'ip',
            'vip_hostname': 'vipHostname',
            'vip': 'vip'
        }

        self._hostname = None
        self._ip = None
        self._vip_hostname = None
        self._vip = None

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this NodeDetails.
        The node host name.


        :return: The hostname of this NodeDetails.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this NodeDetails.
        The node host name.


        :param hostname: The hostname of this NodeDetails.
        :type: str
        """
        self._hostname = hostname

    @property
    def ip(self):
        """
        **[Required]** Gets the ip of this NodeDetails.
        The node IP address.


        :return: The ip of this NodeDetails.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this NodeDetails.
        The node IP address.


        :param ip: The ip of this NodeDetails.
        :type: str
        """
        self._ip = ip

    @property
    def vip_hostname(self):
        """
        Gets the vip_hostname of this NodeDetails.
        The node virtual IP (VIP) host name.


        :return: The vip_hostname of this NodeDetails.
        :rtype: str
        """
        return self._vip_hostname

    @vip_hostname.setter
    def vip_hostname(self, vip_hostname):
        """
        Sets the vip_hostname of this NodeDetails.
        The node virtual IP (VIP) host name.


        :param vip_hostname: The vip_hostname of this NodeDetails.
        :type: str
        """
        self._vip_hostname = vip_hostname

    @property
    def vip(self):
        """
        Gets the vip of this NodeDetails.
        The node virtual IP (VIP) address.


        :return: The vip of this NodeDetails.
        :rtype: str
        """
        return self._vip

    @vip.setter
    def vip(self, vip):
        """
        Sets the vip of this NodeDetails.
        The node virtual IP (VIP) address.


        :param vip: The vip of this NodeDetails.
        :type: str
        """
        self._vip = vip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
