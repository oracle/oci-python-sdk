# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangePeComanagedDatabaseInsightDetails(object):
    """
    Details of a Private Endpoint co-managed database insight.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangePeComanagedDatabaseInsightDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param service_name:
            The value to assign to the service_name property of this ChangePeComanagedDatabaseInsightDetails.
        :type service_name: str

        :param credential_details:
            The value to assign to the credential_details property of this ChangePeComanagedDatabaseInsightDetails.
        :type credential_details: oci.opsi.models.CredentialDetails

        :param opsi_private_endpoint_id:
            The value to assign to the opsi_private_endpoint_id property of this ChangePeComanagedDatabaseInsightDetails.
        :type opsi_private_endpoint_id: str

        """
        self.swagger_types = {
            'service_name': 'str',
            'credential_details': 'CredentialDetails',
            'opsi_private_endpoint_id': 'str'
        }

        self.attribute_map = {
            'service_name': 'serviceName',
            'credential_details': 'credentialDetails',
            'opsi_private_endpoint_id': 'opsiPrivateEndpointId'
        }

        self._service_name = None
        self._credential_details = None
        self._opsi_private_endpoint_id = None

    @property
    def service_name(self):
        """
        **[Required]** Gets the service_name of this ChangePeComanagedDatabaseInsightDetails.
        Database service name used for connection requests.


        :return: The service_name of this ChangePeComanagedDatabaseInsightDetails.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this ChangePeComanagedDatabaseInsightDetails.
        Database service name used for connection requests.


        :param service_name: The service_name of this ChangePeComanagedDatabaseInsightDetails.
        :type: str
        """
        self._service_name = service_name

    @property
    def credential_details(self):
        """
        **[Required]** Gets the credential_details of this ChangePeComanagedDatabaseInsightDetails.

        :return: The credential_details of this ChangePeComanagedDatabaseInsightDetails.
        :rtype: oci.opsi.models.CredentialDetails
        """
        return self._credential_details

    @credential_details.setter
    def credential_details(self, credential_details):
        """
        Sets the credential_details of this ChangePeComanagedDatabaseInsightDetails.

        :param credential_details: The credential_details of this ChangePeComanagedDatabaseInsightDetails.
        :type: oci.opsi.models.CredentialDetails
        """
        self._credential_details = credential_details

    @property
    def opsi_private_endpoint_id(self):
        """
        **[Required]** Gets the opsi_private_endpoint_id of this ChangePeComanagedDatabaseInsightDetails.
        The `OCID`__ of the OPSI private endpoint

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The opsi_private_endpoint_id of this ChangePeComanagedDatabaseInsightDetails.
        :rtype: str
        """
        return self._opsi_private_endpoint_id

    @opsi_private_endpoint_id.setter
    def opsi_private_endpoint_id(self, opsi_private_endpoint_id):
        """
        Sets the opsi_private_endpoint_id of this ChangePeComanagedDatabaseInsightDetails.
        The `OCID`__ of the OPSI private endpoint

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param opsi_private_endpoint_id: The opsi_private_endpoint_id of this ChangePeComanagedDatabaseInsightDetails.
        :type: str
        """
        self._opsi_private_endpoint_id = opsi_private_endpoint_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
