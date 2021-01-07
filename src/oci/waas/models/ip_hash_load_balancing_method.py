# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .load_balancing_method import LoadBalancingMethod
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IPHashLoadBalancingMethod(LoadBalancingMethod):
    """
    An object that represents the `ip-hash` load balancing method.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IPHashLoadBalancingMethod object with values from keyword arguments. The default value of the :py:attr:`~oci.waas.models.IPHashLoadBalancingMethod.method` attribute
        of this class is ``IP_HASH`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param method:
            The value to assign to the method property of this IPHashLoadBalancingMethod.
            Allowed values for this property are: "IP_HASH", "ROUND_ROBIN", "STICKY_COOKIE"
        :type method: str

        """
        self.swagger_types = {
            'method': 'str'
        }

        self.attribute_map = {
            'method': 'method'
        }

        self._method = None
        self._method = 'IP_HASH'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
