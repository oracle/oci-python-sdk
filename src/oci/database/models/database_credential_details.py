# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseCredentialDetails(object):
    """
    Data for the credential used to connect to the database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseCredentialDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param user_name:
            The value to assign to the user_name property of this DatabaseCredentialDetails.
        :type user_name: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this DatabaseCredentialDetails.
        :type password_secret_id: str

        """
        self.swagger_types = {
            'user_name': 'str',
            'password_secret_id': 'str'
        }

        self.attribute_map = {
            'user_name': 'userName',
            'password_secret_id': 'passwordSecretId'
        }

        self._user_name = None
        self._password_secret_id = None

    @property
    def user_name(self):
        """
        **[Required]** Gets the user_name of this DatabaseCredentialDetails.
        The name of the Oracle Database user that will be used to connect to the database.


        :return: The user_name of this DatabaseCredentialDetails.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this DatabaseCredentialDetails.
        The name of the Oracle Database user that will be used to connect to the database.


        :param user_name: The user_name of this DatabaseCredentialDetails.
        :type: str
        """
        self._user_name = user_name

    @property
    def password_secret_id(self):
        """
        **[Required]** Gets the password_secret_id of this DatabaseCredentialDetails.
        The `OCID`__ of the Oracle Cloud Infrastructure `secret`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :return: The password_secret_id of this DatabaseCredentialDetails.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this DatabaseCredentialDetails.
        The `OCID`__ of the Oracle Cloud Infrastructure `secret`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :param password_secret_id: The password_secret_id of this DatabaseCredentialDetails.
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
