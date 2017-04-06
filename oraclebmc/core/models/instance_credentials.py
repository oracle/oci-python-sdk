# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class InstanceCredentials(object):

    def __init__(self):

        self.swagger_types = {
            'password': 'str',
            'username': 'str'
        }

        self.attribute_map = {
            'password': 'password',
            'username': 'username'
        }

        self._password = None
        self._username = None

    @property
    def password(self):
        """
        Gets the password of this InstanceCredentials.
        The password for the username.


        :return: The password of this InstanceCredentials.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this InstanceCredentials.
        The password for the username.


        :param password: The password of this InstanceCredentials.
        :type: str
        """
        self._password = password

    @property
    def username(self):
        """
        Gets the username of this InstanceCredentials.
        The username.


        :return: The username of this InstanceCredentials.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this InstanceCredentials.
        The username.


        :param username: The username of this InstanceCredentials.
        :type: str
        """
        self._username = username

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
