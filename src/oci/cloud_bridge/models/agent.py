# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Agent(object):
    """
    Description of Agent.
    """

    #: A constant which can be used with the agent_type property of a Agent.
    #: This constant has a value of "APPLIANCE"
    AGENT_TYPE_APPLIANCE = "APPLIANCE"

    #: A constant which can be used with the heart_beat_status property of a Agent.
    #: This constant has a value of "HEALTHY"
    HEART_BEAT_STATUS_HEALTHY = "HEALTHY"

    #: A constant which can be used with the heart_beat_status property of a Agent.
    #: This constant has a value of "UNHEALTHY"
    HEART_BEAT_STATUS_UNHEALTHY = "UNHEALTHY"

    #: A constant which can be used with the heart_beat_status property of a Agent.
    #: This constant has a value of "FAILED"
    HEART_BEAT_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the heart_beat_status property of a Agent.
    #: This constant has a value of "INACTIVE"
    HEART_BEAT_STATUS_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Agent.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Agent.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Agent.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Agent.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Agent.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Agent object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Agent.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Agent.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Agent.
        :type compartment_id: str

        :param agent_type:
            The value to assign to the agent_type property of this Agent.
            Allowed values for this property are: "APPLIANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type agent_type: str

        :param agent_version:
            The value to assign to the agent_version property of this Agent.
        :type agent_version: str

        :param os_version:
            The value to assign to the os_version property of this Agent.
        :type os_version: str

        :param time_created:
            The value to assign to the time_created property of this Agent.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Agent.
        :type time_updated: datetime

        :param time_last_sync_received:
            The value to assign to the time_last_sync_received property of this Agent.
        :type time_last_sync_received: datetime

        :param heart_beat_status:
            The value to assign to the heart_beat_status property of this Agent.
            Allowed values for this property are: "HEALTHY", "UNHEALTHY", "FAILED", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type heart_beat_status: str

        :param environment_id:
            The value to assign to the environment_id property of this Agent.
        :type environment_id: str

        :param agent_pub_key:
            The value to assign to the agent_pub_key property of this Agent.
        :type agent_pub_key: str

        :param time_expire_agent_key_in_ms:
            The value to assign to the time_expire_agent_key_in_ms property of this Agent.
        :type time_expire_agent_key_in_ms: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Agent.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Agent.
        :type lifecycle_details: str

        :param plugin_list:
            The value to assign to the plugin_list property of this Agent.
        :type plugin_list: list[oci.cloud_bridge.models.PluginSummary]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Agent.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Agent.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Agent.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'agent_type': 'str',
            'agent_version': 'str',
            'os_version': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_last_sync_received': 'datetime',
            'heart_beat_status': 'str',
            'environment_id': 'str',
            'agent_pub_key': 'str',
            'time_expire_agent_key_in_ms': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'plugin_list': 'list[PluginSummary]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'agent_type': 'agentType',
            'agent_version': 'agentVersion',
            'os_version': 'osVersion',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_last_sync_received': 'timeLastSyncReceived',
            'heart_beat_status': 'heartBeatStatus',
            'environment_id': 'environmentId',
            'agent_pub_key': 'agentPubKey',
            'time_expire_agent_key_in_ms': 'timeExpireAgentKeyInMs',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'plugin_list': 'pluginList',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._agent_type = None
        self._agent_version = None
        self._os_version = None
        self._time_created = None
        self._time_updated = None
        self._time_last_sync_received = None
        self._heart_beat_status = None
        self._environment_id = None
        self._agent_pub_key = None
        self._time_expire_agent_key_in_ms = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._plugin_list = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Agent.
        Unique identifier that is immutable on creation.


        :return: The id of this Agent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Agent.
        Unique identifier that is immutable on creation.


        :param id: The id of this Agent.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Agent.
        Agent identifier, can be renamed.


        :return: The display_name of this Agent.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Agent.
        Agent identifier, can be renamed.


        :param display_name: The display_name of this Agent.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Agent.
        Compartment identifier.


        :return: The compartment_id of this Agent.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Agent.
        Compartment identifier.


        :param compartment_id: The compartment_id of this Agent.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def agent_type(self):
        """
        **[Required]** Gets the agent_type of this Agent.
        Type of the Agent.

        Allowed values for this property are: "APPLIANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The agent_type of this Agent.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        """
        Sets the agent_type of this Agent.
        Type of the Agent.


        :param agent_type: The agent_type of this Agent.
        :type: str
        """
        allowed_values = ["APPLIANCE"]
        if not value_allowed_none_or_none_sentinel(agent_type, allowed_values):
            agent_type = 'UNKNOWN_ENUM_VALUE'
        self._agent_type = agent_type

    @property
    def agent_version(self):
        """
        **[Required]** Gets the agent_version of this Agent.
        Agent identifier.


        :return: The agent_version of this Agent.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """
        Sets the agent_version of this Agent.
        Agent identifier.


        :param agent_version: The agent_version of this Agent.
        :type: str
        """
        self._agent_version = agent_version

    @property
    def os_version(self):
        """
        **[Required]** Gets the os_version of this Agent.
        OS version.


        :return: The os_version of this Agent.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """
        Sets the os_version of this Agent.
        OS version.


        :param os_version: The os_version of this Agent.
        :type: str
        """
        self._os_version = os_version

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Agent.
        The time when the Agent was created. An RFC3339 formatted datetime string.


        :return: The time_created of this Agent.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Agent.
        The time when the Agent was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this Agent.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Agent.
        The time when the Agent was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this Agent.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Agent.
        The time when the Agent was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this Agent.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_last_sync_received(self):
        """
        Gets the time_last_sync_received of this Agent.
        The time when the last heartbeat of the Agent was noted. An RFC3339 formatted datetime string.


        :return: The time_last_sync_received of this Agent.
        :rtype: datetime
        """
        return self._time_last_sync_received

    @time_last_sync_received.setter
    def time_last_sync_received(self, time_last_sync_received):
        """
        Sets the time_last_sync_received of this Agent.
        The time when the last heartbeat of the Agent was noted. An RFC3339 formatted datetime string.


        :param time_last_sync_received: The time_last_sync_received of this Agent.
        :type: datetime
        """
        self._time_last_sync_received = time_last_sync_received

    @property
    def heart_beat_status(self):
        """
        Gets the heart_beat_status of this Agent.
        The current heartbeat status of the Agent based on its timeLastSyncReceived value.

        Allowed values for this property are: "HEALTHY", "UNHEALTHY", "FAILED", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The heart_beat_status of this Agent.
        :rtype: str
        """
        return self._heart_beat_status

    @heart_beat_status.setter
    def heart_beat_status(self, heart_beat_status):
        """
        Sets the heart_beat_status of this Agent.
        The current heartbeat status of the Agent based on its timeLastSyncReceived value.


        :param heart_beat_status: The heart_beat_status of this Agent.
        :type: str
        """
        allowed_values = ["HEALTHY", "UNHEALTHY", "FAILED", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(heart_beat_status, allowed_values):
            heart_beat_status = 'UNKNOWN_ENUM_VALUE'
        self._heart_beat_status = heart_beat_status

    @property
    def environment_id(self):
        """
        **[Required]** Gets the environment_id of this Agent.
        Environment identifier.


        :return: The environment_id of this Agent.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """
        Sets the environment_id of this Agent.
        Environment identifier.


        :param environment_id: The environment_id of this Agent.
        :type: str
        """
        self._environment_id = environment_id

    @property
    def agent_pub_key(self):
        """
        Gets the agent_pub_key of this Agent.
        Resource principal public key.


        :return: The agent_pub_key of this Agent.
        :rtype: str
        """
        return self._agent_pub_key

    @agent_pub_key.setter
    def agent_pub_key(self, agent_pub_key):
        """
        Sets the agent_pub_key of this Agent.
        Resource principal public key.


        :param agent_pub_key: The agent_pub_key of this Agent.
        :type: str
        """
        self._agent_pub_key = agent_pub_key

    @property
    def time_expire_agent_key_in_ms(self):
        """
        Gets the time_expire_agent_key_in_ms of this Agent.
        The time since epoch for when the public key will expire. An RFC3339 formatted datetime string.


        :return: The time_expire_agent_key_in_ms of this Agent.
        :rtype: datetime
        """
        return self._time_expire_agent_key_in_ms

    @time_expire_agent_key_in_ms.setter
    def time_expire_agent_key_in_ms(self, time_expire_agent_key_in_ms):
        """
        Sets the time_expire_agent_key_in_ms of this Agent.
        The time since epoch for when the public key will expire. An RFC3339 formatted datetime string.


        :param time_expire_agent_key_in_ms: The time_expire_agent_key_in_ms of this Agent.
        :type: datetime
        """
        self._time_expire_agent_key_in_ms = time_expire_agent_key_in_ms

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Agent.
        The current state of the Agent.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Agent.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Agent.
        The current state of the Agent.


        :param lifecycle_state: The lifecycle_state of this Agent.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Agent.
        A message describing the current state of the Agent in more detail. For example, it can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this Agent.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Agent.
        A message describing the current state of the Agent in more detail. For example, it can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this Agent.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def plugin_list(self):
        """
        Gets the plugin_list of this Agent.
        List of plugins associated with the agent.


        :return: The plugin_list of this Agent.
        :rtype: list[oci.cloud_bridge.models.PluginSummary]
        """
        return self._plugin_list

    @plugin_list.setter
    def plugin_list(self, plugin_list):
        """
        Sets the plugin_list of this Agent.
        List of plugins associated with the agent.


        :param plugin_list: The plugin_list of this Agent.
        :type: list[oci.cloud_bridge.models.PluginSummary]
        """
        self._plugin_list = plugin_list

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this Agent.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Agent.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Agent.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Agent.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this Agent.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Agent.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Agent.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Agent.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Agent.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this Agent.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Agent.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this Agent.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
