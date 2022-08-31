# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PreferredCredentialSummary(object):
    """
    The summary of preferred credentials.
    """

    #: A constant which can be used with the status property of a PreferredCredentialSummary.
    #: This constant has a value of "SET"
    STATUS_SET = "SET"

    #: A constant which can be used with the status property of a PreferredCredentialSummary.
    #: This constant has a value of "NOT_SET"
    STATUS_NOT_SET = "NOT_SET"

    #: A constant which can be used with the role property of a PreferredCredentialSummary.
    #: This constant has a value of "NORMAL"
    ROLE_NORMAL = "NORMAL"

    #: A constant which can be used with the role property of a PreferredCredentialSummary.
    #: This constant has a value of "SYSDBA"
    ROLE_SYSDBA = "SYSDBA"

    def __init__(self, **kwargs):
        """
        Initializes a new PreferredCredentialSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_name:
            The value to assign to the credential_name property of this PreferredCredentialSummary.
        :type credential_name: str

        :param status:
            The value to assign to the status property of this PreferredCredentialSummary.
            Allowed values for this property are: "SET", "NOT_SET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param is_accessible:
            The value to assign to the is_accessible property of this PreferredCredentialSummary.
        :type is_accessible: bool

        :param user_name:
            The value to assign to the user_name property of this PreferredCredentialSummary.
        :type user_name: str

        :param role:
            The value to assign to the role property of this PreferredCredentialSummary.
            Allowed values for this property are: "NORMAL", "SYSDBA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this PreferredCredentialSummary.
        :type password_secret_id: str

        """
        self.swagger_types = {
            'credential_name': 'str',
            'status': 'str',
            'is_accessible': 'bool',
            'user_name': 'str',
            'role': 'str',
            'password_secret_id': 'str'
        }

        self.attribute_map = {
            'credential_name': 'credentialName',
            'status': 'status',
            'is_accessible': 'isAccessible',
            'user_name': 'userName',
            'role': 'role',
            'password_secret_id': 'passwordSecretId'
        }

        self._credential_name = None
        self._status = None
        self._is_accessible = None
        self._user_name = None
        self._role = None
        self._password_secret_id = None

    @property
    def credential_name(self):
        """
        **[Required]** Gets the credential_name of this PreferredCredentialSummary.
        The name of the preferred credential.


        :return: The credential_name of this PreferredCredentialSummary.
        :rtype: str
        """
        return self._credential_name

    @credential_name.setter
    def credential_name(self, credential_name):
        """
        Sets the credential_name of this PreferredCredentialSummary.
        The name of the preferred credential.


        :param credential_name: The credential_name of this PreferredCredentialSummary.
        :type: str
        """
        self._credential_name = credential_name

    @property
    def status(self):
        """
        **[Required]** Gets the status of this PreferredCredentialSummary.
        The status of the preferred credential.

        Allowed values for this property are: "SET", "NOT_SET", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this PreferredCredentialSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PreferredCredentialSummary.
        The status of the preferred credential.


        :param status: The status of this PreferredCredentialSummary.
        :type: str
        """
        allowed_values = ["SET", "NOT_SET"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def is_accessible(self):
        """
        **[Required]** Gets the is_accessible of this PreferredCredentialSummary.
        Indicates whether the preferred credential is accessible.


        :return: The is_accessible of this PreferredCredentialSummary.
        :rtype: bool
        """
        return self._is_accessible

    @is_accessible.setter
    def is_accessible(self, is_accessible):
        """
        Sets the is_accessible of this PreferredCredentialSummary.
        Indicates whether the preferred credential is accessible.


        :param is_accessible: The is_accessible of this PreferredCredentialSummary.
        :type: bool
        """
        self._is_accessible = is_accessible

    @property
    def user_name(self):
        """
        Gets the user_name of this PreferredCredentialSummary.
        The user name used to connect to the database.


        :return: The user_name of this PreferredCredentialSummary.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this PreferredCredentialSummary.
        The user name used to connect to the database.


        :param user_name: The user_name of this PreferredCredentialSummary.
        :type: str
        """
        self._user_name = user_name

    @property
    def role(self):
        """
        Gets the role of this PreferredCredentialSummary.
        The role of the database user.

        Allowed values for this property are: "NORMAL", "SYSDBA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this PreferredCredentialSummary.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this PreferredCredentialSummary.
        The role of the database user.


        :param role: The role of this PreferredCredentialSummary.
        :type: str
        """
        allowed_values = ["NORMAL", "SYSDBA"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    @property
    def password_secret_id(self):
        """
        Gets the password_secret_id of this PreferredCredentialSummary.
        The `OCID`__ of the Vault service secret that contains the database user password.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The password_secret_id of this PreferredCredentialSummary.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this PreferredCredentialSummary.
        The `OCID`__ of the Vault service secret that contains the database user password.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param password_secret_id: The password_secret_id of this PreferredCredentialSummary.
        :type: str
        """
        self._password_secret_id = password_secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
