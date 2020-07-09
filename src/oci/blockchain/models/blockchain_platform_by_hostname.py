# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BlockchainPlatformByHostname(object):
    """
    Blockchain Platform Instance Details For Hostname.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BlockchainPlatformByHostname object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BlockchainPlatformByHostname.
        :type id: str

        :param service_endpoint:
            The value to assign to the service_endpoint property of this BlockchainPlatformByHostname.
        :type service_endpoint: str

        :param display_name:
            The value to assign to the display_name property of this BlockchainPlatformByHostname.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BlockchainPlatformByHostname.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this BlockchainPlatformByHostname.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this BlockchainPlatformByHostname.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this BlockchainPlatformByHostname.
        :type time_updated: datetime

        :param platform_role:
            The value to assign to the platform_role property of this BlockchainPlatformByHostname.
        :type platform_role: str

        :param compute_shape:
            The value to assign to the compute_shape property of this BlockchainPlatformByHostname.
        :type compute_shape: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BlockchainPlatformByHostname.
        :type lifecycle_state: str

        :param life_cycle_details:
            The value to assign to the life_cycle_details property of this BlockchainPlatformByHostname.
        :type life_cycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BlockchainPlatformByHostname.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this BlockchainPlatformByHostname.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'service_endpoint': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'platform_role': 'str',
            'compute_shape': 'str',
            'lifecycle_state': 'str',
            'life_cycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'service_endpoint': 'serviceEndpoint',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'platform_role': 'platformRole',
            'compute_shape': 'computeShape',
            'lifecycle_state': 'lifecycleState',
            'life_cycle_details': 'lifeCycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._service_endpoint = None
        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._time_created = None
        self._time_updated = None
        self._platform_role = None
        self._compute_shape = None
        self._lifecycle_state = None
        self._life_cycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BlockchainPlatformByHostname.
        unique identifier that is immutable on creation


        :return: The id of this BlockchainPlatformByHostname.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BlockchainPlatformByHostname.
        unique identifier that is immutable on creation


        :param id: The id of this BlockchainPlatformByHostname.
        :type: str
        """
        self._id = id

    @property
    def service_endpoint(self):
        """
        Gets the service_endpoint of this BlockchainPlatformByHostname.
        Service endpoint URL, valid post-provisioning


        :return: The service_endpoint of this BlockchainPlatformByHostname.
        :rtype: str
        """
        return self._service_endpoint

    @service_endpoint.setter
    def service_endpoint(self, service_endpoint):
        """
        Sets the service_endpoint of this BlockchainPlatformByHostname.
        Service endpoint URL, valid post-provisioning


        :param service_endpoint: The service_endpoint of this BlockchainPlatformByHostname.
        :type: str
        """
        self._service_endpoint = service_endpoint

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this BlockchainPlatformByHostname.
        Platform Instance Display name, can be renamed


        :return: The display_name of this BlockchainPlatformByHostname.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BlockchainPlatformByHostname.
        Platform Instance Display name, can be renamed


        :param display_name: The display_name of this BlockchainPlatformByHostname.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this BlockchainPlatformByHostname.
        Compartment Identifier


        :return: The compartment_id of this BlockchainPlatformByHostname.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BlockchainPlatformByHostname.
        Compartment Identifier


        :param compartment_id: The compartment_id of this BlockchainPlatformByHostname.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this BlockchainPlatformByHostname.
        Platform Instance Description


        :return: The description of this BlockchainPlatformByHostname.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BlockchainPlatformByHostname.
        Platform Instance Description


        :param description: The description of this BlockchainPlatformByHostname.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this BlockchainPlatformByHostname.
        The time the the Platform Instance was created. An RFC3339 formatted datetime string


        :return: The time_created of this BlockchainPlatformByHostname.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BlockchainPlatformByHostname.
        The time the the Platform Instance was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this BlockchainPlatformByHostname.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this BlockchainPlatformByHostname.
        The time the Platform Instance was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this BlockchainPlatformByHostname.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this BlockchainPlatformByHostname.
        The time the Platform Instance was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this BlockchainPlatformByHostname.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def platform_role(self):
        """
        Gets the platform_role of this BlockchainPlatformByHostname.
        Role of platform - founder or participant


        :return: The platform_role of this BlockchainPlatformByHostname.
        :rtype: str
        """
        return self._platform_role

    @platform_role.setter
    def platform_role(self, platform_role):
        """
        Sets the platform_role of this BlockchainPlatformByHostname.
        Role of platform - founder or participant


        :param platform_role: The platform_role of this BlockchainPlatformByHostname.
        :type: str
        """
        self._platform_role = platform_role

    @property
    def compute_shape(self):
        """
        **[Required]** Gets the compute_shape of this BlockchainPlatformByHostname.
        Type of compute shape - one of Standard, (Enterprise) Small, Medium, Large or Extra Large


        :return: The compute_shape of this BlockchainPlatformByHostname.
        :rtype: str
        """
        return self._compute_shape

    @compute_shape.setter
    def compute_shape(self, compute_shape):
        """
        Sets the compute_shape of this BlockchainPlatformByHostname.
        Type of compute shape - one of Standard, (Enterprise) Small, Medium, Large or Extra Large


        :param compute_shape: The compute_shape of this BlockchainPlatformByHostname.
        :type: str
        """
        self._compute_shape = compute_shape

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this BlockchainPlatformByHostname.
        The current state of the Platform Instance.


        :return: The lifecycle_state of this BlockchainPlatformByHostname.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BlockchainPlatformByHostname.
        The current state of the Platform Instance.


        :param lifecycle_state: The lifecycle_state of this BlockchainPlatformByHostname.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def life_cycle_details(self):
        """
        Gets the life_cycle_details of this BlockchainPlatformByHostname.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The life_cycle_details of this BlockchainPlatformByHostname.
        :rtype: str
        """
        return self._life_cycle_details

    @life_cycle_details.setter
    def life_cycle_details(self, life_cycle_details):
        """
        Sets the life_cycle_details of this BlockchainPlatformByHostname.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param life_cycle_details: The life_cycle_details of this BlockchainPlatformByHostname.
        :type: str
        """
        self._life_cycle_details = life_cycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this BlockchainPlatformByHostname.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this BlockchainPlatformByHostname.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this BlockchainPlatformByHostname.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this BlockchainPlatformByHostname.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this BlockchainPlatformByHostname.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this BlockchainPlatformByHostname.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this BlockchainPlatformByHostname.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this BlockchainPlatformByHostname.
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
