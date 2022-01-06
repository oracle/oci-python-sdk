# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .unified_agent_parser import UnifiedAgentParser
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnifiedAgentNoneParser(UnifiedAgentParser):
    """
    This parser signifies a non-parser, and puts the entire log line in a message_key.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UnifiedAgentNoneParser object with values from keyword arguments. The default value of the :py:attr:`~oci.logging.models.UnifiedAgentNoneParser.parser_type` attribute
        of this class is ``NONE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param parser_type:
            The value to assign to the parser_type property of this UnifiedAgentNoneParser.
            Allowed values for this property are: "AUDITD", "JSON", "TSV", "CSV", "NONE", "SYSLOG", "APACHE2", "APACHE_ERROR", "MSGPACK", "REGEXP", "MULTILINE", "GROK", "MULTILINE_GROK"
        :type parser_type: str

        :param field_time_key:
            The value to assign to the field_time_key property of this UnifiedAgentNoneParser.
        :type field_time_key: str

        :param types:
            The value to assign to the types property of this UnifiedAgentNoneParser.
        :type types: dict(str, str)

        :param null_value_pattern:
            The value to assign to the null_value_pattern property of this UnifiedAgentNoneParser.
        :type null_value_pattern: str

        :param is_null_empty_string:
            The value to assign to the is_null_empty_string property of this UnifiedAgentNoneParser.
        :type is_null_empty_string: bool

        :param is_estimate_current_event:
            The value to assign to the is_estimate_current_event property of this UnifiedAgentNoneParser.
        :type is_estimate_current_event: bool

        :param is_keep_time_key:
            The value to assign to the is_keep_time_key property of this UnifiedAgentNoneParser.
        :type is_keep_time_key: bool

        :param timeout_in_milliseconds:
            The value to assign to the timeout_in_milliseconds property of this UnifiedAgentNoneParser.
        :type timeout_in_milliseconds: int

        :param message_key:
            The value to assign to the message_key property of this UnifiedAgentNoneParser.
        :type message_key: str

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
            'message_key': 'str'
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
            'message_key': 'messageKey'
        }

        self._parser_type = None
        self._field_time_key = None
        self._types = None
        self._null_value_pattern = None
        self._is_null_empty_string = None
        self._is_estimate_current_event = None
        self._is_keep_time_key = None
        self._timeout_in_milliseconds = None
        self._message_key = None
        self._parser_type = 'NONE'

    @property
    def message_key(self):
        """
        Gets the message_key of this UnifiedAgentNoneParser.

        :return: The message_key of this UnifiedAgentNoneParser.
        :rtype: str
        """
        return self._message_key

    @message_key.setter
    def message_key(self, message_key):
        """
        Sets the message_key of this UnifiedAgentNoneParser.

        :param message_key: The message_key of this UnifiedAgentNoneParser.
        :type: str
        """
        self._message_key = message_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
