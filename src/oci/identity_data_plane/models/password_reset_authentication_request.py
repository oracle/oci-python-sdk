# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PasswordResetAuthenticationRequest(object):
    """
    PasswordResetAuthenticationRequest model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PasswordResetAuthenticationRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param user_id:
            The value to assign to the user_id property of this PasswordResetAuthenticationRequest.
        :type user_id: str

        :param password_reset_token:
            The value to assign to the password_reset_token property of this PasswordResetAuthenticationRequest.
        :type password_reset_token: str

        """
        self.swagger_types = {
            'user_id': 'str',
            'password_reset_token': 'str'
        }

        self.attribute_map = {
            'user_id': 'userId',
            'password_reset_token': 'passwordResetToken'
        }

        self._user_id = None
        self._password_reset_token = None

    @property
    def user_id(self):
        """
        **[Required]** Gets the user_id of this PasswordResetAuthenticationRequest.
        The id of the user


        :return: The user_id of this PasswordResetAuthenticationRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this PasswordResetAuthenticationRequest.
        The id of the user


        :param user_id: The user_id of this PasswordResetAuthenticationRequest.
        :type: str
        """
        self._user_id = user_id

    @property
    def password_reset_token(self):
        """
        **[Required]** Gets the password_reset_token of this PasswordResetAuthenticationRequest.
        The password reset token


        :return: The password_reset_token of this PasswordResetAuthenticationRequest.
        :rtype: str
        """
        return self._password_reset_token

    @password_reset_token.setter
    def password_reset_token(self, password_reset_token):
        """
        Sets the password_reset_token of this PasswordResetAuthenticationRequest.
        The password reset token


        :param password_reset_token: The password_reset_token of this PasswordResetAuthenticationRequest.
        :type: str
        """
        self._password_reset_token = password_reset_token

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
