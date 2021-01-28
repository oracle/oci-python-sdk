# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FastConnectProviderServiceKey(object):
    """
    A provider service key and its details. A provider service key is an identifier for a provider's
    virtual circuit.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FastConnectProviderServiceKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this FastConnectProviderServiceKey.
        :type name: str

        :param bandwidth_shape_name:
            The value to assign to the bandwidth_shape_name property of this FastConnectProviderServiceKey.
        :type bandwidth_shape_name: str

        :param peering_location:
            The value to assign to the peering_location property of this FastConnectProviderServiceKey.
        :type peering_location: str

        """
        self.swagger_types = {
            'name': 'str',
            'bandwidth_shape_name': 'str',
            'peering_location': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'bandwidth_shape_name': 'bandwidthShapeName',
            'peering_location': 'peeringLocation'
        }

        self._name = None
        self._bandwidth_shape_name = None
        self._peering_location = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this FastConnectProviderServiceKey.
        The service key that the provider gives you when you set up a virtual circuit connection
        from the provider to Oracle Cloud Infrastructure. Use this value as the `providerServiceKeyName`
        query parameter for
        :func:`get_fast_connect_provider_service_key`.


        :return: The name of this FastConnectProviderServiceKey.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FastConnectProviderServiceKey.
        The service key that the provider gives you when you set up a virtual circuit connection
        from the provider to Oracle Cloud Infrastructure. Use this value as the `providerServiceKeyName`
        query parameter for
        :func:`get_fast_connect_provider_service_key`.


        :param name: The name of this FastConnectProviderServiceKey.
        :type: str
        """
        self._name = name

    @property
    def bandwidth_shape_name(self):
        """
        Gets the bandwidth_shape_name of this FastConnectProviderServiceKey.
        The provisioned data rate of the connection. To get a list of the
        available bandwidth levels (that is, shapes), see
        :func:`list_fast_connect_provider_virtual_circuit_bandwidth_shapes`.

        Example: `10 Gbps`


        :return: The bandwidth_shape_name of this FastConnectProviderServiceKey.
        :rtype: str
        """
        return self._bandwidth_shape_name

    @bandwidth_shape_name.setter
    def bandwidth_shape_name(self, bandwidth_shape_name):
        """
        Sets the bandwidth_shape_name of this FastConnectProviderServiceKey.
        The provisioned data rate of the connection. To get a list of the
        available bandwidth levels (that is, shapes), see
        :func:`list_fast_connect_provider_virtual_circuit_bandwidth_shapes`.

        Example: `10 Gbps`


        :param bandwidth_shape_name: The bandwidth_shape_name of this FastConnectProviderServiceKey.
        :type: str
        """
        self._bandwidth_shape_name = bandwidth_shape_name

    @property
    def peering_location(self):
        """
        Gets the peering_location of this FastConnectProviderServiceKey.
        The provider's peering location.


        :return: The peering_location of this FastConnectProviderServiceKey.
        :rtype: str
        """
        return self._peering_location

    @peering_location.setter
    def peering_location(self, peering_location):
        """
        Sets the peering_location of this FastConnectProviderServiceKey.
        The provider's peering location.


        :param peering_location: The peering_location of this FastConnectProviderServiceKey.
        :type: str
        """
        self._peering_location = peering_location

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
