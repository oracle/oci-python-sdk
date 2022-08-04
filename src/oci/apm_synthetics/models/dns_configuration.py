# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DnsConfiguration(object):
    """
    Dns settings.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DnsConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_override_dns:
            The value to assign to the is_override_dns property of this DnsConfiguration.
        :type is_override_dns: bool

        :param override_dns_ip:
            The value to assign to the override_dns_ip property of this DnsConfiguration.
        :type override_dns_ip: str

        """
        self.swagger_types = {
            'is_override_dns': 'bool',
            'override_dns_ip': 'str'
        }

        self.attribute_map = {
            'is_override_dns': 'isOverrideDns',
            'override_dns_ip': 'overrideDnsIp'
        }

        self._is_override_dns = None
        self._override_dns_ip = None

    @property
    def is_override_dns(self):
        """
        Gets the is_override_dns of this DnsConfiguration.
        If isOverrideDns is true, then dns will be overridden.


        :return: The is_override_dns of this DnsConfiguration.
        :rtype: bool
        """
        return self._is_override_dns

    @is_override_dns.setter
    def is_override_dns(self, is_override_dns):
        """
        Sets the is_override_dns of this DnsConfiguration.
        If isOverrideDns is true, then dns will be overridden.


        :param is_override_dns: The is_override_dns of this DnsConfiguration.
        :type: bool
        """
        self._is_override_dns = is_override_dns

    @property
    def override_dns_ip(self):
        """
        Gets the override_dns_ip of this DnsConfiguration.
        Override dns ip value. This value will be honored only if *ref-isOverrideDns is set to true.


        :return: The override_dns_ip of this DnsConfiguration.
        :rtype: str
        """
        return self._override_dns_ip

    @override_dns_ip.setter
    def override_dns_ip(self, override_dns_ip):
        """
        Sets the override_dns_ip of this DnsConfiguration.
        Override dns ip value. This value will be honored only if *ref-isOverrideDns is set to true.


        :param override_dns_ip: The override_dns_ip of this DnsConfiguration.
        :type: str
        """
        self._override_dns_ip = override_dns_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
