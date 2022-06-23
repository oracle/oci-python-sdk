# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TrafficRoute(object):
    """
    Defines the traffic route taken in the path in `PathAnalysisResult`.
    """

    #: A constant which can be used with the reachability_status property of a TrafficRoute.
    #: This constant has a value of "REACHABLE"
    REACHABILITY_STATUS_REACHABLE = "REACHABLE"

    #: A constant which can be used with the reachability_status property of a TrafficRoute.
    #: This constant has a value of "UNREACHABLE"
    REACHABILITY_STATUS_UNREACHABLE = "UNREACHABLE"

    #: A constant which can be used with the reachability_status property of a TrafficRoute.
    #: This constant has a value of "INDETERMINATE"
    REACHABILITY_STATUS_INDETERMINATE = "INDETERMINATE"

    def __init__(self, **kwargs):
        """
        Initializes a new TrafficRoute object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param reachability_status:
            The value to assign to the reachability_status property of this TrafficRoute.
            Allowed values for this property are: "REACHABLE", "UNREACHABLE", "INDETERMINATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type reachability_status: str

        :param nodes:
            The value to assign to the nodes property of this TrafficRoute.
        :type nodes: list[oci.vn_monitoring.models.TrafficNode]

        :param route_analysis_description:
            The value to assign to the route_analysis_description property of this TrafficRoute.
        :type route_analysis_description: str

        """
        self.swagger_types = {
            'reachability_status': 'str',
            'nodes': 'list[TrafficNode]',
            'route_analysis_description': 'str'
        }

        self.attribute_map = {
            'reachability_status': 'reachabilityStatus',
            'nodes': 'nodes',
            'route_analysis_description': 'routeAnalysisDescription'
        }

        self._reachability_status = None
        self._nodes = None
        self._route_analysis_description = None

    @property
    def reachability_status(self):
        """
        **[Required]** Gets the reachability_status of this TrafficRoute.
        Reachability status for the given traffic route.

        Allowed values for this property are: "REACHABLE", "UNREACHABLE", "INDETERMINATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The reachability_status of this TrafficRoute.
        :rtype: str
        """
        return self._reachability_status

    @reachability_status.setter
    def reachability_status(self, reachability_status):
        """
        Sets the reachability_status of this TrafficRoute.
        Reachability status for the given traffic route.


        :param reachability_status: The reachability_status of this TrafficRoute.
        :type: str
        """
        allowed_values = ["REACHABLE", "UNREACHABLE", "INDETERMINATE"]
        if not value_allowed_none_or_none_sentinel(reachability_status, allowed_values):
            reachability_status = 'UNKNOWN_ENUM_VALUE'
        self._reachability_status = reachability_status

    @property
    def nodes(self):
        """
        **[Required]** Gets the nodes of this TrafficRoute.
        The ordered sequence of nodes in the given the traffic route forming a path.


        :return: The nodes of this TrafficRoute.
        :rtype: list[oci.vn_monitoring.models.TrafficNode]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """
        Sets the nodes of this TrafficRoute.
        The ordered sequence of nodes in the given the traffic route forming a path.


        :param nodes: The nodes of this TrafficRoute.
        :type: list[oci.vn_monitoring.models.TrafficNode]
        """
        self._nodes = nodes

    @property
    def route_analysis_description(self):
        """
        Gets the route_analysis_description of this TrafficRoute.
        A description of the traffic route analysis. For example: \"Traffic might not reach a destination
        due to the LB backend being unhealthy\".


        :return: The route_analysis_description of this TrafficRoute.
        :rtype: str
        """
        return self._route_analysis_description

    @route_analysis_description.setter
    def route_analysis_description(self, route_analysis_description):
        """
        Sets the route_analysis_description of this TrafficRoute.
        A description of the traffic route analysis. For example: \"Traffic might not reach a destination
        due to the LB backend being unhealthy\".


        :param route_analysis_description: The route_analysis_description of this TrafficRoute.
        :type: str
        """
        self._route_analysis_description = route_analysis_description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
