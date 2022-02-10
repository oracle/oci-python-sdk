# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .format_entry import FormatEntry
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RandomStringFormatEntry(FormatEntry):
    """
    The Random String masking format generates random and unique strings of length
    within a range. The length range is defined by the startLength and endLength
    attributes. The start length must be less than or equal to the end length. When
    masking columns with uniqueness constraint, ensure that the length range is
    sufficient enough to generate unique values. To learn more, check Random String
    in the Data Safe documentation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RandomStringFormatEntry object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.RandomStringFormatEntry.type` attribute
        of this class is ``RANDOM_STRING`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this RandomStringFormatEntry.
            Allowed values for this property are: "DELETE_ROWS", "DETERMINISTIC_SUBSTITUTION", "DETERMINISTIC_ENCRYPTION", "DETERMINISTIC_ENCRYPTION_DATE", "FIXED_NUMBER", "FIXED_STRING", "LIBRARY_MASKING_FORMAT", "NULL_VALUE", "POST_PROCESSING_FUNCTION", "PRESERVE_ORIGINAL_DATA", "RANDOM_DATE", "RANDOM_DECIMAL_NUMBER", "RANDOM_DIGITS", "RANDOM_LIST", "RANDOM_NUMBER", "RANDOM_STRING", "RANDOM_SUBSTITUTION", "REGULAR_EXPRESSION", "SHUFFLE", "SQL_EXPRESSION", "SUBSTRING", "TRUNCATE_TABLE", "USER_DEFINED_FUNCTION"
        :type type: str

        :param description:
            The value to assign to the description property of this RandomStringFormatEntry.
        :type description: str

        :param start_length:
            The value to assign to the start_length property of this RandomStringFormatEntry.
        :type start_length: int

        :param end_length:
            The value to assign to the end_length property of this RandomStringFormatEntry.
        :type end_length: int

        """
        self.swagger_types = {
            'type': 'str',
            'description': 'str',
            'start_length': 'int',
            'end_length': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'description': 'description',
            'start_length': 'startLength',
            'end_length': 'endLength'
        }

        self._type = None
        self._description = None
        self._start_length = None
        self._end_length = None
        self._type = 'RANDOM_STRING'

    @property
    def start_length(self):
        """
        **[Required]** Gets the start_length of this RandomStringFormatEntry.
        The minimum number of characters the generated strings should have. It can
        be any integer greater than zero, but it must be less than or equal to the
        end length.


        :return: The start_length of this RandomStringFormatEntry.
        :rtype: int
        """
        return self._start_length

    @start_length.setter
    def start_length(self, start_length):
        """
        Sets the start_length of this RandomStringFormatEntry.
        The minimum number of characters the generated strings should have. It can
        be any integer greater than zero, but it must be less than or equal to the
        end length.


        :param start_length: The start_length of this RandomStringFormatEntry.
        :type: int
        """
        self._start_length = start_length

    @property
    def end_length(self):
        """
        **[Required]** Gets the end_length of this RandomStringFormatEntry.
        The maximum number of characters the generated strings should have. It can
        be any integer greater than zero, but it must be greater than or equal to
        the start length.


        :return: The end_length of this RandomStringFormatEntry.
        :rtype: int
        """
        return self._end_length

    @end_length.setter
    def end_length(self, end_length):
        """
        Sets the end_length of this RandomStringFormatEntry.
        The maximum number of characters the generated strings should have. It can
        be any integer greater than zero, but it must be greater than or equal to
        the start length.


        :param end_length: The end_length of this RandomStringFormatEntry.
        :type: int
        """
        self._end_length = end_length

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
