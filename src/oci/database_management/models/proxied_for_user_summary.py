# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProxiedForUserSummary(object):
    """
    A summary of users on whose behalf the current user acts as proxy.
    """

    #: A constant which can be used with the authentication property of a ProxiedForUserSummary.
    #: This constant has a value of "YES"
    AUTHENTICATION_YES = "YES"

    #: A constant which can be used with the authentication property of a ProxiedForUserSummary.
    #: This constant has a value of "NO"
    AUTHENTICATION_NO = "NO"

    #: A constant which can be used with the flags property of a ProxiedForUserSummary.
    #: This constant has a value of "PROXY_MAY_ACTIVATE_ALL_CLIENT_ROLES"
    FLAGS_PROXY_MAY_ACTIVATE_ALL_CLIENT_ROLES = "PROXY_MAY_ACTIVATE_ALL_CLIENT_ROLES"

    #: A constant which can be used with the flags property of a ProxiedForUserSummary.
    #: This constant has a value of "NO_CLIENT_ROLES_MAY_BE_ACTIVATED"
    FLAGS_NO_CLIENT_ROLES_MAY_BE_ACTIVATED = "NO_CLIENT_ROLES_MAY_BE_ACTIVATED"

    #: A constant which can be used with the flags property of a ProxiedForUserSummary.
    #: This constant has a value of "PROXY_MAY_ACTIVATE_ROLE"
    FLAGS_PROXY_MAY_ACTIVATE_ROLE = "PROXY_MAY_ACTIVATE_ROLE"

    #: A constant which can be used with the flags property of a ProxiedForUserSummary.
    #: This constant has a value of "PROXY_MAY_NOT_ACTIVATE_ROLE"
    FLAGS_PROXY_MAY_NOT_ACTIVATE_ROLE = "PROXY_MAY_NOT_ACTIVATE_ROLE"

    def __init__(self, **kwargs):
        """
        Initializes a new ProxiedForUserSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ProxiedForUserSummary.
        :type name: str

        :param authentication:
            The value to assign to the authentication property of this ProxiedForUserSummary.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type authentication: str

        :param flags:
            The value to assign to the flags property of this ProxiedForUserSummary.
            Allowed values for this property are: "PROXY_MAY_ACTIVATE_ALL_CLIENT_ROLES", "NO_CLIENT_ROLES_MAY_BE_ACTIVATED", "PROXY_MAY_ACTIVATE_ROLE", "PROXY_MAY_NOT_ACTIVATE_ROLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type flags: str

        """
        self.swagger_types = {
            'name': 'str',
            'authentication': 'str',
            'flags': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'authentication': 'authentication',
            'flags': 'flags'
        }

        self._name = None
        self._authentication = None
        self._flags = None

    @property
    def name(self):
        """
        Gets the name of this ProxiedForUserSummary.
        The name of a proxy user or the name of the client user.


        :return: The name of this ProxiedForUserSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProxiedForUserSummary.
        The name of a proxy user or the name of the client user.


        :param name: The name of this ProxiedForUserSummary.
        :type: str
        """
        self._name = name

    @property
    def authentication(self):
        """
        Gets the authentication of this ProxiedForUserSummary.
        Indicates whether the proxy is required to supply the client credentials (YES) or not (NO).

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The authentication of this ProxiedForUserSummary.
        :rtype: str
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """
        Sets the authentication of this ProxiedForUserSummary.
        Indicates whether the proxy is required to supply the client credentials (YES) or not (NO).


        :param authentication: The authentication of this ProxiedForUserSummary.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(authentication, allowed_values):
            authentication = 'UNKNOWN_ENUM_VALUE'
        self._authentication = authentication

    @property
    def flags(self):
        """
        Gets the flags of this ProxiedForUserSummary.
        The flags associated with the proxy/client pair.

        Allowed values for this property are: "PROXY_MAY_ACTIVATE_ALL_CLIENT_ROLES", "NO_CLIENT_ROLES_MAY_BE_ACTIVATED", "PROXY_MAY_ACTIVATE_ROLE", "PROXY_MAY_NOT_ACTIVATE_ROLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The flags of this ProxiedForUserSummary.
        :rtype: str
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """
        Sets the flags of this ProxiedForUserSummary.
        The flags associated with the proxy/client pair.


        :param flags: The flags of this ProxiedForUserSummary.
        :type: str
        """
        allowed_values = ["PROXY_MAY_ACTIVATE_ALL_CLIENT_ROLES", "NO_CLIENT_ROLES_MAY_BE_ACTIVATED", "PROXY_MAY_ACTIVATE_ROLE", "PROXY_MAY_NOT_ACTIVATE_ROLE"]
        if not value_allowed_none_or_none_sentinel(flags, allowed_values):
            flags = 'UNKNOWN_ENUM_VALUE'
        self._flags = flags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
