# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsEntityTopologySummary(object):
    """
    Log Analytics Entity topology that contains a set of log analytics entities and a set of relationships between those.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsEntityTopologySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param nodes:
            The value to assign to the nodes property of this LogAnalyticsEntityTopologySummary.
        :type nodes: oci.log_analytics.models.LogAnalyticsEntityCollection

        :param links:
            The value to assign to the links property of this LogAnalyticsEntityTopologySummary.
        :type links: oci.log_analytics.models.LogAnalyticsEntityTopologyLinkCollection

        """
        self.swagger_types = {
            'nodes': 'LogAnalyticsEntityCollection',
            'links': 'LogAnalyticsEntityTopologyLinkCollection'
        }

        self.attribute_map = {
            'nodes': 'nodes',
            'links': 'links'
        }

        self._nodes = None
        self._links = None

    @property
    def nodes(self):
        """
        **[Required]** Gets the nodes of this LogAnalyticsEntityTopologySummary.

        :return: The nodes of this LogAnalyticsEntityTopologySummary.
        :rtype: oci.log_analytics.models.LogAnalyticsEntityCollection
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """
        Sets the nodes of this LogAnalyticsEntityTopologySummary.

        :param nodes: The nodes of this LogAnalyticsEntityTopologySummary.
        :type: oci.log_analytics.models.LogAnalyticsEntityCollection
        """
        self._nodes = nodes

    @property
    def links(self):
        """
        **[Required]** Gets the links of this LogAnalyticsEntityTopologySummary.

        :return: The links of this LogAnalyticsEntityTopologySummary.
        :rtype: oci.log_analytics.models.LogAnalyticsEntityTopologyLinkCollection
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this LogAnalyticsEntityTopologySummary.

        :param links: The links of this LogAnalyticsEntityTopologySummary.
        :type: oci.log_analytics.models.LogAnalyticsEntityTopologyLinkCollection
        """
        self._links = links

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
