# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20170115


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoadBalancerProtocol(object):
    """
    A protocol that defines the type of traffic accepted by a listener.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LoadBalancerProtocol object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this LoadBalancerProtocol.
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
        **[Required]** Gets the name of this LoadBalancerProtocol.
        The name of a protocol.

        Example: 'HTTP'


        :return: The name of this LoadBalancerProtocol.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LoadBalancerProtocol.
        The name of a protocol.

        Example: 'HTTP'


        :param name: The name of this LoadBalancerProtocol.
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
