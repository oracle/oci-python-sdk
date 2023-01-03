# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthenticationRequest(object):
    """
    AuthenticationRequest model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AuthenticationRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param user_name:
            The value to assign to the user_name property of this AuthenticationRequest.
        :type user_name: str

        :param password:
            The value to assign to the password property of this AuthenticationRequest.
        :type password: str

        :param tenant_name:
            The value to assign to the tenant_name property of this AuthenticationRequest.
        :type tenant_name: str

        """
        self.swagger_types = {
            'user_name': 'str',
            'password': 'str',
            'tenant_name': 'str'
        }

        self.attribute_map = {
            'user_name': 'userName',
            'password': 'password',
            'tenant_name': 'tenantName'
        }

        self._user_name = None
        self._password = None
        self._tenant_name = None

    @property
    def user_name(self):
        """
        **[Required]** Gets the user_name of this AuthenticationRequest.
        The user name


        :return: The user_name of this AuthenticationRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this AuthenticationRequest.
        The user name


        :param user_name: The user_name of this AuthenticationRequest.
        :type: str
        """
        self._user_name = user_name

    @property
    def password(self):
        """
        **[Required]** Gets the password of this AuthenticationRequest.
        The password


        :return: The password of this AuthenticationRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this AuthenticationRequest.
        The password


        :param password: The password of this AuthenticationRequest.
        :type: str
        """
        self._password = password

    @property
    def tenant_name(self):
        """
        **[Required]** Gets the tenant_name of this AuthenticationRequest.
        The name of the tenancy


        :return: The tenant_name of this AuthenticationRequest.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """
        Sets the tenant_name of this AuthenticationRequest.
        The name of the tenancy


        :param tenant_name: The tenant_name of this AuthenticationRequest.
        :type: str
        """
        self._tenant_name = tenant_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
