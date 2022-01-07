# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IpAddress(object):
    """
    A load balancer IP address.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IpAddress object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ip_address:
            The value to assign to the ip_address property of this IpAddress.
        :type ip_address: str

        :param is_public:
            The value to assign to the is_public property of this IpAddress.
        :type is_public: bool

        :param reserved_ip:
            The value to assign to the reserved_ip property of this IpAddress.
        :type reserved_ip: oci.load_balancer.models.ReservedIP

        """
        self.swagger_types = {
            'ip_address': 'str',
            'is_public': 'bool',
            'reserved_ip': 'ReservedIP'
        }

        self.attribute_map = {
            'ip_address': 'ipAddress',
            'is_public': 'isPublic',
            'reserved_ip': 'reservedIp'
        }

        self._ip_address = None
        self._is_public = None
        self._reserved_ip = None

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this IpAddress.
        An IP address.

        Example: `192.168.0.3`


        :return: The ip_address of this IpAddress.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this IpAddress.
        An IP address.

        Example: `192.168.0.3`


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

    @property
    def reserved_ip(self):
        """
        Gets the reserved_ip of this IpAddress.

        :return: The reserved_ip of this IpAddress.
        :rtype: oci.load_balancer.models.ReservedIP
        """
        return self._reserved_ip

    @reserved_ip.setter
    def reserved_ip(self, reserved_ip):
        """
        Sets the reserved_ip of this IpAddress.

        :param reserved_ip: The reserved_ip of this IpAddress.
        :type: oci.load_balancer.models.ReservedIP
        """
        self._reserved_ip = reserved_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
