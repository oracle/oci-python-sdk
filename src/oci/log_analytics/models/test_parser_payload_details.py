# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TestParserPayloadDetails(object):
    """
    TestParserPayloadDetails
    """

    #: A constant which can be used with the type property of a TestParserPayloadDetails.
    #: This constant has a value of "XML"
    TYPE_XML = "XML"

    #: A constant which can be used with the type property of a TestParserPayloadDetails.
    #: This constant has a value of "JSON"
    TYPE_JSON = "JSON"

    #: A constant which can be used with the type property of a TestParserPayloadDetails.
    #: This constant has a value of "REGEX"
    TYPE_REGEX = "REGEX"

    #: A constant which can be used with the type property of a TestParserPayloadDetails.
    #: This constant has a value of "ODL"
    TYPE_ODL = "ODL"

    def __init__(self, **kwargs):
        """
        Initializes a new TestParserPayloadDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param content:
            The value to assign to the content property of this TestParserPayloadDetails.
        :type content: str

        :param description:
            The value to assign to the description property of this TestParserPayloadDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this TestParserPayloadDetails.
        :type display_name: str

        :param encoding:
            The value to assign to the encoding property of this TestParserPayloadDetails.
        :type encoding: str

        :param example_content:
            The value to assign to the example_content property of this TestParserPayloadDetails.
        :type example_content: str

        :param field_maps:
            The value to assign to the field_maps property of this TestParserPayloadDetails.
        :type field_maps: list[LogAnalyticsParserField]

        :param footer_content:
            The value to assign to the footer_content property of this TestParserPayloadDetails.
        :type footer_content: str

        :param header_content:
            The value to assign to the header_content property of this TestParserPayloadDetails.
        :type header_content: str

        :param name:
            The value to assign to the name property of this TestParserPayloadDetails.
        :type name: str

        :param is_default:
            The value to assign to the is_default property of this TestParserPayloadDetails.
        :type is_default: bool

        :param is_single_line_content:
            The value to assign to the is_single_line_content property of this TestParserPayloadDetails.
        :type is_single_line_content: bool

        :param is_system:
            The value to assign to the is_system property of this TestParserPayloadDetails.
        :type is_system: bool

        :param language:
            The value to assign to the language property of this TestParserPayloadDetails.
        :type language: str

        :param time_updated:
            The value to assign to the time_updated property of this TestParserPayloadDetails.
        :type time_updated: datetime

        :param log_type_test_request_version:
            The value to assign to the log_type_test_request_version property of this TestParserPayloadDetails.
        :type log_type_test_request_version: int

        :param metadata:
            The value to assign to the metadata property of this TestParserPayloadDetails.
        :type metadata: UiParserTestMetadata

        :param parser_ignoreline_characters:
            The value to assign to the parser_ignoreline_characters property of this TestParserPayloadDetails.
        :type parser_ignoreline_characters: str

        :param is_hidden:
            The value to assign to the is_hidden property of this TestParserPayloadDetails.
        :type is_hidden: int

        :param parser_sequence:
            The value to assign to the parser_sequence property of this TestParserPayloadDetails.
        :type parser_sequence: int

        :param parser_timezone:
            The value to assign to the parser_timezone property of this TestParserPayloadDetails.
        :type parser_timezone: str

        :param is_parser_written_once:
            The value to assign to the is_parser_written_once property of this TestParserPayloadDetails.
        :type is_parser_written_once: bool

        :param parser_functions:
            The value to assign to the parser_functions property of this TestParserPayloadDetails.
        :type parser_functions: list[LogAnalyticsParserFunction]

        :param should_tokenize_original_text:
            The value to assign to the should_tokenize_original_text property of this TestParserPayloadDetails.
        :type should_tokenize_original_text: bool

        :param type:
            The value to assign to the type property of this TestParserPayloadDetails.
            Allowed values for this property are: "XML", "JSON", "REGEX", "ODL"
        :type type: str

        """
        self.swagger_types = {
            'content': 'str',
            'description': 'str',
            'display_name': 'str',
            'encoding': 'str',
            'example_content': 'str',
            'field_maps': 'list[LogAnalyticsParserField]',
            'footer_content': 'str',
            'header_content': 'str',
            'name': 'str',
            'is_default': 'bool',
            'is_single_line_content': 'bool',
            'is_system': 'bool',
            'language': 'str',
            'time_updated': 'datetime',
            'log_type_test_request_version': 'int',
            'metadata': 'UiParserTestMetadata',
            'parser_ignoreline_characters': 'str',
            'is_hidden': 'int',
            'parser_sequence': 'int',
            'parser_timezone': 'str',
            'is_parser_written_once': 'bool',
            'parser_functions': 'list[LogAnalyticsParserFunction]',
            'should_tokenize_original_text': 'bool',
            'type': 'str'
        }

        self.attribute_map = {
            'content': 'content',
            'description': 'description',
            'display_name': 'displayName',
            'encoding': 'encoding',
            'example_content': 'exampleContent',
            'field_maps': 'fieldMaps',
            'footer_content': 'footerContent',
            'header_content': 'headerContent',
            'name': 'name',
            'is_default': 'isDefault',
            'is_single_line_content': 'isSingleLineContent',
            'is_system': 'isSystem',
            'language': 'language',
            'time_updated': 'timeUpdated',
            'log_type_test_request_version': 'logTypeTestRequestVersion',
            'metadata': 'metadata',
            'parser_ignoreline_characters': 'parserIgnorelineCharacters',
            'is_hidden': 'isHidden',
            'parser_sequence': 'parserSequence',
            'parser_timezone': 'parserTimezone',
            'is_parser_written_once': 'isParserWrittenOnce',
            'parser_functions': 'parserFunctions',
            'should_tokenize_original_text': 'shouldTokenizeOriginalText',
            'type': 'type'
        }

        self._content = None
        self._description = None
        self._display_name = None
        self._encoding = None
        self._example_content = None
        self._field_maps = None
        self._footer_content = None
        self._header_content = None
        self._name = None
        self._is_default = None
        self._is_single_line_content = None
        self._is_system = None
        self._language = None
        self._time_updated = None
        self._log_type_test_request_version = None
        self._metadata = None
        self._parser_ignoreline_characters = None
        self._is_hidden = None
        self._parser_sequence = None
        self._parser_timezone = None
        self._is_parser_written_once = None
        self._parser_functions = None
        self._should_tokenize_original_text = None
        self._type = None

    @property
    def content(self):
        """
        Gets the content of this TestParserPayloadDetails.
        content


        :return: The content of this TestParserPayloadDetails.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this TestParserPayloadDetails.
        content


        :param content: The content of this TestParserPayloadDetails.
        :type: str
        """
        self._content = content

    @property
    def description(self):
        """
        Gets the description of this TestParserPayloadDetails.
        description


        :return: The description of this TestParserPayloadDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TestParserPayloadDetails.
        description


        :param description: The description of this TestParserPayloadDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this TestParserPayloadDetails.
        Display name


        :return: The display_name of this TestParserPayloadDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TestParserPayloadDetails.
        Display name


        :param display_name: The display_name of this TestParserPayloadDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def encoding(self):
        """
        Gets the encoding of this TestParserPayloadDetails.
        encoding


        :return: The encoding of this TestParserPayloadDetails.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """
        Sets the encoding of this TestParserPayloadDetails.
        encoding


        :param encoding: The encoding of this TestParserPayloadDetails.
        :type: str
        """
        self._encoding = encoding

    @property
    def example_content(self):
        """
        Gets the example_content of this TestParserPayloadDetails.
        exampleContent


        :return: The example_content of this TestParserPayloadDetails.
        :rtype: str
        """
        return self._example_content

    @example_content.setter
    def example_content(self, example_content):
        """
        Sets the example_content of this TestParserPayloadDetails.
        exampleContent


        :param example_content: The example_content of this TestParserPayloadDetails.
        :type: str
        """
        self._example_content = example_content

    @property
    def field_maps(self):
        """
        Gets the field_maps of this TestParserPayloadDetails.
        fieldMaps


        :return: The field_maps of this TestParserPayloadDetails.
        :rtype: list[LogAnalyticsParserField]
        """
        return self._field_maps

    @field_maps.setter
    def field_maps(self, field_maps):
        """
        Sets the field_maps of this TestParserPayloadDetails.
        fieldMaps


        :param field_maps: The field_maps of this TestParserPayloadDetails.
        :type: list[LogAnalyticsParserField]
        """
        self._field_maps = field_maps

    @property
    def footer_content(self):
        """
        Gets the footer_content of this TestParserPayloadDetails.
        footerRegex


        :return: The footer_content of this TestParserPayloadDetails.
        :rtype: str
        """
        return self._footer_content

    @footer_content.setter
    def footer_content(self, footer_content):
        """
        Sets the footer_content of this TestParserPayloadDetails.
        footerRegex


        :param footer_content: The footer_content of this TestParserPayloadDetails.
        :type: str
        """
        self._footer_content = footer_content

    @property
    def header_content(self):
        """
        Gets the header_content of this TestParserPayloadDetails.
        headerContent


        :return: The header_content of this TestParserPayloadDetails.
        :rtype: str
        """
        return self._header_content

    @header_content.setter
    def header_content(self, header_content):
        """
        Sets the header_content of this TestParserPayloadDetails.
        headerContent


        :param header_content: The header_content of this TestParserPayloadDetails.
        :type: str
        """
        self._header_content = header_content

    @property
    def name(self):
        """
        Gets the name of this TestParserPayloadDetails.
        name


        :return: The name of this TestParserPayloadDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TestParserPayloadDetails.
        name


        :param name: The name of this TestParserPayloadDetails.
        :type: str
        """
        self._name = name

    @property
    def is_default(self):
        """
        Gets the is_default of this TestParserPayloadDetails.
        isDefault


        :return: The is_default of this TestParserPayloadDetails.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this TestParserPayloadDetails.
        isDefault


        :param is_default: The is_default of this TestParserPayloadDetails.
        :type: bool
        """
        self._is_default = is_default

    @property
    def is_single_line_content(self):
        """
        Gets the is_single_line_content of this TestParserPayloadDetails.
        isSingleLineContent


        :return: The is_single_line_content of this TestParserPayloadDetails.
        :rtype: bool
        """
        return self._is_single_line_content

    @is_single_line_content.setter
    def is_single_line_content(self, is_single_line_content):
        """
        Sets the is_single_line_content of this TestParserPayloadDetails.
        isSingleLineContent


        :param is_single_line_content: The is_single_line_content of this TestParserPayloadDetails.
        :type: bool
        """
        self._is_single_line_content = is_single_line_content

    @property
    def is_system(self):
        """
        Gets the is_system of this TestParserPayloadDetails.
        isSystem


        :return: The is_system of this TestParserPayloadDetails.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this TestParserPayloadDetails.
        isSystem


        :param is_system: The is_system of this TestParserPayloadDetails.
        :type: bool
        """
        self._is_system = is_system

    @property
    def language(self):
        """
        Gets the language of this TestParserPayloadDetails.
        language


        :return: The language of this TestParserPayloadDetails.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this TestParserPayloadDetails.
        language


        :param language: The language of this TestParserPayloadDetails.
        :type: str
        """
        self._language = language

    @property
    def time_updated(self):
        """
        Gets the time_updated of this TestParserPayloadDetails.
        lastUpdatedDate


        :return: The time_updated of this TestParserPayloadDetails.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this TestParserPayloadDetails.
        lastUpdatedDate


        :param time_updated: The time_updated of this TestParserPayloadDetails.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def log_type_test_request_version(self):
        """
        Gets the log_type_test_request_version of this TestParserPayloadDetails.
        logTypeTestRequestVersion


        :return: The log_type_test_request_version of this TestParserPayloadDetails.
        :rtype: int
        """
        return self._log_type_test_request_version

    @log_type_test_request_version.setter
    def log_type_test_request_version(self, log_type_test_request_version):
        """
        Sets the log_type_test_request_version of this TestParserPayloadDetails.
        logTypeTestRequestVersion


        :param log_type_test_request_version: The log_type_test_request_version of this TestParserPayloadDetails.
        :type: int
        """
        self._log_type_test_request_version = log_type_test_request_version

    @property
    def metadata(self):
        """
        Gets the metadata of this TestParserPayloadDetails.

        :return: The metadata of this TestParserPayloadDetails.
        :rtype: UiParserTestMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this TestParserPayloadDetails.

        :param metadata: The metadata of this TestParserPayloadDetails.
        :type: UiParserTestMetadata
        """
        self._metadata = metadata

    @property
    def parser_ignoreline_characters(self):
        """
        Gets the parser_ignoreline_characters of this TestParserPayloadDetails.
        parser ignore linechars


        :return: The parser_ignoreline_characters of this TestParserPayloadDetails.
        :rtype: str
        """
        return self._parser_ignoreline_characters

    @parser_ignoreline_characters.setter
    def parser_ignoreline_characters(self, parser_ignoreline_characters):
        """
        Sets the parser_ignoreline_characters of this TestParserPayloadDetails.
        parser ignore linechars


        :param parser_ignoreline_characters: The parser_ignoreline_characters of this TestParserPayloadDetails.
        :type: str
        """
        self._parser_ignoreline_characters = parser_ignoreline_characters

    @property
    def is_hidden(self):
        """
        Gets the is_hidden of this TestParserPayloadDetails.
        parser is hidden


        :return: The is_hidden of this TestParserPayloadDetails.
        :rtype: int
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """
        Sets the is_hidden of this TestParserPayloadDetails.
        parser is hidden


        :param is_hidden: The is_hidden of this TestParserPayloadDetails.
        :type: int
        """
        self._is_hidden = is_hidden

    @property
    def parser_sequence(self):
        """
        Gets the parser_sequence of this TestParserPayloadDetails.
        parser seq


        :return: The parser_sequence of this TestParserPayloadDetails.
        :rtype: int
        """
        return self._parser_sequence

    @parser_sequence.setter
    def parser_sequence(self, parser_sequence):
        """
        Sets the parser_sequence of this TestParserPayloadDetails.
        parser seq


        :param parser_sequence: The parser_sequence of this TestParserPayloadDetails.
        :type: int
        """
        self._parser_sequence = parser_sequence

    @property
    def parser_timezone(self):
        """
        Gets the parser_timezone of this TestParserPayloadDetails.
        parser timezone


        :return: The parser_timezone of this TestParserPayloadDetails.
        :rtype: str
        """
        return self._parser_timezone

    @parser_timezone.setter
    def parser_timezone(self, parser_timezone):
        """
        Sets the parser_timezone of this TestParserPayloadDetails.
        parser timezone


        :param parser_timezone: The parser_timezone of this TestParserPayloadDetails.
        :type: str
        """
        self._parser_timezone = parser_timezone

    @property
    def is_parser_written_once(self):
        """
        Gets the is_parser_written_once of this TestParserPayloadDetails.
        isParserWrittenOnce


        :return: The is_parser_written_once of this TestParserPayloadDetails.
        :rtype: bool
        """
        return self._is_parser_written_once

    @is_parser_written_once.setter
    def is_parser_written_once(self, is_parser_written_once):
        """
        Sets the is_parser_written_once of this TestParserPayloadDetails.
        isParserWrittenOnce


        :param is_parser_written_once: The is_parser_written_once of this TestParserPayloadDetails.
        :type: bool
        """
        self._is_parser_written_once = is_parser_written_once

    @property
    def parser_functions(self):
        """
        Gets the parser_functions of this TestParserPayloadDetails.
        plugin instance list


        :return: The parser_functions of this TestParserPayloadDetails.
        :rtype: list[LogAnalyticsParserFunction]
        """
        return self._parser_functions

    @parser_functions.setter
    def parser_functions(self, parser_functions):
        """
        Sets the parser_functions of this TestParserPayloadDetails.
        plugin instance list


        :param parser_functions: The parser_functions of this TestParserPayloadDetails.
        :type: list[LogAnalyticsParserFunction]
        """
        self._parser_functions = parser_functions

    @property
    def should_tokenize_original_text(self):
        """
        Gets the should_tokenize_original_text of this TestParserPayloadDetails.
        tokenize original text


        :return: The should_tokenize_original_text of this TestParserPayloadDetails.
        :rtype: bool
        """
        return self._should_tokenize_original_text

    @should_tokenize_original_text.setter
    def should_tokenize_original_text(self, should_tokenize_original_text):
        """
        Sets the should_tokenize_original_text of this TestParserPayloadDetails.
        tokenize original text


        :param should_tokenize_original_text: The should_tokenize_original_text of this TestParserPayloadDetails.
        :type: bool
        """
        self._should_tokenize_original_text = should_tokenize_original_text

    @property
    def type(self):
        """
        Gets the type of this TestParserPayloadDetails.
        type

        Allowed values for this property are: "XML", "JSON", "REGEX", "ODL"


        :return: The type of this TestParserPayloadDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TestParserPayloadDetails.
        type


        :param type: The type of this TestParserPayloadDetails.
        :type: str
        """
        allowed_values = ["XML", "JSON", "REGEX", "ODL"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
