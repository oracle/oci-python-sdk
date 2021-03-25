# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReplicationStatusDetails(object):
    """
    Details of replication status across all replica regions
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ReplicationStatusDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param replica_details:
            The value to assign to the replica_details property of this ReplicationStatusDetails.
        :type replica_details: list[oci.key_management.models.ReplicaDetails]

        """
        self.swagger_types = {
            'replica_details': 'list[ReplicaDetails]'
        }

        self.attribute_map = {
            'replica_details': 'replicaDetails'
        }

        self._replica_details = None

    @property
    def replica_details(self):
        """
        Gets the replica_details of this ReplicationStatusDetails.

        :return: The replica_details of this ReplicationStatusDetails.
        :rtype: list[oci.key_management.models.ReplicaDetails]
        """
        return self._replica_details

    @replica_details.setter
    def replica_details(self, replica_details):
        """
        Sets the replica_details of this ReplicationStatusDetails.

        :param replica_details: The replica_details of this ReplicationStatusDetails.
        :type: list[oci.key_management.models.ReplicaDetails]
        """
        self._replica_details = replica_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
