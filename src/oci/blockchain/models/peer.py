# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Peer(object):
    """
    A Peer details
    """

    #: A constant which can be used with the lifecycle_state property of a Peer.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Peer.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Peer.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Peer object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param peer_key:
            The value to assign to the peer_key property of this Peer.
        :type peer_key: str

        :param role:
            The value to assign to the role property of this Peer.
        :type role: str

        :param alias:
            The value to assign to the alias property of this Peer.
        :type alias: str

        :param ocpu_allocation_param:
            The value to assign to the ocpu_allocation_param property of this Peer.
        :type ocpu_allocation_param: oci.blockchain.models.OcpuAllocationNumberParam

        :param host:
            The value to assign to the host property of this Peer.
        :type host: str

        :param ad:
            The value to assign to the ad property of this Peer.
        :type ad: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Peer.
            Allowed values for this property are: "ACTIVE", "INACTIVE", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'peer_key': 'str',
            'role': 'str',
            'alias': 'str',
            'ocpu_allocation_param': 'OcpuAllocationNumberParam',
            'host': 'str',
            'ad': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'peer_key': 'peerKey',
            'role': 'role',
            'alias': 'alias',
            'ocpu_allocation_param': 'ocpuAllocationParam',
            'host': 'host',
            'ad': 'ad',
            'lifecycle_state': 'lifecycleState'
        }

        self._peer_key = None
        self._role = None
        self._alias = None
        self._ocpu_allocation_param = None
        self._host = None
        self._ad = None
        self._lifecycle_state = None

    @property
    def peer_key(self):
        """
        **[Required]** Gets the peer_key of this Peer.
        peer identifier


        :return: The peer_key of this Peer.
        :rtype: str
        """
        return self._peer_key

    @peer_key.setter
    def peer_key(self, peer_key):
        """
        Sets the peer_key of this Peer.
        peer identifier


        :param peer_key: The peer_key of this Peer.
        :type: str
        """
        self._peer_key = peer_key

    @property
    def role(self):
        """
        **[Required]** Gets the role of this Peer.
        Peer role


        :return: The role of this Peer.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this Peer.
        Peer role


        :param role: The role of this Peer.
        :type: str
        """
        self._role = role

    @property
    def alias(self):
        """
        Gets the alias of this Peer.
        peer alias


        :return: The alias of this Peer.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """
        Sets the alias of this Peer.
        peer alias


        :param alias: The alias of this Peer.
        :type: str
        """
        self._alias = alias

    @property
    def ocpu_allocation_param(self):
        """
        Gets the ocpu_allocation_param of this Peer.

        :return: The ocpu_allocation_param of this Peer.
        :rtype: oci.blockchain.models.OcpuAllocationNumberParam
        """
        return self._ocpu_allocation_param

    @ocpu_allocation_param.setter
    def ocpu_allocation_param(self, ocpu_allocation_param):
        """
        Sets the ocpu_allocation_param of this Peer.

        :param ocpu_allocation_param: The ocpu_allocation_param of this Peer.
        :type: oci.blockchain.models.OcpuAllocationNumberParam
        """
        self._ocpu_allocation_param = ocpu_allocation_param

    @property
    def host(self):
        """
        **[Required]** Gets the host of this Peer.
        Host on which the Peer exists


        :return: The host of this Peer.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this Peer.
        Host on which the Peer exists


        :param host: The host of this Peer.
        :type: str
        """
        self._host = host

    @property
    def ad(self):
        """
        **[Required]** Gets the ad of this Peer.
        Availability Domain of peer


        :return: The ad of this Peer.
        :rtype: str
        """
        return self._ad

    @ad.setter
    def ad(self, ad):
        """
        Sets the ad of this Peer.
        Availability Domain of peer


        :param ad: The ad of this Peer.
        :type: str
        """
        self._ad = ad

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Peer.
        The current state of the peer.

        Allowed values for this property are: "ACTIVE", "INACTIVE", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Peer.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Peer.
        The current state of the peer.


        :param lifecycle_state: The lifecycle_state of this Peer.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
