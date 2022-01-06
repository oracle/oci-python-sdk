# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateHealthCheckerDetails(object):
    """
    The health checker's configuration details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateHealthCheckerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param protocol:
            The value to assign to the protocol property of this UpdateHealthCheckerDetails.
        :type protocol: str

        :param url_path:
            The value to assign to the url_path property of this UpdateHealthCheckerDetails.
        :type url_path: str

        :param port:
            The value to assign to the port property of this UpdateHealthCheckerDetails.
        :type port: int

        :param return_code:
            The value to assign to the return_code property of this UpdateHealthCheckerDetails.
        :type return_code: int

        :param retries:
            The value to assign to the retries property of this UpdateHealthCheckerDetails.
        :type retries: int

        :param timeout_in_millis:
            The value to assign to the timeout_in_millis property of this UpdateHealthCheckerDetails.
        :type timeout_in_millis: int

        :param interval_in_millis:
            The value to assign to the interval_in_millis property of this UpdateHealthCheckerDetails.
        :type interval_in_millis: int

        :param response_body_regex:
            The value to assign to the response_body_regex property of this UpdateHealthCheckerDetails.
        :type response_body_regex: str

        """
        self.swagger_types = {
            'protocol': 'str',
            'url_path': 'str',
            'port': 'int',
            'return_code': 'int',
            'retries': 'int',
            'timeout_in_millis': 'int',
            'interval_in_millis': 'int',
            'response_body_regex': 'str'
        }

        self.attribute_map = {
            'protocol': 'protocol',
            'url_path': 'urlPath',
            'port': 'port',
            'return_code': 'returnCode',
            'retries': 'retries',
            'timeout_in_millis': 'timeoutInMillis',
            'interval_in_millis': 'intervalInMillis',
            'response_body_regex': 'responseBodyRegex'
        }

        self._protocol = None
        self._url_path = None
        self._port = None
        self._return_code = None
        self._retries = None
        self._timeout_in_millis = None
        self._interval_in_millis = None
        self._response_body_regex = None

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this UpdateHealthCheckerDetails.
        The protocol the health check must use; either HTTP or TCP.

        Example: `HTTP`


        :return: The protocol of this UpdateHealthCheckerDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this UpdateHealthCheckerDetails.
        The protocol the health check must use; either HTTP or TCP.

        Example: `HTTP`


        :param protocol: The protocol of this UpdateHealthCheckerDetails.
        :type: str
        """
        self._protocol = protocol

    @property
    def url_path(self):
        """
        Gets the url_path of this UpdateHealthCheckerDetails.
        The path against which to run the health check.

        Example: `/healthcheck`


        :return: The url_path of this UpdateHealthCheckerDetails.
        :rtype: str
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        """
        Sets the url_path of this UpdateHealthCheckerDetails.
        The path against which to run the health check.

        Example: `/healthcheck`


        :param url_path: The url_path of this UpdateHealthCheckerDetails.
        :type: str
        """
        self._url_path = url_path

    @property
    def port(self):
        """
        **[Required]** Gets the port of this UpdateHealthCheckerDetails.
        The backend server port against which to run the health check.

        Example: `8080`


        :return: The port of this UpdateHealthCheckerDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this UpdateHealthCheckerDetails.
        The backend server port against which to run the health check.

        Example: `8080`


        :param port: The port of this UpdateHealthCheckerDetails.
        :type: int
        """
        self._port = port

    @property
    def return_code(self):
        """
        **[Required]** Gets the return_code of this UpdateHealthCheckerDetails.
        The status code a healthy backend server should return.

        Example: `200`


        :return: The return_code of this UpdateHealthCheckerDetails.
        :rtype: int
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """
        Sets the return_code of this UpdateHealthCheckerDetails.
        The status code a healthy backend server should return.

        Example: `200`


        :param return_code: The return_code of this UpdateHealthCheckerDetails.
        :type: int
        """
        self._return_code = return_code

    @property
    def retries(self):
        """
        **[Required]** Gets the retries of this UpdateHealthCheckerDetails.
        The number of retries to attempt before a backend server is considered \"unhealthy\". This number also applies
        when recovering a server to the \"healthy\" state.

        Example: `3`


        :return: The retries of this UpdateHealthCheckerDetails.
        :rtype: int
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """
        Sets the retries of this UpdateHealthCheckerDetails.
        The number of retries to attempt before a backend server is considered \"unhealthy\". This number also applies
        when recovering a server to the \"healthy\" state.

        Example: `3`


        :param retries: The retries of this UpdateHealthCheckerDetails.
        :type: int
        """
        self._retries = retries

    @property
    def timeout_in_millis(self):
        """
        **[Required]** Gets the timeout_in_millis of this UpdateHealthCheckerDetails.
        The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply
        returns within this timeout period.

        Example: `3000`


        :return: The timeout_in_millis of this UpdateHealthCheckerDetails.
        :rtype: int
        """
        return self._timeout_in_millis

    @timeout_in_millis.setter
    def timeout_in_millis(self, timeout_in_millis):
        """
        Sets the timeout_in_millis of this UpdateHealthCheckerDetails.
        The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply
        returns within this timeout period.

        Example: `3000`


        :param timeout_in_millis: The timeout_in_millis of this UpdateHealthCheckerDetails.
        :type: int
        """
        self._timeout_in_millis = timeout_in_millis

    @property
    def interval_in_millis(self):
        """
        **[Required]** Gets the interval_in_millis of this UpdateHealthCheckerDetails.
        The interval between health checks, in milliseconds.

        Example: `10000`


        :return: The interval_in_millis of this UpdateHealthCheckerDetails.
        :rtype: int
        """
        return self._interval_in_millis

    @interval_in_millis.setter
    def interval_in_millis(self, interval_in_millis):
        """
        Sets the interval_in_millis of this UpdateHealthCheckerDetails.
        The interval between health checks, in milliseconds.

        Example: `10000`


        :param interval_in_millis: The interval_in_millis of this UpdateHealthCheckerDetails.
        :type: int
        """
        self._interval_in_millis = interval_in_millis

    @property
    def response_body_regex(self):
        """
        **[Required]** Gets the response_body_regex of this UpdateHealthCheckerDetails.
        A regular expression for parsing the response body from the backend server.

        Example: `^((?!false).|\\s)*$`


        :return: The response_body_regex of this UpdateHealthCheckerDetails.
        :rtype: str
        """
        return self._response_body_regex

    @response_body_regex.setter
    def response_body_regex(self, response_body_regex):
        """
        Sets the response_body_regex of this UpdateHealthCheckerDetails.
        A regular expression for parsing the response body from the backend server.

        Example: `^((?!false).|\\s)*$`


        :param response_body_regex: The response_body_regex of this UpdateHealthCheckerDetails.
        :type: str
        """
        self._response_body_regex = response_body_regex

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
