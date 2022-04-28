# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .resolver_endpoint import ResolverEndpoint
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResolverVnicEndpoint(ResolverEndpoint):
    """
    An OCI DNS resolver VNIC endpoint. A VNIC is created for each ResolverVnicEndpoint. VCNs and subnets cannot be
    deleted while ResolverVnicEndpoints exist in them due to the VNIC.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResolverVnicEndpoint object with values from keyword arguments. The default value of the :py:attr:`~oci.dns.models.ResolverVnicEndpoint.endpoint_type` attribute
        of this class is ``VNIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ResolverVnicEndpoint.
        :type name: str

        :param endpoint_type:
            The value to assign to the endpoint_type property of this ResolverVnicEndpoint.
            Allowed values for this property are: "VNIC"
        :type endpoint_type: str

        :param forwarding_address:
            The value to assign to the forwarding_address property of this ResolverVnicEndpoint.
        :type forwarding_address: str

        :param is_forwarding:
            The value to assign to the is_forwarding property of this ResolverVnicEndpoint.
        :type is_forwarding: bool

        :param is_listening:
            The value to assign to the is_listening property of this ResolverVnicEndpoint.
        :type is_listening: bool

        :param listening_address:
            The value to assign to the listening_address property of this ResolverVnicEndpoint.
        :type listening_address: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ResolverVnicEndpoint.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this ResolverVnicEndpoint.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ResolverVnicEndpoint.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ResolverVnicEndpoint.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"
        :type lifecycle_state: str

        :param _self:
            The value to assign to the _self property of this ResolverVnicEndpoint.
        :type _self: str

        :param subnet_id:
            The value to assign to the subnet_id property of this ResolverVnicEndpoint.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this ResolverVnicEndpoint.
        :type nsg_ids: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'endpoint_type': 'str',
            'forwarding_address': 'str',
            'is_forwarding': 'bool',
            'is_listening': 'bool',
            'listening_address': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            '_self': 'str',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'endpoint_type': 'endpointType',
            'forwarding_address': 'forwardingAddress',
            'is_forwarding': 'isForwarding',
            'is_listening': 'isListening',
            'listening_address': 'listeningAddress',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            '_self': 'self',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds'
        }

        self._name = None
        self._endpoint_type = None
        self._forwarding_address = None
        self._is_forwarding = None
        self._is_listening = None
        self._listening_address = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self.__self = None
        self._subnet_id = None
        self._nsg_ids = None
        self._endpoint_type = 'VNIC'

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this ResolverVnicEndpoint.
        The OCID of a subnet. Must be part of the VCN that the resolver is attached to.


        :return: The subnet_id of this ResolverVnicEndpoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this ResolverVnicEndpoint.
        The OCID of a subnet. Must be part of the VCN that the resolver is attached to.


        :param subnet_id: The subnet_id of this ResolverVnicEndpoint.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this ResolverVnicEndpoint.
        An array of network security group OCIDs for the resolver endpoint. These must be part of the VCN that the
        resolver endpoint is a part of.


        :return: The nsg_ids of this ResolverVnicEndpoint.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this ResolverVnicEndpoint.
        An array of network security group OCIDs for the resolver endpoint. These must be part of the VCN that the
        resolver endpoint is a part of.


        :param nsg_ids: The nsg_ids of this ResolverVnicEndpoint.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
