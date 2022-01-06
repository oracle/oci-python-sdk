# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BadUserStateAuthenticateUserResult(object):
    """
    BadUserStateAuthenticateUserResult model.
    """

    #: A constant which can be used with the user_state property of a BadUserStateAuthenticateUserResult.
    #: This constant has a value of "USER_BLOCKED"
    USER_STATE_USER_BLOCKED = "USER_BLOCKED"

    #: A constant which can be used with the user_state property of a BadUserStateAuthenticateUserResult.
    #: This constant has a value of "USER_DISABLED"
    USER_STATE_USER_DISABLED = "USER_DISABLED"

    #: A constant which can be used with the user_state property of a BadUserStateAuthenticateUserResult.
    #: This constant has a value of "ONE_TIME_PASSWORD_EXPIRED"
    USER_STATE_ONE_TIME_PASSWORD_EXPIRED = "ONE_TIME_PASSWORD_EXPIRED"

    #: A constant which can be used with the user_state property of a BadUserStateAuthenticateUserResult.
    #: This constant has a value of "PASSWORD_INVALID"
    USER_STATE_PASSWORD_INVALID = "PASSWORD_INVALID"

    def __init__(self, **kwargs):
        """
        Initializes a new BadUserStateAuthenticateUserResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tenant_input:
            The value to assign to the tenant_input property of this BadUserStateAuthenticateUserResult.
        :type tenant_input: str

        :param user_input:
            The value to assign to the user_input property of this BadUserStateAuthenticateUserResult.
        :type user_input: str

        :param resolved_tenant_id:
            The value to assign to the resolved_tenant_id property of this BadUserStateAuthenticateUserResult.
        :type resolved_tenant_id: str

        :param resolved_user_id:
            The value to assign to the resolved_user_id property of this BadUserStateAuthenticateUserResult.
        :type resolved_user_id: str

        :param user_state:
            The value to assign to the user_state property of this BadUserStateAuthenticateUserResult.
            Allowed values for this property are: "USER_BLOCKED", "USER_DISABLED", "ONE_TIME_PASSWORD_EXPIRED", "PASSWORD_INVALID"
        :type user_state: str

        """
        self.swagger_types = {
            'tenant_input': 'str',
            'user_input': 'str',
            'resolved_tenant_id': 'str',
            'resolved_user_id': 'str',
            'user_state': 'str'
        }

        self.attribute_map = {
            'tenant_input': 'tenantInput',
            'user_input': 'userInput',
            'resolved_tenant_id': 'resolvedTenantId',
            'resolved_user_id': 'resolvedUserId',
            'user_state': 'userState'
        }

        self._tenant_input = None
        self._user_input = None
        self._resolved_tenant_id = None
        self._resolved_user_id = None
        self._user_state = None

    @property
    def tenant_input(self):
        """
        **[Required]** Gets the tenant_input of this BadUserStateAuthenticateUserResult.
        The tenant name.


        :return: The tenant_input of this BadUserStateAuthenticateUserResult.
        :rtype: str
        """
        return self._tenant_input

    @tenant_input.setter
    def tenant_input(self, tenant_input):
        """
        Sets the tenant_input of this BadUserStateAuthenticateUserResult.
        The tenant name.


        :param tenant_input: The tenant_input of this BadUserStateAuthenticateUserResult.
        :type: str
        """
        self._tenant_input = tenant_input

    @property
    def user_input(self):
        """
        **[Required]** Gets the user_input of this BadUserStateAuthenticateUserResult.
        The user name.


        :return: The user_input of this BadUserStateAuthenticateUserResult.
        :rtype: str
        """
        return self._user_input

    @user_input.setter
    def user_input(self, user_input):
        """
        Sets the user_input of this BadUserStateAuthenticateUserResult.
        The user name.


        :param user_input: The user_input of this BadUserStateAuthenticateUserResult.
        :type: str
        """
        self._user_input = user_input

    @property
    def resolved_tenant_id(self):
        """
        **[Required]** Gets the resolved_tenant_id of this BadUserStateAuthenticateUserResult.
        The resolved tenant id.


        :return: The resolved_tenant_id of this BadUserStateAuthenticateUserResult.
        :rtype: str
        """
        return self._resolved_tenant_id

    @resolved_tenant_id.setter
    def resolved_tenant_id(self, resolved_tenant_id):
        """
        Sets the resolved_tenant_id of this BadUserStateAuthenticateUserResult.
        The resolved tenant id.


        :param resolved_tenant_id: The resolved_tenant_id of this BadUserStateAuthenticateUserResult.
        :type: str
        """
        self._resolved_tenant_id = resolved_tenant_id

    @property
    def resolved_user_id(self):
        """
        **[Required]** Gets the resolved_user_id of this BadUserStateAuthenticateUserResult.
        The resolved user id.


        :return: The resolved_user_id of this BadUserStateAuthenticateUserResult.
        :rtype: str
        """
        return self._resolved_user_id

    @resolved_user_id.setter
    def resolved_user_id(self, resolved_user_id):
        """
        Sets the resolved_user_id of this BadUserStateAuthenticateUserResult.
        The resolved user id.


        :param resolved_user_id: The resolved_user_id of this BadUserStateAuthenticateUserResult.
        :type: str
        """
        self._resolved_user_id = resolved_user_id

    @property
    def user_state(self):
        """
        **[Required]** Gets the user_state of this BadUserStateAuthenticateUserResult.
        The bad user state.

        Allowed values for this property are: "USER_BLOCKED", "USER_DISABLED", "ONE_TIME_PASSWORD_EXPIRED", "PASSWORD_INVALID"


        :return: The user_state of this BadUserStateAuthenticateUserResult.
        :rtype: str
        """
        return self._user_state

    @user_state.setter
    def user_state(self, user_state):
        """
        Sets the user_state of this BadUserStateAuthenticateUserResult.
        The bad user state.


        :param user_state: The user_state of this BadUserStateAuthenticateUserResult.
        :type: str
        """
        allowed_values = ["USER_BLOCKED", "USER_DISABLED", "ONE_TIME_PASSWORD_EXPIRED", "PASSWORD_INVALID"]
        if not value_allowed_none_or_none_sentinel(user_state, allowed_values):
            raise ValueError(
                "Invalid value for `user_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._user_state = user_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
