# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StatementSummary(object):
    """
    Information derived from parsing a NoSQL SQL statement.
    """

    #: A constant which can be used with the operation property of a StatementSummary.
    #: This constant has a value of "CREATE_TABLE"
    OPERATION_CREATE_TABLE = "CREATE_TABLE"

    #: A constant which can be used with the operation property of a StatementSummary.
    #: This constant has a value of "ALTER_TABLE"
    OPERATION_ALTER_TABLE = "ALTER_TABLE"

    #: A constant which can be used with the operation property of a StatementSummary.
    #: This constant has a value of "DROP_TABLE"
    OPERATION_DROP_TABLE = "DROP_TABLE"

    #: A constant which can be used with the operation property of a StatementSummary.
    #: This constant has a value of "CREATE_INDEX"
    OPERATION_CREATE_INDEX = "CREATE_INDEX"

    #: A constant which can be used with the operation property of a StatementSummary.
    #: This constant has a value of "DROP_INDEX"
    OPERATION_DROP_INDEX = "DROP_INDEX"

    #: A constant which can be used with the operation property of a StatementSummary.
    #: This constant has a value of "SELECT"
    OPERATION_SELECT = "SELECT"

    #: A constant which can be used with the operation property of a StatementSummary.
    #: This constant has a value of "UPDATE"
    OPERATION_UPDATE = "UPDATE"

    #: A constant which can be used with the operation property of a StatementSummary.
    #: This constant has a value of "INSERT"
    OPERATION_INSERT = "INSERT"

    #: A constant which can be used with the operation property of a StatementSummary.
    #: This constant has a value of "DELETE"
    OPERATION_DELETE = "DELETE"

    def __init__(self, **kwargs):
        """
        Initializes a new StatementSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this StatementSummary.
            Allowed values for this property are: "CREATE_TABLE", "ALTER_TABLE", "DROP_TABLE", "CREATE_INDEX", "DROP_INDEX", "SELECT", "UPDATE", "INSERT", "DELETE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation: str

        :param table_name:
            The value to assign to the table_name property of this StatementSummary.
        :type table_name: str

        :param index_name:
            The value to assign to the index_name property of this StatementSummary.
        :type index_name: str

        :param is_if_exists:
            The value to assign to the is_if_exists property of this StatementSummary.
        :type is_if_exists: bool

        :param is_if_not_exists:
            The value to assign to the is_if_not_exists property of this StatementSummary.
        :type is_if_not_exists: bool

        :param syntax_error:
            The value to assign to the syntax_error property of this StatementSummary.
        :type syntax_error: str

        """
        self.swagger_types = {
            'operation': 'str',
            'table_name': 'str',
            'index_name': 'str',
            'is_if_exists': 'bool',
            'is_if_not_exists': 'bool',
            'syntax_error': 'str'
        }

        self.attribute_map = {
            'operation': 'operation',
            'table_name': 'tableName',
            'index_name': 'indexName',
            'is_if_exists': 'isIfExists',
            'is_if_not_exists': 'isIfNotExists',
            'syntax_error': 'syntaxError'
        }

        self._operation = None
        self._table_name = None
        self._index_name = None
        self._is_if_exists = None
        self._is_if_not_exists = None
        self._syntax_error = None

    @property
    def operation(self):
        """
        Gets the operation of this StatementSummary.
        The operation represented in the statement, e.g. CREATE_TABLE.

        Allowed values for this property are: "CREATE_TABLE", "ALTER_TABLE", "DROP_TABLE", "CREATE_INDEX", "DROP_INDEX", "SELECT", "UPDATE", "INSERT", "DELETE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation of this StatementSummary.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this StatementSummary.
        The operation represented in the statement, e.g. CREATE_TABLE.


        :param operation: The operation of this StatementSummary.
        :type: str
        """
        allowed_values = ["CREATE_TABLE", "ALTER_TABLE", "DROP_TABLE", "CREATE_INDEX", "DROP_INDEX", "SELECT", "UPDATE", "INSERT", "DELETE"]
        if not value_allowed_none_or_none_sentinel(operation, allowed_values):
            operation = 'UNKNOWN_ENUM_VALUE'
        self._operation = operation

    @property
    def table_name(self):
        """
        Gets the table_name of this StatementSummary.
        The table name from the SQL statement.


        :return: The table_name of this StatementSummary.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """
        Sets the table_name of this StatementSummary.
        The table name from the SQL statement.


        :param table_name: The table_name of this StatementSummary.
        :type: str
        """
        self._table_name = table_name

    @property
    def index_name(self):
        """
        Gets the index_name of this StatementSummary.
        The index name from the SQL statement, if present.


        :return: The index_name of this StatementSummary.
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        """
        Sets the index_name of this StatementSummary.
        The index name from the SQL statement, if present.


        :param index_name: The index_name of this StatementSummary.
        :type: str
        """
        self._index_name = index_name

    @property
    def is_if_exists(self):
        """
        Gets the is_if_exists of this StatementSummary.
        True if the statement includes \"IF EXISTS.\"


        :return: The is_if_exists of this StatementSummary.
        :rtype: bool
        """
        return self._is_if_exists

    @is_if_exists.setter
    def is_if_exists(self, is_if_exists):
        """
        Sets the is_if_exists of this StatementSummary.
        True if the statement includes \"IF EXISTS.\"


        :param is_if_exists: The is_if_exists of this StatementSummary.
        :type: bool
        """
        self._is_if_exists = is_if_exists

    @property
    def is_if_not_exists(self):
        """
        Gets the is_if_not_exists of this StatementSummary.
        True if the statement includes \"IF NOT EXISTS.\"


        :return: The is_if_not_exists of this StatementSummary.
        :rtype: bool
        """
        return self._is_if_not_exists

    @is_if_not_exists.setter
    def is_if_not_exists(self, is_if_not_exists):
        """
        Sets the is_if_not_exists of this StatementSummary.
        True if the statement includes \"IF NOT EXISTS.\"


        :param is_if_not_exists: The is_if_not_exists of this StatementSummary.
        :type: bool
        """
        self._is_if_not_exists = is_if_not_exists

    @property
    def syntax_error(self):
        """
        Gets the syntax_error of this StatementSummary.
        If present, indicates a syntax error in the statement.


        :return: The syntax_error of this StatementSummary.
        :rtype: str
        """
        return self._syntax_error

    @syntax_error.setter
    def syntax_error(self, syntax_error):
        """
        Sets the syntax_error of this StatementSummary.
        If present, indicates a syntax error in the statement.


        :param syntax_error: The syntax_error of this StatementSummary.
        :type: str
        """
        self._syntax_error = syntax_error

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
