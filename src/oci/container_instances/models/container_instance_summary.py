# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerInstanceSummary(object):
    """
    A reduced set of details about a single ContainerInstance returned by list APIs.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerInstanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ContainerInstanceSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ContainerInstanceSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ContainerInstanceSummary.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ContainerInstanceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ContainerInstanceSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ContainerInstanceSummary.
        :type system_tags: dict(str, dict(str, object))

        :param availability_domain:
            The value to assign to the availability_domain property of this ContainerInstanceSummary.
        :type availability_domain: str

        :param fault_domain:
            The value to assign to the fault_domain property of this ContainerInstanceSummary.
        :type fault_domain: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ContainerInstanceSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ContainerInstanceSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this ContainerInstanceSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ContainerInstanceSummary.
        :type time_updated: datetime

        :param shape:
            The value to assign to the shape property of this ContainerInstanceSummary.
        :type shape: str

        :param shape_config:
            The value to assign to the shape_config property of this ContainerInstanceSummary.
        :type shape_config: oci.container_instances.models.ContainerInstanceShapeConfig

        :param container_count:
            The value to assign to the container_count property of this ContainerInstanceSummary.
        :type container_count: int

        :param graceful_shutdown_timeout_in_seconds:
            The value to assign to the graceful_shutdown_timeout_in_seconds property of this ContainerInstanceSummary.
        :type graceful_shutdown_timeout_in_seconds: int

        :param volume_count:
            The value to assign to the volume_count property of this ContainerInstanceSummary.
        :type volume_count: int

        :param container_restart_policy:
            The value to assign to the container_restart_policy property of this ContainerInstanceSummary.
        :type container_restart_policy: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'availability_domain': 'str',
            'fault_domain': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'shape': 'str',
            'shape_config': 'ContainerInstanceShapeConfig',
            'container_count': 'int',
            'graceful_shutdown_timeout_in_seconds': 'int',
            'volume_count': 'int',
            'container_restart_policy': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'availability_domain': 'availabilityDomain',
            'fault_domain': 'faultDomain',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'shape': 'shape',
            'shape_config': 'shapeConfig',
            'container_count': 'containerCount',
            'graceful_shutdown_timeout_in_seconds': 'gracefulShutdownTimeoutInSeconds',
            'volume_count': 'volumeCount',
            'container_restart_policy': 'containerRestartPolicy'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._availability_domain = None
        self._fault_domain = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._shape = None
        self._shape_config = None
        self._container_count = None
        self._graceful_shutdown_timeout_in_seconds = None
        self._volume_count = None
        self._container_restart_policy = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ContainerInstanceSummary.
        Unique identifier that is immutable on creation


        :return: The id of this ContainerInstanceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ContainerInstanceSummary.
        Unique identifier that is immutable on creation


        :param id: The id of this ContainerInstanceSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ContainerInstanceSummary.
        Display name for the ContainerInstance. Can be renamed.


        :return: The display_name of this ContainerInstanceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ContainerInstanceSummary.
        Display name for the ContainerInstance. Can be renamed.


        :param display_name: The display_name of this ContainerInstanceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ContainerInstanceSummary.
        Compartment Identifier


        :return: The compartment_id of this ContainerInstanceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ContainerInstanceSummary.
        Compartment Identifier


        :param compartment_id: The compartment_id of this ContainerInstanceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ContainerInstanceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ContainerInstanceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ContainerInstanceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ContainerInstanceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ContainerInstanceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ContainerInstanceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ContainerInstanceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ContainerInstanceSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ContainerInstanceSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ContainerInstanceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ContainerInstanceSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ContainerInstanceSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this ContainerInstanceSummary.
        Availability Domain where the ContainerInstance is running.


        :return: The availability_domain of this ContainerInstanceSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ContainerInstanceSummary.
        Availability Domain where the ContainerInstance is running.


        :param availability_domain: The availability_domain of this ContainerInstanceSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this ContainerInstanceSummary.
        Fault Domain where the ContainerInstance is running.


        :return: The fault_domain of this ContainerInstanceSummary.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this ContainerInstanceSummary.
        Fault Domain where the ContainerInstance is running.


        :param fault_domain: The fault_domain of this ContainerInstanceSummary.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ContainerInstanceSummary.
        The current state of the ContainerInstance.


        :return: The lifecycle_state of this ContainerInstanceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ContainerInstanceSummary.
        The current state of the ContainerInstance.


        :param lifecycle_state: The lifecycle_state of this ContainerInstanceSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ContainerInstanceSummary.
        A message describing the current state in more detail. For example, can be used to provide
        actionable information for a resource in Failed state.


        :return: The lifecycle_details of this ContainerInstanceSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ContainerInstanceSummary.
        A message describing the current state in more detail. For example, can be used to provide
        actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this ContainerInstanceSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ContainerInstanceSummary.
        The time the the ContainerInstance was created. An RFC3339 formatted datetime string


        :return: The time_created of this ContainerInstanceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ContainerInstanceSummary.
        The time the the ContainerInstance was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this ContainerInstanceSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ContainerInstanceSummary.
        The time the ContainerInstance was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this ContainerInstanceSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ContainerInstanceSummary.
        The time the ContainerInstance was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this ContainerInstanceSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this ContainerInstanceSummary.
        The shape of the Container Instance. The shape determines the resources available to the Container Instance.


        :return: The shape of this ContainerInstanceSummary.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this ContainerInstanceSummary.
        The shape of the Container Instance. The shape determines the resources available to the Container Instance.


        :param shape: The shape of this ContainerInstanceSummary.
        :type: str
        """
        self._shape = shape

    @property
    def shape_config(self):
        """
        **[Required]** Gets the shape_config of this ContainerInstanceSummary.

        :return: The shape_config of this ContainerInstanceSummary.
        :rtype: oci.container_instances.models.ContainerInstanceShapeConfig
        """
        return self._shape_config

    @shape_config.setter
    def shape_config(self, shape_config):
        """
        Sets the shape_config of this ContainerInstanceSummary.

        :param shape_config: The shape_config of this ContainerInstanceSummary.
        :type: oci.container_instances.models.ContainerInstanceShapeConfig
        """
        self._shape_config = shape_config

    @property
    def container_count(self):
        """
        **[Required]** Gets the container_count of this ContainerInstanceSummary.
        The number of containers on this Instance


        :return: The container_count of this ContainerInstanceSummary.
        :rtype: int
        """
        return self._container_count

    @container_count.setter
    def container_count(self, container_count):
        """
        Sets the container_count of this ContainerInstanceSummary.
        The number of containers on this Instance


        :param container_count: The container_count of this ContainerInstanceSummary.
        :type: int
        """
        self._container_count = container_count

    @property
    def graceful_shutdown_timeout_in_seconds(self):
        """
        Gets the graceful_shutdown_timeout_in_seconds of this ContainerInstanceSummary.
        Duration in seconds processes within a Container have to gracefully terminate. This applies whenever a Container must be halted, such as when the Container Instance is deleted. Processes will first be sent a termination signal. After this timeout is reached, the processes will be sent a termination signal.


        :return: The graceful_shutdown_timeout_in_seconds of this ContainerInstanceSummary.
        :rtype: int
        """
        return self._graceful_shutdown_timeout_in_seconds

    @graceful_shutdown_timeout_in_seconds.setter
    def graceful_shutdown_timeout_in_seconds(self, graceful_shutdown_timeout_in_seconds):
        """
        Sets the graceful_shutdown_timeout_in_seconds of this ContainerInstanceSummary.
        Duration in seconds processes within a Container have to gracefully terminate. This applies whenever a Container must be halted, such as when the Container Instance is deleted. Processes will first be sent a termination signal. After this timeout is reached, the processes will be sent a termination signal.


        :param graceful_shutdown_timeout_in_seconds: The graceful_shutdown_timeout_in_seconds of this ContainerInstanceSummary.
        :type: int
        """
        self._graceful_shutdown_timeout_in_seconds = graceful_shutdown_timeout_in_seconds

    @property
    def volume_count(self):
        """
        Gets the volume_count of this ContainerInstanceSummary.
        The number of volumes that attached to this Instance


        :return: The volume_count of this ContainerInstanceSummary.
        :rtype: int
        """
        return self._volume_count

    @volume_count.setter
    def volume_count(self, volume_count):
        """
        Sets the volume_count of this ContainerInstanceSummary.
        The number of volumes that attached to this Instance


        :param volume_count: The volume_count of this ContainerInstanceSummary.
        :type: int
        """
        self._volume_count = volume_count

    @property
    def container_restart_policy(self):
        """
        **[Required]** Gets the container_restart_policy of this ContainerInstanceSummary.
        Container Restart Policy


        :return: The container_restart_policy of this ContainerInstanceSummary.
        :rtype: str
        """
        return self._container_restart_policy

    @container_restart_policy.setter
    def container_restart_policy(self, container_restart_policy):
        """
        Sets the container_restart_policy of this ContainerInstanceSummary.
        Container Restart Policy


        :param container_restart_policy: The container_restart_policy of this ContainerInstanceSummary.
        :type: str
        """
        self._container_restart_policy = container_restart_policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
