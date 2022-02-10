# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .format_entry import FormatEntry
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RandomNumberFormatEntry(FormatEntry):
    """
    The Random Number masking format generates random and unique integers within
    a range. The range is defined by the startValue and endValue attributes. The
    start value must be less than or equal to the end value. When masking columns
    with uniqueness constraint, ensure that the range is sufficient enough to
    generate unique values. To learn more, check Random Number in the Data Safe
    documentation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RandomNumberFormatEntry object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.RandomNumberFormatEntry.type` attribute
        of this class is ``RANDOM_NUMBER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this RandomNumberFormatEntry.
            Allowed values for this property are: "DELETE_ROWS", "DETERMINISTIC_SUBSTITUTION", "DETERMINISTIC_ENCRYPTION", "DETERMINISTIC_ENCRYPTION_DATE", "FIXED_NUMBER", "FIXED_STRING", "LIBRARY_MASKING_FORMAT", "NULL_VALUE", "POST_PROCESSING_FUNCTION", "PRESERVE_ORIGINAL_DATA", "RANDOM_DATE", "RANDOM_DECIMAL_NUMBER", "RANDOM_DIGITS", "RANDOM_LIST", "RANDOM_NUMBER", "RANDOM_STRING", "RANDOM_SUBSTITUTION", "REGULAR_EXPRESSION", "SHUFFLE", "SQL_EXPRESSION", "SUBSTRING", "TRUNCATE_TABLE", "USER_DEFINED_FUNCTION"
        :type type: str

        :param description:
            The value to assign to the description property of this RandomNumberFormatEntry.
        :type description: str

        :param start_value:
            The value to assign to the start_value property of this RandomNumberFormatEntry.
        :type start_value: int

        :param end_value:
            The value to assign to the end_value property of this RandomNumberFormatEntry.
        :type end_value: int

        """
        self.swagger_types = {
            'type': 'str',
            'description': 'str',
            'start_value': 'int',
            'end_value': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'description': 'description',
            'start_value': 'startValue',
            'end_value': 'endValue'
        }

        self._type = None
        self._description = None
        self._start_value = None
        self._end_value = None
        self._type = 'RANDOM_NUMBER'

    @property
    def start_value(self):
        """
        **[Required]** Gets the start_value of this RandomNumberFormatEntry.
        The lower bound of the range within which random numbers should be
        generated. It must be less than or equal to the end value. It
        supports input of long type.


        :return: The start_value of this RandomNumberFormatEntry.
        :rtype: int
        """
        return self._start_value

    @start_value.setter
    def start_value(self, start_value):
        """
        Sets the start_value of this RandomNumberFormatEntry.
        The lower bound of the range within which random numbers should be
        generated. It must be less than or equal to the end value. It
        supports input of long type.


        :param start_value: The start_value of this RandomNumberFormatEntry.
        :type: int
        """
        self._start_value = start_value

    @property
    def end_value(self):
        """
        **[Required]** Gets the end_value of this RandomNumberFormatEntry.
        The upper bound of the range within which random numbers should be
        generated. It must be greater than or equal to the start value.
        It supports input of long type.


        :return: The end_value of this RandomNumberFormatEntry.
        :rtype: int
        """
        return self._end_value

    @end_value.setter
    def end_value(self, end_value):
        """
        Sets the end_value of this RandomNumberFormatEntry.
        The upper bound of the range within which random numbers should be
        generated. It must be greater than or equal to the start value.
        It supports input of long type.


        :param end_value: The end_value of this RandomNumberFormatEntry.
        :type: int
        """
        self._end_value = end_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
