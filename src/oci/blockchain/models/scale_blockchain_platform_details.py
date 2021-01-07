# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScaleBlockchainPlatformDetails(object):
    """
    Scale operation details for a blockchain platform. The scale operation payload has multiple options
    - Add one or more Ordering Service Node (addOsns)
    - Add one or more Peers (addPeers)
    - Add more replicas of CA, Console and Rest Proxy (addReplicas)
    - Add more storage to the platform (addStorage)
    - Modify the CPU allocation for Peer Nodes (modifyPeers)
    - Remove one or more replicas of CA, Console and Rest Proxy (removeReplicas)
    - Remove one or more Ordering Service Node (removeOsns)
    - Remove one or more Peers (removePeers).
    The scale operation payload must have at least one of the above options.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScaleBlockchainPlatformDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param add_osns:
            The value to assign to the add_osns property of this ScaleBlockchainPlatformDetails.
        :type add_osns: list[oci.blockchain.models.CreateOsnDetails]

        :param add_replicas:
            The value to assign to the add_replicas property of this ScaleBlockchainPlatformDetails.
        :type add_replicas: oci.blockchain.models.ReplicaDetails

        :param add_peers:
            The value to assign to the add_peers property of this ScaleBlockchainPlatformDetails.
        :type add_peers: list[oci.blockchain.models.CreatePeerDetails]

        :param add_storage:
            The value to assign to the add_storage property of this ScaleBlockchainPlatformDetails.
        :type add_storage: oci.blockchain.models.ScaleStorageDetails

        :param modify_peers:
            The value to assign to the modify_peers property of this ScaleBlockchainPlatformDetails.
        :type modify_peers: list[oci.blockchain.models.ModifyPeerDetails]

        :param remove_replicas:
            The value to assign to the remove_replicas property of this ScaleBlockchainPlatformDetails.
        :type remove_replicas: oci.blockchain.models.ReplicaDetails

        :param remove_osns:
            The value to assign to the remove_osns property of this ScaleBlockchainPlatformDetails.
        :type remove_osns: list[str]

        :param remove_peers:
            The value to assign to the remove_peers property of this ScaleBlockchainPlatformDetails.
        :type remove_peers: list[str]

        """
        self.swagger_types = {
            'add_osns': 'list[CreateOsnDetails]',
            'add_replicas': 'ReplicaDetails',
            'add_peers': 'list[CreatePeerDetails]',
            'add_storage': 'ScaleStorageDetails',
            'modify_peers': 'list[ModifyPeerDetails]',
            'remove_replicas': 'ReplicaDetails',
            'remove_osns': 'list[str]',
            'remove_peers': 'list[str]'
        }

        self.attribute_map = {
            'add_osns': 'addOsns',
            'add_replicas': 'addReplicas',
            'add_peers': 'addPeers',
            'add_storage': 'addStorage',
            'modify_peers': 'modifyPeers',
            'remove_replicas': 'removeReplicas',
            'remove_osns': 'removeOsns',
            'remove_peers': 'removePeers'
        }

        self._add_osns = None
        self._add_replicas = None
        self._add_peers = None
        self._add_storage = None
        self._modify_peers = None
        self._remove_replicas = None
        self._remove_osns = None
        self._remove_peers = None

    @property
    def add_osns(self):
        """
        Gets the add_osns of this ScaleBlockchainPlatformDetails.
        new OSNs to add


        :return: The add_osns of this ScaleBlockchainPlatformDetails.
        :rtype: list[oci.blockchain.models.CreateOsnDetails]
        """
        return self._add_osns

    @add_osns.setter
    def add_osns(self, add_osns):
        """
        Sets the add_osns of this ScaleBlockchainPlatformDetails.
        new OSNs to add


        :param add_osns: The add_osns of this ScaleBlockchainPlatformDetails.
        :type: list[oci.blockchain.models.CreateOsnDetails]
        """
        self._add_osns = add_osns

    @property
    def add_replicas(self):
        """
        Gets the add_replicas of this ScaleBlockchainPlatformDetails.

        :return: The add_replicas of this ScaleBlockchainPlatformDetails.
        :rtype: oci.blockchain.models.ReplicaDetails
        """
        return self._add_replicas

    @add_replicas.setter
    def add_replicas(self, add_replicas):
        """
        Sets the add_replicas of this ScaleBlockchainPlatformDetails.

        :param add_replicas: The add_replicas of this ScaleBlockchainPlatformDetails.
        :type: oci.blockchain.models.ReplicaDetails
        """
        self._add_replicas = add_replicas

    @property
    def add_peers(self):
        """
        Gets the add_peers of this ScaleBlockchainPlatformDetails.
        new Peers to add


        :return: The add_peers of this ScaleBlockchainPlatformDetails.
        :rtype: list[oci.blockchain.models.CreatePeerDetails]
        """
        return self._add_peers

    @add_peers.setter
    def add_peers(self, add_peers):
        """
        Sets the add_peers of this ScaleBlockchainPlatformDetails.
        new Peers to add


        :param add_peers: The add_peers of this ScaleBlockchainPlatformDetails.
        :type: list[oci.blockchain.models.CreatePeerDetails]
        """
        self._add_peers = add_peers

    @property
    def add_storage(self):
        """
        Gets the add_storage of this ScaleBlockchainPlatformDetails.

        :return: The add_storage of this ScaleBlockchainPlatformDetails.
        :rtype: oci.blockchain.models.ScaleStorageDetails
        """
        return self._add_storage

    @add_storage.setter
    def add_storage(self, add_storage):
        """
        Sets the add_storage of this ScaleBlockchainPlatformDetails.

        :param add_storage: The add_storage of this ScaleBlockchainPlatformDetails.
        :type: oci.blockchain.models.ScaleStorageDetails
        """
        self._add_storage = add_storage

    @property
    def modify_peers(self):
        """
        Gets the modify_peers of this ScaleBlockchainPlatformDetails.
        modify ocpu allocation to existing Peers


        :return: The modify_peers of this ScaleBlockchainPlatformDetails.
        :rtype: list[oci.blockchain.models.ModifyPeerDetails]
        """
        return self._modify_peers

    @modify_peers.setter
    def modify_peers(self, modify_peers):
        """
        Sets the modify_peers of this ScaleBlockchainPlatformDetails.
        modify ocpu allocation to existing Peers


        :param modify_peers: The modify_peers of this ScaleBlockchainPlatformDetails.
        :type: list[oci.blockchain.models.ModifyPeerDetails]
        """
        self._modify_peers = modify_peers

    @property
    def remove_replicas(self):
        """
        Gets the remove_replicas of this ScaleBlockchainPlatformDetails.

        :return: The remove_replicas of this ScaleBlockchainPlatformDetails.
        :rtype: oci.blockchain.models.ReplicaDetails
        """
        return self._remove_replicas

    @remove_replicas.setter
    def remove_replicas(self, remove_replicas):
        """
        Sets the remove_replicas of this ScaleBlockchainPlatformDetails.

        :param remove_replicas: The remove_replicas of this ScaleBlockchainPlatformDetails.
        :type: oci.blockchain.models.ReplicaDetails
        """
        self._remove_replicas = remove_replicas

    @property
    def remove_osns(self):
        """
        Gets the remove_osns of this ScaleBlockchainPlatformDetails.
        OSN id list to remove


        :return: The remove_osns of this ScaleBlockchainPlatformDetails.
        :rtype: list[str]
        """
        return self._remove_osns

    @remove_osns.setter
    def remove_osns(self, remove_osns):
        """
        Sets the remove_osns of this ScaleBlockchainPlatformDetails.
        OSN id list to remove


        :param remove_osns: The remove_osns of this ScaleBlockchainPlatformDetails.
        :type: list[str]
        """
        self._remove_osns = remove_osns

    @property
    def remove_peers(self):
        """
        Gets the remove_peers of this ScaleBlockchainPlatformDetails.
        Peer id list to remove


        :return: The remove_peers of this ScaleBlockchainPlatformDetails.
        :rtype: list[str]
        """
        return self._remove_peers

    @remove_peers.setter
    def remove_peers(self, remove_peers):
        """
        Sets the remove_peers of this ScaleBlockchainPlatformDetails.
        Peer id list to remove


        :param remove_peers: The remove_peers of this ScaleBlockchainPlatformDetails.
        :type: list[str]
        """
        self._remove_peers = remove_peers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
