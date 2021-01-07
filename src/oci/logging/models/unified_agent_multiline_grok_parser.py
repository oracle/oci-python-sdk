# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .unified_agent_parser import UnifiedAgentParser
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnifiedAgentMultilineGrokParser(UnifiedAgentParser):
    """
    Multiline grok parser.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UnifiedAgentMultilineGrokParser object with values from keyword arguments. The default value of the :py:attr:`~oci.logging.models.UnifiedAgentMultilineGrokParser.parser_type` attribute
        of this class is ``MULTILINE_GROK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param parser_type:
            The value to assign to the parser_type property of this UnifiedAgentMultilineGrokParser.
            Allowed values for this property are: "AUDITD", "JSON", "TSV", "CSV", "NONE", "SYSLOG", "APACHE2", "APACHE_ERROR", "MSGPACK", "REGEXP", "MULTILINE", "GROK", "MULTILINE_GROK"
        :type parser_type: str

        :param field_time_key:
            The value to assign to the field_time_key property of this UnifiedAgentMultilineGrokParser.
        :type field_time_key: str

        :param types:
            The value to assign to the types property of this UnifiedAgentMultilineGrokParser.
        :type types: dict(str, str)

        :param null_value_pattern:
            The value to assign to the null_value_pattern property of this UnifiedAgentMultilineGrokParser.
        :type null_value_pattern: str

        :param is_null_empty_string:
            The value to assign to the is_null_empty_string property of this UnifiedAgentMultilineGrokParser.
        :type is_null_empty_string: bool

        :param is_estimate_current_event:
            The value to assign to the is_estimate_current_event property of this UnifiedAgentMultilineGrokParser.
        :type is_estimate_current_event: bool

        :param is_keep_time_key:
            The value to assign to the is_keep_time_key property of this UnifiedAgentMultilineGrokParser.
        :type is_keep_time_key: bool

        :param timeout_in_milliseconds:
            The value to assign to the timeout_in_milliseconds property of this UnifiedAgentMultilineGrokParser.
        :type timeout_in_milliseconds: int

        :param grok_name_key:
            The value to assign to the grok_name_key property of this UnifiedAgentMultilineGrokParser.
        :type grok_name_key: str

        :param grok_failure_key:
            The value to assign to the grok_failure_key property of this UnifiedAgentMultilineGrokParser.
        :type grok_failure_key: str

        :param multi_line_start_regexp:
            The value to assign to the multi_line_start_regexp property of this UnifiedAgentMultilineGrokParser.
        :type multi_line_start_regexp: str

        :param patterns:
            The value to assign to the patterns property of this UnifiedAgentMultilineGrokParser.
        :type patterns: list[oci.logging.models.GrokPattern]

        """
        self.swagger_types = {
            'parser_type': 'str',
            'field_time_key': 'str',
            'types': 'dict(str, str)',
            'null_value_pattern': 'str',
            'is_null_empty_string': 'bool',
            'is_estimate_current_event': 'bool',
            'is_keep_time_key': 'bool',
            'timeout_in_milliseconds': 'int',
            'grok_name_key': 'str',
            'grok_failure_key': 'str',
            'multi_line_start_regexp': 'str',
            'patterns': 'list[GrokPattern]'
        }

        self.attribute_map = {
            'parser_type': 'parserType',
            'field_time_key': 'fieldTimeKey',
            'types': 'types',
            'null_value_pattern': 'nullValuePattern',
            'is_null_empty_string': 'isNullEmptyString',
            'is_estimate_current_event': 'isEstimateCurrentEvent',
            'is_keep_time_key': 'isKeepTimeKey',
            'timeout_in_milliseconds': 'timeoutInMilliseconds',
            'grok_name_key': 'grokNameKey',
            'grok_failure_key': 'grokFailureKey',
            'multi_line_start_regexp': 'multiLineStartRegexp',
            'patterns': 'patterns'
        }

        self._parser_type = None
        self._field_time_key = None
        self._types = None
        self._null_value_pattern = None
        self._is_null_empty_string = None
        self._is_estimate_current_event = None
        self._is_keep_time_key = None
        self._timeout_in_milliseconds = None
        self._grok_name_key = None
        self._grok_failure_key = None
        self._multi_line_start_regexp = None
        self._patterns = None
        self._parser_type = 'MULTILINE_GROK'

    @property
    def grok_name_key(self):
        """
        Gets the grok_name_key of this UnifiedAgentMultilineGrokParser.

        :return: The grok_name_key of this UnifiedAgentMultilineGrokParser.
        :rtype: str
        """
        return self._grok_name_key

    @grok_name_key.setter
    def grok_name_key(self, grok_name_key):
        """
        Sets the grok_name_key of this UnifiedAgentMultilineGrokParser.

        :param grok_name_key: The grok_name_key of this UnifiedAgentMultilineGrokParser.
        :type: str
        """
        self._grok_name_key = grok_name_key

    @property
    def grok_failure_key(self):
        """
        Gets the grok_failure_key of this UnifiedAgentMultilineGrokParser.

        :return: The grok_failure_key of this UnifiedAgentMultilineGrokParser.
        :rtype: str
        """
        return self._grok_failure_key

    @grok_failure_key.setter
    def grok_failure_key(self, grok_failure_key):
        """
        Sets the grok_failure_key of this UnifiedAgentMultilineGrokParser.

        :param grok_failure_key: The grok_failure_key of this UnifiedAgentMultilineGrokParser.
        :type: str
        """
        self._grok_failure_key = grok_failure_key

    @property
    def multi_line_start_regexp(self):
        """
        Gets the multi_line_start_regexp of this UnifiedAgentMultilineGrokParser.

        :return: The multi_line_start_regexp of this UnifiedAgentMultilineGrokParser.
        :rtype: str
        """
        return self._multi_line_start_regexp

    @multi_line_start_regexp.setter
    def multi_line_start_regexp(self, multi_line_start_regexp):
        """
        Sets the multi_line_start_regexp of this UnifiedAgentMultilineGrokParser.

        :param multi_line_start_regexp: The multi_line_start_regexp of this UnifiedAgentMultilineGrokParser.
        :type: str
        """
        self._multi_line_start_regexp = multi_line_start_regexp

    @property
    def patterns(self):
        """
        Gets the patterns of this UnifiedAgentMultilineGrokParser.

        :return: The patterns of this UnifiedAgentMultilineGrokParser.
        :rtype: list[oci.logging.models.GrokPattern]
        """
        return self._patterns

    @patterns.setter
    def patterns(self, patterns):
        """
        Sets the patterns of this UnifiedAgentMultilineGrokParser.

        :param patterns: The patterns of this UnifiedAgentMultilineGrokParser.
        :type: list[oci.logging.models.GrokPattern]
        """
        self._patterns = patterns

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
