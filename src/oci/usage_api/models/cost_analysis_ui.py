# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CostAnalysisUI(object):
    """
    The common fields for Cost Analysis UI rendering.
    """

    #: A constant which can be used with the graph property of a CostAnalysisUI.
    #: This constant has a value of "BARS"
    GRAPH_BARS = "BARS"

    #: A constant which can be used with the graph property of a CostAnalysisUI.
    #: This constant has a value of "LINES"
    GRAPH_LINES = "LINES"

    #: A constant which can be used with the graph property of a CostAnalysisUI.
    #: This constant has a value of "STACKED_LINES"
    GRAPH_STACKED_LINES = "STACKED_LINES"

    def __init__(self, **kwargs):
        """
        Initializes a new CostAnalysisUI object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param graph:
            The value to assign to the graph property of this CostAnalysisUI.
            Allowed values for this property are: "BARS", "LINES", "STACKED_LINES", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type graph: str

        :param is_cumulative_graph:
            The value to assign to the is_cumulative_graph property of this CostAnalysisUI.
        :type is_cumulative_graph: bool

        """
        self.swagger_types = {
            'graph': 'str',
            'is_cumulative_graph': 'bool'
        }

        self.attribute_map = {
            'graph': 'graph',
            'is_cumulative_graph': 'isCumulativeGraph'
        }

        self._graph = None
        self._is_cumulative_graph = None

    @property
    def graph(self):
        """
        Gets the graph of this CostAnalysisUI.
        the type of graph mode.

        Allowed values for this property are: "BARS", "LINES", "STACKED_LINES", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The graph of this CostAnalysisUI.
        :rtype: str
        """
        return self._graph

    @graph.setter
    def graph(self, graph):
        """
        Sets the graph of this CostAnalysisUI.
        the type of graph mode.


        :param graph: The graph of this CostAnalysisUI.
        :type: str
        """
        allowed_values = ["BARS", "LINES", "STACKED_LINES"]
        if not value_allowed_none_or_none_sentinel(graph, allowed_values):
            graph = 'UNKNOWN_ENUM_VALUE'
        self._graph = graph

    @property
    def is_cumulative_graph(self):
        """
        Gets the is_cumulative_graph of this CostAnalysisUI.
        is cumulative graph.


        :return: The is_cumulative_graph of this CostAnalysisUI.
        :rtype: bool
        """
        return self._is_cumulative_graph

    @is_cumulative_graph.setter
    def is_cumulative_graph(self, is_cumulative_graph):
        """
        Sets the is_cumulative_graph of this CostAnalysisUI.
        is cumulative graph.


        :param is_cumulative_graph: The is_cumulative_graph of this CostAnalysisUI.
        :type: bool
        """
        self._is_cumulative_graph = is_cumulative_graph

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
