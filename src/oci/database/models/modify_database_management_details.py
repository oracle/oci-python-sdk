# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModifyDatabaseManagementDetails(object):
    """
    Data to update one or more attributes of the Database Management configuration for the database.
    """

    #: A constant which can be used with the management_type property of a ModifyDatabaseManagementDetails.
    #: This constant has a value of "BASIC"
    MANAGEMENT_TYPE_BASIC = "BASIC"

    #: A constant which can be used with the management_type property of a ModifyDatabaseManagementDetails.
    #: This constant has a value of "ADVANCED"
    MANAGEMENT_TYPE_ADVANCED = "ADVANCED"

    #: A constant which can be used with the protocol property of a ModifyDatabaseManagementDetails.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    #: A constant which can be used with the protocol property of a ModifyDatabaseManagementDetails.
    #: This constant has a value of "TCPS"
    PROTOCOL_TCPS = "TCPS"

    #: A constant which can be used with the role property of a ModifyDatabaseManagementDetails.
    #: This constant has a value of "SYSDBA"
    ROLE_SYSDBA = "SYSDBA"

    #: A constant which can be used with the role property of a ModifyDatabaseManagementDetails.
    #: This constant has a value of "NORMAL"
    ROLE_NORMAL = "NORMAL"

    def __init__(self, **kwargs):
        """
        Initializes a new ModifyDatabaseManagementDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_details:
            The value to assign to the credential_details property of this ModifyDatabaseManagementDetails.
        :type credential_details: oci.database.models.DatabaseCredentialDetails

        :param private_end_point_id:
            The value to assign to the private_end_point_id property of this ModifyDatabaseManagementDetails.
        :type private_end_point_id: str

        :param management_type:
            The value to assign to the management_type property of this ModifyDatabaseManagementDetails.
            Allowed values for this property are: "BASIC", "ADVANCED"
        :type management_type: str

        :param service_name:
            The value to assign to the service_name property of this ModifyDatabaseManagementDetails.
        :type service_name: str

        :param protocol:
            The value to assign to the protocol property of this ModifyDatabaseManagementDetails.
            Allowed values for this property are: "TCP", "TCPS"
        :type protocol: str

        :param port:
            The value to assign to the port property of this ModifyDatabaseManagementDetails.
        :type port: int

        :param ssl_secret_id:
            The value to assign to the ssl_secret_id property of this ModifyDatabaseManagementDetails.
        :type ssl_secret_id: str

        :param role:
            The value to assign to the role property of this ModifyDatabaseManagementDetails.
            Allowed values for this property are: "SYSDBA", "NORMAL"
        :type role: str

        """
        self.swagger_types = {
            'credential_details': 'DatabaseCredentialDetails',
            'private_end_point_id': 'str',
            'management_type': 'str',
            'service_name': 'str',
            'protocol': 'str',
            'port': 'int',
            'ssl_secret_id': 'str',
            'role': 'str'
        }

        self.attribute_map = {
            'credential_details': 'credentialDetails',
            'private_end_point_id': 'privateEndPointId',
            'management_type': 'managementType',
            'service_name': 'serviceName',
            'protocol': 'protocol',
            'port': 'port',
            'ssl_secret_id': 'sslSecretId',
            'role': 'role'
        }

        self._credential_details = None
        self._private_end_point_id = None
        self._management_type = None
        self._service_name = None
        self._protocol = None
        self._port = None
        self._ssl_secret_id = None
        self._role = None

    @property
    def credential_details(self):
        """
        Gets the credential_details of this ModifyDatabaseManagementDetails.

        :return: The credential_details of this ModifyDatabaseManagementDetails.
        :rtype: oci.database.models.DatabaseCredentialDetails
        """
        return self._credential_details

    @credential_details.setter
    def credential_details(self, credential_details):
        """
        Sets the credential_details of this ModifyDatabaseManagementDetails.

        :param credential_details: The credential_details of this ModifyDatabaseManagementDetails.
        :type: oci.database.models.DatabaseCredentialDetails
        """
        self._credential_details = credential_details

    @property
    def private_end_point_id(self):
        """
        Gets the private_end_point_id of this ModifyDatabaseManagementDetails.
        The `OCID`__ of the private endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The private_end_point_id of this ModifyDatabaseManagementDetails.
        :rtype: str
        """
        return self._private_end_point_id

    @private_end_point_id.setter
    def private_end_point_id(self, private_end_point_id):
        """
        Sets the private_end_point_id of this ModifyDatabaseManagementDetails.
        The `OCID`__ of the private endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param private_end_point_id: The private_end_point_id of this ModifyDatabaseManagementDetails.
        :type: str
        """
        self._private_end_point_id = private_end_point_id

    @property
    def management_type(self):
        """
        Gets the management_type of this ModifyDatabaseManagementDetails.
        The Database Management type.

        Allowed values for this property are: "BASIC", "ADVANCED"


        :return: The management_type of this ModifyDatabaseManagementDetails.
        :rtype: str
        """
        return self._management_type

    @management_type.setter
    def management_type(self, management_type):
        """
        Sets the management_type of this ModifyDatabaseManagementDetails.
        The Database Management type.


        :param management_type: The management_type of this ModifyDatabaseManagementDetails.
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
        Gets the service_name of this ModifyDatabaseManagementDetails.
        The name of the Oracle Database service that will be used to connect to the database.


        :return: The service_name of this ModifyDatabaseManagementDetails.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this ModifyDatabaseManagementDetails.
        The name of the Oracle Database service that will be used to connect to the database.


        :param service_name: The service_name of this ModifyDatabaseManagementDetails.
        :type: str
        """
        self._service_name = service_name

    @property
    def protocol(self):
        """
        Gets the protocol of this ModifyDatabaseManagementDetails.
        Protocol used by the database connection.

        Allowed values for this property are: "TCP", "TCPS"


        :return: The protocol of this ModifyDatabaseManagementDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this ModifyDatabaseManagementDetails.
        Protocol used by the database connection.


        :param protocol: The protocol of this ModifyDatabaseManagementDetails.
        :type: str
        """
        allowed_values = ["TCP", "TCPS"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            raise ValueError(
                "Invalid value for `protocol`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._protocol = protocol

    @property
    def port(self):
        """
        Gets the port of this ModifyDatabaseManagementDetails.
        The port used to connect to the database.


        :return: The port of this ModifyDatabaseManagementDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this ModifyDatabaseManagementDetails.
        The port used to connect to the database.


        :param port: The port of this ModifyDatabaseManagementDetails.
        :type: int
        """
        self._port = port

    @property
    def ssl_secret_id(self):
        """
        Gets the ssl_secret_id of this ModifyDatabaseManagementDetails.
        The `OCID`__ of the Oracle Cloud Infrastructure `secret`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :return: The ssl_secret_id of this ModifyDatabaseManagementDetails.
        :rtype: str
        """
        return self._ssl_secret_id

    @ssl_secret_id.setter
    def ssl_secret_id(self, ssl_secret_id):
        """
        Sets the ssl_secret_id of this ModifyDatabaseManagementDetails.
        The `OCID`__ of the Oracle Cloud Infrastructure `secret`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :param ssl_secret_id: The ssl_secret_id of this ModifyDatabaseManagementDetails.
        :type: str
        """
        self._ssl_secret_id = ssl_secret_id

    @property
    def role(self):
        """
        Gets the role of this ModifyDatabaseManagementDetails.
        The role of the user that will be connecting to the database.

        Allowed values for this property are: "SYSDBA", "NORMAL"


        :return: The role of this ModifyDatabaseManagementDetails.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this ModifyDatabaseManagementDetails.
        The role of the user that will be connecting to the database.


        :param role: The role of this ModifyDatabaseManagementDetails.
        :type: str
        """
        allowed_values = ["SYSDBA", "NORMAL"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            raise ValueError(
                "Invalid value for `role`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._role = role

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
