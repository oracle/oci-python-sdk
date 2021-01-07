# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRetentionRuleDetails(object):
    """
    The details to create a retention rule.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRetentionRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateRetentionRuleDetails.
        :type display_name: str

        :param duration:
            The value to assign to the duration property of this CreateRetentionRuleDetails.
        :type duration: oci.object_storage.models.Duration

        :param time_rule_locked:
            The value to assign to the time_rule_locked property of this CreateRetentionRuleDetails.
        :type time_rule_locked: datetime

        """
        self.swagger_types = {
            'display_name': 'str',
            'duration': 'Duration',
            'time_rule_locked': 'datetime'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'duration': 'duration',
            'time_rule_locked': 'timeRuleLocked'
        }

        self._display_name = None
        self._duration = None
        self._time_rule_locked = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateRetentionRuleDetails.
        A user-specified name for the retention rule. Names can be helpful in identifying retention rules.


        :return: The display_name of this CreateRetentionRuleDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateRetentionRuleDetails.
        A user-specified name for the retention rule. Names can be helpful in identifying retention rules.


        :param display_name: The display_name of this CreateRetentionRuleDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def duration(self):
        """
        Gets the duration of this CreateRetentionRuleDetails.

        :return: The duration of this CreateRetentionRuleDetails.
        :rtype: oci.object_storage.models.Duration
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this CreateRetentionRuleDetails.

        :param duration: The duration of this CreateRetentionRuleDetails.
        :type: oci.object_storage.models.Duration
        """
        self._duration = duration

    @property
    def time_rule_locked(self):
        """
        Gets the time_rule_locked of this CreateRetentionRuleDetails.
        The date and time as per `RFC 3339`__ after which this rule is locked
        and can only be deleted by deleting the bucket. Once a rule is locked, only increases in the duration are
        allowed and no other properties can be changed. This property cannot be updated for rules that are in a
        locked state. Specifying it when a duration is not specified is considered an error.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_rule_locked of this CreateRetentionRuleDetails.
        :rtype: datetime
        """
        return self._time_rule_locked

    @time_rule_locked.setter
    def time_rule_locked(self, time_rule_locked):
        """
        Sets the time_rule_locked of this CreateRetentionRuleDetails.
        The date and time as per `RFC 3339`__ after which this rule is locked
        and can only be deleted by deleting the bucket. Once a rule is locked, only increases in the duration are
        allowed and no other properties can be changed. This property cannot be updated for rules that are in a
        locked state. Specifying it when a duration is not specified is considered an error.

        __ https://tools.ietf.org/html/rfc3339


        :param time_rule_locked: The time_rule_locked of this CreateRetentionRuleDetails.
        :type: datetime
        """
        self._time_rule_locked = time_rule_locked

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
