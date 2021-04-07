# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClusterCacheMetric(object):
    """
    The response containing the cluster cache metrics for the
    Oracle Real Application Clusters (Oracle RAC) database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ClusterCacheMetric object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cluster_cache_metrics:
            The value to assign to the cluster_cache_metrics property of this ClusterCacheMetric.
        :type cluster_cache_metrics: list[oci.database_management.models.TimeSeriesMetricDefinition]

        """
        self.swagger_types = {
            'cluster_cache_metrics': 'list[TimeSeriesMetricDefinition]'
        }

        self.attribute_map = {
            'cluster_cache_metrics': 'clusterCacheMetrics'
        }

        self._cluster_cache_metrics = None

    @property
    def cluster_cache_metrics(self):
        """
        **[Required]** Gets the cluster_cache_metrics of this ClusterCacheMetric.
        A list of cluster cache metrics for a specific database.


        :return: The cluster_cache_metrics of this ClusterCacheMetric.
        :rtype: list[oci.database_management.models.TimeSeriesMetricDefinition]
        """
        return self._cluster_cache_metrics

    @cluster_cache_metrics.setter
    def cluster_cache_metrics(self, cluster_cache_metrics):
        """
        Sets the cluster_cache_metrics of this ClusterCacheMetric.
        A list of cluster cache metrics for a specific database.


        :param cluster_cache_metrics: The cluster_cache_metrics of this ClusterCacheMetric.
        :type: list[oci.database_management.models.TimeSeriesMetricDefinition]
        """
        self._cluster_cache_metrics = cluster_cache_metrics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
