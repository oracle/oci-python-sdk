# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .format_entry import FormatEntry
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeterministicSubstitutionFormatEntry(FormatEntry):
    """
    The Deterministic Substitution masking format uses the specified substitution column
    as the source of masked values. It performs hash-based substitution to replace the
    original data in a column with values from the substitution column. As a masking
    operation renames tables temporarily, the substitution column must be in a table
    that has no masking column. Also, you may want to ensure that the substitution column
    has sufficient values to uniquely mask the target column.

    Deterministic Substitution requires a seed value while submitting a masking work
    request. Passing the same seed value when masking multiple times or masking different
    databases ensures that the data is masked deterministically. To learn more, check
    Deterministic Substitution in the Data Safe documentation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeterministicSubstitutionFormatEntry object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.DeterministicSubstitutionFormatEntry.type` attribute
        of this class is ``DETERMINISTIC_SUBSTITUTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DeterministicSubstitutionFormatEntry.
            Allowed values for this property are: "DELETE_ROWS", "DETERMINISTIC_SUBSTITUTION", "DETERMINISTIC_ENCRYPTION", "DETERMINISTIC_ENCRYPTION_DATE", "FIXED_NUMBER", "FIXED_STRING", "LIBRARY_MASKING_FORMAT", "NULL_VALUE", "POST_PROCESSING_FUNCTION", "PRESERVE_ORIGINAL_DATA", "RANDOM_DATE", "RANDOM_DECIMAL_NUMBER", "RANDOM_DIGITS", "RANDOM_LIST", "RANDOM_NUMBER", "RANDOM_STRING", "RANDOM_SUBSTITUTION", "REGULAR_EXPRESSION", "SHUFFLE", "SQL_EXPRESSION", "SUBSTRING", "TRUNCATE_TABLE", "USER_DEFINED_FUNCTION"
        :type type: str

        :param description:
            The value to assign to the description property of this DeterministicSubstitutionFormatEntry.
        :type description: str

        :param schema_name:
            The value to assign to the schema_name property of this DeterministicSubstitutionFormatEntry.
        :type schema_name: str

        :param table_name:
            The value to assign to the table_name property of this DeterministicSubstitutionFormatEntry.
        :type table_name: str

        :param column_name:
            The value to assign to the column_name property of this DeterministicSubstitutionFormatEntry.
        :type column_name: str

        """
        self.swagger_types = {
            'type': 'str',
            'description': 'str',
            'schema_name': 'str',
            'table_name': 'str',
            'column_name': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'description': 'description',
            'schema_name': 'schemaName',
            'table_name': 'tableName',
            'column_name': 'columnName'
        }

        self._type = None
        self._description = None
        self._schema_name = None
        self._table_name = None
        self._column_name = None
        self._type = 'DETERMINISTIC_SUBSTITUTION'

    @property
    def schema_name(self):
        """
        **[Required]** Gets the schema_name of this DeterministicSubstitutionFormatEntry.
        The name of the schema that contains the substitution column.


        :return: The schema_name of this DeterministicSubstitutionFormatEntry.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this DeterministicSubstitutionFormatEntry.
        The name of the schema that contains the substitution column.


        :param schema_name: The schema_name of this DeterministicSubstitutionFormatEntry.
        :type: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        """
        **[Required]** Gets the table_name of this DeterministicSubstitutionFormatEntry.
        The name of the table that contains the substitution column.


        :return: The table_name of this DeterministicSubstitutionFormatEntry.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """
        Sets the table_name of this DeterministicSubstitutionFormatEntry.
        The name of the table that contains the substitution column.


        :param table_name: The table_name of this DeterministicSubstitutionFormatEntry.
        :type: str
        """
        self._table_name = table_name

    @property
    def column_name(self):
        """
        **[Required]** Gets the column_name of this DeterministicSubstitutionFormatEntry.
        The name of the substitution column.


        :return: The column_name of this DeterministicSubstitutionFormatEntry.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """
        Sets the column_name of this DeterministicSubstitutionFormatEntry.
        The name of the substitution column.


        :param column_name: The column_name of this DeterministicSubstitutionFormatEntry.
        :type: str
        """
        self._column_name = column_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
