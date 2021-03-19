# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstancePool(object):
    """
    An instance pool is a set of instances within the same region that are managed as a group.
    For more information about instance pools and instance configurations, see
    `Managing Compute Instances`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Compute/Concepts/instancemanagement.htm
    """

    #: A constant which can be used with the lifecycle_state property of a InstancePool.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a InstancePool.
    #: This constant has a value of "SCALING"
    LIFECYCLE_STATE_SCALING = "SCALING"

    #: A constant which can be used with the lifecycle_state property of a InstancePool.
    #: This constant has a value of "STARTING"
    LIFECYCLE_STATE_STARTING = "STARTING"

    #: A constant which can be used with the lifecycle_state property of a InstancePool.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_state property of a InstancePool.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a InstancePool.
    #: This constant has a value of "STOPPED"
    LIFECYCLE_STATE_STOPPED = "STOPPED"

    #: A constant which can be used with the lifecycle_state property of a InstancePool.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a InstancePool.
    #: This constant has a value of "RUNNING"
    LIFECYCLE_STATE_RUNNING = "RUNNING"

    def __init__(self, **kwargs):
        """
        Initializes a new InstancePool object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this InstancePool.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this InstancePool.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this InstancePool.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this InstancePool.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this InstancePool.
        :type freeform_tags: dict(str, str)

        :param instance_configuration_id:
            The value to assign to the instance_configuration_id property of this InstancePool.
        :type instance_configuration_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this InstancePool.
            Allowed values for this property are: "PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param placement_configurations:
            The value to assign to the placement_configurations property of this InstancePool.
        :type placement_configurations: list[oci.core.models.InstancePoolPlacementConfiguration]

        :param size:
            The value to assign to the size property of this InstancePool.
        :type size: int

        :param time_created:
            The value to assign to the time_created property of this InstancePool.
        :type time_created: datetime

        :param load_balancers:
            The value to assign to the load_balancers property of this InstancePool.
        :type load_balancers: list[oci.core.models.InstancePoolLoadBalancerAttachment]

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'instance_configuration_id': 'str',
            'lifecycle_state': 'str',
            'placement_configurations': 'list[InstancePoolPlacementConfiguration]',
            'size': 'int',
            'time_created': 'datetime',
            'load_balancers': 'list[InstancePoolLoadBalancerAttachment]'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'instance_configuration_id': 'instanceConfigurationId',
            'lifecycle_state': 'lifecycleState',
            'placement_configurations': 'placementConfigurations',
            'size': 'size',
            'time_created': 'timeCreated',
            'load_balancers': 'loadBalancers'
        }

        self._id = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._instance_configuration_id = None
        self._lifecycle_state = None
        self._placement_configurations = None
        self._size = None
        self._time_created = None
        self._load_balancers = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this InstancePool.
        The `OCID`__ of the instance pool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this InstancePool.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InstancePool.
        The `OCID`__ of the instance pool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this InstancePool.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this InstancePool.
        The `OCID`__ of the compartment containing the instance
        pool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this InstancePool.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this InstancePool.
        The `OCID`__ of the compartment containing the instance
        pool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this InstancePool.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this InstancePool.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this InstancePool.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this InstancePool.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this InstancePool.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this InstancePool.
        The user-friendly name. Does not have to be unique.


        :return: The display_name of this InstancePool.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstancePool.
        The user-friendly name. Does not have to be unique.


        :param display_name: The display_name of this InstancePool.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this InstancePool.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this InstancePool.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this InstancePool.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this InstancePool.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def instance_configuration_id(self):
        """
        **[Required]** Gets the instance_configuration_id of this InstancePool.
        The `OCID`__ of the instance configuration associated
        with the instance pool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The instance_configuration_id of this InstancePool.
        :rtype: str
        """
        return self._instance_configuration_id

    @instance_configuration_id.setter
    def instance_configuration_id(self, instance_configuration_id):
        """
        Sets the instance_configuration_id of this InstancePool.
        The `OCID`__ of the instance configuration associated
        with the instance pool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param instance_configuration_id: The instance_configuration_id of this InstancePool.
        :type: str
        """
        self._instance_configuration_id = instance_configuration_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this InstancePool.
        The current state of the instance pool.

        Allowed values for this property are: "PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this InstancePool.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this InstancePool.
        The current state of the instance pool.


        :param lifecycle_state: The lifecycle_state of this InstancePool.
        :type: str
        """
        allowed_values = ["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def placement_configurations(self):
        """
        **[Required]** Gets the placement_configurations of this InstancePool.
        The placement configurations for the instance pool.


        :return: The placement_configurations of this InstancePool.
        :rtype: list[oci.core.models.InstancePoolPlacementConfiguration]
        """
        return self._placement_configurations

    @placement_configurations.setter
    def placement_configurations(self, placement_configurations):
        """
        Sets the placement_configurations of this InstancePool.
        The placement configurations for the instance pool.


        :param placement_configurations: The placement_configurations of this InstancePool.
        :type: list[oci.core.models.InstancePoolPlacementConfiguration]
        """
        self._placement_configurations = placement_configurations

    @property
    def size(self):
        """
        **[Required]** Gets the size of this InstancePool.
        The number of instances that should be in the instance pool.


        :return: The size of this InstancePool.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this InstancePool.
        The number of instances that should be in the instance pool.


        :param size: The size of this InstancePool.
        :type: int
        """
        self._size = size

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this InstancePool.
        The date and time the instance pool was created, in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this InstancePool.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this InstancePool.
        The date and time the instance pool was created, in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this InstancePool.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def load_balancers(self):
        """
        Gets the load_balancers of this InstancePool.
        The load balancers attached to the instance pool.


        :return: The load_balancers of this InstancePool.
        :rtype: list[oci.core.models.InstancePoolLoadBalancerAttachment]
        """
        return self._load_balancers

    @load_balancers.setter
    def load_balancers(self, load_balancers):
        """
        Sets the load_balancers of this InstancePool.
        The load balancers attached to the instance pool.


        :param load_balancers: The load_balancers of this InstancePool.
        :type: list[oci.core.models.InstancePoolLoadBalancerAttachment]
        """
        self._load_balancers = load_balancers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
