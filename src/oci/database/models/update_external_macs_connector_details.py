# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_external_database_connector_details import UpdateExternalDatabaseConnectorDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateExternalMacsConnectorDetails(UpdateExternalDatabaseConnectorDetails):
    """
    Details for updating an external `Management Agent cloud service (MACS)`__ database connection.

    __ https://docs.cloud.oracle.com/iaas/management-agents/index.html
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateExternalMacsConnectorDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.UpdateExternalMacsConnectorDetails.connector_type` attribute
        of this class is ``MACS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateExternalMacsConnectorDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateExternalMacsConnectorDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateExternalMacsConnectorDetails.
        :type display_name: str

        :param connector_type:
            The value to assign to the connector_type property of this UpdateExternalMacsConnectorDetails.
            Allowed values for this property are: "MACS"
        :type connector_type: str

        :param connection_string:
            The value to assign to the connection_string property of this UpdateExternalMacsConnectorDetails.
        :type connection_string: oci.database.models.DatabaseConnectionString

        :param connection_credentials:
            The value to assign to the connection_credentials property of this UpdateExternalMacsConnectorDetails.
        :type connection_credentials: oci.database.models.DatabaseConnectionCredentials

        """
        self.swagger_types = {
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'connector_type': 'str',
            'connection_string': 'DatabaseConnectionString',
            'connection_credentials': 'DatabaseConnectionCredentials'
        }

        self.attribute_map = {
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'connector_type': 'connectorType',
            'connection_string': 'connectionString',
            'connection_credentials': 'connectionCredentials'
        }

        self._freeform_tags = None
        self._defined_tags = None
        self._display_name = None
        self._connector_type = None
        self._connection_string = None
        self._connection_credentials = None
        self._connector_type = 'MACS'

    @property
    def connection_string(self):
        """
        Gets the connection_string of this UpdateExternalMacsConnectorDetails.

        :return: The connection_string of this UpdateExternalMacsConnectorDetails.
        :rtype: oci.database.models.DatabaseConnectionString
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this UpdateExternalMacsConnectorDetails.

        :param connection_string: The connection_string of this UpdateExternalMacsConnectorDetails.
        :type: oci.database.models.DatabaseConnectionString
        """
        self._connection_string = connection_string

    @property
    def connection_credentials(self):
        """
        Gets the connection_credentials of this UpdateExternalMacsConnectorDetails.

        :return: The connection_credentials of this UpdateExternalMacsConnectorDetails.
        :rtype: oci.database.models.DatabaseConnectionCredentials
        """
        return self._connection_credentials

    @connection_credentials.setter
    def connection_credentials(self, connection_credentials):
        """
        Sets the connection_credentials of this UpdateExternalMacsConnectorDetails.

        :param connection_credentials: The connection_credentials of this UpdateExternalMacsConnectorDetails.
        :type: oci.database.models.DatabaseConnectionCredentials
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
