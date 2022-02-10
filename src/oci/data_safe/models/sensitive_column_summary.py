# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SensitiveColumnSummary(object):
    """
    Summary of a sensitive column present in a sensitive data model.
    """

    #: A constant which can be used with the lifecycle_state property of a SensitiveColumnSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SensitiveColumnSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SensitiveColumnSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SensitiveColumnSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SensitiveColumnSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the object_type property of a SensitiveColumnSummary.
    #: This constant has a value of "TABLE"
    OBJECT_TYPE_TABLE = "TABLE"

    #: A constant which can be used with the object_type property of a SensitiveColumnSummary.
    #: This constant has a value of "EDITIONING_VIEW"
    OBJECT_TYPE_EDITIONING_VIEW = "EDITIONING_VIEW"

    #: A constant which can be used with the status property of a SensitiveColumnSummary.
    #: This constant has a value of "VALID"
    STATUS_VALID = "VALID"

    #: A constant which can be used with the status property of a SensitiveColumnSummary.
    #: This constant has a value of "INVALID"
    STATUS_INVALID = "INVALID"

    #: A constant which can be used with the source property of a SensitiveColumnSummary.
    #: This constant has a value of "MANUAL"
    SOURCE_MANUAL = "MANUAL"

    #: A constant which can be used with the source property of a SensitiveColumnSummary.
    #: This constant has a value of "DISCOVERY"
    SOURCE_DISCOVERY = "DISCOVERY"

    #: A constant which can be used with the relation_type property of a SensitiveColumnSummary.
    #: This constant has a value of "NONE"
    RELATION_TYPE_NONE = "NONE"

    #: A constant which can be used with the relation_type property of a SensitiveColumnSummary.
    #: This constant has a value of "APP_DEFINED"
    RELATION_TYPE_APP_DEFINED = "APP_DEFINED"

    #: A constant which can be used with the relation_type property of a SensitiveColumnSummary.
    #: This constant has a value of "DB_DEFINED"
    RELATION_TYPE_DB_DEFINED = "DB_DEFINED"

    def __init__(self, **kwargs):
        """
        Initializes a new SensitiveColumnSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this SensitiveColumnSummary.
        :type key: str

        :param sensitive_data_model_id:
            The value to assign to the sensitive_data_model_id property of this SensitiveColumnSummary.
        :type sensitive_data_model_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SensitiveColumnSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this SensitiveColumnSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this SensitiveColumnSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SensitiveColumnSummary.
        :type time_updated: datetime

        :param app_name:
            The value to assign to the app_name property of this SensitiveColumnSummary.
        :type app_name: str

        :param schema_name:
            The value to assign to the schema_name property of this SensitiveColumnSummary.
        :type schema_name: str

        :param object_name:
            The value to assign to the object_name property of this SensitiveColumnSummary.
        :type object_name: str

        :param column_name:
            The value to assign to the column_name property of this SensitiveColumnSummary.
        :type column_name: str

        :param object_type:
            The value to assign to the object_type property of this SensitiveColumnSummary.
            Allowed values for this property are: "TABLE", "EDITIONING_VIEW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type object_type: str

        :param data_type:
            The value to assign to the data_type property of this SensitiveColumnSummary.
        :type data_type: str

        :param status:
            The value to assign to the status property of this SensitiveColumnSummary.
            Allowed values for this property are: "VALID", "INVALID", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param sensitive_type_id:
            The value to assign to the sensitive_type_id property of this SensitiveColumnSummary.
        :type sensitive_type_id: str

        :param source:
            The value to assign to the source property of this SensitiveColumnSummary.
            Allowed values for this property are: "MANUAL", "DISCOVERY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source: str

        :param parent_column_keys:
            The value to assign to the parent_column_keys property of this SensitiveColumnSummary.
        :type parent_column_keys: list[str]

        :param relation_type:
            The value to assign to the relation_type property of this SensitiveColumnSummary.
            Allowed values for this property are: "NONE", "APP_DEFINED", "DB_DEFINED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type relation_type: str

        :param estimated_data_value_count:
            The value to assign to the estimated_data_value_count property of this SensitiveColumnSummary.
        :type estimated_data_value_count: int

        :param sample_data_values:
            The value to assign to the sample_data_values property of this SensitiveColumnSummary.
        :type sample_data_values: list[str]

        """
        self.swagger_types = {
            'key': 'str',
            'sensitive_data_model_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'app_name': 'str',
            'schema_name': 'str',
            'object_name': 'str',
            'column_name': 'str',
            'object_type': 'str',
            'data_type': 'str',
            'status': 'str',
            'sensitive_type_id': 'str',
            'source': 'str',
            'parent_column_keys': 'list[str]',
            'relation_type': 'str',
            'estimated_data_value_count': 'int',
            'sample_data_values': 'list[str]'
        }

        self.attribute_map = {
            'key': 'key',
            'sensitive_data_model_id': 'sensitiveDataModelId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'app_name': 'appName',
            'schema_name': 'schemaName',
            'object_name': 'objectName',
            'column_name': 'columnName',
            'object_type': 'objectType',
            'data_type': 'dataType',
            'status': 'status',
            'sensitive_type_id': 'sensitiveTypeId',
            'source': 'source',
            'parent_column_keys': 'parentColumnKeys',
            'relation_type': 'relationType',
            'estimated_data_value_count': 'estimatedDataValueCount',
            'sample_data_values': 'sampleDataValues'
        }

        self._key = None
        self._sensitive_data_model_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._app_name = None
        self._schema_name = None
        self._object_name = None
        self._column_name = None
        self._object_type = None
        self._data_type = None
        self._status = None
        self._sensitive_type_id = None
        self._source = None
        self._parent_column_keys = None
        self._relation_type = None
        self._estimated_data_value_count = None
        self._sample_data_values = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this SensitiveColumnSummary.
        The unique key that identifies the sensitive column. It's numeric and unique within a sensitive data model.


        :return: The key of this SensitiveColumnSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this SensitiveColumnSummary.
        The unique key that identifies the sensitive column. It's numeric and unique within a sensitive data model.


        :param key: The key of this SensitiveColumnSummary.
        :type: str
        """
        self._key = key

    @property
    def sensitive_data_model_id(self):
        """
        **[Required]** Gets the sensitive_data_model_id of this SensitiveColumnSummary.
        The OCID of the sensitive data model that contains the sensitive column.


        :return: The sensitive_data_model_id of this SensitiveColumnSummary.
        :rtype: str
        """
        return self._sensitive_data_model_id

    @sensitive_data_model_id.setter
    def sensitive_data_model_id(self, sensitive_data_model_id):
        """
        Sets the sensitive_data_model_id of this SensitiveColumnSummary.
        The OCID of the sensitive data model that contains the sensitive column.


        :param sensitive_data_model_id: The sensitive_data_model_id of this SensitiveColumnSummary.
        :type: str
        """
        self._sensitive_data_model_id = sensitive_data_model_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SensitiveColumnSummary.
        The current state of the sensitive column.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SensitiveColumnSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SensitiveColumnSummary.
        The current state of the sensitive column.


        :param lifecycle_state: The lifecycle_state of this SensitiveColumnSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this SensitiveColumnSummary.
        Details about the current state of the sensitive column.


        :return: The lifecycle_details of this SensitiveColumnSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this SensitiveColumnSummary.
        Details about the current state of the sensitive column.


        :param lifecycle_details: The lifecycle_details of this SensitiveColumnSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SensitiveColumnSummary.
        The date and time, in the format defined by `RFC3339`__,
        the sensitive column was created in the sensitive data model.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this SensitiveColumnSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SensitiveColumnSummary.
        The date and time, in the format defined by `RFC3339`__,
        the sensitive column was created in the sensitive data model.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this SensitiveColumnSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this SensitiveColumnSummary.
        The date and time, in the format defined by `RFC3339`__,
        the sensitive column was last updated in the sensitive data model.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this SensitiveColumnSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this SensitiveColumnSummary.
        The date and time, in the format defined by `RFC3339`__,
        the sensitive column was last updated in the sensitive data model.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this SensitiveColumnSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def app_name(self):
        """
        **[Required]** Gets the app_name of this SensitiveColumnSummary.
        The name of the application associated with the sensitive column. It's useful when the application name is
        different from the schema name. Otherwise, it can be ignored.


        :return: The app_name of this SensitiveColumnSummary.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """
        Sets the app_name of this SensitiveColumnSummary.
        The name of the application associated with the sensitive column. It's useful when the application name is
        different from the schema name. Otherwise, it can be ignored.


        :param app_name: The app_name of this SensitiveColumnSummary.
        :type: str
        """
        self._app_name = app_name

    @property
    def schema_name(self):
        """
        **[Required]** Gets the schema_name of this SensitiveColumnSummary.
        The database schema that contains the sensitive column.


        :return: The schema_name of this SensitiveColumnSummary.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this SensitiveColumnSummary.
        The database schema that contains the sensitive column.


        :param schema_name: The schema_name of this SensitiveColumnSummary.
        :type: str
        """
        self._schema_name = schema_name

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this SensitiveColumnSummary.
        The database object that contains the sensitive column.


        :return: The object_name of this SensitiveColumnSummary.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this SensitiveColumnSummary.
        The database object that contains the sensitive column.


        :param object_name: The object_name of this SensitiveColumnSummary.
        :type: str
        """
        self._object_name = object_name

    @property
    def column_name(self):
        """
        **[Required]** Gets the column_name of this SensitiveColumnSummary.
        The name of the sensitive column.


        :return: The column_name of this SensitiveColumnSummary.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """
        Sets the column_name of this SensitiveColumnSummary.
        The name of the sensitive column.


        :param column_name: The column_name of this SensitiveColumnSummary.
        :type: str
        """
        self._column_name = column_name

    @property
    def object_type(self):
        """
        **[Required]** Gets the object_type of this SensitiveColumnSummary.
        The type of the database object that contains the sensitive column.

        Allowed values for this property are: "TABLE", "EDITIONING_VIEW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The object_type of this SensitiveColumnSummary.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this SensitiveColumnSummary.
        The type of the database object that contains the sensitive column.


        :param object_type: The object_type of this SensitiveColumnSummary.
        :type: str
        """
        allowed_values = ["TABLE", "EDITIONING_VIEW"]
        if not value_allowed_none_or_none_sentinel(object_type, allowed_values):
            object_type = 'UNKNOWN_ENUM_VALUE'
        self._object_type = object_type

    @property
    def data_type(self):
        """
        **[Required]** Gets the data_type of this SensitiveColumnSummary.
        The data type of the sensitive column.


        :return: The data_type of this SensitiveColumnSummary.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this SensitiveColumnSummary.
        The data type of the sensitive column.


        :param data_type: The data_type of this SensitiveColumnSummary.
        :type: str
        """
        self._data_type = data_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this SensitiveColumnSummary.
        The status of the sensitive column. VALID means the column is considered sensitive. INVALID means the column
        is not considered sensitive. Tracking invalid columns in a sensitive data model helps ensure that an
        incremental data discovery job does not identify these columns as sensitive again.

        Allowed values for this property are: "VALID", "INVALID", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this SensitiveColumnSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SensitiveColumnSummary.
        The status of the sensitive column. VALID means the column is considered sensitive. INVALID means the column
        is not considered sensitive. Tracking invalid columns in a sensitive data model helps ensure that an
        incremental data discovery job does not identify these columns as sensitive again.


        :param status: The status of this SensitiveColumnSummary.
        :type: str
        """
        allowed_values = ["VALID", "INVALID"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def sensitive_type_id(self):
        """
        Gets the sensitive_type_id of this SensitiveColumnSummary.
        The OCID of the sensitive type associated with the sensitive column.


        :return: The sensitive_type_id of this SensitiveColumnSummary.
        :rtype: str
        """
        return self._sensitive_type_id

    @sensitive_type_id.setter
    def sensitive_type_id(self, sensitive_type_id):
        """
        Sets the sensitive_type_id of this SensitiveColumnSummary.
        The OCID of the sensitive type associated with the sensitive column.


        :param sensitive_type_id: The sensitive_type_id of this SensitiveColumnSummary.
        :type: str
        """
        self._sensitive_type_id = sensitive_type_id

    @property
    def source(self):
        """
        **[Required]** Gets the source of this SensitiveColumnSummary.
        The source of the sensitive column. DISCOVERY indicates that the column was added to the sensitive data model
        using a data discovery job. MANUAL indicates that the column was added manually.

        Allowed values for this property are: "MANUAL", "DISCOVERY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source of this SensitiveColumnSummary.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this SensitiveColumnSummary.
        The source of the sensitive column. DISCOVERY indicates that the column was added to the sensitive data model
        using a data discovery job. MANUAL indicates that the column was added manually.


        :param source: The source of this SensitiveColumnSummary.
        :type: str
        """
        allowed_values = ["MANUAL", "DISCOVERY"]
        if not value_allowed_none_or_none_sentinel(source, allowed_values):
            source = 'UNKNOWN_ENUM_VALUE'
        self._source = source

    @property
    def parent_column_keys(self):
        """
        Gets the parent_column_keys of this SensitiveColumnSummary.
        Unique keys identifying the columns that are parents of the sensitive column. At present, it tracks a single parent only.


        :return: The parent_column_keys of this SensitiveColumnSummary.
        :rtype: list[str]
        """
        return self._parent_column_keys

    @parent_column_keys.setter
    def parent_column_keys(self, parent_column_keys):
        """
        Sets the parent_column_keys of this SensitiveColumnSummary.
        Unique keys identifying the columns that are parents of the sensitive column. At present, it tracks a single parent only.


        :param parent_column_keys: The parent_column_keys of this SensitiveColumnSummary.
        :type: list[str]
        """
        self._parent_column_keys = parent_column_keys

    @property
    def relation_type(self):
        """
        **[Required]** Gets the relation_type of this SensitiveColumnSummary.
        The type of referential relationship the sensitive column has with its parent. NONE indicates that the
        sensitive column does not have a parent. DB_DEFINED indicates that the relationship is defined in the database
        dictionary. APP_DEFINED indicates that the relationship is defined at the application level and not in the database dictionary.

        Allowed values for this property are: "NONE", "APP_DEFINED", "DB_DEFINED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The relation_type of this SensitiveColumnSummary.
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """
        Sets the relation_type of this SensitiveColumnSummary.
        The type of referential relationship the sensitive column has with its parent. NONE indicates that the
        sensitive column does not have a parent. DB_DEFINED indicates that the relationship is defined in the database
        dictionary. APP_DEFINED indicates that the relationship is defined at the application level and not in the database dictionary.


        :param relation_type: The relation_type of this SensitiveColumnSummary.
        :type: str
        """
        allowed_values = ["NONE", "APP_DEFINED", "DB_DEFINED"]
        if not value_allowed_none_or_none_sentinel(relation_type, allowed_values):
            relation_type = 'UNKNOWN_ENUM_VALUE'
        self._relation_type = relation_type

    @property
    def estimated_data_value_count(self):
        """
        **[Required]** Gets the estimated_data_value_count of this SensitiveColumnSummary.
        The estimated number of data values the column has in the associated database.


        :return: The estimated_data_value_count of this SensitiveColumnSummary.
        :rtype: int
        """
        return self._estimated_data_value_count

    @estimated_data_value_count.setter
    def estimated_data_value_count(self, estimated_data_value_count):
        """
        Sets the estimated_data_value_count of this SensitiveColumnSummary.
        The estimated number of data values the column has in the associated database.


        :param estimated_data_value_count: The estimated_data_value_count of this SensitiveColumnSummary.
        :type: int
        """
        self._estimated_data_value_count = estimated_data_value_count

    @property
    def sample_data_values(self):
        """
        Gets the sample_data_values of this SensitiveColumnSummary.
        Original data values collected for the sensitive column from the associated database. Sample data helps review
        the column and ensure that it actually contains sensitive data. Note that sample data is retrieved by a data
        discovery job only if the isSampleDataCollectionEnabled attribute is set to true. At present, only one data
        value is collected per sensitive column.


        :return: The sample_data_values of this SensitiveColumnSummary.
        :rtype: list[str]
        """
        return self._sample_data_values

    @sample_data_values.setter
    def sample_data_values(self, sample_data_values):
        """
        Sets the sample_data_values of this SensitiveColumnSummary.
        Original data values collected for the sensitive column from the associated database. Sample data helps review
        the column and ensure that it actually contains sensitive data. Note that sample data is retrieved by a data
        discovery job only if the isSampleDataCollectionEnabled attribute is set to true. At present, only one data
        value is collected per sensitive column.


        :param sample_data_values: The sample_data_values of this SensitiveColumnSummary.
        :type: list[str]
        """
        self._sample_data_values = sample_data_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
