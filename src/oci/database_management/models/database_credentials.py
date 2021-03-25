# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseCredentials(object):
    """
    The database credentials used to perform management activity.
    """

    #: A constant which can be used with the role property of a DatabaseCredentials.
    #: This constant has a value of "NORMAL"
    ROLE_NORMAL = "NORMAL"

    #: A constant which can be used with the role property of a DatabaseCredentials.
    #: This constant has a value of "SYSDBA"
    ROLE_SYSDBA = "SYSDBA"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseCredentials object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param user_name:
            The value to assign to the user_name property of this DatabaseCredentials.
        :type user_name: str

        :param password:
            The value to assign to the password property of this DatabaseCredentials.
        :type password: str

        :param role:
            The value to assign to the role property of this DatabaseCredentials.
            Allowed values for this property are: "NORMAL", "SYSDBA"
        :type role: str

        """
        self.swagger_types = {
            'user_name': 'str',
            'password': 'str',
            'role': 'str'
        }

        self.attribute_map = {
            'user_name': 'userName',
            'password': 'password',
            'role': 'role'
        }

        self._user_name = None
        self._password = None
        self._role = None

    @property
    def user_name(self):
        """
        Gets the user_name of this DatabaseCredentials.
        The database user name used to perform management activity.


        :return: The user_name of this DatabaseCredentials.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this DatabaseCredentials.
        The database user name used to perform management activity.


        :param user_name: The user_name of this DatabaseCredentials.
        :type: str
        """
        self._user_name = user_name

    @property
    def password(self):
        """
        Gets the password of this DatabaseCredentials.
        The password for the database user name.


        :return: The password of this DatabaseCredentials.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this DatabaseCredentials.
        The password for the database user name.


        :param password: The password of this DatabaseCredentials.
        :type: str
        """
        self._password = password

    @property
    def role(self):
        """
        Gets the role of this DatabaseCredentials.
        The role of the database user. Indicates whether the database user is a normal user or sysdba.

        Allowed values for this property are: "NORMAL", "SYSDBA"


        :return: The role of this DatabaseCredentials.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this DatabaseCredentials.
        The role of the database user. Indicates whether the database user is a normal user or sysdba.


        :param role: The role of this DatabaseCredentials.
        :type: str
        """
        allowed_values = ["NORMAL", "SYSDBA"]
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
