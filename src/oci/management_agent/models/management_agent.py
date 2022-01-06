# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagementAgent(object):
    """
    The details of the Management Agent inventory including the associated plugins.
    """

    #: A constant which can be used with the platform_type property of a ManagementAgent.
    #: This constant has a value of "LINUX"
    PLATFORM_TYPE_LINUX = "LINUX"

    #: A constant which can be used with the platform_type property of a ManagementAgent.
    #: This constant has a value of "WINDOWS"
    PLATFORM_TYPE_WINDOWS = "WINDOWS"

    #: A constant which can be used with the platform_type property of a ManagementAgent.
    #: This constant has a value of "SOLARIS"
    PLATFORM_TYPE_SOLARIS = "SOLARIS"

    #: A constant which can be used with the availability_status property of a ManagementAgent.
    #: This constant has a value of "ACTIVE"
    AVAILABILITY_STATUS_ACTIVE = "ACTIVE"

    #: A constant which can be used with the availability_status property of a ManagementAgent.
    #: This constant has a value of "SILENT"
    AVAILABILITY_STATUS_SILENT = "SILENT"

    #: A constant which can be used with the availability_status property of a ManagementAgent.
    #: This constant has a value of "NOT_AVAILABLE"
    AVAILABILITY_STATUS_NOT_AVAILABLE = "NOT_AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgent.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgent.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgent.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgent.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgent.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgent.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgent.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgent.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the install_type property of a ManagementAgent.
    #: This constant has a value of "AGENT"
    INSTALL_TYPE_AGENT = "AGENT"

    #: A constant which can be used with the install_type property of a ManagementAgent.
    #: This constant has a value of "GATEWAY"
    INSTALL_TYPE_GATEWAY = "GATEWAY"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagementAgent object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ManagementAgent.
        :type id: str

        :param install_key_id:
            The value to assign to the install_key_id property of this ManagementAgent.
        :type install_key_id: str

        :param display_name:
            The value to assign to the display_name property of this ManagementAgent.
        :type display_name: str

        :param platform_type:
            The value to assign to the platform_type property of this ManagementAgent.
            Allowed values for this property are: "LINUX", "WINDOWS", "SOLARIS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type platform_type: str

        :param platform_name:
            The value to assign to the platform_name property of this ManagementAgent.
        :type platform_name: str

        :param platform_version:
            The value to assign to the platform_version property of this ManagementAgent.
        :type platform_version: str

        :param version:
            The value to assign to the version property of this ManagementAgent.
        :type version: str

        :param resource_artifact_version:
            The value to assign to the resource_artifact_version property of this ManagementAgent.
        :type resource_artifact_version: str

        :param host:
            The value to assign to the host property of this ManagementAgent.
        :type host: str

        :param host_id:
            The value to assign to the host_id property of this ManagementAgent.
        :type host_id: str

        :param install_path:
            The value to assign to the install_path property of this ManagementAgent.
        :type install_path: str

        :param plugin_list:
            The value to assign to the plugin_list property of this ManagementAgent.
        :type plugin_list: list[oci.management_agent.models.ManagementAgentPluginDetails]

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagementAgent.
        :type compartment_id: str

        :param is_agent_auto_upgradable:
            The value to assign to the is_agent_auto_upgradable property of this ManagementAgent.
        :type is_agent_auto_upgradable: bool

        :param time_created:
            The value to assign to the time_created property of this ManagementAgent.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ManagementAgent.
        :type time_updated: datetime

        :param time_last_heartbeat:
            The value to assign to the time_last_heartbeat property of this ManagementAgent.
        :type time_last_heartbeat: datetime

        :param availability_status:
            The value to assign to the availability_status property of this ManagementAgent.
            Allowed values for this property are: "ACTIVE", "SILENT", "NOT_AVAILABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type availability_status: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ManagementAgent.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ManagementAgent.
        :type lifecycle_details: str

        :param is_customer_deployed:
            The value to assign to the is_customer_deployed property of this ManagementAgent.
        :type is_customer_deployed: bool

        :param install_type:
            The value to assign to the install_type property of this ManagementAgent.
            Allowed values for this property are: "AGENT", "GATEWAY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type install_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ManagementAgent.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ManagementAgent.
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
            'resource_artifact_version': 'str',
            'host': 'str',
            'host_id': 'str',
            'install_path': 'str',
            'plugin_list': 'list[ManagementAgentPluginDetails]',
            'compartment_id': 'str',
            'is_agent_auto_upgradable': 'bool',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_last_heartbeat': 'datetime',
            'availability_status': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'is_customer_deployed': 'bool',
            'install_type': 'str',
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
            'resource_artifact_version': 'resourceArtifactVersion',
            'host': 'host',
            'host_id': 'hostId',
            'install_path': 'installPath',
            'plugin_list': 'pluginList',
            'compartment_id': 'compartmentId',
            'is_agent_auto_upgradable': 'isAgentAutoUpgradable',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_last_heartbeat': 'timeLastHeartbeat',
            'availability_status': 'availabilityStatus',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'is_customer_deployed': 'isCustomerDeployed',
            'install_type': 'installType',
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
        self._resource_artifact_version = None
        self._host = None
        self._host_id = None
        self._install_path = None
        self._plugin_list = None
        self._compartment_id = None
        self._is_agent_auto_upgradable = None
        self._time_created = None
        self._time_updated = None
        self._time_last_heartbeat = None
        self._availability_status = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._is_customer_deployed = None
        self._install_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagementAgent.
        agent identifier


        :return: The id of this ManagementAgent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagementAgent.
        agent identifier


        :param id: The id of this ManagementAgent.
        :type: str
        """
        self._id = id

    @property
    def install_key_id(self):
        """
        Gets the install_key_id of this ManagementAgent.
        agent install key identifier


        :return: The install_key_id of this ManagementAgent.
        :rtype: str
        """
        return self._install_key_id

    @install_key_id.setter
    def install_key_id(self, install_key_id):
        """
        Sets the install_key_id of this ManagementAgent.
        agent install key identifier


        :param install_key_id: The install_key_id of this ManagementAgent.
        :type: str
        """
        self._install_key_id = install_key_id

    @property
    def display_name(self):
        """
        Gets the display_name of this ManagementAgent.
        Management Agent Name


        :return: The display_name of this ManagementAgent.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagementAgent.
        Management Agent Name


        :param display_name: The display_name of this ManagementAgent.
        :type: str
        """
        self._display_name = display_name

    @property
    def platform_type(self):
        """
        Gets the platform_type of this ManagementAgent.
        Platform Type

        Allowed values for this property are: "LINUX", "WINDOWS", "SOLARIS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The platform_type of this ManagementAgent.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """
        Sets the platform_type of this ManagementAgent.
        Platform Type


        :param platform_type: The platform_type of this ManagementAgent.
        :type: str
        """
        allowed_values = ["LINUX", "WINDOWS", "SOLARIS"]
        if not value_allowed_none_or_none_sentinel(platform_type, allowed_values):
            platform_type = 'UNKNOWN_ENUM_VALUE'
        self._platform_type = platform_type

    @property
    def platform_name(self):
        """
        Gets the platform_name of this ManagementAgent.
        Platform Name


        :return: The platform_name of this ManagementAgent.
        :rtype: str
        """
        return self._platform_name

    @platform_name.setter
    def platform_name(self, platform_name):
        """
        Sets the platform_name of this ManagementAgent.
        Platform Name


        :param platform_name: The platform_name of this ManagementAgent.
        :type: str
        """
        self._platform_name = platform_name

    @property
    def platform_version(self):
        """
        Gets the platform_version of this ManagementAgent.
        Platform Version


        :return: The platform_version of this ManagementAgent.
        :rtype: str
        """
        return self._platform_version

    @platform_version.setter
    def platform_version(self, platform_version):
        """
        Sets the platform_version of this ManagementAgent.
        Platform Version


        :param platform_version: The platform_version of this ManagementAgent.
        :type: str
        """
        self._platform_version = platform_version

    @property
    def version(self):
        """
        **[Required]** Gets the version of this ManagementAgent.
        Management Agent Version


        :return: The version of this ManagementAgent.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ManagementAgent.
        Management Agent Version


        :param version: The version of this ManagementAgent.
        :type: str
        """
        self._version = version

    @property
    def resource_artifact_version(self):
        """
        Gets the resource_artifact_version of this ManagementAgent.
        Version of the deployment artifact instantiated by this Management Agent.
        The format for Standalone resourceMode is YYMMDD.HHMM, and the format for other modes
        (whose artifacts are based upon Standalone but can advance independently)
        is YYMMDD.HHMM.VVVVVVVVVVVV.
        VVVVVVVVVVVV is always a numeric value between 000000000000 and 999999999999


        :return: The resource_artifact_version of this ManagementAgent.
        :rtype: str
        """
        return self._resource_artifact_version

    @resource_artifact_version.setter
    def resource_artifact_version(self, resource_artifact_version):
        """
        Sets the resource_artifact_version of this ManagementAgent.
        Version of the deployment artifact instantiated by this Management Agent.
        The format for Standalone resourceMode is YYMMDD.HHMM, and the format for other modes
        (whose artifacts are based upon Standalone but can advance independently)
        is YYMMDD.HHMM.VVVVVVVVVVVV.
        VVVVVVVVVVVV is always a numeric value between 000000000000 and 999999999999


        :param resource_artifact_version: The resource_artifact_version of this ManagementAgent.
        :type: str
        """
        self._resource_artifact_version = resource_artifact_version

    @property
    def host(self):
        """
        Gets the host of this ManagementAgent.
        Management Agent host machine name


        :return: The host of this ManagementAgent.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this ManagementAgent.
        Management Agent host machine name


        :param host: The host of this ManagementAgent.
        :type: str
        """
        self._host = host

    @property
    def host_id(self):
        """
        Gets the host_id of this ManagementAgent.
        Host resource ocid


        :return: The host_id of this ManagementAgent.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """
        Sets the host_id of this ManagementAgent.
        Host resource ocid


        :param host_id: The host_id of this ManagementAgent.
        :type: str
        """
        self._host_id = host_id

    @property
    def install_path(self):
        """
        Gets the install_path of this ManagementAgent.
        Path where Management Agent is installed


        :return: The install_path of this ManagementAgent.
        :rtype: str
        """
        return self._install_path

    @install_path.setter
    def install_path(self, install_path):
        """
        Sets the install_path of this ManagementAgent.
        Path where Management Agent is installed


        :param install_path: The install_path of this ManagementAgent.
        :type: str
        """
        self._install_path = install_path

    @property
    def plugin_list(self):
        """
        Gets the plugin_list of this ManagementAgent.
        list of managementAgentPlugins associated with the agent


        :return: The plugin_list of this ManagementAgent.
        :rtype: list[oci.management_agent.models.ManagementAgentPluginDetails]
        """
        return self._plugin_list

    @plugin_list.setter
    def plugin_list(self, plugin_list):
        """
        Sets the plugin_list of this ManagementAgent.
        list of managementAgentPlugins associated with the agent


        :param plugin_list: The plugin_list of this ManagementAgent.
        :type: list[oci.management_agent.models.ManagementAgentPluginDetails]
        """
        self._plugin_list = plugin_list

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagementAgent.
        Compartment Identifier


        :return: The compartment_id of this ManagementAgent.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagementAgent.
        Compartment Identifier


        :param compartment_id: The compartment_id of this ManagementAgent.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_agent_auto_upgradable(self):
        """
        Gets the is_agent_auto_upgradable of this ManagementAgent.
        true if the agent can be upgraded automatically; false if it must be upgraded manually. This flag is derived from the tenancy level auto upgrade preference.


        :return: The is_agent_auto_upgradable of this ManagementAgent.
        :rtype: bool
        """
        return self._is_agent_auto_upgradable

    @is_agent_auto_upgradable.setter
    def is_agent_auto_upgradable(self, is_agent_auto_upgradable):
        """
        Sets the is_agent_auto_upgradable of this ManagementAgent.
        true if the agent can be upgraded automatically; false if it must be upgraded manually. This flag is derived from the tenancy level auto upgrade preference.


        :param is_agent_auto_upgradable: The is_agent_auto_upgradable of this ManagementAgent.
        :type: bool
        """
        self._is_agent_auto_upgradable = is_agent_auto_upgradable

    @property
    def time_created(self):
        """
        Gets the time_created of this ManagementAgent.
        The time the Management Agent was created. An RFC3339 formatted datetime string


        :return: The time_created of this ManagementAgent.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ManagementAgent.
        The time the Management Agent was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this ManagementAgent.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ManagementAgent.
        The time the Management Agent was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this ManagementAgent.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ManagementAgent.
        The time the Management Agent was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this ManagementAgent.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_last_heartbeat(self):
        """
        Gets the time_last_heartbeat of this ManagementAgent.
        The time the Management Agent has last recorded its health status in telemetry. This value will be null if the agent has not recorded its health status in last 7 days. An RFC3339 formatted datetime string


        :return: The time_last_heartbeat of this ManagementAgent.
        :rtype: datetime
        """
        return self._time_last_heartbeat

    @time_last_heartbeat.setter
    def time_last_heartbeat(self, time_last_heartbeat):
        """
        Sets the time_last_heartbeat of this ManagementAgent.
        The time the Management Agent has last recorded its health status in telemetry. This value will be null if the agent has not recorded its health status in last 7 days. An RFC3339 formatted datetime string


        :param time_last_heartbeat: The time_last_heartbeat of this ManagementAgent.
        :type: datetime
        """
        self._time_last_heartbeat = time_last_heartbeat

    @property
    def availability_status(self):
        """
        Gets the availability_status of this ManagementAgent.
        The current availability status of managementAgent

        Allowed values for this property are: "ACTIVE", "SILENT", "NOT_AVAILABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The availability_status of this ManagementAgent.
        :rtype: str
        """
        return self._availability_status

    @availability_status.setter
    def availability_status(self, availability_status):
        """
        Sets the availability_status of this ManagementAgent.
        The current availability status of managementAgent


        :param availability_status: The availability_status of this ManagementAgent.
        :type: str
        """
        allowed_values = ["ACTIVE", "SILENT", "NOT_AVAILABLE"]
        if not value_allowed_none_or_none_sentinel(availability_status, allowed_values):
            availability_status = 'UNKNOWN_ENUM_VALUE'
        self._availability_status = availability_status

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ManagementAgent.
        The current state of managementAgent

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ManagementAgent.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ManagementAgent.
        The current state of managementAgent


        :param lifecycle_state: The lifecycle_state of this ManagementAgent.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ManagementAgent.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this ManagementAgent.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ManagementAgent.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this ManagementAgent.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def is_customer_deployed(self):
        """
        Gets the is_customer_deployed of this ManagementAgent.
        true, if the agent image is manually downloaded and installed. false, if the agent is deployed as a plugin in Oracle Cloud Agent.


        :return: The is_customer_deployed of this ManagementAgent.
        :rtype: bool
        """
        return self._is_customer_deployed

    @is_customer_deployed.setter
    def is_customer_deployed(self, is_customer_deployed):
        """
        Sets the is_customer_deployed of this ManagementAgent.
        true, if the agent image is manually downloaded and installed. false, if the agent is deployed as a plugin in Oracle Cloud Agent.


        :param is_customer_deployed: The is_customer_deployed of this ManagementAgent.
        :type: bool
        """
        self._is_customer_deployed = is_customer_deployed

    @property
    def install_type(self):
        """
        Gets the install_type of this ManagementAgent.
        The install type, either AGENT or GATEWAY

        Allowed values for this property are: "AGENT", "GATEWAY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The install_type of this ManagementAgent.
        :rtype: str
        """
        return self._install_type

    @install_type.setter
    def install_type(self, install_type):
        """
        Sets the install_type of this ManagementAgent.
        The install type, either AGENT or GATEWAY


        :param install_type: The install_type of this ManagementAgent.
        :type: str
        """
        allowed_values = ["AGENT", "GATEWAY"]
        if not value_allowed_none_or_none_sentinel(install_type, allowed_values):
            install_type = 'UNKNOWN_ENUM_VALUE'
        self._install_type = install_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ManagementAgent.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ManagementAgent.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ManagementAgent.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ManagementAgent.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ManagementAgent.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ManagementAgent.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ManagementAgent.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ManagementAgent.
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
