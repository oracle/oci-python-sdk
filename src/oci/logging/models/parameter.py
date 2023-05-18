# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
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

    #: A constant which can be used with the type property of a Parameter.
    #: This constant has a value of "ENUM_STRING"
    TYPE_ENUM_STRING = "ENUM_STRING"

    #: A constant which can be used with the type property of a Parameter.
    #: This constant has a value of "RQS_FILTER"
    TYPE_RQS_FILTER = "RQS_FILTER"

    def __init__(self, **kwargs):
        """
        Initializes a new Parameter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Parameter.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this Parameter.
        :type display_name: str

        :param type:
            The value to assign to the type property of this Parameter.
            Allowed values for this property are: "integer", "string", "boolean", "ENUM_STRING", "RQS_FILTER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param rqs_type:
            The value to assign to the rqs_type property of this Parameter.
        :type rqs_type: str

        :param pattern:
            The value to assign to the pattern property of this Parameter.
        :type pattern: str

        """
        self.swagger_types = {
            'name': 'str',
            'display_name': 'str',
            'type': 'str',
            'rqs_type': 'str',
            'pattern': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'display_name': 'displayName',
            'type': 'type',
            'rqs_type': 'rqsType',
            'pattern': 'pattern'
        }

        self._name = None
        self._display_name = None
        self._type = None
        self._rqs_type = None
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
    def display_name(self):
        """
        Gets the display_name of this Parameter.
        The user-friendly display name. This must be unique within the enclosing resource,
        and it's changeable. Avoid entering confidential information.


        :return: The display_name of this Parameter.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Parameter.
        The user-friendly display name. This must be unique within the enclosing resource,
        and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this Parameter.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Parameter.
        Parameter type.

        Allowed values for this property are: "integer", "string", "boolean", "ENUM_STRING", "RQS_FILTER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Parameter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Parameter.
        Parameter type.


        :param type: The type of this Parameter.
        :type: str
        """
        allowed_values = ["integer", "string", "boolean", "ENUM_STRING", "RQS_FILTER"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def rqs_type(self):
        """
        Gets the rqs_type of this Parameter.
        Parameter rqsType if applicable.


        :return: The rqs_type of this Parameter.
        :rtype: str
        """
        return self._rqs_type

    @rqs_type.setter
    def rqs_type(self, rqs_type):
        """
        Sets the rqs_type of this Parameter.
        Parameter rqsType if applicable.


        :param rqs_type: The rqs_type of this Parameter.
        :type: str
        """
        self._rqs_type = rqs_type

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
