# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataGuardAssociationDetails(object):
    """
    The configuration details for creating a Data Guard association between databases.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the protection_mode property of a CreateDataGuardAssociationDetails.
    #: This constant has a value of "MAXIMUM_AVAILABILITY"
    PROTECTION_MODE_MAXIMUM_AVAILABILITY = "MAXIMUM_AVAILABILITY"

    #: A constant which can be used with the protection_mode property of a CreateDataGuardAssociationDetails.
    #: This constant has a value of "MAXIMUM_PERFORMANCE"
    PROTECTION_MODE_MAXIMUM_PERFORMANCE = "MAXIMUM_PERFORMANCE"

    #: A constant which can be used with the protection_mode property of a CreateDataGuardAssociationDetails.
    #: This constant has a value of "MAXIMUM_PROTECTION"
    PROTECTION_MODE_MAXIMUM_PROTECTION = "MAXIMUM_PROTECTION"

    #: A constant which can be used with the transport_type property of a CreateDataGuardAssociationDetails.
    #: This constant has a value of "SYNC"
    TRANSPORT_TYPE_SYNC = "SYNC"

    #: A constant which can be used with the transport_type property of a CreateDataGuardAssociationDetails.
    #: This constant has a value of "ASYNC"
    TRANSPORT_TYPE_ASYNC = "ASYNC"

    #: A constant which can be used with the transport_type property of a CreateDataGuardAssociationDetails.
    #: This constant has a value of "FASTSYNC"
    TRANSPORT_TYPE_FASTSYNC = "FASTSYNC"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataGuardAssociationDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database.models.CreateDataGuardAssociationWithNewDbSystemDetails`
        * :class:`~oci.database.models.CreateDataGuardAssociationToExistingVmClusterDetails`
        * :class:`~oci.database.models.CreateDataGuardAssociationToExistingDbSystemDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_software_image_id:
            The value to assign to the database_software_image_id property of this CreateDataGuardAssociationDetails.
        :type database_software_image_id: str

        :param database_admin_password:
            The value to assign to the database_admin_password property of this CreateDataGuardAssociationDetails.
        :type database_admin_password: str

        :param protection_mode:
            The value to assign to the protection_mode property of this CreateDataGuardAssociationDetails.
            Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"
        :type protection_mode: str

        :param transport_type:
            The value to assign to the transport_type property of this CreateDataGuardAssociationDetails.
            Allowed values for this property are: "SYNC", "ASYNC", "FASTSYNC"
        :type transport_type: str

        :param creation_type:
            The value to assign to the creation_type property of this CreateDataGuardAssociationDetails.
        :type creation_type: str

        :param is_active_data_guard_enabled:
            The value to assign to the is_active_data_guard_enabled property of this CreateDataGuardAssociationDetails.
        :type is_active_data_guard_enabled: bool

        :param peer_db_unique_name:
            The value to assign to the peer_db_unique_name property of this CreateDataGuardAssociationDetails.
        :type peer_db_unique_name: str

        :param peer_sid_prefix:
            The value to assign to the peer_sid_prefix property of this CreateDataGuardAssociationDetails.
        :type peer_sid_prefix: str

        """
        self.swagger_types = {
            'database_software_image_id': 'str',
            'database_admin_password': 'str',
            'protection_mode': 'str',
            'transport_type': 'str',
            'creation_type': 'str',
            'is_active_data_guard_enabled': 'bool',
            'peer_db_unique_name': 'str',
            'peer_sid_prefix': 'str'
        }

        self.attribute_map = {
            'database_software_image_id': 'databaseSoftwareImageId',
            'database_admin_password': 'databaseAdminPassword',
            'protection_mode': 'protectionMode',
            'transport_type': 'transportType',
            'creation_type': 'creationType',
            'is_active_data_guard_enabled': 'isActiveDataGuardEnabled',
            'peer_db_unique_name': 'peerDbUniqueName',
            'peer_sid_prefix': 'peerSidPrefix'
        }

        self._database_software_image_id = None
        self._database_admin_password = None
        self._protection_mode = None
        self._transport_type = None
        self._creation_type = None
        self._is_active_data_guard_enabled = None
        self._peer_db_unique_name = None
        self._peer_sid_prefix = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['creationType']

        if type == 'NewDbSystem':
            return 'CreateDataGuardAssociationWithNewDbSystemDetails'

        if type == 'ExistingVmCluster':
            return 'CreateDataGuardAssociationToExistingVmClusterDetails'

        if type == 'ExistingDbSystem':
            return 'CreateDataGuardAssociationToExistingDbSystemDetails'
        else:
            return 'CreateDataGuardAssociationDetails'

    @property
    def database_software_image_id(self):
        """
        Gets the database_software_image_id of this CreateDataGuardAssociationDetails.
        The database software image `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_software_image_id of this CreateDataGuardAssociationDetails.
        :rtype: str
        """
        return self._database_software_image_id

    @database_software_image_id.setter
    def database_software_image_id(self, database_software_image_id):
        """
        Sets the database_software_image_id of this CreateDataGuardAssociationDetails.
        The database software image `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_software_image_id: The database_software_image_id of this CreateDataGuardAssociationDetails.
        :type: str
        """
        self._database_software_image_id = database_software_image_id

    @property
    def database_admin_password(self):
        """
        **[Required]** Gets the database_admin_password of this CreateDataGuardAssociationDetails.
        A strong password for the `SYS`, `SYSTEM`, and `PDB Admin` users to apply during standby creation.

        The password must contain no fewer than nine characters and include:

        * At least two uppercase characters.

        * At least two lowercase characters.

        * At least two numeric characters.

        * At least two special characters. Valid special characters include \"_\", \"#\", and \"-\" only.

        **The password MUST be the same as the primary admin password.**


        :return: The database_admin_password of this CreateDataGuardAssociationDetails.
        :rtype: str
        """
        return self._database_admin_password

    @database_admin_password.setter
    def database_admin_password(self, database_admin_password):
        """
        Sets the database_admin_password of this CreateDataGuardAssociationDetails.
        A strong password for the `SYS`, `SYSTEM`, and `PDB Admin` users to apply during standby creation.

        The password must contain no fewer than nine characters and include:

        * At least two uppercase characters.

        * At least two lowercase characters.

        * At least two numeric characters.

        * At least two special characters. Valid special characters include \"_\", \"#\", and \"-\" only.

        **The password MUST be the same as the primary admin password.**


        :param database_admin_password: The database_admin_password of this CreateDataGuardAssociationDetails.
        :type: str
        """
        self._database_admin_password = database_admin_password

    @property
    def protection_mode(self):
        """
        **[Required]** Gets the protection_mode of this CreateDataGuardAssociationDetails.
        The protection mode to set up between the primary and standby databases. For more information, see
        `Oracle Data Guard Protection Modes`__
        in the Oracle Data Guard documentation.

        **IMPORTANT** - The only protection mode currently supported by the Database service is MAXIMUM_PERFORMANCE.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000

        Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"


        :return: The protection_mode of this CreateDataGuardAssociationDetails.
        :rtype: str
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        """
        Sets the protection_mode of this CreateDataGuardAssociationDetails.
        The protection mode to set up between the primary and standby databases. For more information, see
        `Oracle Data Guard Protection Modes`__
        in the Oracle Data Guard documentation.

        **IMPORTANT** - The only protection mode currently supported by the Database service is MAXIMUM_PERFORMANCE.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000


        :param protection_mode: The protection_mode of this CreateDataGuardAssociationDetails.
        :type: str
        """
        allowed_values = ["MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"]
        if not value_allowed_none_or_none_sentinel(protection_mode, allowed_values):
            raise ValueError(
                "Invalid value for `protection_mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._protection_mode = protection_mode

    @property
    def transport_type(self):
        """
        **[Required]** Gets the transport_type of this CreateDataGuardAssociationDetails.
        The redo transport type to use for this Data Guard association.  Valid values depend on the specified `protectionMode`:

        * MAXIMUM_AVAILABILITY - SYNC or FASTSYNC
        * MAXIMUM_PERFORMANCE - ASYNC
        * MAXIMUM_PROTECTION - SYNC

        For more information, see
        `Redo Transport Services`__
        in the Oracle Data Guard documentation.

        **IMPORTANT** - The only transport type currently supported by the Database service is ASYNC.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400

        Allowed values for this property are: "SYNC", "ASYNC", "FASTSYNC"


        :return: The transport_type of this CreateDataGuardAssociationDetails.
        :rtype: str
        """
        return self._transport_type

    @transport_type.setter
    def transport_type(self, transport_type):
        """
        Sets the transport_type of this CreateDataGuardAssociationDetails.
        The redo transport type to use for this Data Guard association.  Valid values depend on the specified `protectionMode`:

        * MAXIMUM_AVAILABILITY - SYNC or FASTSYNC
        * MAXIMUM_PERFORMANCE - ASYNC
        * MAXIMUM_PROTECTION - SYNC

        For more information, see
        `Redo Transport Services`__
        in the Oracle Data Guard documentation.

        **IMPORTANT** - The only transport type currently supported by the Database service is ASYNC.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400


        :param transport_type: The transport_type of this CreateDataGuardAssociationDetails.
        :type: str
        """
        allowed_values = ["SYNC", "ASYNC", "FASTSYNC"]
        if not value_allowed_none_or_none_sentinel(transport_type, allowed_values):
            raise ValueError(
                "Invalid value for `transport_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._transport_type = transport_type

    @property
    def creation_type(self):
        """
        **[Required]** Gets the creation_type of this CreateDataGuardAssociationDetails.
        Specifies whether to create the peer database in an existing DB system or in a new DB system.


        :return: The creation_type of this CreateDataGuardAssociationDetails.
        :rtype: str
        """
        return self._creation_type

    @creation_type.setter
    def creation_type(self, creation_type):
        """
        Sets the creation_type of this CreateDataGuardAssociationDetails.
        Specifies whether to create the peer database in an existing DB system or in a new DB system.


        :param creation_type: The creation_type of this CreateDataGuardAssociationDetails.
        :type: str
        """
        self._creation_type = creation_type

    @property
    def is_active_data_guard_enabled(self):
        """
        Gets the is_active_data_guard_enabled of this CreateDataGuardAssociationDetails.
        True if active Data Guard is enabled.


        :return: The is_active_data_guard_enabled of this CreateDataGuardAssociationDetails.
        :rtype: bool
        """
        return self._is_active_data_guard_enabled

    @is_active_data_guard_enabled.setter
    def is_active_data_guard_enabled(self, is_active_data_guard_enabled):
        """
        Sets the is_active_data_guard_enabled of this CreateDataGuardAssociationDetails.
        True if active Data Guard is enabled.


        :param is_active_data_guard_enabled: The is_active_data_guard_enabled of this CreateDataGuardAssociationDetails.
        :type: bool
        """
        self._is_active_data_guard_enabled = is_active_data_guard_enabled

    @property
    def peer_db_unique_name(self):
        """
        Gets the peer_db_unique_name of this CreateDataGuardAssociationDetails.
        Specifies the `DB_UNIQUE_NAME` of the peer database to be created.


        :return: The peer_db_unique_name of this CreateDataGuardAssociationDetails.
        :rtype: str
        """
        return self._peer_db_unique_name

    @peer_db_unique_name.setter
    def peer_db_unique_name(self, peer_db_unique_name):
        """
        Sets the peer_db_unique_name of this CreateDataGuardAssociationDetails.
        Specifies the `DB_UNIQUE_NAME` of the peer database to be created.


        :param peer_db_unique_name: The peer_db_unique_name of this CreateDataGuardAssociationDetails.
        :type: str
        """
        self._peer_db_unique_name = peer_db_unique_name

    @property
    def peer_sid_prefix(self):
        """
        Gets the peer_sid_prefix of this CreateDataGuardAssociationDetails.
        Specifies a prefix for the `Oracle SID` of the database to be created.


        :return: The peer_sid_prefix of this CreateDataGuardAssociationDetails.
        :rtype: str
        """
        return self._peer_sid_prefix

    @peer_sid_prefix.setter
    def peer_sid_prefix(self, peer_sid_prefix):
        """
        Sets the peer_sid_prefix of this CreateDataGuardAssociationDetails.
        Specifies a prefix for the `Oracle SID` of the database to be created.


        :param peer_sid_prefix: The peer_sid_prefix of this CreateDataGuardAssociationDetails.
        :type: str
        """
        self._peer_sid_prefix = peer_sid_prefix

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
