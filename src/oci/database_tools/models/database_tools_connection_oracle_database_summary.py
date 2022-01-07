# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_tools_connection_summary import DatabaseToolsConnectionSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseToolsConnectionOracleDatabaseSummary(DatabaseToolsConnectionSummary):
    """
    DatabaseToolsConnectionSummary of an Oracle Database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseToolsConnectionOracleDatabaseSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.database_tools.models.DatabaseToolsConnectionOracleDatabaseSummary.type` attribute
        of this class is ``ORACLE_DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DatabaseToolsConnectionOracleDatabaseSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type time_updated: datetime

        :param defined_tags:
            The value to assign to the defined_tags property of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type freeform_tags: dict(str, str)

        :param system_tags:
            The value to assign to the system_tags property of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type system_tags: dict(str, dict(str, object))

        :param type:
            The value to assign to the type property of this DatabaseToolsConnectionOracleDatabaseSummary.
            Allowed values for this property are: "ORACLE_DATABASE"
        :type type: str

        :param related_resource:
            The value to assign to the related_resource property of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type related_resource: oci.database_tools.models.DatabaseToolsRelatedResource

        :param connection_string:
            The value to assign to the connection_string property of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type connection_string: str

        :param user_name:
            The value to assign to the user_name property of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type user_name: str

        :param user_password:
            The value to assign to the user_password property of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type user_password: oci.database_tools.models.DatabaseToolsUserPasswordSummary

        :param advanced_properties:
            The value to assign to the advanced_properties property of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type advanced_properties: dict(str, str)

        :param key_stores:
            The value to assign to the key_stores property of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type key_stores: list[oci.database_tools.models.DatabaseToolsKeyStoreSummary]

        :param private_endpoint_id:
            The value to assign to the private_endpoint_id property of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type private_endpoint_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'system_tags': 'dict(str, dict(str, object))',
            'type': 'str',
            'related_resource': 'DatabaseToolsRelatedResource',
            'connection_string': 'str',
            'user_name': 'str',
            'user_password': 'DatabaseToolsUserPasswordSummary',
            'advanced_properties': 'dict(str, str)',
            'key_stores': 'list[DatabaseToolsKeyStoreSummary]',
            'private_endpoint_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'system_tags': 'systemTags',
            'type': 'type',
            'related_resource': 'relatedResource',
            'connection_string': 'connectionString',
            'user_name': 'userName',
            'user_password': 'userPassword',
            'advanced_properties': 'advancedProperties',
            'key_stores': 'keyStores',
            'private_endpoint_id': 'privateEndpointId'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._defined_tags = None
        self._freeform_tags = None
        self._system_tags = None
        self._type = None
        self._related_resource = None
        self._connection_string = None
        self._user_name = None
        self._user_password = None
        self._advanced_properties = None
        self._key_stores = None
        self._private_endpoint_id = None
        self._type = 'ORACLE_DATABASE'

    @property
    def related_resource(self):
        """
        Gets the related_resource of this DatabaseToolsConnectionOracleDatabaseSummary.

        :return: The related_resource of this DatabaseToolsConnectionOracleDatabaseSummary.
        :rtype: oci.database_tools.models.DatabaseToolsRelatedResource
        """
        return self._related_resource

    @related_resource.setter
    def related_resource(self, related_resource):
        """
        Sets the related_resource of this DatabaseToolsConnectionOracleDatabaseSummary.

        :param related_resource: The related_resource of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type: oci.database_tools.models.DatabaseToolsRelatedResource
        """
        self._related_resource = related_resource

    @property
    def connection_string(self):
        """
        Gets the connection_string of this DatabaseToolsConnectionOracleDatabaseSummary.
        Connect descriptor or Easy Connect Naming method to connect to the database.


        :return: The connection_string of this DatabaseToolsConnectionOracleDatabaseSummary.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this DatabaseToolsConnectionOracleDatabaseSummary.
        Connect descriptor or Easy Connect Naming method to connect to the database.


        :param connection_string: The connection_string of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def user_name(self):
        """
        Gets the user_name of this DatabaseToolsConnectionOracleDatabaseSummary.
        Database user name.


        :return: The user_name of this DatabaseToolsConnectionOracleDatabaseSummary.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this DatabaseToolsConnectionOracleDatabaseSummary.
        Database user name.


        :param user_name: The user_name of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type: str
        """
        self._user_name = user_name

    @property
    def user_password(self):
        """
        Gets the user_password of this DatabaseToolsConnectionOracleDatabaseSummary.

        :return: The user_password of this DatabaseToolsConnectionOracleDatabaseSummary.
        :rtype: oci.database_tools.models.DatabaseToolsUserPasswordSummary
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        """
        Sets the user_password of this DatabaseToolsConnectionOracleDatabaseSummary.

        :param user_password: The user_password of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type: oci.database_tools.models.DatabaseToolsUserPasswordSummary
        """
        self._user_password = user_password

    @property
    def advanced_properties(self):
        """
        Gets the advanced_properties of this DatabaseToolsConnectionOracleDatabaseSummary.
        Advanced connection properties key-value pair (e.g., oracle.net.ssl_server_dn_match).


        :return: The advanced_properties of this DatabaseToolsConnectionOracleDatabaseSummary.
        :rtype: dict(str, str)
        """
        return self._advanced_properties

    @advanced_properties.setter
    def advanced_properties(self, advanced_properties):
        """
        Sets the advanced_properties of this DatabaseToolsConnectionOracleDatabaseSummary.
        Advanced connection properties key-value pair (e.g., oracle.net.ssl_server_dn_match).


        :param advanced_properties: The advanced_properties of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type: dict(str, str)
        """
        self._advanced_properties = advanced_properties

    @property
    def key_stores(self):
        """
        Gets the key_stores of this DatabaseToolsConnectionOracleDatabaseSummary.
        Oracle wallet or Java Keystores containing trusted certificates for authenticating the server's public certificate and
        the client private key and associated certificates required for client authentication.


        :return: The key_stores of this DatabaseToolsConnectionOracleDatabaseSummary.
        :rtype: list[oci.database_tools.models.DatabaseToolsKeyStoreSummary]
        """
        return self._key_stores

    @key_stores.setter
    def key_stores(self, key_stores):
        """
        Sets the key_stores of this DatabaseToolsConnectionOracleDatabaseSummary.
        Oracle wallet or Java Keystores containing trusted certificates for authenticating the server's public certificate and
        the client private key and associated certificates required for client authentication.


        :param key_stores: The key_stores of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type: list[oci.database_tools.models.DatabaseToolsKeyStoreSummary]
        """
        self._key_stores = key_stores

    @property
    def private_endpoint_id(self):
        """
        Gets the private_endpoint_id of this DatabaseToolsConnectionOracleDatabaseSummary.
        The `OCID`__ of the DatabaseToolsPrivateEndpoint used to access the database in the Customer VCN.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The private_endpoint_id of this DatabaseToolsConnectionOracleDatabaseSummary.
        :rtype: str
        """
        return self._private_endpoint_id

    @private_endpoint_id.setter
    def private_endpoint_id(self, private_endpoint_id):
        """
        Sets the private_endpoint_id of this DatabaseToolsConnectionOracleDatabaseSummary.
        The `OCID`__ of the DatabaseToolsPrivateEndpoint used to access the database in the Customer VCN.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param private_endpoint_id: The private_endpoint_id of this DatabaseToolsConnectionOracleDatabaseSummary.
        :type: str
        """
        self._private_endpoint_id = private_endpoint_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
