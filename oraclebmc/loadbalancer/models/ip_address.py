# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class IpAddress(object):

    def __init__(self):

        self.swagger_types = {
            'ip_address': 'str',
            'is_public': 'bool'
        }

        self.attribute_map = {
            'ip_address': 'ipAddress',
            'is_public': 'isPublic'
        }

        self._ip_address = None
        self._is_public = None

    @property
    def ip_address(self):
        """
        Gets the ip_address of this IpAddress.
        An IP address.

        Example: `128.148.10.20`


        :return: The ip_address of this IpAddress.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this IpAddress.
        An IP address.

        Example: `128.148.10.20`


        :param ip_address: The ip_address of this IpAddress.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def is_public(self):
        """
        Gets the is_public of this IpAddress.
        Whether the IP address is public or private.

        If \"true\", the IP address is public and accessible from the internet.

        If \"false\", the IP address is private and accessible only from within the associated VCN.


        :return: The is_public of this IpAddress.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """
        Sets the is_public of this IpAddress.
        Whether the IP address is public or private.

        If \"true\", the IP address is public and accessible from the internet.

        If \"false\", the IP address is private and accessible only from within the associated VCN.


        :param is_public: The is_public of this IpAddress.
        :type: bool
        """
        self._is_public = is_public

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
