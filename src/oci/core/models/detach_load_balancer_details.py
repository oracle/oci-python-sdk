# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetachLoadBalancerDetails(object):
    """
    Represents a load balancer that is to be detached from an instance pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DetachLoadBalancerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param load_balancer_id:
            The value to assign to the load_balancer_id property of this DetachLoadBalancerDetails.
        :type load_balancer_id: str

        :param backend_set_name:
            The value to assign to the backend_set_name property of this DetachLoadBalancerDetails.
        :type backend_set_name: str

        """
        self.swagger_types = {
            'load_balancer_id': 'str',
            'backend_set_name': 'str'
        }

        self.attribute_map = {
            'load_balancer_id': 'loadBalancerId',
            'backend_set_name': 'backendSetName'
        }

        self._load_balancer_id = None
        self._backend_set_name = None

    @property
    def load_balancer_id(self):
        """
        **[Required]** Gets the load_balancer_id of this DetachLoadBalancerDetails.
        The OCID of the load balancer to detach from the instance pool.


        :return: The load_balancer_id of this DetachLoadBalancerDetails.
        :rtype: str
        """
        return self._load_balancer_id

    @load_balancer_id.setter
    def load_balancer_id(self, load_balancer_id):
        """
        Sets the load_balancer_id of this DetachLoadBalancerDetails.
        The OCID of the load balancer to detach from the instance pool.


        :param load_balancer_id: The load_balancer_id of this DetachLoadBalancerDetails.
        :type: str
        """
        self._load_balancer_id = load_balancer_id

    @property
    def backend_set_name(self):
        """
        **[Required]** Gets the backend_set_name of this DetachLoadBalancerDetails.
        The name of the backend set on the load balancer to detach from the instance pool.


        :return: The backend_set_name of this DetachLoadBalancerDetails.
        :rtype: str
        """
        return self._backend_set_name

    @backend_set_name.setter
    def backend_set_name(self, backend_set_name):
        """
        Sets the backend_set_name of this DetachLoadBalancerDetails.
        The name of the backend set on the load balancer to detach from the instance pool.


        :param backend_set_name: The backend_set_name of this DetachLoadBalancerDetails.
        :type: str
        """
        self._backend_set_name = backend_set_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
