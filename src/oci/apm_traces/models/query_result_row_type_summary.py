# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryResultRowTypeSummary(object):
    """
    A summary of the datatype, unit and related metadata of an individual row element of a query result row that is returned.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new QueryResultRowTypeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_type:
            The value to assign to the data_type property of this QueryResultRowTypeSummary.
        :type data_type: str

        :param unit:
            The value to assign to the unit property of this QueryResultRowTypeSummary.
        :type unit: str

        :param display_name:
            The value to assign to the display_name property of this QueryResultRowTypeSummary.
        :type display_name: str

        :param expression:
            The value to assign to the expression property of this QueryResultRowTypeSummary.
        :type expression: str

        :param query_result_row_type_summaries:
            The value to assign to the query_result_row_type_summaries property of this QueryResultRowTypeSummary.
        :type query_result_row_type_summaries: list[oci.apm_traces.models.QueryResultRowTypeSummary]

        """
        self.swagger_types = {
            'data_type': 'str',
            'unit': 'str',
            'display_name': 'str',
            'expression': 'str',
            'query_result_row_type_summaries': 'list[QueryResultRowTypeSummary]'
        }

        self.attribute_map = {
            'data_type': 'dataType',
            'unit': 'unit',
            'display_name': 'displayName',
            'expression': 'expression',
            'query_result_row_type_summaries': 'queryResultRowTypeSummaries'
        }

        self._data_type = None
        self._unit = None
        self._display_name = None
        self._expression = None
        self._query_result_row_type_summaries = None

    @property
    def data_type(self):
        """
        Gets the data_type of this QueryResultRowTypeSummary.
        Datatype of the query result row element.


        :return: The data_type of this QueryResultRowTypeSummary.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this QueryResultRowTypeSummary.
        Datatype of the query result row element.


        :param data_type: The data_type of this QueryResultRowTypeSummary.
        :type: str
        """
        self._data_type = data_type

    @property
    def unit(self):
        """
        Gets the unit of this QueryResultRowTypeSummary.
        Granular unit in which the query result row element's data is represented.


        :return: The unit of this QueryResultRowTypeSummary.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this QueryResultRowTypeSummary.
        Granular unit in which the query result row element's data is represented.


        :param unit: The unit of this QueryResultRowTypeSummary.
        :type: str
        """
        self._unit = unit

    @property
    def display_name(self):
        """
        Gets the display_name of this QueryResultRowTypeSummary.
        Alias name if an alias is used for the query result row element or an assigned display name from the query language
        in some default cases.


        :return: The display_name of this QueryResultRowTypeSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this QueryResultRowTypeSummary.
        Alias name if an alias is used for the query result row element or an assigned display name from the query language
        in some default cases.


        :param display_name: The display_name of this QueryResultRowTypeSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def expression(self):
        """
        Gets the expression of this QueryResultRowTypeSummary.
        Actual show expression in the user typed query that produced this column.


        :return: The expression of this QueryResultRowTypeSummary.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """
        Sets the expression of this QueryResultRowTypeSummary.
        Actual show expression in the user typed query that produced this column.


        :param expression: The expression of this QueryResultRowTypeSummary.
        :type: str
        """
        self._expression = expression

    @property
    def query_result_row_type_summaries(self):
        """
        Gets the query_result_row_type_summaries of this QueryResultRowTypeSummary.
        A query result row type summary object that represents a nested table structure.


        :return: The query_result_row_type_summaries of this QueryResultRowTypeSummary.
        :rtype: list[oci.apm_traces.models.QueryResultRowTypeSummary]
        """
        return self._query_result_row_type_summaries

    @query_result_row_type_summaries.setter
    def query_result_row_type_summaries(self, query_result_row_type_summaries):
        """
        Sets the query_result_row_type_summaries of this QueryResultRowTypeSummary.
        A query result row type summary object that represents a nested table structure.


        :param query_result_row_type_summaries: The query_result_row_type_summaries of this QueryResultRowTypeSummary.
        :type: list[oci.apm_traces.models.QueryResultRowTypeSummary]
        """
        self._query_result_row_type_summaries = query_result_row_type_summaries

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
