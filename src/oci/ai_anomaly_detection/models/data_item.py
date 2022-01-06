# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataItem(object):
    """
    Simple object representing signal values at a certain point in time.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataItem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param timestamp:
            The value to assign to the timestamp property of this DataItem.
        :type timestamp: datetime

        :param values:
            The value to assign to the values property of this DataItem.
        :type values: list[float]

        """
        self.swagger_types = {
            'timestamp': 'datetime',
            'values': 'list[float]'
        }

        self.attribute_map = {
            'timestamp': 'timestamp',
            'values': 'values'
        }

        self._timestamp = None
        self._values = None

    @property
    def timestamp(self):
        """
        Gets the timestamp of this DataItem.
        Nullable string representing timestamp.


        :return: The timestamp of this DataItem.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this DataItem.
        Nullable string representing timestamp.


        :param timestamp: The timestamp of this DataItem.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def values(self):
        """
        **[Required]** Gets the values of this DataItem.
        Array of double precision values.


        :return: The values of this DataItem.
        :rtype: list[float]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this DataItem.
        Array of double precision values.


        :param values: The values of this DataItem.
        :type: list[float]
        """
        self._values = values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
