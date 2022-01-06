# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Parameter(object):
    """
    Parameters that a resource category supports.
    """

    #: A constant which can be used with the type property of a Parameter.
    #: This constant has a value of "integer"
    TYPE_INTEGER = "integer"

    #: A constant which can be used with the type property of a Parameter.
    #: This constant has a value of "string"
    TYPE_STRING = "string"

    #: A constant which can be used with the type property of a Parameter.
    #: This constant has a value of "boolean"
    TYPE_BOOLEAN = "boolean"

    def __init__(self, **kwargs):
        """
        Initializes a new Parameter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Parameter.
        :type name: str

        :param type:
            The value to assign to the type property of this Parameter.
            Allowed values for this property are: "integer", "string", "boolean", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param pattern:
            The value to assign to the pattern property of this Parameter.
        :type pattern: str

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'pattern': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'pattern': 'pattern'
        }

        self._name = None
        self._type = None
        self._pattern = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Parameter.
        Parameter name.


        :return: The name of this Parameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Parameter.
        Parameter name.


        :param name: The name of this Parameter.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Parameter.
        Parameter type. One of integer, string, boolean.

        Allowed values for this property are: "integer", "string", "boolean", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Parameter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Parameter.
        Parameter type. One of integer, string, boolean.


        :param type: The type of this Parameter.
        :type: str
        """
        allowed_values = ["integer", "string", "boolean"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def pattern(self):
        """
        Gets the pattern of this Parameter.
        Java regex pattern to validate a parameter value.


        :return: The pattern of this Parameter.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this Parameter.
        Java regex pattern to validate a parameter value.


        :param pattern: The pattern of this Parameter.
        :type: str
        """
        self._pattern = pattern

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
