# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsWarning(object):
    """
    LogAnalyticsWarning
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsWarning object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param agent_id:
            The value to assign to the agent_id property of this LogAnalyticsWarning.
        :type agent_id: str

        :param host_name:
            The value to assign to the host_name property of this LogAnalyticsWarning.
        :type host_name: str

        :param rule_display_name:
            The value to assign to the rule_display_name property of this LogAnalyticsWarning.
        :type rule_display_name: str

        :param source_name:
            The value to assign to the source_name property of this LogAnalyticsWarning.
        :type source_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this LogAnalyticsWarning.
        :type compartment_id: str

        :param source_display_name:
            The value to assign to the source_display_name property of this LogAnalyticsWarning.
        :type source_display_name: str

        :param entity_name:
            The value to assign to the entity_name property of this LogAnalyticsWarning.
        :type entity_name: str

        :param time_collected:
            The value to assign to the time_collected property of this LogAnalyticsWarning.
        :type time_collected: datetime

        :param warning_id:
            The value to assign to the warning_id property of this LogAnalyticsWarning.
        :type warning_id: str

        :param time_of_initial_warning:
            The value to assign to the time_of_initial_warning property of this LogAnalyticsWarning.
        :type time_of_initial_warning: datetime

        :param is_active:
            The value to assign to the is_active property of this LogAnalyticsWarning.
        :type is_active: bool

        :param is_suppressed:
            The value to assign to the is_suppressed property of this LogAnalyticsWarning.
        :type is_suppressed: bool

        :param time_of_latest_warning:
            The value to assign to the time_of_latest_warning property of this LogAnalyticsWarning.
        :type time_of_latest_warning: datetime

        :param warning_level:
            The value to assign to the warning_level property of this LogAnalyticsWarning.
        :type warning_level: str

        :param warning_message:
            The value to assign to the warning_message property of this LogAnalyticsWarning.
        :type warning_message: str

        :param pattern_id:
            The value to assign to the pattern_id property of this LogAnalyticsWarning.
        :type pattern_id: str

        :param pattern_text:
            The value to assign to the pattern_text property of this LogAnalyticsWarning.
        :type pattern_text: str

        :param rule_id:
            The value to assign to the rule_id property of this LogAnalyticsWarning.
        :type rule_id: str

        :param source_id:
            The value to assign to the source_id property of this LogAnalyticsWarning.
        :type source_id: str

        :param suppressed_by:
            The value to assign to the suppressed_by property of this LogAnalyticsWarning.
        :type suppressed_by: str

        :param entity_id:
            The value to assign to the entity_id property of this LogAnalyticsWarning.
        :type entity_id: str

        :param entity_type:
            The value to assign to the entity_type property of this LogAnalyticsWarning.
        :type entity_type: str

        :param entity_type_display_name:
            The value to assign to the entity_type_display_name property of this LogAnalyticsWarning.
        :type entity_type_display_name: str

        :param type_display_name:
            The value to assign to the type_display_name property of this LogAnalyticsWarning.
        :type type_display_name: str

        :param type_name:
            The value to assign to the type_name property of this LogAnalyticsWarning.
        :type type_name: str

        :param severity:
            The value to assign to the severity property of this LogAnalyticsWarning.
        :type severity: int

        """
        self.swagger_types = {
            'agent_id': 'str',
            'host_name': 'str',
            'rule_display_name': 'str',
            'source_name': 'str',
            'compartment_id': 'str',
            'source_display_name': 'str',
            'entity_name': 'str',
            'time_collected': 'datetime',
            'warning_id': 'str',
            'time_of_initial_warning': 'datetime',
            'is_active': 'bool',
            'is_suppressed': 'bool',
            'time_of_latest_warning': 'datetime',
            'warning_level': 'str',
            'warning_message': 'str',
            'pattern_id': 'str',
            'pattern_text': 'str',
            'rule_id': 'str',
            'source_id': 'str',
            'suppressed_by': 'str',
            'entity_id': 'str',
            'entity_type': 'str',
            'entity_type_display_name': 'str',
            'type_display_name': 'str',
            'type_name': 'str',
            'severity': 'int'
        }

        self.attribute_map = {
            'agent_id': 'agentId',
            'host_name': 'hostName',
            'rule_display_name': 'ruleDisplayName',
            'source_name': 'sourceName',
            'compartment_id': 'compartmentId',
            'source_display_name': 'sourceDisplayName',
            'entity_name': 'entityName',
            'time_collected': 'timeCollected',
            'warning_id': 'warningId',
            'time_of_initial_warning': 'timeOfInitialWarning',
            'is_active': 'isActive',
            'is_suppressed': 'isSuppressed',
            'time_of_latest_warning': 'timeOfLatestWarning',
            'warning_level': 'warningLevel',
            'warning_message': 'warningMessage',
            'pattern_id': 'patternId',
            'pattern_text': 'patternText',
            'rule_id': 'ruleId',
            'source_id': 'sourceId',
            'suppressed_by': 'suppressedBy',
            'entity_id': 'entityId',
            'entity_type': 'entityType',
            'entity_type_display_name': 'entityTypeDisplayName',
            'type_display_name': 'typeDisplayName',
            'type_name': 'typeName',
            'severity': 'severity'
        }

        self._agent_id = None
        self._host_name = None
        self._rule_display_name = None
        self._source_name = None
        self._compartment_id = None
        self._source_display_name = None
        self._entity_name = None
        self._time_collected = None
        self._warning_id = None
        self._time_of_initial_warning = None
        self._is_active = None
        self._is_suppressed = None
        self._time_of_latest_warning = None
        self._warning_level = None
        self._warning_message = None
        self._pattern_id = None
        self._pattern_text = None
        self._rule_id = None
        self._source_id = None
        self._suppressed_by = None
        self._entity_id = None
        self._entity_type = None
        self._entity_type_display_name = None
        self._type_display_name = None
        self._type_name = None
        self._severity = None

    @property
    def agent_id(self):
        """
        Gets the agent_id of this LogAnalyticsWarning.
        The unique identifier of the agent associated with the warning


        :return: The agent_id of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this LogAnalyticsWarning.
        The unique identifier of the agent associated with the warning


        :param agent_id: The agent_id of this LogAnalyticsWarning.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def host_name(self):
        """
        Gets the host_name of this LogAnalyticsWarning.
        The host containing the agent associated with the warning


        :return: The host_name of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this LogAnalyticsWarning.
        The host containing the agent associated with the warning


        :param host_name: The host_name of this LogAnalyticsWarning.
        :type: str
        """
        self._host_name = host_name

    @property
    def rule_display_name(self):
        """
        Gets the rule_display_name of this LogAnalyticsWarning.
        The display name of the rule which triggered the warning


        :return: The rule_display_name of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._rule_display_name

    @rule_display_name.setter
    def rule_display_name(self, rule_display_name):
        """
        Sets the rule_display_name of this LogAnalyticsWarning.
        The display name of the rule which triggered the warning


        :param rule_display_name: The rule_display_name of this LogAnalyticsWarning.
        :type: str
        """
        self._rule_display_name = rule_display_name

    @property
    def source_name(self):
        """
        Gets the source_name of this LogAnalyticsWarning.
        The name of the source associated with the warning


        :return: The source_name of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this LogAnalyticsWarning.
        The name of the source associated with the warning


        :param source_name: The source_name of this LogAnalyticsWarning.
        :type: str
        """
        self._source_name = source_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this LogAnalyticsWarning.
        The entity compartment ID.


        :return: The compartment_id of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LogAnalyticsWarning.
        The entity compartment ID.


        :param compartment_id: The compartment_id of this LogAnalyticsWarning.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def source_display_name(self):
        """
        Gets the source_display_name of this LogAnalyticsWarning.
        The display name of the source associated with the warning


        :return: The source_display_name of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._source_display_name

    @source_display_name.setter
    def source_display_name(self, source_display_name):
        """
        Sets the source_display_name of this LogAnalyticsWarning.
        The display name of the source associated with the warning


        :param source_display_name: The source_display_name of this LogAnalyticsWarning.
        :type: str
        """
        self._source_display_name = source_display_name

    @property
    def entity_name(self):
        """
        Gets the entity_name of this LogAnalyticsWarning.
        The name of the entity associated with the warning


        :return: The entity_name of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this LogAnalyticsWarning.
        The name of the entity associated with the warning


        :param entity_name: The entity_name of this LogAnalyticsWarning.
        :type: str
        """
        self._entity_name = entity_name

    @property
    def time_collected(self):
        """
        Gets the time_collected of this LogAnalyticsWarning.
        The time at which the warning was most recently collected


        :return: The time_collected of this LogAnalyticsWarning.
        :rtype: datetime
        """
        return self._time_collected

    @time_collected.setter
    def time_collected(self, time_collected):
        """
        Sets the time_collected of this LogAnalyticsWarning.
        The time at which the warning was most recently collected


        :param time_collected: The time_collected of this LogAnalyticsWarning.
        :type: datetime
        """
        self._time_collected = time_collected

    @property
    def warning_id(self):
        """
        Gets the warning_id of this LogAnalyticsWarning.
        The unique identifier of the warning


        :return: The warning_id of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._warning_id

    @warning_id.setter
    def warning_id(self, warning_id):
        """
        Sets the warning_id of this LogAnalyticsWarning.
        The unique identifier of the warning


        :param warning_id: The warning_id of this LogAnalyticsWarning.
        :type: str
        """
        self._warning_id = warning_id

    @property
    def time_of_initial_warning(self):
        """
        Gets the time_of_initial_warning of this LogAnalyticsWarning.
        The date at which the warning was initially triggered


        :return: The time_of_initial_warning of this LogAnalyticsWarning.
        :rtype: datetime
        """
        return self._time_of_initial_warning

    @time_of_initial_warning.setter
    def time_of_initial_warning(self, time_of_initial_warning):
        """
        Sets the time_of_initial_warning of this LogAnalyticsWarning.
        The date at which the warning was initially triggered


        :param time_of_initial_warning: The time_of_initial_warning of this LogAnalyticsWarning.
        :type: datetime
        """
        self._time_of_initial_warning = time_of_initial_warning

    @property
    def is_active(self):
        """
        Gets the is_active of this LogAnalyticsWarning.
        A flag indicating if the warning is currently active


        :return: The is_active of this LogAnalyticsWarning.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """
        Sets the is_active of this LogAnalyticsWarning.
        A flag indicating if the warning is currently active


        :param is_active: The is_active of this LogAnalyticsWarning.
        :type: bool
        """
        self._is_active = is_active

    @property
    def is_suppressed(self):
        """
        Gets the is_suppressed of this LogAnalyticsWarning.
        A flag indicating if the warning is currently suppressed


        :return: The is_suppressed of this LogAnalyticsWarning.
        :rtype: bool
        """
        return self._is_suppressed

    @is_suppressed.setter
    def is_suppressed(self, is_suppressed):
        """
        Sets the is_suppressed of this LogAnalyticsWarning.
        A flag indicating if the warning is currently suppressed


        :param is_suppressed: The is_suppressed of this LogAnalyticsWarning.
        :type: bool
        """
        self._is_suppressed = is_suppressed

    @property
    def time_of_latest_warning(self):
        """
        Gets the time_of_latest_warning of this LogAnalyticsWarning.
        The most recent date on which the warning was triggered


        :return: The time_of_latest_warning of this LogAnalyticsWarning.
        :rtype: datetime
        """
        return self._time_of_latest_warning

    @time_of_latest_warning.setter
    def time_of_latest_warning(self, time_of_latest_warning):
        """
        Sets the time_of_latest_warning of this LogAnalyticsWarning.
        The most recent date on which the warning was triggered


        :param time_of_latest_warning: The time_of_latest_warning of this LogAnalyticsWarning.
        :type: datetime
        """
        self._time_of_latest_warning = time_of_latest_warning

    @property
    def warning_level(self):
        """
        Gets the warning_level of this LogAnalyticsWarning.
        The warning level - either pattern, rule, or source.


        :return: The warning_level of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._warning_level

    @warning_level.setter
    def warning_level(self, warning_level):
        """
        Sets the warning_level of this LogAnalyticsWarning.
        The warning level - either pattern, rule, or source.


        :param warning_level: The warning_level of this LogAnalyticsWarning.
        :type: str
        """
        self._warning_level = warning_level

    @property
    def warning_message(self):
        """
        Gets the warning_message of this LogAnalyticsWarning.
        A description of the warning intended for the consumer of the warning.  It will
        usually detail the cause of the warning, may suggest a remedy, and can contain any
        other relevant information the consumer might find useful


        :return: The warning_message of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._warning_message

    @warning_message.setter
    def warning_message(self, warning_message):
        """
        Sets the warning_message of this LogAnalyticsWarning.
        A description of the warning intended for the consumer of the warning.  It will
        usually detail the cause of the warning, may suggest a remedy, and can contain any
        other relevant information the consumer might find useful


        :param warning_message: The warning_message of this LogAnalyticsWarning.
        :type: str
        """
        self._warning_message = warning_message

    @property
    def pattern_id(self):
        """
        Gets the pattern_id of this LogAnalyticsWarning.
        The unique identifier of the warning pattern


        :return: The pattern_id of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._pattern_id

    @pattern_id.setter
    def pattern_id(self, pattern_id):
        """
        Sets the pattern_id of this LogAnalyticsWarning.
        The unique identifier of the warning pattern


        :param pattern_id: The pattern_id of this LogAnalyticsWarning.
        :type: str
        """
        self._pattern_id = pattern_id

    @property
    def pattern_text(self):
        """
        Gets the pattern_text of this LogAnalyticsWarning.
        The text of the pattern used by the warning


        :return: The pattern_text of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._pattern_text

    @pattern_text.setter
    def pattern_text(self, pattern_text):
        """
        Sets the pattern_text of this LogAnalyticsWarning.
        The text of the pattern used by the warning


        :param pattern_text: The pattern_text of this LogAnalyticsWarning.
        :type: str
        """
        self._pattern_text = pattern_text

    @property
    def rule_id(self):
        """
        Gets the rule_id of this LogAnalyticsWarning.
        The unique identifier of the rule associated with the warning


        :return: The rule_id of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """
        Sets the rule_id of this LogAnalyticsWarning.
        The unique identifier of the rule associated with the warning


        :param rule_id: The rule_id of this LogAnalyticsWarning.
        :type: str
        """
        self._rule_id = rule_id

    @property
    def source_id(self):
        """
        Gets the source_id of this LogAnalyticsWarning.
        The unique identifier of the source associated with the warning


        :return: The source_id of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this LogAnalyticsWarning.
        The unique identifier of the source associated with the warning


        :param source_id: The source_id of this LogAnalyticsWarning.
        :type: str
        """
        self._source_id = source_id

    @property
    def suppressed_by(self):
        """
        Gets the suppressed_by of this LogAnalyticsWarning.
        The user who suppressed the warning, or empty if the warning is not suppressed


        :return: The suppressed_by of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._suppressed_by

    @suppressed_by.setter
    def suppressed_by(self, suppressed_by):
        """
        Sets the suppressed_by of this LogAnalyticsWarning.
        The user who suppressed the warning, or empty if the warning is not suppressed


        :param suppressed_by: The suppressed_by of this LogAnalyticsWarning.
        :type: str
        """
        self._suppressed_by = suppressed_by

    @property
    def entity_id(self):
        """
        Gets the entity_id of this LogAnalyticsWarning.
        The unique identifier of the entity associated with the warning


        :return: The entity_id of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this LogAnalyticsWarning.
        The unique identifier of the entity associated with the warning


        :param entity_id: The entity_id of this LogAnalyticsWarning.
        :type: str
        """
        self._entity_id = entity_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this LogAnalyticsWarning.
        The type of the entity associated with the warning


        :return: The entity_type of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this LogAnalyticsWarning.
        The type of the entity associated with the warning


        :param entity_type: The entity_type of this LogAnalyticsWarning.
        :type: str
        """
        self._entity_type = entity_type

    @property
    def entity_type_display_name(self):
        """
        Gets the entity_type_display_name of this LogAnalyticsWarning.
        The display name of the entity type associated with the warning


        :return: The entity_type_display_name of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._entity_type_display_name

    @entity_type_display_name.setter
    def entity_type_display_name(self, entity_type_display_name):
        """
        Sets the entity_type_display_name of this LogAnalyticsWarning.
        The display name of the entity type associated with the warning


        :param entity_type_display_name: The entity_type_display_name of this LogAnalyticsWarning.
        :type: str
        """
        self._entity_type_display_name = entity_type_display_name

    @property
    def type_display_name(self):
        """
        Gets the type_display_name of this LogAnalyticsWarning.
        The display name of the warning type


        :return: The type_display_name of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._type_display_name

    @type_display_name.setter
    def type_display_name(self, type_display_name):
        """
        Sets the type_display_name of this LogAnalyticsWarning.
        The display name of the warning type


        :param type_display_name: The type_display_name of this LogAnalyticsWarning.
        :type: str
        """
        self._type_display_name = type_display_name

    @property
    def type_name(self):
        """
        Gets the type_name of this LogAnalyticsWarning.
        The internal name of the warning


        :return: The type_name of this LogAnalyticsWarning.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """
        Sets the type_name of this LogAnalyticsWarning.
        The internal name of the warning


        :param type_name: The type_name of this LogAnalyticsWarning.
        :type: str
        """
        self._type_name = type_name

    @property
    def severity(self):
        """
        Gets the severity of this LogAnalyticsWarning.
        The warning severity


        :return: The severity of this LogAnalyticsWarning.
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this LogAnalyticsWarning.
        The warning severity


        :param severity: The severity of this LogAnalyticsWarning.
        :type: int
        """
        self._severity = severity

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
