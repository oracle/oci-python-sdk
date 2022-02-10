# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .format_entry import FormatEntry
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RandomSubstitutionFormatEntry(FormatEntry):
    """
    The Random Substitution masking format uses the specified substitution column
    as the source of masked values. The values in the substitution column are randomly
    ordered before mapping them to the original column values. As a masking operation
    renames tables temporarily, the substitution column must be in a table that has
    no masking column. Also, you may want to ensure that the substitution column has
    sufficient values to uniquely mask the target column.

    Unlike Deterministic Substitution, Random Substitution doesn't do deterministic
    masking, and thus, doesn't require a seed value. To learn more, check Random
    Substitution in the Data Safe documentation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RandomSubstitutionFormatEntry object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.RandomSubstitutionFormatEntry.type` attribute
        of this class is ``RANDOM_SUBSTITUTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this RandomSubstitutionFormatEntry.
            Allowed values for this property are: "DELETE_ROWS", "DETERMINISTIC_SUBSTITUTION", "DETERMINISTIC_ENCRYPTION", "DETERMINISTIC_ENCRYPTION_DATE", "FIXED_NUMBER", "FIXED_STRING", "LIBRARY_MASKING_FORMAT", "NULL_VALUE", "POST_PROCESSING_FUNCTION", "PRESERVE_ORIGINAL_DATA", "RANDOM_DATE", "RANDOM_DECIMAL_NUMBER", "RANDOM_DIGITS", "RANDOM_LIST", "RANDOM_NUMBER", "RANDOM_STRING", "RANDOM_SUBSTITUTION", "REGULAR_EXPRESSION", "SHUFFLE", "SQL_EXPRESSION", "SUBSTRING", "TRUNCATE_TABLE", "USER_DEFINED_FUNCTION"
        :type type: str

        :param description:
            The value to assign to the description property of this RandomSubstitutionFormatEntry.
        :type description: str

        :param schema_name:
            The value to assign to the schema_name property of this RandomSubstitutionFormatEntry.
        :type schema_name: str

        :param table_name:
            The value to assign to the table_name property of this RandomSubstitutionFormatEntry.
        :type table_name: str

        :param column_name:
            The value to assign to the column_name property of this RandomSubstitutionFormatEntry.
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
        self._type = 'RANDOM_SUBSTITUTION'

    @property
    def schema_name(self):
        """
        **[Required]** Gets the schema_name of this RandomSubstitutionFormatEntry.
        The name of the schema that contains the substitution column.


        :return: The schema_name of this RandomSubstitutionFormatEntry.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this RandomSubstitutionFormatEntry.
        The name of the schema that contains the substitution column.


        :param schema_name: The schema_name of this RandomSubstitutionFormatEntry.
        :type: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        """
        **[Required]** Gets the table_name of this RandomSubstitutionFormatEntry.
        The name of the table that contains the substitution column.


        :return: The table_name of this RandomSubstitutionFormatEntry.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """
        Sets the table_name of this RandomSubstitutionFormatEntry.
        The name of the table that contains the substitution column.


        :param table_name: The table_name of this RandomSubstitutionFormatEntry.
        :type: str
        """
        self._table_name = table_name

    @property
    def column_name(self):
        """
        **[Required]** Gets the column_name of this RandomSubstitutionFormatEntry.
        The name of the substitution column.


        :return: The column_name of this RandomSubstitutionFormatEntry.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """
        Sets the column_name of this RandomSubstitutionFormatEntry.
        The name of the substitution column.


        :param column_name: The column_name of this RandomSubstitutionFormatEntry.
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
