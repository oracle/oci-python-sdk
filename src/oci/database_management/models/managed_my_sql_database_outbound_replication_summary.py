# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedMySqlDatabaseOutboundReplicationSummary(object):
    """
    An outbound replication record of a MySQL server.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedMySqlDatabaseOutboundReplicationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param replica_host:
            The value to assign to the replica_host property of this ManagedMySqlDatabaseOutboundReplicationSummary.
        :type replica_host: str

        :param replica_port:
            The value to assign to the replica_port property of this ManagedMySqlDatabaseOutboundReplicationSummary.
        :type replica_port: int

        :param replica_uuid:
            The value to assign to the replica_uuid property of this ManagedMySqlDatabaseOutboundReplicationSummary.
        :type replica_uuid: str

        :param replica_server_id:
            The value to assign to the replica_server_id property of this ManagedMySqlDatabaseOutboundReplicationSummary.
        :type replica_server_id: int

        """
        self.swagger_types = {
            'replica_host': 'str',
            'replica_port': 'int',
            'replica_uuid': 'str',
            'replica_server_id': 'int'
        }
        self.attribute_map = {
            'replica_host': 'replicaHost',
            'replica_port': 'replicaPort',
            'replica_uuid': 'replicaUuid',
            'replica_server_id': 'replicaServerId'
        }
        self._replica_host = None
        self._replica_port = None
        self._replica_uuid = None
        self._replica_server_id = None

    @property
    def replica_host(self):
        """
        Gets the replica_host of this ManagedMySqlDatabaseOutboundReplicationSummary.
        The host name of the replica server, as specified on the replica with the --report-host option. This can differ from the machine name as configured in the operating system.


        :return: The replica_host of this ManagedMySqlDatabaseOutboundReplicationSummary.
        :rtype: str
        """
        return self._replica_host

    @replica_host.setter
    def replica_host(self, replica_host):
        """
        Sets the replica_host of this ManagedMySqlDatabaseOutboundReplicationSummary.
        The host name of the replica server, as specified on the replica with the --report-host option. This can differ from the machine name as configured in the operating system.


        :param replica_host: The replica_host of this ManagedMySqlDatabaseOutboundReplicationSummary.
        :type: str
        """
        self._replica_host = replica_host

    @property
    def replica_port(self):
        """
        Gets the replica_port of this ManagedMySqlDatabaseOutboundReplicationSummary.
        The port on the replica server, as specified on the replica with the --report-port option. A zero in this column means that the replica port (--report-port) was not set.


        :return: The replica_port of this ManagedMySqlDatabaseOutboundReplicationSummary.
        :rtype: int
        """
        return self._replica_port

    @replica_port.setter
    def replica_port(self, replica_port):
        """
        Sets the replica_port of this ManagedMySqlDatabaseOutboundReplicationSummary.
        The port on the replica server, as specified on the replica with the --report-port option. A zero in this column means that the replica port (--report-port) was not set.


        :param replica_port: The replica_port of this ManagedMySqlDatabaseOutboundReplicationSummary.
        :type: int
        """
        self._replica_port = replica_port

    @property
    def replica_uuid(self):
        """
        **[Required]** Gets the replica_uuid of this ManagedMySqlDatabaseOutboundReplicationSummary.
        The Universally Unique Identifier (UUID) value of the replica server.


        :return: The replica_uuid of this ManagedMySqlDatabaseOutboundReplicationSummary.
        :rtype: str
        """
        return self._replica_uuid

    @replica_uuid.setter
    def replica_uuid(self, replica_uuid):
        """
        Sets the replica_uuid of this ManagedMySqlDatabaseOutboundReplicationSummary.
        The Universally Unique Identifier (UUID) value of the replica server.


        :param replica_uuid: The replica_uuid of this ManagedMySqlDatabaseOutboundReplicationSummary.
        :type: str
        """
        self._replica_uuid = replica_uuid

    @property
    def replica_server_id(self):
        """
        **[Required]** Gets the replica_server_id of this ManagedMySqlDatabaseOutboundReplicationSummary.
        The server ID value of the replica.


        :return: The replica_server_id of this ManagedMySqlDatabaseOutboundReplicationSummary.
        :rtype: int
        """
        return self._replica_server_id

    @replica_server_id.setter
    def replica_server_id(self, replica_server_id):
        """
        Sets the replica_server_id of this ManagedMySqlDatabaseOutboundReplicationSummary.
        The server ID value of the replica.


        :param replica_server_id: The replica_server_id of this ManagedMySqlDatabaseOutboundReplicationSummary.
        :type: int
        """
        self._replica_server_id = replica_server_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
