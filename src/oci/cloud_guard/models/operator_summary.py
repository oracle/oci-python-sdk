# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OperatorSummary(object):
    """
    Summary of Operator
    """

    #: A constant which can be used with the filter_type property of a OperatorSummary.
    #: This constant has a value of "CONDITION"
    FILTER_TYPE_CONDITION = "CONDITION"

    #: A constant which can be used with the filter_type property of a OperatorSummary.
    #: This constant has a value of "CONFIG"
    FILTER_TYPE_CONFIG = "CONFIG"

    def __init__(self, **kwargs):
        """
        Initializes a new OperatorSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this OperatorSummary.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this OperatorSummary.
        :type display_name: str

        :param datatype:
            The value to assign to the datatype property of this OperatorSummary.
        :type datatype: str

        :param managed_listtype:
            The value to assign to the managed_listtype property of this OperatorSummary.
        :type managed_listtype: str

        :param filter_type:
            The value to assign to the filter_type property of this OperatorSummary.
            Allowed values for this property are: "CONDITION", "CONFIG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type filter_type: str

        :param operators:
            The value to assign to the operators property of this OperatorSummary.
        :type operators: list[oci.cloud_guard.models.ConditionOperator]

        :param multi_list_types:
            The value to assign to the multi_list_types property of this OperatorSummary.
        :type multi_list_types: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'display_name': 'str',
            'datatype': 'str',
            'managed_listtype': 'str',
            'filter_type': 'str',
            'operators': 'list[ConditionOperator]',
            'multi_list_types': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'display_name': 'displayName',
            'datatype': 'datatype',
            'managed_listtype': 'managedListtype',
            'filter_type': 'filterType',
            'operators': 'operators',
            'multi_list_types': 'multiListTypes'
        }

        self._name = None
        self._display_name = None
        self._datatype = None
        self._managed_listtype = None
        self._filter_type = None
        self._operators = None
        self._multi_list_types = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this OperatorSummary.
        name of the operand


        :return: The name of this OperatorSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OperatorSummary.
        name of the operand


        :param name: The name of this OperatorSummary.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this OperatorSummary.
        display name of the operand


        :return: The display_name of this OperatorSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OperatorSummary.
        display name of the operand


        :param display_name: The display_name of this OperatorSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def datatype(self):
        """
        **[Required]** Gets the datatype of this OperatorSummary.
        data type of operand


        :return: The datatype of this OperatorSummary.
        :rtype: str
        """
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        """
        Sets the datatype of this OperatorSummary.
        data type of operand


        :param datatype: The datatype of this OperatorSummary.
        :type: str
        """
        self._datatype = datatype

    @property
    def managed_listtype(self):
        """
        **[Required]** Gets the managed_listtype of this OperatorSummary.
        operand list type


        :return: The managed_listtype of this OperatorSummary.
        :rtype: str
        """
        return self._managed_listtype

    @managed_listtype.setter
    def managed_listtype(self, managed_listtype):
        """
        Sets the managed_listtype of this OperatorSummary.
        operand list type


        :param managed_listtype: The managed_listtype of this OperatorSummary.
        :type: str
        """
        self._managed_listtype = managed_listtype

    @property
    def filter_type(self):
        """
        **[Required]** Gets the filter_type of this OperatorSummary.
        Filter type can be config filter or condition filter

        Allowed values for this property are: "CONDITION", "CONFIG", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The filter_type of this OperatorSummary.
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """
        Sets the filter_type of this OperatorSummary.
        Filter type can be config filter or condition filter


        :param filter_type: The filter_type of this OperatorSummary.
        :type: str
        """
        allowed_values = ["CONDITION", "CONFIG"]
        if not value_allowed_none_or_none_sentinel(filter_type, allowed_values):
            filter_type = 'UNKNOWN_ENUM_VALUE'
        self._filter_type = filter_type

    @property
    def operators(self):
        """
        **[Required]** Gets the operators of this OperatorSummary.
        List of parameters


        :return: The operators of this OperatorSummary.
        :rtype: list[oci.cloud_guard.models.ConditionOperator]
        """
        return self._operators

    @operators.setter
    def operators(self, operators):
        """
        Sets the operators of this OperatorSummary.
        List of parameters


        :param operators: The operators of this OperatorSummary.
        :type: list[oci.cloud_guard.models.ConditionOperator]
        """
        self._operators = operators

    @property
    def multi_list_types(self):
        """
        Gets the multi_list_types of this OperatorSummary.
        configuration value type list for multilist data type


        :return: The multi_list_types of this OperatorSummary.
        :rtype: list[str]
        """
        return self._multi_list_types

    @multi_list_types.setter
    def multi_list_types(self, multi_list_types):
        """
        Sets the multi_list_types of this OperatorSummary.
        configuration value type list for multilist data type


        :param multi_list_types: The multi_list_types of this OperatorSummary.
        :type: list[str]
        """
        self._multi_list_types = multi_list_types

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
