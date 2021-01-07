# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OrchestrationVariable(object):
    """
    The model of a variable for an orchestration resource.
    """

    #: A constant which can be used with the data_type property of a OrchestrationVariable.
    #: This constant has a value of "STRING"
    DATA_TYPE_STRING = "STRING"

    #: A constant which can be used with the data_type property of a OrchestrationVariable.
    #: This constant has a value of "INTEGER"
    DATA_TYPE_INTEGER = "INTEGER"

    def __init__(self, **kwargs):
        """
        Initializes a new OrchestrationVariable object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this OrchestrationVariable.
        :type name: str

        :param default_value:
            The value to assign to the default_value property of this OrchestrationVariable.
        :type default_value: str

        :param description:
            The value to assign to the description property of this OrchestrationVariable.
        :type description: str

        :param data_type:
            The value to assign to the data_type property of this OrchestrationVariable.
            Allowed values for this property are: "STRING", "INTEGER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_type: str

        :param is_mandatory:
            The value to assign to the is_mandatory property of this OrchestrationVariable.
        :type is_mandatory: bool

        :param hint_message:
            The value to assign to the hint_message property of this OrchestrationVariable.
        :type hint_message: str

        """
        self.swagger_types = {
            'name': 'str',
            'default_value': 'str',
            'description': 'str',
            'data_type': 'str',
            'is_mandatory': 'bool',
            'hint_message': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'default_value': 'defaultValue',
            'description': 'description',
            'data_type': 'dataType',
            'is_mandatory': 'isMandatory',
            'hint_message': 'hintMessage'
        }

        self._name = None
        self._default_value = None
        self._description = None
        self._data_type = None
        self._is_mandatory = None
        self._hint_message = None

    @property
    def name(self):
        """
        Gets the name of this OrchestrationVariable.
        The name of the variable.


        :return: The name of this OrchestrationVariable.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OrchestrationVariable.
        The name of the variable.


        :param name: The name of this OrchestrationVariable.
        :type: str
        """
        self._name = name

    @property
    def default_value(self):
        """
        Gets the default_value of this OrchestrationVariable.
        The variable's default value.


        :return: The default_value of this OrchestrationVariable.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this OrchestrationVariable.
        The variable's default value.


        :param default_value: The default_value of this OrchestrationVariable.
        :type: str
        """
        self._default_value = default_value

    @property
    def description(self):
        """
        Gets the description of this OrchestrationVariable.
        A description of the variable.


        :return: The description of this OrchestrationVariable.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OrchestrationVariable.
        A description of the variable.


        :param description: The description of this OrchestrationVariable.
        :type: str
        """
        self._description = description

    @property
    def data_type(self):
        """
        Gets the data_type of this OrchestrationVariable.
        The data type of the variable.

        Allowed values for this property are: "STRING", "INTEGER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_type of this OrchestrationVariable.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this OrchestrationVariable.
        The data type of the variable.


        :param data_type: The data_type of this OrchestrationVariable.
        :type: str
        """
        allowed_values = ["STRING", "INTEGER"]
        if not value_allowed_none_or_none_sentinel(data_type, allowed_values):
            data_type = 'UNKNOWN_ENUM_VALUE'
        self._data_type = data_type

    @property
    def is_mandatory(self):
        """
        Gets the is_mandatory of this OrchestrationVariable.
        Whether the variable is mandatory.


        :return: The is_mandatory of this OrchestrationVariable.
        :rtype: bool
        """
        return self._is_mandatory

    @is_mandatory.setter
    def is_mandatory(self, is_mandatory):
        """
        Sets the is_mandatory of this OrchestrationVariable.
        Whether the variable is mandatory.


        :param is_mandatory: The is_mandatory of this OrchestrationVariable.
        :type: bool
        """
        self._is_mandatory = is_mandatory

    @property
    def hint_message(self):
        """
        Gets the hint_message of this OrchestrationVariable.
        A brief textual description that helps to explain the variable.


        :return: The hint_message of this OrchestrationVariable.
        :rtype: str
        """
        return self._hint_message

    @hint_message.setter
    def hint_message(self, hint_message):
        """
        Sets the hint_message of this OrchestrationVariable.
        A brief textual description that helps to explain the variable.


        :param hint_message: The hint_message of this OrchestrationVariable.
        :type: str
        """
        self._hint_message = hint_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
