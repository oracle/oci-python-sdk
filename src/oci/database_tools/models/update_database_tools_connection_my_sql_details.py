# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_database_tools_connection_details import UpdateDatabaseToolsConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDatabaseToolsConnectionMySqlDetails(UpdateDatabaseToolsConnectionDetails):
    """
    The update details for a Database Tools MySQL Server connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDatabaseToolsConnectionMySqlDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_tools.models.UpdateDatabaseToolsConnectionMySqlDetails.type` attribute
        of this class is ``MYSQL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateDatabaseToolsConnectionMySqlDetails.
        :type display_name: str

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDatabaseToolsConnectionMySqlDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDatabaseToolsConnectionMySqlDetails.
        :type freeform_tags: dict(str, str)

        :param type:
            The value to assign to the type property of this UpdateDatabaseToolsConnectionMySqlDetails.
            Allowed values for this property are: "ORACLE_DATABASE", "MYSQL"
        :type type: str

        :param related_resource:
            The value to assign to the related_resource property of this UpdateDatabaseToolsConnectionMySqlDetails.
        :type related_resource: oci.database_tools.models.UpdateDatabaseToolsRelatedResourceMySqlDetails

        :param connection_string:
            The value to assign to the connection_string property of this UpdateDatabaseToolsConnectionMySqlDetails.
        :type connection_string: str

        :param user_name:
            The value to assign to the user_name property of this UpdateDatabaseToolsConnectionMySqlDetails.
        :type user_name: str

        :param user_password:
            The value to assign to the user_password property of this UpdateDatabaseToolsConnectionMySqlDetails.
        :type user_password: oci.database_tools.models.DatabaseToolsUserPasswordDetails

        :param advanced_properties:
            The value to assign to the advanced_properties property of this UpdateDatabaseToolsConnectionMySqlDetails.
        :type advanced_properties: dict(str, str)

        :param key_stores:
            The value to assign to the key_stores property of this UpdateDatabaseToolsConnectionMySqlDetails.
        :type key_stores: list[oci.database_tools.models.DatabaseToolsKeyStoreMySqlDetails]

        :param private_endpoint_id:
            The value to assign to the private_endpoint_id property of this UpdateDatabaseToolsConnectionMySqlDetails.
        :type private_endpoint_id: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'type': 'str',
            'related_resource': 'UpdateDatabaseToolsRelatedResourceMySqlDetails',
            'connection_string': 'str',
            'user_name': 'str',
            'user_password': 'DatabaseToolsUserPasswordDetails',
            'advanced_properties': 'dict(str, str)',
            'key_stores': 'list[DatabaseToolsKeyStoreMySqlDetails]',
            'private_endpoint_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'type': 'type',
            'related_resource': 'relatedResource',
            'connection_string': 'connectionString',
            'user_name': 'userName',
            'user_password': 'userPassword',
            'advanced_properties': 'advancedProperties',
            'key_stores': 'keyStores',
            'private_endpoint_id': 'privateEndpointId'
        }

        self._display_name = None
        self._defined_tags = None
        self._freeform_tags = None
        self._type = None
        self._related_resource = None
        self._connection_string = None
        self._user_name = None
        self._user_password = None
        self._advanced_properties = None
        self._key_stores = None
        self._private_endpoint_id = None
        self._type = 'MYSQL'

    @property
    def related_resource(self):
        """
        Gets the related_resource of this UpdateDatabaseToolsConnectionMySqlDetails.

        :return: The related_resource of this UpdateDatabaseToolsConnectionMySqlDetails.
        :rtype: oci.database_tools.models.UpdateDatabaseToolsRelatedResourceMySqlDetails
        """
        return self._related_resource

    @related_resource.setter
    def related_resource(self, related_resource):
        """
        Sets the related_resource of this UpdateDatabaseToolsConnectionMySqlDetails.

        :param related_resource: The related_resource of this UpdateDatabaseToolsConnectionMySqlDetails.
        :type: oci.database_tools.models.UpdateDatabaseToolsRelatedResourceMySqlDetails
        """
        self._related_resource = related_resource

    @property
    def connection_string(self):
        """
        Gets the connection_string of this UpdateDatabaseToolsConnectionMySqlDetails.
        The connection string used to connect to the MySQL Server.


        :return: The connection_string of this UpdateDatabaseToolsConnectionMySqlDetails.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this UpdateDatabaseToolsConnectionMySqlDetails.
        The connection string used to connect to the MySQL Server.


        :param connection_string: The connection_string of this UpdateDatabaseToolsConnectionMySqlDetails.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def user_name(self):
        """
        Gets the user_name of this UpdateDatabaseToolsConnectionMySqlDetails.
        The user name.


        :return: The user_name of this UpdateDatabaseToolsConnectionMySqlDetails.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this UpdateDatabaseToolsConnectionMySqlDetails.
        The user name.


        :param user_name: The user_name of this UpdateDatabaseToolsConnectionMySqlDetails.
        :type: str
        """
        self._user_name = user_name

    @property
    def user_password(self):
        """
        Gets the user_password of this UpdateDatabaseToolsConnectionMySqlDetails.

        :return: The user_password of this UpdateDatabaseToolsConnectionMySqlDetails.
        :rtype: oci.database_tools.models.DatabaseToolsUserPasswordDetails
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        """
        Sets the user_password of this UpdateDatabaseToolsConnectionMySqlDetails.

        :param user_password: The user_password of this UpdateDatabaseToolsConnectionMySqlDetails.
        :type: oci.database_tools.models.DatabaseToolsUserPasswordDetails
        """
        self._user_password = user_password

    @property
    def advanced_properties(self):
        """
        Gets the advanced_properties of this UpdateDatabaseToolsConnectionMySqlDetails.
        The advanced connection properties key-value pair (e.g., `sslMode`).


        :return: The advanced_properties of this UpdateDatabaseToolsConnectionMySqlDetails.
        :rtype: dict(str, str)
        """
        return self._advanced_properties

    @advanced_properties.setter
    def advanced_properties(self, advanced_properties):
        """
        Sets the advanced_properties of this UpdateDatabaseToolsConnectionMySqlDetails.
        The advanced connection properties key-value pair (e.g., `sslMode`).


        :param advanced_properties: The advanced_properties of this UpdateDatabaseToolsConnectionMySqlDetails.
        :type: dict(str, str)
        """
        self._advanced_properties = advanced_properties

    @property
    def key_stores(self):
        """
        Gets the key_stores of this UpdateDatabaseToolsConnectionMySqlDetails.
        The CA certificate to verify the server's certificate and
        the client private key and associated certificate required for client authentication.


        :return: The key_stores of this UpdateDatabaseToolsConnectionMySqlDetails.
        :rtype: list[oci.database_tools.models.DatabaseToolsKeyStoreMySqlDetails]
        """
        return self._key_stores

    @key_stores.setter
    def key_stores(self, key_stores):
        """
        Sets the key_stores of this UpdateDatabaseToolsConnectionMySqlDetails.
        The CA certificate to verify the server's certificate and
        the client private key and associated certificate required for client authentication.


        :param key_stores: The key_stores of this UpdateDatabaseToolsConnectionMySqlDetails.
        :type: list[oci.database_tools.models.DatabaseToolsKeyStoreMySqlDetails]
        """
        self._key_stores = key_stores

    @property
    def private_endpoint_id(self):
        """
        Gets the private_endpoint_id of this UpdateDatabaseToolsConnectionMySqlDetails.
        The `OCID`__ of the DatabaseToolsPrivateEndpoint used to access the database in the Customer VCN.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The private_endpoint_id of this UpdateDatabaseToolsConnectionMySqlDetails.
        :rtype: str
        """
        return self._private_endpoint_id

    @private_endpoint_id.setter
    def private_endpoint_id(self, private_endpoint_id):
        """
        Sets the private_endpoint_id of this UpdateDatabaseToolsConnectionMySqlDetails.
        The `OCID`__ of the DatabaseToolsPrivateEndpoint used to access the database in the Customer VCN.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param private_endpoint_id: The private_endpoint_id of this UpdateDatabaseToolsConnectionMySqlDetails.
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
