# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_external_db_system_connector_details import UpdateExternalDbSystemConnectorDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateExternalDbSystemMacsConnectorDetails(UpdateExternalDbSystemConnectorDetails):
    """
    The details for updating the external `Management Agent Cloud Service (MACS)`__
    connector used to connect to an external DB system component.

    __ https://docs.cloud.oracle.com/iaas/management-agents/index.html
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateExternalDbSystemMacsConnectorDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.UpdateExternalDbSystemMacsConnectorDetails.connector_type` attribute
        of this class is ``MACS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connector_type:
            The value to assign to the connector_type property of this UpdateExternalDbSystemMacsConnectorDetails.
            Allowed values for this property are: "MACS"
        :type connector_type: str

        :param connection_info:
            The value to assign to the connection_info property of this UpdateExternalDbSystemMacsConnectorDetails.
        :type connection_info: oci.database_management.models.ExternalDbSystemConnectionInfo

        """
        self.swagger_types = {
            'connector_type': 'str',
            'connection_info': 'ExternalDbSystemConnectionInfo'
        }

        self.attribute_map = {
            'connector_type': 'connectorType',
            'connection_info': 'connectionInfo'
        }

        self._connector_type = None
        self._connection_info = None
        self._connector_type = 'MACS'

    @property
    def connection_info(self):
        """
        **[Required]** Gets the connection_info of this UpdateExternalDbSystemMacsConnectorDetails.

        :return: The connection_info of this UpdateExternalDbSystemMacsConnectorDetails.
        :rtype: oci.database_management.models.ExternalDbSystemConnectionInfo
        """
        return self._connection_info

    @connection_info.setter
    def connection_info(self, connection_info):
        """
        Sets the connection_info of this UpdateExternalDbSystemMacsConnectorDetails.

        :param connection_info: The connection_info of this UpdateExternalDbSystemMacsConnectorDetails.
        :type: oci.database_management.models.ExternalDbSystemConnectionInfo
        """
        self._connection_info = connection_info

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
