# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsLabelView(object):
    """
    LogAnalyticsLabelView
    """

    #: A constant which can be used with the priority property of a LogAnalyticsLabelView.
    #: This constant has a value of "NONE"
    PRIORITY_NONE = "NONE"

    #: A constant which can be used with the priority property of a LogAnalyticsLabelView.
    #: This constant has a value of "LOW"
    PRIORITY_LOW = "LOW"

    #: A constant which can be used with the priority property of a LogAnalyticsLabelView.
    #: This constant has a value of "MEDIUM"
    PRIORITY_MEDIUM = "MEDIUM"

    #: A constant which can be used with the priority property of a LogAnalyticsLabelView.
    #: This constant has a value of "HIGH"
    PRIORITY_HIGH = "HIGH"

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsLabelView object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param aliases:
            The value to assign to the aliases property of this LogAnalyticsLabelView.
        :type aliases: list[oci.log_analytics.models.LogAnalyticsLabelAlias]

        :param count_usage_in_alert_rule:
            The value to assign to the count_usage_in_alert_rule property of this LogAnalyticsLabelView.
        :type count_usage_in_alert_rule: int

        :param count_usage_in_source:
            The value to assign to the count_usage_in_source property of this LogAnalyticsLabelView.
        :type count_usage_in_source: int

        :param id:
            The value to assign to the id property of this LogAnalyticsLabelView.
        :type id: object

        :param suggest_type:
            The value to assign to the suggest_type property of this LogAnalyticsLabelView.
        :type suggest_type: int

        :param description:
            The value to assign to the description property of this LogAnalyticsLabelView.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this LogAnalyticsLabelView.
        :type display_name: str

        :param edit_version:
            The value to assign to the edit_version property of this LogAnalyticsLabelView.
        :type edit_version: int

        :param impact:
            The value to assign to the impact property of this LogAnalyticsLabelView.
        :type impact: str

        :param is_system:
            The value to assign to the is_system property of this LogAnalyticsLabelView.
        :type is_system: bool

        :param name:
            The value to assign to the name property of this LogAnalyticsLabelView.
        :type name: str

        :param priority:
            The value to assign to the priority property of this LogAnalyticsLabelView.
            Allowed values for this property are: "NONE", "LOW", "MEDIUM", "HIGH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type priority: str

        :param recommendation:
            The value to assign to the recommendation property of this LogAnalyticsLabelView.
        :type recommendation: str

        :param type:
            The value to assign to the type property of this LogAnalyticsLabelView.
        :type type: int

        :param is_user_deleted:
            The value to assign to the is_user_deleted property of this LogAnalyticsLabelView.
        :type is_user_deleted: bool

        """
        self.swagger_types = {
            'aliases': 'list[LogAnalyticsLabelAlias]',
            'count_usage_in_alert_rule': 'int',
            'count_usage_in_source': 'int',
            'id': 'object',
            'suggest_type': 'int',
            'description': 'str',
            'display_name': 'str',
            'edit_version': 'int',
            'impact': 'str',
            'is_system': 'bool',
            'name': 'str',
            'priority': 'str',
            'recommendation': 'str',
            'type': 'int',
            'is_user_deleted': 'bool'
        }

        self.attribute_map = {
            'aliases': 'aliases',
            'count_usage_in_alert_rule': 'countUsageInAlertRule',
            'count_usage_in_source': 'countUsageInSource',
            'id': 'id',
            'suggest_type': 'suggestType',
            'description': 'description',
            'display_name': 'displayName',
            'edit_version': 'editVersion',
            'impact': 'impact',
            'is_system': 'isSystem',
            'name': 'name',
            'priority': 'priority',
            'recommendation': 'recommendation',
            'type': 'type',
            'is_user_deleted': 'isUserDeleted'
        }

        self._aliases = None
        self._count_usage_in_alert_rule = None
        self._count_usage_in_source = None
        self._id = None
        self._suggest_type = None
        self._description = None
        self._display_name = None
        self._edit_version = None
        self._impact = None
        self._is_system = None
        self._name = None
        self._priority = None
        self._recommendation = None
        self._type = None
        self._is_user_deleted = None

    @property
    def aliases(self):
        """
        Gets the aliases of this LogAnalyticsLabelView.
        An arrya of label aliases.


        :return: The aliases of this LogAnalyticsLabelView.
        :rtype: list[oci.log_analytics.models.LogAnalyticsLabelAlias]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """
        Sets the aliases of this LogAnalyticsLabelView.
        An arrya of label aliases.


        :param aliases: The aliases of this LogAnalyticsLabelView.
        :type: list[oci.log_analytics.models.LogAnalyticsLabelAlias]
        """
        self._aliases = aliases

    @property
    def count_usage_in_alert_rule(self):
        """
        Gets the count_usage_in_alert_rule of this LogAnalyticsLabelView.
        The label alert rule usage count.


        :return: The count_usage_in_alert_rule of this LogAnalyticsLabelView.
        :rtype: int
        """
        return self._count_usage_in_alert_rule

    @count_usage_in_alert_rule.setter
    def count_usage_in_alert_rule(self, count_usage_in_alert_rule):
        """
        Sets the count_usage_in_alert_rule of this LogAnalyticsLabelView.
        The label alert rule usage count.


        :param count_usage_in_alert_rule: The count_usage_in_alert_rule of this LogAnalyticsLabelView.
        :type: int
        """
        self._count_usage_in_alert_rule = count_usage_in_alert_rule

    @property
    def count_usage_in_source(self):
        """
        Gets the count_usage_in_source of this LogAnalyticsLabelView.
        The label source usage count.


        :return: The count_usage_in_source of this LogAnalyticsLabelView.
        :rtype: int
        """
        return self._count_usage_in_source

    @count_usage_in_source.setter
    def count_usage_in_source(self, count_usage_in_source):
        """
        Sets the count_usage_in_source of this LogAnalyticsLabelView.
        The label source usage count.


        :param count_usage_in_source: The count_usage_in_source of this LogAnalyticsLabelView.
        :type: int
        """
        self._count_usage_in_source = count_usage_in_source

    @property
    def id(self):
        """
        Gets the id of this LogAnalyticsLabelView.
        The label unique identifier.


        :return: The id of this LogAnalyticsLabelView.
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LogAnalyticsLabelView.
        The label unique identifier.


        :param id: The id of this LogAnalyticsLabelView.
        :type: object
        """
        self._id = id

    @property
    def suggest_type(self):
        """
        Gets the suggest_type of this LogAnalyticsLabelView.
        The label suggestion type.


        :return: The suggest_type of this LogAnalyticsLabelView.
        :rtype: int
        """
        return self._suggest_type

    @suggest_type.setter
    def suggest_type(self, suggest_type):
        """
        Sets the suggest_type of this LogAnalyticsLabelView.
        The label suggestion type.


        :param suggest_type: The suggest_type of this LogAnalyticsLabelView.
        :type: int
        """
        self._suggest_type = suggest_type

    @property
    def description(self):
        """
        Gets the description of this LogAnalyticsLabelView.
        The label description.


        :return: The description of this LogAnalyticsLabelView.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogAnalyticsLabelView.
        The label description.


        :param description: The description of this LogAnalyticsLabelView.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this LogAnalyticsLabelView.
        The label display name.


        :return: The display_name of this LogAnalyticsLabelView.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LogAnalyticsLabelView.
        The label display name.


        :param display_name: The display_name of this LogAnalyticsLabelView.
        :type: str
        """
        self._display_name = display_name

    @property
    def edit_version(self):
        """
        Gets the edit_version of this LogAnalyticsLabelView.
        The label edit version.


        :return: The edit_version of this LogAnalyticsLabelView.
        :rtype: int
        """
        return self._edit_version

    @edit_version.setter
    def edit_version(self, edit_version):
        """
        Sets the edit_version of this LogAnalyticsLabelView.
        The label edit version.


        :param edit_version: The edit_version of this LogAnalyticsLabelView.
        :type: int
        """
        self._edit_version = edit_version

    @property
    def impact(self):
        """
        Gets the impact of this LogAnalyticsLabelView.
        The label impact.


        :return: The impact of this LogAnalyticsLabelView.
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        """
        Sets the impact of this LogAnalyticsLabelView.
        The label impact.


        :param impact: The impact of this LogAnalyticsLabelView.
        :type: str
        """
        self._impact = impact

    @property
    def is_system(self):
        """
        Gets the is_system of this LogAnalyticsLabelView.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :return: The is_system of this LogAnalyticsLabelView.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this LogAnalyticsLabelView.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :param is_system: The is_system of this LogAnalyticsLabelView.
        :type: bool
        """
        self._is_system = is_system

    @property
    def name(self):
        """
        Gets the name of this LogAnalyticsLabelView.
        The label name.


        :return: The name of this LogAnalyticsLabelView.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsLabelView.
        The label name.


        :param name: The name of this LogAnalyticsLabelView.
        :type: str
        """
        self._name = name

    @property
    def priority(self):
        """
        Gets the priority of this LogAnalyticsLabelView.
        The label priority.  Default value is NONE.

        Allowed values for this property are: "NONE", "LOW", "MEDIUM", "HIGH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The priority of this LogAnalyticsLabelView.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this LogAnalyticsLabelView.
        The label priority.  Default value is NONE.


        :param priority: The priority of this LogAnalyticsLabelView.
        :type: str
        """
        allowed_values = ["NONE", "LOW", "MEDIUM", "HIGH"]
        if not value_allowed_none_or_none_sentinel(priority, allowed_values):
            priority = 'UNKNOWN_ENUM_VALUE'
        self._priority = priority

    @property
    def recommendation(self):
        """
        Gets the recommendation of this LogAnalyticsLabelView.
        The label recommendation.


        :return: The recommendation of this LogAnalyticsLabelView.
        :rtype: str
        """
        return self._recommendation

    @recommendation.setter
    def recommendation(self, recommendation):
        """
        Sets the recommendation of this LogAnalyticsLabelView.
        The label recommendation.


        :param recommendation: The recommendation of this LogAnalyticsLabelView.
        :type: str
        """
        self._recommendation = recommendation

    @property
    def type(self):
        """
        Gets the type of this LogAnalyticsLabelView.
        The label type.


        :return: The type of this LogAnalyticsLabelView.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this LogAnalyticsLabelView.
        The label type.


        :param type: The type of this LogAnalyticsLabelView.
        :type: int
        """
        self._type = type

    @property
    def is_user_deleted(self):
        """
        Gets the is_user_deleted of this LogAnalyticsLabelView.
        A flag indicating whether or not the label has been deleted.


        :return: The is_user_deleted of this LogAnalyticsLabelView.
        :rtype: bool
        """
        return self._is_user_deleted

    @is_user_deleted.setter
    def is_user_deleted(self, is_user_deleted):
        """
        Sets the is_user_deleted of this LogAnalyticsLabelView.
        A flag indicating whether or not the label has been deleted.


        :param is_user_deleted: The is_user_deleted of this LogAnalyticsLabelView.
        :type: bool
        """
        self._is_user_deleted = is_user_deleted

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
