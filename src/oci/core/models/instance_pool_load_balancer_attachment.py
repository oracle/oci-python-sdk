# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstancePoolLoadBalancerAttachment(object):
    """
    Represents a load balancer that is attached to an instance pool.
    """

    #: A constant which can be used with the lifecycle_state property of a InstancePoolLoadBalancerAttachment.
    #: This constant has a value of "ATTACHING"
    LIFECYCLE_STATE_ATTACHING = "ATTACHING"

    #: A constant which can be used with the lifecycle_state property of a InstancePoolLoadBalancerAttachment.
    #: This constant has a value of "ATTACHED"
    LIFECYCLE_STATE_ATTACHED = "ATTACHED"

    #: A constant which can be used with the lifecycle_state property of a InstancePoolLoadBalancerAttachment.
    #: This constant has a value of "DETACHING"
    LIFECYCLE_STATE_DETACHING = "DETACHING"

    #: A constant which can be used with the lifecycle_state property of a InstancePoolLoadBalancerAttachment.
    #: This constant has a value of "DETACHED"
    LIFECYCLE_STATE_DETACHED = "DETACHED"

    def __init__(self, **kwargs):
        """
        Initializes a new InstancePoolLoadBalancerAttachment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this InstancePoolLoadBalancerAttachment.
        :type id: str

        :param instance_pool_id:
            The value to assign to the instance_pool_id property of this InstancePoolLoadBalancerAttachment.
        :type instance_pool_id: str

        :param load_balancer_id:
            The value to assign to the load_balancer_id property of this InstancePoolLoadBalancerAttachment.
        :type load_balancer_id: str

        :param backend_set_name:
            The value to assign to the backend_set_name property of this InstancePoolLoadBalancerAttachment.
        :type backend_set_name: str

        :param port:
            The value to assign to the port property of this InstancePoolLoadBalancerAttachment.
        :type port: int

        :param vnic_selection:
            The value to assign to the vnic_selection property of this InstancePoolLoadBalancerAttachment.
        :type vnic_selection: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this InstancePoolLoadBalancerAttachment.
            Allowed values for this property are: "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'instance_pool_id': 'str',
            'load_balancer_id': 'str',
            'backend_set_name': 'str',
            'port': 'int',
            'vnic_selection': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'instance_pool_id': 'instancePoolId',
            'load_balancer_id': 'loadBalancerId',
            'backend_set_name': 'backendSetName',
            'port': 'port',
            'vnic_selection': 'vnicSelection',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._instance_pool_id = None
        self._load_balancer_id = None
        self._backend_set_name = None
        self._port = None
        self._vnic_selection = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this InstancePoolLoadBalancerAttachment.
        The `OCID`__ of the load balancer attachment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this InstancePoolLoadBalancerAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InstancePoolLoadBalancerAttachment.
        The `OCID`__ of the load balancer attachment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this InstancePoolLoadBalancerAttachment.
        :type: str
        """
        self._id = id

    @property
    def instance_pool_id(self):
        """
        **[Required]** Gets the instance_pool_id of this InstancePoolLoadBalancerAttachment.
        The `OCID`__ of the instance pool of the load balancer attachment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The instance_pool_id of this InstancePoolLoadBalancerAttachment.
        :rtype: str
        """
        return self._instance_pool_id

    @instance_pool_id.setter
    def instance_pool_id(self, instance_pool_id):
        """
        Sets the instance_pool_id of this InstancePoolLoadBalancerAttachment.
        The `OCID`__ of the instance pool of the load balancer attachment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param instance_pool_id: The instance_pool_id of this InstancePoolLoadBalancerAttachment.
        :type: str
        """
        self._instance_pool_id = instance_pool_id

    @property
    def load_balancer_id(self):
        """
        **[Required]** Gets the load_balancer_id of this InstancePoolLoadBalancerAttachment.
        The `OCID`__ of the load balancer attached to the instance pool.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The load_balancer_id of this InstancePoolLoadBalancerAttachment.
        :rtype: str
        """
        return self._load_balancer_id

    @load_balancer_id.setter
    def load_balancer_id(self, load_balancer_id):
        """
        Sets the load_balancer_id of this InstancePoolLoadBalancerAttachment.
        The `OCID`__ of the load balancer attached to the instance pool.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param load_balancer_id: The load_balancer_id of this InstancePoolLoadBalancerAttachment.
        :type: str
        """
        self._load_balancer_id = load_balancer_id

    @property
    def backend_set_name(self):
        """
        **[Required]** Gets the backend_set_name of this InstancePoolLoadBalancerAttachment.
        The name of the backend set on the load balancer.


        :return: The backend_set_name of this InstancePoolLoadBalancerAttachment.
        :rtype: str
        """
        return self._backend_set_name

    @backend_set_name.setter
    def backend_set_name(self, backend_set_name):
        """
        Sets the backend_set_name of this InstancePoolLoadBalancerAttachment.
        The name of the backend set on the load balancer.


        :param backend_set_name: The backend_set_name of this InstancePoolLoadBalancerAttachment.
        :type: str
        """
        self._backend_set_name = backend_set_name

    @property
    def port(self):
        """
        **[Required]** Gets the port of this InstancePoolLoadBalancerAttachment.
        The port value used for the backends.


        :return: The port of this InstancePoolLoadBalancerAttachment.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this InstancePoolLoadBalancerAttachment.
        The port value used for the backends.


        :param port: The port of this InstancePoolLoadBalancerAttachment.
        :type: int
        """
        self._port = port

    @property
    def vnic_selection(self):
        """
        **[Required]** Gets the vnic_selection of this InstancePoolLoadBalancerAttachment.
        Indicates which VNIC on each instance in the instance pool should be used to associate with the load balancer. Possible values are \"PrimaryVnic\" or the displayName of one of the secondary VNICs on the instance configuration that is associated with the instance pool.


        :return: The vnic_selection of this InstancePoolLoadBalancerAttachment.
        :rtype: str
        """
        return self._vnic_selection

    @vnic_selection.setter
    def vnic_selection(self, vnic_selection):
        """
        Sets the vnic_selection of this InstancePoolLoadBalancerAttachment.
        Indicates which VNIC on each instance in the instance pool should be used to associate with the load balancer. Possible values are \"PrimaryVnic\" or the displayName of one of the secondary VNICs on the instance configuration that is associated with the instance pool.


        :param vnic_selection: The vnic_selection of this InstancePoolLoadBalancerAttachment.
        :type: str
        """
        self._vnic_selection = vnic_selection

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this InstancePoolLoadBalancerAttachment.
        The status of the interaction between the instance pool and the load balancer.

        Allowed values for this property are: "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this InstancePoolLoadBalancerAttachment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this InstancePoolLoadBalancerAttachment.
        The status of the interaction between the instance pool and the load balancer.


        :param lifecycle_state: The lifecycle_state of this InstancePoolLoadBalancerAttachment.
        :type: str
        """
        allowed_values = ["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
