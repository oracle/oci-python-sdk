# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserAssessmentComparison(object):
    """
    Provides a list of differences for user assessment when compared with the baseline value.
    """

    #: A constant which can be used with the lifecycle_state property of a UserAssessmentComparison.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a UserAssessmentComparison.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a UserAssessmentComparison.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new UserAssessmentComparison object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this UserAssessmentComparison.
            Allowed values for this property are: "CREATING", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this UserAssessmentComparison.
        :type time_created: datetime

        :param summary:
            The value to assign to the summary property of this UserAssessmentComparison.
        :type summary: list[object]

        """
        self.swagger_types = {
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'summary': 'list[object]'
        }

        self.attribute_map = {
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'summary': 'summary'
        }

        self._lifecycle_state = None
        self._time_created = None
        self._summary = None

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this UserAssessmentComparison.
        The current state of the user assessment comparison.

        Allowed values for this property are: "CREATING", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this UserAssessmentComparison.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this UserAssessmentComparison.
        The current state of the user assessment comparison.


        :param lifecycle_state: The lifecycle_state of this UserAssessmentComparison.
        :type: str
        """
        allowed_values = ["CREATING", "SUCCEEDED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this UserAssessmentComparison.
        The date and time the user assessment comparison was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this UserAssessmentComparison.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this UserAssessmentComparison.
        The date and time the user assessment comparison was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this UserAssessmentComparison.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def summary(self):
        """
        Gets the summary of this UserAssessmentComparison.
        List containing maps as values.
        Example: `{\"Operations\": [ {\"CostCenter\": \"42\"} ] }`


        :return: The summary of this UserAssessmentComparison.
        :rtype: list[object]
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this UserAssessmentComparison.
        List containing maps as values.
        Example: `{\"Operations\": [ {\"CostCenter\": \"42\"} ] }`


        :param summary: The summary of this UserAssessmentComparison.
        :type: list[object]
        """
        self._summary = summary

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
