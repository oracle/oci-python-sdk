# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagementAgentSummary(object):
    """
    The summary of the Management Agent inventory including the associated plugins.
    """

    #: A constant which can be used with the platform_type property of a ManagementAgentSummary.
    #: This constant has a value of "LINUX"
    PLATFORM_TYPE_LINUX = "LINUX"

    #: A constant which can be used with the platform_type property of a ManagementAgentSummary.
    #: This constant has a value of "WINDOWS"
    PLATFORM_TYPE_WINDOWS = "WINDOWS"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentSummary.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagementAgentSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ManagementAgentSummary.
        :type id: str

        :param install_key_id:
            The value to assign to the install_key_id property of this ManagementAgentSummary.
        :type install_key_id: str

        :param display_name:
            The value to assign to the display_name property of this ManagementAgentSummary.
        :type display_name: str

        :param platform_type:
            The value to assign to the platform_type property of this ManagementAgentSummary.
            Allowed values for this property are: "LINUX", "WINDOWS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type platform_type: str

        :param platform_name:
            The value to assign to the platform_name property of this ManagementAgentSummary.
        :type platform_name: str

        :param platform_version:
            The value to assign to the platform_version property of this ManagementAgentSummary.
        :type platform_version: str

        :param version:
            The value to assign to the version property of this ManagementAgentSummary.
        :type version: str

        :param is_agent_auto_upgradable:
            The value to assign to the is_agent_auto_upgradable property of this ManagementAgentSummary.
        :type is_agent_auto_upgradable: bool

        :param time_created:
            The value to assign to the time_created property of this ManagementAgentSummary.
        :type time_created: datetime

        :param host:
            The value to assign to the host property of this ManagementAgentSummary.
        :type host: str

        :param plugin_list:
            The value to assign to the plugin_list property of this ManagementAgentSummary.
        :type plugin_list: list[ManagementAgentPluginDetails]

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagementAgentSummary.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ManagementAgentSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ManagementAgentSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ManagementAgentSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ManagementAgentSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'install_key_id': 'str',
            'display_name': 'str',
            'platform_type': 'str',
            'platform_name': 'str',
            'platform_version': 'str',
            'version': 'str',
            'is_agent_auto_upgradable': 'bool',
            'time_created': 'datetime',
            'host': 'str',
            'plugin_list': 'list[ManagementAgentPluginDetails]',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'install_key_id': 'installKeyId',
            'display_name': 'displayName',
            'platform_type': 'platformType',
            'platform_name': 'platformName',
            'platform_version': 'platformVersion',
            'version': 'version',
            'is_agent_auto_upgradable': 'isAgentAutoUpgradable',
            'time_created': 'timeCreated',
            'host': 'host',
            'plugin_list': 'pluginList',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._install_key_id = None
        self._display_name = None
        self._platform_type = None
        self._platform_name = None
        self._platform_version = None
        self._version = None
        self._is_agent_auto_upgradable = None
        self._time_created = None
        self._host = None
        self._plugin_list = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagementAgentSummary.
        agent identifier


        :return: The id of this ManagementAgentSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagementAgentSummary.
        agent identifier


        :param id: The id of this ManagementAgentSummary.
        :type: str
        """
        self._id = id

    @property
    def install_key_id(self):
        """
        Gets the install_key_id of this ManagementAgentSummary.
        agent install key identifier


        :return: The install_key_id of this ManagementAgentSummary.
        :rtype: str
        """
        return self._install_key_id

    @install_key_id.setter
    def install_key_id(self, install_key_id):
        """
        Sets the install_key_id of this ManagementAgentSummary.
        agent install key identifier


        :param install_key_id: The install_key_id of this ManagementAgentSummary.
        :type: str
        """
        self._install_key_id = install_key_id

    @property
    def display_name(self):
        """
        Gets the display_name of this ManagementAgentSummary.
        Management Agent Name


        :return: The display_name of this ManagementAgentSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagementAgentSummary.
        Management Agent Name


        :param display_name: The display_name of this ManagementAgentSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def platform_type(self):
        """
        Gets the platform_type of this ManagementAgentSummary.
        Platform Type

        Allowed values for this property are: "LINUX", "WINDOWS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The platform_type of this ManagementAgentSummary.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """
        Sets the platform_type of this ManagementAgentSummary.
        Platform Type


        :param platform_type: The platform_type of this ManagementAgentSummary.
        :type: str
        """
        allowed_values = ["LINUX", "WINDOWS"]
        if not value_allowed_none_or_none_sentinel(platform_type, allowed_values):
            platform_type = 'UNKNOWN_ENUM_VALUE'
        self._platform_type = platform_type

    @property
    def platform_name(self):
        """
        Gets the platform_name of this ManagementAgentSummary.
        Platform Name


        :return: The platform_name of this ManagementAgentSummary.
        :rtype: str
        """
        return self._platform_name

    @platform_name.setter
    def platform_name(self, platform_name):
        """
        Sets the platform_name of this ManagementAgentSummary.
        Platform Name


        :param platform_name: The platform_name of this ManagementAgentSummary.
        :type: str
        """
        self._platform_name = platform_name

    @property
    def platform_version(self):
        """
        Gets the platform_version of this ManagementAgentSummary.
        Platform Version


        :return: The platform_version of this ManagementAgentSummary.
        :rtype: str
        """
        return self._platform_version

    @platform_version.setter
    def platform_version(self, platform_version):
        """
        Sets the platform_version of this ManagementAgentSummary.
        Platform Version


        :param platform_version: The platform_version of this ManagementAgentSummary.
        :type: str
        """
        self._platform_version = platform_version

    @property
    def version(self):
        """
        **[Required]** Gets the version of this ManagementAgentSummary.
        Management Agent Version


        :return: The version of this ManagementAgentSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ManagementAgentSummary.
        Management Agent Version


        :param version: The version of this ManagementAgentSummary.
        :type: str
        """
        self._version = version

    @property
    def is_agent_auto_upgradable(self):
        """
        Gets the is_agent_auto_upgradable of this ManagementAgentSummary.
        true if the agent can be upgraded automatically; false if it must be upgraded manually. true is currently unsupported.


        :return: The is_agent_auto_upgradable of this ManagementAgentSummary.
        :rtype: bool
        """
        return self._is_agent_auto_upgradable

    @is_agent_auto_upgradable.setter
    def is_agent_auto_upgradable(self, is_agent_auto_upgradable):
        """
        Sets the is_agent_auto_upgradable of this ManagementAgentSummary.
        true if the agent can be upgraded automatically; false if it must be upgraded manually. true is currently unsupported.


        :param is_agent_auto_upgradable: The is_agent_auto_upgradable of this ManagementAgentSummary.
        :type: bool
        """
        self._is_agent_auto_upgradable = is_agent_auto_upgradable

    @property
    def time_created(self):
        """
        Gets the time_created of this ManagementAgentSummary.
        The time the Management Agent was created. An RFC3339 formatted datetime string


        :return: The time_created of this ManagementAgentSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ManagementAgentSummary.
        The time the Management Agent was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this ManagementAgentSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def host(self):
        """
        Gets the host of this ManagementAgentSummary.
        Management Agent host machine name


        :return: The host of this ManagementAgentSummary.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this ManagementAgentSummary.
        Management Agent host machine name


        :param host: The host of this ManagementAgentSummary.
        :type: str
        """
        self._host = host

    @property
    def plugin_list(self):
        """
        Gets the plugin_list of this ManagementAgentSummary.
        list of managementAgentPlugins associated with the agent


        :return: The plugin_list of this ManagementAgentSummary.
        :rtype: list[ManagementAgentPluginDetails]
        """
        return self._plugin_list

    @plugin_list.setter
    def plugin_list(self, plugin_list):
        """
        Sets the plugin_list of this ManagementAgentSummary.
        list of managementAgentPlugins associated with the agent


        :param plugin_list: The plugin_list of this ManagementAgentSummary.
        :type: list[ManagementAgentPluginDetails]
        """
        self._plugin_list = plugin_list

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagementAgentSummary.
        Compartment Identifier


        :return: The compartment_id of this ManagementAgentSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagementAgentSummary.
        Compartment Identifier


        :param compartment_id: The compartment_id of this ManagementAgentSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ManagementAgentSummary.
        The current state of managementAgent

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ManagementAgentSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ManagementAgentSummary.
        The current state of managementAgent


        :param lifecycle_state: The lifecycle_state of this ManagementAgentSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ManagementAgentSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this ManagementAgentSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ManagementAgentSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this ManagementAgentSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ManagementAgentSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ManagementAgentSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ManagementAgentSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ManagementAgentSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ManagementAgentSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ManagementAgentSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ManagementAgentSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ManagementAgentSummary.
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
