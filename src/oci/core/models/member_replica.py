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

    #: A constant which can be used with the membership_state property of a MemberReplica.
    #: This constant has a value of "ADD_PENDING"
    MEMBERSHIP_STATE_ADD_PENDING = "ADD_PENDING"

    #: A constant which can be used with the membership_state property of a MemberReplica.
    #: This constant has a value of "STABLE"
    MEMBERSHIP_STATE_STABLE = "STABLE"

    #: A constant which can be used with the membership_state property of a MemberReplica.
    #: This constant has a value of "REMOVE_PENDING"
    MEMBERSHIP_STATE_REMOVE_PENDING = "REMOVE_PENDING"

    def __init__(self, **kwargs):
        """
        Initializes a new MemberReplica object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param volume_replica_id:
            The value to assign to the volume_replica_id property of this MemberReplica.
        :type volume_replica_id: str

        :param membership_state:
            The value to assign to the membership_state property of this MemberReplica.
            Allowed values for this property are: "ADD_PENDING", "STABLE", "REMOVE_PENDING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type membership_state: str

        """
        self.swagger_types = {
            'volume_replica_id': 'str',
            'membership_state': 'str'
        }

        self.attribute_map = {
            'volume_replica_id': 'volumeReplicaId',
            'membership_state': 'membershipState'
        }

        self._volume_replica_id = None
        self._membership_state = None

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

    @property
    def membership_state(self):
        """
        Gets the membership_state of this MemberReplica.
        Membership state of the volume replica in relation to the volume group replica.

        Allowed values for this property are: "ADD_PENDING", "STABLE", "REMOVE_PENDING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The membership_state of this MemberReplica.
        :rtype: str
        """
        return self._membership_state

    @membership_state.setter
    def membership_state(self, membership_state):
        """
        Sets the membership_state of this MemberReplica.
        Membership state of the volume replica in relation to the volume group replica.


        :param membership_state: The membership_state of this MemberReplica.
        :type: str
        """
        allowed_values = ["ADD_PENDING", "STABLE", "REMOVE_PENDING"]
        if not value_allowed_none_or_none_sentinel(membership_state, allowed_values):
            membership_state = 'UNKNOWN_ENUM_VALUE'
        self._membership_state = membership_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
