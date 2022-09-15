# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IngestTimeRule(object):
    """
    An ingest time rule object.
    """

    #: A constant which can be used with the lifecycle_state property of a IngestTimeRule.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a IngestTimeRule.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new IngestTimeRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this IngestTimeRule.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this IngestTimeRule.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this IngestTimeRule.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this IngestTimeRule.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this IngestTimeRule.
        :type defined_tags: dict(str, dict(str, object))

        :param time_created:
            The value to assign to the time_created property of this IngestTimeRule.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this IngestTimeRule.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this IngestTimeRule.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param display_name:
            The value to assign to the display_name property of this IngestTimeRule.
        :type display_name: str

        :param is_enabled:
            The value to assign to the is_enabled property of this IngestTimeRule.
        :type is_enabled: bool

        :param conditions:
            The value to assign to the conditions property of this IngestTimeRule.
        :type conditions: oci.log_analytics.models.IngestTimeRuleCondition

        :param actions:
            The value to assign to the actions property of this IngestTimeRule.
        :type actions: list[oci.log_analytics.models.IngestTimeRuleAction]

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'display_name': 'str',
            'is_enabled': 'bool',
            'conditions': 'IngestTimeRuleCondition',
            'actions': 'list[IngestTimeRuleAction]'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'display_name': 'displayName',
            'is_enabled': 'isEnabled',
            'conditions': 'conditions',
            'actions': 'actions'
        }

        self._id = None
        self._compartment_id = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._display_name = None
        self._is_enabled = None
        self._conditions = None
        self._actions = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this IngestTimeRule.
        The log analytics entity OCID. This ID is a reference used by log analytics features and it represents
        a resource that is provisioned and managed by the customer on their premises or on the cloud.


        :return: The id of this IngestTimeRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IngestTimeRule.
        The log analytics entity OCID. This ID is a reference used by log analytics features and it represents
        a resource that is provisioned and managed by the customer on their premises or on the cloud.


        :param id: The id of this IngestTimeRule.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this IngestTimeRule.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this IngestTimeRule.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IngestTimeRule.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this IngestTimeRule.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this IngestTimeRule.
        Description for this resource.


        :return: The description of this IngestTimeRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this IngestTimeRule.
        Description for this resource.


        :param description: The description of this IngestTimeRule.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this IngestTimeRule.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this IngestTimeRule.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this IngestTimeRule.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this IngestTimeRule.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this IngestTimeRule.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this IngestTimeRule.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this IngestTimeRule.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this IngestTimeRule.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def time_created(self):
        """
        Gets the time_created of this IngestTimeRule.
        The date and time the resource was created, in the format defined by RFC3339.


        :return: The time_created of this IngestTimeRule.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this IngestTimeRule.
        The date and time the resource was created, in the format defined by RFC3339.


        :param time_created: The time_created of this IngestTimeRule.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this IngestTimeRule.
        The date and time the resource was last updated, in the format defined by RFC3339.


        :return: The time_updated of this IngestTimeRule.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this IngestTimeRule.
        The date and time the resource was last updated, in the format defined by RFC3339.


        :param time_updated: The time_updated of this IngestTimeRule.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this IngestTimeRule.
        The current state of the ingest time rule.

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this IngestTimeRule.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this IngestTimeRule.
        The current state of the ingest time rule.


        :param lifecycle_state: The lifecycle_state of this IngestTimeRule.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this IngestTimeRule.
        The ingest time rule display name.


        :return: The display_name of this IngestTimeRule.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this IngestTimeRule.
        The ingest time rule display name.


        :param display_name: The display_name of this IngestTimeRule.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this IngestTimeRule.
        A flag indicating whether or not the ingest time rule is enabled.


        :return: The is_enabled of this IngestTimeRule.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this IngestTimeRule.
        A flag indicating whether or not the ingest time rule is enabled.


        :param is_enabled: The is_enabled of this IngestTimeRule.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def conditions(self):
        """
        Gets the conditions of this IngestTimeRule.

        :return: The conditions of this IngestTimeRule.
        :rtype: oci.log_analytics.models.IngestTimeRuleCondition
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this IngestTimeRule.

        :param conditions: The conditions of this IngestTimeRule.
        :type: oci.log_analytics.models.IngestTimeRuleCondition
        """
        self._conditions = conditions

    @property
    def actions(self):
        """
        Gets the actions of this IngestTimeRule.
        The action(s) to be performed if the ingest time rule condition(s) are satisfied.


        :return: The actions of this IngestTimeRule.
        :rtype: list[oci.log_analytics.models.IngestTimeRuleAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this IngestTimeRule.
        The action(s) to be performed if the ingest time rule condition(s) are satisfied.


        :param actions: The actions of this IngestTimeRule.
        :type: list[oci.log_analytics.models.IngestTimeRuleAction]
        """
        self._actions = actions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
