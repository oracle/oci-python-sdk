# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SearchResultSummary(object):
    """
    Summary of results.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SearchResultSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param result_count:
            The value to assign to the result_count property of this SearchResultSummary.
        :type result_count: int

        :param field_count:
            The value to assign to the field_count property of this SearchResultSummary.
        :type field_count: int

        """
        self.swagger_types = {
            'result_count': 'int',
            'field_count': 'int'
        }

        self.attribute_map = {
            'result_count': 'resultCount',
            'field_count': 'fieldCount'
        }

        self._result_count = None
        self._field_count = None

    @property
    def result_count(self):
        """
        Gets the result_count of this SearchResultSummary.
        Total number of search results.


        :return: The result_count of this SearchResultSummary.
        :rtype: int
        """
        return self._result_count

    @result_count.setter
    def result_count(self, result_count):
        """
        Sets the result_count of this SearchResultSummary.
        Total number of search results.


        :param result_count: The result_count of this SearchResultSummary.
        :type: int
        """
        self._result_count = result_count

    @property
    def field_count(self):
        """
        Gets the field_count of this SearchResultSummary.
        Total number of field schema information.


        :return: The field_count of this SearchResultSummary.
        :rtype: int
        """
        return self._field_count

    @field_count.setter
    def field_count(self, field_count):
        """
        Sets the field_count of this SearchResultSummary.
        Total number of field schema information.


        :param field_count: The field_count of this SearchResultSummary.
        :type: int
        """
        self._field_count = field_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
