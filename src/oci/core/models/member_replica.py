# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MemberReplica(object):
    """
    OCIDs for the volume replicas in this volume group replica.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MemberReplica object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param volume_replica_id:
            The value to assign to the volume_replica_id property of this MemberReplica.
        :type volume_replica_id: str

        """
        self.swagger_types = {
            'volume_replica_id': 'str'
        }

        self.attribute_map = {
            'volume_replica_id': 'volumeReplicaId'
        }

        self._volume_replica_id = None

    @property
    def volume_replica_id(self):
        """
        **[Required]** Gets the volume_replica_id of this MemberReplica.
        The volume replica ID.


        :return: The volume_replica_id of this MemberReplica.
        :rtype: str
        """
        return self._volume_replica_id

    @volume_replica_id.setter
    def volume_replica_id(self, volume_replica_id):
        """
        Sets the volume_replica_id of this MemberReplica.
        The volume replica ID.


        :param volume_replica_id: The volume_replica_id of this MemberReplica.
        :type: str
        """
        self._volume_replica_id = volume_replica_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
