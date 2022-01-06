# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsParserFilter(object):
    """
    LogAnalyticsParserFilter
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsParserFilter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this LogAnalyticsParserFilter.
        :type id: str

        :param parser:
            The value to assign to the parser property of this LogAnalyticsParserFilter.
        :type parser: oci.log_analytics.models.LogAnalyticsParser

        :param agent_version:
            The value to assign to the agent_version property of this LogAnalyticsParserFilter.
        :type agent_version: str

        :param is_in_use:
            The value to assign to the is_in_use property of this LogAnalyticsParserFilter.
        :type is_in_use: int

        :param operating_system:
            The value to assign to the operating_system property of this LogAnalyticsParserFilter.
        :type operating_system: str

        :param parser_id:
            The value to assign to the parser_id property of this LogAnalyticsParserFilter.
        :type parser_id: int

        :param version:
            The value to assign to the version property of this LogAnalyticsParserFilter.
        :type version: str

        """
        self.swagger_types = {
            'id': 'str',
            'parser': 'LogAnalyticsParser',
            'agent_version': 'str',
            'is_in_use': 'int',
            'operating_system': 'str',
            'parser_id': 'int',
            'version': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'parser': 'parser',
            'agent_version': 'agentVersion',
            'is_in_use': 'isInUse',
            'operating_system': 'operatingSystem',
            'parser_id': 'parserId',
            'version': 'version'
        }

        self._id = None
        self._parser = None
        self._agent_version = None
        self._is_in_use = None
        self._operating_system = None
        self._parser_id = None
        self._version = None

    @property
    def id(self):
        """
        Gets the id of this LogAnalyticsParserFilter.
        The parser filter unique identifier.


        :return: The id of this LogAnalyticsParserFilter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LogAnalyticsParserFilter.
        The parser filter unique identifier.


        :param id: The id of this LogAnalyticsParserFilter.
        :type: str
        """
        self._id = id

    @property
    def parser(self):
        """
        Gets the parser of this LogAnalyticsParserFilter.

        :return: The parser of this LogAnalyticsParserFilter.
        :rtype: oci.log_analytics.models.LogAnalyticsParser
        """
        return self._parser

    @parser.setter
    def parser(self, parser):
        """
        Sets the parser of this LogAnalyticsParserFilter.

        :param parser: The parser of this LogAnalyticsParserFilter.
        :type: oci.log_analytics.models.LogAnalyticsParser
        """
        self._parser = parser

    @property
    def agent_version(self):
        """
        Gets the agent_version of this LogAnalyticsParserFilter.
        The agent version.


        :return: The agent_version of this LogAnalyticsParserFilter.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """
        Sets the agent_version of this LogAnalyticsParserFilter.
        The agent version.


        :param agent_version: The agent_version of this LogAnalyticsParserFilter.
        :type: str
        """
        self._agent_version = agent_version

    @property
    def is_in_use(self):
        """
        Gets the is_in_use of this LogAnalyticsParserFilter.
        A flag idicating whether or not hte filter is currently being used.


        :return: The is_in_use of this LogAnalyticsParserFilter.
        :rtype: int
        """
        return self._is_in_use

    @is_in_use.setter
    def is_in_use(self, is_in_use):
        """
        Sets the is_in_use of this LogAnalyticsParserFilter.
        A flag idicating whether or not hte filter is currently being used.


        :param is_in_use: The is_in_use of this LogAnalyticsParserFilter.
        :type: int
        """
        self._is_in_use = is_in_use

    @property
    def operating_system(self):
        """
        Gets the operating_system of this LogAnalyticsParserFilter.
        The operating system.


        :return: The operating_system of this LogAnalyticsParserFilter.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """
        Sets the operating_system of this LogAnalyticsParserFilter.
        The operating system.


        :param operating_system: The operating_system of this LogAnalyticsParserFilter.
        :type: str
        """
        self._operating_system = operating_system

    @property
    def parser_id(self):
        """
        Gets the parser_id of this LogAnalyticsParserFilter.
        The parser unique identifier.


        :return: The parser_id of this LogAnalyticsParserFilter.
        :rtype: int
        """
        return self._parser_id

    @parser_id.setter
    def parser_id(self, parser_id):
        """
        Sets the parser_id of this LogAnalyticsParserFilter.
        The parser unique identifier.


        :param parser_id: The parser_id of this LogAnalyticsParserFilter.
        :type: int
        """
        self._parser_id = parser_id

    @property
    def version(self):
        """
        Gets the version of this LogAnalyticsParserFilter.
        The version.


        :return: The version of this LogAnalyticsParserFilter.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this LogAnalyticsParserFilter.
        The version.


        :param version: The version of this LogAnalyticsParserFilter.
        :type: str
        """
        self._version = version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
