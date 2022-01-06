# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstancePoolInstance(object):
    """
    Information about an instance that belongs to an instance pool.
    """

    #: A constant which can be used with the lifecycle_state property of a InstancePoolInstance.
    #: This constant has a value of "ATTACHING"
    LIFECYCLE_STATE_ATTACHING = "ATTACHING"

    #: A constant which can be used with the lifecycle_state property of a InstancePoolInstance.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a InstancePoolInstance.
    #: This constant has a value of "DETACHING"
    LIFECYCLE_STATE_DETACHING = "DETACHING"

    def __init__(self, **kwargs):
        """
        Initializes a new InstancePoolInstance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this InstancePoolInstance.
        :type id: str

        :param instance_pool_id:
            The value to assign to the instance_pool_id property of this InstancePoolInstance.
        :type instance_pool_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this InstancePoolInstance.
        :type availability_domain: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this InstancePoolInstance.
            Allowed values for this property are: "ATTACHING", "ACTIVE", "DETACHING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param compartment_id:
            The value to assign to the compartment_id property of this InstancePoolInstance.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this InstancePoolInstance.
        :type display_name: str

        :param fault_domain:
            The value to assign to the fault_domain property of this InstancePoolInstance.
        :type fault_domain: str

        :param instance_configuration_id:
            The value to assign to the instance_configuration_id property of this InstancePoolInstance.
        :type instance_configuration_id: str

        :param region:
            The value to assign to the region property of this InstancePoolInstance.
        :type region: str

        :param shape:
            The value to assign to the shape property of this InstancePoolInstance.
        :type shape: str

        :param state:
            The value to assign to the state property of this InstancePoolInstance.
        :type state: str

        :param time_created:
            The value to assign to the time_created property of this InstancePoolInstance.
        :type time_created: datetime

        :param load_balancer_backends:
            The value to assign to the load_balancer_backends property of this InstancePoolInstance.
        :type load_balancer_backends: list[oci.core.models.InstancePoolInstanceLoadBalancerBackend]

        """
        self.swagger_types = {
            'id': 'str',
            'instance_pool_id': 'str',
            'availability_domain': 'str',
            'lifecycle_state': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'fault_domain': 'str',
            'instance_configuration_id': 'str',
            'region': 'str',
            'shape': 'str',
            'state': 'str',
            'time_created': 'datetime',
            'load_balancer_backends': 'list[InstancePoolInstanceLoadBalancerBackend]'
        }

        self.attribute_map = {
            'id': 'id',
            'instance_pool_id': 'instancePoolId',
            'availability_domain': 'availabilityDomain',
            'lifecycle_state': 'lifecycleState',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'fault_domain': 'faultDomain',
            'instance_configuration_id': 'instanceConfigurationId',
            'region': 'region',
            'shape': 'shape',
            'state': 'state',
            'time_created': 'timeCreated',
            'load_balancer_backends': 'loadBalancerBackends'
        }

        self._id = None
        self._instance_pool_id = None
        self._availability_domain = None
        self._lifecycle_state = None
        self._compartment_id = None
        self._display_name = None
        self._fault_domain = None
        self._instance_configuration_id = None
        self._region = None
        self._shape = None
        self._state = None
        self._time_created = None
        self._load_balancer_backends = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this InstancePoolInstance.
        The `OCID`__ of the instance.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this InstancePoolInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InstancePoolInstance.
        The `OCID`__ of the instance.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this InstancePoolInstance.
        :type: str
        """
        self._id = id

    @property
    def instance_pool_id(self):
        """
        **[Required]** Gets the instance_pool_id of this InstancePoolInstance.
        The `OCID`__ of the instance pool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The instance_pool_id of this InstancePoolInstance.
        :rtype: str
        """
        return self._instance_pool_id

    @instance_pool_id.setter
    def instance_pool_id(self, instance_pool_id):
        """
        Sets the instance_pool_id of this InstancePoolInstance.
        The `OCID`__ of the instance pool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param instance_pool_id: The instance_pool_id of this InstancePoolInstance.
        :type: str
        """
        self._instance_pool_id = instance_pool_id

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this InstancePoolInstance.
        The availability domain the instance is running in.


        :return: The availability_domain of this InstancePoolInstance.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this InstancePoolInstance.
        The availability domain the instance is running in.


        :param availability_domain: The availability_domain of this InstancePoolInstance.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this InstancePoolInstance.
        The attachment state of the instance in relation to the instance pool.

        Allowed values for this property are: "ATTACHING", "ACTIVE", "DETACHING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this InstancePoolInstance.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this InstancePoolInstance.
        The attachment state of the instance in relation to the instance pool.


        :param lifecycle_state: The lifecycle_state of this InstancePoolInstance.
        :type: str
        """
        allowed_values = ["ATTACHING", "ACTIVE", "DETACHING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this InstancePoolInstance.
        The `OCID`__ of the compartment that contains the
        instance.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this InstancePoolInstance.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this InstancePoolInstance.
        The `OCID`__ of the compartment that contains the
        instance.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this InstancePoolInstance.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this InstancePoolInstance.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this InstancePoolInstance.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstancePoolInstance.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this InstancePoolInstance.
        :type: str
        """
        self._display_name = display_name

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this InstancePoolInstance.
        The fault domain the instance is running in.


        :return: The fault_domain of this InstancePoolInstance.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this InstancePoolInstance.
        The fault domain the instance is running in.


        :param fault_domain: The fault_domain of this InstancePoolInstance.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def instance_configuration_id(self):
        """
        **[Required]** Gets the instance_configuration_id of this InstancePoolInstance.
        The `OCID`__ of the instance configuration
        used to create the instance.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The instance_configuration_id of this InstancePoolInstance.
        :rtype: str
        """
        return self._instance_configuration_id

    @instance_configuration_id.setter
    def instance_configuration_id(self, instance_configuration_id):
        """
        Sets the instance_configuration_id of this InstancePoolInstance.
        The `OCID`__ of the instance configuration
        used to create the instance.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param instance_configuration_id: The instance_configuration_id of this InstancePoolInstance.
        :type: str
        """
        self._instance_configuration_id = instance_configuration_id

    @property
    def region(self):
        """
        **[Required]** Gets the region of this InstancePoolInstance.
        The region that contains the availability domain the instance is running in.


        :return: The region of this InstancePoolInstance.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this InstancePoolInstance.
        The region that contains the availability domain the instance is running in.


        :param region: The region of this InstancePoolInstance.
        :type: str
        """
        self._region = region

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this InstancePoolInstance.
        The shape of the instance. The shape determines the number of CPUs, amount of memory,
        and other resources allocated to the instance.


        :return: The shape of this InstancePoolInstance.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this InstancePoolInstance.
        The shape of the instance. The shape determines the number of CPUs, amount of memory,
        and other resources allocated to the instance.


        :param shape: The shape of this InstancePoolInstance.
        :type: str
        """
        self._shape = shape

    @property
    def state(self):
        """
        **[Required]** Gets the state of this InstancePoolInstance.
        The lifecycle state of the instance. Refer to `lifecycleState` in the :class:`Instance` resource.


        :return: The state of this InstancePoolInstance.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this InstancePoolInstance.
        The lifecycle state of the instance. Refer to `lifecycleState` in the :class:`Instance` resource.


        :param state: The state of this InstancePoolInstance.
        :type: str
        """
        self._state = state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this InstancePoolInstance.
        The date and time the instance pool instance was created, in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this InstancePoolInstance.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this InstancePoolInstance.
        The date and time the instance pool instance was created, in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this InstancePoolInstance.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def load_balancer_backends(self):
        """
        Gets the load_balancer_backends of this InstancePoolInstance.
        The load balancer backends that are configured for the instance.


        :return: The load_balancer_backends of this InstancePoolInstance.
        :rtype: list[oci.core.models.InstancePoolInstanceLoadBalancerBackend]
        """
        return self._load_balancer_backends

    @load_balancer_backends.setter
    def load_balancer_backends(self, load_balancer_backends):
        """
        Sets the load_balancer_backends of this InstancePoolInstance.
        The load balancer backends that are configured for the instance.


        :param load_balancer_backends: The load_balancer_backends of this InstancePoolInstance.
        :type: list[oci.core.models.InstancePoolInstanceLoadBalancerBackend]
        """
        self._load_balancer_backends = load_balancer_backends

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
