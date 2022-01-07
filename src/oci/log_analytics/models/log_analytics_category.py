# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsCategory(object):
    """
    A category into which resources can be placed.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsCategory object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this LogAnalyticsCategory.
        :type name: str

        :param description:
            The value to assign to the description property of this LogAnalyticsCategory.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this LogAnalyticsCategory.
        :type display_name: str

        :param type:
            The value to assign to the type property of this LogAnalyticsCategory.
        :type type: str

        :param is_system:
            The value to assign to the is_system property of this LogAnalyticsCategory.
        :type is_system: bool

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'display_name': 'str',
            'type': 'str',
            'is_system': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'display_name': 'displayName',
            'type': 'type',
            'is_system': 'isSystem'
        }

        self._name = None
        self._description = None
        self._display_name = None
        self._type = None
        self._is_system = None

    @property
    def name(self):
        """
        Gets the name of this LogAnalyticsCategory.
        The unique name that identifies the category.


        :return: The name of this LogAnalyticsCategory.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsCategory.
        The unique name that identifies the category.


        :param name: The name of this LogAnalyticsCategory.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this LogAnalyticsCategory.
        The category description.


        :return: The description of this LogAnalyticsCategory.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogAnalyticsCategory.
        The category description.


        :param description: The description of this LogAnalyticsCategory.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this LogAnalyticsCategory.
        The category display name.


        :return: The display_name of this LogAnalyticsCategory.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LogAnalyticsCategory.
        The category display name.


        :param display_name: The display_name of this LogAnalyticsCategory.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        Gets the type of this LogAnalyticsCategory.
        The category type. Values include \"PRODUCT\", \"TIER\", \"VENDOR\" and \"GENERIC\".


        :return: The type of this LogAnalyticsCategory.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this LogAnalyticsCategory.
        The category type. Values include \"PRODUCT\", \"TIER\", \"VENDOR\" and \"GENERIC\".


        :param type: The type of this LogAnalyticsCategory.
        :type: str
        """
        self._type = type

    @property
    def is_system(self):
        """
        Gets the is_system of this LogAnalyticsCategory.
        The system flag. A value of false denotes a user-created
        category. A value of true denotes an Oracle-defined category.


        :return: The is_system of this LogAnalyticsCategory.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this LogAnalyticsCategory.
        The system flag. A value of false denotes a user-created
        category. A value of true denotes an Oracle-defined category.


        :param is_system: The is_system of this LogAnalyticsCategory.
        :type: bool
        """
        self._is_system = is_system

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
