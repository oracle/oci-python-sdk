# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkEndpointDetails(object):
    """
    Base representation of a network endpoint.
    """

    #: A constant which can be used with the network_endpoint_type property of a NetworkEndpointDetails.
    #: This constant has a value of "PUBLIC"
    NETWORK_ENDPOINT_TYPE_PUBLIC = "PUBLIC"

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkEndpointDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.integration.models.PublicEndpointDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param network_endpoint_type:
            The value to assign to the network_endpoint_type property of this NetworkEndpointDetails.
            Allowed values for this property are: "PUBLIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type network_endpoint_type: str

        """
        self.swagger_types = {
            'network_endpoint_type': 'str'
        }

        self.attribute_map = {
            'network_endpoint_type': 'networkEndpointType'
        }

        self._network_endpoint_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['networkEndpointType']

        if type == 'PUBLIC':
            return 'PublicEndpointDetails'
        else:
            return 'NetworkEndpointDetails'

    @property
    def network_endpoint_type(self):
        """
        **[Required]** Gets the network_endpoint_type of this NetworkEndpointDetails.
        The type of network endpoint.

        Allowed values for this property are: "PUBLIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The network_endpoint_type of this NetworkEndpointDetails.
        :rtype: str
        """
        return self._network_endpoint_type

    @network_endpoint_type.setter
    def network_endpoint_type(self, network_endpoint_type):
        """
        Sets the network_endpoint_type of this NetworkEndpointDetails.
        The type of network endpoint.


        :param network_endpoint_type: The network_endpoint_type of this NetworkEndpointDetails.
        :type: str
        """
        allowed_values = ["PUBLIC"]
        if not value_allowed_none_or_none_sentinel(network_endpoint_type, allowed_values):
            network_endpoint_type = 'UNKNOWN_ENUM_VALUE'
        self._network_endpoint_type = network_endpoint_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
