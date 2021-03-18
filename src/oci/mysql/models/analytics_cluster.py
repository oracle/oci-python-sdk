# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnalyticsCluster(object):
    """
    DEPRECATED -- please use HeatWave API instead.
    An Analytics Cluster is a database accelerator for a DB System.
    """

    #: A constant which can be used with the lifecycle_state property of a AnalyticsCluster.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsCluster.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsCluster.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsCluster.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsCluster.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsCluster.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsCluster.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new AnalyticsCluster object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_system_id:
            The value to assign to the db_system_id property of this AnalyticsCluster.
        :type db_system_id: str

        :param shape_name:
            The value to assign to the shape_name property of this AnalyticsCluster.
        :type shape_name: str

        :param cluster_size:
            The value to assign to the cluster_size property of this AnalyticsCluster.
        :type cluster_size: int

        :param cluster_nodes:
            The value to assign to the cluster_nodes property of this AnalyticsCluster.
        :type cluster_nodes: list[oci.mysql.models.AnalyticsClusterNode]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AnalyticsCluster.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AnalyticsCluster.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this AnalyticsCluster.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AnalyticsCluster.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'db_system_id': 'str',
            'shape_name': 'str',
            'cluster_size': 'int',
            'cluster_nodes': 'list[AnalyticsClusterNode]',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'db_system_id': 'dbSystemId',
            'shape_name': 'shapeName',
            'cluster_size': 'clusterSize',
            'cluster_nodes': 'clusterNodes',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._db_system_id = None
        self._shape_name = None
        self._cluster_size = None
        self._cluster_nodes = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None

    @property
    def db_system_id(self):
        """
        **[Required]** Gets the db_system_id of this AnalyticsCluster.
        The OCID of the parent DB System this Analytics Cluster is attached to.


        :return: The db_system_id of this AnalyticsCluster.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this AnalyticsCluster.
        The OCID of the parent DB System this Analytics Cluster is attached to.


        :param db_system_id: The db_system_id of this AnalyticsCluster.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this AnalyticsCluster.
        The shape determines resources to allocate to the Analytics
        Cluster nodes - CPU cores, memory.


        :return: The shape_name of this AnalyticsCluster.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this AnalyticsCluster.
        The shape determines resources to allocate to the Analytics
        Cluster nodes - CPU cores, memory.


        :param shape_name: The shape_name of this AnalyticsCluster.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def cluster_size(self):
        """
        **[Required]** Gets the cluster_size of this AnalyticsCluster.
        The number of analytics-processing compute instances, of the
        specified shape, in the Analytics Cluster.


        :return: The cluster_size of this AnalyticsCluster.
        :rtype: int
        """
        return self._cluster_size

    @cluster_size.setter
    def cluster_size(self, cluster_size):
        """
        Sets the cluster_size of this AnalyticsCluster.
        The number of analytics-processing compute instances, of the
        specified shape, in the Analytics Cluster.


        :param cluster_size: The cluster_size of this AnalyticsCluster.
        :type: int
        """
        self._cluster_size = cluster_size

    @property
    def cluster_nodes(self):
        """
        **[Required]** Gets the cluster_nodes of this AnalyticsCluster.
        An Analytics Cluster Node is a compute host that is part of an Analytics Cluster.


        :return: The cluster_nodes of this AnalyticsCluster.
        :rtype: list[oci.mysql.models.AnalyticsClusterNode]
        """
        return self._cluster_nodes

    @cluster_nodes.setter
    def cluster_nodes(self, cluster_nodes):
        """
        Sets the cluster_nodes of this AnalyticsCluster.
        An Analytics Cluster Node is a compute host that is part of an Analytics Cluster.


        :param cluster_nodes: The cluster_nodes of this AnalyticsCluster.
        :type: list[oci.mysql.models.AnalyticsClusterNode]
        """
        self._cluster_nodes = cluster_nodes

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AnalyticsCluster.
        The current state of the Analytics Cluster.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AnalyticsCluster.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AnalyticsCluster.
        The current state of the Analytics Cluster.


        :param lifecycle_state: The lifecycle_state of this AnalyticsCluster.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AnalyticsCluster.
        Additional information about the current lifecycleState.


        :return: The lifecycle_details of this AnalyticsCluster.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AnalyticsCluster.
        Additional information about the current lifecycleState.


        :param lifecycle_details: The lifecycle_details of this AnalyticsCluster.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AnalyticsCluster.
        The date and time the Analytics Cluster was created, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this AnalyticsCluster.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AnalyticsCluster.
        The date and time the Analytics Cluster was created, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this AnalyticsCluster.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this AnalyticsCluster.
        The time the Analytics Cluster was last updated, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this AnalyticsCluster.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AnalyticsCluster.
        The time the Analytics Cluster was last updated, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this AnalyticsCluster.
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
