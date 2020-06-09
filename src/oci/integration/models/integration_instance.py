# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IntegrationInstance(object):
    """
    Description of Integration Instance.
    """

    #: A constant which can be used with the integration_instance_type property of a IntegrationInstance.
    #: This constant has a value of "STANDARD"
    INTEGRATION_INSTANCE_TYPE_STANDARD = "STANDARD"

    #: A constant which can be used with the integration_instance_type property of a IntegrationInstance.
    #: This constant has a value of "ENTERPRISE"
    INTEGRATION_INSTANCE_TYPE_ENTERPRISE = "ENTERPRISE"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstance.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstance.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstance.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstance.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstance.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstance.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstance.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new IntegrationInstance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this IntegrationInstance.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this IntegrationInstance.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this IntegrationInstance.
        :type compartment_id: str

        :param integration_instance_type:
            The value to assign to the integration_instance_type property of this IntegrationInstance.
            Allowed values for this property are: "STANDARD", "ENTERPRISE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type integration_instance_type: str

        :param time_created:
            The value to assign to the time_created property of this IntegrationInstance.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this IntegrationInstance.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this IntegrationInstance.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param state_message:
            The value to assign to the state_message property of this IntegrationInstance.
        :type state_message: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this IntegrationInstance.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this IntegrationInstance.
        :type defined_tags: dict(str, dict(str, object))

        :param is_byol:
            The value to assign to the is_byol property of this IntegrationInstance.
        :type is_byol: bool

        :param instance_url:
            The value to assign to the instance_url property of this IntegrationInstance.
        :type instance_url: str

        :param message_packs:
            The value to assign to the message_packs property of this IntegrationInstance.
        :type message_packs: int

        :param is_file_server_enabled:
            The value to assign to the is_file_server_enabled property of this IntegrationInstance.
        :type is_file_server_enabled: bool

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'integration_instance_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'state_message': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'is_byol': 'bool',
            'instance_url': 'str',
            'message_packs': 'int',
            'is_file_server_enabled': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'integration_instance_type': 'integrationInstanceType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'state_message': 'stateMessage',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'is_byol': 'isByol',
            'instance_url': 'instanceUrl',
            'message_packs': 'messagePacks',
            'is_file_server_enabled': 'isFileServerEnabled'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._integration_instance_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._state_message = None
        self._freeform_tags = None
        self._defined_tags = None
        self._is_byol = None
        self._instance_url = None
        self._message_packs = None
        self._is_file_server_enabled = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this IntegrationInstance.
        Unique identifier that is immutable on creation.


        :return: The id of this IntegrationInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IntegrationInstance.
        Unique identifier that is immutable on creation.


        :param id: The id of this IntegrationInstance.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this IntegrationInstance.
        Integration Instance Identifier, can be renamed.


        :return: The display_name of this IntegrationInstance.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this IntegrationInstance.
        Integration Instance Identifier, can be renamed.


        :param display_name: The display_name of this IntegrationInstance.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this IntegrationInstance.
        Compartment Identifier.


        :return: The compartment_id of this IntegrationInstance.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IntegrationInstance.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this IntegrationInstance.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def integration_instance_type(self):
        """
        **[Required]** Gets the integration_instance_type of this IntegrationInstance.
        Standard or Enterprise type

        Allowed values for this property are: "STANDARD", "ENTERPRISE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The integration_instance_type of this IntegrationInstance.
        :rtype: str
        """
        return self._integration_instance_type

    @integration_instance_type.setter
    def integration_instance_type(self, integration_instance_type):
        """
        Sets the integration_instance_type of this IntegrationInstance.
        Standard or Enterprise type


        :param integration_instance_type: The integration_instance_type of this IntegrationInstance.
        :type: str
        """
        allowed_values = ["STANDARD", "ENTERPRISE"]
        if not value_allowed_none_or_none_sentinel(integration_instance_type, allowed_values):
            integration_instance_type = 'UNKNOWN_ENUM_VALUE'
        self._integration_instance_type = integration_instance_type

    @property
    def time_created(self):
        """
        Gets the time_created of this IntegrationInstance.
        The time the the IntegrationInstance was created. An RFC3339 formatted datetime string.


        :return: The time_created of this IntegrationInstance.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this IntegrationInstance.
        The time the the IntegrationInstance was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this IntegrationInstance.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this IntegrationInstance.
        The time the IntegrationInstance was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this IntegrationInstance.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this IntegrationInstance.
        The time the IntegrationInstance was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this IntegrationInstance.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this IntegrationInstance.
        The current state of the integration instance.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this IntegrationInstance.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this IntegrationInstance.
        The current state of the integration instance.


        :param lifecycle_state: The lifecycle_state of this IntegrationInstance.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def state_message(self):
        """
        Gets the state_message of this IntegrationInstance.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The state_message of this IntegrationInstance.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        """
        Sets the state_message of this IntegrationInstance.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param state_message: The state_message of this IntegrationInstance.
        :type: str
        """
        self._state_message = state_message

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this IntegrationInstance.
        Simple key-value pair that is applied without any predefined name,
        type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this IntegrationInstance.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this IntegrationInstance.
        Simple key-value pair that is applied without any predefined name,
        type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this IntegrationInstance.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this IntegrationInstance.
        Usage of predefined tag keys. These predefined keys are scoped to
        namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this IntegrationInstance.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this IntegrationInstance.
        Usage of predefined tag keys. These predefined keys are scoped to
        namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this IntegrationInstance.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def is_byol(self):
        """
        **[Required]** Gets the is_byol of this IntegrationInstance.
        Bring your own license.


        :return: The is_byol of this IntegrationInstance.
        :rtype: bool
        """
        return self._is_byol

    @is_byol.setter
    def is_byol(self, is_byol):
        """
        Sets the is_byol of this IntegrationInstance.
        Bring your own license.


        :param is_byol: The is_byol of this IntegrationInstance.
        :type: bool
        """
        self._is_byol = is_byol

    @property
    def instance_url(self):
        """
        **[Required]** Gets the instance_url of this IntegrationInstance.
        The Integration Instance URL.


        :return: The instance_url of this IntegrationInstance.
        :rtype: str
        """
        return self._instance_url

    @instance_url.setter
    def instance_url(self, instance_url):
        """
        Sets the instance_url of this IntegrationInstance.
        The Integration Instance URL.


        :param instance_url: The instance_url of this IntegrationInstance.
        :type: str
        """
        self._instance_url = instance_url

    @property
    def message_packs(self):
        """
        **[Required]** Gets the message_packs of this IntegrationInstance.
        The number of configured message packs (if any)


        :return: The message_packs of this IntegrationInstance.
        :rtype: int
        """
        return self._message_packs

    @message_packs.setter
    def message_packs(self, message_packs):
        """
        Sets the message_packs of this IntegrationInstance.
        The number of configured message packs (if any)


        :param message_packs: The message_packs of this IntegrationInstance.
        :type: int
        """
        self._message_packs = message_packs

    @property
    def is_file_server_enabled(self):
        """
        Gets the is_file_server_enabled of this IntegrationInstance.
        The file server is enabled or not.


        :return: The is_file_server_enabled of this IntegrationInstance.
        :rtype: bool
        """
        return self._is_file_server_enabled

    @is_file_server_enabled.setter
    def is_file_server_enabled(self, is_file_server_enabled):
        """
        Sets the is_file_server_enabled of this IntegrationInstance.
        The file server is enabled or not.


        :param is_file_server_enabled: The is_file_server_enabled of this IntegrationInstance.
        :type: bool
        """
        self._is_file_server_enabled = is_file_server_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
