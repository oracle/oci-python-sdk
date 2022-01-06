# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryableFieldDescription(object):
    """
    An individual field that can be used as part of a query filter.
    """

    #: A constant which can be used with the field_type property of a QueryableFieldDescription.
    #: This constant has a value of "IDENTIFIER"
    FIELD_TYPE_IDENTIFIER = "IDENTIFIER"

    #: A constant which can be used with the field_type property of a QueryableFieldDescription.
    #: This constant has a value of "STRING"
    FIELD_TYPE_STRING = "STRING"

    #: A constant which can be used with the field_type property of a QueryableFieldDescription.
    #: This constant has a value of "INTEGER"
    FIELD_TYPE_INTEGER = "INTEGER"

    #: A constant which can be used with the field_type property of a QueryableFieldDescription.
    #: This constant has a value of "RATIONAL"
    FIELD_TYPE_RATIONAL = "RATIONAL"

    #: A constant which can be used with the field_type property of a QueryableFieldDescription.
    #: This constant has a value of "BOOLEAN"
    FIELD_TYPE_BOOLEAN = "BOOLEAN"

    #: A constant which can be used with the field_type property of a QueryableFieldDescription.
    #: This constant has a value of "DATETIME"
    FIELD_TYPE_DATETIME = "DATETIME"

    #: A constant which can be used with the field_type property of a QueryableFieldDescription.
    #: This constant has a value of "IP"
    FIELD_TYPE_IP = "IP"

    #: A constant which can be used with the field_type property of a QueryableFieldDescription.
    #: This constant has a value of "OBJECT"
    FIELD_TYPE_OBJECT = "OBJECT"

    def __init__(self, **kwargs):
        """
        Initializes a new QueryableFieldDescription object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param field_type:
            The value to assign to the field_type property of this QueryableFieldDescription.
            Allowed values for this property are: "IDENTIFIER", "STRING", "INTEGER", "RATIONAL", "BOOLEAN", "DATETIME", "IP", "OBJECT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type field_type: str

        :param field_name:
            The value to assign to the field_name property of this QueryableFieldDescription.
        :type field_name: str

        :param is_array:
            The value to assign to the is_array property of this QueryableFieldDescription.
        :type is_array: bool

        :param object_properties:
            The value to assign to the object_properties property of this QueryableFieldDescription.
        :type object_properties: list[oci.resource_search.models.QueryableFieldDescription]

        """
        self.swagger_types = {
            'field_type': 'str',
            'field_name': 'str',
            'is_array': 'bool',
            'object_properties': 'list[QueryableFieldDescription]'
        }

        self.attribute_map = {
            'field_type': 'fieldType',
            'field_name': 'fieldName',
            'is_array': 'isArray',
            'object_properties': 'objectProperties'
        }

        self._field_type = None
        self._field_name = None
        self._is_array = None
        self._object_properties = None

    @property
    def field_type(self):
        """
        **[Required]** Gets the field_type of this QueryableFieldDescription.
        The type of the field, which dictates what semantics and query constraints you can use when searching or querying.

        Allowed values for this property are: "IDENTIFIER", "STRING", "INTEGER", "RATIONAL", "BOOLEAN", "DATETIME", "IP", "OBJECT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The field_type of this QueryableFieldDescription.
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """
        Sets the field_type of this QueryableFieldDescription.
        The type of the field, which dictates what semantics and query constraints you can use when searching or querying.


        :param field_type: The field_type of this QueryableFieldDescription.
        :type: str
        """
        allowed_values = ["IDENTIFIER", "STRING", "INTEGER", "RATIONAL", "BOOLEAN", "DATETIME", "IP", "OBJECT"]
        if not value_allowed_none_or_none_sentinel(field_type, allowed_values):
            field_type = 'UNKNOWN_ENUM_VALUE'
        self._field_type = field_type

    @property
    def field_name(self):
        """
        **[Required]** Gets the field_name of this QueryableFieldDescription.
        The name of the field to use when constructing the query. Field names are present for all types except `OBJECT`.


        :return: The field_name of this QueryableFieldDescription.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this QueryableFieldDescription.
        The name of the field to use when constructing the query. Field names are present for all types except `OBJECT`.


        :param field_name: The field_name of this QueryableFieldDescription.
        :type: str
        """
        self._field_name = field_name

    @property
    def is_array(self):
        """
        Gets the is_array of this QueryableFieldDescription.
        Indicates that this field is actually an array of the specified field type.


        :return: The is_array of this QueryableFieldDescription.
        :rtype: bool
        """
        return self._is_array

    @is_array.setter
    def is_array(self, is_array):
        """
        Sets the is_array of this QueryableFieldDescription.
        Indicates that this field is actually an array of the specified field type.


        :param is_array: The is_array of this QueryableFieldDescription.
        :type: bool
        """
        self._is_array = is_array

    @property
    def object_properties(self):
        """
        Gets the object_properties of this QueryableFieldDescription.
        If the field type is `OBJECT`, then this property will provide all the individual properties of the object that can
        be queried.


        :return: The object_properties of this QueryableFieldDescription.
        :rtype: list[oci.resource_search.models.QueryableFieldDescription]
        """
        return self._object_properties

    @object_properties.setter
    def object_properties(self, object_properties):
        """
        Sets the object_properties of this QueryableFieldDescription.
        If the field type is `OBJECT`, then this property will provide all the individual properties of the object that can
        be queried.


        :param object_properties: The object_properties of this QueryableFieldDescription.
        :type: list[oci.resource_search.models.QueryableFieldDescription]
        """
        self._object_properties = object_properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
