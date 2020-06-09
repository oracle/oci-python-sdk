# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IntegrationInstanceSummary(object):
    """
    Summary of the Integration Instance.
    """

    #: A constant which can be used with the integration_instance_type property of a IntegrationInstanceSummary.
    #: This constant has a value of "STANDARD"
    INTEGRATION_INSTANCE_TYPE_STANDARD = "STANDARD"

    #: A constant which can be used with the integration_instance_type property of a IntegrationInstanceSummary.
    #: This constant has a value of "ENTERPRISE"
    INTEGRATION_INSTANCE_TYPE_ENTERPRISE = "ENTERPRISE"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstanceSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstanceSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstanceSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstanceSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstanceSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstanceSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstanceSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new IntegrationInstanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this IntegrationInstanceSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this IntegrationInstanceSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this IntegrationInstanceSummary.
        :type compartment_id: str

        :param integration_instance_type:
            The value to assign to the integration_instance_type property of this IntegrationInstanceSummary.
            Allowed values for this property are: "STANDARD", "ENTERPRISE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type integration_instance_type: str

        :param time_created:
            The value to assign to the time_created property of this IntegrationInstanceSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this IntegrationInstanceSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this IntegrationInstanceSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param state_message:
            The value to assign to the state_message property of this IntegrationInstanceSummary.
        :type state_message: str

        :param is_byol:
            The value to assign to the is_byol property of this IntegrationInstanceSummary.
        :type is_byol: bool

        :param instance_url:
            The value to assign to the instance_url property of this IntegrationInstanceSummary.
        :type instance_url: str

        :param message_packs:
            The value to assign to the message_packs property of this IntegrationInstanceSummary.
        :type message_packs: int

        :param is_file_server_enabled:
            The value to assign to the is_file_server_enabled property of this IntegrationInstanceSummary.
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
        self._is_byol = None
        self._instance_url = None
        self._message_packs = None
        self._is_file_server_enabled = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this IntegrationInstanceSummary.
        Unique identifier that is immutable on creation.


        :return: The id of this IntegrationInstanceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IntegrationInstanceSummary.
        Unique identifier that is immutable on creation.


        :param id: The id of this IntegrationInstanceSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this IntegrationInstanceSummary.
        Integration Instance Identifier, can be renamed.


        :return: The display_name of this IntegrationInstanceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this IntegrationInstanceSummary.
        Integration Instance Identifier, can be renamed.


        :param display_name: The display_name of this IntegrationInstanceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this IntegrationInstanceSummary.
        Compartment Identifier.


        :return: The compartment_id of this IntegrationInstanceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IntegrationInstanceSummary.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this IntegrationInstanceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def integration_instance_type(self):
        """
        **[Required]** Gets the integration_instance_type of this IntegrationInstanceSummary.
        Standard or Enterprise type

        Allowed values for this property are: "STANDARD", "ENTERPRISE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The integration_instance_type of this IntegrationInstanceSummary.
        :rtype: str
        """
        return self._integration_instance_type

    @integration_instance_type.setter
    def integration_instance_type(self, integration_instance_type):
        """
        Sets the integration_instance_type of this IntegrationInstanceSummary.
        Standard or Enterprise type


        :param integration_instance_type: The integration_instance_type of this IntegrationInstanceSummary.
        :type: str
        """
        allowed_values = ["STANDARD", "ENTERPRISE"]
        if not value_allowed_none_or_none_sentinel(integration_instance_type, allowed_values):
            integration_instance_type = 'UNKNOWN_ENUM_VALUE'
        self._integration_instance_type = integration_instance_type

    @property
    def time_created(self):
        """
        Gets the time_created of this IntegrationInstanceSummary.
        The time the the Integration Instance was created. An RFC3339 formatted datetime string.


        :return: The time_created of this IntegrationInstanceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this IntegrationInstanceSummary.
        The time the the Integration Instance was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this IntegrationInstanceSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this IntegrationInstanceSummary.
        The time the IntegrationInstance was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this IntegrationInstanceSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this IntegrationInstanceSummary.
        The time the IntegrationInstance was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this IntegrationInstanceSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this IntegrationInstanceSummary.
        The current state of the Integration Instance.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this IntegrationInstanceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this IntegrationInstanceSummary.
        The current state of the Integration Instance.


        :param lifecycle_state: The lifecycle_state of this IntegrationInstanceSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def state_message(self):
        """
        Gets the state_message of this IntegrationInstanceSummary.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The state_message of this IntegrationInstanceSummary.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        """
        Sets the state_message of this IntegrationInstanceSummary.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param state_message: The state_message of this IntegrationInstanceSummary.
        :type: str
        """
        self._state_message = state_message

    @property
    def is_byol(self):
        """
        **[Required]** Gets the is_byol of this IntegrationInstanceSummary.
        Bring your own license.


        :return: The is_byol of this IntegrationInstanceSummary.
        :rtype: bool
        """
        return self._is_byol

    @is_byol.setter
    def is_byol(self, is_byol):
        """
        Sets the is_byol of this IntegrationInstanceSummary.
        Bring your own license.


        :param is_byol: The is_byol of this IntegrationInstanceSummary.
        :type: bool
        """
        self._is_byol = is_byol

    @property
    def instance_url(self):
        """
        **[Required]** Gets the instance_url of this IntegrationInstanceSummary.
        The Integration Instance URL.


        :return: The instance_url of this IntegrationInstanceSummary.
        :rtype: str
        """
        return self._instance_url

    @instance_url.setter
    def instance_url(self, instance_url):
        """
        Sets the instance_url of this IntegrationInstanceSummary.
        The Integration Instance URL.


        :param instance_url: The instance_url of this IntegrationInstanceSummary.
        :type: str
        """
        self._instance_url = instance_url

    @property
    def message_packs(self):
        """
        **[Required]** Gets the message_packs of this IntegrationInstanceSummary.
        The number of configured message packs (if any)


        :return: The message_packs of this IntegrationInstanceSummary.
        :rtype: int
        """
        return self._message_packs

    @message_packs.setter
    def message_packs(self, message_packs):
        """
        Sets the message_packs of this IntegrationInstanceSummary.
        The number of configured message packs (if any)


        :param message_packs: The message_packs of this IntegrationInstanceSummary.
        :type: int
        """
        self._message_packs = message_packs

    @property
    def is_file_server_enabled(self):
        """
        Gets the is_file_server_enabled of this IntegrationInstanceSummary.
        The file server is enabled or not.


        :return: The is_file_server_enabled of this IntegrationInstanceSummary.
        :rtype: bool
        """
        return self._is_file_server_enabled

    @is_file_server_enabled.setter
    def is_file_server_enabled(self, is_file_server_enabled):
        """
        Sets the is_file_server_enabled of this IntegrationInstanceSummary.
        The file server is enabled or not.


        :param is_file_server_enabled: The is_file_server_enabled of this IntegrationInstanceSummary.
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
