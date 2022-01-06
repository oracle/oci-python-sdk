# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HumanInteractionChallenge(object):
    """
    The human interaction challenge settings. The human interaction challenge checks various event listeners in the user's browser to determine if there is a human user making a request.
    """

    #: A constant which can be used with the action property of a HumanInteractionChallenge.
    #: This constant has a value of "DETECT"
    ACTION_DETECT = "DETECT"

    #: A constant which can be used with the action property of a HumanInteractionChallenge.
    #: This constant has a value of "BLOCK"
    ACTION_BLOCK = "BLOCK"

    def __init__(self, **kwargs):
        """
        Initializes a new HumanInteractionChallenge object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this HumanInteractionChallenge.
        :type is_enabled: bool

        :param action:
            The value to assign to the action property of this HumanInteractionChallenge.
            Allowed values for this property are: "DETECT", "BLOCK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param failure_threshold:
            The value to assign to the failure_threshold property of this HumanInteractionChallenge.
        :type failure_threshold: int

        :param action_expiration_in_seconds:
            The value to assign to the action_expiration_in_seconds property of this HumanInteractionChallenge.
        :type action_expiration_in_seconds: int

        :param failure_threshold_expiration_in_seconds:
            The value to assign to the failure_threshold_expiration_in_seconds property of this HumanInteractionChallenge.
        :type failure_threshold_expiration_in_seconds: int

        :param interaction_threshold:
            The value to assign to the interaction_threshold property of this HumanInteractionChallenge.
        :type interaction_threshold: int

        :param recording_period_in_seconds:
            The value to assign to the recording_period_in_seconds property of this HumanInteractionChallenge.
        :type recording_period_in_seconds: int

        :param set_http_header:
            The value to assign to the set_http_header property of this HumanInteractionChallenge.
        :type set_http_header: oci.waas.models.Header

        :param challenge_settings:
            The value to assign to the challenge_settings property of this HumanInteractionChallenge.
        :type challenge_settings: oci.waas.models.BlockChallengeSettings

        :param is_nat_enabled:
            The value to assign to the is_nat_enabled property of this HumanInteractionChallenge.
        :type is_nat_enabled: bool

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'action': 'str',
            'failure_threshold': 'int',
            'action_expiration_in_seconds': 'int',
            'failure_threshold_expiration_in_seconds': 'int',
            'interaction_threshold': 'int',
            'recording_period_in_seconds': 'int',
            'set_http_header': 'Header',
            'challenge_settings': 'BlockChallengeSettings',
            'is_nat_enabled': 'bool'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'action': 'action',
            'failure_threshold': 'failureThreshold',
            'action_expiration_in_seconds': 'actionExpirationInSeconds',
            'failure_threshold_expiration_in_seconds': 'failureThresholdExpirationInSeconds',
            'interaction_threshold': 'interactionThreshold',
            'recording_period_in_seconds': 'recordingPeriodInSeconds',
            'set_http_header': 'setHttpHeader',
            'challenge_settings': 'challengeSettings',
            'is_nat_enabled': 'isNatEnabled'
        }

        self._is_enabled = None
        self._action = None
        self._failure_threshold = None
        self._action_expiration_in_seconds = None
        self._failure_threshold_expiration_in_seconds = None
        self._interaction_threshold = None
        self._recording_period_in_seconds = None
        self._set_http_header = None
        self._challenge_settings = None
        self._is_nat_enabled = None

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this HumanInteractionChallenge.
        Enables or disables the human interaction challenge Web Application Firewall feature.


        :return: The is_enabled of this HumanInteractionChallenge.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this HumanInteractionChallenge.
        Enables or disables the human interaction challenge Web Application Firewall feature.


        :param is_enabled: The is_enabled of this HumanInteractionChallenge.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def action(self):
        """
        Gets the action of this HumanInteractionChallenge.
        The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.

        Allowed values for this property are: "DETECT", "BLOCK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this HumanInteractionChallenge.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this HumanInteractionChallenge.
        The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.


        :param action: The action of this HumanInteractionChallenge.
        :type: str
        """
        allowed_values = ["DETECT", "BLOCK"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def failure_threshold(self):
        """
        Gets the failure_threshold of this HumanInteractionChallenge.
        The number of failed requests before taking action. If unspecified, defaults to `10`.


        :return: The failure_threshold of this HumanInteractionChallenge.
        :rtype: int
        """
        return self._failure_threshold

    @failure_threshold.setter
    def failure_threshold(self, failure_threshold):
        """
        Sets the failure_threshold of this HumanInteractionChallenge.
        The number of failed requests before taking action. If unspecified, defaults to `10`.


        :param failure_threshold: The failure_threshold of this HumanInteractionChallenge.
        :type: int
        """
        self._failure_threshold = failure_threshold

    @property
    def action_expiration_in_seconds(self):
        """
        Gets the action_expiration_in_seconds of this HumanInteractionChallenge.
        The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.


        :return: The action_expiration_in_seconds of this HumanInteractionChallenge.
        :rtype: int
        """
        return self._action_expiration_in_seconds

    @action_expiration_in_seconds.setter
    def action_expiration_in_seconds(self, action_expiration_in_seconds):
        """
        Sets the action_expiration_in_seconds of this HumanInteractionChallenge.
        The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.


        :param action_expiration_in_seconds: The action_expiration_in_seconds of this HumanInteractionChallenge.
        :type: int
        """
        self._action_expiration_in_seconds = action_expiration_in_seconds

    @property
    def failure_threshold_expiration_in_seconds(self):
        """
        Gets the failure_threshold_expiration_in_seconds of this HumanInteractionChallenge.
        The number of seconds before the failure threshold resets. If unspecified, defaults to  `60`.


        :return: The failure_threshold_expiration_in_seconds of this HumanInteractionChallenge.
        :rtype: int
        """
        return self._failure_threshold_expiration_in_seconds

    @failure_threshold_expiration_in_seconds.setter
    def failure_threshold_expiration_in_seconds(self, failure_threshold_expiration_in_seconds):
        """
        Sets the failure_threshold_expiration_in_seconds of this HumanInteractionChallenge.
        The number of seconds before the failure threshold resets. If unspecified, defaults to  `60`.


        :param failure_threshold_expiration_in_seconds: The failure_threshold_expiration_in_seconds of this HumanInteractionChallenge.
        :type: int
        """
        self._failure_threshold_expiration_in_seconds = failure_threshold_expiration_in_seconds

    @property
    def interaction_threshold(self):
        """
        Gets the interaction_threshold of this HumanInteractionChallenge.
        The number of interactions required to pass the challenge. If unspecified, defaults to `3`.


        :return: The interaction_threshold of this HumanInteractionChallenge.
        :rtype: int
        """
        return self._interaction_threshold

    @interaction_threshold.setter
    def interaction_threshold(self, interaction_threshold):
        """
        Sets the interaction_threshold of this HumanInteractionChallenge.
        The number of interactions required to pass the challenge. If unspecified, defaults to `3`.


        :param interaction_threshold: The interaction_threshold of this HumanInteractionChallenge.
        :type: int
        """
        self._interaction_threshold = interaction_threshold

    @property
    def recording_period_in_seconds(self):
        """
        Gets the recording_period_in_seconds of this HumanInteractionChallenge.
        The number of seconds to record the interactions from the user. If unspecified, defaults to `15`.


        :return: The recording_period_in_seconds of this HumanInteractionChallenge.
        :rtype: int
        """
        return self._recording_period_in_seconds

    @recording_period_in_seconds.setter
    def recording_period_in_seconds(self, recording_period_in_seconds):
        """
        Sets the recording_period_in_seconds of this HumanInteractionChallenge.
        The number of seconds to record the interactions from the user. If unspecified, defaults to `15`.


        :param recording_period_in_seconds: The recording_period_in_seconds of this HumanInteractionChallenge.
        :type: int
        """
        self._recording_period_in_seconds = recording_period_in_seconds

    @property
    def set_http_header(self):
        """
        Gets the set_http_header of this HumanInteractionChallenge.
        Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the `action` is set to `DETECT`.


        :return: The set_http_header of this HumanInteractionChallenge.
        :rtype: oci.waas.models.Header
        """
        return self._set_http_header

    @set_http_header.setter
    def set_http_header(self, set_http_header):
        """
        Sets the set_http_header of this HumanInteractionChallenge.
        Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the `action` is set to `DETECT`.


        :param set_http_header: The set_http_header of this HumanInteractionChallenge.
        :type: oci.waas.models.Header
        """
        self._set_http_header = set_http_header

    @property
    def challenge_settings(self):
        """
        Gets the challenge_settings of this HumanInteractionChallenge.

        :return: The challenge_settings of this HumanInteractionChallenge.
        :rtype: oci.waas.models.BlockChallengeSettings
        """
        return self._challenge_settings

    @challenge_settings.setter
    def challenge_settings(self, challenge_settings):
        """
        Sets the challenge_settings of this HumanInteractionChallenge.

        :param challenge_settings: The challenge_settings of this HumanInteractionChallenge.
        :type: oci.waas.models.BlockChallengeSettings
        """
        self._challenge_settings = challenge_settings

    @property
    def is_nat_enabled(self):
        """
        Gets the is_nat_enabled of this HumanInteractionChallenge.
        When enabled, the user is identified not only by the IP address but also by an unique additional hash, which prevents blocking visitors with shared IP addresses.


        :return: The is_nat_enabled of this HumanInteractionChallenge.
        :rtype: bool
        """
        return self._is_nat_enabled

    @is_nat_enabled.setter
    def is_nat_enabled(self, is_nat_enabled):
        """
        Sets the is_nat_enabled of this HumanInteractionChallenge.
        When enabled, the user is identified not only by the IP address but also by an unique additional hash, which prevents blocking visitors with shared IP addresses.


        :param is_nat_enabled: The is_nat_enabled of this HumanInteractionChallenge.
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
