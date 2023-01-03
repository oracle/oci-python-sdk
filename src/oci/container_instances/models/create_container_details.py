# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateContainerDetails(object):
    """
    Information to create a new Container within a ContainerInstance.

    The Container created by this call will contain both the tags specified
    in this object as well as any tags specified in the parent ContainerInstance object.

    The Container will be created with the same `compartmentId`, `availabilityDomain`,
    and `faultDomain` as the parent ContainerInstance object.
    """

    #: A constant which can be used with the additional_capabilities property of a CreateContainerDetails.
    #: This constant has a value of "CAP_NET_ADMIN"
    ADDITIONAL_CAPABILITIES_CAP_NET_ADMIN = "CAP_NET_ADMIN"

    #: A constant which can be used with the additional_capabilities property of a CreateContainerDetails.
    #: This constant has a value of "CAP_NET_RAW"
    ADDITIONAL_CAPABILITIES_CAP_NET_RAW = "CAP_NET_RAW"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateContainerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateContainerDetails.
        :type display_name: str

        :param image_url:
            The value to assign to the image_url property of this CreateContainerDetails.
        :type image_url: str

        :param command:
            The value to assign to the command property of this CreateContainerDetails.
        :type command: list[str]

        :param arguments:
            The value to assign to the arguments property of this CreateContainerDetails.
        :type arguments: list[str]

        :param additional_capabilities:
            The value to assign to the additional_capabilities property of this CreateContainerDetails.
            Allowed values for items in this list are: "CAP_NET_ADMIN", "CAP_NET_RAW"
        :type additional_capabilities: list[str]

        :param working_directory:
            The value to assign to the working_directory property of this CreateContainerDetails.
        :type working_directory: str

        :param environment_variables:
            The value to assign to the environment_variables property of this CreateContainerDetails.
        :type environment_variables: dict(str, str)

        :param volume_mounts:
            The value to assign to the volume_mounts property of this CreateContainerDetails.
        :type volume_mounts: list[oci.container_instances.models.CreateVolumeMountDetails]

        :param is_resource_principal_disabled:
            The value to assign to the is_resource_principal_disabled property of this CreateContainerDetails.
        :type is_resource_principal_disabled: bool

        :param resource_config:
            The value to assign to the resource_config property of this CreateContainerDetails.
        :type resource_config: oci.container_instances.models.CreateContainerResourceConfigDetails

        :param health_checks:
            The value to assign to the health_checks property of this CreateContainerDetails.
        :type health_checks: list[oci.container_instances.models.CreateContainerHealthCheckDetails]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateContainerDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateContainerDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'image_url': 'str',
            'command': 'list[str]',
            'arguments': 'list[str]',
            'additional_capabilities': 'list[str]',
            'working_directory': 'str',
            'environment_variables': 'dict(str, str)',
            'volume_mounts': 'list[CreateVolumeMountDetails]',
            'is_resource_principal_disabled': 'bool',
            'resource_config': 'CreateContainerResourceConfigDetails',
            'health_checks': 'list[CreateContainerHealthCheckDetails]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'image_url': 'imageUrl',
            'command': 'command',
            'arguments': 'arguments',
            'additional_capabilities': 'additionalCapabilities',
            'working_directory': 'workingDirectory',
            'environment_variables': 'environmentVariables',
            'volume_mounts': 'volumeMounts',
            'is_resource_principal_disabled': 'isResourcePrincipalDisabled',
            'resource_config': 'resourceConfig',
            'health_checks': 'healthChecks',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._image_url = None
        self._command = None
        self._arguments = None
        self._additional_capabilities = None
        self._working_directory = None
        self._environment_variables = None
        self._volume_mounts = None
        self._is_resource_principal_disabled = None
        self._resource_config = None
        self._health_checks = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateContainerDetails.
        Display name for the Container. There are no guarantees of uniqueness
        for this name. If none is provided, it will be calculated automatically.


        :return: The display_name of this CreateContainerDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateContainerDetails.
        Display name for the Container. There are no guarantees of uniqueness
        for this name. If none is provided, it will be calculated automatically.


        :param display_name: The display_name of this CreateContainerDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def image_url(self):
        """
        **[Required]** Gets the image_url of this CreateContainerDetails.
        The container image information. Currently only support public docker registry. Can be either image name,
        e.g `containerImage`, image name with version, e.g `containerImage:v1` or complete docker image Url e.g
        `docker.io/library/containerImage:latest`.
        If no registry is provided, will default the registry to public docker hub `docker.io/library`.
        The registry used for container image must be reachable over the Container Instance's VNIC.


        :return: The image_url of this CreateContainerDetails.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """
        Sets the image_url of this CreateContainerDetails.
        The container image information. Currently only support public docker registry. Can be either image name,
        e.g `containerImage`, image name with version, e.g `containerImage:v1` or complete docker image Url e.g
        `docker.io/library/containerImage:latest`.
        If no registry is provided, will default the registry to public docker hub `docker.io/library`.
        The registry used for container image must be reachable over the Container Instance's VNIC.


        :param image_url: The image_url of this CreateContainerDetails.
        :type: str
        """
        self._image_url = image_url

    @property
    def command(self):
        """
        Gets the command of this CreateContainerDetails.
        This command will override the container's entrypoint process.
        If not specified, the existing entrypoint process defined in the image will be used.


        :return: The command of this CreateContainerDetails.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this CreateContainerDetails.
        This command will override the container's entrypoint process.
        If not specified, the existing entrypoint process defined in the image will be used.


        :param command: The command of this CreateContainerDetails.
        :type: list[str]
        """
        self._command = command

    @property
    def arguments(self):
        """
        Gets the arguments of this CreateContainerDetails.
        A list of string arguments for a container's entrypoint process.

        Many containers use an entrypoint process pointing to a shell,
        for example /bin/bash. For such containers, this argument list
        can also be used to specify the main command in the container process.

        All arguments together must be 64KB or smaller.


        :return: The arguments of this CreateContainerDetails.
        :rtype: list[str]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """
        Sets the arguments of this CreateContainerDetails.
        A list of string arguments for a container's entrypoint process.

        Many containers use an entrypoint process pointing to a shell,
        for example /bin/bash. For such containers, this argument list
        can also be used to specify the main command in the container process.

        All arguments together must be 64KB or smaller.


        :param arguments: The arguments of this CreateContainerDetails.
        :type: list[str]
        """
        self._arguments = arguments

    @property
    def additional_capabilities(self):
        """
        Gets the additional_capabilities of this CreateContainerDetails.
        A list of additional capabilities for the container.

        Allowed values for items in this list are: "CAP_NET_ADMIN", "CAP_NET_RAW"


        :return: The additional_capabilities of this CreateContainerDetails.
        :rtype: list[str]
        """
        return self._additional_capabilities

    @additional_capabilities.setter
    def additional_capabilities(self, additional_capabilities):
        """
        Sets the additional_capabilities of this CreateContainerDetails.
        A list of additional capabilities for the container.


        :param additional_capabilities: The additional_capabilities of this CreateContainerDetails.
        :type: list[str]
        """
        allowed_values = ["CAP_NET_ADMIN", "CAP_NET_RAW"]

        if additional_capabilities and additional_capabilities is not NONE_SENTINEL:
            for value in additional_capabilities:
                if not value_allowed_none_or_none_sentinel(value, allowed_values):
                    raise ValueError(
                        "Invalid value for `additional_capabilities`, must be None or one of {0}"
                        .format(allowed_values)
                    )
        self._additional_capabilities = additional_capabilities

    @property
    def working_directory(self):
        """
        Gets the working_directory of this CreateContainerDetails.
        The working directory within the Container's filesystem for
        the Container process. If none is set, the Container will run in the
        working directory set by the container image.


        :return: The working_directory of this CreateContainerDetails.
        :rtype: str
        """
        return self._working_directory

    @working_directory.setter
    def working_directory(self, working_directory):
        """
        Sets the working_directory of this CreateContainerDetails.
        The working directory within the Container's filesystem for
        the Container process. If none is set, the Container will run in the
        working directory set by the container image.


        :param working_directory: The working_directory of this CreateContainerDetails.
        :type: str
        """
        self._working_directory = working_directory

    @property
    def environment_variables(self):
        """
        Gets the environment_variables of this CreateContainerDetails.
        A map of additional environment variables to set in the environment of the container's
        entrypoint process. These variables are in addition to any variables already defined
        in the container's image.

        All environment variables together, name and values, must be 64KB or smaller.


        :return: The environment_variables of this CreateContainerDetails.
        :rtype: dict(str, str)
        """
        return self._environment_variables

    @environment_variables.setter
    def environment_variables(self, environment_variables):
        """
        Sets the environment_variables of this CreateContainerDetails.
        A map of additional environment variables to set in the environment of the container's
        entrypoint process. These variables are in addition to any variables already defined
        in the container's image.

        All environment variables together, name and values, must be 64KB or smaller.


        :param environment_variables: The environment_variables of this CreateContainerDetails.
        :type: dict(str, str)
        """
        self._environment_variables = environment_variables

    @property
    def volume_mounts(self):
        """
        Gets the volume_mounts of this CreateContainerDetails.
        List of the volume mounts.


        :return: The volume_mounts of this CreateContainerDetails.
        :rtype: list[oci.container_instances.models.CreateVolumeMountDetails]
        """
        return self._volume_mounts

    @volume_mounts.setter
    def volume_mounts(self, volume_mounts):
        """
        Sets the volume_mounts of this CreateContainerDetails.
        List of the volume mounts.


        :param volume_mounts: The volume_mounts of this CreateContainerDetails.
        :type: list[oci.container_instances.models.CreateVolumeMountDetails]
        """
        self._volume_mounts = volume_mounts

    @property
    def is_resource_principal_disabled(self):
        """
        Gets the is_resource_principal_disabled of this CreateContainerDetails.
        Determines if the Container will have access to the Container Instance Resource Principal.
        This method utilizes resource principal version 2.2. Please refer to
        https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#sdk_authentication_methods_resource_principal
        for detailed explanation of how to leverage the exposed resource principal elements.


        :return: The is_resource_principal_disabled of this CreateContainerDetails.
        :rtype: bool
        """
        return self._is_resource_principal_disabled

    @is_resource_principal_disabled.setter
    def is_resource_principal_disabled(self, is_resource_principal_disabled):
        """
        Sets the is_resource_principal_disabled of this CreateContainerDetails.
        Determines if the Container will have access to the Container Instance Resource Principal.
        This method utilizes resource principal version 2.2. Please refer to
        https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#sdk_authentication_methods_resource_principal
        for detailed explanation of how to leverage the exposed resource principal elements.


        :param is_resource_principal_disabled: The is_resource_principal_disabled of this CreateContainerDetails.
        :type: bool
        """
        self._is_resource_principal_disabled = is_resource_principal_disabled

    @property
    def resource_config(self):
        """
        Gets the resource_config of this CreateContainerDetails.

        :return: The resource_config of this CreateContainerDetails.
        :rtype: oci.container_instances.models.CreateContainerResourceConfigDetails
        """
        return self._resource_config

    @resource_config.setter
    def resource_config(self, resource_config):
        """
        Sets the resource_config of this CreateContainerDetails.

        :param resource_config: The resource_config of this CreateContainerDetails.
        :type: oci.container_instances.models.CreateContainerResourceConfigDetails
        """
        self._resource_config = resource_config

    @property
    def health_checks(self):
        """
        Gets the health_checks of this CreateContainerDetails.
        list of container health checks to check container status and take appropriate action if container status is failed.
        There are three types of health checks that we currently support HTTP, TCP, and Command.


        :return: The health_checks of this CreateContainerDetails.
        :rtype: list[oci.container_instances.models.CreateContainerHealthCheckDetails]
        """
        return self._health_checks

    @health_checks.setter
    def health_checks(self, health_checks):
        """
        Sets the health_checks of this CreateContainerDetails.
        list of container health checks to check container status and take appropriate action if container status is failed.
        There are three types of health checks that we currently support HTTP, TCP, and Command.


        :param health_checks: The health_checks of this CreateContainerDetails.
        :type: list[oci.container_instances.models.CreateContainerHealthCheckDetails]
        """
        self._health_checks = health_checks

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateContainerDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateContainerDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateContainerDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateContainerDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateContainerDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateContainerDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateContainerDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateContainerDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
