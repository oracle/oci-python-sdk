# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClusterMigrateToNativeVcnStatus(object):
    """
    Information regarding a cluster's move to Native VCN.
    """

    #: A constant which can be used with the state property of a ClusterMigrateToNativeVcnStatus.
    #: This constant has a value of "NOT_STARTED"
    STATE_NOT_STARTED = "NOT_STARTED"

    #: A constant which can be used with the state property of a ClusterMigrateToNativeVcnStatus.
    #: This constant has a value of "REQUESTED"
    STATE_REQUESTED = "REQUESTED"

    #: A constant which can be used with the state property of a ClusterMigrateToNativeVcnStatus.
    #: This constant has a value of "IN_PROGRESS"
    STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the state property of a ClusterMigrateToNativeVcnStatus.
    #: This constant has a value of "PENDING_DECOMMISSION"
    STATE_PENDING_DECOMMISSION = "PENDING_DECOMMISSION"

    #: A constant which can be used with the state property of a ClusterMigrateToNativeVcnStatus.
    #: This constant has a value of "COMPLETED"
    STATE_COMPLETED = "COMPLETED"

    def __init__(self, **kwargs):
        """
        Initializes a new ClusterMigrateToNativeVcnStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_decommission_scheduled:
            The value to assign to the time_decommission_scheduled property of this ClusterMigrateToNativeVcnStatus.
        :type time_decommission_scheduled: datetime

        :param state:
            The value to assign to the state property of this ClusterMigrateToNativeVcnStatus.
            Allowed values for this property are: "NOT_STARTED", "REQUESTED", "IN_PROGRESS", "PENDING_DECOMMISSION", "COMPLETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type state: str

        """
        self.swagger_types = {
            'time_decommission_scheduled': 'datetime',
            'state': 'str'
        }

        self.attribute_map = {
            'time_decommission_scheduled': 'timeDecommissionScheduled',
            'state': 'state'
        }

        self._time_decommission_scheduled = None
        self._state = None

    @property
    def time_decommission_scheduled(self):
        """
        Gets the time_decommission_scheduled of this ClusterMigrateToNativeVcnStatus.
        The date and time the non-native VCN is due to be decommissioned.


        :return: The time_decommission_scheduled of this ClusterMigrateToNativeVcnStatus.
        :rtype: datetime
        """
        return self._time_decommission_scheduled

    @time_decommission_scheduled.setter
    def time_decommission_scheduled(self, time_decommission_scheduled):
        """
        Sets the time_decommission_scheduled of this ClusterMigrateToNativeVcnStatus.
        The date and time the non-native VCN is due to be decommissioned.


        :param time_decommission_scheduled: The time_decommission_scheduled of this ClusterMigrateToNativeVcnStatus.
        :type: datetime
        """
        self._time_decommission_scheduled = time_decommission_scheduled

    @property
    def state(self):
        """
        **[Required]** Gets the state of this ClusterMigrateToNativeVcnStatus.
        The current migration status of the cluster.

        Allowed values for this property are: "NOT_STARTED", "REQUESTED", "IN_PROGRESS", "PENDING_DECOMMISSION", "COMPLETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The state of this ClusterMigrateToNativeVcnStatus.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this ClusterMigrateToNativeVcnStatus.
        The current migration status of the cluster.


        :param state: The state of this ClusterMigrateToNativeVcnStatus.
        :type: str
        """
        allowed_values = ["NOT_STARTED", "REQUESTED", "IN_PROGRESS", "PENDING_DECOMMISSION", "COMPLETED"]
        if not value_allowed_none_or_none_sentinel(state, allowed_values):
            state = 'UNKNOWN_ENUM_VALUE'
        self._state = state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
