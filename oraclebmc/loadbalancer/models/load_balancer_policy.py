# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class LoadBalancerPolicy(object):

    def __init__(self):

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
        Gets the name of this LoadBalancerPolicy.
        The name of the load balancing policy.


        :return: The name of this LoadBalancerPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LoadBalancerPolicy.
        The name of the load balancing policy.


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
