# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerSummary(object):
    """
    A reduced set of details about a single Container returned by list APIs.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ContainerSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ContainerSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ContainerSummary.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ContainerSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ContainerSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ContainerSummary.
        :type system_tags: dict(str, dict(str, object))

        :param availability_domain:
            The value to assign to the availability_domain property of this ContainerSummary.
        :type availability_domain: str

        :param fault_domain:
            The value to assign to the fault_domain property of this ContainerSummary.
        :type fault_domain: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ContainerSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ContainerSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this ContainerSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ContainerSummary.
        :type time_updated: datetime

        :param container_instance_id:
            The value to assign to the container_instance_id property of this ContainerSummary.
        :type container_instance_id: str

        :param resource_config:
            The value to assign to the resource_config property of this ContainerSummary.
        :type resource_config: oci.container_instances.models.ContainerResourceConfig

        :param image_url:
            The value to assign to the image_url property of this ContainerSummary.
        :type image_url: str

        :param is_resource_principal_disabled:
            The value to assign to the is_resource_principal_disabled property of this ContainerSummary.
        :type is_resource_principal_disabled: bool

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
            'container_instance_id': 'str',
            'resource_config': 'ContainerResourceConfig',
            'image_url': 'str',
            'is_resource_principal_disabled': 'bool'
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
            'container_instance_id': 'containerInstanceId',
            'resource_config': 'resourceConfig',
            'image_url': 'imageUrl',
            'is_resource_principal_disabled': 'isResourcePrincipalDisabled'
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
        self._container_instance_id = None
        self._resource_config = None
        self._image_url = None
        self._is_resource_principal_disabled = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ContainerSummary.
        Unique identifier that is immutable on creation


        :return: The id of this ContainerSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ContainerSummary.
        Unique identifier that is immutable on creation


        :param id: The id of this ContainerSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ContainerSummary.
        Display name for the Container. Can be renamed.


        :return: The display_name of this ContainerSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ContainerSummary.
        Display name for the Container. Can be renamed.


        :param display_name: The display_name of this ContainerSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ContainerSummary.
        Compartment Identifier


        :return: The compartment_id of this ContainerSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ContainerSummary.
        Compartment Identifier


        :param compartment_id: The compartment_id of this ContainerSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ContainerSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ContainerSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ContainerSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ContainerSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ContainerSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ContainerSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ContainerSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ContainerSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ContainerSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ContainerSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ContainerSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ContainerSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this ContainerSummary.
        Availability Domain where the Container's Instance is running.


        :return: The availability_domain of this ContainerSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ContainerSummary.
        Availability Domain where the Container's Instance is running.


        :param availability_domain: The availability_domain of this ContainerSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this ContainerSummary.
        Fault Domain where the Container's Instance is running.


        :return: The fault_domain of this ContainerSummary.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this ContainerSummary.
        Fault Domain where the Container's Instance is running.


        :param fault_domain: The fault_domain of this ContainerSummary.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ContainerSummary.
        The current state of the Container.


        :return: The lifecycle_state of this ContainerSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ContainerSummary.
        The current state of the Container.


        :param lifecycle_state: The lifecycle_state of this ContainerSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ContainerSummary.
        A message describing the current state in more detail. For example, can be used to provide
        actionable information for a resource in Failed state.


        :return: The lifecycle_details of this ContainerSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ContainerSummary.
        A message describing the current state in more detail. For example, can be used to provide
        actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this ContainerSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ContainerSummary.
        The time the the Container was created. An RFC3339 formatted datetime string


        :return: The time_created of this ContainerSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ContainerSummary.
        The time the the Container was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this ContainerSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ContainerSummary.
        The time the Container was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this ContainerSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ContainerSummary.
        The time the Container was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this ContainerSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def container_instance_id(self):
        """
        **[Required]** Gets the container_instance_id of this ContainerSummary.
        The identifier of the Container Instance on which this container is running.


        :return: The container_instance_id of this ContainerSummary.
        :rtype: str
        """
        return self._container_instance_id

    @container_instance_id.setter
    def container_instance_id(self, container_instance_id):
        """
        Sets the container_instance_id of this ContainerSummary.
        The identifier of the Container Instance on which this container is running.


        :param container_instance_id: The container_instance_id of this ContainerSummary.
        :type: str
        """
        self._container_instance_id = container_instance_id

    @property
    def resource_config(self):
        """
        Gets the resource_config of this ContainerSummary.

        :return: The resource_config of this ContainerSummary.
        :rtype: oci.container_instances.models.ContainerResourceConfig
        """
        return self._resource_config

    @resource_config.setter
    def resource_config(self, resource_config):
        """
        Sets the resource_config of this ContainerSummary.

        :param resource_config: The resource_config of this ContainerSummary.
        :type: oci.container_instances.models.ContainerResourceConfig
        """
        self._resource_config = resource_config

    @property
    def image_url(self):
        """
        **[Required]** Gets the image_url of this ContainerSummary.
        The container image information. Currently only support public docker registry. Can be either image name,
        e.g `containerImage`, image name with version, e.g `containerImage:v1` or complete docker image Url e.g
        `docker.io/library/containerImage:latest`.
        If no registry is provided, will default the registry to public docker hub `docker.io/library`.
        The registry used for container image must be reachable over the Container Instance's VNIC.


        :return: The image_url of this ContainerSummary.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """
        Sets the image_url of this ContainerSummary.
        The container image information. Currently only support public docker registry. Can be either image name,
        e.g `containerImage`, image name with version, e.g `containerImage:v1` or complete docker image Url e.g
        `docker.io/library/containerImage:latest`.
        If no registry is provided, will default the registry to public docker hub `docker.io/library`.
        The registry used for container image must be reachable over the Container Instance's VNIC.


        :param image_url: The image_url of this ContainerSummary.
        :type: str
        """
        self._image_url = image_url

    @property
    def is_resource_principal_disabled(self):
        """
        Gets the is_resource_principal_disabled of this ContainerSummary.
        Determines if the Container will have access to the Container Instance Resource Principal.
        This method utilizes resource principal version 2.2. Please refer to
        https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#sdk_authentication_methods_resource_principal
        for detailed explanation of how to leverage the exposed resource principal elements.


        :return: The is_resource_principal_disabled of this ContainerSummary.
        :rtype: bool
        """
        return self._is_resource_principal_disabled

    @is_resource_principal_disabled.setter
    def is_resource_principal_disabled(self, is_resource_principal_disabled):
        """
        Sets the is_resource_principal_disabled of this ContainerSummary.
        Determines if the Container will have access to the Container Instance Resource Principal.
        This method utilizes resource principal version 2.2. Please refer to
        https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm#sdk_authentication_methods_resource_principal
        for detailed explanation of how to leverage the exposed resource principal elements.


        :param is_resource_principal_disabled: The is_resource_principal_disabled of this ContainerSummary.
        :type: bool
        """
        self._is_resource_principal_disabled = is_resource_principal_disabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
