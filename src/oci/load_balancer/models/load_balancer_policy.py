# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoadBalancerPolicy(object):
    """
    A policy that determines how traffic is distributed among backend servers.
    For more information on load balancing policies, see
    `How Load Balancing Policies Work`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Balance/Reference/lbpolicies.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LoadBalancerPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this LoadBalancerPolicy.
        :type name: str

        """
        self.swagger_types = {
            'name': 'str'
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this LoadBalancerPolicy.
        The name of a load balancing policy.

        Example: 'LEAST_CONNECTIONS'


        :return: The name of this LoadBalancerPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LoadBalancerPolicy.
        The name of a load balancing policy.

        Example: 'LEAST_CONNECTIONS'


        :param name: The name of this LoadBalancerPolicy.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
