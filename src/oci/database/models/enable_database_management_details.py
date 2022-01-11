# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnableDatabaseManagementDetails(object):
    """
    Data to enable the Database Management service for the database.
    """

    #: A constant which can be used with the management_type property of a EnableDatabaseManagementDetails.
    #: This constant has a value of "BASIC"
    MANAGEMENT_TYPE_BASIC = "BASIC"

    #: A constant which can be used with the management_type property of a EnableDatabaseManagementDetails.
    #: This constant has a value of "ADVANCED"
    MANAGEMENT_TYPE_ADVANCED = "ADVANCED"

    def __init__(self, **kwargs):
        """
        Initializes a new EnableDatabaseManagementDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_details:
            The value to assign to the credential_details property of this EnableDatabaseManagementDetails.
        :type credential_details: oci.database.models.DatabaseCredentialDetails

        :param private_end_point_id:
            The value to assign to the private_end_point_id property of this EnableDatabaseManagementDetails.
        :type private_end_point_id: str

        :param management_type:
            The value to assign to the management_type property of this EnableDatabaseManagementDetails.
            Allowed values for this property are: "BASIC", "ADVANCED"
        :type management_type: str

        :param service_name:
            The value to assign to the service_name property of this EnableDatabaseManagementDetails.
        :type service_name: str

        """
        self.swagger_types = {
            'credential_details': 'DatabaseCredentialDetails',
            'private_end_point_id': 'str',
            'management_type': 'str',
            'service_name': 'str'
        }

        self.attribute_map = {
            'credential_details': 'credentialDetails',
            'private_end_point_id': 'privateEndPointId',
            'management_type': 'managementType',
            'service_name': 'serviceName'
        }

        self._credential_details = None
        self._private_end_point_id = None
        self._management_type = None
        self._service_name = None

    @property
    def credential_details(self):
        """
        **[Required]** Gets the credential_details of this EnableDatabaseManagementDetails.

        :return: The credential_details of this EnableDatabaseManagementDetails.
        :rtype: oci.database.models.DatabaseCredentialDetails
        """
        return self._credential_details

    @credential_details.setter
    def credential_details(self, credential_details):
        """
        Sets the credential_details of this EnableDatabaseManagementDetails.

        :param credential_details: The credential_details of this EnableDatabaseManagementDetails.
        :type: oci.database.models.DatabaseCredentialDetails
        """
        self._credential_details = credential_details

    @property
    def private_end_point_id(self):
        """
        **[Required]** Gets the private_end_point_id of this EnableDatabaseManagementDetails.
        The `OCID`__ of the private endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The private_end_point_id of this EnableDatabaseManagementDetails.
        :rtype: str
        """
        return self._private_end_point_id

    @private_end_point_id.setter
    def private_end_point_id(self, private_end_point_id):
        """
        Sets the private_end_point_id of this EnableDatabaseManagementDetails.
        The `OCID`__ of the private endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param private_end_point_id: The private_end_point_id of this EnableDatabaseManagementDetails.
        :type: str
        """
        self._private_end_point_id = private_end_point_id

    @property
    def management_type(self):
        """
        Gets the management_type of this EnableDatabaseManagementDetails.
        The Database Management type.

        Allowed values for this property are: "BASIC", "ADVANCED"


        :return: The management_type of this EnableDatabaseManagementDetails.
        :rtype: str
        """
        return self._management_type

    @management_type.setter
    def management_type(self, management_type):
        """
        Sets the management_type of this EnableDatabaseManagementDetails.
        The Database Management type.


        :param management_type: The management_type of this EnableDatabaseManagementDetails.
        :type: str
        """
        allowed_values = ["BASIC", "ADVANCED"]
        if not value_allowed_none_or_none_sentinel(management_type, allowed_values):
            raise ValueError(
                "Invalid value for `management_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._management_type = management_type

    @property
    def service_name(self):
        """
        **[Required]** Gets the service_name of this EnableDatabaseManagementDetails.
        The name of the Oracle Database service that will be used to connect to the database.


        :return: The service_name of this EnableDatabaseManagementDetails.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this EnableDatabaseManagementDetails.
        The name of the Oracle Database service that will be used to connect to the database.


        :param service_name: The service_name of this EnableDatabaseManagementDetails.
        :type: str
        """
        self._service_name = service_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
