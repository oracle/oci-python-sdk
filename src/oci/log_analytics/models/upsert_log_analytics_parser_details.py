# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpsertLogAnalyticsParserDetails(object):
    """
    UpsertLogAnalyticsParserDetails
    """

    #: A constant which can be used with the type property of a UpsertLogAnalyticsParserDetails.
    #: This constant has a value of "XML"
    TYPE_XML = "XML"

    #: A constant which can be used with the type property of a UpsertLogAnalyticsParserDetails.
    #: This constant has a value of "JSON"
    TYPE_JSON = "JSON"

    #: A constant which can be used with the type property of a UpsertLogAnalyticsParserDetails.
    #: This constant has a value of "REGEX"
    TYPE_REGEX = "REGEX"

    #: A constant which can be used with the type property of a UpsertLogAnalyticsParserDetails.
    #: This constant has a value of "ODL"
    TYPE_ODL = "ODL"

    #: A constant which can be used with the type property of a UpsertLogAnalyticsParserDetails.
    #: This constant has a value of "DELIMITED"
    TYPE_DELIMITED = "DELIMITED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpsertLogAnalyticsParserDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param content:
            The value to assign to the content property of this UpsertLogAnalyticsParserDetails.
        :type content: str

        :param description:
            The value to assign to the description property of this UpsertLogAnalyticsParserDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpsertLogAnalyticsParserDetails.
        :type display_name: str

        :param edit_version:
            The value to assign to the edit_version property of this UpsertLogAnalyticsParserDetails.
        :type edit_version: int

        :param encoding:
            The value to assign to the encoding property of this UpsertLogAnalyticsParserDetails.
        :type encoding: str

        :param example_content:
            The value to assign to the example_content property of this UpsertLogAnalyticsParserDetails.
        :type example_content: str

        :param field_maps:
            The value to assign to the field_maps property of this UpsertLogAnalyticsParserDetails.
        :type field_maps: list[oci.log_analytics.models.LogAnalyticsParserField]

        :param footer_content:
            The value to assign to the footer_content property of this UpsertLogAnalyticsParserDetails.
        :type footer_content: str

        :param header_content:
            The value to assign to the header_content property of this UpsertLogAnalyticsParserDetails.
        :type header_content: str

        :param name:
            The value to assign to the name property of this UpsertLogAnalyticsParserDetails.
        :type name: str

        :param is_default:
            The value to assign to the is_default property of this UpsertLogAnalyticsParserDetails.
        :type is_default: bool

        :param is_single_line_content:
            The value to assign to the is_single_line_content property of this UpsertLogAnalyticsParserDetails.
        :type is_single_line_content: bool

        :param is_system:
            The value to assign to the is_system property of this UpsertLogAnalyticsParserDetails.
        :type is_system: bool

        :param language:
            The value to assign to the language property of this UpsertLogAnalyticsParserDetails.
        :type language: str

        :param log_type_test_request_version:
            The value to assign to the log_type_test_request_version property of this UpsertLogAnalyticsParserDetails.
        :type log_type_test_request_version: int

        :param parser_ignoreline_characters:
            The value to assign to the parser_ignoreline_characters property of this UpsertLogAnalyticsParserDetails.
        :type parser_ignoreline_characters: str

        :param parser_sequence:
            The value to assign to the parser_sequence property of this UpsertLogAnalyticsParserDetails.
        :type parser_sequence: int

        :param parser_timezone:
            The value to assign to the parser_timezone property of this UpsertLogAnalyticsParserDetails.
        :type parser_timezone: str

        :param is_parser_written_once:
            The value to assign to the is_parser_written_once property of this UpsertLogAnalyticsParserDetails.
        :type is_parser_written_once: bool

        :param parser_functions:
            The value to assign to the parser_functions property of this UpsertLogAnalyticsParserDetails.
        :type parser_functions: list[oci.log_analytics.models.LogAnalyticsParserFunction]

        :param should_tokenize_original_text:
            The value to assign to the should_tokenize_original_text property of this UpsertLogAnalyticsParserDetails.
        :type should_tokenize_original_text: bool

        :param field_delimiter:
            The value to assign to the field_delimiter property of this UpsertLogAnalyticsParserDetails.
        :type field_delimiter: str

        :param field_qualifier:
            The value to assign to the field_qualifier property of this UpsertLogAnalyticsParserDetails.
        :type field_qualifier: str

        :param type:
            The value to assign to the type property of this UpsertLogAnalyticsParserDetails.
            Allowed values for this property are: "XML", "JSON", "REGEX", "ODL", "DELIMITED"
        :type type: str

        :param is_namespace_aware:
            The value to assign to the is_namespace_aware property of this UpsertLogAnalyticsParserDetails.
        :type is_namespace_aware: bool

        :param categories:
            The value to assign to the categories property of this UpsertLogAnalyticsParserDetails.
        :type categories: list[oci.log_analytics.models.LogAnalyticsCategory]

        """
        self.swagger_types = {
            'content': 'str',
            'description': 'str',
            'display_name': 'str',
            'edit_version': 'int',
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
            'log_type_test_request_version': 'int',
            'parser_ignoreline_characters': 'str',
            'parser_sequence': 'int',
            'parser_timezone': 'str',
            'is_parser_written_once': 'bool',
            'parser_functions': 'list[LogAnalyticsParserFunction]',
            'should_tokenize_original_text': 'bool',
            'field_delimiter': 'str',
            'field_qualifier': 'str',
            'type': 'str',
            'is_namespace_aware': 'bool',
            'categories': 'list[LogAnalyticsCategory]'
        }

        self.attribute_map = {
            'content': 'content',
            'description': 'description',
            'display_name': 'displayName',
            'edit_version': 'editVersion',
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
            'log_type_test_request_version': 'logTypeTestRequestVersion',
            'parser_ignoreline_characters': 'parserIgnorelineCharacters',
            'parser_sequence': 'parserSequence',
            'parser_timezone': 'parserTimezone',
            'is_parser_written_once': 'isParserWrittenOnce',
            'parser_functions': 'parserFunctions',
            'should_tokenize_original_text': 'shouldTokenizeOriginalText',
            'field_delimiter': 'fieldDelimiter',
            'field_qualifier': 'fieldQualifier',
            'type': 'type',
            'is_namespace_aware': 'isNamespaceAware',
            'categories': 'categories'
        }

        self._content = None
        self._description = None
        self._display_name = None
        self._edit_version = None
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
        self._log_type_test_request_version = None
        self._parser_ignoreline_characters = None
        self._parser_sequence = None
        self._parser_timezone = None
        self._is_parser_written_once = None
        self._parser_functions = None
        self._should_tokenize_original_text = None
        self._field_delimiter = None
        self._field_qualifier = None
        self._type = None
        self._is_namespace_aware = None
        self._categories = None

    @property
    def content(self):
        """
        Gets the content of this UpsertLogAnalyticsParserDetails.
        The content.


        :return: The content of this UpsertLogAnalyticsParserDetails.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this UpsertLogAnalyticsParserDetails.
        The content.


        :param content: The content of this UpsertLogAnalyticsParserDetails.
        :type: str
        """
        self._content = content

    @property
    def description(self):
        """
        Gets the description of this UpsertLogAnalyticsParserDetails.
        The parser description.


        :return: The description of this UpsertLogAnalyticsParserDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpsertLogAnalyticsParserDetails.
        The parser description.


        :param description: The description of this UpsertLogAnalyticsParserDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this UpsertLogAnalyticsParserDetails.
        The parser display name.


        :return: The display_name of this UpsertLogAnalyticsParserDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpsertLogAnalyticsParserDetails.
        The parser display name.


        :param display_name: The display_name of this UpsertLogAnalyticsParserDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def edit_version(self):
        """
        Gets the edit_version of this UpsertLogAnalyticsParserDetails.
        The parser edit version.


        :return: The edit_version of this UpsertLogAnalyticsParserDetails.
        :rtype: int
        """
        return self._edit_version

    @edit_version.setter
    def edit_version(self, edit_version):
        """
        Sets the edit_version of this UpsertLogAnalyticsParserDetails.
        The parser edit version.


        :param edit_version: The edit_version of this UpsertLogAnalyticsParserDetails.
        :type: int
        """
        self._edit_version = edit_version

    @property
    def encoding(self):
        """
        Gets the encoding of this UpsertLogAnalyticsParserDetails.
        The encoding.


        :return: The encoding of this UpsertLogAnalyticsParserDetails.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """
        Sets the encoding of this UpsertLogAnalyticsParserDetails.
        The encoding.


        :param encoding: The encoding of this UpsertLogAnalyticsParserDetails.
        :type: str
        """
        self._encoding = encoding

    @property
    def example_content(self):
        """
        Gets the example_content of this UpsertLogAnalyticsParserDetails.
        Example content.


        :return: The example_content of this UpsertLogAnalyticsParserDetails.
        :rtype: str
        """
        return self._example_content

    @example_content.setter
    def example_content(self, example_content):
        """
        Sets the example_content of this UpsertLogAnalyticsParserDetails.
        Example content.


        :param example_content: The example_content of this UpsertLogAnalyticsParserDetails.
        :type: str
        """
        self._example_content = example_content

    @property
    def field_maps(self):
        """
        Gets the field_maps of this UpsertLogAnalyticsParserDetails.
        The parser fields.


        :return: The field_maps of this UpsertLogAnalyticsParserDetails.
        :rtype: list[oci.log_analytics.models.LogAnalyticsParserField]
        """
        return self._field_maps

    @field_maps.setter
    def field_maps(self, field_maps):
        """
        Sets the field_maps of this UpsertLogAnalyticsParserDetails.
        The parser fields.


        :param field_maps: The field_maps of this UpsertLogAnalyticsParserDetails.
        :type: list[oci.log_analytics.models.LogAnalyticsParserField]
        """
        self._field_maps = field_maps

    @property
    def footer_content(self):
        """
        Gets the footer_content of this UpsertLogAnalyticsParserDetails.
        The footer regular expression.


        :return: The footer_content of this UpsertLogAnalyticsParserDetails.
        :rtype: str
        """
        return self._footer_content

    @footer_content.setter
    def footer_content(self, footer_content):
        """
        Sets the footer_content of this UpsertLogAnalyticsParserDetails.
        The footer regular expression.


        :param footer_content: The footer_content of this UpsertLogAnalyticsParserDetails.
        :type: str
        """
        self._footer_content = footer_content

    @property
    def header_content(self):
        """
        Gets the header_content of this UpsertLogAnalyticsParserDetails.
        The header content.


        :return: The header_content of this UpsertLogAnalyticsParserDetails.
        :rtype: str
        """
        return self._header_content

    @header_content.setter
    def header_content(self, header_content):
        """
        Sets the header_content of this UpsertLogAnalyticsParserDetails.
        The header content.


        :param header_content: The header_content of this UpsertLogAnalyticsParserDetails.
        :type: str
        """
        self._header_content = header_content

    @property
    def name(self):
        """
        Gets the name of this UpsertLogAnalyticsParserDetails.
        The parser internal name.


        :return: The name of this UpsertLogAnalyticsParserDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpsertLogAnalyticsParserDetails.
        The parser internal name.


        :param name: The name of this UpsertLogAnalyticsParserDetails.
        :type: str
        """
        self._name = name

    @property
    def is_default(self):
        """
        Gets the is_default of this UpsertLogAnalyticsParserDetails.
        A flag indicating if this is a default parser.


        :return: The is_default of this UpsertLogAnalyticsParserDetails.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this UpsertLogAnalyticsParserDetails.
        A flag indicating if this is a default parser.


        :param is_default: The is_default of this UpsertLogAnalyticsParserDetails.
        :type: bool
        """
        self._is_default = is_default

    @property
    def is_single_line_content(self):
        """
        Gets the is_single_line_content of this UpsertLogAnalyticsParserDetails.
        A flag indicating if this is a single line content parser.


        :return: The is_single_line_content of this UpsertLogAnalyticsParserDetails.
        :rtype: bool
        """
        return self._is_single_line_content

    @is_single_line_content.setter
    def is_single_line_content(self, is_single_line_content):
        """
        Sets the is_single_line_content of this UpsertLogAnalyticsParserDetails.
        A flag indicating if this is a single line content parser.


        :param is_single_line_content: The is_single_line_content of this UpsertLogAnalyticsParserDetails.
        :type: bool
        """
        self._is_single_line_content = is_single_line_content

    @property
    def is_system(self):
        """
        Gets the is_system of this UpsertLogAnalyticsParserDetails.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :return: The is_system of this UpsertLogAnalyticsParserDetails.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this UpsertLogAnalyticsParserDetails.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :param is_system: The is_system of this UpsertLogAnalyticsParserDetails.
        :type: bool
        """
        self._is_system = is_system

    @property
    def language(self):
        """
        Gets the language of this UpsertLogAnalyticsParserDetails.
        The language.


        :return: The language of this UpsertLogAnalyticsParserDetails.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this UpsertLogAnalyticsParserDetails.
        The language.


        :param language: The language of this UpsertLogAnalyticsParserDetails.
        :type: str
        """
        self._language = language

    @property
    def log_type_test_request_version(self):
        """
        Gets the log_type_test_request_version of this UpsertLogAnalyticsParserDetails.
        The log type test request version.


        :return: The log_type_test_request_version of this UpsertLogAnalyticsParserDetails.
        :rtype: int
        """
        return self._log_type_test_request_version

    @log_type_test_request_version.setter
    def log_type_test_request_version(self, log_type_test_request_version):
        """
        Sets the log_type_test_request_version of this UpsertLogAnalyticsParserDetails.
        The log type test request version.


        :param log_type_test_request_version: The log_type_test_request_version of this UpsertLogAnalyticsParserDetails.
        :type: int
        """
        self._log_type_test_request_version = log_type_test_request_version

    @property
    def parser_ignoreline_characters(self):
        """
        Gets the parser_ignoreline_characters of this UpsertLogAnalyticsParserDetails.
        The line characters for the parser to ignore.


        :return: The parser_ignoreline_characters of this UpsertLogAnalyticsParserDetails.
        :rtype: str
        """
        return self._parser_ignoreline_characters

    @parser_ignoreline_characters.setter
    def parser_ignoreline_characters(self, parser_ignoreline_characters):
        """
        Sets the parser_ignoreline_characters of this UpsertLogAnalyticsParserDetails.
        The line characters for the parser to ignore.


        :param parser_ignoreline_characters: The parser_ignoreline_characters of this UpsertLogAnalyticsParserDetails.
        :type: str
        """
        self._parser_ignoreline_characters = parser_ignoreline_characters

    @property
    def parser_sequence(self):
        """
        Gets the parser_sequence of this UpsertLogAnalyticsParserDetails.
        The parser sequence.


        :return: The parser_sequence of this UpsertLogAnalyticsParserDetails.
        :rtype: int
        """
        return self._parser_sequence

    @parser_sequence.setter
    def parser_sequence(self, parser_sequence):
        """
        Sets the parser_sequence of this UpsertLogAnalyticsParserDetails.
        The parser sequence.


        :param parser_sequence: The parser_sequence of this UpsertLogAnalyticsParserDetails.
        :type: int
        """
        self._parser_sequence = parser_sequence

    @property
    def parser_timezone(self):
        """
        Gets the parser_timezone of this UpsertLogAnalyticsParserDetails.
        The time zone.


        :return: The parser_timezone of this UpsertLogAnalyticsParserDetails.
        :rtype: str
        """
        return self._parser_timezone

    @parser_timezone.setter
    def parser_timezone(self, parser_timezone):
        """
        Sets the parser_timezone of this UpsertLogAnalyticsParserDetails.
        The time zone.


        :param parser_timezone: The parser_timezone of this UpsertLogAnalyticsParserDetails.
        :type: str
        """
        self._parser_timezone = parser_timezone

    @property
    def is_parser_written_once(self):
        """
        Gets the is_parser_written_once of this UpsertLogAnalyticsParserDetails.
        A flag indicating whther or not the parser is write once.


        :return: The is_parser_written_once of this UpsertLogAnalyticsParserDetails.
        :rtype: bool
        """
        return self._is_parser_written_once

    @is_parser_written_once.setter
    def is_parser_written_once(self, is_parser_written_once):
        """
        Sets the is_parser_written_once of this UpsertLogAnalyticsParserDetails.
        A flag indicating whther or not the parser is write once.


        :param is_parser_written_once: The is_parser_written_once of this UpsertLogAnalyticsParserDetails.
        :type: bool
        """
        self._is_parser_written_once = is_parser_written_once

    @property
    def parser_functions(self):
        """
        Gets the parser_functions of this UpsertLogAnalyticsParserDetails.
        The parser function list.


        :return: The parser_functions of this UpsertLogAnalyticsParserDetails.
        :rtype: list[oci.log_analytics.models.LogAnalyticsParserFunction]
        """
        return self._parser_functions

    @parser_functions.setter
    def parser_functions(self, parser_functions):
        """
        Sets the parser_functions of this UpsertLogAnalyticsParserDetails.
        The parser function list.


        :param parser_functions: The parser_functions of this UpsertLogAnalyticsParserDetails.
        :type: list[oci.log_analytics.models.LogAnalyticsParserFunction]
        """
        self._parser_functions = parser_functions

    @property
    def should_tokenize_original_text(self):
        """
        Gets the should_tokenize_original_text of this UpsertLogAnalyticsParserDetails.
        A flag indicating whether or not to tokenize the original text.


        :return: The should_tokenize_original_text of this UpsertLogAnalyticsParserDetails.
        :rtype: bool
        """
        return self._should_tokenize_original_text

    @should_tokenize_original_text.setter
    def should_tokenize_original_text(self, should_tokenize_original_text):
        """
        Sets the should_tokenize_original_text of this UpsertLogAnalyticsParserDetails.
        A flag indicating whether or not to tokenize the original text.


        :param should_tokenize_original_text: The should_tokenize_original_text of this UpsertLogAnalyticsParserDetails.
        :type: bool
        """
        self._should_tokenize_original_text = should_tokenize_original_text

    @property
    def field_delimiter(self):
        """
        Gets the field_delimiter of this UpsertLogAnalyticsParserDetails.
        The parser field delimiter.


        :return: The field_delimiter of this UpsertLogAnalyticsParserDetails.
        :rtype: str
        """
        return self._field_delimiter

    @field_delimiter.setter
    def field_delimiter(self, field_delimiter):
        """
        Sets the field_delimiter of this UpsertLogAnalyticsParserDetails.
        The parser field delimiter.


        :param field_delimiter: The field_delimiter of this UpsertLogAnalyticsParserDetails.
        :type: str
        """
        self._field_delimiter = field_delimiter

    @property
    def field_qualifier(self):
        """
        Gets the field_qualifier of this UpsertLogAnalyticsParserDetails.
        The parser field qualifier.


        :return: The field_qualifier of this UpsertLogAnalyticsParserDetails.
        :rtype: str
        """
        return self._field_qualifier

    @field_qualifier.setter
    def field_qualifier(self, field_qualifier):
        """
        Sets the field_qualifier of this UpsertLogAnalyticsParserDetails.
        The parser field qualifier.


        :param field_qualifier: The field_qualifier of this UpsertLogAnalyticsParserDetails.
        :type: str
        """
        self._field_qualifier = field_qualifier

    @property
    def type(self):
        """
        Gets the type of this UpsertLogAnalyticsParserDetails.
        The parser type.  Default value is REGEX.

        Allowed values for this property are: "XML", "JSON", "REGEX", "ODL", "DELIMITED"


        :return: The type of this UpsertLogAnalyticsParserDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UpsertLogAnalyticsParserDetails.
        The parser type.  Default value is REGEX.


        :param type: The type of this UpsertLogAnalyticsParserDetails.
        :type: str
        """
        allowed_values = ["XML", "JSON", "REGEX", "ODL", "DELIMITED"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def is_namespace_aware(self):
        """
        Gets the is_namespace_aware of this UpsertLogAnalyticsParserDetails.
        A flag indicating whether the XML parser should consider the namespace(s) while processing the log data.


        :return: The is_namespace_aware of this UpsertLogAnalyticsParserDetails.
        :rtype: bool
        """
        return self._is_namespace_aware

    @is_namespace_aware.setter
    def is_namespace_aware(self, is_namespace_aware):
        """
        Sets the is_namespace_aware of this UpsertLogAnalyticsParserDetails.
        A flag indicating whether the XML parser should consider the namespace(s) while processing the log data.


        :param is_namespace_aware: The is_namespace_aware of this UpsertLogAnalyticsParserDetails.
        :type: bool
        """
        self._is_namespace_aware = is_namespace_aware

    @property
    def categories(self):
        """
        Gets the categories of this UpsertLogAnalyticsParserDetails.
        An array of categories to assign to the parser. Specifying the name attribute for each category would suffice.
        Oracle-defined category assignments cannot be removed.


        :return: The categories of this UpsertLogAnalyticsParserDetails.
        :rtype: list[oci.log_analytics.models.LogAnalyticsCategory]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this UpsertLogAnalyticsParserDetails.
        An array of categories to assign to the parser. Specifying the name attribute for each category would suffice.
        Oracle-defined category assignments cannot be removed.


        :param categories: The categories of this UpsertLogAnalyticsParserDetails.
        :type: list[oci.log_analytics.models.LogAnalyticsCategory]
        """
        self._categories = categories

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
