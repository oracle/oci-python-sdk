# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_format_attribute import AbstractFormatAttribute
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CsvFormatAttribute(AbstractFormatAttribute):
    """
    The CSV format attribute.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CsvFormatAttribute object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.CsvFormatAttribute.model_type` attribute
        of this class is ``CSV_FORMAT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CsvFormatAttribute.
            Allowed values for this property are: "JSON_FORMAT", "CSV_FORMAT", "AVRO_FORMAT", "PARQUET_FORMAT"
        :type model_type: str

        :param encoding:
            The value to assign to the encoding property of this CsvFormatAttribute.
        :type encoding: str

        :param escape_character:
            The value to assign to the escape_character property of this CsvFormatAttribute.
        :type escape_character: str

        :param delimiter:
            The value to assign to the delimiter property of this CsvFormatAttribute.
        :type delimiter: str

        :param quote_character:
            The value to assign to the quote_character property of this CsvFormatAttribute.
        :type quote_character: str

        :param has_header:
            The value to assign to the has_header property of this CsvFormatAttribute.
        :type has_header: bool

        :param is_file_pattern:
            The value to assign to the is_file_pattern property of this CsvFormatAttribute.
        :type is_file_pattern: bool

        :param timestamp_format:
            The value to assign to the timestamp_format property of this CsvFormatAttribute.
        :type timestamp_format: str

        :param is_quote_all:
            The value to assign to the is_quote_all property of this CsvFormatAttribute.
        :type is_quote_all: bool

        :param is_multiline:
            The value to assign to the is_multiline property of this CsvFormatAttribute.
        :type is_multiline: bool

        :param is_trailing_delimiter:
            The value to assign to the is_trailing_delimiter property of this CsvFormatAttribute.
        :type is_trailing_delimiter: bool

        """
        self.swagger_types = {
            'model_type': 'str',
            'encoding': 'str',
            'escape_character': 'str',
            'delimiter': 'str',
            'quote_character': 'str',
            'has_header': 'bool',
            'is_file_pattern': 'bool',
            'timestamp_format': 'str',
            'is_quote_all': 'bool',
            'is_multiline': 'bool',
            'is_trailing_delimiter': 'bool'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'encoding': 'encoding',
            'escape_character': 'escapeCharacter',
            'delimiter': 'delimiter',
            'quote_character': 'quoteCharacter',
            'has_header': 'hasHeader',
            'is_file_pattern': 'isFilePattern',
            'timestamp_format': 'timestampFormat',
            'is_quote_all': 'isQuoteAll',
            'is_multiline': 'isMultiline',
            'is_trailing_delimiter': 'isTrailingDelimiter'
        }

        self._model_type = None
        self._encoding = None
        self._escape_character = None
        self._delimiter = None
        self._quote_character = None
        self._has_header = None
        self._is_file_pattern = None
        self._timestamp_format = None
        self._is_quote_all = None
        self._is_multiline = None
        self._is_trailing_delimiter = None
        self._model_type = 'CSV_FORMAT'

    @property
    def encoding(self):
        """
        Gets the encoding of this CsvFormatAttribute.
        The encoding for the file.


        :return: The encoding of this CsvFormatAttribute.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """
        Sets the encoding of this CsvFormatAttribute.
        The encoding for the file.


        :param encoding: The encoding of this CsvFormatAttribute.
        :type: str
        """
        self._encoding = encoding

    @property
    def escape_character(self):
        """
        Gets the escape_character of this CsvFormatAttribute.
        The escape character for the CSV format.


        :return: The escape_character of this CsvFormatAttribute.
        :rtype: str
        """
        return self._escape_character

    @escape_character.setter
    def escape_character(self, escape_character):
        """
        Sets the escape_character of this CsvFormatAttribute.
        The escape character for the CSV format.


        :param escape_character: The escape_character of this CsvFormatAttribute.
        :type: str
        """
        self._escape_character = escape_character

    @property
    def delimiter(self):
        """
        Gets the delimiter of this CsvFormatAttribute.
        The delimiter for the CSV format.


        :return: The delimiter of this CsvFormatAttribute.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """
        Sets the delimiter of this CsvFormatAttribute.
        The delimiter for the CSV format.


        :param delimiter: The delimiter of this CsvFormatAttribute.
        :type: str
        """
        self._delimiter = delimiter

    @property
    def quote_character(self):
        """
        Gets the quote_character of this CsvFormatAttribute.
        The quote character for the CSV format.


        :return: The quote_character of this CsvFormatAttribute.
        :rtype: str
        """
        return self._quote_character

    @quote_character.setter
    def quote_character(self, quote_character):
        """
        Sets the quote_character of this CsvFormatAttribute.
        The quote character for the CSV format.


        :param quote_character: The quote_character of this CsvFormatAttribute.
        :type: str
        """
        self._quote_character = quote_character

    @property
    def has_header(self):
        """
        Gets the has_header of this CsvFormatAttribute.
        Defines whether the file has a header row.


        :return: The has_header of this CsvFormatAttribute.
        :rtype: bool
        """
        return self._has_header

    @has_header.setter
    def has_header(self, has_header):
        """
        Sets the has_header of this CsvFormatAttribute.
        Defines whether the file has a header row.


        :param has_header: The has_header of this CsvFormatAttribute.
        :type: bool
        """
        self._has_header = has_header

    @property
    def is_file_pattern(self):
        """
        Gets the is_file_pattern of this CsvFormatAttribute.
        Defines whether a file pattern is supported.


        :return: The is_file_pattern of this CsvFormatAttribute.
        :rtype: bool
        """
        return self._is_file_pattern

    @is_file_pattern.setter
    def is_file_pattern(self, is_file_pattern):
        """
        Sets the is_file_pattern of this CsvFormatAttribute.
        Defines whether a file pattern is supported.


        :param is_file_pattern: The is_file_pattern of this CsvFormatAttribute.
        :type: bool
        """
        self._is_file_pattern = is_file_pattern

    @property
    def timestamp_format(self):
        """
        Gets the timestamp_format of this CsvFormatAttribute.
        Format for timestamp information.


        :return: The timestamp_format of this CsvFormatAttribute.
        :rtype: str
        """
        return self._timestamp_format

    @timestamp_format.setter
    def timestamp_format(self, timestamp_format):
        """
        Sets the timestamp_format of this CsvFormatAttribute.
        Format for timestamp information.


        :param timestamp_format: The timestamp_format of this CsvFormatAttribute.
        :type: str
        """
        self._timestamp_format = timestamp_format

    @property
    def is_quote_all(self):
        """
        Gets the is_quote_all of this CsvFormatAttribute.
        Defines whether the quote entire content while performing read/write.


        :return: The is_quote_all of this CsvFormatAttribute.
        :rtype: bool
        """
        return self._is_quote_all

    @is_quote_all.setter
    def is_quote_all(self, is_quote_all):
        """
        Sets the is_quote_all of this CsvFormatAttribute.
        Defines whether the quote entire content while performing read/write.


        :param is_quote_all: The is_quote_all of this CsvFormatAttribute.
        :type: bool
        """
        self._is_quote_all = is_quote_all

    @property
    def is_multiline(self):
        """
        Gets the is_multiline of this CsvFormatAttribute.
        Defines whether the file has a multiline content


        :return: The is_multiline of this CsvFormatAttribute.
        :rtype: bool
        """
        return self._is_multiline

    @is_multiline.setter
    def is_multiline(self, is_multiline):
        """
        Sets the is_multiline of this CsvFormatAttribute.
        Defines whether the file has a multiline content


        :param is_multiline: The is_multiline of this CsvFormatAttribute.
        :type: bool
        """
        self._is_multiline = is_multiline

    @property
    def is_trailing_delimiter(self):
        """
        Gets the is_trailing_delimiter of this CsvFormatAttribute.
        Defines whether the file has a trailing delimiter


        :return: The is_trailing_delimiter of this CsvFormatAttribute.
        :rtype: bool
        """
        return self._is_trailing_delimiter

    @is_trailing_delimiter.setter
    def is_trailing_delimiter(self, is_trailing_delimiter):
        """
        Sets the is_trailing_delimiter of this CsvFormatAttribute.
        Defines whether the file has a trailing delimiter


        :param is_trailing_delimiter: The is_trailing_delimiter of this CsvFormatAttribute.
        :type: bool
        """
        self._is_trailing_delimiter = is_trailing_delimiter

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
