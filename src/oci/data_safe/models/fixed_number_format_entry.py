# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .format_entry import FormatEntry
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FixedNumberFormatEntry(FormatEntry):
    """
    The Fixed Number masking format uses a constant number for masking. To learn more,
    check Fixed Number in the Data Safe documentation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FixedNumberFormatEntry object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.FixedNumberFormatEntry.type` attribute
        of this class is ``FIXED_NUMBER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this FixedNumberFormatEntry.
            Allowed values for this property are: "DELETE_ROWS", "DETERMINISTIC_SUBSTITUTION", "DETERMINISTIC_ENCRYPTION", "DETERMINISTIC_ENCRYPTION_DATE", "FIXED_NUMBER", "FIXED_STRING", "LIBRARY_MASKING_FORMAT", "NULL_VALUE", "POST_PROCESSING_FUNCTION", "PRESERVE_ORIGINAL_DATA", "RANDOM_DATE", "RANDOM_DECIMAL_NUMBER", "RANDOM_DIGITS", "RANDOM_LIST", "RANDOM_NUMBER", "RANDOM_STRING", "RANDOM_SUBSTITUTION", "REGULAR_EXPRESSION", "SHUFFLE", "SQL_EXPRESSION", "SUBSTRING", "TRUNCATE_TABLE", "USER_DEFINED_FUNCTION"
        :type type: str

        :param description:
            The value to assign to the description property of this FixedNumberFormatEntry.
        :type description: str

        :param fixed_number:
            The value to assign to the fixed_number property of this FixedNumberFormatEntry.
        :type fixed_number: float

        """
        self.swagger_types = {
            'type': 'str',
            'description': 'str',
            'fixed_number': 'float'
        }

        self.attribute_map = {
            'type': 'type',
            'description': 'description',
            'fixed_number': 'fixedNumber'
        }

        self._type = None
        self._description = None
        self._fixed_number = None
        self._type = 'FIXED_NUMBER'

    @property
    def fixed_number(self):
        """
        **[Required]** Gets the fixed_number of this FixedNumberFormatEntry.
        The constant number to be used for masking.


        :return: The fixed_number of this FixedNumberFormatEntry.
        :rtype: float
        """
        return self._fixed_number

    @fixed_number.setter
    def fixed_number(self, fixed_number):
        """
        Sets the fixed_number of this FixedNumberFormatEntry.
        The constant number to be used for masking.


        :param fixed_number: The fixed_number of this FixedNumberFormatEntry.
        :type: float
        """
        self._fixed_number = fixed_number

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
