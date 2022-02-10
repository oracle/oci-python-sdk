# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSensitiveColumnDetails(object):
    """
    Details to create a new sensitive column in a sensitive data model.
    """

    #: A constant which can be used with the object_type property of a CreateSensitiveColumnDetails.
    #: This constant has a value of "TABLE"
    OBJECT_TYPE_TABLE = "TABLE"

    #: A constant which can be used with the object_type property of a CreateSensitiveColumnDetails.
    #: This constant has a value of "EDITIONING_VIEW"
    OBJECT_TYPE_EDITIONING_VIEW = "EDITIONING_VIEW"

    #: A constant which can be used with the status property of a CreateSensitiveColumnDetails.
    #: This constant has a value of "VALID"
    STATUS_VALID = "VALID"

    #: A constant which can be used with the status property of a CreateSensitiveColumnDetails.
    #: This constant has a value of "INVALID"
    STATUS_INVALID = "INVALID"

    #: A constant which can be used with the relation_type property of a CreateSensitiveColumnDetails.
    #: This constant has a value of "NONE"
    RELATION_TYPE_NONE = "NONE"

    #: A constant which can be used with the relation_type property of a CreateSensitiveColumnDetails.
    #: This constant has a value of "APP_DEFINED"
    RELATION_TYPE_APP_DEFINED = "APP_DEFINED"

    #: A constant which can be used with the relation_type property of a CreateSensitiveColumnDetails.
    #: This constant has a value of "DB_DEFINED"
    RELATION_TYPE_DB_DEFINED = "DB_DEFINED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSensitiveColumnDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param app_name:
            The value to assign to the app_name property of this CreateSensitiveColumnDetails.
        :type app_name: str

        :param schema_name:
            The value to assign to the schema_name property of this CreateSensitiveColumnDetails.
        :type schema_name: str

        :param object_name:
            The value to assign to the object_name property of this CreateSensitiveColumnDetails.
        :type object_name: str

        :param column_name:
            The value to assign to the column_name property of this CreateSensitiveColumnDetails.
        :type column_name: str

        :param object_type:
            The value to assign to the object_type property of this CreateSensitiveColumnDetails.
            Allowed values for this property are: "TABLE", "EDITIONING_VIEW"
        :type object_type: str

        :param data_type:
            The value to assign to the data_type property of this CreateSensitiveColumnDetails.
        :type data_type: str

        :param status:
            The value to assign to the status property of this CreateSensitiveColumnDetails.
            Allowed values for this property are: "VALID", "INVALID"
        :type status: str

        :param sensitive_type_id:
            The value to assign to the sensitive_type_id property of this CreateSensitiveColumnDetails.
        :type sensitive_type_id: str

        :param parent_column_keys:
            The value to assign to the parent_column_keys property of this CreateSensitiveColumnDetails.
        :type parent_column_keys: list[str]

        :param relation_type:
            The value to assign to the relation_type property of this CreateSensitiveColumnDetails.
            Allowed values for this property are: "NONE", "APP_DEFINED", "DB_DEFINED"
        :type relation_type: str

        :param app_defined_child_column_keys:
            The value to assign to the app_defined_child_column_keys property of this CreateSensitiveColumnDetails.
        :type app_defined_child_column_keys: list[str]

        :param db_defined_child_column_keys:
            The value to assign to the db_defined_child_column_keys property of this CreateSensitiveColumnDetails.
        :type db_defined_child_column_keys: list[str]

        """
        self.swagger_types = {
            'app_name': 'str',
            'schema_name': 'str',
            'object_name': 'str',
            'column_name': 'str',
            'object_type': 'str',
            'data_type': 'str',
            'status': 'str',
            'sensitive_type_id': 'str',
            'parent_column_keys': 'list[str]',
            'relation_type': 'str',
            'app_defined_child_column_keys': 'list[str]',
            'db_defined_child_column_keys': 'list[str]'
        }

        self.attribute_map = {
            'app_name': 'appName',
            'schema_name': 'schemaName',
            'object_name': 'objectName',
            'column_name': 'columnName',
            'object_type': 'objectType',
            'data_type': 'dataType',
            'status': 'status',
            'sensitive_type_id': 'sensitiveTypeId',
            'parent_column_keys': 'parentColumnKeys',
            'relation_type': 'relationType',
            'app_defined_child_column_keys': 'appDefinedChildColumnKeys',
            'db_defined_child_column_keys': 'dbDefinedChildColumnKeys'
        }

        self._app_name = None
        self._schema_name = None
        self._object_name = None
        self._column_name = None
        self._object_type = None
        self._data_type = None
        self._status = None
        self._sensitive_type_id = None
        self._parent_column_keys = None
        self._relation_type = None
        self._app_defined_child_column_keys = None
        self._db_defined_child_column_keys = None

    @property
    def app_name(self):
        """
        Gets the app_name of this CreateSensitiveColumnDetails.
        The name of the application associated with the sensitive column. It's useful when the application name is
        different from the schema name. Otherwise, it can be ignored. If this attribute is not provided, it's automatically
        populated with the value provided for the schemaName attribute.


        :return: The app_name of this CreateSensitiveColumnDetails.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """
        Sets the app_name of this CreateSensitiveColumnDetails.
        The name of the application associated with the sensitive column. It's useful when the application name is
        different from the schema name. Otherwise, it can be ignored. If this attribute is not provided, it's automatically
        populated with the value provided for the schemaName attribute.


        :param app_name: The app_name of this CreateSensitiveColumnDetails.
        :type: str
        """
        self._app_name = app_name

    @property
    def schema_name(self):
        """
        **[Required]** Gets the schema_name of this CreateSensitiveColumnDetails.
        The database schema that contains the sensitive column.


        :return: The schema_name of this CreateSensitiveColumnDetails.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this CreateSensitiveColumnDetails.
        The database schema that contains the sensitive column.


        :param schema_name: The schema_name of this CreateSensitiveColumnDetails.
        :type: str
        """
        self._schema_name = schema_name

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this CreateSensitiveColumnDetails.
        The database object that contains the sensitive column.


        :return: The object_name of this CreateSensitiveColumnDetails.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this CreateSensitiveColumnDetails.
        The database object that contains the sensitive column.


        :param object_name: The object_name of this CreateSensitiveColumnDetails.
        :type: str
        """
        self._object_name = object_name

    @property
    def column_name(self):
        """
        **[Required]** Gets the column_name of this CreateSensitiveColumnDetails.
        The name of the sensitive column.


        :return: The column_name of this CreateSensitiveColumnDetails.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """
        Sets the column_name of this CreateSensitiveColumnDetails.
        The name of the sensitive column.


        :param column_name: The column_name of this CreateSensitiveColumnDetails.
        :type: str
        """
        self._column_name = column_name

    @property
    def object_type(self):
        """
        Gets the object_type of this CreateSensitiveColumnDetails.
        The type of the database object that contains the sensitive column.

        Allowed values for this property are: "TABLE", "EDITIONING_VIEW"


        :return: The object_type of this CreateSensitiveColumnDetails.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this CreateSensitiveColumnDetails.
        The type of the database object that contains the sensitive column.


        :param object_type: The object_type of this CreateSensitiveColumnDetails.
        :type: str
        """
        allowed_values = ["TABLE", "EDITIONING_VIEW"]
        if not value_allowed_none_or_none_sentinel(object_type, allowed_values):
            raise ValueError(
                "Invalid value for `object_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._object_type = object_type

    @property
    def data_type(self):
        """
        Gets the data_type of this CreateSensitiveColumnDetails.
        The data type of the sensitive column.


        :return: The data_type of this CreateSensitiveColumnDetails.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this CreateSensitiveColumnDetails.
        The data type of the sensitive column.


        :param data_type: The data_type of this CreateSensitiveColumnDetails.
        :type: str
        """
        self._data_type = data_type

    @property
    def status(self):
        """
        Gets the status of this CreateSensitiveColumnDetails.
        The status of the sensitive column. VALID means the column is considered sensitive. INVALID means the column
        is not considered sensitive. Tracking invalid columns in a sensitive data model helps ensure that an incremental
        data discovery job does not identify these columns as sensitive.

        Allowed values for this property are: "VALID", "INVALID"


        :return: The status of this CreateSensitiveColumnDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this CreateSensitiveColumnDetails.
        The status of the sensitive column. VALID means the column is considered sensitive. INVALID means the column
        is not considered sensitive. Tracking invalid columns in a sensitive data model helps ensure that an incremental
        data discovery job does not identify these columns as sensitive.


        :param status: The status of this CreateSensitiveColumnDetails.
        :type: str
        """
        allowed_values = ["VALID", "INVALID"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                "Invalid value for `status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def sensitive_type_id(self):
        """
        Gets the sensitive_type_id of this CreateSensitiveColumnDetails.
        The OCID of the sensitive type to be associated with the sensitive column.


        :return: The sensitive_type_id of this CreateSensitiveColumnDetails.
        :rtype: str
        """
        return self._sensitive_type_id

    @sensitive_type_id.setter
    def sensitive_type_id(self, sensitive_type_id):
        """
        Sets the sensitive_type_id of this CreateSensitiveColumnDetails.
        The OCID of the sensitive type to be associated with the sensitive column.


        :param sensitive_type_id: The sensitive_type_id of this CreateSensitiveColumnDetails.
        :type: str
        """
        self._sensitive_type_id = sensitive_type_id

    @property
    def parent_column_keys(self):
        """
        Gets the parent_column_keys of this CreateSensitiveColumnDetails.
        Unique keys identifying the columns that are parents of the sensitive column. At present, it accepts only one
        parent column key. This attribute can be used to establish relationship between columns in a sensitive data model.
        Note that the parent column must be added to the sensitive data model before its key can be specified here.
        If this attribute is provided, the appDefinedChildColumnKeys or dbDefinedChildColumnKeys attribute of the parent
        column is automatically updated to reflect the relationship.


        :return: The parent_column_keys of this CreateSensitiveColumnDetails.
        :rtype: list[str]
        """
        return self._parent_column_keys

    @parent_column_keys.setter
    def parent_column_keys(self, parent_column_keys):
        """
        Sets the parent_column_keys of this CreateSensitiveColumnDetails.
        Unique keys identifying the columns that are parents of the sensitive column. At present, it accepts only one
        parent column key. This attribute can be used to establish relationship between columns in a sensitive data model.
        Note that the parent column must be added to the sensitive data model before its key can be specified here.
        If this attribute is provided, the appDefinedChildColumnKeys or dbDefinedChildColumnKeys attribute of the parent
        column is automatically updated to reflect the relationship.


        :param parent_column_keys: The parent_column_keys of this CreateSensitiveColumnDetails.
        :type: list[str]
        """
        self._parent_column_keys = parent_column_keys

    @property
    def relation_type(self):
        """
        Gets the relation_type of this CreateSensitiveColumnDetails.
        The type of referential relationship the sensitive column has with its parent. NONE indicates that the sensitive
        column does not have a parent. DB_DEFINED indicates that the relationship is defined in the database dictionary.
        APP_DEFINED indicates that the relationship is defined at the application level and not in the database dictionary.

        Allowed values for this property are: "NONE", "APP_DEFINED", "DB_DEFINED"


        :return: The relation_type of this CreateSensitiveColumnDetails.
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """
        Sets the relation_type of this CreateSensitiveColumnDetails.
        The type of referential relationship the sensitive column has with its parent. NONE indicates that the sensitive
        column does not have a parent. DB_DEFINED indicates that the relationship is defined in the database dictionary.
        APP_DEFINED indicates that the relationship is defined at the application level and not in the database dictionary.


        :param relation_type: The relation_type of this CreateSensitiveColumnDetails.
        :type: str
        """
        allowed_values = ["NONE", "APP_DEFINED", "DB_DEFINED"]
        if not value_allowed_none_or_none_sentinel(relation_type, allowed_values):
            raise ValueError(
                "Invalid value for `relation_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._relation_type = relation_type

    @property
    def app_defined_child_column_keys(self):
        """
        Gets the app_defined_child_column_keys of this CreateSensitiveColumnDetails.
        Unique keys identifying the columns that are application-level (non-dictionary) children of the sensitive column.
        This attribute can be used to establish relationship between columns in a sensitive data model. Note that the
        child columns must be added to the sensitive data model before their keys can be specified here. If this attribute
        is provided, the parentColumnKeys and relationType attributes of the child columns are automatically updated to reflect the relationship.


        :return: The app_defined_child_column_keys of this CreateSensitiveColumnDetails.
        :rtype: list[str]
        """
        return self._app_defined_child_column_keys

    @app_defined_child_column_keys.setter
    def app_defined_child_column_keys(self, app_defined_child_column_keys):
        """
        Sets the app_defined_child_column_keys of this CreateSensitiveColumnDetails.
        Unique keys identifying the columns that are application-level (non-dictionary) children of the sensitive column.
        This attribute can be used to establish relationship between columns in a sensitive data model. Note that the
        child columns must be added to the sensitive data model before their keys can be specified here. If this attribute
        is provided, the parentColumnKeys and relationType attributes of the child columns are automatically updated to reflect the relationship.


        :param app_defined_child_column_keys: The app_defined_child_column_keys of this CreateSensitiveColumnDetails.
        :type: list[str]
        """
        self._app_defined_child_column_keys = app_defined_child_column_keys

    @property
    def db_defined_child_column_keys(self):
        """
        Gets the db_defined_child_column_keys of this CreateSensitiveColumnDetails.
        Unique keys identifying the columns that are database-level (dictionary-defined) children of the sensitive column.
        This attribute can be used to establish relationship between columns in a sensitive data model. Note that the
        child columns must be added to the sensitive data model before their keys can be specified here. If this attribute
        is provided, the parentColumnKeys and relationType attributes of the child columns are automatically updated to reflect the relationship.


        :return: The db_defined_child_column_keys of this CreateSensitiveColumnDetails.
        :rtype: list[str]
        """
        return self._db_defined_child_column_keys

    @db_defined_child_column_keys.setter
    def db_defined_child_column_keys(self, db_defined_child_column_keys):
        """
        Sets the db_defined_child_column_keys of this CreateSensitiveColumnDetails.
        Unique keys identifying the columns that are database-level (dictionary-defined) children of the sensitive column.
        This attribute can be used to establish relationship between columns in a sensitive data model. Note that the
        child columns must be added to the sensitive data model before their keys can be specified here. If this attribute
        is provided, the parentColumnKeys and relationType attributes of the child columns are automatically updated to reflect the relationship.


        :param db_defined_child_column_keys: The db_defined_child_column_keys of this CreateSensitiveColumnDetails.
        :type: list[str]
        """
        self._db_defined_child_column_keys = db_defined_child_column_keys

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
