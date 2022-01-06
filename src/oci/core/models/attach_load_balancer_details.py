# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachLoadBalancerDetails(object):
    """
    Represents a load balancer that is to be attached to an instance pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AttachLoadBalancerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param load_balancer_id:
            The value to assign to the load_balancer_id property of this AttachLoadBalancerDetails.
        :type load_balancer_id: str

        :param backend_set_name:
            The value to assign to the backend_set_name property of this AttachLoadBalancerDetails.
        :type backend_set_name: str

        :param port:
            The value to assign to the port property of this AttachLoadBalancerDetails.
        :type port: int

        :param vnic_selection:
            The value to assign to the vnic_selection property of this AttachLoadBalancerDetails.
        :type vnic_selection: str

        """
        self.swagger_types = {
            'load_balancer_id': 'str',
            'backend_set_name': 'str',
            'port': 'int',
            'vnic_selection': 'str'
        }

        self.attribute_map = {
            'load_balancer_id': 'loadBalancerId',
            'backend_set_name': 'backendSetName',
            'port': 'port',
            'vnic_selection': 'vnicSelection'
        }

        self._load_balancer_id = None
        self._backend_set_name = None
        self._port = None
        self._vnic_selection = None

    @property
    def load_balancer_id(self):
        """
        **[Required]** Gets the load_balancer_id of this AttachLoadBalancerDetails.
        The `OCID`__ of the load balancer to attach to the instance pool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The load_balancer_id of this AttachLoadBalancerDetails.
        :rtype: str
        """
        return self._load_balancer_id

    @load_balancer_id.setter
    def load_balancer_id(self, load_balancer_id):
        """
        Sets the load_balancer_id of this AttachLoadBalancerDetails.
        The `OCID`__ of the load balancer to attach to the instance pool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param load_balancer_id: The load_balancer_id of this AttachLoadBalancerDetails.
        :type: str
        """
        self._load_balancer_id = load_balancer_id

    @property
    def backend_set_name(self):
        """
        **[Required]** Gets the backend_set_name of this AttachLoadBalancerDetails.
        The name of the backend set on the load balancer to add instances to.


        :return: The backend_set_name of this AttachLoadBalancerDetails.
        :rtype: str
        """
        return self._backend_set_name

    @backend_set_name.setter
    def backend_set_name(self, backend_set_name):
        """
        Sets the backend_set_name of this AttachLoadBalancerDetails.
        The name of the backend set on the load balancer to add instances to.


        :param backend_set_name: The backend_set_name of this AttachLoadBalancerDetails.
        :type: str
        """
        self._backend_set_name = backend_set_name

    @property
    def port(self):
        """
        **[Required]** Gets the port of this AttachLoadBalancerDetails.
        The port value to use when creating the backend set.


        :return: The port of this AttachLoadBalancerDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this AttachLoadBalancerDetails.
        The port value to use when creating the backend set.


        :param port: The port of this AttachLoadBalancerDetails.
        :type: int
        """
        self._port = port

    @property
    def vnic_selection(self):
        """
        **[Required]** Gets the vnic_selection of this AttachLoadBalancerDetails.
        Indicates which VNIC on each instance in the pool should be used to associate with the load balancer.
        Possible values are \"PrimaryVnic\" or the displayName of one of the secondary VNICs on the instance configuration
        that is associated with the instance pool.


        :return: The vnic_selection of this AttachLoadBalancerDetails.
        :rtype: str
        """
        return self._vnic_selection

    @vnic_selection.setter
    def vnic_selection(self, vnic_selection):
        """
        Sets the vnic_selection of this AttachLoadBalancerDetails.
        Indicates which VNIC on each instance in the pool should be used to associate with the load balancer.
        Possible values are \"PrimaryVnic\" or the displayName of one of the secondary VNICs on the instance configuration
        that is associated with the instance pool.


        :param vnic_selection: The vnic_selection of this AttachLoadBalancerDetails.
        :type: str
        """
        self._vnic_selection = vnic_selection

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
