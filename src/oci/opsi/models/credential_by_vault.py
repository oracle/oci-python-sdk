# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .credential_details import CredentialDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CredentialByVault(CredentialDetails):
    """
    Vault Credential Details to connect to the database.
    """

    #: A constant which can be used with the role property of a CredentialByVault.
    #: This constant has a value of "NORMAL"
    ROLE_NORMAL = "NORMAL"

    def __init__(self, **kwargs):
        """
        Initializes a new CredentialByVault object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.CredentialByVault.credential_type` attribute
        of this class is ``CREDENTIALS_BY_VAULT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_source_name:
            The value to assign to the credential_source_name property of this CredentialByVault.
        :type credential_source_name: str

        :param credential_type:
            The value to assign to the credential_type property of this CredentialByVault.
            Allowed values for this property are: "CREDENTIALS_BY_SOURCE", "CREDENTIALS_BY_VAULT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type credential_type: str

        :param user_name:
            The value to assign to the user_name property of this CredentialByVault.
        :type user_name: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this CredentialByVault.
        :type password_secret_id: str

        :param role:
            The value to assign to the role property of this CredentialByVault.
            Allowed values for this property are: "NORMAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        """
        self.swagger_types = {
            'credential_source_name': 'str',
            'credential_type': 'str',
            'user_name': 'str',
            'password_secret_id': 'str',
            'role': 'str'
        }

        self.attribute_map = {
            'credential_source_name': 'credentialSourceName',
            'credential_type': 'credentialType',
            'user_name': 'userName',
            'password_secret_id': 'passwordSecretId',
            'role': 'role'
        }

        self._credential_source_name = None
        self._credential_type = None
        self._user_name = None
        self._password_secret_id = None
        self._role = None
        self._credential_type = 'CREDENTIALS_BY_VAULT'

    @property
    def user_name(self):
        """
        Gets the user_name of this CredentialByVault.
        database user name.


        :return: The user_name of this CredentialByVault.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this CredentialByVault.
        database user name.


        :param user_name: The user_name of this CredentialByVault.
        :type: str
        """
        self._user_name = user_name

    @property
    def password_secret_id(self):
        """
        Gets the password_secret_id of this CredentialByVault.
        The secret `OCID`__ mapping to the database credentials.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The password_secret_id of this CredentialByVault.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this CredentialByVault.
        The secret `OCID`__ mapping to the database credentials.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param password_secret_id: The password_secret_id of this CredentialByVault.
        :type: str
        """
        self._password_secret_id = password_secret_id

    @property
    def role(self):
        """
        Gets the role of this CredentialByVault.
        database user role.

        Allowed values for this property are: "NORMAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this CredentialByVault.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this CredentialByVault.
        database user role.


        :param role: The role of this CredentialByVault.
        :type: str
        """
        allowed_values = ["NORMAL"]
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
