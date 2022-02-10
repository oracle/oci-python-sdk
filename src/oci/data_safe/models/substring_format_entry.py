# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .format_entry import FormatEntry
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubstringFormatEntry(FormatEntry):
    """
    The Substring masking format extracts a portion of the original column
    value and uses it to replace the original value. It internally uses the
    Oracle SUBSTR function. It takes the start position and length as input,
    extracts substring from the original value using SUBSTR, and uses the
    substring to replace the original value. To learn more, check Substring
    in the Data Safe documentation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SubstringFormatEntry object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.SubstringFormatEntry.type` attribute
        of this class is ``SUBSTRING`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this SubstringFormatEntry.
            Allowed values for this property are: "DELETE_ROWS", "DETERMINISTIC_SUBSTITUTION", "DETERMINISTIC_ENCRYPTION", "DETERMINISTIC_ENCRYPTION_DATE", "FIXED_NUMBER", "FIXED_STRING", "LIBRARY_MASKING_FORMAT", "NULL_VALUE", "POST_PROCESSING_FUNCTION", "PRESERVE_ORIGINAL_DATA", "RANDOM_DATE", "RANDOM_DECIMAL_NUMBER", "RANDOM_DIGITS", "RANDOM_LIST", "RANDOM_NUMBER", "RANDOM_STRING", "RANDOM_SUBSTITUTION", "REGULAR_EXPRESSION", "SHUFFLE", "SQL_EXPRESSION", "SUBSTRING", "TRUNCATE_TABLE", "USER_DEFINED_FUNCTION"
        :type type: str

        :param description:
            The value to assign to the description property of this SubstringFormatEntry.
        :type description: str

        :param start_position:
            The value to assign to the start_position property of this SubstringFormatEntry.
        :type start_position: int

        :param length:
            The value to assign to the length property of this SubstringFormatEntry.
        :type length: int

        """
        self.swagger_types = {
            'type': 'str',
            'description': 'str',
            'start_position': 'int',
            'length': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'description': 'description',
            'start_position': 'startPosition',
            'length': 'length'
        }

        self._type = None
        self._description = None
        self._start_position = None
        self._length = None
        self._type = 'SUBSTRING'

    @property
    def start_position(self):
        """
        **[Required]** Gets the start_position of this SubstringFormatEntry.
        The starting position in the original string from where the substring
        should be extracted. It can be either a positive or a negative integer.
        If It's negative, the counting starts from the end of the string.


        :return: The start_position of this SubstringFormatEntry.
        :rtype: int
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        """
        Sets the start_position of this SubstringFormatEntry.
        The starting position in the original string from where the substring
        should be extracted. It can be either a positive or a negative integer.
        If It's negative, the counting starts from the end of the string.


        :param start_position: The start_position of this SubstringFormatEntry.
        :type: int
        """
        self._start_position = start_position

    @property
    def length(self):
        """
        **[Required]** Gets the length of this SubstringFormatEntry.
        The number of characters that should be there in the substring. It should
        be an integer and greater than zero.


        :return: The length of this SubstringFormatEntry.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Sets the length of this SubstringFormatEntry.
        The number of characters that should be there in the substring. It should
        be an integer and greater than zero.


        :param length: The length of this SubstringFormatEntry.
        :type: int
        """
        self._length = length

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
