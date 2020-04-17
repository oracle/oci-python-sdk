# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HttpRedirectTarget(object):
    """
    HttpRedirectTarget model.
    """

    #: A constant which can be used with the protocol property of a HttpRedirectTarget.
    #: This constant has a value of "HTTP"
    PROTOCOL_HTTP = "HTTP"

    #: A constant which can be used with the protocol property of a HttpRedirectTarget.
    #: This constant has a value of "HTTPS"
    PROTOCOL_HTTPS = "HTTPS"

    def __init__(self, **kwargs):
        """
        Initializes a new HttpRedirectTarget object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param protocol:
            The value to assign to the protocol property of this HttpRedirectTarget.
            Allowed values for this property are: "HTTP", "HTTPS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protocol: str

        :param host:
            The value to assign to the host property of this HttpRedirectTarget.
        :type host: str

        :param port:
            The value to assign to the port property of this HttpRedirectTarget.
        :type port: int

        :param path:
            The value to assign to the path property of this HttpRedirectTarget.
        :type path: str

        :param query:
            The value to assign to the query property of this HttpRedirectTarget.
        :type query: str

        """
        self.swagger_types = {
            'protocol': 'str',
            'host': 'str',
            'port': 'int',
            'path': 'str',
            'query': 'str'
        }

        self.attribute_map = {
            'protocol': 'protocol',
            'host': 'host',
            'port': 'port',
            'path': 'path',
            'query': 'query'
        }

        self._protocol = None
        self._host = None
        self._port = None
        self._path = None
        self._query = None

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this HttpRedirectTarget.
        The protocol used for the target, http or https.

        Allowed values for this property are: "HTTP", "HTTPS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protocol of this HttpRedirectTarget.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this HttpRedirectTarget.
        The protocol used for the target, http or https.


        :param protocol: The protocol of this HttpRedirectTarget.
        :type: str
        """
        allowed_values = ["HTTP", "HTTPS"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            protocol = 'UNKNOWN_ENUM_VALUE'
        self._protocol = protocol

    @property
    def host(self):
        """
        **[Required]** Gets the host of this HttpRedirectTarget.
        The host portion of the redirect.


        :return: The host of this HttpRedirectTarget.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this HttpRedirectTarget.
        The host portion of the redirect.


        :param host: The host of this HttpRedirectTarget.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        Gets the port of this HttpRedirectTarget.
        Port number of the target destination of the redirect, default to match protocol


        :return: The port of this HttpRedirectTarget.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this HttpRedirectTarget.
        Port number of the target destination of the redirect, default to match protocol


        :param port: The port of this HttpRedirectTarget.
        :type: int
        """
        self._port = port

    @property
    def path(self):
        """
        **[Required]** Gets the path of this HttpRedirectTarget.
        The path component of the target URL (e.g., \"/path/to/resource\" in \"https://target.example.com/path/to/resource?redirected\"), which can be empty, static, or request-copying, or request-prefixing. Use of \\ is not permitted except to escape a following \\, {, or }. An empty value is treated the same as static \"/\". A static value must begin with a leading \"/\", optionally followed by other path characters. A request-copying value must exactly match \"{path}\", and will be replaced with the path component of the request URL (including its initial \"/\"). A request-prefixing value must start with \"/\" and end with a non-escaped \"{path}\", which will be replaced with the path component of the request URL (including its initial \"/\"). Only one such replacement token is allowed.


        :return: The path of this HttpRedirectTarget.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this HttpRedirectTarget.
        The path component of the target URL (e.g., \"/path/to/resource\" in \"https://target.example.com/path/to/resource?redirected\"), which can be empty, static, or request-copying, or request-prefixing. Use of \\ is not permitted except to escape a following \\, {, or }. An empty value is treated the same as static \"/\". A static value must begin with a leading \"/\", optionally followed by other path characters. A request-copying value must exactly match \"{path}\", and will be replaced with the path component of the request URL (including its initial \"/\"). A request-prefixing value must start with \"/\" and end with a non-escaped \"{path}\", which will be replaced with the path component of the request URL (including its initial \"/\"). Only one such replacement token is allowed.


        :param path: The path of this HttpRedirectTarget.
        :type: str
        """
        self._path = path

    @property
    def query(self):
        """
        **[Required]** Gets the query of this HttpRedirectTarget.
        The query component of the target URL (e.g., \"?redirected\" in \"https://target.example.com/path/to/resource?redirected\"), which can be empty, static, or request-copying. Use of \\ is not permitted except to escape a following \\, {, or }. An empty value results in a redirection target URL with no query component. A static value must begin with a leading \"?\", optionally followed by other query characters. A request-copying value must exactly match \"{query}\", and will be replaced with the query component of the request URL (including a leading \"?\" if and only if the request URL includes a query component).


        :return: The query of this HttpRedirectTarget.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this HttpRedirectTarget.
        The query component of the target URL (e.g., \"?redirected\" in \"https://target.example.com/path/to/resource?redirected\"), which can be empty, static, or request-copying. Use of \\ is not permitted except to escape a following \\, {, or }. An empty value results in a redirection target URL with no query component. A static value must begin with a leading \"?\", optionally followed by other query characters. A request-copying value must exactly match \"{query}\", and will be replaced with the query component of the request URL (including a leading \"?\" if and only if the request URL includes a query component).


        :param query: The query of this HttpRedirectTarget.
        :type: str
        """
        self._query = query

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
