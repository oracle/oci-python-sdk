# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Indexes(object):
    """
    Indexes
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Indexes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param end_index:
            The value to assign to the end_index property of this Indexes.
        :type end_index: int

        :param start_index:
            The value to assign to the start_index property of this Indexes.
        :type start_index: int

        """
        self.swagger_types = {
            'end_index': 'int',
            'start_index': 'int'
        }

        self.attribute_map = {
            'end_index': 'endIndex',
            'start_index': 'startIndex'
        }

        self._end_index = None
        self._start_index = None

    @property
    def end_index(self):
        """
        Gets the end_index of this Indexes.
        The end index.


        :return: The end_index of this Indexes.
        :rtype: int
        """
        return self._end_index

    @end_index.setter
    def end_index(self, end_index):
        """
        Sets the end_index of this Indexes.
        The end index.


        :param end_index: The end_index of this Indexes.
        :type: int
        """
        self._end_index = end_index

    @property
    def start_index(self):
        """
        Gets the start_index of this Indexes.
        The start index.


        :return: The start_index of this Indexes.
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """
        Sets the start_index of this Indexes.
        The start index.


        :param start_index: The start_index of this Indexes.
        :type: int
        """
        self._start_index = start_index

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
