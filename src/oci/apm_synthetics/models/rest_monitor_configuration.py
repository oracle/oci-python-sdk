# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .monitor_configuration import MonitorConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RestMonitorConfiguration(MonitorConfiguration):
    """
    Request configuration details for the REST monitor type.
    """

    #: A constant which can be used with the request_method property of a RestMonitorConfiguration.
    #: This constant has a value of "GET"
    REQUEST_METHOD_GET = "GET"

    #: A constant which can be used with the request_method property of a RestMonitorConfiguration.
    #: This constant has a value of "POST"
    REQUEST_METHOD_POST = "POST"

    #: A constant which can be used with the req_authentication_scheme property of a RestMonitorConfiguration.
    #: This constant has a value of "OAUTH"
    REQ_AUTHENTICATION_SCHEME_OAUTH = "OAUTH"

    #: A constant which can be used with the req_authentication_scheme property of a RestMonitorConfiguration.
    #: This constant has a value of "NONE"
    REQ_AUTHENTICATION_SCHEME_NONE = "NONE"

    #: A constant which can be used with the req_authentication_scheme property of a RestMonitorConfiguration.
    #: This constant has a value of "BASIC"
    REQ_AUTHENTICATION_SCHEME_BASIC = "BASIC"

    #: A constant which can be used with the req_authentication_scheme property of a RestMonitorConfiguration.
    #: This constant has a value of "BEARER"
    REQ_AUTHENTICATION_SCHEME_BEARER = "BEARER"

    def __init__(self, **kwargs):
        """
        Initializes a new RestMonitorConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.apm_synthetics.models.RestMonitorConfiguration.config_type` attribute
        of this class is ``REST_CONFIG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_type:
            The value to assign to the config_type property of this RestMonitorConfiguration.
            Allowed values for this property are: "BROWSER_CONFIG", "SCRIPTED_BROWSER_CONFIG", "REST_CONFIG", "SCRIPTED_REST_CONFIG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type config_type: str

        :param is_failure_retried:
            The value to assign to the is_failure_retried property of this RestMonitorConfiguration.
        :type is_failure_retried: bool

        :param dns_configuration:
            The value to assign to the dns_configuration property of this RestMonitorConfiguration.
        :type dns_configuration: oci.apm_synthetics.models.DnsConfiguration

        :param is_redirection_enabled:
            The value to assign to the is_redirection_enabled property of this RestMonitorConfiguration.
        :type is_redirection_enabled: bool

        :param is_certificate_validation_enabled:
            The value to assign to the is_certificate_validation_enabled property of this RestMonitorConfiguration.
        :type is_certificate_validation_enabled: bool

        :param request_method:
            The value to assign to the request_method property of this RestMonitorConfiguration.
            Allowed values for this property are: "GET", "POST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type request_method: str

        :param req_authentication_scheme:
            The value to assign to the req_authentication_scheme property of this RestMonitorConfiguration.
            Allowed values for this property are: "OAUTH", "NONE", "BASIC", "BEARER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type req_authentication_scheme: str

        :param req_authentication_details:
            The value to assign to the req_authentication_details property of this RestMonitorConfiguration.
        :type req_authentication_details: oci.apm_synthetics.models.RequestAuthenticationDetails

        :param request_headers:
            The value to assign to the request_headers property of this RestMonitorConfiguration.
        :type request_headers: list[oci.apm_synthetics.models.Header]

        :param request_query_params:
            The value to assign to the request_query_params property of this RestMonitorConfiguration.
        :type request_query_params: list[oci.apm_synthetics.models.RequestQueryParam]

        :param request_post_body:
            The value to assign to the request_post_body property of this RestMonitorConfiguration.
        :type request_post_body: str

        :param verify_response_content:
            The value to assign to the verify_response_content property of this RestMonitorConfiguration.
        :type verify_response_content: str

        :param verify_response_codes:
            The value to assign to the verify_response_codes property of this RestMonitorConfiguration.
        :type verify_response_codes: list[str]

        :param network_configuration:
            The value to assign to the network_configuration property of this RestMonitorConfiguration.
        :type network_configuration: oci.apm_synthetics.models.NetworkConfiguration

        """
        self.swagger_types = {
            'config_type': 'str',
            'is_failure_retried': 'bool',
            'dns_configuration': 'DnsConfiguration',
            'is_redirection_enabled': 'bool',
            'is_certificate_validation_enabled': 'bool',
            'request_method': 'str',
            'req_authentication_scheme': 'str',
            'req_authentication_details': 'RequestAuthenticationDetails',
            'request_headers': 'list[Header]',
            'request_query_params': 'list[RequestQueryParam]',
            'request_post_body': 'str',
            'verify_response_content': 'str',
            'verify_response_codes': 'list[str]',
            'network_configuration': 'NetworkConfiguration'
        }

        self.attribute_map = {
            'config_type': 'configType',
            'is_failure_retried': 'isFailureRetried',
            'dns_configuration': 'dnsConfiguration',
            'is_redirection_enabled': 'isRedirectionEnabled',
            'is_certificate_validation_enabled': 'isCertificateValidationEnabled',
            'request_method': 'requestMethod',
            'req_authentication_scheme': 'reqAuthenticationScheme',
            'req_authentication_details': 'reqAuthenticationDetails',
            'request_headers': 'requestHeaders',
            'request_query_params': 'requestQueryParams',
            'request_post_body': 'requestPostBody',
            'verify_response_content': 'verifyResponseContent',
            'verify_response_codes': 'verifyResponseCodes',
            'network_configuration': 'networkConfiguration'
        }

        self._config_type = None
        self._is_failure_retried = None
        self._dns_configuration = None
        self._is_redirection_enabled = None
        self._is_certificate_validation_enabled = None
        self._request_method = None
        self._req_authentication_scheme = None
        self._req_authentication_details = None
        self._request_headers = None
        self._request_query_params = None
        self._request_post_body = None
        self._verify_response_content = None
        self._verify_response_codes = None
        self._network_configuration = None
        self._config_type = 'REST_CONFIG'

    @property
    def is_redirection_enabled(self):
        """
        Gets the is_redirection_enabled of this RestMonitorConfiguration.
        If redirection enabled, then redirects will be allowed while accessing target URL.


        :return: The is_redirection_enabled of this RestMonitorConfiguration.
        :rtype: bool
        """
        return self._is_redirection_enabled

    @is_redirection_enabled.setter
    def is_redirection_enabled(self, is_redirection_enabled):
        """
        Sets the is_redirection_enabled of this RestMonitorConfiguration.
        If redirection enabled, then redirects will be allowed while accessing target URL.


        :param is_redirection_enabled: The is_redirection_enabled of this RestMonitorConfiguration.
        :type: bool
        """
        self._is_redirection_enabled = is_redirection_enabled

    @property
    def is_certificate_validation_enabled(self):
        """
        Gets the is_certificate_validation_enabled of this RestMonitorConfiguration.
        If certificate validation enabled, then call will fail for certificate errors.


        :return: The is_certificate_validation_enabled of this RestMonitorConfiguration.
        :rtype: bool
        """
        return self._is_certificate_validation_enabled

    @is_certificate_validation_enabled.setter
    def is_certificate_validation_enabled(self, is_certificate_validation_enabled):
        """
        Sets the is_certificate_validation_enabled of this RestMonitorConfiguration.
        If certificate validation enabled, then call will fail for certificate errors.


        :param is_certificate_validation_enabled: The is_certificate_validation_enabled of this RestMonitorConfiguration.
        :type: bool
        """
        self._is_certificate_validation_enabled = is_certificate_validation_enabled

    @property
    def request_method(self):
        """
        Gets the request_method of this RestMonitorConfiguration.
        Request HTTP method.

        Allowed values for this property are: "GET", "POST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The request_method of this RestMonitorConfiguration.
        :rtype: str
        """
        return self._request_method

    @request_method.setter
    def request_method(self, request_method):
        """
        Sets the request_method of this RestMonitorConfiguration.
        Request HTTP method.


        :param request_method: The request_method of this RestMonitorConfiguration.
        :type: str
        """
        allowed_values = ["GET", "POST"]
        if not value_allowed_none_or_none_sentinel(request_method, allowed_values):
            request_method = 'UNKNOWN_ENUM_VALUE'
        self._request_method = request_method

    @property
    def req_authentication_scheme(self):
        """
        Gets the req_authentication_scheme of this RestMonitorConfiguration.
        Request http authentication scheme.

        Allowed values for this property are: "OAUTH", "NONE", "BASIC", "BEARER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The req_authentication_scheme of this RestMonitorConfiguration.
        :rtype: str
        """
        return self._req_authentication_scheme

    @req_authentication_scheme.setter
    def req_authentication_scheme(self, req_authentication_scheme):
        """
        Sets the req_authentication_scheme of this RestMonitorConfiguration.
        Request http authentication scheme.


        :param req_authentication_scheme: The req_authentication_scheme of this RestMonitorConfiguration.
        :type: str
        """
        allowed_values = ["OAUTH", "NONE", "BASIC", "BEARER"]
        if not value_allowed_none_or_none_sentinel(req_authentication_scheme, allowed_values):
            req_authentication_scheme = 'UNKNOWN_ENUM_VALUE'
        self._req_authentication_scheme = req_authentication_scheme

    @property
    def req_authentication_details(self):
        """
        Gets the req_authentication_details of this RestMonitorConfiguration.

        :return: The req_authentication_details of this RestMonitorConfiguration.
        :rtype: oci.apm_synthetics.models.RequestAuthenticationDetails
        """
        return self._req_authentication_details

    @req_authentication_details.setter
    def req_authentication_details(self, req_authentication_details):
        """
        Sets the req_authentication_details of this RestMonitorConfiguration.

        :param req_authentication_details: The req_authentication_details of this RestMonitorConfiguration.
        :type: oci.apm_synthetics.models.RequestAuthenticationDetails
        """
        self._req_authentication_details = req_authentication_details

    @property
    def request_headers(self):
        """
        Gets the request_headers of this RestMonitorConfiguration.
        List of request headers. Example: `[{\"headerName\": \"content-type\", \"headerValue\":\"json\"}]`


        :return: The request_headers of this RestMonitorConfiguration.
        :rtype: list[oci.apm_synthetics.models.Header]
        """
        return self._request_headers

    @request_headers.setter
    def request_headers(self, request_headers):
        """
        Sets the request_headers of this RestMonitorConfiguration.
        List of request headers. Example: `[{\"headerName\": \"content-type\", \"headerValue\":\"json\"}]`


        :param request_headers: The request_headers of this RestMonitorConfiguration.
        :type: list[oci.apm_synthetics.models.Header]
        """
        self._request_headers = request_headers

    @property
    def request_query_params(self):
        """
        Gets the request_query_params of this RestMonitorConfiguration.
        List of request query params. Example: `[{\"paramName\": \"sortOrder\", \"paramValue\": \"asc\"}]`


        :return: The request_query_params of this RestMonitorConfiguration.
        :rtype: list[oci.apm_synthetics.models.RequestQueryParam]
        """
        return self._request_query_params

    @request_query_params.setter
    def request_query_params(self, request_query_params):
        """
        Sets the request_query_params of this RestMonitorConfiguration.
        List of request query params. Example: `[{\"paramName\": \"sortOrder\", \"paramValue\": \"asc\"}]`


        :param request_query_params: The request_query_params of this RestMonitorConfiguration.
        :type: list[oci.apm_synthetics.models.RequestQueryParam]
        """
        self._request_query_params = request_query_params

    @property
    def request_post_body(self):
        """
        Gets the request_post_body of this RestMonitorConfiguration.
        Request post body content.


        :return: The request_post_body of this RestMonitorConfiguration.
        :rtype: str
        """
        return self._request_post_body

    @request_post_body.setter
    def request_post_body(self, request_post_body):
        """
        Sets the request_post_body of this RestMonitorConfiguration.
        Request post body content.


        :param request_post_body: The request_post_body of this RestMonitorConfiguration.
        :type: str
        """
        self._request_post_body = request_post_body

    @property
    def verify_response_content(self):
        """
        Gets the verify_response_content of this RestMonitorConfiguration.
        Verify response content against regular expression based string.
        If response content does not match the verifyResponseContent value, then it will be considered a failure.


        :return: The verify_response_content of this RestMonitorConfiguration.
        :rtype: str
        """
        return self._verify_response_content

    @verify_response_content.setter
    def verify_response_content(self, verify_response_content):
        """
        Sets the verify_response_content of this RestMonitorConfiguration.
        Verify response content against regular expression based string.
        If response content does not match the verifyResponseContent value, then it will be considered a failure.


        :param verify_response_content: The verify_response_content of this RestMonitorConfiguration.
        :type: str
        """
        self._verify_response_content = verify_response_content

    @property
    def verify_response_codes(self):
        """
        Gets the verify_response_codes of this RestMonitorConfiguration.
        Expected HTTP response codes. For status code range, set values such as 2xx, 3xx.


        :return: The verify_response_codes of this RestMonitorConfiguration.
        :rtype: list[str]
        """
        return self._verify_response_codes

    @verify_response_codes.setter
    def verify_response_codes(self, verify_response_codes):
        """
        Sets the verify_response_codes of this RestMonitorConfiguration.
        Expected HTTP response codes. For status code range, set values such as 2xx, 3xx.


        :param verify_response_codes: The verify_response_codes of this RestMonitorConfiguration.
        :type: list[str]
        """
        self._verify_response_codes = verify_response_codes

    @property
    def network_configuration(self):
        """
        Gets the network_configuration of this RestMonitorConfiguration.

        :return: The network_configuration of this RestMonitorConfiguration.
        :rtype: oci.apm_synthetics.models.NetworkConfiguration
        """
        return self._network_configuration

    @network_configuration.setter
    def network_configuration(self, network_configuration):
        """
        Sets the network_configuration of this RestMonitorConfiguration.

        :param network_configuration: The network_configuration of this RestMonitorConfiguration.
        :type: oci.apm_synthetics.models.NetworkConfiguration
        """
        self._network_configuration = network_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
