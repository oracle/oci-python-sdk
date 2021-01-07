# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsParserFunction(object):
    """
    LogAnalyticsParserFunction
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsParserFunction object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param parser_meta_plugin:
            The value to assign to the parser_meta_plugin property of this LogAnalyticsParserFunction.
        :type parser_meta_plugin: oci.log_analytics.models.LogAnalyticsParserMetaPlugin

        :param parser_function_id:
            The value to assign to the parser_function_id property of this LogAnalyticsParserFunction.
        :type parser_function_id: int

        :param parser_function_name:
            The value to assign to the parser_function_name property of this LogAnalyticsParserFunction.
        :type parser_function_name: str

        :param is_enabled:
            The value to assign to the is_enabled property of this LogAnalyticsParserFunction.
        :type is_enabled: bool

        :param is_system:
            The value to assign to the is_system property of this LogAnalyticsParserFunction.
        :type is_system: bool

        :param parser_id:
            The value to assign to the parser_id property of this LogAnalyticsParserFunction.
        :type parser_id: int

        :param parser_name:
            The value to assign to the parser_name property of this LogAnalyticsParserFunction.
        :type parser_name: str

        :param parser_meta_plugin_name:
            The value to assign to the parser_meta_plugin_name property of this LogAnalyticsParserFunction.
        :type parser_meta_plugin_name: str

        :param parser_function_priority:
            The value to assign to the parser_function_priority property of this LogAnalyticsParserFunction.
        :type parser_function_priority: int

        :param parser_function_parameters:
            The value to assign to the parser_function_parameters property of this LogAnalyticsParserFunction.
        :type parser_function_parameters: list[oci.log_analytics.models.LogAnalyticsParserFunctionParameter]

        """
        self.swagger_types = {
            'parser_meta_plugin': 'LogAnalyticsParserMetaPlugin',
            'parser_function_id': 'int',
            'parser_function_name': 'str',
            'is_enabled': 'bool',
            'is_system': 'bool',
            'parser_id': 'int',
            'parser_name': 'str',
            'parser_meta_plugin_name': 'str',
            'parser_function_priority': 'int',
            'parser_function_parameters': 'list[LogAnalyticsParserFunctionParameter]'
        }

        self.attribute_map = {
            'parser_meta_plugin': 'parserMetaPlugin',
            'parser_function_id': 'parserFunctionId',
            'parser_function_name': 'parserFunctionName',
            'is_enabled': 'isEnabled',
            'is_system': 'isSystem',
            'parser_id': 'parserId',
            'parser_name': 'parserName',
            'parser_meta_plugin_name': 'parserMetaPluginName',
            'parser_function_priority': 'parserFunctionPriority',
            'parser_function_parameters': 'parserFunctionParameters'
        }

        self._parser_meta_plugin = None
        self._parser_function_id = None
        self._parser_function_name = None
        self._is_enabled = None
        self._is_system = None
        self._parser_id = None
        self._parser_name = None
        self._parser_meta_plugin_name = None
        self._parser_function_priority = None
        self._parser_function_parameters = None

    @property
    def parser_meta_plugin(self):
        """
        Gets the parser_meta_plugin of this LogAnalyticsParserFunction.

        :return: The parser_meta_plugin of this LogAnalyticsParserFunction.
        :rtype: oci.log_analytics.models.LogAnalyticsParserMetaPlugin
        """
        return self._parser_meta_plugin

    @parser_meta_plugin.setter
    def parser_meta_plugin(self, parser_meta_plugin):
        """
        Sets the parser_meta_plugin of this LogAnalyticsParserFunction.

        :param parser_meta_plugin: The parser_meta_plugin of this LogAnalyticsParserFunction.
        :type: oci.log_analytics.models.LogAnalyticsParserMetaPlugin
        """
        self._parser_meta_plugin = parser_meta_plugin

    @property
    def parser_function_id(self):
        """
        Gets the parser_function_id of this LogAnalyticsParserFunction.
        plugin instance Id


        :return: The parser_function_id of this LogAnalyticsParserFunction.
        :rtype: int
        """
        return self._parser_function_id

    @parser_function_id.setter
    def parser_function_id(self, parser_function_id):
        """
        Sets the parser_function_id of this LogAnalyticsParserFunction.
        plugin instance Id


        :param parser_function_id: The parser_function_id of this LogAnalyticsParserFunction.
        :type: int
        """
        self._parser_function_id = parser_function_id

    @property
    def parser_function_name(self):
        """
        Gets the parser_function_name of this LogAnalyticsParserFunction.
        plugin instance internal name


        :return: The parser_function_name of this LogAnalyticsParserFunction.
        :rtype: str
        """
        return self._parser_function_name

    @parser_function_name.setter
    def parser_function_name(self, parser_function_name):
        """
        Sets the parser_function_name of this LogAnalyticsParserFunction.
        plugin instance internal name


        :param parser_function_name: The parser_function_name of this LogAnalyticsParserFunction.
        :type: str
        """
        self._parser_function_name = parser_function_name

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this LogAnalyticsParserFunction.
        is enabled flag


        :return: The is_enabled of this LogAnalyticsParserFunction.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this LogAnalyticsParserFunction.
        is enabled flag


        :param is_enabled: The is_enabled of this LogAnalyticsParserFunction.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def is_system(self):
        """
        Gets the is_system of this LogAnalyticsParserFunction.
        is system flag


        :return: The is_system of this LogAnalyticsParserFunction.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this LogAnalyticsParserFunction.
        is system flag


        :param is_system: The is_system of this LogAnalyticsParserFunction.
        :type: bool
        """
        self._is_system = is_system

    @property
    def parser_id(self):
        """
        Gets the parser_id of this LogAnalyticsParserFunction.
        parser Id


        :return: The parser_id of this LogAnalyticsParserFunction.
        :rtype: int
        """
        return self._parser_id

    @parser_id.setter
    def parser_id(self, parser_id):
        """
        Sets the parser_id of this LogAnalyticsParserFunction.
        parser Id


        :param parser_id: The parser_id of this LogAnalyticsParserFunction.
        :type: int
        """
        self._parser_id = parser_id

    @property
    def parser_name(self):
        """
        Gets the parser_name of this LogAnalyticsParserFunction.
        parser internal name


        :return: The parser_name of this LogAnalyticsParserFunction.
        :rtype: str
        """
        return self._parser_name

    @parser_name.setter
    def parser_name(self, parser_name):
        """
        Sets the parser_name of this LogAnalyticsParserFunction.
        parser internal name


        :param parser_name: The parser_name of this LogAnalyticsParserFunction.
        :type: str
        """
        self._parser_name = parser_name

    @property
    def parser_meta_plugin_name(self):
        """
        Gets the parser_meta_plugin_name of this LogAnalyticsParserFunction.
        plugin type internal name


        :return: The parser_meta_plugin_name of this LogAnalyticsParserFunction.
        :rtype: str
        """
        return self._parser_meta_plugin_name

    @parser_meta_plugin_name.setter
    def parser_meta_plugin_name(self, parser_meta_plugin_name):
        """
        Sets the parser_meta_plugin_name of this LogAnalyticsParserFunction.
        plugin type internal name


        :param parser_meta_plugin_name: The parser_meta_plugin_name of this LogAnalyticsParserFunction.
        :type: str
        """
        self._parser_meta_plugin_name = parser_meta_plugin_name

    @property
    def parser_function_priority(self):
        """
        Gets the parser_function_priority of this LogAnalyticsParserFunction.
        priority


        :return: The parser_function_priority of this LogAnalyticsParserFunction.
        :rtype: int
        """
        return self._parser_function_priority

    @parser_function_priority.setter
    def parser_function_priority(self, parser_function_priority):
        """
        Sets the parser_function_priority of this LogAnalyticsParserFunction.
        priority


        :param parser_function_priority: The parser_function_priority of this LogAnalyticsParserFunction.
        :type: int
        """
        self._parser_function_priority = parser_function_priority

    @property
    def parser_function_parameters(self):
        """
        Gets the parser_function_parameters of this LogAnalyticsParserFunction.
        parameter map list


        :return: The parser_function_parameters of this LogAnalyticsParserFunction.
        :rtype: list[oci.log_analytics.models.LogAnalyticsParserFunctionParameter]
        """
        return self._parser_function_parameters

    @parser_function_parameters.setter
    def parser_function_parameters(self, parser_function_parameters):
        """
        Sets the parser_function_parameters of this LogAnalyticsParserFunction.
        parameter map list


        :param parser_function_parameters: The parser_function_parameters of this LogAnalyticsParserFunction.
        :type: list[oci.log_analytics.models.LogAnalyticsParserFunctionParameter]
        """
        self._parser_function_parameters = parser_function_parameters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
