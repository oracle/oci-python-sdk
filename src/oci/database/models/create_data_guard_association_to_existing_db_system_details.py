# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_data_guard_association_details import CreateDataGuardAssociationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataGuardAssociationToExistingDbSystemDetails(CreateDataGuardAssociationDetails):
    """
    The configuration details for creating a Data Guard association for a bare metal or Exadata DB system database. For these types of DB system databases, the `creationType` should be `ExistingDbSystem`. A standby database will be created in the DB system you specify.

    To create a Data Guard association for a database in a virtual machine DB system, use the :func:`create_data_guard_association_with_new_db_system_details` subtype instead.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataGuardAssociationToExistingDbSystemDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateDataGuardAssociationToExistingDbSystemDetails.creation_type` attribute
        of this class is ``ExistingDbSystem`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_admin_password:
            The value to assign to the database_admin_password property of this CreateDataGuardAssociationToExistingDbSystemDetails.
        :type database_admin_password: str

        :param protection_mode:
            The value to assign to the protection_mode property of this CreateDataGuardAssociationToExistingDbSystemDetails.
            Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"
        :type protection_mode: str

        :param transport_type:
            The value to assign to the transport_type property of this CreateDataGuardAssociationToExistingDbSystemDetails.
            Allowed values for this property are: "SYNC", "ASYNC", "FASTSYNC"
        :type transport_type: str

        :param creation_type:
            The value to assign to the creation_type property of this CreateDataGuardAssociationToExistingDbSystemDetails.
        :type creation_type: str

        :param peer_db_system_id:
            The value to assign to the peer_db_system_id property of this CreateDataGuardAssociationToExistingDbSystemDetails.
        :type peer_db_system_id: str

        """
        self.swagger_types = {
            'database_admin_password': 'str',
            'protection_mode': 'str',
            'transport_type': 'str',
            'creation_type': 'str',
            'peer_db_system_id': 'str'
        }

        self.attribute_map = {
            'database_admin_password': 'databaseAdminPassword',
            'protection_mode': 'protectionMode',
            'transport_type': 'transportType',
            'creation_type': 'creationType',
            'peer_db_system_id': 'peerDbSystemId'
        }

        self._database_admin_password = None
        self._protection_mode = None
        self._transport_type = None
        self._creation_type = None
        self._peer_db_system_id = None
        self._creation_type = 'ExistingDbSystem'

    @property
    def peer_db_system_id(self):
        """
        Gets the peer_db_system_id of this CreateDataGuardAssociationToExistingDbSystemDetails.
        The `OCID`__ of the DB system in which to create the standby database.
        You must supply this value if creationType is `ExistingDbSystem`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The peer_db_system_id of this CreateDataGuardAssociationToExistingDbSystemDetails.
        :rtype: str
        """
        return self._peer_db_system_id

    @peer_db_system_id.setter
    def peer_db_system_id(self, peer_db_system_id):
        """
        Sets the peer_db_system_id of this CreateDataGuardAssociationToExistingDbSystemDetails.
        The `OCID`__ of the DB system in which to create the standby database.
        You must supply this value if creationType is `ExistingDbSystem`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


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
