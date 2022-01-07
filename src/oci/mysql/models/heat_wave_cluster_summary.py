# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HeatWaveClusterSummary(object):
    """
    A summary of a HeatWave cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HeatWaveClusterSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param shape_name:
            The value to assign to the shape_name property of this HeatWaveClusterSummary.
        :type shape_name: str

        :param cluster_size:
            The value to assign to the cluster_size property of this HeatWaveClusterSummary.
        :type cluster_size: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this HeatWaveClusterSummary.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this HeatWaveClusterSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this HeatWaveClusterSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'shape_name': 'str',
            'cluster_size': 'int',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'shape_name': 'shapeName',
            'cluster_size': 'clusterSize',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._shape_name = None
        self._cluster_size = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this HeatWaveClusterSummary.
        The shape determines resources to allocate to the HeatWave
        nodes - CPU cores, memory.


        :return: The shape_name of this HeatWaveClusterSummary.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this HeatWaveClusterSummary.
        The shape determines resources to allocate to the HeatWave
        nodes - CPU cores, memory.


        :param shape_name: The shape_name of this HeatWaveClusterSummary.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def cluster_size(self):
        """
        **[Required]** Gets the cluster_size of this HeatWaveClusterSummary.
        The number of analytics-processing compute instances, of the
        specified shape, in the HeatWave cluster.


        :return: The cluster_size of this HeatWaveClusterSummary.
        :rtype: int
        """
        return self._cluster_size

    @cluster_size.setter
    def cluster_size(self, cluster_size):
        """
        Sets the cluster_size of this HeatWaveClusterSummary.
        The number of analytics-processing compute instances, of the
        specified shape, in the HeatWave cluster.


        :param cluster_size: The cluster_size of this HeatWaveClusterSummary.
        :type: int
        """
        self._cluster_size = cluster_size

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this HeatWaveClusterSummary.
        The current state of the MySQL HeatWave cluster.


        :return: The lifecycle_state of this HeatWaveClusterSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this HeatWaveClusterSummary.
        The current state of the MySQL HeatWave cluster.


        :param lifecycle_state: The lifecycle_state of this HeatWaveClusterSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this HeatWaveClusterSummary.
        The date and time the HeatWave cluster was created,
        as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this HeatWaveClusterSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this HeatWaveClusterSummary.
        The date and time the HeatWave cluster was created,
        as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this HeatWaveClusterSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this HeatWaveClusterSummary.
        The time the HeatWave cluster was last updated,
        as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this HeatWaveClusterSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this HeatWaveClusterSummary.
        The time the HeatWave cluster was last updated,
        as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this HeatWaveClusterSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
