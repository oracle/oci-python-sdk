# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .test_preferred_credential_details import TestPreferredCredentialDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TestBasicPreferredCredentialDetails(TestPreferredCredentialDetails):
    """
    The details of the 'BASIC' preferred credential.
    """

    #: A constant which can be used with the role property of a TestBasicPreferredCredentialDetails.
    #: This constant has a value of "NORMAL"
    ROLE_NORMAL = "NORMAL"

    #: A constant which can be used with the role property of a TestBasicPreferredCredentialDetails.
    #: This constant has a value of "SYSDBA"
    ROLE_SYSDBA = "SYSDBA"

    def __init__(self, **kwargs):
        """
        Initializes a new TestBasicPreferredCredentialDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.TestBasicPreferredCredentialDetails.type` attribute
        of this class is ``BASIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this TestBasicPreferredCredentialDetails.
            Allowed values for this property are: "BASIC"
        :type type: str

        :param user_name:
            The value to assign to the user_name property of this TestBasicPreferredCredentialDetails.
        :type user_name: str

        :param role:
            The value to assign to the role property of this TestBasicPreferredCredentialDetails.
            Allowed values for this property are: "NORMAL", "SYSDBA"
        :type role: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this TestBasicPreferredCredentialDetails.
        :type password_secret_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'user_name': 'str',
            'role': 'str',
            'password_secret_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'user_name': 'userName',
            'role': 'role',
            'password_secret_id': 'passwordSecretId'
        }

        self._type = None
        self._user_name = None
        self._role = None
        self._password_secret_id = None
        self._type = 'BASIC'

    @property
    def user_name(self):
        """
        Gets the user_name of this TestBasicPreferredCredentialDetails.
        The user name used to connect to the database.


        :return: The user_name of this TestBasicPreferredCredentialDetails.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this TestBasicPreferredCredentialDetails.
        The user name used to connect to the database.


        :param user_name: The user_name of this TestBasicPreferredCredentialDetails.
        :type: str
        """
        self._user_name = user_name

    @property
    def role(self):
        """
        Gets the role of this TestBasicPreferredCredentialDetails.
        The role of the database user.

        Allowed values for this property are: "NORMAL", "SYSDBA"


        :return: The role of this TestBasicPreferredCredentialDetails.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this TestBasicPreferredCredentialDetails.
        The role of the database user.


        :param role: The role of this TestBasicPreferredCredentialDetails.
        :type: str
        """
        allowed_values = ["NORMAL", "SYSDBA"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            raise ValueError(
                "Invalid value for `role`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._role = role

    @property
    def password_secret_id(self):
        """
        Gets the password_secret_id of this TestBasicPreferredCredentialDetails.
        The `OCID`__ of the Vault service secret that contains the database user password.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The password_secret_id of this TestBasicPreferredCredentialDetails.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this TestBasicPreferredCredentialDetails.
        The `OCID`__ of the Vault service secret that contains the database user password.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param password_secret_id: The password_secret_id of this TestBasicPreferredCredentialDetails.
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
