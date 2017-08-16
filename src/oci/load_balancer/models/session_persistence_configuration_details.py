# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class SessionPersistenceConfigurationDetails(object):

    def __init__(self):

        self.swagger_types = {
            'cookie_name': 'str',
            'disable_fallback': 'bool'
        }

        self.attribute_map = {
            'cookie_name': 'cookieName',
            'disable_fallback': 'disableFallback'
        }

        self._cookie_name = None
        self._disable_fallback = None

    @property
    def cookie_name(self):
        """
        Gets the cookie_name of this SessionPersistenceConfigurationDetails.
        The name of the cookie used to detect a session initiated by the backend server. Use '*' to specify
        that any cookie set by the backend causes the session to persist.

        Example: `myCookieName`


        :return: The cookie_name of this SessionPersistenceConfigurationDetails.
        :rtype: str
        """
        return self._cookie_name

    @cookie_name.setter
    def cookie_name(self, cookie_name):
        """
        Sets the cookie_name of this SessionPersistenceConfigurationDetails.
        The name of the cookie used to detect a session initiated by the backend server. Use '*' to specify
        that any cookie set by the backend causes the session to persist.

        Example: `myCookieName`


        :param cookie_name: The cookie_name of this SessionPersistenceConfigurationDetails.
        :type: str
        """
        self._cookie_name = cookie_name

    @property
    def disable_fallback(self):
        """
        Gets the disable_fallback of this SessionPersistenceConfigurationDetails.
        Whether the load balancer is prevented from directing traffic from a persistent session client to
        a different backend server if the original server is unavailable. Defaults to false.

        Example: `true`


        :return: The disable_fallback of this SessionPersistenceConfigurationDetails.
        :rtype: bool
        """
        return self._disable_fallback

    @disable_fallback.setter
    def disable_fallback(self, disable_fallback):
        """
        Sets the disable_fallback of this SessionPersistenceConfigurationDetails.
        Whether the load balancer is prevented from directing traffic from a persistent session client to
        a different backend server if the original server is unavailable. Defaults to false.

        Example: `true`


        :param disable_fallback: The disable_fallback of this SessionPersistenceConfigurationDetails.
        :type: bool
        """
        self._disable_fallback = disable_fallback

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
