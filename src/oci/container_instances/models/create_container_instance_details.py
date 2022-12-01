# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateContainerInstanceDetails(object):
    """
    The information about new ContainerInstance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateContainerInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateContainerInstanceDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateContainerInstanceDetails.
        :type compartment_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateContainerInstanceDetails.
        :type availability_domain: str

        :param fault_domain:
            The value to assign to the fault_domain property of this CreateContainerInstanceDetails.
        :type fault_domain: str

        :param shape:
            The value to assign to the shape property of this CreateContainerInstanceDetails.
        :type shape: str

        :param shape_config:
            The value to assign to the shape_config property of this CreateContainerInstanceDetails.
        :type shape_config: oci.container_instances.models.CreateContainerInstanceShapeConfigDetails

        :param volumes:
            The value to assign to the volumes property of this CreateContainerInstanceDetails.
        :type volumes: list[oci.container_instances.models.CreateContainerVolumeDetails]

        :param containers:
            The value to assign to the containers property of this CreateContainerInstanceDetails.
        :type containers: list[oci.container_instances.models.CreateContainerDetails]

        :param vnics:
            The value to assign to the vnics property of this CreateContainerInstanceDetails.
        :type vnics: list[oci.container_instances.models.CreateContainerVnicDetails]

        :param dns_config:
            The value to assign to the dns_config property of this CreateContainerInstanceDetails.
        :type dns_config: oci.container_instances.models.CreateContainerDnsConfigDetails

        :param graceful_shutdown_timeout_in_seconds:
            The value to assign to the graceful_shutdown_timeout_in_seconds property of this CreateContainerInstanceDetails.
        :type graceful_shutdown_timeout_in_seconds: int

        :param image_pull_secrets:
            The value to assign to the image_pull_secrets property of this CreateContainerInstanceDetails.
        :type image_pull_secrets: list[oci.container_instances.models.CreateImagePullSecretDetails]

        :param container_restart_policy:
            The value to assign to the container_restart_policy property of this CreateContainerInstanceDetails.
        :type container_restart_policy: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateContainerInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateContainerInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'availability_domain': 'str',
            'fault_domain': 'str',
            'shape': 'str',
            'shape_config': 'CreateContainerInstanceShapeConfigDetails',
            'volumes': 'list[CreateContainerVolumeDetails]',
            'containers': 'list[CreateContainerDetails]',
            'vnics': 'list[CreateContainerVnicDetails]',
            'dns_config': 'CreateContainerDnsConfigDetails',
            'graceful_shutdown_timeout_in_seconds': 'int',
            'image_pull_secrets': 'list[CreateImagePullSecretDetails]',
            'container_restart_policy': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'availability_domain': 'availabilityDomain',
            'fault_domain': 'faultDomain',
            'shape': 'shape',
            'shape_config': 'shapeConfig',
            'volumes': 'volumes',
            'containers': 'containers',
            'vnics': 'vnics',
            'dns_config': 'dnsConfig',
            'graceful_shutdown_timeout_in_seconds': 'gracefulShutdownTimeoutInSeconds',
            'image_pull_secrets': 'imagePullSecrets',
            'container_restart_policy': 'containerRestartPolicy',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._availability_domain = None
        self._fault_domain = None
        self._shape = None
        self._shape_config = None
        self._volumes = None
        self._containers = None
        self._vnics = None
        self._dns_config = None
        self._graceful_shutdown_timeout_in_seconds = None
        self._image_pull_secrets = None
        self._container_restart_policy = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateContainerInstanceDetails.
        Human-readable name for the ContainerInstance. If none is provided,
        OCI will select one for you.


        :return: The display_name of this CreateContainerInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateContainerInstanceDetails.
        Human-readable name for the ContainerInstance. If none is provided,
        OCI will select one for you.


        :param display_name: The display_name of this CreateContainerInstanceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateContainerInstanceDetails.
        Compartment Identifier


        :return: The compartment_id of this CreateContainerInstanceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateContainerInstanceDetails.
        Compartment Identifier


        :param compartment_id: The compartment_id of this CreateContainerInstanceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CreateContainerInstanceDetails.
        Availability Domain where the ContainerInstance should be created.


        :return: The availability_domain of this CreateContainerInstanceDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateContainerInstanceDetails.
        Availability Domain where the ContainerInstance should be created.


        :param availability_domain: The availability_domain of this CreateContainerInstanceDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this CreateContainerInstanceDetails.
        Fault Domain where the ContainerInstance should run.


        :return: The fault_domain of this CreateContainerInstanceDetails.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this CreateContainerInstanceDetails.
        Fault Domain where the ContainerInstance should run.


        :param fault_domain: The fault_domain of this CreateContainerInstanceDetails.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this CreateContainerInstanceDetails.
        The shape of the Container Instance. The shape determines the resources available to the Container Instance.


        :return: The shape of this CreateContainerInstanceDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this CreateContainerInstanceDetails.
        The shape of the Container Instance. The shape determines the resources available to the Container Instance.


        :param shape: The shape of this CreateContainerInstanceDetails.
        :type: str
        """
        self._shape = shape

    @property
    def shape_config(self):
        """
        **[Required]** Gets the shape_config of this CreateContainerInstanceDetails.

        :return: The shape_config of this CreateContainerInstanceDetails.
        :rtype: oci.container_instances.models.CreateContainerInstanceShapeConfigDetails
        """
        return self._shape_config

    @shape_config.setter
    def shape_config(self, shape_config):
        """
        Sets the shape_config of this CreateContainerInstanceDetails.

        :param shape_config: The shape_config of this CreateContainerInstanceDetails.
        :type: oci.container_instances.models.CreateContainerInstanceShapeConfigDetails
        """
        self._shape_config = shape_config

    @property
    def volumes(self):
        """
        Gets the volumes of this CreateContainerInstanceDetails.
        A Volume represents a directory with data that is accessible across multiple containers in a
        ContainerInstance.
        Up to 32 volumes can be attached to single container instance.


        :return: The volumes of this CreateContainerInstanceDetails.
        :rtype: list[oci.container_instances.models.CreateContainerVolumeDetails]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """
        Sets the volumes of this CreateContainerInstanceDetails.
        A Volume represents a directory with data that is accessible across multiple containers in a
        ContainerInstance.
        Up to 32 volumes can be attached to single container instance.


        :param volumes: The volumes of this CreateContainerInstanceDetails.
        :type: list[oci.container_instances.models.CreateContainerVolumeDetails]
        """
        self._volumes = volumes

    @property
    def containers(self):
        """
        **[Required]** Gets the containers of this CreateContainerInstanceDetails.
        The Containers to create on this Instance.


        :return: The containers of this CreateContainerInstanceDetails.
        :rtype: list[oci.container_instances.models.CreateContainerDetails]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        """
        Sets the containers of this CreateContainerInstanceDetails.
        The Containers to create on this Instance.


        :param containers: The containers of this CreateContainerInstanceDetails.
        :type: list[oci.container_instances.models.CreateContainerDetails]
        """
        self._containers = containers

    @property
    def vnics(self):
        """
        **[Required]** Gets the vnics of this CreateContainerInstanceDetails.
        The networks to make available to containers on this Instance.


        :return: The vnics of this CreateContainerInstanceDetails.
        :rtype: list[oci.container_instances.models.CreateContainerVnicDetails]
        """
        return self._vnics

    @vnics.setter
    def vnics(self, vnics):
        """
        Sets the vnics of this CreateContainerInstanceDetails.
        The networks to make available to containers on this Instance.


        :param vnics: The vnics of this CreateContainerInstanceDetails.
        :type: list[oci.container_instances.models.CreateContainerVnicDetails]
        """
        self._vnics = vnics

    @property
    def dns_config(self):
        """
        Gets the dns_config of this CreateContainerInstanceDetails.

        :return: The dns_config of this CreateContainerInstanceDetails.
        :rtype: oci.container_instances.models.CreateContainerDnsConfigDetails
        """
        return self._dns_config

    @dns_config.setter
    def dns_config(self, dns_config):
        """
        Sets the dns_config of this CreateContainerInstanceDetails.

        :param dns_config: The dns_config of this CreateContainerInstanceDetails.
        :type: oci.container_instances.models.CreateContainerDnsConfigDetails
        """
        self._dns_config = dns_config

    @property
    def graceful_shutdown_timeout_in_seconds(self):
        """
        Gets the graceful_shutdown_timeout_in_seconds of this CreateContainerInstanceDetails.
        Duration in seconds processes within a Container have to gracefully terminate. This applies whenever a Container must be halted, such as when the Container Instance is deleted. Processes will first be sent a termination signal. After this timeout is reached, the processes will be sent a termination signal.


        :return: The graceful_shutdown_timeout_in_seconds of this CreateContainerInstanceDetails.
        :rtype: int
        """
        return self._graceful_shutdown_timeout_in_seconds

    @graceful_shutdown_timeout_in_seconds.setter
    def graceful_shutdown_timeout_in_seconds(self, graceful_shutdown_timeout_in_seconds):
        """
        Sets the graceful_shutdown_timeout_in_seconds of this CreateContainerInstanceDetails.
        Duration in seconds processes within a Container have to gracefully terminate. This applies whenever a Container must be halted, such as when the Container Instance is deleted. Processes will first be sent a termination signal. After this timeout is reached, the processes will be sent a termination signal.


        :param graceful_shutdown_timeout_in_seconds: The graceful_shutdown_timeout_in_seconds of this CreateContainerInstanceDetails.
        :type: int
        """
        self._graceful_shutdown_timeout_in_seconds = graceful_shutdown_timeout_in_seconds

    @property
    def image_pull_secrets(self):
        """
        Gets the image_pull_secrets of this CreateContainerInstanceDetails.
        The image pull secrets for accessing private registry to pull images for containers


        :return: The image_pull_secrets of this CreateContainerInstanceDetails.
        :rtype: list[oci.container_instances.models.CreateImagePullSecretDetails]
        """
        return self._image_pull_secrets

    @image_pull_secrets.setter
    def image_pull_secrets(self, image_pull_secrets):
        """
        Sets the image_pull_secrets of this CreateContainerInstanceDetails.
        The image pull secrets for accessing private registry to pull images for containers


        :param image_pull_secrets: The image_pull_secrets of this CreateContainerInstanceDetails.
        :type: list[oci.container_instances.models.CreateImagePullSecretDetails]
        """
        self._image_pull_secrets = image_pull_secrets

    @property
    def container_restart_policy(self):
        """
        Gets the container_restart_policy of this CreateContainerInstanceDetails.
        Container restart policy


        :return: The container_restart_policy of this CreateContainerInstanceDetails.
        :rtype: str
        """
        return self._container_restart_policy

    @container_restart_policy.setter
    def container_restart_policy(self, container_restart_policy):
        """
        Sets the container_restart_policy of this CreateContainerInstanceDetails.
        Container restart policy


        :param container_restart_policy: The container_restart_policy of this CreateContainerInstanceDetails.
        :type: str
        """
        self._container_restart_policy = container_restart_policy

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateContainerInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateContainerInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateContainerInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateContainerInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateContainerInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateContainerInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateContainerInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateContainerInstanceDetails.
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
