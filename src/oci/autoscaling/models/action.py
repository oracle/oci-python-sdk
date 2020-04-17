# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Action(object):
    """
    The action to take when autoscaling is triggered.
    """

    #: A constant which can be used with the type property of a Action.
    #: This constant has a value of "CHANGE_COUNT_BY"
    TYPE_CHANGE_COUNT_BY = "CHANGE_COUNT_BY"

    def __init__(self, **kwargs):
        """
        Initializes a new Action object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this Action.
            Allowed values for this property are: "CHANGE_COUNT_BY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param value:
            The value to assign to the value property of this Action.
        :type value: int

        """
        self.swagger_types = {
            'type': 'str',
            'value': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'value': 'value'
        }

        self._type = None
        self._value = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Action.
        The type of action to take.

        Allowed values for this property are: "CHANGE_COUNT_BY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Action.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Action.
        The type of action to take.


        :param type: The type of this Action.
        :type: str
        """
        allowed_values = ["CHANGE_COUNT_BY"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def value(self):
        """
        **[Required]** Gets the value of this Action.
        To scale out (increase the number of instances), provide a positive value. To scale in (decrease the number of
        instances), provide a negative value.


        :return: The value of this Action.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Action.
        To scale out (increase the number of instances), provide a positive value. To scale in (decrease the number of
        instances), provide a negative value.


        :param value: The value of this Action.
        :type: int
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
