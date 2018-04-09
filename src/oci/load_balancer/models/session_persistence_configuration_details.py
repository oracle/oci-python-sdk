# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SessionPersistenceConfigurationDetails(object):
    """
    The configuration details for implementing session persistence. Session persistence enables the Load Balancing
    Service to direct any number of requests that originate from a single logical client to a single backend web server.
    For more information, see `Session Persistence`__.

    To disable session persistence on a running load balancer, use the
    :func:`update_backend_set` operation and specify \"null\" for the
    `SessionPersistenceConfigurationDetails` object.

    Example: `SessionPersistenceConfigurationDetails: null`

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Balance/Reference/sessionpersistence.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SessionPersistenceConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cookie_name:
            The value to assign to the cookie_name property of this SessionPersistenceConfigurationDetails.
        :type cookie_name: str

        :param disable_fallback:
            The value to assign to the disable_fallback property of this SessionPersistenceConfigurationDetails.
        :type disable_fallback: bool

        """
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
        **[Required]** Gets the cookie_name of this SessionPersistenceConfigurationDetails.
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
