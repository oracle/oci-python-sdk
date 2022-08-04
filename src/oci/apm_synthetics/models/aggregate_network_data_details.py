# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AggregateNetworkDataDetails(object):
    """
    Details of the vantage point and corresponding execution times.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AggregateNetworkDataDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vantage_point_execution_times:
            The value to assign to the vantage_point_execution_times property of this AggregateNetworkDataDetails.
        :type vantage_point_execution_times: list[oci.apm_synthetics.models.VantagePointExecution]

        """
        self.swagger_types = {
            'vantage_point_execution_times': 'list[VantagePointExecution]'
        }

        self.attribute_map = {
            'vantage_point_execution_times': 'vantagePointExecutionTimes'
        }

        self._vantage_point_execution_times = None

    @property
    def vantage_point_execution_times(self):
        """
        **[Required]** Gets the vantage_point_execution_times of this AggregateNetworkDataDetails.
        List of VantagePointExecution items.


        :return: The vantage_point_execution_times of this AggregateNetworkDataDetails.
        :rtype: list[oci.apm_synthetics.models.VantagePointExecution]
        """
        return self._vantage_point_execution_times

    @vantage_point_execution_times.setter
    def vantage_point_execution_times(self, vantage_point_execution_times):
        """
        Sets the vantage_point_execution_times of this AggregateNetworkDataDetails.
        List of VantagePointExecution items.


        :param vantage_point_execution_times: The vantage_point_execution_times of this AggregateNetworkDataDetails.
        :type: list[oci.apm_synthetics.models.VantagePointExecution]
        """
        self._vantage_point_execution_times = vantage_point_execution_times

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
