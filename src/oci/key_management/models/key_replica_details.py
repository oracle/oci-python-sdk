# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KeyReplicaDetails(object):
    """
    Key replica details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KeyReplicaDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param replication_id:
            The value to assign to the replication_id property of this KeyReplicaDetails.
        :type replication_id: str

        """
        self.swagger_types = {
            'replication_id': 'str'
        }

        self.attribute_map = {
            'replication_id': 'replicationId'
        }

        self._replication_id = None

    @property
    def replication_id(self):
        """
        Gets the replication_id of this KeyReplicaDetails.
        ReplicationId associated with a key operation


        :return: The replication_id of this KeyReplicaDetails.
        :rtype: str
        """
        return self._replication_id

    @replication_id.setter
    def replication_id(self, replication_id):
        """
        Sets the replication_id of this KeyReplicaDetails.
        ReplicationId associated with a key operation


        :param replication_id: The replication_id of this KeyReplicaDetails.
        :type: str
        """
        self._replication_id = replication_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
