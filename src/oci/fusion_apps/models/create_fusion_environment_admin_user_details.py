# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateFusionEnvironmentAdminUserDetails(object):
    """
    The credentials for the Fusion Applications service administrator.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateFusionEnvironmentAdminUserDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param username:
            The value to assign to the username property of this CreateFusionEnvironmentAdminUserDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this CreateFusionEnvironmentAdminUserDetails.
        :type password: str

        :param email_address:
            The value to assign to the email_address property of this CreateFusionEnvironmentAdminUserDetails.
        :type email_address: str

        :param first_name:
            The value to assign to the first_name property of this CreateFusionEnvironmentAdminUserDetails.
        :type first_name: str

        :param last_name:
            The value to assign to the last_name property of this CreateFusionEnvironmentAdminUserDetails.
        :type last_name: str

        """
        self.swagger_types = {
            'username': 'str',
            'password': 'str',
            'email_address': 'str',
            'first_name': 'str',
            'last_name': 'str'
        }

        self.attribute_map = {
            'username': 'username',
            'password': 'password',
            'email_address': 'emailAddress',
            'first_name': 'firstName',
            'last_name': 'lastName'
        }

        self._username = None
        self._password = None
        self._email_address = None
        self._first_name = None
        self._last_name = None

    @property
    def username(self):
        """
        **[Required]** Gets the username of this CreateFusionEnvironmentAdminUserDetails.
        The username for the administrator.


        :return: The username of this CreateFusionEnvironmentAdminUserDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this CreateFusionEnvironmentAdminUserDetails.
        The username for the administrator.


        :param username: The username of this CreateFusionEnvironmentAdminUserDetails.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        **[Required]** Gets the password of this CreateFusionEnvironmentAdminUserDetails.
        The password for the administrator.


        :return: The password of this CreateFusionEnvironmentAdminUserDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this CreateFusionEnvironmentAdminUserDetails.
        The password for the administrator.


        :param password: The password of this CreateFusionEnvironmentAdminUserDetails.
        :type: str
        """
        self._password = password

    @property
    def email_address(self):
        """
        **[Required]** Gets the email_address of this CreateFusionEnvironmentAdminUserDetails.
        The email address for the administrator.


        :return: The email_address of this CreateFusionEnvironmentAdminUserDetails.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this CreateFusionEnvironmentAdminUserDetails.
        The email address for the administrator.


        :param email_address: The email_address of this CreateFusionEnvironmentAdminUserDetails.
        :type: str
        """
        self._email_address = email_address

    @property
    def first_name(self):
        """
        **[Required]** Gets the first_name of this CreateFusionEnvironmentAdminUserDetails.
        The administrator's first name.


        :return: The first_name of this CreateFusionEnvironmentAdminUserDetails.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this CreateFusionEnvironmentAdminUserDetails.
        The administrator's first name.


        :param first_name: The first_name of this CreateFusionEnvironmentAdminUserDetails.
        :type: str
        """
        self._first_name = first_name

    @property
    def last_name(self):
        """
        **[Required]** Gets the last_name of this CreateFusionEnvironmentAdminUserDetails.
        The administrator's last name.


        :return: The last_name of this CreateFusionEnvironmentAdminUserDetails.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this CreateFusionEnvironmentAdminUserDetails.
        The administrator's last name.


        :param last_name: The last_name of this CreateFusionEnvironmentAdminUserDetails.
        :type: str
        """
        self._last_name = last_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
