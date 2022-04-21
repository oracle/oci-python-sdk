# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduleSummary(object):
    """
    Schedule summary for listSchedule.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ScheduleSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this ScheduleSummary.
        :type name: str

        :param schedule_recurrences:
            The value to assign to the schedule_recurrences property of this ScheduleSummary.
        :type schedule_recurrences: str

        :param time_scheduled:
            The value to assign to the time_scheduled property of this ScheduleSummary.
        :type time_scheduled: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ScheduleSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ScheduleSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ScheduleSummary.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ScheduleSummary.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'schedule_recurrences': 'str',
            'time_scheduled': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'schedule_recurrences': 'scheduleRecurrences',
            'time_scheduled': 'timeScheduled',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._name = None
        self._schedule_recurrences = None
        self._time_scheduled = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ScheduleSummary.
        The schedule OCID.


        :return: The id of this ScheduleSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScheduleSummary.
        The schedule OCID.


        :param id: The id of this ScheduleSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ScheduleSummary.
        The unique name of the schedule created by the user


        :return: The name of this ScheduleSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ScheduleSummary.
        The unique name of the schedule created by the user


        :param name: The name of this ScheduleSummary.
        :type: str
        """
        self._name = name

    @property
    def schedule_recurrences(self):
        """
        **[Required]** Gets the schedule_recurrences of this ScheduleSummary.
        In x-obmcs-recurring-time format shown here: https://datatracker.ietf.org/doc/html/rfc5545#section-3.3.10
        Describes the frequency of when the schedule will be run


        :return: The schedule_recurrences of this ScheduleSummary.
        :rtype: str
        """
        return self._schedule_recurrences

    @schedule_recurrences.setter
    def schedule_recurrences(self, schedule_recurrences):
        """
        Sets the schedule_recurrences of this ScheduleSummary.
        In x-obmcs-recurring-time format shown here: https://datatracker.ietf.org/doc/html/rfc5545#section-3.3.10
        Describes the frequency of when the schedule will be run


        :param schedule_recurrences: The schedule_recurrences of this ScheduleSummary.
        :type: str
        """
        self._schedule_recurrences = schedule_recurrences

    @property
    def time_scheduled(self):
        """
        **[Required]** Gets the time_scheduled of this ScheduleSummary.
        The date and time of the first time job execution


        :return: The time_scheduled of this ScheduleSummary.
        :rtype: datetime
        """
        return self._time_scheduled

    @time_scheduled.setter
    def time_scheduled(self, time_scheduled):
        """
        Sets the time_scheduled of this ScheduleSummary.
        The date and time of the first time job execution


        :param time_scheduled: The time_scheduled of this ScheduleSummary.
        :type: datetime
        """
        self._time_scheduled = time_scheduled

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ScheduleSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ScheduleSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ScheduleSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ScheduleSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ScheduleSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ScheduleSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ScheduleSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ScheduleSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ScheduleSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this ScheduleSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ScheduleSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this ScheduleSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ScheduleSummary.
        The lifecycle state of the schedule summary


        :return: The lifecycle_state of this ScheduleSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ScheduleSummary.
        The lifecycle state of the schedule summary


        :param lifecycle_state: The lifecycle_state of this ScheduleSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
