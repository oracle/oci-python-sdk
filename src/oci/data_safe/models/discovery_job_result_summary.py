# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiscoveryJobResultSummary(object):
    """
    Summary of a discovery job result.
    """

    #: A constant which can be used with the object_type property of a DiscoveryJobResultSummary.
    #: This constant has a value of "TABLE"
    OBJECT_TYPE_TABLE = "TABLE"

    #: A constant which can be used with the object_type property of a DiscoveryJobResultSummary.
    #: This constant has a value of "EDITIONING_VIEW"
    OBJECT_TYPE_EDITIONING_VIEW = "EDITIONING_VIEW"

    #: A constant which can be used with the relation_type property of a DiscoveryJobResultSummary.
    #: This constant has a value of "NONE"
    RELATION_TYPE_NONE = "NONE"

    #: A constant which can be used with the relation_type property of a DiscoveryJobResultSummary.
    #: This constant has a value of "APP_DEFINED"
    RELATION_TYPE_APP_DEFINED = "APP_DEFINED"

    #: A constant which can be used with the relation_type property of a DiscoveryJobResultSummary.
    #: This constant has a value of "DB_DEFINED"
    RELATION_TYPE_DB_DEFINED = "DB_DEFINED"

    def __init__(self, **kwargs):
        """
        Initializes a new DiscoveryJobResultSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this DiscoveryJobResultSummary.
        :type key: str

        :param discovery_type:
            The value to assign to the discovery_type property of this DiscoveryJobResultSummary.
        :type discovery_type: str

        :param sensitive_columnkey:
            The value to assign to the sensitive_columnkey property of this DiscoveryJobResultSummary.
        :type sensitive_columnkey: str

        :param schema_name:
            The value to assign to the schema_name property of this DiscoveryJobResultSummary.
        :type schema_name: str

        :param object_name:
            The value to assign to the object_name property of this DiscoveryJobResultSummary.
        :type object_name: str

        :param column_name:
            The value to assign to the column_name property of this DiscoveryJobResultSummary.
        :type column_name: str

        :param object_type:
            The value to assign to the object_type property of this DiscoveryJobResultSummary.
            Allowed values for this property are: "TABLE", "EDITIONING_VIEW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type object_type: str

        :param data_type:
            The value to assign to the data_type property of this DiscoveryJobResultSummary.
        :type data_type: str

        :param sensitive_type_id:
            The value to assign to the sensitive_type_id property of this DiscoveryJobResultSummary.
        :type sensitive_type_id: str

        :param parent_column_keys:
            The value to assign to the parent_column_keys property of this DiscoveryJobResultSummary.
        :type parent_column_keys: list[str]

        :param relation_type:
            The value to assign to the relation_type property of this DiscoveryJobResultSummary.
            Allowed values for this property are: "NONE", "APP_DEFINED", "DB_DEFINED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type relation_type: str

        :param estimated_data_value_count:
            The value to assign to the estimated_data_value_count property of this DiscoveryJobResultSummary.
        :type estimated_data_value_count: int

        :param sample_data_values:
            The value to assign to the sample_data_values property of this DiscoveryJobResultSummary.
        :type sample_data_values: list[str]

        :param planned_action:
            The value to assign to the planned_action property of this DiscoveryJobResultSummary.
        :type planned_action: str

        :param is_result_applied:
            The value to assign to the is_result_applied property of this DiscoveryJobResultSummary.
        :type is_result_applied: bool

        :param discovery_job_id:
            The value to assign to the discovery_job_id property of this DiscoveryJobResultSummary.
        :type discovery_job_id: str

        """
        self.swagger_types = {
            'key': 'str',
            'discovery_type': 'str',
            'sensitive_columnkey': 'str',
            'schema_name': 'str',
            'object_name': 'str',
            'column_name': 'str',
            'object_type': 'str',
            'data_type': 'str',
            'sensitive_type_id': 'str',
            'parent_column_keys': 'list[str]',
            'relation_type': 'str',
            'estimated_data_value_count': 'int',
            'sample_data_values': 'list[str]',
            'planned_action': 'str',
            'is_result_applied': 'bool',
            'discovery_job_id': 'str'
        }
        self.attribute_map = {
            'key': 'key',
            'discovery_type': 'discoveryType',
            'sensitive_columnkey': 'sensitiveColumnkey',
            'schema_name': 'schemaName',
            'object_name': 'objectName',
            'column_name': 'columnName',
            'object_type': 'objectType',
            'data_type': 'dataType',
            'sensitive_type_id': 'sensitiveTypeId',
            'parent_column_keys': 'parentColumnKeys',
            'relation_type': 'relationType',
            'estimated_data_value_count': 'estimatedDataValueCount',
            'sample_data_values': 'sampleDataValues',
            'planned_action': 'plannedAction',
            'is_result_applied': 'isResultApplied',
            'discovery_job_id': 'discoveryJobId'
        }
        self._key = None
        self._discovery_type = None
        self._sensitive_columnkey = None
        self._schema_name = None
        self._object_name = None
        self._column_name = None
        self._object_type = None
        self._data_type = None
        self._sensitive_type_id = None
        self._parent_column_keys = None
        self._relation_type = None
        self._estimated_data_value_count = None
        self._sample_data_values = None
        self._planned_action = None
        self._is_result_applied = None
        self._discovery_job_id = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this DiscoveryJobResultSummary.
        The unique key that identifies the discovery result.


        :return: The key of this DiscoveryJobResultSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DiscoveryJobResultSummary.
        The unique key that identifies the discovery result.


        :param key: The key of this DiscoveryJobResultSummary.
        :type: str
        """
        self._key = key

    @property
    def discovery_type(self):
        """
        **[Required]** Gets the discovery_type of this DiscoveryJobResultSummary.
        The type of the discovery result. It can be one of the following three types:
        NEW: A new sensitive column in the target database that is not in the sensitive data model.
        DELETED: A column that is present in the sensitive data model but has been deleted from the target database.
        MODIFIED: A column that is present in the target database as well as the sensitive data model but some of its attributes have been modified.


        :return: The discovery_type of this DiscoveryJobResultSummary.
        :rtype: str
        """
        return self._discovery_type

    @discovery_type.setter
    def discovery_type(self, discovery_type):
        """
        Sets the discovery_type of this DiscoveryJobResultSummary.
        The type of the discovery result. It can be one of the following three types:
        NEW: A new sensitive column in the target database that is not in the sensitive data model.
        DELETED: A column that is present in the sensitive data model but has been deleted from the target database.
        MODIFIED: A column that is present in the target database as well as the sensitive data model but some of its attributes have been modified.


        :param discovery_type: The discovery_type of this DiscoveryJobResultSummary.
        :type: str
        """
        self._discovery_type = discovery_type

    @property
    def sensitive_columnkey(self):
        """
        Gets the sensitive_columnkey of this DiscoveryJobResultSummary.
        The unique key that identifies the sensitive column represented by the discovery result.


        :return: The sensitive_columnkey of this DiscoveryJobResultSummary.
        :rtype: str
        """
        return self._sensitive_columnkey

    @sensitive_columnkey.setter
    def sensitive_columnkey(self, sensitive_columnkey):
        """
        Sets the sensitive_columnkey of this DiscoveryJobResultSummary.
        The unique key that identifies the sensitive column represented by the discovery result.


        :param sensitive_columnkey: The sensitive_columnkey of this DiscoveryJobResultSummary.
        :type: str
        """
        self._sensitive_columnkey = sensitive_columnkey

    @property
    def schema_name(self):
        """
        **[Required]** Gets the schema_name of this DiscoveryJobResultSummary.
        The database schema that contains the sensitive column.


        :return: The schema_name of this DiscoveryJobResultSummary.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this DiscoveryJobResultSummary.
        The database schema that contains the sensitive column.


        :param schema_name: The schema_name of this DiscoveryJobResultSummary.
        :type: str
        """
        self._schema_name = schema_name

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this DiscoveryJobResultSummary.
        The database object that contains the sensitive column.


        :return: The object_name of this DiscoveryJobResultSummary.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this DiscoveryJobResultSummary.
        The database object that contains the sensitive column.


        :param object_name: The object_name of this DiscoveryJobResultSummary.
        :type: str
        """
        self._object_name = object_name

    @property
    def column_name(self):
        """
        **[Required]** Gets the column_name of this DiscoveryJobResultSummary.
        The name of the sensitive column.


        :return: The column_name of this DiscoveryJobResultSummary.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """
        Sets the column_name of this DiscoveryJobResultSummary.
        The name of the sensitive column.


        :param column_name: The column_name of this DiscoveryJobResultSummary.
        :type: str
        """
        self._column_name = column_name

    @property
    def object_type(self):
        """
        **[Required]** Gets the object_type of this DiscoveryJobResultSummary.
        The type of the database object that contains the sensitive column.

        Allowed values for this property are: "TABLE", "EDITIONING_VIEW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The object_type of this DiscoveryJobResultSummary.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this DiscoveryJobResultSummary.
        The type of the database object that contains the sensitive column.


        :param object_type: The object_type of this DiscoveryJobResultSummary.
        :type: str
        """
        allowed_values = ["TABLE", "EDITIONING_VIEW"]
        if not value_allowed_none_or_none_sentinel(object_type, allowed_values):
            object_type = 'UNKNOWN_ENUM_VALUE'
        self._object_type = object_type

    @property
    def data_type(self):
        """
        **[Required]** Gets the data_type of this DiscoveryJobResultSummary.
        The data type of the sensitive column.


        :return: The data_type of this DiscoveryJobResultSummary.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this DiscoveryJobResultSummary.
        The data type of the sensitive column.


        :param data_type: The data_type of this DiscoveryJobResultSummary.
        :type: str
        """
        self._data_type = data_type

    @property
    def sensitive_type_id(self):
        """
        Gets the sensitive_type_id of this DiscoveryJobResultSummary.
        The OCID of the sensitive type associated with the sensitive column.


        :return: The sensitive_type_id of this DiscoveryJobResultSummary.
        :rtype: str
        """
        return self._sensitive_type_id

    @sensitive_type_id.setter
    def sensitive_type_id(self, sensitive_type_id):
        """
        Sets the sensitive_type_id of this DiscoveryJobResultSummary.
        The OCID of the sensitive type associated with the sensitive column.


        :param sensitive_type_id: The sensitive_type_id of this DiscoveryJobResultSummary.
        :type: str
        """
        self._sensitive_type_id = sensitive_type_id

    @property
    def parent_column_keys(self):
        """
        Gets the parent_column_keys of this DiscoveryJobResultSummary.
        Unique keys identifying the columns that are parents of the sensitive column. At present, it tracks a single parent only.


        :return: The parent_column_keys of this DiscoveryJobResultSummary.
        :rtype: list[str]
        """
        return self._parent_column_keys

    @parent_column_keys.setter
    def parent_column_keys(self, parent_column_keys):
        """
        Sets the parent_column_keys of this DiscoveryJobResultSummary.
        Unique keys identifying the columns that are parents of the sensitive column. At present, it tracks a single parent only.


        :param parent_column_keys: The parent_column_keys of this DiscoveryJobResultSummary.
        :type: list[str]
        """
        self._parent_column_keys = parent_column_keys

    @property
    def relation_type(self):
        """
        **[Required]** Gets the relation_type of this DiscoveryJobResultSummary.
        The type of referential relationship the sensitive column has with its parent. NONE indicates that the sensitive
        column does not have a parent. DB_DEFINED indicates that the relationship is defined in the database dictionary.
        APP_DEFINED indicates that the relationship is defined at the application level and not in the database dictionary.

        Allowed values for this property are: "NONE", "APP_DEFINED", "DB_DEFINED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The relation_type of this DiscoveryJobResultSummary.
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """
        Sets the relation_type of this DiscoveryJobResultSummary.
        The type of referential relationship the sensitive column has with its parent. NONE indicates that the sensitive
        column does not have a parent. DB_DEFINED indicates that the relationship is defined in the database dictionary.
        APP_DEFINED indicates that the relationship is defined at the application level and not in the database dictionary.


        :param relation_type: The relation_type of this DiscoveryJobResultSummary.
        :type: str
        """
        allowed_values = ["NONE", "APP_DEFINED", "DB_DEFINED"]
        if not value_allowed_none_or_none_sentinel(relation_type, allowed_values):
            relation_type = 'UNKNOWN_ENUM_VALUE'
        self._relation_type = relation_type

    @property
    def estimated_data_value_count(self):
        """
        **[Required]** Gets the estimated_data_value_count of this DiscoveryJobResultSummary.
        The estimated number of data values the column has in the associated database.


        :return: The estimated_data_value_count of this DiscoveryJobResultSummary.
        :rtype: int
        """
        return self._estimated_data_value_count

    @estimated_data_value_count.setter
    def estimated_data_value_count(self, estimated_data_value_count):
        """
        Sets the estimated_data_value_count of this DiscoveryJobResultSummary.
        The estimated number of data values the column has in the associated database.


        :param estimated_data_value_count: The estimated_data_value_count of this DiscoveryJobResultSummary.
        :type: int
        """
        self._estimated_data_value_count = estimated_data_value_count

    @property
    def sample_data_values(self):
        """
        Gets the sample_data_values of this DiscoveryJobResultSummary.
        Original data values collected for the sensitive column from the associated database. Sample data helps review
        the column and ensure that it actually contains sensitive data. Note that sample data is retrieved by a data
        discovery job only if the isSampleDataCollectionEnabled attribute is set to true. At present, only one data
        value is collected per sensitive column.


        :return: The sample_data_values of this DiscoveryJobResultSummary.
        :rtype: list[str]
        """
        return self._sample_data_values

    @sample_data_values.setter
    def sample_data_values(self, sample_data_values):
        """
        Sets the sample_data_values of this DiscoveryJobResultSummary.
        Original data values collected for the sensitive column from the associated database. Sample data helps review
        the column and ensure that it actually contains sensitive data. Note that sample data is retrieved by a data
        discovery job only if the isSampleDataCollectionEnabled attribute is set to true. At present, only one data
        value is collected per sensitive column.


        :param sample_data_values: The sample_data_values of this DiscoveryJobResultSummary.
        :type: list[str]
        """
        self._sample_data_values = sample_data_values

    @property
    def planned_action(self):
        """
        **[Required]** Gets the planned_action of this DiscoveryJobResultSummary.
        Specifies how to process the discovery result. It's set to NONE by default. Use the PatchDiscoveryJobResults operation to update this attribute. You can choose one of the following options:
        ACCEPT: To accept the discovery result and update the sensitive data model to reflect the changes.
        REJECT: To reject the discovery result so that it doesn't change the sensitive data model.
        INVALIDATE: To invalidate a newly discovered column. It adds the column to the sensitive data model but marks it as invalid. It helps track false positives and ensure that they aren't reported by future discovery jobs.
        After specifying the planned action, you can use the ApplyDiscoveryJobResults operation to automatically process the discovery results.


        :return: The planned_action of this DiscoveryJobResultSummary.
        :rtype: str
        """
        return self._planned_action

    @planned_action.setter
    def planned_action(self, planned_action):
        """
        Sets the planned_action of this DiscoveryJobResultSummary.
        Specifies how to process the discovery result. It's set to NONE by default. Use the PatchDiscoveryJobResults operation to update this attribute. You can choose one of the following options:
        ACCEPT: To accept the discovery result and update the sensitive data model to reflect the changes.
        REJECT: To reject the discovery result so that it doesn't change the sensitive data model.
        INVALIDATE: To invalidate a newly discovered column. It adds the column to the sensitive data model but marks it as invalid. It helps track false positives and ensure that they aren't reported by future discovery jobs.
        After specifying the planned action, you can use the ApplyDiscoveryJobResults operation to automatically process the discovery results.


        :param planned_action: The planned_action of this DiscoveryJobResultSummary.
        :type: str
        """
        self._planned_action = planned_action

    @property
    def is_result_applied(self):
        """
        **[Required]** Gets the is_result_applied of this DiscoveryJobResultSummary.
        Indicates whether the discovery result has been processed. You can update this attribute using the PatchDiscoveryJobResults
        operation to track whether the discovery result has already been processed and applied to the sensitive data model.


        :return: The is_result_applied of this DiscoveryJobResultSummary.
        :rtype: bool
        """
        return self._is_result_applied

    @is_result_applied.setter
    def is_result_applied(self, is_result_applied):
        """
        Sets the is_result_applied of this DiscoveryJobResultSummary.
        Indicates whether the discovery result has been processed. You can update this attribute using the PatchDiscoveryJobResults
        operation to track whether the discovery result has already been processed and applied to the sensitive data model.


        :param is_result_applied: The is_result_applied of this DiscoveryJobResultSummary.
        :type: bool
        """
        self._is_result_applied = is_result_applied

    @property
    def discovery_job_id(self):
        """
        **[Required]** Gets the discovery_job_id of this DiscoveryJobResultSummary.
        The OCID of the discovery job.


        :return: The discovery_job_id of this DiscoveryJobResultSummary.
        :rtype: str
        """
        return self._discovery_job_id

    @discovery_job_id.setter
    def discovery_job_id(self, discovery_job_id):
        """
        Sets the discovery_job_id of this DiscoveryJobResultSummary.
        The OCID of the discovery job.


        :param discovery_job_id: The discovery_job_id of this DiscoveryJobResultSummary.
        :type: str
        """
        self._discovery_job_id = discovery_job_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
