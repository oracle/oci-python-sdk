# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .format_entry import FormatEntry
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FixedStringFormatEntry(FormatEntry):
    """
    The Fixed String masking format uses a constant string for masking. To learn
    more, check Fixed String in the Data Safe documentation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FixedStringFormatEntry object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.FixedStringFormatEntry.type` attribute
        of this class is ``FIXED_STRING`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this FixedStringFormatEntry.
            Allowed values for this property are: "DELETE_ROWS", "DETERMINISTIC_SUBSTITUTION", "DETERMINISTIC_ENCRYPTION", "DETERMINISTIC_ENCRYPTION_DATE", "FIXED_NUMBER", "FIXED_STRING", "LIBRARY_MASKING_FORMAT", "NULL_VALUE", "POST_PROCESSING_FUNCTION", "PRESERVE_ORIGINAL_DATA", "RANDOM_DATE", "RANDOM_DECIMAL_NUMBER", "RANDOM_DIGITS", "RANDOM_LIST", "RANDOM_NUMBER", "RANDOM_STRING", "RANDOM_SUBSTITUTION", "REGULAR_EXPRESSION", "SHUFFLE", "SQL_EXPRESSION", "SUBSTRING", "TRUNCATE_TABLE", "USER_DEFINED_FUNCTION"
        :type type: str

        :param description:
            The value to assign to the description property of this FixedStringFormatEntry.
        :type description: str

        :param fixed_string:
            The value to assign to the fixed_string property of this FixedStringFormatEntry.
        :type fixed_string: str

        """
        self.swagger_types = {
            'type': 'str',
            'description': 'str',
            'fixed_string': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'description': 'description',
            'fixed_string': 'fixedString'
        }

        self._type = None
        self._description = None
        self._fixed_string = None
        self._type = 'FIXED_STRING'

    @property
    def fixed_string(self):
        """
        **[Required]** Gets the fixed_string of this FixedStringFormatEntry.
        The constant string to be used for masking.


        :return: The fixed_string of this FixedStringFormatEntry.
        :rtype: str
        """
        return self._fixed_string

    @fixed_string.setter
    def fixed_string(self, fixed_string):
        """
        Sets the fixed_string of this FixedStringFormatEntry.
        The constant string to be used for masking.


        :param fixed_string: The fixed_string of this FixedStringFormatEntry.
        :type: str
        """
        self._fixed_string = fixed_string

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
