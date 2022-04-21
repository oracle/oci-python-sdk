# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .service_discovery_configuration import ServiceDiscoveryConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DnsServiceDiscoveryConfiguration(ServiceDiscoveryConfiguration):
    """
    DNS-based service discovery configuration for virtual deployments.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DnsServiceDiscoveryConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.service_mesh.models.DnsServiceDiscoveryConfiguration.type` attribute
        of this class is ``DNS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DnsServiceDiscoveryConfiguration.
            Allowed values for this property are: "DNS"
        :type type: str

        :param hostname:
            The value to assign to the hostname property of this DnsServiceDiscoveryConfiguration.
        :type hostname: str

        """
        self.swagger_types = {
            'type': 'str',
            'hostname': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'hostname': 'hostname'
        }

        self._type = None
        self._hostname = None
        self._type = 'DNS'

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this DnsServiceDiscoveryConfiguration.
        The hostname of the virtual deployments.


        :return: The hostname of this DnsServiceDiscoveryConfiguration.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this DnsServiceDiscoveryConfiguration.
        The hostname of the virtual deployments.


        :param hostname: The hostname of this DnsServiceDiscoveryConfiguration.
        :type: str
        """
        self._hostname = hostname

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
