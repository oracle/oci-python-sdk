# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Month(object):
    """
    Month of the year.
    """

    #: A constant which can be used with the name property of a Month.
    #: This constant has a value of "JANUARY"
    NAME_JANUARY = "JANUARY"

    #: A constant which can be used with the name property of a Month.
    #: This constant has a value of "FEBRUARY"
    NAME_FEBRUARY = "FEBRUARY"

    #: A constant which can be used with the name property of a Month.
    #: This constant has a value of "MARCH"
    NAME_MARCH = "MARCH"

    #: A constant which can be used with the name property of a Month.
    #: This constant has a value of "APRIL"
    NAME_APRIL = "APRIL"

    #: A constant which can be used with the name property of a Month.
    #: This constant has a value of "MAY"
    NAME_MAY = "MAY"

    #: A constant which can be used with the name property of a Month.
    #: This constant has a value of "JUNE"
    NAME_JUNE = "JUNE"

    #: A constant which can be used with the name property of a Month.
    #: This constant has a value of "JULY"
    NAME_JULY = "JULY"

    #: A constant which can be used with the name property of a Month.
    #: This constant has a value of "AUGUST"
    NAME_AUGUST = "AUGUST"

    #: A constant which can be used with the name property of a Month.
    #: This constant has a value of "SEPTEMBER"
    NAME_SEPTEMBER = "SEPTEMBER"

    #: A constant which can be used with the name property of a Month.
    #: This constant has a value of "OCTOBER"
    NAME_OCTOBER = "OCTOBER"

    #: A constant which can be used with the name property of a Month.
    #: This constant has a value of "NOVEMBER"
    NAME_NOVEMBER = "NOVEMBER"

    #: A constant which can be used with the name property of a Month.
    #: This constant has a value of "DECEMBER"
    NAME_DECEMBER = "DECEMBER"

    def __init__(self, **kwargs):
        """
        Initializes a new Month object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Month.
            Allowed values for this property are: "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER", 'UNKNOWN_ENUM_VALUE'.
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
        **[Required]** Gets the name of this Month.
        Name of the month of the year.

        Allowed values for this property are: "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The name of this Month.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Month.
        Name of the month of the year.


        :param name: The name of this Month.
        :type: str
        """
        allowed_values = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
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
