# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Capacity(object):
    """
    Service instance capacity metadata (e.g.: OLPU count, number of users, ...etc...).
    """

    #: A constant which can be used with the capacity_type property of a Capacity.
    #: This constant has a value of "OLPU_COUNT"
    CAPACITY_TYPE_OLPU_COUNT = "OLPU_COUNT"

    #: A constant which can be used with the capacity_type property of a Capacity.
    #: This constant has a value of "USER_COUNT"
    CAPACITY_TYPE_USER_COUNT = "USER_COUNT"

    def __init__(self, **kwargs):
        """
        Initializes a new Capacity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param capacity_type:
            The value to assign to the capacity_type property of this Capacity.
            Allowed values for this property are: "OLPU_COUNT", "USER_COUNT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type capacity_type: str

        :param capacity_value:
            The value to assign to the capacity_value property of this Capacity.
        :type capacity_value: int

        """
        self.swagger_types = {
            'capacity_type': 'str',
            'capacity_value': 'int'
        }

        self.attribute_map = {
            'capacity_type': 'capacityType',
            'capacity_value': 'capacityValue'
        }

        self._capacity_type = None
        self._capacity_value = None

    @property
    def capacity_type(self):
        """
        **[Required]** Gets the capacity_type of this Capacity.
        The capacity model to use.

        Allowed values for this property are: "OLPU_COUNT", "USER_COUNT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The capacity_type of this Capacity.
        :rtype: str
        """
        return self._capacity_type

    @capacity_type.setter
    def capacity_type(self, capacity_type):
        """
        Sets the capacity_type of this Capacity.
        The capacity model to use.


        :param capacity_type: The capacity_type of this Capacity.
        :type: str
        """
        allowed_values = ["OLPU_COUNT", "USER_COUNT"]
        if not value_allowed_none_or_none_sentinel(capacity_type, allowed_values):
            capacity_type = 'UNKNOWN_ENUM_VALUE'
        self._capacity_type = capacity_type

    @property
    def capacity_value(self):
        """
        **[Required]** Gets the capacity_value of this Capacity.
        The capacity value selected (OLPU count, number of users, ...etc...). This parameter affects the
        number of CPUs, amount of memory or other resources allocated to the instance.


        :return: The capacity_value of this Capacity.
        :rtype: int
        """
        return self._capacity_value

    @capacity_value.setter
    def capacity_value(self, capacity_value):
        """
        Sets the capacity_value of this Capacity.
        The capacity value selected (OLPU count, number of users, ...etc...). This parameter affects the
        number of CPUs, amount of memory or other resources allocated to the instance.


        :param capacity_value: The capacity_value of this Capacity.
        :type: int
        """
        self._capacity_value = capacity_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
