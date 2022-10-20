# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateRunDetails(object):
    """
    The update run details. Only a limited set of properties of a run can be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateRunDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateRunDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateRunDetails.
        :type freeform_tags: dict(str, str)

        :param max_duration_in_minutes:
            The value to assign to the max_duration_in_minutes property of this UpdateRunDetails.
        :type max_duration_in_minutes: int

        :param idle_timeout_in_minutes:
            The value to assign to the idle_timeout_in_minutes property of this UpdateRunDetails.
        :type idle_timeout_in_minutes: int

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'max_duration_in_minutes': 'int',
            'idle_timeout_in_minutes': 'int'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'max_duration_in_minutes': 'maxDurationInMinutes',
            'idle_timeout_in_minutes': 'idleTimeoutInMinutes'
        }

        self._defined_tags = None
        self._freeform_tags = None
        self._max_duration_in_minutes = None
        self._idle_timeout_in_minutes = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateRunDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateRunDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateRunDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateRunDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateRunDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateRunDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateRunDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateRunDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def max_duration_in_minutes(self):
        """
        Gets the max_duration_in_minutes of this UpdateRunDetails.
        The maximum duration in minutes for which an Application should run. Data Flow Run would be terminated
        once it reaches this duration from the time it transitions to `IN_PROGRESS` state.


        :return: The max_duration_in_minutes of this UpdateRunDetails.
        :rtype: int
        """
        return self._max_duration_in_minutes

    @max_duration_in_minutes.setter
    def max_duration_in_minutes(self, max_duration_in_minutes):
        """
        Sets the max_duration_in_minutes of this UpdateRunDetails.
        The maximum duration in minutes for which an Application should run. Data Flow Run would be terminated
        once it reaches this duration from the time it transitions to `IN_PROGRESS` state.


        :param max_duration_in_minutes: The max_duration_in_minutes of this UpdateRunDetails.
        :type: int
        """
        self._max_duration_in_minutes = max_duration_in_minutes

    @property
    def idle_timeout_in_minutes(self):
        """
        Gets the idle_timeout_in_minutes of this UpdateRunDetails.
        The timeout value in minutes used to manage Runs. A Run would be stopped after inactivity for this amount of time period.
        Note: This parameter is currently only applicable for Runs of type `SESSION`. Default value is 2880 minutes (2 days)


        :return: The idle_timeout_in_minutes of this UpdateRunDetails.
        :rtype: int
        """
        return self._idle_timeout_in_minutes

    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, idle_timeout_in_minutes):
        """
        Sets the idle_timeout_in_minutes of this UpdateRunDetails.
        The timeout value in minutes used to manage Runs. A Run would be stopped after inactivity for this amount of time period.
        Note: This parameter is currently only applicable for Runs of type `SESSION`. Default value is 2880 minutes (2 days)


        :param idle_timeout_in_minutes: The idle_timeout_in_minutes of this UpdateRunDetails.
        :type: int
        """
        self._idle_timeout_in_minutes = idle_timeout_in_minutes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
