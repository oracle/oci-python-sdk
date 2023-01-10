# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Container(object):
    """
    A single container on a Container Instance.

    If this Container is DELETED, the record will remain visible for a short period
    of time before being permanently removed.
    """

    #: A constant which can be used with the lifecycle_state property of a Container.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Container.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Container.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Container.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Container.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Container.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Container.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the additional_capabilities property of a Container.
    #: This constant has a value of "CAP_NET_ADMIN"
    ADDITIONAL_CAPABILITIES_CAP_NET_ADMIN = "CAP_NET_ADMIN"

    #: A constant which can be used with the additional_capabilities property of a Container.
    #: This constant has a value of "CAP_NET_RAW"
    ADDITIONAL_CAPABILITIES_CAP_NET_RAW = "CAP_NET_RAW"

    def __init__(self, **kwargs):
        """
        Initializes a new Container object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Container.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Container.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Container.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Container.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Container.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Container.
        :type system_tags: dict(str, dict(str, object))

        :param availability_domain:
            The value to assign to the availability_domain property of this Container.
        :type availability_domain: str

        :param fault_domain:
            The value to assign to the fault_domain property of this Container.
        :type fault_domain: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Container.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Container.
        :type lifecycle_details: str

        :param exit_code:
            The value to assign to the exit_code property of this Container.
        :type exit_code: int

        :param time_terminated:
            The value to assign to the time_terminated property of this Container.
        :type time_terminated: datetime

        :param time_created:
            The value to assign to the time_created property of this Container.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Container.
        :type time_updated: datetime

        :param container_instance_id:
            The value to assign to the container_instance_id property of this Container.
        :type container_instance_id: str

        :param image_url:
            The value to assign to the image_url property of this Container.
        :type image_url: str

        :param command:
            The value to assign to the command property of this Container.
        :type command: list[str]

        :param arguments:
            The value to assign to the arguments property of this Container.
        :type arguments: list[str]

        :param additional_capabilities:
            The value to assign to the additional_capabilities property of this Container.
            Allowed values for items in this list are: "CAP_NET_ADMIN", "CAP_NET_RAW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type additional_capabilities: list[str]

        :param working_directory:
            The value to assign to the working_directory property of this Container.
        :type working_directory: str

        :param environment_variables:
            The value to assign to the environment_variables property of this Container.
        :type environment_variables: dict(str, str)

        :param volume_mounts:
            The value to assign to the volume_mounts property of this Container.
        :type volume_mounts: list[oci.container_instances.models.VolumeMount]

        :param health_checks:
            The value to assign to the health_checks property of this Container.
        :type health_checks: list[oci.container_instances.models.ContainerHealthCheck]

        :param is_resource_principal_disabled:
            The value to assign to the is_resource_principal_disabled property of this Container.
        :type is_resource_principal_disabled: bool

        :param resource_config:
            The value to assign to the resource_config property of this Container.
        :type resource_config: oci.container_instances.models.ContainerResourceConfig

        :param container_restart_attempt_count:
            The value to assign to the container_restart_attempt_count property of this Container.
        :type container_restart_attempt_count: int

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
            'exit_code': 'int',
            'time_terminated': 'datetime',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'container_instance_id': 'str',
            'image_url': 'str',
            'command': 'list[str]',
            'arguments': 'list[str]',
            'additional_capabilities': 'list[str]',
            'working_directory': 'str',
            'environment_variables': 'dict(str, str)',
            'volume_mounts': 'list[VolumeMount]',
            'health_checks': 'list[ContainerHealthCheck]',
            'is_resource_principal_disabled': 'bool',
            'resource_config': 'ContainerResourceConfig',
            'container_restart_attempt_count': 'int'
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
            'exit_code': 'exitCode',
            'time_terminated': 'timeTerminated',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'container_instance_id': 'containerInstanceId',
            'image_url': 'imageUrl',
            'command': 'command',
            'arguments': 'arguments',
            'additional_capabilities': 'additionalCapabilities',
            'working_directory': 'workingDirectory',
            'environment_variables': 'environmentVariables',
            'volume_mounts': 'volumeMounts',
            'health_checks': 'healthChecks',
            'is_resource_principal_disabled': 'isResourcePrincipalDisabled',
            'resource_config': 'resourceConfig',
            'container_restart_attempt_count': 'containerRestartAttemptCount'
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
        self._exit_code = None
        self._time_terminated = None
        self._time_created = None
        self._time_updated = None
        self._container_instance_id = None
        self._image_url = None
        self._command = None
        self._arguments = None
        self._additional_capabilities = None
        self._working_directory = None
        self._environment_variables = None
        self._volume_mounts = None
        self._health_checks = None
        self._is_resource_principal_disabled = None
        self._resource_config = None
        self._container_restart_attempt_count = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Container.
        Unique identifier that is immutable on creation


        :return: The id of this Container.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Container.
        Unique identifier that is immutable on creation


        :param id: The id of this Container.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Container.
        Display name for the Container. Can be renamed.


        :return: The display_name of this Container.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Container.
        Display name for the Container. Can be renamed.


        :param display_name: The display_name of this Container.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Container.
        Compartment Identifier


        :return: The compartment_id of this Container.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Container.
        Compartment Identifier


        :param compartment_id: The compartment_id of this Container.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Container.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Container.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Container.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Container.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Container.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Container.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Container.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Container.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Container.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this Container.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Container.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this Container.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this Container.
        Availability Domain where the Container's Instance is running.


        :return: The availability_domain of this Container.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Container.
        Availability Domain where the Container's Instance is running.


        :param availability_domain: The availability_domain of this Container.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this Container.
        Fault Domain where the Container's Instance is running.


        :return: The fault_domain of this Container.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this Container.
        Fault Domain where the Container's Instance is running.


        :param fault_domain: The fault_domain of this Container.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Container.
        The current state of the Container.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Container.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Container.
        The current state of the Container.


        :param lifecycle_state: The lifecycle_state of this Container.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Container.
        A message describing the current state in more detail. For example, can be used to provide
        actionable information for a resource in Failed state.


        :return: The lifecycle_details of this Container.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Container.
        A message describing the current state in more detail. For example, can be used to provide
        actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this Container.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def exit_code(self):
        """
        Gets the exit_code of this Container.
        The exit code of the container process if it has stopped executing.


        :return: The exit_code of this Container.
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """
        Sets the exit_code of this Container.
        The exit code of the container process if it has stopped executing.


        :param exit_code: The exit_code of this Container.
        :type: int
        """
        self._exit_code = exit_code

    @property
    def time_terminated(self):
        """
        Gets the time_terminated of this Container.
        Time at which the container last terminated. An RFC3339 formatted datetime string


        :return: The time_terminated of this Container.
        :rtype: datetime
        """
        return self._time_terminated

    @time_terminated.setter
    def time_terminated(self, time_terminated):
        """
        Sets the time_terminated of this Container.
        Time at which the container last terminated. An RFC3339 formatted datetime string


        :param time_terminated: The time_terminated of this Container.
        :type: datetime
        """
        self._time_terminated = time_terminated

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Container.
        The time the the Container was created. An RFC3339 formatted datetime string


        :return: The time_created of this Container.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Container.
        The time the the Container was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this Container.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Container.
        The time the Container was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this Container.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Container.
        The time the Container was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this Container.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def container_instance_id(self):
        """
        **[Required]** Gets the container_instance_id of this Container.
        The identifier of the Container Instance on which this container is running.


        :return: The container_instance_id of this Container.
        :rtype: str
        """
        return self._container_instance_id

    @container_instance_id.setter
    def container_instance_id(self, container_instance_id):
        """
        Sets the container_instance_id of this Container.
        The identifier of the Container Instance on which this container is running.


        :param container_instance_id: The container_instance_id of this Container.
        :type: str
        """
        self._container_instance_id = container_instance_id

    @property
    def image_url(self):
        """
        **[Required]** Gets the image_url of this Container.
        The container image information. Currently only support public docker registry. Can be either image name,
        e.g `containerImage`, image name with version, e.g `containerImage:v1` or complete docker image Url e.g
        `docker.io/library/containerImage:latest`.
        If no registry is provided, will default the registry to public docker hub `docker.io/library`.
        The registry used for container image must be reachable over the Container Instance's VNIC.


        :return: The image_url of this Container.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """
        Sets the image_url of this Container.
        The container image information. Currently only support public docker registry. Can be either image name,
        e.g `containerImage`, image name with version, e.g `containerImage:v1` or complete docker image Url e.g
        `docker.io/library/containerImage:latest`.
        If no registry is provided, will default the registry to public docker hub `docker.io/library`.
        The registry used for container image must be reachable over the Container Instance's VNIC.


        :param image_url: The image_url of this Container.
        :type: str
        """
        self._image_url = image_url

    @property
    def command(self):
        """
        Gets the command of this Container.
        This command will override the container's entrypoint process.
        If not specified, the existing entrypoint process defined in the image will be used.


        :return: The command of this Container.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this Container.
        This command will override the container's entrypoint process.
        If not specified, the existing entrypoint process defined in the image will be used.


        :param command: The command of this Container.
        :type: list[str]
        """
        self._command = command

    @property
    def arguments(self):
        """
        Gets the arguments of this Container.
        A list of string arguments for a Container's entrypoint process.

        Many containers use an entrypoint process pointing to a shell,
        for example /bin/bash. For such containers, this argument list
        can also be used to specify the main command in the container process.


        :return: The arguments of this Container.
        :rtype: list[str]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """
        Sets the arguments of this Container.
        A list of string arguments for a Container's entrypoint process.

        Many containers use an entrypoint process pointing to a shell,
        for example /bin/bash. For such containers, this argument list
        can also be used to specify the main command in the container process.


        :param arguments: The arguments of this Container.
        :type: list[str]
        """
        self._arguments = arguments

    @property
    def additional_capabilities(self):
        """
        Gets the additional_capabilities of this Container.
        A list of additional configurable container capabilities

        Allowed values for items in this list are: "CAP_NET_ADMIN", "CAP_NET_RAW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The additional_capabilities of this Container.
        :rtype: list[str]
        """
        return self._additional_capabilities

    @additional_capabilities.setter
    def additional_capabilities(self, additional_capabilities):
        """
        Sets the additional_capabilities of this Container.
        A list of additional configurable container capabilities


        :param additional_capabilities: The additional_capabilities of this Container.
        :type: list[str]
        """
        allowed_values = ["CAP_NET_ADMIN", "CAP_NET_RAW"]
        if additional_capabilities:
            additional_capabilities[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in additional_capabilities]
        self._additional_capabilities = additional_capabilities

    @property
    def working_directory(self):
        """
        Gets the working_directory of this Container.
        The working directory within the Container's filesystem for
        the Container process. If this is not present, the default
        working directory from the image will be used.


        :return: The working_directory of this Container.
        :rtype: str
        """
        return self._working_directory

    @working_directory.setter
    def working_directory(self, working_directory):
        """
        Sets the working_directory of this Container.
        The working directory within the Container's filesystem for
        the Container process. If this is not present, the default
        working directory from the image will be used.


        :param working_directory: The working_directory of this Container.
        :type: str
        """
        self._working_directory = working_directory

    @property
    def environment_variables(self):
        """
        Gets the environment_variables of this Container.
        A map of additional environment variables to set in the environment of the container's
        entrypoint process. These variables are in addition to any variables already defined
        in the container's image.


        :return: The environment_variables of this Container.
        :rtype: dict(str, str)
        """
        return self._environment_variables

    @environment_variables.setter
    def environment_variables(self, environment_variables):
        """
        Sets the environment_variables of this Container.
        A map of additional environment variables to set in the environment of the container's
        entrypoint process. These variables are in addition to any variables already defined
        in the container's image.


        :param environment_variables: The environment_variables of this Container.
        :type: dict(str, str)
        """
        self._environment_variables = environment_variables

    @property
    def volume_mounts(self):
        """
        Gets the volume_mounts of this Container.
        List of the volume mounts.


        :return: The volume_mounts of this Container.
        :rtype: list[oci.container_instances.models.VolumeMount]
        """
        return self._volume_mounts

    @volume_mounts.setter
    def volume_mounts(self, volume_mounts):
        """
        Sets the volume_mounts of this Container.
        List of the volume mounts.


        :param volume_mounts: The volume_mounts of this Container.
        :type: list[oci.container_instances.models.VolumeMount]
        """
        self._volume_mounts = volume_mounts

    @property
    def health_checks(self):
        """
        Gets the health_checks of this Container.
        List of container health checks


        :return: The health_checks of this Container.
        :rtype: list[oci.container_instances.models.ContainerHealthCheck]
        """
        return self._health_checks

    @health_checks.setter
    def health_checks(self, health_checks):
        """
        Sets the health_checks of this Container.
        List of container health checks


        :param health_checks: The health_checks of this Container.
        :type: list[oci.container_instances.models.ContainerHealthCheck]
        """
        self._health_checks = health_checks

    @property
    def is_resource_principal_disabled(self):
        """
        Gets the is_resource_principal_disabled of this Container.
        Determines if the Container will have access to the Container Instance Resource Principal.
        This method utilizes resource principal version 2.2. Please refer to
        https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#sdk_authentication_methods_resource_principal
        for detailed explanation of how to leverage the exposed resource principal elements.


        :return: The is_resource_principal_disabled of this Container.
        :rtype: bool
        """
        return self._is_resource_principal_disabled

    @is_resource_principal_disabled.setter
    def is_resource_principal_disabled(self, is_resource_principal_disabled):
        """
        Sets the is_resource_principal_disabled of this Container.
        Determines if the Container will have access to the Container Instance Resource Principal.
        This method utilizes resource principal version 2.2. Please refer to
        https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#sdk_authentication_methods_resource_principal
        for detailed explanation of how to leverage the exposed resource principal elements.


        :param is_resource_principal_disabled: The is_resource_principal_disabled of this Container.
        :type: bool
        """
        self._is_resource_principal_disabled = is_resource_principal_disabled

    @property
    def resource_config(self):
        """
        Gets the resource_config of this Container.

        :return: The resource_config of this Container.
        :rtype: oci.container_instances.models.ContainerResourceConfig
        """
        return self._resource_config

    @resource_config.setter
    def resource_config(self, resource_config):
        """
        Sets the resource_config of this Container.

        :param resource_config: The resource_config of this Container.
        :type: oci.container_instances.models.ContainerResourceConfig
        """
        self._resource_config = resource_config

    @property
    def container_restart_attempt_count(self):
        """
        Gets the container_restart_attempt_count of this Container.
        The number of container restart attempts. A restart may be attempted after a health check failure or a container exit, based on the restart policy.


        :return: The container_restart_attempt_count of this Container.
        :rtype: int
        """
        return self._container_restart_attempt_count

    @container_restart_attempt_count.setter
    def container_restart_attempt_count(self, container_restart_attempt_count):
        """
        Sets the container_restart_attempt_count of this Container.
        The number of container restart attempts. A restart may be attempted after a health check failure or a container exit, based on the restart policy.


        :param container_restart_attempt_count: The container_restart_attempt_count of this Container.
        :type: int
        """
        self._container_restart_attempt_count = container_restart_attempt_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
