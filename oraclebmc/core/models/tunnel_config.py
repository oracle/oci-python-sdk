# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class TunnelConfig(object):

    def __init__(self):

        self.swagger_types = {
            'ip_address': 'str',
            'shared_secret': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'ip_address': 'ipAddress',
            'shared_secret': 'sharedSecret',
            'time_created': 'timeCreated'
        }

        self._ip_address = None
        self._shared_secret = None
        self._time_created = None

    @property
    def ip_address(self):
        """
        Gets the ip_address of this TunnelConfig.
        The IP address of Oracle's VPN headend.

        Example: `129.146.17.50`


        :return: The ip_address of this TunnelConfig.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this TunnelConfig.
        The IP address of Oracle's VPN headend.

        Example: `129.146.17.50`


        :param ip_address: The ip_address of this TunnelConfig.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def shared_secret(self):
        """
        Gets the shared_secret of this TunnelConfig.
        The shared secret of the IPSec tunnel.

        Example: `vFG2IF6TWq4UToUiLSRDoJEUs6j1c.p8G.dVQxiMfMO0yXMLi.lZTbYIWhGu4V8o`


        :return: The shared_secret of this TunnelConfig.
        :rtype: str
        """
        return self._shared_secret

    @shared_secret.setter
    def shared_secret(self, shared_secret):
        """
        Sets the shared_secret of this TunnelConfig.
        The shared secret of the IPSec tunnel.

        Example: `vFG2IF6TWq4UToUiLSRDoJEUs6j1c.p8G.dVQxiMfMO0yXMLi.lZTbYIWhGu4V8o`


        :param shared_secret: The shared_secret of this TunnelConfig.
        :type: str
        """
        self._shared_secret = shared_secret

    @property
    def time_created(self):
        """
        Gets the time_created of this TunnelConfig.
        The date and time the IPSec connection was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this TunnelConfig.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TunnelConfig.
        The date and time the IPSec connection was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this TunnelConfig.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
