# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeviceFingerprintChallenge(object):
    """
    The device fingerprint challenge settings. The device fingerprint challenge generates hashed signatures of both virtual and real browsers to identify and block malicious bots.
    """

    #: A constant which can be used with the action property of a DeviceFingerprintChallenge.
    #: This constant has a value of "DETECT"
    ACTION_DETECT = "DETECT"

    #: A constant which can be used with the action property of a DeviceFingerprintChallenge.
    #: This constant has a value of "BLOCK"
    ACTION_BLOCK = "BLOCK"

    def __init__(self, **kwargs):
        """
        Initializes a new DeviceFingerprintChallenge object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this DeviceFingerprintChallenge.
        :type is_enabled: bool

        :param action:
            The value to assign to the action property of this DeviceFingerprintChallenge.
            Allowed values for this property are: "DETECT", "BLOCK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param failure_threshold:
            The value to assign to the failure_threshold property of this DeviceFingerprintChallenge.
        :type failure_threshold: int

        :param action_expiration_in_seconds:
            The value to assign to the action_expiration_in_seconds property of this DeviceFingerprintChallenge.
        :type action_expiration_in_seconds: int

        :param failure_threshold_expiration_in_seconds:
            The value to assign to the failure_threshold_expiration_in_seconds property of this DeviceFingerprintChallenge.
        :type failure_threshold_expiration_in_seconds: int

        :param max_address_count:
            The value to assign to the max_address_count property of this DeviceFingerprintChallenge.
        :type max_address_count: int

        :param max_address_count_expiration_in_seconds:
            The value to assign to the max_address_count_expiration_in_seconds property of this DeviceFingerprintChallenge.
        :type max_address_count_expiration_in_seconds: int

        :param challenge_settings:
            The value to assign to the challenge_settings property of this DeviceFingerprintChallenge.
        :type challenge_settings: oci.waas.models.BlockChallengeSettings

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'action': 'str',
            'failure_threshold': 'int',
            'action_expiration_in_seconds': 'int',
            'failure_threshold_expiration_in_seconds': 'int',
            'max_address_count': 'int',
            'max_address_count_expiration_in_seconds': 'int',
            'challenge_settings': 'BlockChallengeSettings'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'action': 'action',
            'failure_threshold': 'failureThreshold',
            'action_expiration_in_seconds': 'actionExpirationInSeconds',
            'failure_threshold_expiration_in_seconds': 'failureThresholdExpirationInSeconds',
            'max_address_count': 'maxAddressCount',
            'max_address_count_expiration_in_seconds': 'maxAddressCountExpirationInSeconds',
            'challenge_settings': 'challengeSettings'
        }

        self._is_enabled = None
        self._action = None
        self._failure_threshold = None
        self._action_expiration_in_seconds = None
        self._failure_threshold_expiration_in_seconds = None
        self._max_address_count = None
        self._max_address_count_expiration_in_seconds = None
        self._challenge_settings = None

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this DeviceFingerprintChallenge.
        Enables or disables the device fingerprint challenge Web Application Firewall feature.


        :return: The is_enabled of this DeviceFingerprintChallenge.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this DeviceFingerprintChallenge.
        Enables or disables the device fingerprint challenge Web Application Firewall feature.


        :param is_enabled: The is_enabled of this DeviceFingerprintChallenge.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def action(self):
        """
        Gets the action of this DeviceFingerprintChallenge.
        The action to take on requests from detected bots. If unspecified, defaults to `DETECT`.

        Allowed values for this property are: "DETECT", "BLOCK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this DeviceFingerprintChallenge.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this DeviceFingerprintChallenge.
        The action to take on requests from detected bots. If unspecified, defaults to `DETECT`.


        :param action: The action of this DeviceFingerprintChallenge.
        :type: str
        """
        allowed_values = ["DETECT", "BLOCK"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def failure_threshold(self):
        """
        Gets the failure_threshold of this DeviceFingerprintChallenge.
        The number of failed requests allowed before taking action. If unspecified, defaults to `10`.


        :return: The failure_threshold of this DeviceFingerprintChallenge.
        :rtype: int
        """
        return self._failure_threshold

    @failure_threshold.setter
    def failure_threshold(self, failure_threshold):
        """
        Sets the failure_threshold of this DeviceFingerprintChallenge.
        The number of failed requests allowed before taking action. If unspecified, defaults to `10`.


        :param failure_threshold: The failure_threshold of this DeviceFingerprintChallenge.
        :type: int
        """
        self._failure_threshold = failure_threshold

    @property
    def action_expiration_in_seconds(self):
        """
        Gets the action_expiration_in_seconds of this DeviceFingerprintChallenge.
        The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.


        :return: The action_expiration_in_seconds of this DeviceFingerprintChallenge.
        :rtype: int
        """
        return self._action_expiration_in_seconds

    @action_expiration_in_seconds.setter
    def action_expiration_in_seconds(self, action_expiration_in_seconds):
        """
        Sets the action_expiration_in_seconds of this DeviceFingerprintChallenge.
        The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.


        :param action_expiration_in_seconds: The action_expiration_in_seconds of this DeviceFingerprintChallenge.
        :type: int
        """
        self._action_expiration_in_seconds = action_expiration_in_seconds

    @property
    def failure_threshold_expiration_in_seconds(self):
        """
        Gets the failure_threshold_expiration_in_seconds of this DeviceFingerprintChallenge.
        The number of seconds before the failure threshold resets. If unspecified, defaults to `60`.


        :return: The failure_threshold_expiration_in_seconds of this DeviceFingerprintChallenge.
        :rtype: int
        """
        return self._failure_threshold_expiration_in_seconds

    @failure_threshold_expiration_in_seconds.setter
    def failure_threshold_expiration_in_seconds(self, failure_threshold_expiration_in_seconds):
        """
        Sets the failure_threshold_expiration_in_seconds of this DeviceFingerprintChallenge.
        The number of seconds before the failure threshold resets. If unspecified, defaults to `60`.


        :param failure_threshold_expiration_in_seconds: The failure_threshold_expiration_in_seconds of this DeviceFingerprintChallenge.
        :type: int
        """
        self._failure_threshold_expiration_in_seconds = failure_threshold_expiration_in_seconds

    @property
    def max_address_count(self):
        """
        Gets the max_address_count of this DeviceFingerprintChallenge.
        The maximum number of IP addresses permitted with the same device fingerprint. If unspecified, defaults to `20`.


        :return: The max_address_count of this DeviceFingerprintChallenge.
        :rtype: int
        """
        return self._max_address_count

    @max_address_count.setter
    def max_address_count(self, max_address_count):
        """
        Sets the max_address_count of this DeviceFingerprintChallenge.
        The maximum number of IP addresses permitted with the same device fingerprint. If unspecified, defaults to `20`.


        :param max_address_count: The max_address_count of this DeviceFingerprintChallenge.
        :type: int
        """
        self._max_address_count = max_address_count

    @property
    def max_address_count_expiration_in_seconds(self):
        """
        Gets the max_address_count_expiration_in_seconds of this DeviceFingerprintChallenge.
        The number of seconds before the maximum addresses count resets. If unspecified, defaults to `60`.


        :return: The max_address_count_expiration_in_seconds of this DeviceFingerprintChallenge.
        :rtype: int
        """
        return self._max_address_count_expiration_in_seconds

    @max_address_count_expiration_in_seconds.setter
    def max_address_count_expiration_in_seconds(self, max_address_count_expiration_in_seconds):
        """
        Sets the max_address_count_expiration_in_seconds of this DeviceFingerprintChallenge.
        The number of seconds before the maximum addresses count resets. If unspecified, defaults to `60`.


        :param max_address_count_expiration_in_seconds: The max_address_count_expiration_in_seconds of this DeviceFingerprintChallenge.
        :type: int
        """
        self._max_address_count_expiration_in_seconds = max_address_count_expiration_in_seconds

    @property
    def challenge_settings(self):
        """
        Gets the challenge_settings of this DeviceFingerprintChallenge.

        :return: The challenge_settings of this DeviceFingerprintChallenge.
        :rtype: oci.waas.models.BlockChallengeSettings
        """
        return self._challenge_settings

    @challenge_settings.setter
    def challenge_settings(self, challenge_settings):
        """
        Sets the challenge_settings of this DeviceFingerprintChallenge.

        :param challenge_settings: The challenge_settings of this DeviceFingerprintChallenge.
        :type: oci.waas.models.BlockChallengeSettings
        """
        self._challenge_settings = challenge_settings

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
