# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsLabelAlias(object):
    """
    Label alias mapping view
    """

    #: A constant which can be used with the priority property of a LogAnalyticsLabelAlias.
    #: This constant has a value of "NONE"
    PRIORITY_NONE = "NONE"

    #: A constant which can be used with the priority property of a LogAnalyticsLabelAlias.
    #: This constant has a value of "LOW"
    PRIORITY_LOW = "LOW"

    #: A constant which can be used with the priority property of a LogAnalyticsLabelAlias.
    #: This constant has a value of "MEDIUM"
    PRIORITY_MEDIUM = "MEDIUM"

    #: A constant which can be used with the priority property of a LogAnalyticsLabelAlias.
    #: This constant has a value of "HIGH"
    PRIORITY_HIGH = "HIGH"

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsLabelAlias object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param alias:
            The value to assign to the alias property of this LogAnalyticsLabelAlias.
        :type alias: str

        :param alias_display_name:
            The value to assign to the alias_display_name property of this LogAnalyticsLabelAlias.
        :type alias_display_name: str

        :param is_system:
            The value to assign to the is_system property of this LogAnalyticsLabelAlias.
        :type is_system: bool

        :param display_name:
            The value to assign to the display_name property of this LogAnalyticsLabelAlias.
        :type display_name: str

        :param name:
            The value to assign to the name property of this LogAnalyticsLabelAlias.
        :type name: str

        :param priority:
            The value to assign to the priority property of this LogAnalyticsLabelAlias.
            Allowed values for this property are: "NONE", "LOW", "MEDIUM", "HIGH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type priority: str

        """
        self.swagger_types = {
            'alias': 'str',
            'alias_display_name': 'str',
            'is_system': 'bool',
            'display_name': 'str',
            'name': 'str',
            'priority': 'str'
        }

        self.attribute_map = {
            'alias': 'alias',
            'alias_display_name': 'aliasDisplayName',
            'is_system': 'isSystem',
            'display_name': 'displayName',
            'name': 'name',
            'priority': 'priority'
        }

        self._alias = None
        self._alias_display_name = None
        self._is_system = None
        self._display_name = None
        self._name = None
        self._priority = None

    @property
    def alias(self):
        """
        Gets the alias of this LogAnalyticsLabelAlias.
        The alias.


        :return: The alias of this LogAnalyticsLabelAlias.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """
        Sets the alias of this LogAnalyticsLabelAlias.
        The alias.


        :param alias: The alias of this LogAnalyticsLabelAlias.
        :type: str
        """
        self._alias = alias

    @property
    def alias_display_name(self):
        """
        Gets the alias_display_name of this LogAnalyticsLabelAlias.
        The alias display name.


        :return: The alias_display_name of this LogAnalyticsLabelAlias.
        :rtype: str
        """
        return self._alias_display_name

    @alias_display_name.setter
    def alias_display_name(self, alias_display_name):
        """
        Sets the alias_display_name of this LogAnalyticsLabelAlias.
        The alias display name.


        :param alias_display_name: The alias_display_name of this LogAnalyticsLabelAlias.
        :type: str
        """
        self._alias_display_name = alias_display_name

    @property
    def is_system(self):
        """
        Gets the is_system of this LogAnalyticsLabelAlias.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :return: The is_system of this LogAnalyticsLabelAlias.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this LogAnalyticsLabelAlias.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :param is_system: The is_system of this LogAnalyticsLabelAlias.
        :type: bool
        """
        self._is_system = is_system

    @property
    def display_name(self):
        """
        Gets the display_name of this LogAnalyticsLabelAlias.
        The label display name.


        :return: The display_name of this LogAnalyticsLabelAlias.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LogAnalyticsLabelAlias.
        The label display name.


        :param display_name: The display_name of this LogAnalyticsLabelAlias.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        Gets the name of this LogAnalyticsLabelAlias.
        The label name.


        :return: The name of this LogAnalyticsLabelAlias.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsLabelAlias.
        The label name.


        :param name: The name of this LogAnalyticsLabelAlias.
        :type: str
        """
        self._name = name

    @property
    def priority(self):
        """
        Gets the priority of this LogAnalyticsLabelAlias.
        The label priority. Default value is NONE.

        Allowed values for this property are: "NONE", "LOW", "MEDIUM", "HIGH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The priority of this LogAnalyticsLabelAlias.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this LogAnalyticsLabelAlias.
        The label priority. Default value is NONE.


        :param priority: The priority of this LogAnalyticsLabelAlias.
        :type: str
        """
        allowed_values = ["NONE", "LOW", "MEDIUM", "HIGH"]
        if not value_allowed_none_or_none_sentinel(priority, allowed_values):
            priority = 'UNKNOWN_ENUM_VALUE'
        self._priority = priority

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
