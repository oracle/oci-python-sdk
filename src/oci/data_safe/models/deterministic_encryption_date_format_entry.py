# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .format_entry import FormatEntry
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeterministicEncryptionDateFormatEntry(FormatEntry):
    """
    The Deterministic Encryption (Date) masking format encrypts column data using a cryptographic
    key and Advanced Encryption Standard (AES 128). It can be used to encrypt date columns only.
    It requires a range of dates as input defined by the startDate and endDate attributes. The
    start date must be less than or equal to the end date.

    The original column values in all the rows must be within the specified date range. The
    encrypted values are also within the specified range. Therefore, to ensure uniqueness, the
    total number of dates in the range must be greater than or equal to the number of distinct
    original values in the column. If an original value is not in the specified date range, it
    might not produce a one-to-one mapping. All non-confirming values are mapped to a single
    encrypted value, thereby producing a many-to-one mapping.

    Deterministic Encryption (Date) is a format-preserving, deterministic and reversible masking
    format, which requires a seed value while submitting a masking work request. Passing the
    same seed value when masking multiple times or masking different databases ensures that
    the data is masked deterministically. To learn more, check Deterministic Encryption in the
    Data Safe documentation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeterministicEncryptionDateFormatEntry object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.DeterministicEncryptionDateFormatEntry.type` attribute
        of this class is ``DETERMINISTIC_ENCRYPTION_DATE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DeterministicEncryptionDateFormatEntry.
            Allowed values for this property are: "DELETE_ROWS", "DETERMINISTIC_SUBSTITUTION", "DETERMINISTIC_ENCRYPTION", "DETERMINISTIC_ENCRYPTION_DATE", "FIXED_NUMBER", "FIXED_STRING", "LIBRARY_MASKING_FORMAT", "NULL_VALUE", "POST_PROCESSING_FUNCTION", "PRESERVE_ORIGINAL_DATA", "RANDOM_DATE", "RANDOM_DECIMAL_NUMBER", "RANDOM_DIGITS", "RANDOM_LIST", "RANDOM_NUMBER", "RANDOM_STRING", "RANDOM_SUBSTITUTION", "REGULAR_EXPRESSION", "SHUFFLE", "SQL_EXPRESSION", "SUBSTRING", "TRUNCATE_TABLE", "USER_DEFINED_FUNCTION"
        :type type: str

        :param description:
            The value to assign to the description property of this DeterministicEncryptionDateFormatEntry.
        :type description: str

        :param start_date:
            The value to assign to the start_date property of this DeterministicEncryptionDateFormatEntry.
        :type start_date: datetime

        :param end_date:
            The value to assign to the end_date property of this DeterministicEncryptionDateFormatEntry.
        :type end_date: datetime

        """
        self.swagger_types = {
            'type': 'str',
            'description': 'str',
            'start_date': 'datetime',
            'end_date': 'datetime'
        }

        self.attribute_map = {
            'type': 'type',
            'description': 'description',
            'start_date': 'startDate',
            'end_date': 'endDate'
        }

        self._type = None
        self._description = None
        self._start_date = None
        self._end_date = None
        self._type = 'DETERMINISTIC_ENCRYPTION_DATE'

    @property
    def start_date(self):
        """
        **[Required]** Gets the start_date of this DeterministicEncryptionDateFormatEntry.
        The lower bound of the range within which all the original column values fall.
        The start date must be less than or equal to the end date.


        :return: The start_date of this DeterministicEncryptionDateFormatEntry.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this DeterministicEncryptionDateFormatEntry.
        The lower bound of the range within which all the original column values fall.
        The start date must be less than or equal to the end date.


        :param start_date: The start_date of this DeterministicEncryptionDateFormatEntry.
        :type: datetime
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """
        **[Required]** Gets the end_date of this DeterministicEncryptionDateFormatEntry.
        The upper bound of the range within which all the original column values fall.
        The end date must be greater than or equal to the start date.


        :return: The end_date of this DeterministicEncryptionDateFormatEntry.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this DeterministicEncryptionDateFormatEntry.
        The upper bound of the range within which all the original column values fall.
        The end date must be greater than or equal to the start date.


        :param end_date: The end_date of this DeterministicEncryptionDateFormatEntry.
        :type: datetime
        """
        self._end_date = end_date

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
