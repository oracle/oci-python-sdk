# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProfileDetails(object):
    """
    The details of a particular profile
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProfileDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param num_users:
            The value to assign to the num_users property of this ProfileDetails.
        :type num_users: int

        :param connect_time:
            The value to assign to the connect_time property of this ProfileDetails.
        :type connect_time: str

        :param failed_login_attempts:
            The value to assign to the failed_login_attempts property of this ProfileDetails.
        :type failed_login_attempts: str

        :param idle_time:
            The value to assign to the idle_time property of this ProfileDetails.
        :type idle_time: str

        :param inactive_account_time:
            The value to assign to the inactive_account_time property of this ProfileDetails.
        :type inactive_account_time: str

        :param password_grace_time:
            The value to assign to the password_grace_time property of this ProfileDetails.
        :type password_grace_time: str

        :param password_life_time:
            The value to assign to the password_life_time property of this ProfileDetails.
        :type password_life_time: str

        :param password_lock_time:
            The value to assign to the password_lock_time property of this ProfileDetails.
        :type password_lock_time: str

        :param password_reuse_time:
            The value to assign to the password_reuse_time property of this ProfileDetails.
        :type password_reuse_time: str

        :param password_reuse_max:
            The value to assign to the password_reuse_max property of this ProfileDetails.
        :type password_reuse_max: str

        :param password_verify_function:
            The value to assign to the password_verify_function property of this ProfileDetails.
        :type password_verify_function: str

        """
        self.swagger_types = {
            'num_users': 'int',
            'connect_time': 'str',
            'failed_login_attempts': 'str',
            'idle_time': 'str',
            'inactive_account_time': 'str',
            'password_grace_time': 'str',
            'password_life_time': 'str',
            'password_lock_time': 'str',
            'password_reuse_time': 'str',
            'password_reuse_max': 'str',
            'password_verify_function': 'str'
        }

        self.attribute_map = {
            'num_users': 'numUsers',
            'connect_time': 'connectTime',
            'failed_login_attempts': 'failedLoginAttempts',
            'idle_time': 'idleTime',
            'inactive_account_time': 'inactiveAccountTime',
            'password_grace_time': 'passwordGraceTime',
            'password_life_time': 'passwordLifeTime',
            'password_lock_time': 'passwordLockTime',
            'password_reuse_time': 'passwordReuseTime',
            'password_reuse_max': 'passwordReuseMax',
            'password_verify_function': 'passwordVerifyFunction'
        }

        self._num_users = None
        self._connect_time = None
        self._failed_login_attempts = None
        self._idle_time = None
        self._inactive_account_time = None
        self._password_grace_time = None
        self._password_life_time = None
        self._password_lock_time = None
        self._password_reuse_time = None
        self._password_reuse_max = None
        self._password_verify_function = None

    @property
    def num_users(self):
        """
        Gets the num_users of this ProfileDetails.
        The number of users using this profile.


        :return: The num_users of this ProfileDetails.
        :rtype: int
        """
        return self._num_users

    @num_users.setter
    def num_users(self, num_users):
        """
        Sets the num_users of this ProfileDetails.
        The number of users using this profile.


        :param num_users: The num_users of this ProfileDetails.
        :type: int
        """
        self._num_users = num_users

    @property
    def connect_time(self):
        """
        Gets the connect_time of this ProfileDetails.
        The value of the CONNECT_TIME resource parameter.


        :return: The connect_time of this ProfileDetails.
        :rtype: str
        """
        return self._connect_time

    @connect_time.setter
    def connect_time(self, connect_time):
        """
        Sets the connect_time of this ProfileDetails.
        The value of the CONNECT_TIME resource parameter.


        :param connect_time: The connect_time of this ProfileDetails.
        :type: str
        """
        self._connect_time = connect_time

    @property
    def failed_login_attempts(self):
        """
        Gets the failed_login_attempts of this ProfileDetails.
        The value of the FAILED_LOGIN_ATTEMPTS password parameter.


        :return: The failed_login_attempts of this ProfileDetails.
        :rtype: str
        """
        return self._failed_login_attempts

    @failed_login_attempts.setter
    def failed_login_attempts(self, failed_login_attempts):
        """
        Sets the failed_login_attempts of this ProfileDetails.
        The value of the FAILED_LOGIN_ATTEMPTS password parameter.


        :param failed_login_attempts: The failed_login_attempts of this ProfileDetails.
        :type: str
        """
        self._failed_login_attempts = failed_login_attempts

    @property
    def idle_time(self):
        """
        Gets the idle_time of this ProfileDetails.
        The value of the IDLE_TIME resource parameter.


        :return: The idle_time of this ProfileDetails.
        :rtype: str
        """
        return self._idle_time

    @idle_time.setter
    def idle_time(self, idle_time):
        """
        Sets the idle_time of this ProfileDetails.
        The value of the IDLE_TIME resource parameter.


        :param idle_time: The idle_time of this ProfileDetails.
        :type: str
        """
        self._idle_time = idle_time

    @property
    def inactive_account_time(self):
        """
        Gets the inactive_account_time of this ProfileDetails.
        The value of the INACTIVE_ACCOUNT_TIME password parameter.


        :return: The inactive_account_time of this ProfileDetails.
        :rtype: str
        """
        return self._inactive_account_time

    @inactive_account_time.setter
    def inactive_account_time(self, inactive_account_time):
        """
        Sets the inactive_account_time of this ProfileDetails.
        The value of the INACTIVE_ACCOUNT_TIME password parameter.


        :param inactive_account_time: The inactive_account_time of this ProfileDetails.
        :type: str
        """
        self._inactive_account_time = inactive_account_time

    @property
    def password_grace_time(self):
        """
        Gets the password_grace_time of this ProfileDetails.
        The value of the PASSWORD_GRACE_TIME password parameter.


        :return: The password_grace_time of this ProfileDetails.
        :rtype: str
        """
        return self._password_grace_time

    @password_grace_time.setter
    def password_grace_time(self, password_grace_time):
        """
        Sets the password_grace_time of this ProfileDetails.
        The value of the PASSWORD_GRACE_TIME password parameter.


        :param password_grace_time: The password_grace_time of this ProfileDetails.
        :type: str
        """
        self._password_grace_time = password_grace_time

    @property
    def password_life_time(self):
        """
        Gets the password_life_time of this ProfileDetails.
        The value of the PASSWORD_LIFE_TIME password parameter.


        :return: The password_life_time of this ProfileDetails.
        :rtype: str
        """
        return self._password_life_time

    @password_life_time.setter
    def password_life_time(self, password_life_time):
        """
        Sets the password_life_time of this ProfileDetails.
        The value of the PASSWORD_LIFE_TIME password parameter.


        :param password_life_time: The password_life_time of this ProfileDetails.
        :type: str
        """
        self._password_life_time = password_life_time

    @property
    def password_lock_time(self):
        """
        Gets the password_lock_time of this ProfileDetails.
        The value of the PASSWORD_LOCK_TIME password parameter.


        :return: The password_lock_time of this ProfileDetails.
        :rtype: str
        """
        return self._password_lock_time

    @password_lock_time.setter
    def password_lock_time(self, password_lock_time):
        """
        Sets the password_lock_time of this ProfileDetails.
        The value of the PASSWORD_LOCK_TIME password parameter.


        :param password_lock_time: The password_lock_time of this ProfileDetails.
        :type: str
        """
        self._password_lock_time = password_lock_time

    @property
    def password_reuse_time(self):
        """
        Gets the password_reuse_time of this ProfileDetails.
        The value of the PASSWORD_REUSE_TIME password parameter.


        :return: The password_reuse_time of this ProfileDetails.
        :rtype: str
        """
        return self._password_reuse_time

    @password_reuse_time.setter
    def password_reuse_time(self, password_reuse_time):
        """
        Sets the password_reuse_time of this ProfileDetails.
        The value of the PASSWORD_REUSE_TIME password parameter.


        :param password_reuse_time: The password_reuse_time of this ProfileDetails.
        :type: str
        """
        self._password_reuse_time = password_reuse_time

    @property
    def password_reuse_max(self):
        """
        Gets the password_reuse_max of this ProfileDetails.
        The value of the PASSWORD_REUSE_MAX resource parameter.


        :return: The password_reuse_max of this ProfileDetails.
        :rtype: str
        """
        return self._password_reuse_max

    @password_reuse_max.setter
    def password_reuse_max(self, password_reuse_max):
        """
        Sets the password_reuse_max of this ProfileDetails.
        The value of the PASSWORD_REUSE_MAX resource parameter.


        :param password_reuse_max: The password_reuse_max of this ProfileDetails.
        :type: str
        """
        self._password_reuse_max = password_reuse_max

    @property
    def password_verify_function(self):
        """
        Gets the password_verify_function of this ProfileDetails.
        The value of the PASSWORD_VERIFY_FUNCTION resource.


        :return: The password_verify_function of this ProfileDetails.
        :rtype: str
        """
        return self._password_verify_function

    @password_verify_function.setter
    def password_verify_function(self, password_verify_function):
        """
        Sets the password_verify_function of this ProfileDetails.
        The value of the PASSWORD_VERIFY_FUNCTION resource.


        :param password_verify_function: The password_verify_function of this ProfileDetails.
        :type: str
        """
        self._password_verify_function = password_verify_function

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
