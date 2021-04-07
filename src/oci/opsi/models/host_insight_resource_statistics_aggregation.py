# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostInsightResourceStatisticsAggregation(object):
    """
    Contains host details and resource statistics.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostInsightResourceStatisticsAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param host_details:
            The value to assign to the host_details property of this HostInsightResourceStatisticsAggregation.
        :type host_details: oci.opsi.models.HostDetails

        :param current_statistics:
            The value to assign to the current_statistics property of this HostInsightResourceStatisticsAggregation.
        :type current_statistics: oci.opsi.models.HostResourceStatistics

        """
        self.swagger_types = {
            'host_details': 'HostDetails',
            'current_statistics': 'HostResourceStatistics'
        }

        self.attribute_map = {
            'host_details': 'hostDetails',
            'current_statistics': 'currentStatistics'
        }

        self._host_details = None
        self._current_statistics = None

    @property
    def host_details(self):
        """
        **[Required]** Gets the host_details of this HostInsightResourceStatisticsAggregation.

        :return: The host_details of this HostInsightResourceStatisticsAggregation.
        :rtype: oci.opsi.models.HostDetails
        """
        return self._host_details

    @host_details.setter
    def host_details(self, host_details):
        """
        Sets the host_details of this HostInsightResourceStatisticsAggregation.

        :param host_details: The host_details of this HostInsightResourceStatisticsAggregation.
        :type: oci.opsi.models.HostDetails
        """
        self._host_details = host_details

    @property
    def current_statistics(self):
        """
        **[Required]** Gets the current_statistics of this HostInsightResourceStatisticsAggregation.

        :return: The current_statistics of this HostInsightResourceStatisticsAggregation.
        :rtype: oci.opsi.models.HostResourceStatistics
        """
        return self._current_statistics

    @current_statistics.setter
    def current_statistics(self, current_statistics):
        """
        Sets the current_statistics of this HostInsightResourceStatisticsAggregation.

        :param current_statistics: The current_statistics of this HostInsightResourceStatisticsAggregation.
        :type: oci.opsi.models.HostResourceStatistics
        """
        self._current_statistics = current_statistics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
