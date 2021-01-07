# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Rule(object):
    """
    The configuration details of an Events rule. For more information, see
    `Managing Rules for Events`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Events/Task/managingrules.htm
    """

    #: A constant which can be used with the lifecycle_state property of a Rule.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Rule.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Rule.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Rule.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Rule.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Rule.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Rule.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Rule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this Rule.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Rule.
        :type description: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Rule.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param condition:
            The value to assign to the condition property of this Rule.
        :type condition: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Rule.
        :type compartment_id: str

        :param is_enabled:
            The value to assign to the is_enabled property of this Rule.
        :type is_enabled: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Rule.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Rule.
        :type defined_tags: dict(str, dict(str, object))

        :param actions:
            The value to assign to the actions property of this Rule.
        :type actions: oci.events.models.ActionList

        :param id:
            The value to assign to the id property of this Rule.
        :type id: str

        :param time_created:
            The value to assign to the time_created property of this Rule.
        :type time_created: datetime

        :param lifecycle_message:
            The value to assign to the lifecycle_message property of this Rule.
        :type lifecycle_message: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'lifecycle_state': 'str',
            'condition': 'str',
            'compartment_id': 'str',
            'is_enabled': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'actions': 'ActionList',
            'id': 'str',
            'time_created': 'datetime',
            'lifecycle_message': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'lifecycle_state': 'lifecycleState',
            'condition': 'condition',
            'compartment_id': 'compartmentId',
            'is_enabled': 'isEnabled',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'actions': 'actions',
            'id': 'id',
            'time_created': 'timeCreated',
            'lifecycle_message': 'lifecycleMessage'
        }

        self._display_name = None
        self._description = None
        self._lifecycle_state = None
        self._condition = None
        self._compartment_id = None
        self._is_enabled = None
        self._freeform_tags = None
        self._defined_tags = None
        self._actions = None
        self._id = None
        self._time_created = None
        self._lifecycle_message = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Rule.
        A string that describes the rule. It does not have to be unique, and you can change it. Avoid entering
        confidential information.

        Example: `\"This rule sends a notification upon completion of DbaaS backup.\"`


        :return: The display_name of this Rule.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Rule.
        A string that describes the rule. It does not have to be unique, and you can change it. Avoid entering
        confidential information.

        Example: `\"This rule sends a notification upon completion of DbaaS backup.\"`


        :param display_name: The display_name of this Rule.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Rule.
        A string that describes the details of the rule. It does not have to be unique, and you can change it. Avoid entering
        confidential information.


        :return: The description of this Rule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Rule.
        A string that describes the details of the rule. It does not have to be unique, and you can change it. Avoid entering
        confidential information.


        :param description: The description of this Rule.
        :type: str
        """
        self._description = description

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Rule.
        The current state of the rule.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Rule.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Rule.
        The current state of the rule.


        :param lifecycle_state: The lifecycle_state of this Rule.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def condition(self):
        """
        **[Required]** Gets the condition of this Rule.
        A filter that specifies the event that will trigger actions associated with this rule. A few
        important things to remember about filters:

        * Fields not mentioned in the condition are ignored. You can create a valid filter that matches
        all events with two curly brackets: `{}`

          For more examples, see
        `Matching Events with Filters`__.
        * For a condition with fields to match an event, the event must contain all the field names
        listed in the condition. Field names must appear in the condition with the same nesting
        structure used in the event.

          For a list of reference events, see
        `Services that Produce Events`__.
        * Rules apply to events in the compartment in which you create them and any child compartments.
        This means that a condition specified by a rule only matches events emitted from resources in
        the compartment or any of its child compartments.
        * Wildcard matching is supported with the asterisk (*) character.

          For examples of wildcard matching, see
        `Matching Events with Filters`__

        Example: `\\\"eventType\\\": \\\"com.oraclecloud.databaseservice.autonomous.database.backup.end\\\"`

        __ https://docs.cloud.oracle.com/iaas/Content/Events/Concepts/filterevents.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Events/Concepts/filterevents.htm


        :return: The condition of this Rule.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this Rule.
        A filter that specifies the event that will trigger actions associated with this rule. A few
        important things to remember about filters:

        * Fields not mentioned in the condition are ignored. You can create a valid filter that matches
        all events with two curly brackets: `{}`

          For more examples, see
        `Matching Events with Filters`__.
        * For a condition with fields to match an event, the event must contain all the field names
        listed in the condition. Field names must appear in the condition with the same nesting
        structure used in the event.

          For a list of reference events, see
        `Services that Produce Events`__.
        * Rules apply to events in the compartment in which you create them and any child compartments.
        This means that a condition specified by a rule only matches events emitted from resources in
        the compartment or any of its child compartments.
        * Wildcard matching is supported with the asterisk (*) character.

          For examples of wildcard matching, see
        `Matching Events with Filters`__

        Example: `\\\"eventType\\\": \\\"com.oraclecloud.databaseservice.autonomous.database.backup.end\\\"`

        __ https://docs.cloud.oracle.com/iaas/Content/Events/Concepts/filterevents.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Events/Concepts/filterevents.htm


        :param condition: The condition of this Rule.
        :type: str
        """
        self._condition = condition

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Rule.
        The `OCID`__ of the compartment to which this rule belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Rule.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Rule.
        The `OCID`__ of the compartment to which this rule belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Rule.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this Rule.
        Whether or not this rule is currently enabled.

        Example: `true`


        :return: The is_enabled of this Rule.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this Rule.
        Whether or not this rule is currently enabled.

        Example: `true`


        :param is_enabled: The is_enabled of this Rule.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Rule.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-compatibility only.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Rule.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Rule.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-compatibility only.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Rule.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Rule.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Rule.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Rule.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Rule.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def actions(self):
        """
        **[Required]** Gets the actions of this Rule.

        :return: The actions of this Rule.
        :rtype: oci.events.models.ActionList
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this Rule.

        :param actions: The actions of this Rule.
        :type: oci.events.models.ActionList
        """
        self._actions = actions

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Rule.
        The `OCID`__ of this rule.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Rule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Rule.
        The `OCID`__ of this rule.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this Rule.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Rule.
        The time this rule was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2018-09-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Rule.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Rule.
        The time this rule was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2018-09-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Rule.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_message(self):
        """
        Gets the lifecycle_message of this Rule.
        A message generated by the Events service about the current state of this rule.


        :return: The lifecycle_message of this Rule.
        :rtype: str
        """
        return self._lifecycle_message

    @lifecycle_message.setter
    def lifecycle_message(self, lifecycle_message):
        """
        Sets the lifecycle_message of this Rule.
        A message generated by the Events service about the current state of this rule.


        :param lifecycle_message: The lifecycle_message of this Rule.
        :type: str
        """
        self._lifecycle_message = lifecycle_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
