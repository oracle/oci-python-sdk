# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsPatternFilter(object):
    """
    LogAnalyticsPatternFilter
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsPatternFilter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param pattern:
            The value to assign to the pattern property of this LogAnalyticsPatternFilter.
        :type pattern: LogAnalyticsSourcePattern

        :param agent_version:
            The value to assign to the agent_version property of this LogAnalyticsPatternFilter.
        :type agent_version: str

        :param is_in_use:
            The value to assign to the is_in_use property of this LogAnalyticsPatternFilter.
        :type is_in_use: bool

        :param operating_system:
            The value to assign to the operating_system property of this LogAnalyticsPatternFilter.
        :type operating_system: str

        :param pattern_id:
            The value to assign to the pattern_id property of this LogAnalyticsPatternFilter.
        :type pattern_id: int

        :param source_id:
            The value to assign to the source_id property of this LogAnalyticsPatternFilter.
        :type source_id: int

        :param version:
            The value to assign to the version property of this LogAnalyticsPatternFilter.
        :type version: str

        :param source:
            The value to assign to the source property of this LogAnalyticsPatternFilter.
        :type source: LogAnalyticsSource

        """
        self.swagger_types = {
            'pattern': 'LogAnalyticsSourcePattern',
            'agent_version': 'str',
            'is_in_use': 'bool',
            'operating_system': 'str',
            'pattern_id': 'int',
            'source_id': 'int',
            'version': 'str',
            'source': 'LogAnalyticsSource'
        }

        self.attribute_map = {
            'pattern': 'pattern',
            'agent_version': 'agentVersion',
            'is_in_use': 'isInUse',
            'operating_system': 'operatingSystem',
            'pattern_id': 'patternId',
            'source_id': 'sourceId',
            'version': 'version',
            'source': 'source'
        }

        self._pattern = None
        self._agent_version = None
        self._is_in_use = None
        self._operating_system = None
        self._pattern_id = None
        self._source_id = None
        self._version = None
        self._source = None

    @property
    def pattern(self):
        """
        Gets the pattern of this LogAnalyticsPatternFilter.

        :return: The pattern of this LogAnalyticsPatternFilter.
        :rtype: LogAnalyticsSourcePattern
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this LogAnalyticsPatternFilter.

        :param pattern: The pattern of this LogAnalyticsPatternFilter.
        :type: LogAnalyticsSourcePattern
        """
        self._pattern = pattern

    @property
    def agent_version(self):
        """
        Gets the agent_version of this LogAnalyticsPatternFilter.
        agent version


        :return: The agent_version of this LogAnalyticsPatternFilter.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """
        Sets the agent_version of this LogAnalyticsPatternFilter.
        agent version


        :param agent_version: The agent_version of this LogAnalyticsPatternFilter.
        :type: str
        """
        self._agent_version = agent_version

    @property
    def is_in_use(self):
        """
        Gets the is_in_use of this LogAnalyticsPatternFilter.
        is in use flag


        :return: The is_in_use of this LogAnalyticsPatternFilter.
        :rtype: bool
        """
        return self._is_in_use

    @is_in_use.setter
    def is_in_use(self, is_in_use):
        """
        Sets the is_in_use of this LogAnalyticsPatternFilter.
        is in use flag


        :param is_in_use: The is_in_use of this LogAnalyticsPatternFilter.
        :type: bool
        """
        self._is_in_use = is_in_use

    @property
    def operating_system(self):
        """
        Gets the operating_system of this LogAnalyticsPatternFilter.
        operating system


        :return: The operating_system of this LogAnalyticsPatternFilter.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """
        Sets the operating_system of this LogAnalyticsPatternFilter.
        operating system


        :param operating_system: The operating_system of this LogAnalyticsPatternFilter.
        :type: str
        """
        self._operating_system = operating_system

    @property
    def pattern_id(self):
        """
        Gets the pattern_id of this LogAnalyticsPatternFilter.
        pattern Id


        :return: The pattern_id of this LogAnalyticsPatternFilter.
        :rtype: int
        """
        return self._pattern_id

    @pattern_id.setter
    def pattern_id(self, pattern_id):
        """
        Sets the pattern_id of this LogAnalyticsPatternFilter.
        pattern Id


        :param pattern_id: The pattern_id of this LogAnalyticsPatternFilter.
        :type: int
        """
        self._pattern_id = pattern_id

    @property
    def source_id(self):
        """
        Gets the source_id of this LogAnalyticsPatternFilter.
        source Id


        :return: The source_id of this LogAnalyticsPatternFilter.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this LogAnalyticsPatternFilter.
        source Id


        :param source_id: The source_id of this LogAnalyticsPatternFilter.
        :type: int
        """
        self._source_id = source_id

    @property
    def version(self):
        """
        Gets the version of this LogAnalyticsPatternFilter.
        version


        :return: The version of this LogAnalyticsPatternFilter.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this LogAnalyticsPatternFilter.
        version


        :param version: The version of this LogAnalyticsPatternFilter.
        :type: str
        """
        self._version = version

    @property
    def source(self):
        """
        Gets the source of this LogAnalyticsPatternFilter.

        :return: The source of this LogAnalyticsPatternFilter.
        :rtype: LogAnalyticsSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this LogAnalyticsPatternFilter.

        :param source: The source of this LogAnalyticsPatternFilter.
        :type: LogAnalyticsSource
        """
        self._source = source

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
