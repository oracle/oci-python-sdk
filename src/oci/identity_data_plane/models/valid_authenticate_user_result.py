# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValidAuthenticateUserResult(object):
    """
    ValidAuthenticateUserResult model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ValidAuthenticateUserResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tenant_input:
            The value to assign to the tenant_input property of this ValidAuthenticateUserResult.
        :type tenant_input: str

        :param user_input:
            The value to assign to the user_input property of this ValidAuthenticateUserResult.
        :type user_input: str

        :param resolved_principal:
            The value to assign to the resolved_principal property of this ValidAuthenticateUserResult.
        :type resolved_principal: oci.identity_data_plane.models.AuthenticationPrincipal

        """
        self.swagger_types = {
            'tenant_input': 'str',
            'user_input': 'str',
            'resolved_principal': 'AuthenticationPrincipal'
        }

        self.attribute_map = {
            'tenant_input': 'tenantInput',
            'user_input': 'userInput',
            'resolved_principal': 'resolvedPrincipal'
        }

        self._tenant_input = None
        self._user_input = None
        self._resolved_principal = None

    @property
    def tenant_input(self):
        """
        **[Required]** Gets the tenant_input of this ValidAuthenticateUserResult.
        The tenant name.


        :return: The tenant_input of this ValidAuthenticateUserResult.
        :rtype: str
        """
        return self._tenant_input

    @tenant_input.setter
    def tenant_input(self, tenant_input):
        """
        Sets the tenant_input of this ValidAuthenticateUserResult.
        The tenant name.


        :param tenant_input: The tenant_input of this ValidAuthenticateUserResult.
        :type: str
        """
        self._tenant_input = tenant_input

    @property
    def user_input(self):
        """
        **[Required]** Gets the user_input of this ValidAuthenticateUserResult.
        The user name.


        :return: The user_input of this ValidAuthenticateUserResult.
        :rtype: str
        """
        return self._user_input

    @user_input.setter
    def user_input(self, user_input):
        """
        Sets the user_input of this ValidAuthenticateUserResult.
        The user name.


        :param user_input: The user_input of this ValidAuthenticateUserResult.
        :type: str
        """
        self._user_input = user_input

    @property
    def resolved_principal(self):
        """
        **[Required]** Gets the resolved_principal of this ValidAuthenticateUserResult.
        The resolved principal.


        :return: The resolved_principal of this ValidAuthenticateUserResult.
        :rtype: oci.identity_data_plane.models.AuthenticationPrincipal
        """
        return self._resolved_principal

    @resolved_principal.setter
    def resolved_principal(self, resolved_principal):
        """
        Sets the resolved_principal of this ValidAuthenticateUserResult.
        The resolved principal.


        :param resolved_principal: The resolved_principal of this ValidAuthenticateUserResult.
        :type: oci.identity_data_plane.models.AuthenticationPrincipal
        """
        self._resolved_principal = resolved_principal

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
