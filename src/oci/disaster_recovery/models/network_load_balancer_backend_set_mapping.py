# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkLoadBalancerBackendSetMapping(object):
    """
    A backend set mapping between source and destination network load balancer.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkLoadBalancerBackendSetMapping object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_backend_set_for_non_movable:
            The value to assign to the is_backend_set_for_non_movable property of this NetworkLoadBalancerBackendSetMapping.
        :type is_backend_set_for_non_movable: bool

        :param source_backend_set_name:
            The value to assign to the source_backend_set_name property of this NetworkLoadBalancerBackendSetMapping.
        :type source_backend_set_name: str

        :param destination_backend_set_name:
            The value to assign to the destination_backend_set_name property of this NetworkLoadBalancerBackendSetMapping.
        :type destination_backend_set_name: str

        """
        self.swagger_types = {
            'is_backend_set_for_non_movable': 'bool',
            'source_backend_set_name': 'str',
            'destination_backend_set_name': 'str'
        }

        self.attribute_map = {
            'is_backend_set_for_non_movable': 'isBackendSetForNonMovable',
            'source_backend_set_name': 'sourceBackendSetName',
            'destination_backend_set_name': 'destinationBackendSetName'
        }

        self._is_backend_set_for_non_movable = None
        self._source_backend_set_name = None
        self._destination_backend_set_name = None

    @property
    def is_backend_set_for_non_movable(self):
        """
        **[Required]** Gets the is_backend_set_for_non_movable of this NetworkLoadBalancerBackendSetMapping.
        This flag specifies if this backend set is used for traffic for non-movable compute instances.
        Backend sets that point to non-movable instances are only enabled or disabled during DR. For non-movable instances this flag should be set to 'true'.
        Backend sets that point to movable instances are emptied and their contents are transferred to the destination region network load balancer.  For movable instances this flag should be set to 'false'.

        Example: `true`


        :return: The is_backend_set_for_non_movable of this NetworkLoadBalancerBackendSetMapping.
        :rtype: bool
        """
        return self._is_backend_set_for_non_movable

    @is_backend_set_for_non_movable.setter
    def is_backend_set_for_non_movable(self, is_backend_set_for_non_movable):
        """
        Sets the is_backend_set_for_non_movable of this NetworkLoadBalancerBackendSetMapping.
        This flag specifies if this backend set is used for traffic for non-movable compute instances.
        Backend sets that point to non-movable instances are only enabled or disabled during DR. For non-movable instances this flag should be set to 'true'.
        Backend sets that point to movable instances are emptied and their contents are transferred to the destination region network load balancer.  For movable instances this flag should be set to 'false'.

        Example: `true`


        :param is_backend_set_for_non_movable: The is_backend_set_for_non_movable of this NetworkLoadBalancerBackendSetMapping.
        :type: bool
        """
        self._is_backend_set_for_non_movable = is_backend_set_for_non_movable

    @property
    def source_backend_set_name(self):
        """
        **[Required]** Gets the source_backend_set_name of this NetworkLoadBalancerBackendSetMapping.
        The name of the source backend set.

        Example: `example_backend_set`


        :return: The source_backend_set_name of this NetworkLoadBalancerBackendSetMapping.
        :rtype: str
        """
        return self._source_backend_set_name

    @source_backend_set_name.setter
    def source_backend_set_name(self, source_backend_set_name):
        """
        Sets the source_backend_set_name of this NetworkLoadBalancerBackendSetMapping.
        The name of the source backend set.

        Example: `example_backend_set`


        :param source_backend_set_name: The source_backend_set_name of this NetworkLoadBalancerBackendSetMapping.
        :type: str
        """
        self._source_backend_set_name = source_backend_set_name

    @property
    def destination_backend_set_name(self):
        """
        **[Required]** Gets the destination_backend_set_name of this NetworkLoadBalancerBackendSetMapping.
        The name of the destination backend set.

        Example: `example_backend_set`


        :return: The destination_backend_set_name of this NetworkLoadBalancerBackendSetMapping.
        :rtype: str
        """
        return self._destination_backend_set_name

    @destination_backend_set_name.setter
    def destination_backend_set_name(self, destination_backend_set_name):
        """
        Sets the destination_backend_set_name of this NetworkLoadBalancerBackendSetMapping.
        The name of the destination backend set.

        Example: `example_backend_set`


        :param destination_backend_set_name: The destination_backend_set_name of this NetworkLoadBalancerBackendSetMapping.
        :type: str
        """
        self._destination_backend_set_name = destination_backend_set_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
