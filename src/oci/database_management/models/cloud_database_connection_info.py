# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101

from .cloud_db_system_connection_info import CloudDbSystemConnectionInfo
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloudDatabaseConnectionInfo(CloudDbSystemConnectionInfo):
    """
    The details required to connect to a cloud Oracle Database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CloudDatabaseConnectionInfo object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.CloudDatabaseConnectionInfo.component_type` attribute
        of this class is ``DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param component_type:
            The value to assign to the component_type property of this CloudDatabaseConnectionInfo.
            Allowed values for this property are: "DATABASE", "ASM"
        :type component_type: str

        :param connection_string:
            The value to assign to the connection_string property of this CloudDatabaseConnectionInfo.
        :type connection_string: oci.database_management.models.DatabaseConnectionString

        :param connection_credentials:
            The value to assign to the connection_credentials property of this CloudDatabaseConnectionInfo.
        :type connection_credentials: oci.database_management.models.DatabaseConnectionCredentials

        """
        self.swagger_types = {
            'component_type': 'str',
            'connection_string': 'DatabaseConnectionString',
            'connection_credentials': 'DatabaseConnectionCredentials'
        }
        self.attribute_map = {
            'component_type': 'componentType',
            'connection_string': 'connectionString',
            'connection_credentials': 'connectionCredentials'
        }
        self._component_type = None
        self._connection_string = None
        self._connection_credentials = None
        self._component_type = 'DATABASE'

    @property
    def connection_string(self):
        """
        **[Required]** Gets the connection_string of this CloudDatabaseConnectionInfo.

        :return: The connection_string of this CloudDatabaseConnectionInfo.
        :rtype: oci.database_management.models.DatabaseConnectionString
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this CloudDatabaseConnectionInfo.

        :param connection_string: The connection_string of this CloudDatabaseConnectionInfo.
        :type: oci.database_management.models.DatabaseConnectionString
        """
        self._connection_string = connection_string

    @property
    def connection_credentials(self):
        """
        Gets the connection_credentials of this CloudDatabaseConnectionInfo.

        :return: The connection_credentials of this CloudDatabaseConnectionInfo.
        :rtype: oci.database_management.models.DatabaseConnectionCredentials
        """
        return self._connection_credentials

    @connection_credentials.setter
    def connection_credentials(self, connection_credentials):
        """
        Sets the connection_credentials of this CloudDatabaseConnectionInfo.

        :param connection_credentials: The connection_credentials of this CloudDatabaseConnectionInfo.
        :type: oci.database_management.models.DatabaseConnectionCredentials
        """
        self._connection_credentials = connection_credentials

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
