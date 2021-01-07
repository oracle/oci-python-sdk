# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProblemAggregation(object):
    """
    Provides the dimensions and their corresponding count value.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProblemAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dimensions_map:
            The value to assign to the dimensions_map property of this ProblemAggregation.
        :type dimensions_map: dict(str, str)

        :param count:
            The value to assign to the count property of this ProblemAggregation.
        :type count: int

        """
        self.swagger_types = {
            'dimensions_map': 'dict(str, str)',
            'count': 'int'
        }

        self.attribute_map = {
            'dimensions_map': 'dimensionsMap',
            'count': 'count'
        }

        self._dimensions_map = None
        self._count = None

    @property
    def dimensions_map(self):
        """
        **[Required]** Gets the dimensions_map of this ProblemAggregation.
        The key-value pairs of dimensions and their names.


        :return: The dimensions_map of this ProblemAggregation.
        :rtype: dict(str, str)
        """
        return self._dimensions_map

    @dimensions_map.setter
    def dimensions_map(self, dimensions_map):
        """
        Sets the dimensions_map of this ProblemAggregation.
        The key-value pairs of dimensions and their names.


        :param dimensions_map: The dimensions_map of this ProblemAggregation.
        :type: dict(str, str)
        """
        self._dimensions_map = dimensions_map

    @property
    def count(self):
        """
        **[Required]** Gets the count of this ProblemAggregation.
        The number of occurences with given dimension/s


        :return: The count of this ProblemAggregation.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this ProblemAggregation.
        The number of occurences with given dimension/s


        :param count: The count of this ProblemAggregation.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
