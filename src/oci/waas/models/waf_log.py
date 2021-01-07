# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WafLog(object):
    """
    A list of Web Application Firewall log entries. Each entry is a JSON object, including a timestamp property and other fields varying based on log type. Logs record what rules and countermeasures are triggered by requests and are used as a basis to move request handling into block mode. For more information about WAF logs, see `Logs`__.

    __ https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/logs.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WafLog object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this WafLog.
        :type action: str

        :param captcha_action:
            The value to assign to the captcha_action property of this WafLog.
        :type captcha_action: str

        :param captcha_expected:
            The value to assign to the captcha_expected property of this WafLog.
        :type captcha_expected: str

        :param captcha_received:
            The value to assign to the captcha_received property of this WafLog.
        :type captcha_received: str

        :param captcha_fail_count:
            The value to assign to the captcha_fail_count property of this WafLog.
        :type captcha_fail_count: str

        :param client_address:
            The value to assign to the client_address property of this WafLog.
        :type client_address: str

        :param country_name:
            The value to assign to the country_name property of this WafLog.
        :type country_name: str

        :param user_agent:
            The value to assign to the user_agent property of this WafLog.
        :type user_agent: str

        :param domain:
            The value to assign to the domain property of this WafLog.
        :type domain: str

        :param protection_rule_detections:
            The value to assign to the protection_rule_detections property of this WafLog.
        :type protection_rule_detections: dict(str, str)

        :param http_method:
            The value to assign to the http_method property of this WafLog.
        :type http_method: str

        :param request_url:
            The value to assign to the request_url property of this WafLog.
        :type request_url: str

        :param http_headers:
            The value to assign to the http_headers property of this WafLog.
        :type http_headers: dict(str, str)

        :param referrer:
            The value to assign to the referrer property of this WafLog.
        :type referrer: str

        :param response_code:
            The value to assign to the response_code property of this WafLog.
        :type response_code: int

        :param response_size:
            The value to assign to the response_size property of this WafLog.
        :type response_size: int

        :param incident_key:
            The value to assign to the incident_key property of this WafLog.
        :type incident_key: str

        :param fingerprint:
            The value to assign to the fingerprint property of this WafLog.
        :type fingerprint: str

        :param device:
            The value to assign to the device property of this WafLog.
        :type device: str

        :param country_code:
            The value to assign to the country_code property of this WafLog.
        :type country_code: str

        :param request_headers:
            The value to assign to the request_headers property of this WafLog.
        :type request_headers: dict(str, str)

        :param threat_feed_key:
            The value to assign to the threat_feed_key property of this WafLog.
        :type threat_feed_key: str

        :param access_rule_key:
            The value to assign to the access_rule_key property of this WafLog.
        :type access_rule_key: str

        :param address_rate_limiting_key:
            The value to assign to the address_rate_limiting_key property of this WafLog.
        :type address_rate_limiting_key: str

        :param timestamp:
            The value to assign to the timestamp property of this WafLog.
        :type timestamp: datetime

        :param log_type:
            The value to assign to the log_type property of this WafLog.
        :type log_type: str

        :param origin_address:
            The value to assign to the origin_address property of this WafLog.
        :type origin_address: str

        :param origin_response_time:
            The value to assign to the origin_response_time property of this WafLog.
        :type origin_response_time: str

        """
        self.swagger_types = {
            'action': 'str',
            'captcha_action': 'str',
            'captcha_expected': 'str',
            'captcha_received': 'str',
            'captcha_fail_count': 'str',
            'client_address': 'str',
            'country_name': 'str',
            'user_agent': 'str',
            'domain': 'str',
            'protection_rule_detections': 'dict(str, str)',
            'http_method': 'str',
            'request_url': 'str',
            'http_headers': 'dict(str, str)',
            'referrer': 'str',
            'response_code': 'int',
            'response_size': 'int',
            'incident_key': 'str',
            'fingerprint': 'str',
            'device': 'str',
            'country_code': 'str',
            'request_headers': 'dict(str, str)',
            'threat_feed_key': 'str',
            'access_rule_key': 'str',
            'address_rate_limiting_key': 'str',
            'timestamp': 'datetime',
            'log_type': 'str',
            'origin_address': 'str',
            'origin_response_time': 'str'
        }

        self.attribute_map = {
            'action': 'action',
            'captcha_action': 'captchaAction',
            'captcha_expected': 'captchaExpected',
            'captcha_received': 'captchaReceived',
            'captcha_fail_count': 'captchaFailCount',
            'client_address': 'clientAddress',
            'country_name': 'countryName',
            'user_agent': 'userAgent',
            'domain': 'domain',
            'protection_rule_detections': 'protectionRuleDetections',
            'http_method': 'httpMethod',
            'request_url': 'requestUrl',
            'http_headers': 'httpHeaders',
            'referrer': 'referrer',
            'response_code': 'responseCode',
            'response_size': 'responseSize',
            'incident_key': 'incidentKey',
            'fingerprint': 'fingerprint',
            'device': 'device',
            'country_code': 'countryCode',
            'request_headers': 'requestHeaders',
            'threat_feed_key': 'threatFeedKey',
            'access_rule_key': 'accessRuleKey',
            'address_rate_limiting_key': 'addressRateLimitingKey',
            'timestamp': 'timestamp',
            'log_type': 'logType',
            'origin_address': 'originAddress',
            'origin_response_time': 'originResponseTime'
        }

        self._action = None
        self._captcha_action = None
        self._captcha_expected = None
        self._captcha_received = None
        self._captcha_fail_count = None
        self._client_address = None
        self._country_name = None
        self._user_agent = None
        self._domain = None
        self._protection_rule_detections = None
        self._http_method = None
        self._request_url = None
        self._http_headers = None
        self._referrer = None
        self._response_code = None
        self._response_size = None
        self._incident_key = None
        self._fingerprint = None
        self._device = None
        self._country_code = None
        self._request_headers = None
        self._threat_feed_key = None
        self._access_rule_key = None
        self._address_rate_limiting_key = None
        self._timestamp = None
        self._log_type = None
        self._origin_address = None
        self._origin_response_time = None

    @property
    def action(self):
        """
        Gets the action of this WafLog.
        The action taken on the request, either `ALLOW`, `DETECT`, or `BLOCK`.


        :return: The action of this WafLog.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this WafLog.
        The action taken on the request, either `ALLOW`, `DETECT`, or `BLOCK`.


        :param action: The action of this WafLog.
        :type: str
        """
        self._action = action

    @property
    def captcha_action(self):
        """
        Gets the captcha_action of this WafLog.
        The CAPTCHA action taken on the request, `ALLOW` or `BLOCK`. For more information about
        CAPTCHAs, see `UpdateCaptchas`.


        :return: The captcha_action of this WafLog.
        :rtype: str
        """
        return self._captcha_action

    @captcha_action.setter
    def captcha_action(self, captcha_action):
        """
        Sets the captcha_action of this WafLog.
        The CAPTCHA action taken on the request, `ALLOW` or `BLOCK`. For more information about
        CAPTCHAs, see `UpdateCaptchas`.


        :param captcha_action: The captcha_action of this WafLog.
        :type: str
        """
        self._captcha_action = captcha_action

    @property
    def captcha_expected(self):
        """
        Gets the captcha_expected of this WafLog.
        The CAPTCHA challenge answer that was expected.


        :return: The captcha_expected of this WafLog.
        :rtype: str
        """
        return self._captcha_expected

    @captcha_expected.setter
    def captcha_expected(self, captcha_expected):
        """
        Sets the captcha_expected of this WafLog.
        The CAPTCHA challenge answer that was expected.


        :param captcha_expected: The captcha_expected of this WafLog.
        :type: str
        """
        self._captcha_expected = captcha_expected

    @property
    def captcha_received(self):
        """
        Gets the captcha_received of this WafLog.
        The CAPTCHA challenge answer that was received.


        :return: The captcha_received of this WafLog.
        :rtype: str
        """
        return self._captcha_received

    @captcha_received.setter
    def captcha_received(self, captcha_received):
        """
        Sets the captcha_received of this WafLog.
        The CAPTCHA challenge answer that was received.


        :param captcha_received: The captcha_received of this WafLog.
        :type: str
        """
        self._captcha_received = captcha_received

    @property
    def captcha_fail_count(self):
        """
        Gets the captcha_fail_count of this WafLog.
        The number of times the CAPTCHA challenge was failed.


        :return: The captcha_fail_count of this WafLog.
        :rtype: str
        """
        return self._captcha_fail_count

    @captcha_fail_count.setter
    def captcha_fail_count(self, captcha_fail_count):
        """
        Sets the captcha_fail_count of this WafLog.
        The number of times the CAPTCHA challenge was failed.


        :param captcha_fail_count: The captcha_fail_count of this WafLog.
        :type: str
        """
        self._captcha_fail_count = captcha_fail_count

    @property
    def client_address(self):
        """
        Gets the client_address of this WafLog.
        The IPv4 address of the requesting client.


        :return: The client_address of this WafLog.
        :rtype: str
        """
        return self._client_address

    @client_address.setter
    def client_address(self, client_address):
        """
        Sets the client_address of this WafLog.
        The IPv4 address of the requesting client.


        :param client_address: The client_address of this WafLog.
        :type: str
        """
        self._client_address = client_address

    @property
    def country_name(self):
        """
        Gets the country_name of this WafLog.
        The name of the country where the request originated.


        :return: The country_name of this WafLog.
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """
        Sets the country_name of this WafLog.
        The name of the country where the request originated.


        :param country_name: The country_name of this WafLog.
        :type: str
        """
        self._country_name = country_name

    @property
    def user_agent(self):
        """
        Gets the user_agent of this WafLog.
        The value of the request's `User-Agent` header field.


        :return: The user_agent of this WafLog.
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """
        Sets the user_agent of this WafLog.
        The value of the request's `User-Agent` header field.


        :param user_agent: The user_agent of this WafLog.
        :type: str
        """
        self._user_agent = user_agent

    @property
    def domain(self):
        """
        Gets the domain of this WafLog.
        The `Host` header data of the request.


        :return: The domain of this WafLog.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this WafLog.
        The `Host` header data of the request.


        :param domain: The domain of this WafLog.
        :type: str
        """
        self._domain = domain

    @property
    def protection_rule_detections(self):
        """
        Gets the protection_rule_detections of this WafLog.
        A map of protection rule keys to detection message details. Detections are
        requests that matched the criteria of a protection rule but the rule's
        action was set to `DETECT`.


        :return: The protection_rule_detections of this WafLog.
        :rtype: dict(str, str)
        """
        return self._protection_rule_detections

    @protection_rule_detections.setter
    def protection_rule_detections(self, protection_rule_detections):
        """
        Sets the protection_rule_detections of this WafLog.
        A map of protection rule keys to detection message details. Detections are
        requests that matched the criteria of a protection rule but the rule's
        action was set to `DETECT`.


        :param protection_rule_detections: The protection_rule_detections of this WafLog.
        :type: dict(str, str)
        """
        self._protection_rule_detections = protection_rule_detections

    @property
    def http_method(self):
        """
        Gets the http_method of this WafLog.
        The HTTP method of the request.


        :return: The http_method of this WafLog.
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """
        Sets the http_method of this WafLog.
        The HTTP method of the request.


        :param http_method: The http_method of this WafLog.
        :type: str
        """
        self._http_method = http_method

    @property
    def request_url(self):
        """
        Gets the request_url of this WafLog.
        The path and query string of the request.


        :return: The request_url of this WafLog.
        :rtype: str
        """
        return self._request_url

    @request_url.setter
    def request_url(self, request_url):
        """
        Sets the request_url of this WafLog.
        The path and query string of the request.


        :param request_url: The request_url of this WafLog.
        :type: str
        """
        self._request_url = request_url

    @property
    def http_headers(self):
        """
        Gets the http_headers of this WafLog.
        The map of the request's header names to their respective values.


        :return: The http_headers of this WafLog.
        :rtype: dict(str, str)
        """
        return self._http_headers

    @http_headers.setter
    def http_headers(self, http_headers):
        """
        Sets the http_headers of this WafLog.
        The map of the request's header names to their respective values.


        :param http_headers: The http_headers of this WafLog.
        :type: dict(str, str)
        """
        self._http_headers = http_headers

    @property
    def referrer(self):
        """
        Gets the referrer of this WafLog.
        The `Referrer` header value of the request.


        :return: The referrer of this WafLog.
        :rtype: str
        """
        return self._referrer

    @referrer.setter
    def referrer(self, referrer):
        """
        Sets the referrer of this WafLog.
        The `Referrer` header value of the request.


        :param referrer: The referrer of this WafLog.
        :type: str
        """
        self._referrer = referrer

    @property
    def response_code(self):
        """
        Gets the response_code of this WafLog.
        The status code of the response.


        :return: The response_code of this WafLog.
        :rtype: int
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this WafLog.
        The status code of the response.


        :param response_code: The response_code of this WafLog.
        :type: int
        """
        self._response_code = response_code

    @property
    def response_size(self):
        """
        Gets the response_size of this WafLog.
        The size in bytes of the response.


        :return: The response_size of this WafLog.
        :rtype: int
        """
        return self._response_size

    @response_size.setter
    def response_size(self, response_size):
        """
        Sets the response_size of this WafLog.
        The size in bytes of the response.


        :param response_size: The response_size of this WafLog.
        :type: int
        """
        self._response_size = response_size

    @property
    def incident_key(self):
        """
        Gets the incident_key of this WafLog.
        The incident key of a request. An incident key is generated for
        each request processed by the Web Application Firewall and is used to
        idenitfy blocked requests in applicable logs.


        :return: The incident_key of this WafLog.
        :rtype: str
        """
        return self._incident_key

    @incident_key.setter
    def incident_key(self, incident_key):
        """
        Sets the incident_key of this WafLog.
        The incident key of a request. An incident key is generated for
        each request processed by the Web Application Firewall and is used to
        idenitfy blocked requests in applicable logs.


        :param incident_key: The incident_key of this WafLog.
        :type: str
        """
        self._incident_key = incident_key

    @property
    def fingerprint(self):
        """
        Gets the fingerprint of this WafLog.
        The hashed signature of the device's fingerprint. For more information,
        see `DeviceFingerPrintChallenge`.


        :return: The fingerprint of this WafLog.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """
        Sets the fingerprint of this WafLog.
        The hashed signature of the device's fingerprint. For more information,
        see `DeviceFingerPrintChallenge`.


        :param fingerprint: The fingerprint of this WafLog.
        :type: str
        """
        self._fingerprint = fingerprint

    @property
    def device(self):
        """
        Gets the device of this WafLog.
        The type of device that the request was made from.


        :return: The device of this WafLog.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this WafLog.
        The type of device that the request was made from.


        :param device: The device of this WafLog.
        :type: str
        """
        self._device = device

    @property
    def country_code(self):
        """
        Gets the country_code of this WafLog.
        ISO 3166-1 alpha-2 code of the country from which the request originated.
        For a list of codes, see `ISO's website`__.

        __ https://www.iso.org/obp/ui/#search/code/


        :return: The country_code of this WafLog.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this WafLog.
        ISO 3166-1 alpha-2 code of the country from which the request originated.
        For a list of codes, see `ISO's website`__.

        __ https://www.iso.org/obp/ui/#search/code/


        :param country_code: The country_code of this WafLog.
        :type: str
        """
        self._country_code = country_code

    @property
    def request_headers(self):
        """
        Gets the request_headers of this WafLog.
        A map of header names to values of the request sent to the origin, including any headers
        appended by the Web Application Firewall.


        :return: The request_headers of this WafLog.
        :rtype: dict(str, str)
        """
        return self._request_headers

    @request_headers.setter
    def request_headers(self, request_headers):
        """
        Sets the request_headers of this WafLog.
        A map of header names to values of the request sent to the origin, including any headers
        appended by the Web Application Firewall.


        :param request_headers: The request_headers of this WafLog.
        :type: dict(str, str)
        """
        self._request_headers = request_headers

    @property
    def threat_feed_key(self):
        """
        Gets the threat_feed_key of this WafLog.
        The `ThreatFeed` key that matched the request. For more information about
        threat feeds, see `UpdateThreatFeeds`.


        :return: The threat_feed_key of this WafLog.
        :rtype: str
        """
        return self._threat_feed_key

    @threat_feed_key.setter
    def threat_feed_key(self, threat_feed_key):
        """
        Sets the threat_feed_key of this WafLog.
        The `ThreatFeed` key that matched the request. For more information about
        threat feeds, see `UpdateThreatFeeds`.


        :param threat_feed_key: The threat_feed_key of this WafLog.
        :type: str
        """
        self._threat_feed_key = threat_feed_key

    @property
    def access_rule_key(self):
        """
        Gets the access_rule_key of this WafLog.
        The `AccessRule` key that matched the request. For more information about
        access rules, see `UpdateAccessRules`.


        :return: The access_rule_key of this WafLog.
        :rtype: str
        """
        return self._access_rule_key

    @access_rule_key.setter
    def access_rule_key(self, access_rule_key):
        """
        Sets the access_rule_key of this WafLog.
        The `AccessRule` key that matched the request. For more information about
        access rules, see `UpdateAccessRules`.


        :param access_rule_key: The access_rule_key of this WafLog.
        :type: str
        """
        self._access_rule_key = access_rule_key

    @property
    def address_rate_limiting_key(self):
        """
        Gets the address_rate_limiting_key of this WafLog.
        The `AddressRateLimiting` key that matched the request. For more information
        about address rate limiting, see `UpdateWafAddressRateLimiting`.


        :return: The address_rate_limiting_key of this WafLog.
        :rtype: str
        """
        return self._address_rate_limiting_key

    @address_rate_limiting_key.setter
    def address_rate_limiting_key(self, address_rate_limiting_key):
        """
        Sets the address_rate_limiting_key of this WafLog.
        The `AddressRateLimiting` key that matched the request. For more information
        about address rate limiting, see `UpdateWafAddressRateLimiting`.


        :param address_rate_limiting_key: The address_rate_limiting_key of this WafLog.
        :type: str
        """
        self._address_rate_limiting_key = address_rate_limiting_key

    @property
    def timestamp(self):
        """
        Gets the timestamp of this WafLog.
        The date and time the Web Application Firewall processed the request and logged it.


        :return: The timestamp of this WafLog.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this WafLog.
        The date and time the Web Application Firewall processed the request and logged it.


        :param timestamp: The timestamp of this WafLog.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def log_type(self):
        """
        Gets the log_type of this WafLog.
        The type of log of the request. For more about log types, see `Logs`__.

        __ https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/logs.htm


        :return: The log_type of this WafLog.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        """
        Sets the log_type of this WafLog.
        The type of log of the request. For more about log types, see `Logs`__.

        __ https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/logs.htm


        :param log_type: The log_type of this WafLog.
        :type: str
        """
        self._log_type = log_type

    @property
    def origin_address(self):
        """
        Gets the origin_address of this WafLog.
        The address of the origin server where the request was sent.


        :return: The origin_address of this WafLog.
        :rtype: str
        """
        return self._origin_address

    @origin_address.setter
    def origin_address(self, origin_address):
        """
        Sets the origin_address of this WafLog.
        The address of the origin server where the request was sent.


        :param origin_address: The origin_address of this WafLog.
        :type: str
        """
        self._origin_address = origin_address

    @property
    def origin_response_time(self):
        """
        Gets the origin_response_time of this WafLog.
        The amount of time it took the origin server to respond to the request, in seconds.


        :return: The origin_response_time of this WafLog.
        :rtype: str
        """
        return self._origin_response_time

    @origin_response_time.setter
    def origin_response_time(self, origin_response_time):
        """
        Sets the origin_response_time of this WafLog.
        The amount of time it took the origin server to respond to the request, in seconds.


        :param origin_response_time: The origin_response_time of this WafLog.
        :type: str
        """
        self._origin_response_time = origin_response_time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
