# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PluginSummary(object):
    """
    Summary of the plugin in an Agent.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PluginSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this PluginSummary.
        :type name: str

        :param agent_id:
            The value to assign to the agent_id property of this PluginSummary.
        :type agent_id: str

        :param plugin_version:
            The value to assign to the plugin_version property of this PluginSummary.
        :type plugin_version: str

        :param time_created:
            The value to assign to the time_created property of this PluginSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this PluginSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PluginSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this PluginSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PluginSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this PluginSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'agent_id': 'str',
            'plugin_version': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'agent_id': 'agentId',
            'plugin_version': 'pluginVersion',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._name = None
        self._agent_id = None
        self._plugin_version = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this PluginSummary.
        Plugin identifier, which can be renamed.


        :return: The name of this PluginSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PluginSummary.
        Plugin identifier, which can be renamed.


        :param name: The name of this PluginSummary.
        :type: str
        """
        self._name = name

    @property
    def agent_id(self):
        """
        **[Required]** Gets the agent_id of this PluginSummary.
        Agent identifier.


        :return: The agent_id of this PluginSummary.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this PluginSummary.
        Agent identifier.


        :param agent_id: The agent_id of this PluginSummary.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def plugin_version(self):
        """
        **[Required]** Gets the plugin_version of this PluginSummary.
        Plugin version.


        :return: The plugin_version of this PluginSummary.
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        """
        Sets the plugin_version of this PluginSummary.
        Plugin version.


        :param plugin_version: The plugin_version of this PluginSummary.
        :type: str
        """
        self._plugin_version = plugin_version

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PluginSummary.
        The time when the plugin was created. An RFC3339 formatted datetime string.


        :return: The time_created of this PluginSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PluginSummary.
        The time when the plugin was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this PluginSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this PluginSummary.
        The time when the plugin was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this PluginSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this PluginSummary.
        The time when the plugin was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this PluginSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this PluginSummary.
        The current state of the plugin.


        :return: The lifecycle_state of this PluginSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PluginSummary.
        The current state of the plugin.


        :param lifecycle_state: The lifecycle_state of this PluginSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this PluginSummary.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this PluginSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this PluginSummary.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this PluginSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this PluginSummary.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this PluginSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this PluginSummary.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this PluginSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this PluginSummary.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this PluginSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this PluginSummary.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this PluginSummary.
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
