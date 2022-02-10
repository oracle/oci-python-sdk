# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaskedColumnSummary(object):
    """
    Summary of a masked column. A masked column is a database column masked by a data masking request.
    """

    #: A constant which can be used with the object_type property of a MaskedColumnSummary.
    #: This constant has a value of "TABLE"
    OBJECT_TYPE_TABLE = "TABLE"

    #: A constant which can be used with the object_type property of a MaskedColumnSummary.
    #: This constant has a value of "EDITIONING_VIEW"
    OBJECT_TYPE_EDITIONING_VIEW = "EDITIONING_VIEW"

    def __init__(self, **kwargs):
        """
        Initializes a new MaskedColumnSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this MaskedColumnSummary.
        :type key: str

        :param parent_column_key:
            The value to assign to the parent_column_key property of this MaskedColumnSummary.
        :type parent_column_key: str

        :param sensitive_type_id:
            The value to assign to the sensitive_type_id property of this MaskedColumnSummary.
        :type sensitive_type_id: str

        :param schema_name:
            The value to assign to the schema_name property of this MaskedColumnSummary.
        :type schema_name: str

        :param object_name:
            The value to assign to the object_name property of this MaskedColumnSummary.
        :type object_name: str

        :param object_type:
            The value to assign to the object_type property of this MaskedColumnSummary.
            Allowed values for this property are: "TABLE", "EDITIONING_VIEW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type object_type: str

        :param column_name:
            The value to assign to the column_name property of this MaskedColumnSummary.
        :type column_name: str

        :param masking_column_group:
            The value to assign to the masking_column_group property of this MaskedColumnSummary.
        :type masking_column_group: str

        :param masking_format_used:
            The value to assign to the masking_format_used property of this MaskedColumnSummary.
        :type masking_format_used: str

        :param total_masked_values:
            The value to assign to the total_masked_values property of this MaskedColumnSummary.
        :type total_masked_values: int

        """
        self.swagger_types = {
            'key': 'str',
            'parent_column_key': 'str',
            'sensitive_type_id': 'str',
            'schema_name': 'str',
            'object_name': 'str',
            'object_type': 'str',
            'column_name': 'str',
            'masking_column_group': 'str',
            'masking_format_used': 'str',
            'total_masked_values': 'int'
        }

        self.attribute_map = {
            'key': 'key',
            'parent_column_key': 'parentColumnKey',
            'sensitive_type_id': 'sensitiveTypeId',
            'schema_name': 'schemaName',
            'object_name': 'objectName',
            'object_type': 'objectType',
            'column_name': 'columnName',
            'masking_column_group': 'maskingColumnGroup',
            'masking_format_used': 'maskingFormatUsed',
            'total_masked_values': 'totalMaskedValues'
        }

        self._key = None
        self._parent_column_key = None
        self._sensitive_type_id = None
        self._schema_name = None
        self._object_name = None
        self._object_type = None
        self._column_name = None
        self._masking_column_group = None
        self._masking_format_used = None
        self._total_masked_values = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this MaskedColumnSummary.
        The unique key that identifies the masked column. It's numeric and unique within a masking policy.


        :return: The key of this MaskedColumnSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this MaskedColumnSummary.
        The unique key that identifies the masked column. It's numeric and unique within a masking policy.


        :param key: The key of this MaskedColumnSummary.
        :type: str
        """
        self._key = key

    @property
    def parent_column_key(self):
        """
        Gets the parent_column_key of this MaskedColumnSummary.
        The unique key that identifies the parent column of the masked column.


        :return: The parent_column_key of this MaskedColumnSummary.
        :rtype: str
        """
        return self._parent_column_key

    @parent_column_key.setter
    def parent_column_key(self, parent_column_key):
        """
        Sets the parent_column_key of this MaskedColumnSummary.
        The unique key that identifies the parent column of the masked column.


        :param parent_column_key: The parent_column_key of this MaskedColumnSummary.
        :type: str
        """
        self._parent_column_key = parent_column_key

    @property
    def sensitive_type_id(self):
        """
        Gets the sensitive_type_id of this MaskedColumnSummary.
        The OCID of the sensitive type associated with the masked column.


        :return: The sensitive_type_id of this MaskedColumnSummary.
        :rtype: str
        """
        return self._sensitive_type_id

    @sensitive_type_id.setter
    def sensitive_type_id(self, sensitive_type_id):
        """
        Sets the sensitive_type_id of this MaskedColumnSummary.
        The OCID of the sensitive type associated with the masked column.


        :param sensitive_type_id: The sensitive_type_id of this MaskedColumnSummary.
        :type: str
        """
        self._sensitive_type_id = sensitive_type_id

    @property
    def schema_name(self):
        """
        **[Required]** Gets the schema_name of this MaskedColumnSummary.
        The name of the schema that contains the masked column.


        :return: The schema_name of this MaskedColumnSummary.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this MaskedColumnSummary.
        The name of the schema that contains the masked column.


        :param schema_name: The schema_name of this MaskedColumnSummary.
        :type: str
        """
        self._schema_name = schema_name

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this MaskedColumnSummary.
        The name of the object (table or editioning view) that contains the masked column.


        :return: The object_name of this MaskedColumnSummary.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this MaskedColumnSummary.
        The name of the object (table or editioning view) that contains the masked column.


        :param object_name: The object_name of this MaskedColumnSummary.
        :type: str
        """
        self._object_name = object_name

    @property
    def object_type(self):
        """
        **[Required]** Gets the object_type of this MaskedColumnSummary.
        The type of the object (table or editioning view) that contains the masked column.

        Allowed values for this property are: "TABLE", "EDITIONING_VIEW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The object_type of this MaskedColumnSummary.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this MaskedColumnSummary.
        The type of the object (table or editioning view) that contains the masked column.


        :param object_type: The object_type of this MaskedColumnSummary.
        :type: str
        """
        allowed_values = ["TABLE", "EDITIONING_VIEW"]
        if not value_allowed_none_or_none_sentinel(object_type, allowed_values):
            object_type = 'UNKNOWN_ENUM_VALUE'
        self._object_type = object_type

    @property
    def column_name(self):
        """
        **[Required]** Gets the column_name of this MaskedColumnSummary.
        The name of the masked column.


        :return: The column_name of this MaskedColumnSummary.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """
        Sets the column_name of this MaskedColumnSummary.
        The name of the masked column.


        :param column_name: The column_name of this MaskedColumnSummary.
        :type: str
        """
        self._column_name = column_name

    @property
    def masking_column_group(self):
        """
        Gets the masking_column_group of this MaskedColumnSummary.
        The masking group of the masked column.


        :return: The masking_column_group of this MaskedColumnSummary.
        :rtype: str
        """
        return self._masking_column_group

    @masking_column_group.setter
    def masking_column_group(self, masking_column_group):
        """
        Sets the masking_column_group of this MaskedColumnSummary.
        The masking group of the masked column.


        :param masking_column_group: The masking_column_group of this MaskedColumnSummary.
        :type: str
        """
        self._masking_column_group = masking_column_group

    @property
    def masking_format_used(self):
        """
        **[Required]** Gets the masking_format_used of this MaskedColumnSummary.
        The masking format used for masking the column.


        :return: The masking_format_used of this MaskedColumnSummary.
        :rtype: str
        """
        return self._masking_format_used

    @masking_format_used.setter
    def masking_format_used(self, masking_format_used):
        """
        Sets the masking_format_used of this MaskedColumnSummary.
        The masking format used for masking the column.


        :param masking_format_used: The masking_format_used of this MaskedColumnSummary.
        :type: str
        """
        self._masking_format_used = masking_format_used

    @property
    def total_masked_values(self):
        """
        **[Required]** Gets the total_masked_values of this MaskedColumnSummary.
        The total number of values masked in the column.


        :return: The total_masked_values of this MaskedColumnSummary.
        :rtype: int
        """
        return self._total_masked_values

    @total_masked_values.setter
    def total_masked_values(self, total_masked_values):
        """
        Sets the total_masked_values of this MaskedColumnSummary.
        The total number of values masked in the column.


        :param total_masked_values: The total_masked_values of this MaskedColumnSummary.
        :type: int
        """
        self._total_masked_values = total_masked_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
