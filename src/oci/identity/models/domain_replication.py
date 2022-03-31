# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DomainReplication(object):
    """
    (For tenancies that support identity domains) Identity domain replication states.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DomainReplication object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param opc_water_mark:
            The value to assign to the opc_water_mark property of this DomainReplication.
        :type opc_water_mark: float

        :param txn_seq_number:
            The value to assign to the txn_seq_number property of this DomainReplication.
        :type txn_seq_number: float

        :param domain_replication_states:
            The value to assign to the domain_replication_states property of this DomainReplication.
        :type domain_replication_states: list[oci.identity.models.DomainReplicationStates]

        """
        self.swagger_types = {
            'opc_water_mark': 'float',
            'txn_seq_number': 'float',
            'domain_replication_states': 'list[DomainReplicationStates]'
        }

        self.attribute_map = {
            'opc_water_mark': 'opcWaterMark',
            'txn_seq_number': 'txnSeqNumber',
            'domain_replication_states': 'domainReplicationStates'
        }

        self._opc_water_mark = None
        self._txn_seq_number = None
        self._domain_replication_states = None

    @property
    def opc_water_mark(self):
        """
        **[Required]** Gets the opc_water_mark of this DomainReplication.
        The version number indicating the value of kievTxnId, starting from which the identity domain replication events need to be returned.


        :return: The opc_water_mark of this DomainReplication.
        :rtype: float
        """
        return self._opc_water_mark

    @opc_water_mark.setter
    def opc_water_mark(self, opc_water_mark):
        """
        Sets the opc_water_mark of this DomainReplication.
        The version number indicating the value of kievTxnId, starting from which the identity domain replication events need to be returned.


        :param opc_water_mark: The opc_water_mark of this DomainReplication.
        :type: float
        """
        self._opc_water_mark = opc_water_mark

    @property
    def txn_seq_number(self):
        """
        **[Required]** Gets the txn_seq_number of this DomainReplication.
        A custom value defining the order of records with the same kievTxnId.


        :return: The txn_seq_number of this DomainReplication.
        :rtype: float
        """
        return self._txn_seq_number

    @txn_seq_number.setter
    def txn_seq_number(self, txn_seq_number):
        """
        Sets the txn_seq_number of this DomainReplication.
        A custom value defining the order of records with the same kievTxnId.


        :param txn_seq_number: The txn_seq_number of this DomainReplication.
        :type: float
        """
        self._txn_seq_number = txn_seq_number

    @property
    def domain_replication_states(self):
        """
        **[Required]** Gets the domain_replication_states of this DomainReplication.
        The identity domain's replication state.


        :return: The domain_replication_states of this DomainReplication.
        :rtype: list[oci.identity.models.DomainReplicationStates]
        """
        return self._domain_replication_states

    @domain_replication_states.setter
    def domain_replication_states(self, domain_replication_states):
        """
        Sets the domain_replication_states of this DomainReplication.
        The identity domain's replication state.


        :param domain_replication_states: The domain_replication_states of this DomainReplication.
        :type: list[oci.identity.models.DomainReplicationStates]
        """
        self._domain_replication_states = domain_replication_states

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
