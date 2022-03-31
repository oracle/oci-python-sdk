# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DomainReplicationStates(object):
    """
    (For tenancies that support identity domains) The identity domain replication log for all identity domains for a given region.
    """

    #: A constant which can be used with the state property of a DomainReplicationStates.
    #: This constant has a value of "ENABLING_REPLICATION"
    STATE_ENABLING_REPLICATION = "ENABLING_REPLICATION"

    #: A constant which can be used with the state property of a DomainReplicationStates.
    #: This constant has a value of "REPLICATION_ENABLED"
    STATE_REPLICATION_ENABLED = "REPLICATION_ENABLED"

    #: A constant which can be used with the state property of a DomainReplicationStates.
    #: This constant has a value of "DISABLING_REPLICATION"
    STATE_DISABLING_REPLICATION = "DISABLING_REPLICATION"

    #: A constant which can be used with the state property of a DomainReplicationStates.
    #: This constant has a value of "REPLICATION_DISABLED"
    STATE_REPLICATION_DISABLED = "REPLICATION_DISABLED"

    #: A constant which can be used with the state property of a DomainReplicationStates.
    #: This constant has a value of "DELETED"
    STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new DomainReplicationStates object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param domain_id:
            The value to assign to the domain_id property of this DomainReplicationStates.
        :type domain_id: str

        :param state:
            The value to assign to the state property of this DomainReplicationStates.
            Allowed values for this property are: "ENABLING_REPLICATION", "REPLICATION_ENABLED", "DISABLING_REPLICATION", "REPLICATION_DISABLED", "DELETED"
        :type state: str

        :param replica_region:
            The value to assign to the replica_region property of this DomainReplicationStates.
        :type replica_region: str

        """
        self.swagger_types = {
            'domain_id': 'str',
            'state': 'str',
            'replica_region': 'str'
        }

        self.attribute_map = {
            'domain_id': 'domainId',
            'state': 'state',
            'replica_region': 'replicaRegion'
        }

        self._domain_id = None
        self._state = None
        self._replica_region = None

    @property
    def domain_id(self):
        """
        **[Required]** Gets the domain_id of this DomainReplicationStates.
        The OCID of the identity domain.


        :return: The domain_id of this DomainReplicationStates.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """
        Sets the domain_id of this DomainReplicationStates.
        The OCID of the identity domain.


        :param domain_id: The domain_id of this DomainReplicationStates.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def state(self):
        """
        **[Required]** Gets the state of this DomainReplicationStates.
        The IDCS-replicated region state.

        Allowed values for this property are: "ENABLING_REPLICATION", "REPLICATION_ENABLED", "DISABLING_REPLICATION", "REPLICATION_DISABLED", "DELETED"


        :return: The state of this DomainReplicationStates.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this DomainReplicationStates.
        The IDCS-replicated region state.


        :param state: The state of this DomainReplicationStates.
        :type: str
        """
        allowed_values = ["ENABLING_REPLICATION", "REPLICATION_ENABLED", "DISABLING_REPLICATION", "REPLICATION_DISABLED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(state, allowed_values):
            raise ValueError(
                "Invalid value for `state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._state = state

    @property
    def replica_region(self):
        """
        **[Required]** Gets the replica_region of this DomainReplicationStates.
        The replica region for the identity domain.


        :return: The replica_region of this DomainReplicationStates.
        :rtype: str
        """
        return self._replica_region

    @replica_region.setter
    def replica_region(self, replica_region):
        """
        Sets the replica_region of this DomainReplicationStates.
        The replica region for the identity domain.


        :param replica_region: The replica_region of this DomainReplicationStates.
        :type: str
        """
        self._replica_region = replica_region

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
