# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190801


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Recurrence(object):
    """
    An object for representing a recurrence time interval
    """

    #: A constant which can be used with the interval_type property of a Recurrence.
    #: This constant has a value of "MINUTES"
    INTERVAL_TYPE_MINUTES = "MINUTES"

    #: A constant which can be used with the interval_type property of a Recurrence.
    #: This constant has a value of "HOURS"
    INTERVAL_TYPE_HOURS = "HOURS"

    #: A constant which can be used with the interval_type property of a Recurrence.
    #: This constant has a value of "DAYS"
    INTERVAL_TYPE_DAYS = "DAYS"

    #: A constant which can be used with the interval_type property of a Recurrence.
    #: This constant has a value of "WEEKS"
    INTERVAL_TYPE_WEEKS = "WEEKS"

    def __init__(self, **kwargs):
        """
        Initializes a new Recurrence object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param interval_type:
            The value to assign to the interval_type property of this Recurrence.
            Allowed values for this property are: "MINUTES", "HOURS", "DAYS", "WEEKS"
        :type interval_type: str

        :param interval_value:
            The value to assign to the interval_value property of this Recurrence.
        :type interval_value: str

        """
        self.swagger_types = {
            'interval_type': 'str',
            'interval_value': 'str'
        }
        self.attribute_map = {
            'interval_type': 'intervalType',
            'interval_value': 'intervalValue'
        }
        self._interval_type = None
        self._interval_value = None

    @property
    def interval_type(self):
        """
        **[Required]** Gets the interval_type of this Recurrence.
        the interval period for the recurrence

        Allowed values for this property are: "MINUTES", "HOURS", "DAYS", "WEEKS"


        :return: The interval_type of this Recurrence.
        :rtype: str
        """
        return self._interval_type

    @interval_type.setter
    def interval_type(self, interval_type):
        """
        Sets the interval_type of this Recurrence.
        the interval period for the recurrence


        :param interval_type: The interval_type of this Recurrence.
        :type: str
        """
        allowed_values = ["MINUTES", "HOURS", "DAYS", "WEEKS"]
        if not value_allowed_none_or_none_sentinel(interval_type, allowed_values):
            raise ValueError(
                f"Invalid value for `interval_type`, must be None or one of {allowed_values}"
            )
        self._interval_type = interval_type

    @property
    def interval_value(self):
        """
        **[Required]** Gets the interval_value of this Recurrence.
        the value for the interval period for the recurrence


        :return: The interval_value of this Recurrence.
        :rtype: str
        """
        return self._interval_value

    @interval_value.setter
    def interval_value(self, interval_value):
        """
        Sets the interval_value of this Recurrence.
        the value for the interval period for the recurrence


        :param interval_value: The interval_value of this Recurrence.
        :type: str
        """
        self._interval_value = interval_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
