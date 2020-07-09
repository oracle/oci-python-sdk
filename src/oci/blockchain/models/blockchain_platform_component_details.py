# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BlockchainPlatformComponentDetails(object):
    """
    Blockchain Platform component details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BlockchainPlatformComponentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param osns:
            The value to assign to the osns property of this BlockchainPlatformComponentDetails.
        :type osns: list[Osn]

        :param peers:
            The value to assign to the peers property of this BlockchainPlatformComponentDetails.
        :type peers: list[Peer]

        """
        self.swagger_types = {
            'osns': 'list[Osn]',
            'peers': 'list[Peer]'
        }

        self.attribute_map = {
            'osns': 'osns',
            'peers': 'peers'
        }

        self._osns = None
        self._peers = None

    @property
    def osns(self):
        """
        Gets the osns of this BlockchainPlatformComponentDetails.
        List of OSNs


        :return: The osns of this BlockchainPlatformComponentDetails.
        :rtype: list[Osn]
        """
        return self._osns

    @osns.setter
    def osns(self, osns):
        """
        Sets the osns of this BlockchainPlatformComponentDetails.
        List of OSNs


        :param osns: The osns of this BlockchainPlatformComponentDetails.
        :type: list[Osn]
        """
        self._osns = osns

    @property
    def peers(self):
        """
        Gets the peers of this BlockchainPlatformComponentDetails.
        List of Peers


        :return: The peers of this BlockchainPlatformComponentDetails.
        :rtype: list[Peer]
        """
        return self._peers

    @peers.setter
    def peers(self, peers):
        """
        Sets the peers of this BlockchainPlatformComponentDetails.
        List of Peers


        :param peers: The peers of this BlockchainPlatformComponentDetails.
        :type: list[Peer]
        """
        self._peers = peers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
