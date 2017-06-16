# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class HealthChecker(object):

    def __init__(self):

        self.swagger_types = {
            'interval_in_millis': 'int',
            'port': 'int',
            'protocol': 'str',
            'response_body_regex': 'str',
            'retries': 'int',
            'return_code': 'int',
            'timeout_in_millis': 'int',
            'url_path': 'str'
        }

        self.attribute_map = {
            'interval_in_millis': 'intervalInMillis',
            'port': 'port',
            'protocol': 'protocol',
            'response_body_regex': 'responseBodyRegex',
            'retries': 'retries',
            'return_code': 'returnCode',
            'timeout_in_millis': 'timeoutInMillis',
            'url_path': 'urlPath'
        }

        self._interval_in_millis = None
        self._port = None
        self._protocol = None
        self._response_body_regex = None
        self._retries = None
        self._return_code = None
        self._timeout_in_millis = None
        self._url_path = None

    @property
    def interval_in_millis(self):
        """
        Gets the interval_in_millis of this HealthChecker.
        The interval between health checks, in milliseconds. The default is 10000 (10 seconds).

        Example: `30000`


        :return: The interval_in_millis of this HealthChecker.
        :rtype: int
        """
        return self._interval_in_millis

    @interval_in_millis.setter
    def interval_in_millis(self, interval_in_millis):
        """
        Sets the interval_in_millis of this HealthChecker.
        The interval between health checks, in milliseconds. The default is 10000 (10 seconds).

        Example: `30000`


        :param interval_in_millis: The interval_in_millis of this HealthChecker.
        :type: int
        """
        self._interval_in_millis = interval_in_millis

    @property
    def port(self):
        """
        Gets the port of this HealthChecker.
        The backend server port against which to run the health check. If the port is not specified, the load balancer uses the
        port information from the `Backend` object.

        Example: `8080`


        :return: The port of this HealthChecker.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this HealthChecker.
        The backend server port against which to run the health check. If the port is not specified, the load balancer uses the
        port information from the `Backend` object.

        Example: `8080`


        :param port: The port of this HealthChecker.
        :type: int
        """
        self._port = port

    @property
    def protocol(self):
        """
        Gets the protocol of this HealthChecker.
        The protocol the health check must use; either HTTP or TCP.

        Example: `HTTP`


        :return: The protocol of this HealthChecker.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this HealthChecker.
        The protocol the health check must use; either HTTP or TCP.

        Example: `HTTP`


        :param protocol: The protocol of this HealthChecker.
        :type: str
        """
        self._protocol = protocol

    @property
    def response_body_regex(self):
        """
        Gets the response_body_regex of this HealthChecker.
        A regular expression for parsing the response body from the backend server.

        Example: `^(500|40[1348])$`


        :return: The response_body_regex of this HealthChecker.
        :rtype: str
        """
        return self._response_body_regex

    @response_body_regex.setter
    def response_body_regex(self, response_body_regex):
        """
        Sets the response_body_regex of this HealthChecker.
        A regular expression for parsing the response body from the backend server.

        Example: `^(500|40[1348])$`


        :param response_body_regex: The response_body_regex of this HealthChecker.
        :type: str
        """
        self._response_body_regex = response_body_regex

    @property
    def retries(self):
        """
        Gets the retries of this HealthChecker.
        The number of retries to attempt before a backend server is considered \"unhealthy\". Defaults to 3.

        Example: `3`


        :return: The retries of this HealthChecker.
        :rtype: int
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """
        Sets the retries of this HealthChecker.
        The number of retries to attempt before a backend server is considered \"unhealthy\". Defaults to 3.

        Example: `3`


        :param retries: The retries of this HealthChecker.
        :type: int
        """
        self._retries = retries

    @property
    def return_code(self):
        """
        Gets the return_code of this HealthChecker.
        The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol,
        you can use common HTTP status codes such as \"200\".

        Example: `200`


        :return: The return_code of this HealthChecker.
        :rtype: int
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """
        Sets the return_code of this HealthChecker.
        The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol,
        you can use common HTTP status codes such as \"200\".

        Example: `200`


        :param return_code: The return_code of this HealthChecker.
        :type: int
        """
        self._return_code = return_code

    @property
    def timeout_in_millis(self):
        """
        Gets the timeout_in_millis of this HealthChecker.
        The maximum timeout before a retry, in milliseconds. Defaults to 3000 (3 seconds).

        Example: `6000`


        :return: The timeout_in_millis of this HealthChecker.
        :rtype: int
        """
        return self._timeout_in_millis

    @timeout_in_millis.setter
    def timeout_in_millis(self, timeout_in_millis):
        """
        Sets the timeout_in_millis of this HealthChecker.
        The maximum timeout before a retry, in milliseconds. Defaults to 3000 (3 seconds).

        Example: `6000`


        :param timeout_in_millis: The timeout_in_millis of this HealthChecker.
        :type: int
        """
        self._timeout_in_millis = timeout_in_millis

    @property
    def url_path(self):
        """
        Gets the url_path of this HealthChecker.
        The path against which to run the health check.

        Example: `/healthcheck`


        :return: The url_path of this HealthChecker.
        :rtype: str
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        """
        Sets the url_path of this HealthChecker.
        The path against which to run the health check.

        Example: `/healthcheck`


        :param url_path: The url_path of this HealthChecker.
        :type: str
        """
        self._url_path = url_path

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
