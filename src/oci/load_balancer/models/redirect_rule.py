# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .rule import Rule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RedirectRule(Rule):
    """
    An object that represents the action of returning a specified response code and a redirect URI. Each RedirectRule
    object is configured for a particular listener and a designated path.

    The default response code is `302 Found`.

    **NOTES:**
    *  This rule applies only to HTTP listeners.
    *  You can specify this rule only with the :func:`rule_condition`
    type `PATH`.
    *  A listener can have only one RedirectRule object for a given original path. The
    :func:`path_match_condition` `attributeValue` specifies the
    original path.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RedirectRule object with values from keyword arguments. The default value of the :py:attr:`~oci.load_balancer.models.RedirectRule.action` attribute
        of this class is ``REDIRECT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this RedirectRule.
            Allowed values for this property are: "ADD_HTTP_REQUEST_HEADER", "EXTEND_HTTP_REQUEST_HEADER_VALUE", "REMOVE_HTTP_REQUEST_HEADER", "ADD_HTTP_RESPONSE_HEADER", "EXTEND_HTTP_RESPONSE_HEADER_VALUE", "REMOVE_HTTP_RESPONSE_HEADER", "ALLOW", "CONTROL_ACCESS_USING_HTTP_METHODS", "REDIRECT"
        :type action: str

        :param response_code:
            The value to assign to the response_code property of this RedirectRule.
        :type response_code: int

        :param conditions:
            The value to assign to the conditions property of this RedirectRule.
        :type conditions: list[RuleCondition]

        :param redirect_uri:
            The value to assign to the redirect_uri property of this RedirectRule.
        :type redirect_uri: RedirectUri

        """
        self.swagger_types = {
            'action': 'str',
            'response_code': 'int',
            'conditions': 'list[RuleCondition]',
            'redirect_uri': 'RedirectUri'
        }

        self.attribute_map = {
            'action': 'action',
            'response_code': 'responseCode',
            'conditions': 'conditions',
            'redirect_uri': 'redirectUri'
        }

        self._action = None
        self._response_code = None
        self._conditions = None
        self._redirect_uri = None
        self._action = 'REDIRECT'

    @property
    def response_code(self):
        """
        Gets the response_code of this RedirectRule.
        The HTTP status code to return when the incoming request is redirected.

        The status line returned with the code is mapped from the standard HTTP specification. Valid response
        codes for redirection are:

        *  301
        *  302
        *  303
        *  307
        *  308

        The default value is `302` (Found).

        Example: `301`


        :return: The response_code of this RedirectRule.
        :rtype: int
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this RedirectRule.
        The HTTP status code to return when the incoming request is redirected.

        The status line returned with the code is mapped from the standard HTTP specification. Valid response
        codes for redirection are:

        *  301
        *  302
        *  303
        *  307
        *  308

        The default value is `302` (Found).

        Example: `301`


        :param response_code: The response_code of this RedirectRule.
        :type: int
        """
        self._response_code = response_code

    @property
    def conditions(self):
        """
        **[Required]** Gets the conditions of this RedirectRule.

        :return: The conditions of this RedirectRule.
        :rtype: list[RuleCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this RedirectRule.

        :param conditions: The conditions of this RedirectRule.
        :type: list[RuleCondition]
        """
        self._conditions = conditions

    @property
    def redirect_uri(self):
        """
        Gets the redirect_uri of this RedirectRule.

        :return: The redirect_uri of this RedirectRule.
        :rtype: RedirectUri
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """
        Sets the redirect_uri of this RedirectRule.

        :param redirect_uri: The redirect_uri of this RedirectRule.
        :type: RedirectUri
        """
        self._redirect_uri = redirect_uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
