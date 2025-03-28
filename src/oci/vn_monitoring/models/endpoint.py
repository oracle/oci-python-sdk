# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Endpoint(object):
    """
    Information describing a source or destination in a `PathAnalyzerTest` resource.
    """

    #: A constant which can be used with the type property of a Endpoint.
    #: This constant has a value of "IP_ADDRESS"
    TYPE_IP_ADDRESS = "IP_ADDRESS"

    #: A constant which can be used with the type property of a Endpoint.
    #: This constant has a value of "SUBNET"
    TYPE_SUBNET = "SUBNET"

    #: A constant which can be used with the type property of a Endpoint.
    #: This constant has a value of "COMPUTE_INSTANCE"
    TYPE_COMPUTE_INSTANCE = "COMPUTE_INSTANCE"

    #: A constant which can be used with the type property of a Endpoint.
    #: This constant has a value of "VNIC"
    TYPE_VNIC = "VNIC"

    #: A constant which can be used with the type property of a Endpoint.
    #: This constant has a value of "LOAD_BALANCER"
    TYPE_LOAD_BALANCER = "LOAD_BALANCER"

    #: A constant which can be used with the type property of a Endpoint.
    #: This constant has a value of "LOAD_BALANCER_LISTENER"
    TYPE_LOAD_BALANCER_LISTENER = "LOAD_BALANCER_LISTENER"

    #: A constant which can be used with the type property of a Endpoint.
    #: This constant has a value of "NETWORK_LOAD_BALANCER"
    TYPE_NETWORK_LOAD_BALANCER = "NETWORK_LOAD_BALANCER"

    #: A constant which can be used with the type property of a Endpoint.
    #: This constant has a value of "NETWORK_LOAD_BALANCER_LISTENER"
    TYPE_NETWORK_LOAD_BALANCER_LISTENER = "NETWORK_LOAD_BALANCER_LISTENER"

    #: A constant which can be used with the type property of a Endpoint.
    #: This constant has a value of "VLAN"
    TYPE_VLAN = "VLAN"

    #: A constant which can be used with the type property of a Endpoint.
    #: This constant has a value of "ON_PREM"
    TYPE_ON_PREM = "ON_PREM"

    def __init__(self, **kwargs):
        """
        Initializes a new Endpoint object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.vn_monitoring.models.NetworkLoadBalancerListenerEndpoint`
        * :class:`~oci.vn_monitoring.models.ComputeInstanceEndpoint`
        * :class:`~oci.vn_monitoring.models.NetworkLoadBalancerEndpoint`
        * :class:`~oci.vn_monitoring.models.OnPremEndpoint`
        * :class:`~oci.vn_monitoring.models.LoadBalancerEndpoint`
        * :class:`~oci.vn_monitoring.models.VnicEndpoint`
        * :class:`~oci.vn_monitoring.models.IpAddressEndpoint`
        * :class:`~oci.vn_monitoring.models.VlanEndpoint`
        * :class:`~oci.vn_monitoring.models.SubnetEndpoint`
        * :class:`~oci.vn_monitoring.models.LoadBalancerListenerEndpoint`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this Endpoint.
            Allowed values for this property are: "IP_ADDRESS", "SUBNET", "COMPUTE_INSTANCE", "VNIC", "LOAD_BALANCER", "LOAD_BALANCER_LISTENER", "NETWORK_LOAD_BALANCER", "NETWORK_LOAD_BALANCER_LISTENER", "VLAN", "ON_PREM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }
        self.attribute_map = {
            'type': 'type'
        }
        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'NETWORK_LOAD_BALANCER_LISTENER':
            return 'NetworkLoadBalancerListenerEndpoint'

        if type == 'COMPUTE_INSTANCE':
            return 'ComputeInstanceEndpoint'

        if type == 'NETWORK_LOAD_BALANCER':
            return 'NetworkLoadBalancerEndpoint'

        if type == 'ON_PREM':
            return 'OnPremEndpoint'

        if type == 'LOAD_BALANCER':
            return 'LoadBalancerEndpoint'

        if type == 'VNIC':
            return 'VnicEndpoint'

        if type == 'IP_ADDRESS':
            return 'IpAddressEndpoint'

        if type == 'VLAN':
            return 'VlanEndpoint'

        if type == 'SUBNET':
            return 'SubnetEndpoint'

        if type == 'LOAD_BALANCER_LISTENER':
            return 'LoadBalancerListenerEndpoint'
        else:
            return 'Endpoint'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Endpoint.
        The type of the `Endpoint`.

        Allowed values for this property are: "IP_ADDRESS", "SUBNET", "COMPUTE_INSTANCE", "VNIC", "LOAD_BALANCER", "LOAD_BALANCER_LISTENER", "NETWORK_LOAD_BALANCER", "NETWORK_LOAD_BALANCER_LISTENER", "VLAN", "ON_PREM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Endpoint.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Endpoint.
        The type of the `Endpoint`.


        :param type: The type of this Endpoint.
        :type: str
        """
        allowed_values = ["IP_ADDRESS", "SUBNET", "COMPUTE_INSTANCE", "VNIC", "LOAD_BALANCER", "LOAD_BALANCER_LISTENER", "NETWORK_LOAD_BALANCER", "NETWORK_LOAD_BALANCER_LISTENER", "VLAN", "ON_PREM"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
