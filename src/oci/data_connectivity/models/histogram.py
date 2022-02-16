# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Histogram(object):
    """
    To capture all the histograms data related to profiling
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Histogram object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ranges:
            The value to assign to the ranges property of this Histogram.
        :type ranges: list[str]

        :param counts:
            The value to assign to the counts property of this Histogram.
        :type counts: list[int]

        """
        self.swagger_types = {
            'ranges': 'list[str]',
            'counts': 'list[int]'
        }

        self.attribute_map = {
            'ranges': 'ranges',
            'counts': 'counts'
        }

        self._ranges = None
        self._counts = None

    @property
    def ranges(self):
        """
        Gets the ranges of this Histogram.
        Range of values


        :return: The ranges of this Histogram.
        :rtype: list[str]
        """
        return self._ranges

    @ranges.setter
    def ranges(self, ranges):
        """
        Sets the ranges of this Histogram.
        Range of values


        :param ranges: The ranges of this Histogram.
        :type: list[str]
        """
        self._ranges = ranges

    @property
    def counts(self):
        """
        Gets the counts of this Histogram.
        Count of each ranges.


        :return: The counts of this Histogram.
        :rtype: list[int]
        """
        return self._counts

    @counts.setter
    def counts(self, counts):
        """
        Sets the counts of this Histogram.
        Count of each ranges.


        :param counts: The counts of this Histogram.
        :type: list[int]
        """
        self._counts = counts

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
