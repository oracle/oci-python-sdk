# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FlattenProjectionPreferences(object):
    """
    The preferences for the flatten operation.
    """

    #: A constant which can be used with the create_array_index property of a FlattenProjectionPreferences.
    #: This constant has a value of "ALLOW"
    CREATE_ARRAY_INDEX_ALLOW = "ALLOW"

    #: A constant which can be used with the create_array_index property of a FlattenProjectionPreferences.
    #: This constant has a value of "DO_NOT_ALLOW"
    CREATE_ARRAY_INDEX_DO_NOT_ALLOW = "DO_NOT_ALLOW"

    #: A constant which can be used with the retain_all_attributes property of a FlattenProjectionPreferences.
    #: This constant has a value of "ALLOW"
    RETAIN_ALL_ATTRIBUTES_ALLOW = "ALLOW"

    #: A constant which can be used with the retain_all_attributes property of a FlattenProjectionPreferences.
    #: This constant has a value of "DO_NOT_ALLOW"
    RETAIN_ALL_ATTRIBUTES_DO_NOT_ALLOW = "DO_NOT_ALLOW"

    #: A constant which can be used with the ignore_null_values property of a FlattenProjectionPreferences.
    #: This constant has a value of "ALLOW"
    IGNORE_NULL_VALUES_ALLOW = "ALLOW"

    #: A constant which can be used with the ignore_null_values property of a FlattenProjectionPreferences.
    #: This constant has a value of "DO_NOT_ALLOW"
    IGNORE_NULL_VALUES_DO_NOT_ALLOW = "DO_NOT_ALLOW"

    #: A constant which can be used with the retain_parent_name_lineage property of a FlattenProjectionPreferences.
    #: This constant has a value of "ALLOW"
    RETAIN_PARENT_NAME_LINEAGE_ALLOW = "ALLOW"

    #: A constant which can be used with the retain_parent_name_lineage property of a FlattenProjectionPreferences.
    #: This constant has a value of "DO_NOT_ALLOW"
    RETAIN_PARENT_NAME_LINEAGE_DO_NOT_ALLOW = "DO_NOT_ALLOW"

    def __init__(self, **kwargs):
        """
        Initializes a new FlattenProjectionPreferences object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param create_array_index:
            The value to assign to the create_array_index property of this FlattenProjectionPreferences.
            Allowed values for this property are: "ALLOW", "DO_NOT_ALLOW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type create_array_index: str

        :param retain_all_attributes:
            The value to assign to the retain_all_attributes property of this FlattenProjectionPreferences.
            Allowed values for this property are: "ALLOW", "DO_NOT_ALLOW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type retain_all_attributes: str

        :param ignore_null_values:
            The value to assign to the ignore_null_values property of this FlattenProjectionPreferences.
            Allowed values for this property are: "ALLOW", "DO_NOT_ALLOW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type ignore_null_values: str

        :param retain_parent_name_lineage:
            The value to assign to the retain_parent_name_lineage property of this FlattenProjectionPreferences.
            Allowed values for this property are: "ALLOW", "DO_NOT_ALLOW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type retain_parent_name_lineage: str

        """
        self.swagger_types = {
            'create_array_index': 'str',
            'retain_all_attributes': 'str',
            'ignore_null_values': 'str',
            'retain_parent_name_lineage': 'str'
        }

        self.attribute_map = {
            'create_array_index': 'createArrayIndex',
            'retain_all_attributes': 'retainAllAttributes',
            'ignore_null_values': 'ignoreNullValues',
            'retain_parent_name_lineage': 'retainParentNameLineage'
        }

        self._create_array_index = None
        self._retain_all_attributes = None
        self._ignore_null_values = None
        self._retain_parent_name_lineage = None

    @property
    def create_array_index(self):
        """
        **[Required]** Gets the create_array_index of this FlattenProjectionPreferences.
        Property defining whether to create array indexes in flattened result.

        Allowed values for this property are: "ALLOW", "DO_NOT_ALLOW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The create_array_index of this FlattenProjectionPreferences.
        :rtype: str
        """
        return self._create_array_index

    @create_array_index.setter
    def create_array_index(self, create_array_index):
        """
        Sets the create_array_index of this FlattenProjectionPreferences.
        Property defining whether to create array indexes in flattened result.


        :param create_array_index: The create_array_index of this FlattenProjectionPreferences.
        :type: str
        """
        allowed_values = ["ALLOW", "DO_NOT_ALLOW"]
        if not value_allowed_none_or_none_sentinel(create_array_index, allowed_values):
            create_array_index = 'UNKNOWN_ENUM_VALUE'
        self._create_array_index = create_array_index

    @property
    def retain_all_attributes(self):
        """
        **[Required]** Gets the retain_all_attributes of this FlattenProjectionPreferences.
        Property defining whether to retain all attributes in flattened result.

        Allowed values for this property are: "ALLOW", "DO_NOT_ALLOW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The retain_all_attributes of this FlattenProjectionPreferences.
        :rtype: str
        """
        return self._retain_all_attributes

    @retain_all_attributes.setter
    def retain_all_attributes(self, retain_all_attributes):
        """
        Sets the retain_all_attributes of this FlattenProjectionPreferences.
        Property defining whether to retain all attributes in flattened result.


        :param retain_all_attributes: The retain_all_attributes of this FlattenProjectionPreferences.
        :type: str
        """
        allowed_values = ["ALLOW", "DO_NOT_ALLOW"]
        if not value_allowed_none_or_none_sentinel(retain_all_attributes, allowed_values):
            retain_all_attributes = 'UNKNOWN_ENUM_VALUE'
        self._retain_all_attributes = retain_all_attributes

    @property
    def ignore_null_values(self):
        """
        **[Required]** Gets the ignore_null_values of this FlattenProjectionPreferences.
        Property defining whether to ignore null values in flattened result.

        Allowed values for this property are: "ALLOW", "DO_NOT_ALLOW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The ignore_null_values of this FlattenProjectionPreferences.
        :rtype: str
        """
        return self._ignore_null_values

    @ignore_null_values.setter
    def ignore_null_values(self, ignore_null_values):
        """
        Sets the ignore_null_values of this FlattenProjectionPreferences.
        Property defining whether to ignore null values in flattened result.


        :param ignore_null_values: The ignore_null_values of this FlattenProjectionPreferences.
        :type: str
        """
        allowed_values = ["ALLOW", "DO_NOT_ALLOW"]
        if not value_allowed_none_or_none_sentinel(ignore_null_values, allowed_values):
            ignore_null_values = 'UNKNOWN_ENUM_VALUE'
        self._ignore_null_values = ignore_null_values

    @property
    def retain_parent_name_lineage(self):
        """
        **[Required]** Gets the retain_parent_name_lineage of this FlattenProjectionPreferences.
        Property defining whether to retain parent name lineage.

        Allowed values for this property are: "ALLOW", "DO_NOT_ALLOW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The retain_parent_name_lineage of this FlattenProjectionPreferences.
        :rtype: str
        """
        return self._retain_parent_name_lineage

    @retain_parent_name_lineage.setter
    def retain_parent_name_lineage(self, retain_parent_name_lineage):
        """
        Sets the retain_parent_name_lineage of this FlattenProjectionPreferences.
        Property defining whether to retain parent name lineage.


        :param retain_parent_name_lineage: The retain_parent_name_lineage of this FlattenProjectionPreferences.
        :type: str
        """
        allowed_values = ["ALLOW", "DO_NOT_ALLOW"]
        if not value_allowed_none_or_none_sentinel(retain_parent_name_lineage, allowed_values):
            retain_parent_name_lineage = 'UNKNOWN_ENUM_VALUE'
        self._retain_parent_name_lineage = retain_parent_name_lineage

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
