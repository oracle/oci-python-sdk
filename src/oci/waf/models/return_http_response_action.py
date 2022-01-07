# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .action import Action
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReturnHttpResponseAction(Action):
    """
    An object that represents an action which returns a defined HTTP response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ReturnHttpResponseAction object with values from keyword arguments. The default value of the :py:attr:`~oci.waf.models.ReturnHttpResponseAction.type` attribute
        of this class is ``RETURN_HTTP_RESPONSE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ReturnHttpResponseAction.
            Allowed values for this property are: "CHECK", "ALLOW", "RETURN_HTTP_RESPONSE"
        :type type: str

        :param name:
            The value to assign to the name property of this ReturnHttpResponseAction.
        :type name: str

        :param code:
            The value to assign to the code property of this ReturnHttpResponseAction.
        :type code: int

        :param headers:
            The value to assign to the headers property of this ReturnHttpResponseAction.
        :type headers: list[oci.waf.models.ResponseHeader]

        :param body:
            The value to assign to the body property of this ReturnHttpResponseAction.
        :type body: oci.waf.models.HttpResponseBody

        """
        self.swagger_types = {
            'type': 'str',
            'name': 'str',
            'code': 'int',
            'headers': 'list[ResponseHeader]',
            'body': 'HttpResponseBody'
        }

        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'code': 'code',
            'headers': 'headers',
            'body': 'body'
        }

        self._type = None
        self._name = None
        self._code = None
        self._headers = None
        self._body = None
        self._type = 'RETURN_HTTP_RESPONSE'

    @property
    def code(self):
        """
        **[Required]** Gets the code of this ReturnHttpResponseAction.
        Response code.

        The following response codes are valid values for this property:

        * 2xx

          200 OK
          201 Created
          202 Accepted
          206 Partial Content

        * 3xx

          300 Multiple Choices
          301 Moved Permanently
          302 Found
          303 See Other
          307 Temporary Redirect

        * 4xx

          400 Bad Request
          401 Unauthorized
          403 Forbidden
          404 Not Found
          405 Method Not Allowed
          408 Request Timeout
          409 Conflict
          411 Length Required
          412 Precondition Failed
          413 Payload Too Large
          414 URI Too Long
          415 Unsupported Media Type
          416 Range Not Satisfiable
          422 Unprocessable Entity
          494 Request Header Too Large
          495 Cert Error
          496 No Cert
          497 HTTP to HTTPS

        * 5xx

          500 Internal Server Error
          501 Not Implemented
          502 Bad Gateway
          503 Service Unavailable
          504 Gateway Timeout
          507 Insufficient Storage

        Example: `200`


        :return: The code of this ReturnHttpResponseAction.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ReturnHttpResponseAction.
        Response code.

        The following response codes are valid values for this property:

        * 2xx

          200 OK
          201 Created
          202 Accepted
          206 Partial Content

        * 3xx

          300 Multiple Choices
          301 Moved Permanently
          302 Found
          303 See Other
          307 Temporary Redirect

        * 4xx

          400 Bad Request
          401 Unauthorized
          403 Forbidden
          404 Not Found
          405 Method Not Allowed
          408 Request Timeout
          409 Conflict
          411 Length Required
          412 Precondition Failed
          413 Payload Too Large
          414 URI Too Long
          415 Unsupported Media Type
          416 Range Not Satisfiable
          422 Unprocessable Entity
          494 Request Header Too Large
          495 Cert Error
          496 No Cert
          497 HTTP to HTTPS

        * 5xx

          500 Internal Server Error
          501 Not Implemented
          502 Bad Gateway
          503 Service Unavailable
          504 Gateway Timeout
          507 Insufficient Storage

        Example: `200`


        :param code: The code of this ReturnHttpResponseAction.
        :type: int
        """
        self._code = code

    @property
    def headers(self):
        """
        Gets the headers of this ReturnHttpResponseAction.
        Adds headers defined in this array for HTTP response.

        Hop-by-hop headers are not allowed to be set:

        * Connection
        * Keep-Alive
        * Proxy-Authenticate
        * Proxy-Authorization
        * TE
        * Trailer
        * Transfer-Encoding
        * Upgrade


        :return: The headers of this ReturnHttpResponseAction.
        :rtype: list[oci.waf.models.ResponseHeader]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """
        Sets the headers of this ReturnHttpResponseAction.
        Adds headers defined in this array for HTTP response.

        Hop-by-hop headers are not allowed to be set:

        * Connection
        * Keep-Alive
        * Proxy-Authenticate
        * Proxy-Authorization
        * TE
        * Trailer
        * Transfer-Encoding
        * Upgrade


        :param headers: The headers of this ReturnHttpResponseAction.
        :type: list[oci.waf.models.ResponseHeader]
        """
        self._headers = headers

    @property
    def body(self):
        """
        Gets the body of this ReturnHttpResponseAction.

        :return: The body of this ReturnHttpResponseAction.
        :rtype: oci.waf.models.HttpResponseBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this ReturnHttpResponseAction.

        :param body: The body of this ReturnHttpResponseAction.
        :type: oci.waf.models.HttpResponseBody
        """
        self._body = body

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
