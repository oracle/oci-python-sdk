# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateClusterStatusDetails(object):
    """
    Information about the update cluster event.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateClusterStatusDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cluster_id:
            The value to assign to the cluster_id property of this UpdateClusterStatusDetails.
        :type cluster_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this UpdateClusterStatusDetails.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'cluster_id': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'cluster_id': 'clusterId',
            'lifecycle_state': 'lifecycleState'
        }

        self._cluster_id = None
        self._lifecycle_state = None

    @property
    def cluster_id(self):
        """
        **[Required]** Gets the cluster_id of this UpdateClusterStatusDetails.
        The OCID of the OpenSearch cluster.


        :return: The cluster_id of this UpdateClusterStatusDetails.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this UpdateClusterStatusDetails.
        The OCID of the OpenSearch cluster.


        :param cluster_id: The cluster_id of this UpdateClusterStatusDetails.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this UpdateClusterStatusDetails.
        The state of the cluster after the cluster was updated.


        :return: The lifecycle_state of this UpdateClusterStatusDetails.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this UpdateClusterStatusDetails.
        The state of the cluster after the cluster was updated.


        :param lifecycle_state: The lifecycle_state of this UpdateClusterStatusDetails.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
