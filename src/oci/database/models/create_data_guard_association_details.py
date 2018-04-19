# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataGuardAssociationDetails(object):
    """
    The configuration details for creating a Data Guard association between databases.

    **NOTE:**
    \"ExistingDbSystem\" is the only supported `creationType` value. Therefore, all
    :func:`create_data_guard_association`
    requests must include the `peerDbSystemId` parameter found in the
    :func:`create_data_guard_association_to_existing_db_system_details`
    object.
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

        * :class:`~oci.database.models.CreateDataGuardAssociationToExistingDbSystemDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param creation_type:
            The value to assign to the creation_type property of this CreateDataGuardAssociationDetails.
        :type creation_type: str

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

        """
        self.swagger_types = {
            'creation_type': 'str',
            'database_admin_password': 'str',
            'protection_mode': 'str',
            'transport_type': 'str'
        }

        self.attribute_map = {
            'creation_type': 'creationType',
            'database_admin_password': 'databaseAdminPassword',
            'protection_mode': 'protectionMode',
            'transport_type': 'transportType'
        }

        self._creation_type = None
        self._database_admin_password = None
        self._protection_mode = None
        self._transport_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['creationType']

        if type == 'ExistingDbSystem':
            return 'CreateDataGuardAssociationToExistingDbSystemDetails'
        else:
            return 'CreateDataGuardAssociationDetails'

    @property
    def creation_type(self):
        """
        **[Required]** Gets the creation_type of this CreateDataGuardAssociationDetails.
        Specifies where to create the associated database.
        \"ExistingDbSystem\" is the only supported `creationType` value.


        :return: The creation_type of this CreateDataGuardAssociationDetails.
        :rtype: str
        """
        return self._creation_type

    @creation_type.setter
    def creation_type(self, creation_type):
        """
        Sets the creation_type of this CreateDataGuardAssociationDetails.
        Specifies where to create the associated database.
        \"ExistingDbSystem\" is the only supported `creationType` value.


        :param creation_type: The creation_type of this CreateDataGuardAssociationDetails.
        :type: str
        """
        self._creation_type = creation_type

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

        **IMPORTANT** - The only protection mode currently supported by the Database Service is MAXIMUM_PERFORMANCE.

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

        **IMPORTANT** - The only protection mode currently supported by the Database Service is MAXIMUM_PERFORMANCE.

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

        **IMPORTANT** - The only transport type currently supported by the Database Service is ASYNC.

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

        **IMPORTANT** - The only transport type currently supported by the Database Service is ASYNC.

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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
