# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_connection_credentials import DatabaseConnectionCredentials
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseConnectionCredentialsByDetails(DatabaseConnectionCredentials):
    """
    User information to connect to the database. Required when performing the :func:`create_external_database_connector_details` operation.
    *IMPORTANT*: Not supported for the :func:`update_external_database_connector_details` operation.
    """

    #: A constant which can be used with the role property of a DatabaseConnectionCredentialsByDetails.
    #: This constant has a value of "SYSDBA"
    ROLE_SYSDBA = "SYSDBA"

    #: A constant which can be used with the role property of a DatabaseConnectionCredentialsByDetails.
    #: This constant has a value of "NORMAL"
    ROLE_NORMAL = "NORMAL"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseConnectionCredentialsByDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.DatabaseConnectionCredentialsByDetails.credential_type` attribute
        of this class is ``DETAILS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_type:
            The value to assign to the credential_type property of this DatabaseConnectionCredentialsByDetails.
            Allowed values for this property are: "NAME_REFERENCE", "DETAILS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type credential_type: str

        :param credential_name:
            The value to assign to the credential_name property of this DatabaseConnectionCredentialsByDetails.
        :type credential_name: str

        :param username:
            The value to assign to the username property of this DatabaseConnectionCredentialsByDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this DatabaseConnectionCredentialsByDetails.
        :type password: str

        :param role:
            The value to assign to the role property of this DatabaseConnectionCredentialsByDetails.
            Allowed values for this property are: "SYSDBA", "NORMAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        """
        self.swagger_types = {
            'credential_type': 'str',
            'credential_name': 'str',
            'username': 'str',
            'password': 'str',
            'role': 'str'
        }

        self.attribute_map = {
            'credential_type': 'credentialType',
            'credential_name': 'credentialName',
            'username': 'username',
            'password': 'password',
            'role': 'role'
        }

        self._credential_type = None
        self._credential_name = None
        self._username = None
        self._password = None
        self._role = None
        self._credential_type = 'DETAILS'

    @property
    def credential_name(self):
        """
        Gets the credential_name of this DatabaseConnectionCredentialsByDetails.
        The name of the credential information that used to connect to the database. The name should be in \"x.y\" format, where
        the length of \"x\" has a maximum of 64 characters, and length of \"y\" has a maximum of 199 characters.
        The name strings can contain letters, numbers and the underscore character only. Other characters are not valid, except for
        the \".\" character that separates the \"x\" and \"y\" portions of the name.
        *IMPORTANT* - The name must be unique within the OCI region the credential is being created in. If you specify a name
        that duplicates the name of another credential within the same OCI region, you may overwrite or corrupt the credential that is already
        using the name.

        For example: inventorydb.abc112233445566778899


        :return: The credential_name of this DatabaseConnectionCredentialsByDetails.
        :rtype: str
        """
        return self._credential_name

    @credential_name.setter
    def credential_name(self, credential_name):
        """
        Sets the credential_name of this DatabaseConnectionCredentialsByDetails.
        The name of the credential information that used to connect to the database. The name should be in \"x.y\" format, where
        the length of \"x\" has a maximum of 64 characters, and length of \"y\" has a maximum of 199 characters.
        The name strings can contain letters, numbers and the underscore character only. Other characters are not valid, except for
        the \".\" character that separates the \"x\" and \"y\" portions of the name.
        *IMPORTANT* - The name must be unique within the OCI region the credential is being created in. If you specify a name
        that duplicates the name of another credential within the same OCI region, you may overwrite or corrupt the credential that is already
        using the name.

        For example: inventorydb.abc112233445566778899


        :param credential_name: The credential_name of this DatabaseConnectionCredentialsByDetails.
        :type: str
        """
        self._credential_name = credential_name

    @property
    def username(self):
        """
        **[Required]** Gets the username of this DatabaseConnectionCredentialsByDetails.
        The username that will be used to connect to the database.


        :return: The username of this DatabaseConnectionCredentialsByDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this DatabaseConnectionCredentialsByDetails.
        The username that will be used to connect to the database.


        :param username: The username of this DatabaseConnectionCredentialsByDetails.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        **[Required]** Gets the password of this DatabaseConnectionCredentialsByDetails.
        The password that will be used to connect to the database.


        :return: The password of this DatabaseConnectionCredentialsByDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this DatabaseConnectionCredentialsByDetails.
        The password that will be used to connect to the database.


        :param password: The password of this DatabaseConnectionCredentialsByDetails.
        :type: str
        """
        self._password = password

    @property
    def role(self):
        """
        **[Required]** Gets the role of this DatabaseConnectionCredentialsByDetails.
        The role of the user that will be connecting to the database.

        Allowed values for this property are: "SYSDBA", "NORMAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this DatabaseConnectionCredentialsByDetails.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this DatabaseConnectionCredentialsByDetails.
        The role of the user that will be connecting to the database.


        :param role: The role of this DatabaseConnectionCredentialsByDetails.
        :type: str
        """
        allowed_values = ["SYSDBA", "NORMAL"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
