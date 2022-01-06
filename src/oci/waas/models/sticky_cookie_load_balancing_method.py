# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .load_balancing_method import LoadBalancingMethod
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StickyCookieLoadBalancingMethod(LoadBalancingMethod):
    """
    An object that represents the `sticky-cookie` load balancing method and its properties.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StickyCookieLoadBalancingMethod object with values from keyword arguments. The default value of the :py:attr:`~oci.waas.models.StickyCookieLoadBalancingMethod.method` attribute
        of this class is ``STICKY_COOKIE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param method:
            The value to assign to the method property of this StickyCookieLoadBalancingMethod.
            Allowed values for this property are: "IP_HASH", "ROUND_ROBIN", "STICKY_COOKIE"
        :type method: str

        :param name:
            The value to assign to the name property of this StickyCookieLoadBalancingMethod.
        :type name: str

        :param domain:
            The value to assign to the domain property of this StickyCookieLoadBalancingMethod.
        :type domain: str

        :param expiration_time_in_seconds:
            The value to assign to the expiration_time_in_seconds property of this StickyCookieLoadBalancingMethod.
        :type expiration_time_in_seconds: int

        """
        self.swagger_types = {
            'method': 'str',
            'name': 'str',
            'domain': 'str',
            'expiration_time_in_seconds': 'int'
        }

        self.attribute_map = {
            'method': 'method',
            'name': 'name',
            'domain': 'domain',
            'expiration_time_in_seconds': 'expirationTimeInSeconds'
        }

        self._method = None
        self._name = None
        self._domain = None
        self._expiration_time_in_seconds = None
        self._method = 'STICKY_COOKIE'

    @property
    def name(self):
        """
        Gets the name of this StickyCookieLoadBalancingMethod.
        The name of the cookie used to track the persistence.
        Can contain any US-ASCII character except separator or control character.


        :return: The name of this StickyCookieLoadBalancingMethod.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StickyCookieLoadBalancingMethod.
        The name of the cookie used to track the persistence.
        Can contain any US-ASCII character except separator or control character.


        :param name: The name of this StickyCookieLoadBalancingMethod.
        :type: str
        """
        self._name = name

    @property
    def domain(self):
        """
        Gets the domain of this StickyCookieLoadBalancingMethod.
        The domain for which the cookie is set, defaults to WAAS policy domain.


        :return: The domain of this StickyCookieLoadBalancingMethod.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this StickyCookieLoadBalancingMethod.
        The domain for which the cookie is set, defaults to WAAS policy domain.


        :param domain: The domain of this StickyCookieLoadBalancingMethod.
        :type: str
        """
        self._domain = domain

    @property
    def expiration_time_in_seconds(self):
        """
        Gets the expiration_time_in_seconds of this StickyCookieLoadBalancingMethod.
        The time for which a browser should keep the cookie in seconds.
        Empty value will cause the cookie to expire at the end of a browser session.


        :return: The expiration_time_in_seconds of this StickyCookieLoadBalancingMethod.
        :rtype: int
        """
        return self._expiration_time_in_seconds

    @expiration_time_in_seconds.setter
    def expiration_time_in_seconds(self, expiration_time_in_seconds):
        """
        Sets the expiration_time_in_seconds of this StickyCookieLoadBalancingMethod.
        The time for which a browser should keep the cookie in seconds.
        Empty value will cause the cookie to expire at the end of a browser session.


        :param expiration_time_in_seconds: The expiration_time_in_seconds of this StickyCookieLoadBalancingMethod.
        :type: int
        """
        self._expiration_time_in_seconds = expiration_time_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
