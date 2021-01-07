# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Origin(object):
    """
    A detailed description of your web application's origin host server. An origin must be defined to set up WAF rules.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Origin object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param uri:
            The value to assign to the uri property of this Origin.
        :type uri: str

        :param http_port:
            The value to assign to the http_port property of this Origin.
        :type http_port: int

        :param https_port:
            The value to assign to the https_port property of this Origin.
        :type https_port: int

        :param custom_headers:
            The value to assign to the custom_headers property of this Origin.
        :type custom_headers: list[oci.waas.models.Header]

        """
        self.swagger_types = {
            'uri': 'str',
            'http_port': 'int',
            'https_port': 'int',
            'custom_headers': 'list[Header]'
        }

        self.attribute_map = {
            'uri': 'uri',
            'http_port': 'httpPort',
            'https_port': 'httpsPort',
            'custom_headers': 'customHeaders'
        }

        self._uri = None
        self._http_port = None
        self._https_port = None
        self._custom_headers = None

    @property
    def uri(self):
        """
        **[Required]** Gets the uri of this Origin.
        The URI of the origin. Does not support paths. Port numbers should be specified in the `httpPort` and `httpsPort` fields.


        :return: The uri of this Origin.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this Origin.
        The URI of the origin. Does not support paths. Port numbers should be specified in the `httpPort` and `httpsPort` fields.


        :param uri: The uri of this Origin.
        :type: str
        """
        self._uri = uri

    @property
    def http_port(self):
        """
        Gets the http_port of this Origin.
        The HTTP port on the origin that the web application listens on. If unspecified, defaults to `80`.


        :return: The http_port of this Origin.
        :rtype: int
        """
        return self._http_port

    @http_port.setter
    def http_port(self, http_port):
        """
        Sets the http_port of this Origin.
        The HTTP port on the origin that the web application listens on. If unspecified, defaults to `80`.


        :param http_port: The http_port of this Origin.
        :type: int
        """
        self._http_port = http_port

    @property
    def https_port(self):
        """
        Gets the https_port of this Origin.
        The HTTPS port on the origin that the web application listens on. If unspecified, defaults to `443`.


        :return: The https_port of this Origin.
        :rtype: int
        """
        return self._https_port

    @https_port.setter
    def https_port(self, https_port):
        """
        Sets the https_port of this Origin.
        The HTTPS port on the origin that the web application listens on. If unspecified, defaults to `443`.


        :param https_port: The https_port of this Origin.
        :type: int
        """
        self._https_port = https_port

    @property
    def custom_headers(self):
        """
        Gets the custom_headers of this Origin.
        A list of HTTP headers to forward to your origin.


        :return: The custom_headers of this Origin.
        :rtype: list[oci.waas.models.Header]
        """
        return self._custom_headers

    @custom_headers.setter
    def custom_headers(self, custom_headers):
        """
        Sets the custom_headers of this Origin.
        A list of HTTP headers to forward to your origin.


        :param custom_headers: The custom_headers of this Origin.
        :type: list[oci.waas.models.Header]
        """
        self._custom_headers = custom_headers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
