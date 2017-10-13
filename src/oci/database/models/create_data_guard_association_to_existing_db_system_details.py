# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .create_data_guard_association_details import CreateDataGuardAssociationDetails
from ...util import formatted_flat_dict


class CreateDataGuardAssociationToExistingDbSystemDetails(CreateDataGuardAssociationDetails):

    def __init__(self):

        self.swagger_types = {
            'creation_type': 'str',
            'database_admin_password': 'str',
            'protection_mode': 'str',
            'transport_type': 'str',
            'peer_db_system_id': 'str'
        }

        self.attribute_map = {
            'creation_type': 'creationType',
            'database_admin_password': 'databaseAdminPassword',
            'protection_mode': 'protectionMode',
            'transport_type': 'transportType',
            'peer_db_system_id': 'peerDbSystemId'
        }

        self._creation_type = None
        self._database_admin_password = None
        self._protection_mode = None
        self._transport_type = None
        self._peer_db_system_id = None
        self._creation_type = 'ExistingDbSystem'

    @property
    def peer_db_system_id(self):
        """
        Gets the peer_db_system_id of this CreateDataGuardAssociationToExistingDbSystemDetails.
        The `OCID`__ of the DB System to create the standby database on.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The peer_db_system_id of this CreateDataGuardAssociationToExistingDbSystemDetails.
        :rtype: str
        """
        return self._peer_db_system_id

    @peer_db_system_id.setter
    def peer_db_system_id(self, peer_db_system_id):
        """
        Sets the peer_db_system_id of this CreateDataGuardAssociationToExistingDbSystemDetails.
        The `OCID`__ of the DB System to create the standby database on.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param peer_db_system_id: The peer_db_system_id of this CreateDataGuardAssociationToExistingDbSystemDetails.
        :type: str
        """
        self._peer_db_system_id = peer_db_system_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
