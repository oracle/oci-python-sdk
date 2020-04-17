# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WafBlockedRequest(object):
    """
    WafBlockedRequest model.
    """

    #: A constant which can be used with the waf_feature property of a WafBlockedRequest.
    #: This constant has a value of "PROTECTION_RULES"
    WAF_FEATURE_PROTECTION_RULES = "PROTECTION_RULES"

    #: A constant which can be used with the waf_feature property of a WafBlockedRequest.
    #: This constant has a value of "JS_CHALLENGE"
    WAF_FEATURE_JS_CHALLENGE = "JS_CHALLENGE"

    #: A constant which can be used with the waf_feature property of a WafBlockedRequest.
    #: This constant has a value of "ACCESS_RULES"
    WAF_FEATURE_ACCESS_RULES = "ACCESS_RULES"

    #: A constant which can be used with the waf_feature property of a WafBlockedRequest.
    #: This constant has a value of "THREAT_FEEDS"
    WAF_FEATURE_THREAT_FEEDS = "THREAT_FEEDS"

    #: A constant which can be used with the waf_feature property of a WafBlockedRequest.
    #: This constant has a value of "HUMAN_INTERACTION_CHALLENGE"
    WAF_FEATURE_HUMAN_INTERACTION_CHALLENGE = "HUMAN_INTERACTION_CHALLENGE"

    #: A constant which can be used with the waf_feature property of a WafBlockedRequest.
    #: This constant has a value of "DEVICE_FINGERPRINT_CHALLENGE"
    WAF_FEATURE_DEVICE_FINGERPRINT_CHALLENGE = "DEVICE_FINGERPRINT_CHALLENGE"

    #: A constant which can be used with the waf_feature property of a WafBlockedRequest.
    #: This constant has a value of "CAPTCHA"
    WAF_FEATURE_CAPTCHA = "CAPTCHA"

    #: A constant which can be used with the waf_feature property of a WafBlockedRequest.
    #: This constant has a value of "ADDRESS_RATE_LIMITING"
    WAF_FEATURE_ADDRESS_RATE_LIMITING = "ADDRESS_RATE_LIMITING"

    def __init__(self, **kwargs):
        """
        Initializes a new WafBlockedRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_observed:
            The value to assign to the time_observed property of this WafBlockedRequest.
        :type time_observed: datetime

        :param time_range_in_seconds:
            The value to assign to the time_range_in_seconds property of this WafBlockedRequest.
        :type time_range_in_seconds: int

        :param waf_feature:
            The value to assign to the waf_feature property of this WafBlockedRequest.
            Allowed values for this property are: "PROTECTION_RULES", "JS_CHALLENGE", "ACCESS_RULES", "THREAT_FEEDS", "HUMAN_INTERACTION_CHALLENGE", "DEVICE_FINGERPRINT_CHALLENGE", "CAPTCHA", "ADDRESS_RATE_LIMITING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type waf_feature: str

        :param count:
            The value to assign to the count property of this WafBlockedRequest.
        :type count: int

        """
        self.swagger_types = {
            'time_observed': 'datetime',
            'time_range_in_seconds': 'int',
            'waf_feature': 'str',
            'count': 'int'
        }

        self.attribute_map = {
            'time_observed': 'timeObserved',
            'time_range_in_seconds': 'timeRangeInSeconds',
            'waf_feature': 'wafFeature',
            'count': 'count'
        }

        self._time_observed = None
        self._time_range_in_seconds = None
        self._waf_feature = None
        self._count = None

    @property
    def time_observed(self):
        """
        Gets the time_observed of this WafBlockedRequest.
        The date and time the blocked requests were observed, expressed in RFC 3339 timestamp format.


        :return: The time_observed of this WafBlockedRequest.
        :rtype: datetime
        """
        return self._time_observed

    @time_observed.setter
    def time_observed(self, time_observed):
        """
        Sets the time_observed of this WafBlockedRequest.
        The date and time the blocked requests were observed, expressed in RFC 3339 timestamp format.


        :param time_observed: The time_observed of this WafBlockedRequest.
        :type: datetime
        """
        self._time_observed = time_observed

    @property
    def time_range_in_seconds(self):
        """
        Gets the time_range_in_seconds of this WafBlockedRequest.
        The number of seconds the data covers.


        :return: The time_range_in_seconds of this WafBlockedRequest.
        :rtype: int
        """
        return self._time_range_in_seconds

    @time_range_in_seconds.setter
    def time_range_in_seconds(self, time_range_in_seconds):
        """
        Sets the time_range_in_seconds of this WafBlockedRequest.
        The number of seconds the data covers.


        :param time_range_in_seconds: The time_range_in_seconds of this WafBlockedRequest.
        :type: int
        """
        self._time_range_in_seconds = time_range_in_seconds

    @property
    def waf_feature(self):
        """
        Gets the waf_feature of this WafBlockedRequest.
        The specific Web Application Firewall feature that blocked the requests, such as JavaScript Challenge or Access Control.

        Allowed values for this property are: "PROTECTION_RULES", "JS_CHALLENGE", "ACCESS_RULES", "THREAT_FEEDS", "HUMAN_INTERACTION_CHALLENGE", "DEVICE_FINGERPRINT_CHALLENGE", "CAPTCHA", "ADDRESS_RATE_LIMITING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The waf_feature of this WafBlockedRequest.
        :rtype: str
        """
        return self._waf_feature

    @waf_feature.setter
    def waf_feature(self, waf_feature):
        """
        Sets the waf_feature of this WafBlockedRequest.
        The specific Web Application Firewall feature that blocked the requests, such as JavaScript Challenge or Access Control.


        :param waf_feature: The waf_feature of this WafBlockedRequest.
        :type: str
        """
        allowed_values = ["PROTECTION_RULES", "JS_CHALLENGE", "ACCESS_RULES", "THREAT_FEEDS", "HUMAN_INTERACTION_CHALLENGE", "DEVICE_FINGERPRINT_CHALLENGE", "CAPTCHA", "ADDRESS_RATE_LIMITING"]
        if not value_allowed_none_or_none_sentinel(waf_feature, allowed_values):
            waf_feature = 'UNKNOWN_ENUM_VALUE'
        self._waf_feature = waf_feature

    @property
    def count(self):
        """
        Gets the count of this WafBlockedRequest.
        The count of blocked requests.


        :return: The count of this WafBlockedRequest.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this WafBlockedRequest.
        The count of blocked requests.


        :param count: The count of this WafBlockedRequest.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
