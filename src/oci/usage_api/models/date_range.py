# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DateRange(object):
    """
    Static or dynamic date range `dateRangeType`,
    which corresponds with type-specific characteristics.
    """

    #: A constant which can be used with the date_range_type property of a DateRange.
    #: This constant has a value of "STATIC"
    DATE_RANGE_TYPE_STATIC = "STATIC"

    #: A constant which can be used with the date_range_type property of a DateRange.
    #: This constant has a value of "DYNAMIC"
    DATE_RANGE_TYPE_DYNAMIC = "DYNAMIC"

    def __init__(self, **kwargs):
        """
        Initializes a new DateRange object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.usage_api.models.StaticDateRange`
        * :class:`~oci.usage_api.models.DynamicDateRange`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param date_range_type:
            The value to assign to the date_range_type property of this DateRange.
            Allowed values for this property are: "STATIC", "DYNAMIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type date_range_type: str

        """
        self.swagger_types = {
            'date_range_type': 'str'
        }

        self.attribute_map = {
            'date_range_type': 'dateRangeType'
        }

        self._date_range_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['dateRangeType']

        if type == 'STATIC':
            return 'StaticDateRange'

        if type == 'DYNAMIC':
            return 'DynamicDateRange'
        else:
            return 'DateRange'

    @property
    def date_range_type(self):
        """
        **[Required]** Gets the date_range_type of this DateRange.
        Defines whether the schedule date range is STATIC or DYNAMIC

        Allowed values for this property are: "STATIC", "DYNAMIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The date_range_type of this DateRange.
        :rtype: str
        """
        return self._date_range_type

    @date_range_type.setter
    def date_range_type(self, date_range_type):
        """
        Sets the date_range_type of this DateRange.
        Defines whether the schedule date range is STATIC or DYNAMIC


        :param date_range_type: The date_range_type of this DateRange.
        :type: str
        """
        allowed_values = ["STATIC", "DYNAMIC"]
        if not value_allowed_none_or_none_sentinel(date_range_type, allowed_values):
            date_range_type = 'UNKNOWN_ENUM_VALUE'
        self._date_range_type = date_range_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
