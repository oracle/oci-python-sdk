# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRuleDetails(object):
    """
    Object used to create a rule.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateRuleDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateRuleDetails.
        :type description: str

        :param is_enabled:
            The value to assign to the is_enabled property of this CreateRuleDetails.
        :type is_enabled: bool

        :param condition:
            The value to assign to the condition property of this CreateRuleDetails.
        :type condition: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateRuleDetails.
        :type compartment_id: str

        :param actions:
            The value to assign to the actions property of this CreateRuleDetails.
        :type actions: oci.events.models.ActionDetailsList

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateRuleDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateRuleDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'is_enabled': 'bool',
            'condition': 'str',
            'compartment_id': 'str',
            'actions': 'ActionDetailsList',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'is_enabled': 'isEnabled',
            'condition': 'condition',
            'compartment_id': 'compartmentId',
            'actions': 'actions',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._is_enabled = None
        self._condition = None
        self._compartment_id = None
        self._actions = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateRuleDetails.
        A string that describes the rule. It does not have to be unique, and you can change it. Avoid entering
        confidential information.


        :return: The display_name of this CreateRuleDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateRuleDetails.
        A string that describes the rule. It does not have to be unique, and you can change it. Avoid entering
        confidential information.


        :param display_name: The display_name of this CreateRuleDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateRuleDetails.
        A string that describes the details of the rule. It does not have to be unique, and you can change it. Avoid entering
        confidential information.


        :return: The description of this CreateRuleDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateRuleDetails.
        A string that describes the details of the rule. It does not have to be unique, and you can change it. Avoid entering
        confidential information.


        :param description: The description of this CreateRuleDetails.
        :type: str
        """
        self._description = description

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this CreateRuleDetails.
        Whether or not this rule is currently enabled.

        Example: `true`


        :return: The is_enabled of this CreateRuleDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this CreateRuleDetails.
        Whether or not this rule is currently enabled.

        Example: `true`


        :param is_enabled: The is_enabled of this CreateRuleDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def condition(self):
        """
        **[Required]** Gets the condition of this CreateRuleDetails.
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


        :return: The condition of this CreateRuleDetails.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this CreateRuleDetails.
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


        :param condition: The condition of this CreateRuleDetails.
        :type: str
        """
        self._condition = condition

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateRuleDetails.
        The `OCID`__ of the compartment to which this rule belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateRuleDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateRuleDetails.
        The `OCID`__ of the compartment to which this rule belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateRuleDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def actions(self):
        """
        **[Required]** Gets the actions of this CreateRuleDetails.

        :return: The actions of this CreateRuleDetails.
        :rtype: oci.events.models.ActionDetailsList
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this CreateRuleDetails.

        :param actions: The actions of this CreateRuleDetails.
        :type: oci.events.models.ActionDetailsList
        """
        self._actions = actions

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateRuleDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-compatibility only.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateRuleDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateRuleDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-compatibility only.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateRuleDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateRuleDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateRuleDetails.
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
