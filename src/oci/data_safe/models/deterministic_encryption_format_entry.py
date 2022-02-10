# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .format_entry import FormatEntry
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeterministicEncryptionFormatEntry(FormatEntry):
    """
    The Deterministic Encryption masking format encrypts column data using a cryptographic
    key and Advanced Encryption Standard (AES 128). It can be used to encrypt character and
    number columns. It can encrypt ASCII data without any input (except seed value), but it
    needs a regular expression to encrypt non-ASCII data.

    Deterministic Encryption is a format-preserving, deterministic and reversible masking
    format, which requires a seed value while submitting a masking work request. Passing
    the same seed value when masking multiple times or masking different databases ensures
    that the data is masked deterministically. To learn more, check Deterministic Encryption
    in the Data Safe documentation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeterministicEncryptionFormatEntry object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.DeterministicEncryptionFormatEntry.type` attribute
        of this class is ``DETERMINISTIC_ENCRYPTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DeterministicEncryptionFormatEntry.
            Allowed values for this property are: "DELETE_ROWS", "DETERMINISTIC_SUBSTITUTION", "DETERMINISTIC_ENCRYPTION", "DETERMINISTIC_ENCRYPTION_DATE", "FIXED_NUMBER", "FIXED_STRING", "LIBRARY_MASKING_FORMAT", "NULL_VALUE", "POST_PROCESSING_FUNCTION", "PRESERVE_ORIGINAL_DATA", "RANDOM_DATE", "RANDOM_DECIMAL_NUMBER", "RANDOM_DIGITS", "RANDOM_LIST", "RANDOM_NUMBER", "RANDOM_STRING", "RANDOM_SUBSTITUTION", "REGULAR_EXPRESSION", "SHUFFLE", "SQL_EXPRESSION", "SUBSTRING", "TRUNCATE_TABLE", "USER_DEFINED_FUNCTION"
        :type type: str

        :param description:
            The value to assign to the description property of this DeterministicEncryptionFormatEntry.
        :type description: str

        :param regular_expression:
            The value to assign to the regular_expression property of this DeterministicEncryptionFormatEntry.
        :type regular_expression: str

        """
        self.swagger_types = {
            'type': 'str',
            'description': 'str',
            'regular_expression': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'description': 'description',
            'regular_expression': 'regularExpression'
        }

        self._type = None
        self._description = None
        self._regular_expression = None
        self._type = 'DETERMINISTIC_ENCRYPTION'

    @property
    def regular_expression(self):
        """
        Gets the regular_expression of this DeterministicEncryptionFormatEntry.
        The regular expression to be used for masking. For data with characters in the
        ASCII character set, providing a regular expression is optional. However, it
        is required if the data contains multi-byte characters. If not provided, an
        error is returned when a multi-byte character is found.

        In the case of ASCII characters, if a regular expression is not provided,
        Deterministic Encryption can encrypt variable-length column values while
        preserving their original format.

        If a regular expression is provided, the column values in all the rows must match
        the regular expression. Deterministic Encryption supports a subset of the regular
        expression language. It supports encryption of fixed-length strings, and does not
        support * or + syntax of regular expressions. The encrypted values also match the
        regular expression, which helps to ensure that the original format is preserved.
        If an original value does not match the regular expression, Deterministic Encryption
        might not produce a one-to-one mapping. All non-confirming values are mapped to a
        single encrypted value, thereby producing a many-to-one mapping.


        :return: The regular_expression of this DeterministicEncryptionFormatEntry.
        :rtype: str
        """
        return self._regular_expression

    @regular_expression.setter
    def regular_expression(self, regular_expression):
        """
        Sets the regular_expression of this DeterministicEncryptionFormatEntry.
        The regular expression to be used for masking. For data with characters in the
        ASCII character set, providing a regular expression is optional. However, it
        is required if the data contains multi-byte characters. If not provided, an
        error is returned when a multi-byte character is found.

        In the case of ASCII characters, if a regular expression is not provided,
        Deterministic Encryption can encrypt variable-length column values while
        preserving their original format.

        If a regular expression is provided, the column values in all the rows must match
        the regular expression. Deterministic Encryption supports a subset of the regular
        expression language. It supports encryption of fixed-length strings, and does not
        support * or + syntax of regular expressions. The encrypted values also match the
        regular expression, which helps to ensure that the original format is preserved.
        If an original value does not match the regular expression, Deterministic Encryption
        might not produce a one-to-one mapping. All non-confirming values are mapped to a
        single encrypted value, thereby producing a many-to-one mapping.


        :param regular_expression: The regular_expression of this DeterministicEncryptionFormatEntry.
        :type: str
        """
        self._regular_expression = regular_expression

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
