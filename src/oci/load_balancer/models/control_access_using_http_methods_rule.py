# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .rule import Rule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ControlAccessUsingHttpMethodsRule(Rule):
    """
    An object that represents the action of returning a specified response code when the requested HTTP method is not in
    the list of allowed methods for the listener. The load balancer does not forward a disallowed request to the back end
    servers. The default response code is `405 Method Not Allowed`.

    If you set the response code to `405` or leave it blank, the system adds an \"allow\" response header that contains a
    list of the allowed methods for the listener. If you set the response code to anything other than `405` (or blank),
    the system does not add the \"allow\" response header with a list of allowed methods.

    This rule applies only to HTTP listeners. No more than one `ControlAccessUsingHttpMethodsRule` object can be present in
    a given listener.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ControlAccessUsingHttpMethodsRule object with values from keyword arguments. The default value of the :py:attr:`~oci.load_balancer.models.ControlAccessUsingHttpMethodsRule.action` attribute
        of this class is ``CONTROL_ACCESS_USING_HTTP_METHODS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this ControlAccessUsingHttpMethodsRule.
            Allowed values for this property are: "ADD_HTTP_REQUEST_HEADER", "EXTEND_HTTP_REQUEST_HEADER_VALUE", "REMOVE_HTTP_REQUEST_HEADER", "ADD_HTTP_RESPONSE_HEADER", "EXTEND_HTTP_RESPONSE_HEADER_VALUE", "REMOVE_HTTP_RESPONSE_HEADER", "ALLOW", "CONTROL_ACCESS_USING_HTTP_METHODS", "REDIRECT", "HTTP_HEADER"
        :type action: str

        :param allowed_methods:
            The value to assign to the allowed_methods property of this ControlAccessUsingHttpMethodsRule.
        :type allowed_methods: list[str]

        :param status_code:
            The value to assign to the status_code property of this ControlAccessUsingHttpMethodsRule.
        :type status_code: int

        """
        self.swagger_types = {
            'action': 'str',
            'allowed_methods': 'list[str]',
            'status_code': 'int'
        }

        self.attribute_map = {
            'action': 'action',
            'allowed_methods': 'allowedMethods',
            'status_code': 'statusCode'
        }

        self._action = None
        self._allowed_methods = None
        self._status_code = None
        self._action = 'CONTROL_ACCESS_USING_HTTP_METHODS'

    @property
    def allowed_methods(self):
        """
        **[Required]** Gets the allowed_methods of this ControlAccessUsingHttpMethodsRule.
        The list of HTTP methods allowed for this listener.

        By default, you can specify only the standard HTTP methods defined in the
        `HTTP Method Registry`__. You can also
        see a list of supported standard HTTP methods in the Load Balancing service documentation at
        `Managing Rule Sets`__.

        Your backend application must be able to handle the methods specified in this list.

        The list of HTTP methods is extensible. If you need to configure custom HTTP methods, contact
        `My Oracle Support`__ to remove the restriction for your tenancy.

        Example: [\"GET\", \"PUT\", \"POST\", \"PROPFIND\"]

        __ http://www.iana.org/assignments/http-methods/http-methods.xhtml
        __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrulesets.htm
        __ http://support.oracle.com/


        :return: The allowed_methods of this ControlAccessUsingHttpMethodsRule.
        :rtype: list[str]
        """
        return self._allowed_methods

    @allowed_methods.setter
    def allowed_methods(self, allowed_methods):
        """
        Sets the allowed_methods of this ControlAccessUsingHttpMethodsRule.
        The list of HTTP methods allowed for this listener.

        By default, you can specify only the standard HTTP methods defined in the
        `HTTP Method Registry`__. You can also
        see a list of supported standard HTTP methods in the Load Balancing service documentation at
        `Managing Rule Sets`__.

        Your backend application must be able to handle the methods specified in this list.

        The list of HTTP methods is extensible. If you need to configure custom HTTP methods, contact
        `My Oracle Support`__ to remove the restriction for your tenancy.

        Example: [\"GET\", \"PUT\", \"POST\", \"PROPFIND\"]

        __ http://www.iana.org/assignments/http-methods/http-methods.xhtml
        __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrulesets.htm
        __ http://support.oracle.com/


        :param allowed_methods: The allowed_methods of this ControlAccessUsingHttpMethodsRule.
        :type: list[str]
        """
        self._allowed_methods = allowed_methods

    @property
    def status_code(self):
        """
        Gets the status_code of this ControlAccessUsingHttpMethodsRule.
        The HTTP status code to return when the requested HTTP method is not in the list of allowed methods.
        The associated status line returned with the code is mapped from the standard HTTP specification. The
        default value is `405 (Method Not Allowed)`.

        Example: 403


        :return: The status_code of this ControlAccessUsingHttpMethodsRule.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """
        Sets the status_code of this ControlAccessUsingHttpMethodsRule.
        The HTTP status code to return when the requested HTTP method is not in the list of allowed methods.
        The associated status line returned with the code is mapped from the standard HTTP specification. The
        default value is `405 (Method Not Allowed)`.

        Example: 403


        :param status_code: The status_code of this ControlAccessUsingHttpMethodsRule.
        :type: int
        """
        self._status_code = status_code

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
