# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FormatEntry(object):
    """
    A format entry is part of a masking format and defines the logic to mask data. A format
    entry can be a basic masking format such as Random Number, or it can be a library masking
    format. If a masking format has more than one format entries, the combined output of all
    the format entries is used for masking.
    """

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "DELETE_ROWS"
    TYPE_DELETE_ROWS = "DELETE_ROWS"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "DETERMINISTIC_SUBSTITUTION"
    TYPE_DETERMINISTIC_SUBSTITUTION = "DETERMINISTIC_SUBSTITUTION"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "DETERMINISTIC_ENCRYPTION"
    TYPE_DETERMINISTIC_ENCRYPTION = "DETERMINISTIC_ENCRYPTION"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "DETERMINISTIC_ENCRYPTION_DATE"
    TYPE_DETERMINISTIC_ENCRYPTION_DATE = "DETERMINISTIC_ENCRYPTION_DATE"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "FIXED_NUMBER"
    TYPE_FIXED_NUMBER = "FIXED_NUMBER"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "FIXED_STRING"
    TYPE_FIXED_STRING = "FIXED_STRING"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "LIBRARY_MASKING_FORMAT"
    TYPE_LIBRARY_MASKING_FORMAT = "LIBRARY_MASKING_FORMAT"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "NULL_VALUE"
    TYPE_NULL_VALUE = "NULL_VALUE"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "POST_PROCESSING_FUNCTION"
    TYPE_POST_PROCESSING_FUNCTION = "POST_PROCESSING_FUNCTION"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "PRESERVE_ORIGINAL_DATA"
    TYPE_PRESERVE_ORIGINAL_DATA = "PRESERVE_ORIGINAL_DATA"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "RANDOM_DATE"
    TYPE_RANDOM_DATE = "RANDOM_DATE"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "RANDOM_DECIMAL_NUMBER"
    TYPE_RANDOM_DECIMAL_NUMBER = "RANDOM_DECIMAL_NUMBER"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "RANDOM_DIGITS"
    TYPE_RANDOM_DIGITS = "RANDOM_DIGITS"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "RANDOM_LIST"
    TYPE_RANDOM_LIST = "RANDOM_LIST"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "RANDOM_NUMBER"
    TYPE_RANDOM_NUMBER = "RANDOM_NUMBER"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "RANDOM_STRING"
    TYPE_RANDOM_STRING = "RANDOM_STRING"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "RANDOM_SUBSTITUTION"
    TYPE_RANDOM_SUBSTITUTION = "RANDOM_SUBSTITUTION"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "REGULAR_EXPRESSION"
    TYPE_REGULAR_EXPRESSION = "REGULAR_EXPRESSION"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "SHUFFLE"
    TYPE_SHUFFLE = "SHUFFLE"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "SQL_EXPRESSION"
    TYPE_SQL_EXPRESSION = "SQL_EXPRESSION"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "SUBSTRING"
    TYPE_SUBSTRING = "SUBSTRING"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "TRUNCATE_TABLE"
    TYPE_TRUNCATE_TABLE = "TRUNCATE_TABLE"

    #: A constant which can be used with the type property of a FormatEntry.
    #: This constant has a value of "USER_DEFINED_FUNCTION"
    TYPE_USER_DEFINED_FUNCTION = "USER_DEFINED_FUNCTION"

    def __init__(self, **kwargs):
        """
        Initializes a new FormatEntry object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_safe.models.RandomStringFormatEntry`
        * :class:`~oci.data_safe.models.DeterministicSubstitutionFormatEntry`
        * :class:`~oci.data_safe.models.DeterministicEncryptionFormatEntry`
        * :class:`~oci.data_safe.models.RandomDecimalNumberFormatEntry`
        * :class:`~oci.data_safe.models.RandomSubstitutionFormatEntry`
        * :class:`~oci.data_safe.models.PPFFormatEntry`
        * :class:`~oci.data_safe.models.NullValueFormatEntry`
        * :class:`~oci.data_safe.models.FixedNumberFormatEntry`
        * :class:`~oci.data_safe.models.RegularExpressionFormatEntry`
        * :class:`~oci.data_safe.models.UDFFormatEntry`
        * :class:`~oci.data_safe.models.ShuffleFormatEntry`
        * :class:`~oci.data_safe.models.FixedStringFormatEntry`
        * :class:`~oci.data_safe.models.TruncateTableFormatEntry`
        * :class:`~oci.data_safe.models.LibraryMaskingFormatEntry`
        * :class:`~oci.data_safe.models.SQLExpressionFormatEntry`
        * :class:`~oci.data_safe.models.DeterministicEncryptionDateFormatEntry`
        * :class:`~oci.data_safe.models.RandomDigitsFormatEntry`
        * :class:`~oci.data_safe.models.DeleteRowsFormatEntry`
        * :class:`~oci.data_safe.models.SubstringFormatEntry`
        * :class:`~oci.data_safe.models.RandomNumberFormatEntry`
        * :class:`~oci.data_safe.models.PreserveOriginalDataFormatEntry`
        * :class:`~oci.data_safe.models.RandomDateFormatEntry`
        * :class:`~oci.data_safe.models.RandomListFormatEntry`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this FormatEntry.
            Allowed values for this property are: "DELETE_ROWS", "DETERMINISTIC_SUBSTITUTION", "DETERMINISTIC_ENCRYPTION", "DETERMINISTIC_ENCRYPTION_DATE", "FIXED_NUMBER", "FIXED_STRING", "LIBRARY_MASKING_FORMAT", "NULL_VALUE", "POST_PROCESSING_FUNCTION", "PRESERVE_ORIGINAL_DATA", "RANDOM_DATE", "RANDOM_DECIMAL_NUMBER", "RANDOM_DIGITS", "RANDOM_LIST", "RANDOM_NUMBER", "RANDOM_STRING", "RANDOM_SUBSTITUTION", "REGULAR_EXPRESSION", "SHUFFLE", "SQL_EXPRESSION", "SUBSTRING", "TRUNCATE_TABLE", "USER_DEFINED_FUNCTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param description:
            The value to assign to the description property of this FormatEntry.
        :type description: str

        """
        self.swagger_types = {
            'type': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'description': 'description'
        }

        self._type = None
        self._description = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'RANDOM_STRING':
            return 'RandomStringFormatEntry'

        if type == 'DETERMINISTIC_SUBSTITUTION':
            return 'DeterministicSubstitutionFormatEntry'

        if type == 'DETERMINISTIC_ENCRYPTION':
            return 'DeterministicEncryptionFormatEntry'

        if type == 'RANDOM_DECIMAL_NUMBER':
            return 'RandomDecimalNumberFormatEntry'

        if type == 'RANDOM_SUBSTITUTION':
            return 'RandomSubstitutionFormatEntry'

        if type == 'POST_PROCESSING_FUNCTION':
            return 'PPFFormatEntry'

        if type == 'NULL_VALUE':
            return 'NullValueFormatEntry'

        if type == 'FIXED_NUMBER':
            return 'FixedNumberFormatEntry'

        if type == 'REGULAR_EXPRESSION':
            return 'RegularExpressionFormatEntry'

        if type == 'USER_DEFINED_FUNCTION':
            return 'UDFFormatEntry'

        if type == 'SHUFFLE':
            return 'ShuffleFormatEntry'

        if type == 'FIXED_STRING':
            return 'FixedStringFormatEntry'

        if type == 'TRUNCATE_TABLE':
            return 'TruncateTableFormatEntry'

        if type == 'LIBRARY_MASKING_FORMAT':
            return 'LibraryMaskingFormatEntry'

        if type == 'SQL_EXPRESSION':
            return 'SQLExpressionFormatEntry'

        if type == 'DETERMINISTIC_ENCRYPTION_DATE':
            return 'DeterministicEncryptionDateFormatEntry'

        if type == 'RANDOM_DIGITS':
            return 'RandomDigitsFormatEntry'

        if type == 'DELETE_ROWS':
            return 'DeleteRowsFormatEntry'

        if type == 'SUBSTRING':
            return 'SubstringFormatEntry'

        if type == 'RANDOM_NUMBER':
            return 'RandomNumberFormatEntry'

        if type == 'PRESERVE_ORIGINAL_DATA':
            return 'PreserveOriginalDataFormatEntry'

        if type == 'RANDOM_DATE':
            return 'RandomDateFormatEntry'

        if type == 'RANDOM_LIST':
            return 'RandomListFormatEntry'
        else:
            return 'FormatEntry'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this FormatEntry.
        The type of the format entry.

        Allowed values for this property are: "DELETE_ROWS", "DETERMINISTIC_SUBSTITUTION", "DETERMINISTIC_ENCRYPTION", "DETERMINISTIC_ENCRYPTION_DATE", "FIXED_NUMBER", "FIXED_STRING", "LIBRARY_MASKING_FORMAT", "NULL_VALUE", "POST_PROCESSING_FUNCTION", "PRESERVE_ORIGINAL_DATA", "RANDOM_DATE", "RANDOM_DECIMAL_NUMBER", "RANDOM_DIGITS", "RANDOM_LIST", "RANDOM_NUMBER", "RANDOM_STRING", "RANDOM_SUBSTITUTION", "REGULAR_EXPRESSION", "SHUFFLE", "SQL_EXPRESSION", "SUBSTRING", "TRUNCATE_TABLE", "USER_DEFINED_FUNCTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this FormatEntry.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FormatEntry.
        The type of the format entry.


        :param type: The type of this FormatEntry.
        :type: str
        """
        allowed_values = ["DELETE_ROWS", "DETERMINISTIC_SUBSTITUTION", "DETERMINISTIC_ENCRYPTION", "DETERMINISTIC_ENCRYPTION_DATE", "FIXED_NUMBER", "FIXED_STRING", "LIBRARY_MASKING_FORMAT", "NULL_VALUE", "POST_PROCESSING_FUNCTION", "PRESERVE_ORIGINAL_DATA", "RANDOM_DATE", "RANDOM_DECIMAL_NUMBER", "RANDOM_DIGITS", "RANDOM_LIST", "RANDOM_NUMBER", "RANDOM_STRING", "RANDOM_SUBSTITUTION", "REGULAR_EXPRESSION", "SHUFFLE", "SQL_EXPRESSION", "SUBSTRING", "TRUNCATE_TABLE", "USER_DEFINED_FUNCTION"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def description(self):
        """
        Gets the description of this FormatEntry.
        The description of the format entry.


        :return: The description of this FormatEntry.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FormatEntry.
        The description of the format entry.


        :param description: The description of this FormatEntry.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
