# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .text_file_type_metadata import TextFileTypeMetadata
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DelimitedFileTypeMetadata(TextFileTypeMetadata):
    """
    Metadata of delimited files.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DelimitedFileTypeMetadata object with values from keyword arguments. The default value of the :py:attr:`~oci.data_labeling_service_dataplane.models.DelimitedFileTypeMetadata.format_type` attribute
        of this class is ``DELIMITED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param format_type:
            The value to assign to the format_type property of this DelimitedFileTypeMetadata.
            Allowed values for this property are: "DELIMITED"
        :type format_type: str

        :param column_name:
            The value to assign to the column_name property of this DelimitedFileTypeMetadata.
        :type column_name: str

        :param column_index:
            The value to assign to the column_index property of this DelimitedFileTypeMetadata.
        :type column_index: int

        :param column_delimiter:
            The value to assign to the column_delimiter property of this DelimitedFileTypeMetadata.
        :type column_delimiter: str

        :param line_delimiter:
            The value to assign to the line_delimiter property of this DelimitedFileTypeMetadata.
        :type line_delimiter: str

        :param escape_character:
            The value to assign to the escape_character property of this DelimitedFileTypeMetadata.
        :type escape_character: str

        """
        self.swagger_types = {
            'format_type': 'str',
            'column_name': 'str',
            'column_index': 'int',
            'column_delimiter': 'str',
            'line_delimiter': 'str',
            'escape_character': 'str'
        }

        self.attribute_map = {
            'format_type': 'formatType',
            'column_name': 'columnName',
            'column_index': 'columnIndex',
            'column_delimiter': 'columnDelimiter',
            'line_delimiter': 'lineDelimiter',
            'escape_character': 'escapeCharacter'
        }

        self._format_type = None
        self._column_name = None
        self._column_index = None
        self._column_delimiter = None
        self._line_delimiter = None
        self._escape_character = None
        self._format_type = 'DELIMITED'

    @property
    def column_name(self):
        """
        Gets the column_name of this DelimitedFileTypeMetadata.
        The name of a selected column.


        :return: The column_name of this DelimitedFileTypeMetadata.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """
        Sets the column_name of this DelimitedFileTypeMetadata.
        The name of a selected column.


        :param column_name: The column_name of this DelimitedFileTypeMetadata.
        :type: str
        """
        self._column_name = column_name

    @property
    def column_index(self):
        """
        **[Required]** Gets the column_index of this DelimitedFileTypeMetadata.
        The index of a selected column. This is a zero-based index.


        :return: The column_index of this DelimitedFileTypeMetadata.
        :rtype: int
        """
        return self._column_index

    @column_index.setter
    def column_index(self, column_index):
        """
        Sets the column_index of this DelimitedFileTypeMetadata.
        The index of a selected column. This is a zero-based index.


        :param column_index: The column_index of this DelimitedFileTypeMetadata.
        :type: int
        """
        self._column_index = column_index

    @property
    def column_delimiter(self):
        """
        Gets the column_delimiter of this DelimitedFileTypeMetadata.
        A column delimiter


        :return: The column_delimiter of this DelimitedFileTypeMetadata.
        :rtype: str
        """
        return self._column_delimiter

    @column_delimiter.setter
    def column_delimiter(self, column_delimiter):
        """
        Sets the column_delimiter of this DelimitedFileTypeMetadata.
        A column delimiter


        :param column_delimiter: The column_delimiter of this DelimitedFileTypeMetadata.
        :type: str
        """
        self._column_delimiter = column_delimiter

    @property
    def line_delimiter(self):
        """
        Gets the line_delimiter of this DelimitedFileTypeMetadata.
        A line delimiter.


        :return: The line_delimiter of this DelimitedFileTypeMetadata.
        :rtype: str
        """
        return self._line_delimiter

    @line_delimiter.setter
    def line_delimiter(self, line_delimiter):
        """
        Sets the line_delimiter of this DelimitedFileTypeMetadata.
        A line delimiter.


        :param line_delimiter: The line_delimiter of this DelimitedFileTypeMetadata.
        :type: str
        """
        self._line_delimiter = line_delimiter

    @property
    def escape_character(self):
        """
        Gets the escape_character of this DelimitedFileTypeMetadata.
        An escape character.


        :return: The escape_character of this DelimitedFileTypeMetadata.
        :rtype: str
        """
        return self._escape_character

    @escape_character.setter
    def escape_character(self, escape_character):
        """
        Sets the escape_character of this DelimitedFileTypeMetadata.
        An escape character.


        :param escape_character: The escape_character of this DelimitedFileTypeMetadata.
        :type: str
        """
        self._escape_character = escape_character

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
