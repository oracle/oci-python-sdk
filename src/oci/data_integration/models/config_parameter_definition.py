# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigParameterDefinition(object):
    """
    The configurable properties of an object type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigParameterDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param parameter_type:
            The value to assign to the parameter_type property of this ConfigParameterDefinition.
        :type parameter_type: oci.data_integration.models.BaseType

        :param parameter_name:
            The value to assign to the parameter_name property of this ConfigParameterDefinition.
        :type parameter_name: str

        :param description:
            The value to assign to the description property of this ConfigParameterDefinition.
        :type description: str

        :param default_value:
            The value to assign to the default_value property of this ConfigParameterDefinition.
        :type default_value: object

        :param class_field_name:
            The value to assign to the class_field_name property of this ConfigParameterDefinition.
        :type class_field_name: str

        :param is_static:
            The value to assign to the is_static property of this ConfigParameterDefinition.
        :type is_static: bool

        :param is_class_field_value:
            The value to assign to the is_class_field_value property of this ConfigParameterDefinition.
        :type is_class_field_value: bool

        """
        self.swagger_types = {
            'parameter_type': 'BaseType',
            'parameter_name': 'str',
            'description': 'str',
            'default_value': 'object',
            'class_field_name': 'str',
            'is_static': 'bool',
            'is_class_field_value': 'bool'
        }

        self.attribute_map = {
            'parameter_type': 'parameterType',
            'parameter_name': 'parameterName',
            'description': 'description',
            'default_value': 'defaultValue',
            'class_field_name': 'classFieldName',
            'is_static': 'isStatic',
            'is_class_field_value': 'isClassFieldValue'
        }

        self._parameter_type = None
        self._parameter_name = None
        self._description = None
        self._default_value = None
        self._class_field_name = None
        self._is_static = None
        self._is_class_field_value = None

    @property
    def parameter_type(self):
        """
        Gets the parameter_type of this ConfigParameterDefinition.

        :return: The parameter_type of this ConfigParameterDefinition.
        :rtype: oci.data_integration.models.BaseType
        """
        return self._parameter_type

    @parameter_type.setter
    def parameter_type(self, parameter_type):
        """
        Sets the parameter_type of this ConfigParameterDefinition.

        :param parameter_type: The parameter_type of this ConfigParameterDefinition.
        :type: oci.data_integration.models.BaseType
        """
        self._parameter_type = parameter_type

    @property
    def parameter_name(self):
        """
        Gets the parameter_name of this ConfigParameterDefinition.
        This object represents the configurable properties for an object type.


        :return: The parameter_name of this ConfigParameterDefinition.
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        """
        Sets the parameter_name of this ConfigParameterDefinition.
        This object represents the configurable properties for an object type.


        :param parameter_name: The parameter_name of this ConfigParameterDefinition.
        :type: str
        """
        self._parameter_name = parameter_name

    @property
    def description(self):
        """
        Gets the description of this ConfigParameterDefinition.
        A user defined description for the object.


        :return: The description of this ConfigParameterDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ConfigParameterDefinition.
        A user defined description for the object.


        :param description: The description of this ConfigParameterDefinition.
        :type: str
        """
        self._description = description

    @property
    def default_value(self):
        """
        Gets the default_value of this ConfigParameterDefinition.
        The default value for the parameter.


        :return: The default_value of this ConfigParameterDefinition.
        :rtype: object
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this ConfigParameterDefinition.
        The default value for the parameter.


        :param default_value: The default_value of this ConfigParameterDefinition.
        :type: object
        """
        self._default_value = default_value

    @property
    def class_field_name(self):
        """
        Gets the class_field_name of this ConfigParameterDefinition.
        The parameter class field name.


        :return: The class_field_name of this ConfigParameterDefinition.
        :rtype: str
        """
        return self._class_field_name

    @class_field_name.setter
    def class_field_name(self, class_field_name):
        """
        Sets the class_field_name of this ConfigParameterDefinition.
        The parameter class field name.


        :param class_field_name: The class_field_name of this ConfigParameterDefinition.
        :type: str
        """
        self._class_field_name = class_field_name

    @property
    def is_static(self):
        """
        Gets the is_static of this ConfigParameterDefinition.
        Specifies whether the parameter is static or not.


        :return: The is_static of this ConfigParameterDefinition.
        :rtype: bool
        """
        return self._is_static

    @is_static.setter
    def is_static(self, is_static):
        """
        Sets the is_static of this ConfigParameterDefinition.
        Specifies whether the parameter is static or not.


        :param is_static: The is_static of this ConfigParameterDefinition.
        :type: bool
        """
        self._is_static = is_static

    @property
    def is_class_field_value(self):
        """
        Gets the is_class_field_value of this ConfigParameterDefinition.
        Specifies whether the parameter is a class field or not.


        :return: The is_class_field_value of this ConfigParameterDefinition.
        :rtype: bool
        """
        return self._is_class_field_value

    @is_class_field_value.setter
    def is_class_field_value(self, is_class_field_value):
        """
        Sets the is_class_field_value of this ConfigParameterDefinition.
        Specifies whether the parameter is a class field or not.


        :param is_class_field_value: The is_class_field_value of this ConfigParameterDefinition.
        :type: bool
        """
        self._is_class_field_value = is_class_field_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
