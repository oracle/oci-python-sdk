# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsSourceFunction(object):
    """
    LogAnalyticsSourceFunction
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsSourceFunction object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param arguments:
            The value to assign to the arguments property of this LogAnalyticsSourceFunction.
        :type arguments: list[LogAnalyticsMetaFunctionArgument]

        :param is_enabled:
            The value to assign to the is_enabled property of this LogAnalyticsSourceFunction.
        :type is_enabled: bool

        :param function:
            The value to assign to the function property of this LogAnalyticsSourceFunction.
        :type function: LogAnalyticsMetaFunction

        :param function_id:
            The value to assign to the function_id property of this LogAnalyticsSourceFunction.
        :type function_id: int

        :param order:
            The value to assign to the order property of this LogAnalyticsSourceFunction.
        :type order: int

        :param is_system:
            The value to assign to the is_system property of this LogAnalyticsSourceFunction.
        :type is_system: bool

        :param lookup_column:
            The value to assign to the lookup_column property of this LogAnalyticsSourceFunction.
        :type lookup_column: str

        :param lookup_column_position:
            The value to assign to the lookup_column_position property of this LogAnalyticsSourceFunction.
        :type lookup_column_position: int

        :param lookup_display_name:
            The value to assign to the lookup_display_name property of this LogAnalyticsSourceFunction.
        :type lookup_display_name: str

        :param lookup_mode:
            The value to assign to the lookup_mode property of this LogAnalyticsSourceFunction.
        :type lookup_mode: int

        :param lookup_table:
            The value to assign to the lookup_table property of this LogAnalyticsSourceFunction.
        :type lookup_table: str

        :param source_id:
            The value to assign to the source_id property of this LogAnalyticsSourceFunction.
        :type source_id: int

        """
        self.swagger_types = {
            'arguments': 'list[LogAnalyticsMetaFunctionArgument]',
            'is_enabled': 'bool',
            'function': 'LogAnalyticsMetaFunction',
            'function_id': 'int',
            'order': 'int',
            'is_system': 'bool',
            'lookup_column': 'str',
            'lookup_column_position': 'int',
            'lookup_display_name': 'str',
            'lookup_mode': 'int',
            'lookup_table': 'str',
            'source_id': 'int'
        }

        self.attribute_map = {
            'arguments': 'arguments',
            'is_enabled': 'isEnabled',
            'function': 'function',
            'function_id': 'functionId',
            'order': 'order',
            'is_system': 'isSystem',
            'lookup_column': 'lookupColumn',
            'lookup_column_position': 'lookupColumnPosition',
            'lookup_display_name': 'lookupDisplayName',
            'lookup_mode': 'lookupMode',
            'lookup_table': 'lookupTable',
            'source_id': 'sourceId'
        }

        self._arguments = None
        self._is_enabled = None
        self._function = None
        self._function_id = None
        self._order = None
        self._is_system = None
        self._lookup_column = None
        self._lookup_column_position = None
        self._lookup_display_name = None
        self._lookup_mode = None
        self._lookup_table = None
        self._source_id = None

    @property
    def arguments(self):
        """
        Gets the arguments of this LogAnalyticsSourceFunction.
        argument


        :return: The arguments of this LogAnalyticsSourceFunction.
        :rtype: list[LogAnalyticsMetaFunctionArgument]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """
        Sets the arguments of this LogAnalyticsSourceFunction.
        argument


        :param arguments: The arguments of this LogAnalyticsSourceFunction.
        :type: list[LogAnalyticsMetaFunctionArgument]
        """
        self._arguments = arguments

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this LogAnalyticsSourceFunction.
        enabled flag


        :return: The is_enabled of this LogAnalyticsSourceFunction.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this LogAnalyticsSourceFunction.
        enabled flag


        :param is_enabled: The is_enabled of this LogAnalyticsSourceFunction.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def function(self):
        """
        Gets the function of this LogAnalyticsSourceFunction.

        :return: The function of this LogAnalyticsSourceFunction.
        :rtype: LogAnalyticsMetaFunction
        """
        return self._function

    @function.setter
    def function(self, function):
        """
        Sets the function of this LogAnalyticsSourceFunction.

        :param function: The function of this LogAnalyticsSourceFunction.
        :type: LogAnalyticsMetaFunction
        """
        self._function = function

    @property
    def function_id(self):
        """
        Gets the function_id of this LogAnalyticsSourceFunction.
        source function Id


        :return: The function_id of this LogAnalyticsSourceFunction.
        :rtype: int
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """
        Sets the function_id of this LogAnalyticsSourceFunction.
        source function Id


        :param function_id: The function_id of this LogAnalyticsSourceFunction.
        :type: int
        """
        self._function_id = function_id

    @property
    def order(self):
        """
        Gets the order of this LogAnalyticsSourceFunction.
        source function order


        :return: The order of this LogAnalyticsSourceFunction.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this LogAnalyticsSourceFunction.
        source function order


        :param order: The order of this LogAnalyticsSourceFunction.
        :type: int
        """
        self._order = order

    @property
    def is_system(self):
        """
        Gets the is_system of this LogAnalyticsSourceFunction.
        is system flag


        :return: The is_system of this LogAnalyticsSourceFunction.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this LogAnalyticsSourceFunction.
        is system flag


        :param is_system: The is_system of this LogAnalyticsSourceFunction.
        :type: bool
        """
        self._is_system = is_system

    @property
    def lookup_column(self):
        """
        Gets the lookup_column of this LogAnalyticsSourceFunction.
        column


        :return: The lookup_column of this LogAnalyticsSourceFunction.
        :rtype: str
        """
        return self._lookup_column

    @lookup_column.setter
    def lookup_column(self, lookup_column):
        """
        Sets the lookup_column of this LogAnalyticsSourceFunction.
        column


        :param lookup_column: The lookup_column of this LogAnalyticsSourceFunction.
        :type: str
        """
        self._lookup_column = lookup_column

    @property
    def lookup_column_position(self):
        """
        Gets the lookup_column_position of this LogAnalyticsSourceFunction.
        column position


        :return: The lookup_column_position of this LogAnalyticsSourceFunction.
        :rtype: int
        """
        return self._lookup_column_position

    @lookup_column_position.setter
    def lookup_column_position(self, lookup_column_position):
        """
        Sets the lookup_column_position of this LogAnalyticsSourceFunction.
        column position


        :param lookup_column_position: The lookup_column_position of this LogAnalyticsSourceFunction.
        :type: int
        """
        self._lookup_column_position = lookup_column_position

    @property
    def lookup_display_name(self):
        """
        Gets the lookup_display_name of this LogAnalyticsSourceFunction.
        lookup display name


        :return: The lookup_display_name of this LogAnalyticsSourceFunction.
        :rtype: str
        """
        return self._lookup_display_name

    @lookup_display_name.setter
    def lookup_display_name(self, lookup_display_name):
        """
        Sets the lookup_display_name of this LogAnalyticsSourceFunction.
        lookup display name


        :param lookup_display_name: The lookup_display_name of this LogAnalyticsSourceFunction.
        :type: str
        """
        self._lookup_display_name = lookup_display_name

    @property
    def lookup_mode(self):
        """
        Gets the lookup_mode of this LogAnalyticsSourceFunction.
        lookup mode


        :return: The lookup_mode of this LogAnalyticsSourceFunction.
        :rtype: int
        """
        return self._lookup_mode

    @lookup_mode.setter
    def lookup_mode(self, lookup_mode):
        """
        Sets the lookup_mode of this LogAnalyticsSourceFunction.
        lookup mode


        :param lookup_mode: The lookup_mode of this LogAnalyticsSourceFunction.
        :type: int
        """
        self._lookup_mode = lookup_mode

    @property
    def lookup_table(self):
        """
        Gets the lookup_table of this LogAnalyticsSourceFunction.
        lookup table


        :return: The lookup_table of this LogAnalyticsSourceFunction.
        :rtype: str
        """
        return self._lookup_table

    @lookup_table.setter
    def lookup_table(self, lookup_table):
        """
        Sets the lookup_table of this LogAnalyticsSourceFunction.
        lookup table


        :param lookup_table: The lookup_table of this LogAnalyticsSourceFunction.
        :type: str
        """
        self._lookup_table = lookup_table

    @property
    def source_id(self):
        """
        Gets the source_id of this LogAnalyticsSourceFunction.
        source Id


        :return: The source_id of this LogAnalyticsSourceFunction.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this LogAnalyticsSourceFunction.
        source Id


        :param source_id: The source_id of this LogAnalyticsSourceFunction.
        :type: int
        """
        self._source_id = source_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
