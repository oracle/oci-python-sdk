# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseToolsPrivateEndpointReverseConnectionConfiguration(object):
    """
    Reverse connection configuration details of the private endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseToolsPrivateEndpointReverseConnectionConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param reverse_connections_source_ips:
            The value to assign to the reverse_connections_source_ips property of this DatabaseToolsPrivateEndpointReverseConnectionConfiguration.
        :type reverse_connections_source_ips: list[oci.database_tools.models.DatabaseToolsPrivateEndpointReverseConnectionsSourceIp]

        """
        self.swagger_types = {
            'reverse_connections_source_ips': 'list[DatabaseToolsPrivateEndpointReverseConnectionsSourceIp]'
        }

        self.attribute_map = {
            'reverse_connections_source_ips': 'reverseConnectionsSourceIps'
        }

        self._reverse_connections_source_ips = None

    @property
    def reverse_connections_source_ips(self):
        """
        Gets the reverse_connections_source_ips of this DatabaseToolsPrivateEndpointReverseConnectionConfiguration.
        A list of IP addresses in the customer VCN to be used as the source IPs for reverse connection packets
        traveling from the service's VCN to the customer's VCN.


        :return: The reverse_connections_source_ips of this DatabaseToolsPrivateEndpointReverseConnectionConfiguration.
        :rtype: list[oci.database_tools.models.DatabaseToolsPrivateEndpointReverseConnectionsSourceIp]
        """
        return self._reverse_connections_source_ips

    @reverse_connections_source_ips.setter
    def reverse_connections_source_ips(self, reverse_connections_source_ips):
        """
        Sets the reverse_connections_source_ips of this DatabaseToolsPrivateEndpointReverseConnectionConfiguration.
        A list of IP addresses in the customer VCN to be used as the source IPs for reverse connection packets
        traveling from the service's VCN to the customer's VCN.


        :param reverse_connections_source_ips: The reverse_connections_source_ips of this DatabaseToolsPrivateEndpointReverseConnectionConfiguration.
        :type: list[oci.database_tools.models.DatabaseToolsPrivateEndpointReverseConnectionsSourceIp]
        """
        self._reverse_connections_source_ips = reverse_connections_source_ips

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
