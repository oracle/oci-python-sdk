# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SchemaDriftConfig(object):
    """
    The configuration for handling schema drift in a Source or Target operator.
    """

    #: A constant which can be used with the extra_column_handling property of a SchemaDriftConfig.
    #: This constant has a value of "ALLOW"
    EXTRA_COLUMN_HANDLING_ALLOW = "ALLOW"

    #: A constant which can be used with the extra_column_handling property of a SchemaDriftConfig.
    #: This constant has a value of "NULL_FILLUP"
    EXTRA_COLUMN_HANDLING_NULL_FILLUP = "NULL_FILLUP"

    #: A constant which can be used with the extra_column_handling property of a SchemaDriftConfig.
    #: This constant has a value of "DO_NOT_ALLOW"
    EXTRA_COLUMN_HANDLING_DO_NOT_ALLOW = "DO_NOT_ALLOW"

    #: A constant which can be used with the missing_column_handling property of a SchemaDriftConfig.
    #: This constant has a value of "ALLOW"
    MISSING_COLUMN_HANDLING_ALLOW = "ALLOW"

    #: A constant which can be used with the missing_column_handling property of a SchemaDriftConfig.
    #: This constant has a value of "NULL_SELECT"
    MISSING_COLUMN_HANDLING_NULL_SELECT = "NULL_SELECT"

    #: A constant which can be used with the missing_column_handling property of a SchemaDriftConfig.
    #: This constant has a value of "DO_NOT_ALLOW"
    MISSING_COLUMN_HANDLING_DO_NOT_ALLOW = "DO_NOT_ALLOW"

    #: A constant which can be used with the data_type_change_handling property of a SchemaDriftConfig.
    #: This constant has a value of "ALLOW"
    DATA_TYPE_CHANGE_HANDLING_ALLOW = "ALLOW"

    #: A constant which can be used with the data_type_change_handling property of a SchemaDriftConfig.
    #: This constant has a value of "DO_CAST_IF_POSSIBLE"
    DATA_TYPE_CHANGE_HANDLING_DO_CAST_IF_POSSIBLE = "DO_CAST_IF_POSSIBLE"

    #: A constant which can be used with the data_type_change_handling property of a SchemaDriftConfig.
    #: This constant has a value of "DO_NOT_ALLOW"
    DATA_TYPE_CHANGE_HANDLING_DO_NOT_ALLOW = "DO_NOT_ALLOW"

    def __init__(self, **kwargs):
        """
        Initializes a new SchemaDriftConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param extra_column_handling:
            The value to assign to the extra_column_handling property of this SchemaDriftConfig.
            Allowed values for this property are: "ALLOW", "NULL_FILLUP", "DO_NOT_ALLOW"
        :type extra_column_handling: str

        :param missing_column_handling:
            The value to assign to the missing_column_handling property of this SchemaDriftConfig.
            Allowed values for this property are: "ALLOW", "NULL_SELECT", "DO_NOT_ALLOW"
        :type missing_column_handling: str

        :param data_type_change_handling:
            The value to assign to the data_type_change_handling property of this SchemaDriftConfig.
            Allowed values for this property are: "ALLOW", "DO_CAST_IF_POSSIBLE", "DO_NOT_ALLOW"
        :type data_type_change_handling: str

        :param is_validation_warning_if_allowed:
            The value to assign to the is_validation_warning_if_allowed property of this SchemaDriftConfig.
        :type is_validation_warning_if_allowed: bool

        """
        self.swagger_types = {
            'extra_column_handling': 'str',
            'missing_column_handling': 'str',
            'data_type_change_handling': 'str',
            'is_validation_warning_if_allowed': 'bool'
        }

        self.attribute_map = {
            'extra_column_handling': 'extraColumnHandling',
            'missing_column_handling': 'missingColumnHandling',
            'data_type_change_handling': 'dataTypeChangeHandling',
            'is_validation_warning_if_allowed': 'isValidationWarningIfAllowed'
        }

        self._extra_column_handling = None
        self._missing_column_handling = None
        self._data_type_change_handling = None
        self._is_validation_warning_if_allowed = None

    @property
    def extra_column_handling(self):
        """
        Gets the extra_column_handling of this SchemaDriftConfig.
        The setting to handle extra columns/fields.  NULL_FILLUP means that nulls will be loaded into the target for extra columns.

        Allowed values for this property are: "ALLOW", "NULL_FILLUP", "DO_NOT_ALLOW"


        :return: The extra_column_handling of this SchemaDriftConfig.
        :rtype: str
        """
        return self._extra_column_handling

    @extra_column_handling.setter
    def extra_column_handling(self, extra_column_handling):
        """
        Sets the extra_column_handling of this SchemaDriftConfig.
        The setting to handle extra columns/fields.  NULL_FILLUP means that nulls will be loaded into the target for extra columns.


        :param extra_column_handling: The extra_column_handling of this SchemaDriftConfig.
        :type: str
        """
        allowed_values = ["ALLOW", "NULL_FILLUP", "DO_NOT_ALLOW"]
        if not value_allowed_none_or_none_sentinel(extra_column_handling, allowed_values):
            raise ValueError(
                "Invalid value for `extra_column_handling`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._extra_column_handling = extra_column_handling

    @property
    def missing_column_handling(self):
        """
        Gets the missing_column_handling of this SchemaDriftConfig.
        The setting to handle missing columns/fields.  NULL_SELECT means that null values will be selected from the source for missing columns.

        Allowed values for this property are: "ALLOW", "NULL_SELECT", "DO_NOT_ALLOW"


        :return: The missing_column_handling of this SchemaDriftConfig.
        :rtype: str
        """
        return self._missing_column_handling

    @missing_column_handling.setter
    def missing_column_handling(self, missing_column_handling):
        """
        Sets the missing_column_handling of this SchemaDriftConfig.
        The setting to handle missing columns/fields.  NULL_SELECT means that null values will be selected from the source for missing columns.


        :param missing_column_handling: The missing_column_handling of this SchemaDriftConfig.
        :type: str
        """
        allowed_values = ["ALLOW", "NULL_SELECT", "DO_NOT_ALLOW"]
        if not value_allowed_none_or_none_sentinel(missing_column_handling, allowed_values):
            raise ValueError(
                "Invalid value for `missing_column_handling`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._missing_column_handling = missing_column_handling

    @property
    def data_type_change_handling(self):
        """
        Gets the data_type_change_handling of this SchemaDriftConfig.
        The setting to handle columns/fields with changed data types.

        Allowed values for this property are: "ALLOW", "DO_CAST_IF_POSSIBLE", "DO_NOT_ALLOW"


        :return: The data_type_change_handling of this SchemaDriftConfig.
        :rtype: str
        """
        return self._data_type_change_handling

    @data_type_change_handling.setter
    def data_type_change_handling(self, data_type_change_handling):
        """
        Sets the data_type_change_handling of this SchemaDriftConfig.
        The setting to handle columns/fields with changed data types.


        :param data_type_change_handling: The data_type_change_handling of this SchemaDriftConfig.
        :type: str
        """
        allowed_values = ["ALLOW", "DO_CAST_IF_POSSIBLE", "DO_NOT_ALLOW"]
        if not value_allowed_none_or_none_sentinel(data_type_change_handling, allowed_values):
            raise ValueError(
                "Invalid value for `data_type_change_handling`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._data_type_change_handling = data_type_change_handling

    @property
    def is_validation_warning_if_allowed(self):
        """
        Gets the is_validation_warning_if_allowed of this SchemaDriftConfig.
        If true, display a validation warning for schema changes, even if they are allowed.


        :return: The is_validation_warning_if_allowed of this SchemaDriftConfig.
        :rtype: bool
        """
        return self._is_validation_warning_if_allowed

    @is_validation_warning_if_allowed.setter
    def is_validation_warning_if_allowed(self, is_validation_warning_if_allowed):
        """
        Sets the is_validation_warning_if_allowed of this SchemaDriftConfig.
        If true, display a validation warning for schema changes, even if they are allowed.


        :param is_validation_warning_if_allowed: The is_validation_warning_if_allowed of this SchemaDriftConfig.
        :type: bool
        """
        self._is_validation_warning_if_allowed = is_validation_warning_if_allowed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
