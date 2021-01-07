# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JsChallenge(object):
    """
    The JavaScript challenge settings. JavaScript Challenge is the function to filter abnormal or malicious bots and allow access to real clients.
    """

    #: A constant which can be used with the action property of a JsChallenge.
    #: This constant has a value of "DETECT"
    ACTION_DETECT = "DETECT"

    #: A constant which can be used with the action property of a JsChallenge.
    #: This constant has a value of "BLOCK"
    ACTION_BLOCK = "BLOCK"

    def __init__(self, **kwargs):
        """
        Initializes a new JsChallenge object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this JsChallenge.
        :type is_enabled: bool

        :param action:
            The value to assign to the action property of this JsChallenge.
            Allowed values for this property are: "DETECT", "BLOCK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param failure_threshold:
            The value to assign to the failure_threshold property of this JsChallenge.
        :type failure_threshold: int

        :param action_expiration_in_seconds:
            The value to assign to the action_expiration_in_seconds property of this JsChallenge.
        :type action_expiration_in_seconds: int

        :param set_http_header:
            The value to assign to the set_http_header property of this JsChallenge.
        :type set_http_header: oci.waas.models.Header

        :param challenge_settings:
            The value to assign to the challenge_settings property of this JsChallenge.
        :type challenge_settings: oci.waas.models.BlockChallengeSettings

        :param are_redirects_challenged:
            The value to assign to the are_redirects_challenged property of this JsChallenge.
        :type are_redirects_challenged: bool

        :param criteria:
            The value to assign to the criteria property of this JsChallenge.
        :type criteria: list[oci.waas.models.AccessRuleCriteria]

        :param is_nat_enabled:
            The value to assign to the is_nat_enabled property of this JsChallenge.
        :type is_nat_enabled: bool

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'action': 'str',
            'failure_threshold': 'int',
            'action_expiration_in_seconds': 'int',
            'set_http_header': 'Header',
            'challenge_settings': 'BlockChallengeSettings',
            'are_redirects_challenged': 'bool',
            'criteria': 'list[AccessRuleCriteria]',
            'is_nat_enabled': 'bool'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'action': 'action',
            'failure_threshold': 'failureThreshold',
            'action_expiration_in_seconds': 'actionExpirationInSeconds',
            'set_http_header': 'setHttpHeader',
            'challenge_settings': 'challengeSettings',
            'are_redirects_challenged': 'areRedirectsChallenged',
            'criteria': 'criteria',
            'is_nat_enabled': 'isNatEnabled'
        }

        self._is_enabled = None
        self._action = None
        self._failure_threshold = None
        self._action_expiration_in_seconds = None
        self._set_http_header = None
        self._challenge_settings = None
        self._are_redirects_challenged = None
        self._criteria = None
        self._is_nat_enabled = None

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this JsChallenge.
        Enables or disables the JavaScript challenge Web Application Firewall feature.


        :return: The is_enabled of this JsChallenge.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this JsChallenge.
        Enables or disables the JavaScript challenge Web Application Firewall feature.


        :param is_enabled: The is_enabled of this JsChallenge.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def action(self):
        """
        Gets the action of this JsChallenge.
        The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.

        Allowed values for this property are: "DETECT", "BLOCK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this JsChallenge.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this JsChallenge.
        The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.


        :param action: The action of this JsChallenge.
        :type: str
        """
        allowed_values = ["DETECT", "BLOCK"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def failure_threshold(self):
        """
        Gets the failure_threshold of this JsChallenge.
        The number of failed requests before taking action. If unspecified, defaults to `10`.


        :return: The failure_threshold of this JsChallenge.
        :rtype: int
        """
        return self._failure_threshold

    @failure_threshold.setter
    def failure_threshold(self, failure_threshold):
        """
        Sets the failure_threshold of this JsChallenge.
        The number of failed requests before taking action. If unspecified, defaults to `10`.


        :param failure_threshold: The failure_threshold of this JsChallenge.
        :type: int
        """
        self._failure_threshold = failure_threshold

    @property
    def action_expiration_in_seconds(self):
        """
        Gets the action_expiration_in_seconds of this JsChallenge.
        The number of seconds between challenges from the same IP address. If unspecified, defaults to `60`.


        :return: The action_expiration_in_seconds of this JsChallenge.
        :rtype: int
        """
        return self._action_expiration_in_seconds

    @action_expiration_in_seconds.setter
    def action_expiration_in_seconds(self, action_expiration_in_seconds):
        """
        Sets the action_expiration_in_seconds of this JsChallenge.
        The number of seconds between challenges from the same IP address. If unspecified, defaults to `60`.


        :param action_expiration_in_seconds: The action_expiration_in_seconds of this JsChallenge.
        :type: int
        """
        self._action_expiration_in_seconds = action_expiration_in_seconds

    @property
    def set_http_header(self):
        """
        Gets the set_http_header of this JsChallenge.
        Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the `action` is set to `DETECT`.


        :return: The set_http_header of this JsChallenge.
        :rtype: oci.waas.models.Header
        """
        return self._set_http_header

    @set_http_header.setter
    def set_http_header(self, set_http_header):
        """
        Sets the set_http_header of this JsChallenge.
        Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the `action` is set to `DETECT`.


        :param set_http_header: The set_http_header of this JsChallenge.
        :type: oci.waas.models.Header
        """
        self._set_http_header = set_http_header

    @property
    def challenge_settings(self):
        """
        Gets the challenge_settings of this JsChallenge.

        :return: The challenge_settings of this JsChallenge.
        :rtype: oci.waas.models.BlockChallengeSettings
        """
        return self._challenge_settings

    @challenge_settings.setter
    def challenge_settings(self, challenge_settings):
        """
        Sets the challenge_settings of this JsChallenge.

        :param challenge_settings: The challenge_settings of this JsChallenge.
        :type: oci.waas.models.BlockChallengeSettings
        """
        self._challenge_settings = challenge_settings

    @property
    def are_redirects_challenged(self):
        """
        Gets the are_redirects_challenged of this JsChallenge.
        When enabled, redirect responses from the origin will also be challenged. This will change HTTP 301/302 responses from origin to HTTP 200 with an HTML body containing JavaScript page redirection.


        :return: The are_redirects_challenged of this JsChallenge.
        :rtype: bool
        """
        return self._are_redirects_challenged

    @are_redirects_challenged.setter
    def are_redirects_challenged(self, are_redirects_challenged):
        """
        Sets the are_redirects_challenged of this JsChallenge.
        When enabled, redirect responses from the origin will also be challenged. This will change HTTP 301/302 responses from origin to HTTP 200 with an HTML body containing JavaScript page redirection.


        :param are_redirects_challenged: The are_redirects_challenged of this JsChallenge.
        :type: bool
        """
        self._are_redirects_challenged = are_redirects_challenged

    @property
    def criteria(self):
        """
        Gets the criteria of this JsChallenge.
        When defined, the JavaScript Challenge would be applied only for the requests that matched all the listed conditions.


        :return: The criteria of this JsChallenge.
        :rtype: list[oci.waas.models.AccessRuleCriteria]
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        """
        Sets the criteria of this JsChallenge.
        When defined, the JavaScript Challenge would be applied only for the requests that matched all the listed conditions.


        :param criteria: The criteria of this JsChallenge.
        :type: list[oci.waas.models.AccessRuleCriteria]
        """
        self._criteria = criteria

    @property
    def is_nat_enabled(self):
        """
        Gets the is_nat_enabled of this JsChallenge.
        When enabled, the user is identified not only by the IP address but also by an unique additional hash, which prevents blocking visitors with shared IP addresses.


        :return: The is_nat_enabled of this JsChallenge.
        :rtype: bool
        """
        return self._is_nat_enabled

    @is_nat_enabled.setter
    def is_nat_enabled(self, is_nat_enabled):
        """
        Sets the is_nat_enabled of this JsChallenge.
        When enabled, the user is identified not only by the IP address but also by an unique additional hash, which prevents blocking visitors with shared IP addresses.


        :param is_nat_enabled: The is_nat_enabled of this JsChallenge.
        :type: bool
        """
        self._is_nat_enabled = is_nat_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
