# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DayOfWeek(object):
    """
    Day of the week.
    """

    #: A constant which can be used with the name property of a DayOfWeek.
    #: This constant has a value of "MONDAY"
    NAME_MONDAY = "MONDAY"

    #: A constant which can be used with the name property of a DayOfWeek.
    #: This constant has a value of "TUESDAY"
    NAME_TUESDAY = "TUESDAY"

    #: A constant which can be used with the name property of a DayOfWeek.
    #: This constant has a value of "WEDNESDAY"
    NAME_WEDNESDAY = "WEDNESDAY"

    #: A constant which can be used with the name property of a DayOfWeek.
    #: This constant has a value of "THURSDAY"
    NAME_THURSDAY = "THURSDAY"

    #: A constant which can be used with the name property of a DayOfWeek.
    #: This constant has a value of "FRIDAY"
    NAME_FRIDAY = "FRIDAY"

    #: A constant which can be used with the name property of a DayOfWeek.
    #: This constant has a value of "SATURDAY"
    NAME_SATURDAY = "SATURDAY"

    #: A constant which can be used with the name property of a DayOfWeek.
    #: This constant has a value of "SUNDAY"
    NAME_SUNDAY = "SUNDAY"

    def __init__(self, **kwargs):
        """
        Initializes a new DayOfWeek object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this DayOfWeek.
            Allowed values for this property are: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type name: str

        """
        self.swagger_types = {
            'name': 'str'
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DayOfWeek.
        Name of the day of the week.

        Allowed values for this property are: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The name of this DayOfWeek.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DayOfWeek.
        Name of the day of the week.


        :param name: The name of this DayOfWeek.
        :type: str
        """
        allowed_values = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        if not value_allowed_none_or_none_sentinel(name, allowed_values):
            name = 'UNKNOWN_ENUM_VALUE'
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
