# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Credentials(object):
    """
    The database credentials required for Data Safe to connect to the database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Credentials object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param user_name:
            The value to assign to the user_name property of this Credentials.
        :type user_name: str

        :param password:
            The value to assign to the password property of this Credentials.
        :type password: str

        """
        self.swagger_types = {
            'user_name': 'str',
            'password': 'str'
        }

        self.attribute_map = {
            'user_name': 'userName',
            'password': 'password'
        }

        self._user_name = None
        self._password = None

    @property
    def user_name(self):
        """
        **[Required]** Gets the user_name of this Credentials.
        The database user name.


        :return: The user_name of this Credentials.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this Credentials.
        The database user name.


        :param user_name: The user_name of this Credentials.
        :type: str
        """
        self._user_name = user_name

    @property
    def password(self):
        """
        **[Required]** Gets the password of this Credentials.
        The password of the database user.


        :return: The password of this Credentials.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this Credentials.
        The password of the database user.


        :param password: The password of this Credentials.
        :type: str
        """
        self._password = password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
