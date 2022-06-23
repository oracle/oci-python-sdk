# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DefaultDrgRouteTables(object):
    """
    The default DRG route table for this DRG. Each network type
    has a default DRG route table.

    You can update a network type to use a different DRG route table, but
    each network type must have a default DRG route table. You cannot delete
    a default DRG route table.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DefaultDrgRouteTables object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vcn:
            The value to assign to the vcn property of this DefaultDrgRouteTables.
        :type vcn: str

        :param ipsec_tunnel:
            The value to assign to the ipsec_tunnel property of this DefaultDrgRouteTables.
        :type ipsec_tunnel: str

        :param virtual_circuit:
            The value to assign to the virtual_circuit property of this DefaultDrgRouteTables.
        :type virtual_circuit: str

        :param remote_peering_connection:
            The value to assign to the remote_peering_connection property of this DefaultDrgRouteTables.
        :type remote_peering_connection: str

        """
        self.swagger_types = {
            'vcn': 'str',
            'ipsec_tunnel': 'str',
            'virtual_circuit': 'str',
            'remote_peering_connection': 'str'
        }

        self.attribute_map = {
            'vcn': 'vcn',
            'ipsec_tunnel': 'ipsecTunnel',
            'virtual_circuit': 'virtualCircuit',
            'remote_peering_connection': 'remotePeeringConnection'
        }

        self._vcn = None
        self._ipsec_tunnel = None
        self._virtual_circuit = None
        self._remote_peering_connection = None

    @property
    def vcn(self):
        """
        Gets the vcn of this DefaultDrgRouteTables.
        The `OCID`__ of the default DRG route table to be assigned to DRG attachments
        of type VCN on creation.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The vcn of this DefaultDrgRouteTables.
        :rtype: str
        """
        return self._vcn

    @vcn.setter
    def vcn(self, vcn):
        """
        Sets the vcn of this DefaultDrgRouteTables.
        The `OCID`__ of the default DRG route table to be assigned to DRG attachments
        of type VCN on creation.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param vcn: The vcn of this DefaultDrgRouteTables.
        :type: str
        """
        self._vcn = vcn

    @property
    def ipsec_tunnel(self):
        """
        Gets the ipsec_tunnel of this DefaultDrgRouteTables.
        The `OCID`__ of the default DRG route table assigned to DRG attachments
        of type IPSEC_TUNNEL on creation.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The ipsec_tunnel of this DefaultDrgRouteTables.
        :rtype: str
        """
        return self._ipsec_tunnel

    @ipsec_tunnel.setter
    def ipsec_tunnel(self, ipsec_tunnel):
        """
        Sets the ipsec_tunnel of this DefaultDrgRouteTables.
        The `OCID`__ of the default DRG route table assigned to DRG attachments
        of type IPSEC_TUNNEL on creation.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param ipsec_tunnel: The ipsec_tunnel of this DefaultDrgRouteTables.
        :type: str
        """
        self._ipsec_tunnel = ipsec_tunnel

    @property
    def virtual_circuit(self):
        """
        Gets the virtual_circuit of this DefaultDrgRouteTables.
        The `OCID`__ of the default DRG route table to be assigned to DRG attachments
        of type VIRTUAL_CIRCUIT on creation.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The virtual_circuit of this DefaultDrgRouteTables.
        :rtype: str
        """
        return self._virtual_circuit

    @virtual_circuit.setter
    def virtual_circuit(self, virtual_circuit):
        """
        Sets the virtual_circuit of this DefaultDrgRouteTables.
        The `OCID`__ of the default DRG route table to be assigned to DRG attachments
        of type VIRTUAL_CIRCUIT on creation.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param virtual_circuit: The virtual_circuit of this DefaultDrgRouteTables.
        :type: str
        """
        self._virtual_circuit = virtual_circuit

    @property
    def remote_peering_connection(self):
        """
        Gets the remote_peering_connection of this DefaultDrgRouteTables.
        The `OCID`__ of the default DRG route table to be assigned to DRG attachments
        of type REMOTE_PEERING_CONNECTION on creation.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The remote_peering_connection of this DefaultDrgRouteTables.
        :rtype: str
        """
        return self._remote_peering_connection

    @remote_peering_connection.setter
    def remote_peering_connection(self, remote_peering_connection):
        """
        Sets the remote_peering_connection of this DefaultDrgRouteTables.
        The `OCID`__ of the default DRG route table to be assigned to DRG attachments
        of type REMOTE_PEERING_CONNECTION on creation.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param remote_peering_connection: The remote_peering_connection of this DefaultDrgRouteTables.
        :type: str
        """
        self._remote_peering_connection = remote_peering_connection

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
