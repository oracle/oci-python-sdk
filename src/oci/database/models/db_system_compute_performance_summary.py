# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbSystemComputePerformanceSummary(object):
    """
    Representation of disk performance detail parameters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DbSystemComputePerformanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param shape:
            The value to assign to the shape property of this DbSystemComputePerformanceSummary.
        :type shape: str

        :param compute_performance_list:
            The value to assign to the compute_performance_list property of this DbSystemComputePerformanceSummary.
        :type compute_performance_list: list[oci.database.models.ComputePerformanceSummary]

        """
        self.swagger_types = {
            'shape': 'str',
            'compute_performance_list': 'list[ComputePerformanceSummary]'
        }

        self.attribute_map = {
            'shape': 'shape',
            'compute_performance_list': 'computePerformanceList'
        }

        self._shape = None
        self._compute_performance_list = None

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this DbSystemComputePerformanceSummary.
        The shape of the DB system.


        :return: The shape of this DbSystemComputePerformanceSummary.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this DbSystemComputePerformanceSummary.
        The shape of the DB system.


        :param shape: The shape of this DbSystemComputePerformanceSummary.
        :type: str
        """
        self._shape = shape

    @property
    def compute_performance_list(self):
        """
        **[Required]** Gets the compute_performance_list of this DbSystemComputePerformanceSummary.
        List of Compute performance details for the specified DB system shape.


        :return: The compute_performance_list of this DbSystemComputePerformanceSummary.
        :rtype: list[oci.database.models.ComputePerformanceSummary]
        """
        return self._compute_performance_list

    @compute_performance_list.setter
    def compute_performance_list(self, compute_performance_list):
        """
        Sets the compute_performance_list of this DbSystemComputePerformanceSummary.
        List of Compute performance details for the specified DB system shape.


        :param compute_performance_list: The compute_performance_list of this DbSystemComputePerformanceSummary.
        :type: list[oci.database.models.ComputePerformanceSummary]
        """
        self._compute_performance_list = compute_performance_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
