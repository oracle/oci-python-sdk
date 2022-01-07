# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .secret_rule import SecretRule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecretExpiryRule(SecretRule):
    """
    A rule that helps enforce the expiration of a secret's contents.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SecretExpiryRule object with values from keyword arguments. The default value of the :py:attr:`~oci.vault.models.SecretExpiryRule.rule_type` attribute
        of this class is ``SECRET_EXPIRY_RULE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param rule_type:
            The value to assign to the rule_type property of this SecretExpiryRule.
            Allowed values for this property are: "SECRET_EXPIRY_RULE", "SECRET_REUSE_RULE"
        :type rule_type: str

        :param secret_version_expiry_interval:
            The value to assign to the secret_version_expiry_interval property of this SecretExpiryRule.
        :type secret_version_expiry_interval: str

        :param time_of_absolute_expiry:
            The value to assign to the time_of_absolute_expiry property of this SecretExpiryRule.
        :type time_of_absolute_expiry: datetime

        :param is_secret_content_retrieval_blocked_on_expiry:
            The value to assign to the is_secret_content_retrieval_blocked_on_expiry property of this SecretExpiryRule.
        :type is_secret_content_retrieval_blocked_on_expiry: bool

        """
        self.swagger_types = {
            'rule_type': 'str',
            'secret_version_expiry_interval': 'str',
            'time_of_absolute_expiry': 'datetime',
            'is_secret_content_retrieval_blocked_on_expiry': 'bool'
        }

        self.attribute_map = {
            'rule_type': 'ruleType',
            'secret_version_expiry_interval': 'secretVersionExpiryInterval',
            'time_of_absolute_expiry': 'timeOfAbsoluteExpiry',
            'is_secret_content_retrieval_blocked_on_expiry': 'isSecretContentRetrievalBlockedOnExpiry'
        }

        self._rule_type = None
        self._secret_version_expiry_interval = None
        self._time_of_absolute_expiry = None
        self._is_secret_content_retrieval_blocked_on_expiry = None
        self._rule_type = 'SECRET_EXPIRY_RULE'

    @property
    def secret_version_expiry_interval(self):
        """
        Gets the secret_version_expiry_interval of this SecretExpiryRule.
        A property indicating how long the secret contents will be considered valid, expressed in
        `ISO 8601`__ format. The secret needs to be
        updated when the secret content expires. No enforcement mechanism exists at this time, but audit logs
        record the expiration on the appropriate date, according to the time interval specified in the rule.
        The timer resets after you update the secret contents.
        The minimum value is 1 day and the maximum value is 90 days for this property. Currently, only intervals expressed in days are supported.
        For example, pass `P3D` to have the secret version expire every 3 days.

        __ https://en.wikipedia.org/wiki/ISO_8601#Time_intervals


        :return: The secret_version_expiry_interval of this SecretExpiryRule.
        :rtype: str
        """
        return self._secret_version_expiry_interval

    @secret_version_expiry_interval.setter
    def secret_version_expiry_interval(self, secret_version_expiry_interval):
        """
        Sets the secret_version_expiry_interval of this SecretExpiryRule.
        A property indicating how long the secret contents will be considered valid, expressed in
        `ISO 8601`__ format. The secret needs to be
        updated when the secret content expires. No enforcement mechanism exists at this time, but audit logs
        record the expiration on the appropriate date, according to the time interval specified in the rule.
        The timer resets after you update the secret contents.
        The minimum value is 1 day and the maximum value is 90 days for this property. Currently, only intervals expressed in days are supported.
        For example, pass `P3D` to have the secret version expire every 3 days.

        __ https://en.wikipedia.org/wiki/ISO_8601#Time_intervals


        :param secret_version_expiry_interval: The secret_version_expiry_interval of this SecretExpiryRule.
        :type: str
        """
        self._secret_version_expiry_interval = secret_version_expiry_interval

    @property
    def time_of_absolute_expiry(self):
        """
        Gets the time_of_absolute_expiry of this SecretExpiryRule.
        An optional property indicating the absolute time when this secret will expire, expressed in `RFC 3339`__ timestamp format.
        The minimum number of days from current time is 1 day and the maximum number of days from current time is 365 days.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_absolute_expiry of this SecretExpiryRule.
        :rtype: datetime
        """
        return self._time_of_absolute_expiry

    @time_of_absolute_expiry.setter
    def time_of_absolute_expiry(self, time_of_absolute_expiry):
        """
        Sets the time_of_absolute_expiry of this SecretExpiryRule.
        An optional property indicating the absolute time when this secret will expire, expressed in `RFC 3339`__ timestamp format.
        The minimum number of days from current time is 1 day and the maximum number of days from current time is 365 days.
        Example: `2019-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_absolute_expiry: The time_of_absolute_expiry of this SecretExpiryRule.
        :type: datetime
        """
        self._time_of_absolute_expiry = time_of_absolute_expiry

    @property
    def is_secret_content_retrieval_blocked_on_expiry(self):
        """
        Gets the is_secret_content_retrieval_blocked_on_expiry of this SecretExpiryRule.
        A property indicating whether to block retrieval of the secret content, on expiry. The default is false.
        If the secret has already expired and you would like to retrieve the secret contents,
        you need to edit the secret rule to disable this property, to allow reading the secret content.


        :return: The is_secret_content_retrieval_blocked_on_expiry of this SecretExpiryRule.
        :rtype: bool
        """
        return self._is_secret_content_retrieval_blocked_on_expiry

    @is_secret_content_retrieval_blocked_on_expiry.setter
    def is_secret_content_retrieval_blocked_on_expiry(self, is_secret_content_retrieval_blocked_on_expiry):
        """
        Sets the is_secret_content_retrieval_blocked_on_expiry of this SecretExpiryRule.
        A property indicating whether to block retrieval of the secret content, on expiry. The default is false.
        If the secret has already expired and you would like to retrieve the secret contents,
        you need to edit the secret rule to disable this property, to allow reading the secret content.


        :param is_secret_content_retrieval_blocked_on_expiry: The is_secret_content_retrieval_blocked_on_expiry of this SecretExpiryRule.
        :type: bool
        """
        self._is_secret_content_retrieval_blocked_on_expiry = is_secret_content_retrieval_blocked_on_expiry

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
