# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnifiedAgentParser(object):
    """
    source parser object.
    """

    #: A constant which can be used with the parser_type property of a UnifiedAgentParser.
    #: This constant has a value of "AUDITD"
    PARSER_TYPE_AUDITD = "AUDITD"

    #: A constant which can be used with the parser_type property of a UnifiedAgentParser.
    #: This constant has a value of "JSON"
    PARSER_TYPE_JSON = "JSON"

    #: A constant which can be used with the parser_type property of a UnifiedAgentParser.
    #: This constant has a value of "TSV"
    PARSER_TYPE_TSV = "TSV"

    #: A constant which can be used with the parser_type property of a UnifiedAgentParser.
    #: This constant has a value of "CSV"
    PARSER_TYPE_CSV = "CSV"

    #: A constant which can be used with the parser_type property of a UnifiedAgentParser.
    #: This constant has a value of "NONE"
    PARSER_TYPE_NONE = "NONE"

    #: A constant which can be used with the parser_type property of a UnifiedAgentParser.
    #: This constant has a value of "SYSLOG"
    PARSER_TYPE_SYSLOG = "SYSLOG"

    #: A constant which can be used with the parser_type property of a UnifiedAgentParser.
    #: This constant has a value of "APACHE2"
    PARSER_TYPE_APACHE2 = "APACHE2"

    #: A constant which can be used with the parser_type property of a UnifiedAgentParser.
    #: This constant has a value of "APACHE_ERROR"
    PARSER_TYPE_APACHE_ERROR = "APACHE_ERROR"

    #: A constant which can be used with the parser_type property of a UnifiedAgentParser.
    #: This constant has a value of "MSGPACK"
    PARSER_TYPE_MSGPACK = "MSGPACK"

    #: A constant which can be used with the parser_type property of a UnifiedAgentParser.
    #: This constant has a value of "REGEXP"
    PARSER_TYPE_REGEXP = "REGEXP"

    #: A constant which can be used with the parser_type property of a UnifiedAgentParser.
    #: This constant has a value of "MULTILINE"
    PARSER_TYPE_MULTILINE = "MULTILINE"

    #: A constant which can be used with the parser_type property of a UnifiedAgentParser.
    #: This constant has a value of "GROK"
    PARSER_TYPE_GROK = "GROK"

    #: A constant which can be used with the parser_type property of a UnifiedAgentParser.
    #: This constant has a value of "MULTILINE_GROK"
    PARSER_TYPE_MULTILINE_GROK = "MULTILINE_GROK"

    def __init__(self, **kwargs):
        """
        Initializes a new UnifiedAgentParser object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.logging.models.UnifiedAgentMultilineGrokParser`
        * :class:`~oci.logging.models.UnifiedJSONParser`
        * :class:`~oci.logging.models.UnifiedAgentGrokParser`
        * :class:`~oci.logging.models.UnifiedAgentNoneParser`
        * :class:`~oci.logging.models.UnifiedAgentSyslogParser`
        * :class:`~oci.logging.models.UnifiedAgentAuditdParser`
        * :class:`~oci.logging.models.UnifiedAgentApache2Parser`
        * :class:`~oci.logging.models.UnifiedAgentRegexParser`
        * :class:`~oci.logging.models.UnifiedAgentMultilineParser`
        * :class:`~oci.logging.models.UnifiedAgentTsvParser`
        * :class:`~oci.logging.models.UnifiedAgentApacheErrorParser`
        * :class:`~oci.logging.models.UnifiedAgentMsgpackParser`
        * :class:`~oci.logging.models.UnifiedAgentCsvParser`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param parser_type:
            The value to assign to the parser_type property of this UnifiedAgentParser.
            Allowed values for this property are: "AUDITD", "JSON", "TSV", "CSV", "NONE", "SYSLOG", "APACHE2", "APACHE_ERROR", "MSGPACK", "REGEXP", "MULTILINE", "GROK", "MULTILINE_GROK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type parser_type: str

        :param field_time_key:
            The value to assign to the field_time_key property of this UnifiedAgentParser.
        :type field_time_key: str

        :param types:
            The value to assign to the types property of this UnifiedAgentParser.
        :type types: dict(str, str)

        :param null_value_pattern:
            The value to assign to the null_value_pattern property of this UnifiedAgentParser.
        :type null_value_pattern: str

        :param is_null_empty_string:
            The value to assign to the is_null_empty_string property of this UnifiedAgentParser.
        :type is_null_empty_string: bool

        :param is_estimate_current_event:
            The value to assign to the is_estimate_current_event property of this UnifiedAgentParser.
        :type is_estimate_current_event: bool

        :param is_keep_time_key:
            The value to assign to the is_keep_time_key property of this UnifiedAgentParser.
        :type is_keep_time_key: bool

        :param timeout_in_milliseconds:
            The value to assign to the timeout_in_milliseconds property of this UnifiedAgentParser.
        :type timeout_in_milliseconds: int

        """
        self.swagger_types = {
            'parser_type': 'str',
            'field_time_key': 'str',
            'types': 'dict(str, str)',
            'null_value_pattern': 'str',
            'is_null_empty_string': 'bool',
            'is_estimate_current_event': 'bool',
            'is_keep_time_key': 'bool',
            'timeout_in_milliseconds': 'int'
        }

        self.attribute_map = {
            'parser_type': 'parserType',
            'field_time_key': 'fieldTimeKey',
            'types': 'types',
            'null_value_pattern': 'nullValuePattern',
            'is_null_empty_string': 'isNullEmptyString',
            'is_estimate_current_event': 'isEstimateCurrentEvent',
            'is_keep_time_key': 'isKeepTimeKey',
            'timeout_in_milliseconds': 'timeoutInMilliseconds'
        }

        self._parser_type = None
        self._field_time_key = None
        self._types = None
        self._null_value_pattern = None
        self._is_null_empty_string = None
        self._is_estimate_current_event = None
        self._is_keep_time_key = None
        self._timeout_in_milliseconds = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['parserType']

        if type == 'MULTILINE_GROK':
            return 'UnifiedAgentMultilineGrokParser'

        if type == 'JSON':
            return 'UnifiedJSONParser'

        if type == 'GROK':
            return 'UnifiedAgentGrokParser'

        if type == 'NONE':
            return 'UnifiedAgentNoneParser'

        if type == 'SYSLOG':
            return 'UnifiedAgentSyslogParser'

        if type == 'AUDITD':
            return 'UnifiedAgentAuditdParser'

        if type == 'APACHE2':
            return 'UnifiedAgentApache2Parser'

        if type == 'REGEXP':
            return 'UnifiedAgentRegexParser'

        if type == 'MULTILINE':
            return 'UnifiedAgentMultilineParser'

        if type == 'TSV':
            return 'UnifiedAgentTsvParser'

        if type == 'APACHE_ERROR':
            return 'UnifiedAgentApacheErrorParser'

        if type == 'MSGPACK':
            return 'UnifiedAgentMsgpackParser'

        if type == 'CSV':
            return 'UnifiedAgentCsvParser'
        else:
            return 'UnifiedAgentParser'

    @property
    def parser_type(self):
        """
        **[Required]** Gets the parser_type of this UnifiedAgentParser.
        Type of fluent parser.

        Allowed values for this property are: "AUDITD", "JSON", "TSV", "CSV", "NONE", "SYSLOG", "APACHE2", "APACHE_ERROR", "MSGPACK", "REGEXP", "MULTILINE", "GROK", "MULTILINE_GROK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The parser_type of this UnifiedAgentParser.
        :rtype: str
        """
        return self._parser_type

    @parser_type.setter
    def parser_type(self, parser_type):
        """
        Sets the parser_type of this UnifiedAgentParser.
        Type of fluent parser.


        :param parser_type: The parser_type of this UnifiedAgentParser.
        :type: str
        """
        allowed_values = ["AUDITD", "JSON", "TSV", "CSV", "NONE", "SYSLOG", "APACHE2", "APACHE_ERROR", "MSGPACK", "REGEXP", "MULTILINE", "GROK", "MULTILINE_GROK"]
        if not value_allowed_none_or_none_sentinel(parser_type, allowed_values):
            parser_type = 'UNKNOWN_ENUM_VALUE'
        self._parser_type = parser_type

    @property
    def field_time_key(self):
        """
        Gets the field_time_key of this UnifiedAgentParser.
        Specify time field for the event time. If the event doesn't have this field, the current time is used.


        :return: The field_time_key of this UnifiedAgentParser.
        :rtype: str
        """
        return self._field_time_key

    @field_time_key.setter
    def field_time_key(self, field_time_key):
        """
        Sets the field_time_key of this UnifiedAgentParser.
        Specify time field for the event time. If the event doesn't have this field, the current time is used.


        :param field_time_key: The field_time_key of this UnifiedAgentParser.
        :type: str
        """
        self._field_time_key = field_time_key

    @property
    def types(self):
        """
        Gets the types of this UnifiedAgentParser.
        Specify types for converting a field into another type.


        :return: The types of this UnifiedAgentParser.
        :rtype: dict(str, str)
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this UnifiedAgentParser.
        Specify types for converting a field into another type.


        :param types: The types of this UnifiedAgentParser.
        :type: dict(str, str)
        """
        self._types = types

    @property
    def null_value_pattern(self):
        """
        Gets the null_value_pattern of this UnifiedAgentParser.
        Specify the null value pattern.


        :return: The null_value_pattern of this UnifiedAgentParser.
        :rtype: str
        """
        return self._null_value_pattern

    @null_value_pattern.setter
    def null_value_pattern(self, null_value_pattern):
        """
        Sets the null_value_pattern of this UnifiedAgentParser.
        Specify the null value pattern.


        :param null_value_pattern: The null_value_pattern of this UnifiedAgentParser.
        :type: str
        """
        self._null_value_pattern = null_value_pattern

    @property
    def is_null_empty_string(self):
        """
        Gets the is_null_empty_string of this UnifiedAgentParser.
        If true, an empty string field is replaced with nil.


        :return: The is_null_empty_string of this UnifiedAgentParser.
        :rtype: bool
        """
        return self._is_null_empty_string

    @is_null_empty_string.setter
    def is_null_empty_string(self, is_null_empty_string):
        """
        Sets the is_null_empty_string of this UnifiedAgentParser.
        If true, an empty string field is replaced with nil.


        :param is_null_empty_string: The is_null_empty_string of this UnifiedAgentParser.
        :type: bool
        """
        self._is_null_empty_string = is_null_empty_string

    @property
    def is_estimate_current_event(self):
        """
        Gets the is_estimate_current_event of this UnifiedAgentParser.
        If true, use Fluent::EventTime.now(current time) as a timestamp when time_key is specified.


        :return: The is_estimate_current_event of this UnifiedAgentParser.
        :rtype: bool
        """
        return self._is_estimate_current_event

    @is_estimate_current_event.setter
    def is_estimate_current_event(self, is_estimate_current_event):
        """
        Sets the is_estimate_current_event of this UnifiedAgentParser.
        If true, use Fluent::EventTime.now(current time) as a timestamp when time_key is specified.


        :param is_estimate_current_event: The is_estimate_current_event of this UnifiedAgentParser.
        :type: bool
        """
        self._is_estimate_current_event = is_estimate_current_event

    @property
    def is_keep_time_key(self):
        """
        Gets the is_keep_time_key of this UnifiedAgentParser.
        If true, keep time field in the record.


        :return: The is_keep_time_key of this UnifiedAgentParser.
        :rtype: bool
        """
        return self._is_keep_time_key

    @is_keep_time_key.setter
    def is_keep_time_key(self, is_keep_time_key):
        """
        Sets the is_keep_time_key of this UnifiedAgentParser.
        If true, keep time field in the record.


        :param is_keep_time_key: The is_keep_time_key of this UnifiedAgentParser.
        :type: bool
        """
        self._is_keep_time_key = is_keep_time_key

    @property
    def timeout_in_milliseconds(self):
        """
        Gets the timeout_in_milliseconds of this UnifiedAgentParser.
        Specify the timeout for parse processing. This is mainly for detecting an incorrect regexp pattern.


        :return: The timeout_in_milliseconds of this UnifiedAgentParser.
        :rtype: int
        """
        return self._timeout_in_milliseconds

    @timeout_in_milliseconds.setter
    def timeout_in_milliseconds(self, timeout_in_milliseconds):
        """
        Sets the timeout_in_milliseconds of this UnifiedAgentParser.
        Specify the timeout for parse processing. This is mainly for detecting an incorrect regexp pattern.


        :param timeout_in_milliseconds: The timeout_in_milliseconds of this UnifiedAgentParser.
        :type: int
        """
        self._timeout_in_milliseconds = timeout_in_milliseconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
