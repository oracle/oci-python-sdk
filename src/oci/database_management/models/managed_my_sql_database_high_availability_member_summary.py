# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedMySqlDatabaseHighAvailabilityMemberSummary(object):
    """
    Information about a member of a MySQL server group replication for high availability.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedMySqlDatabaseHighAvailabilityMemberSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param member_host:
            The value to assign to the member_host property of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        :type member_host: str

        :param member_port:
            The value to assign to the member_port property of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        :type member_port: int

        :param member_state:
            The value to assign to the member_state property of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        :type member_state: str

        :param member_role:
            The value to assign to the member_role property of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        :type member_role: str

        :param member_uuid:
            The value to assign to the member_uuid property of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        :type member_uuid: str

        """
        self.swagger_types = {
            'member_host': 'str',
            'member_port': 'int',
            'member_state': 'str',
            'member_role': 'str',
            'member_uuid': 'str'
        }
        self.attribute_map = {
            'member_host': 'memberHost',
            'member_port': 'memberPort',
            'member_state': 'memberState',
            'member_role': 'memberRole',
            'member_uuid': 'memberUuid'
        }
        self._member_host = None
        self._member_port = None
        self._member_state = None
        self._member_role = None
        self._member_uuid = None

    @property
    def member_host(self):
        """
        **[Required]** Gets the member_host of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        The host name of the group member that clients use to connect to it.


        :return: The member_host of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        :rtype: str
        """
        return self._member_host

    @member_host.setter
    def member_host(self, member_host):
        """
        Sets the member_host of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        The host name of the group member that clients use to connect to it.


        :param member_host: The member_host of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        :type: str
        """
        self._member_host = member_host

    @property
    def member_port(self):
        """
        **[Required]** Gets the member_port of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        The port number of the group member that clients use to connect to it.


        :return: The member_port of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        :rtype: int
        """
        return self._member_port

    @member_port.setter
    def member_port(self, member_port):
        """
        Sets the member_port of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        The port number of the group member that clients use to connect to it.


        :param member_port: The member_port of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        :type: int
        """
        self._member_port = member_port

    @property
    def member_state(self):
        """
        Gets the member_state of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        The current state of the group member.


        :return: The member_state of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        :rtype: str
        """
        return self._member_state

    @member_state.setter
    def member_state(self, member_state):
        """
        Sets the member_state of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        The current state of the group member.


        :param member_state: The member_state of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        :type: str
        """
        self._member_state = member_state

    @property
    def member_role(self):
        """
        Gets the member_role of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        The current role of the group member in the group.


        :return: The member_role of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        :rtype: str
        """
        return self._member_role

    @member_role.setter
    def member_role(self, member_role):
        """
        Sets the member_role of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        The current role of the group member in the group.


        :param member_role: The member_role of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        :type: str
        """
        self._member_role = member_role

    @property
    def member_uuid(self):
        """
        **[Required]** Gets the member_uuid of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        The Universally Unique Identifier (UUID) of the member server.


        :return: The member_uuid of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        :rtype: str
        """
        return self._member_uuid

    @member_uuid.setter
    def member_uuid(self, member_uuid):
        """
        Sets the member_uuid of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        The Universally Unique Identifier (UUID) of the member server.


        :param member_uuid: The member_uuid of this ManagedMySqlDatabaseHighAvailabilityMemberSummary.
        :type: str
        """
        self._member_uuid = member_uuid

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
