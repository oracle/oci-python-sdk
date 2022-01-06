# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseToolsPrivateEndpointReverseConnectionsSourceIp(object):
    """
    Source IP information for reverse connection configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseToolsPrivateEndpointReverseConnectionsSourceIp object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_ip:
            The value to assign to the source_ip property of this DatabaseToolsPrivateEndpointReverseConnectionsSourceIp.
        :type source_ip: str

        """
        self.swagger_types = {
            'source_ip': 'str'
        }

        self.attribute_map = {
            'source_ip': 'sourceIp'
        }

        self._source_ip = None

    @property
    def source_ip(self):
        """
        Gets the source_ip of this DatabaseToolsPrivateEndpointReverseConnectionsSourceIp.
        The IP address in the customer's VCN to be used as the source IP for reverse connection packets
        traveling from the customer's VCN to the service's VCN.


        :return: The source_ip of this DatabaseToolsPrivateEndpointReverseConnectionsSourceIp.
        :rtype: str
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        """
        Sets the source_ip of this DatabaseToolsPrivateEndpointReverseConnectionsSourceIp.
        The IP address in the customer's VCN to be used as the source IP for reverse connection packets
        traveling from the customer's VCN to the service's VCN.


        :param source_ip: The source_ip of this DatabaseToolsPrivateEndpointReverseConnectionsSourceIp.
        :type: str
        """
        self._source_ip = source_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
