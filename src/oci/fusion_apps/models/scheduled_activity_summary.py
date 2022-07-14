# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduledActivitySummary(object):
    """
    Summary of the scheduled activity for a Fusion environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduledActivitySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ScheduledActivitySummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ScheduledActivitySummary.
        :type display_name: str

        :param run_cycle:
            The value to assign to the run_cycle property of this ScheduledActivitySummary.
        :type run_cycle: str

        :param fusion_environment_id:
            The value to assign to the fusion_environment_id property of this ScheduledActivitySummary.
        :type fusion_environment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ScheduledActivitySummary.
        :type lifecycle_state: str

        :param actions:
            The value to assign to the actions property of this ScheduledActivitySummary.
        :type actions: list[oci.fusion_apps.models.Action]

        :param time_scheduled_start:
            The value to assign to the time_scheduled_start property of this ScheduledActivitySummary.
        :type time_scheduled_start: datetime

        :param time_expected_finish:
            The value to assign to the time_expected_finish property of this ScheduledActivitySummary.
        :type time_expected_finish: datetime

        :param time_finished:
            The value to assign to the time_finished property of this ScheduledActivitySummary.
        :type time_finished: datetime

        :param delay_in_hours:
            The value to assign to the delay_in_hours property of this ScheduledActivitySummary.
        :type delay_in_hours: int

        :param service_availability:
            The value to assign to the service_availability property of this ScheduledActivitySummary.
        :type service_availability: str

        :param time_accepted:
            The value to assign to the time_accepted property of this ScheduledActivitySummary.
        :type time_accepted: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ScheduledActivitySummary.
        :type time_updated: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ScheduledActivitySummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ScheduledActivitySummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ScheduledActivitySummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'run_cycle': 'str',
            'fusion_environment_id': 'str',
            'lifecycle_state': 'str',
            'actions': 'list[Action]',
            'time_scheduled_start': 'datetime',
            'time_expected_finish': 'datetime',
            'time_finished': 'datetime',
            'delay_in_hours': 'int',
            'service_availability': 'str',
            'time_accepted': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'run_cycle': 'runCycle',
            'fusion_environment_id': 'fusionEnvironmentId',
            'lifecycle_state': 'lifecycleState',
            'actions': 'actions',
            'time_scheduled_start': 'timeScheduledStart',
            'time_expected_finish': 'timeExpectedFinish',
            'time_finished': 'timeFinished',
            'delay_in_hours': 'delayInHours',
            'service_availability': 'serviceAvailability',
            'time_accepted': 'timeAccepted',
            'time_updated': 'timeUpdated',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._run_cycle = None
        self._fusion_environment_id = None
        self._lifecycle_state = None
        self._actions = None
        self._time_scheduled_start = None
        self._time_expected_finish = None
        self._time_finished = None
        self._delay_in_hours = None
        self._service_availability = None
        self._time_accepted = None
        self._time_updated = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ScheduledActivitySummary.
        Unique identifier that is immutable on creation.


        :return: The id of this ScheduledActivitySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScheduledActivitySummary.
        Unique identifier that is immutable on creation.


        :param id: The id of this ScheduledActivitySummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ScheduledActivitySummary.
        A friendly name for the scheduled activity. Can be changed later.


        :return: The display_name of this ScheduledActivitySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ScheduledActivitySummary.
        A friendly name for the scheduled activity. Can be changed later.


        :param display_name: The display_name of this ScheduledActivitySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def run_cycle(self):
        """
        **[Required]** Gets the run_cycle of this ScheduledActivitySummary.
        The run cadence of this scheduled activity. Valid values are Quarterly, Monthly, OneOff, and Vertex.


        :return: The run_cycle of this ScheduledActivitySummary.
        :rtype: str
        """
        return self._run_cycle

    @run_cycle.setter
    def run_cycle(self, run_cycle):
        """
        Sets the run_cycle of this ScheduledActivitySummary.
        The run cadence of this scheduled activity. Valid values are Quarterly, Monthly, OneOff, and Vertex.


        :param run_cycle: The run_cycle of this ScheduledActivitySummary.
        :type: str
        """
        self._run_cycle = run_cycle

    @property
    def fusion_environment_id(self):
        """
        **[Required]** Gets the fusion_environment_id of this ScheduledActivitySummary.
        The OCID of the Fusion environment for the scheduled activity.


        :return: The fusion_environment_id of this ScheduledActivitySummary.
        :rtype: str
        """
        return self._fusion_environment_id

    @fusion_environment_id.setter
    def fusion_environment_id(self, fusion_environment_id):
        """
        Sets the fusion_environment_id of this ScheduledActivitySummary.
        The OCID of the Fusion environment for the scheduled activity.


        :param fusion_environment_id: The fusion_environment_id of this ScheduledActivitySummary.
        :type: str
        """
        self._fusion_environment_id = fusion_environment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ScheduledActivitySummary.
        The current state of the scheduled activity. Valid values are Scheduled, In progress , Failed, Completed.


        :return: The lifecycle_state of this ScheduledActivitySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ScheduledActivitySummary.
        The current state of the scheduled activity. Valid values are Scheduled, In progress , Failed, Completed.


        :param lifecycle_state: The lifecycle_state of this ScheduledActivitySummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def actions(self):
        """
        Gets the actions of this ScheduledActivitySummary.
        List of actions


        :return: The actions of this ScheduledActivitySummary.
        :rtype: list[oci.fusion_apps.models.Action]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this ScheduledActivitySummary.
        List of actions


        :param actions: The actions of this ScheduledActivitySummary.
        :type: list[oci.fusion_apps.models.Action]
        """
        self._actions = actions

    @property
    def time_scheduled_start(self):
        """
        **[Required]** Gets the time_scheduled_start of this ScheduledActivitySummary.
        Current time the scheduled activity is scheduled to start. An RFC3339 formatted datetime string.


        :return: The time_scheduled_start of this ScheduledActivitySummary.
        :rtype: datetime
        """
        return self._time_scheduled_start

    @time_scheduled_start.setter
    def time_scheduled_start(self, time_scheduled_start):
        """
        Sets the time_scheduled_start of this ScheduledActivitySummary.
        Current time the scheduled activity is scheduled to start. An RFC3339 formatted datetime string.


        :param time_scheduled_start: The time_scheduled_start of this ScheduledActivitySummary.
        :type: datetime
        """
        self._time_scheduled_start = time_scheduled_start

    @property
    def time_expected_finish(self):
        """
        **[Required]** Gets the time_expected_finish of this ScheduledActivitySummary.
        Current time the scheduled activity is scheduled to end. An RFC3339 formatted datetime string.


        :return: The time_expected_finish of this ScheduledActivitySummary.
        :rtype: datetime
        """
        return self._time_expected_finish

    @time_expected_finish.setter
    def time_expected_finish(self, time_expected_finish):
        """
        Sets the time_expected_finish of this ScheduledActivitySummary.
        Current time the scheduled activity is scheduled to end. An RFC3339 formatted datetime string.


        :param time_expected_finish: The time_expected_finish of this ScheduledActivitySummary.
        :type: datetime
        """
        self._time_expected_finish = time_expected_finish

    @property
    def time_finished(self):
        """
        Gets the time_finished of this ScheduledActivitySummary.
        The time the scheduled activity actually completed / cancelled / failed. An RFC3339 formatted datetime string.


        :return: The time_finished of this ScheduledActivitySummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this ScheduledActivitySummary.
        The time the scheduled activity actually completed / cancelled / failed. An RFC3339 formatted datetime string.


        :param time_finished: The time_finished of this ScheduledActivitySummary.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def delay_in_hours(self):
        """
        Gets the delay_in_hours of this ScheduledActivitySummary.
        Cumulative delay hours


        :return: The delay_in_hours of this ScheduledActivitySummary.
        :rtype: int
        """
        return self._delay_in_hours

    @delay_in_hours.setter
    def delay_in_hours(self, delay_in_hours):
        """
        Sets the delay_in_hours of this ScheduledActivitySummary.
        Cumulative delay hours


        :param delay_in_hours: The delay_in_hours of this ScheduledActivitySummary.
        :type: int
        """
        self._delay_in_hours = delay_in_hours

    @property
    def service_availability(self):
        """
        **[Required]** Gets the service_availability of this ScheduledActivitySummary.
        Service availability / impact during scheduled activity execution, up down


        :return: The service_availability of this ScheduledActivitySummary.
        :rtype: str
        """
        return self._service_availability

    @service_availability.setter
    def service_availability(self, service_availability):
        """
        Sets the service_availability of this ScheduledActivitySummary.
        Service availability / impact during scheduled activity execution, up down


        :param service_availability: The service_availability of this ScheduledActivitySummary.
        :type: str
        """
        self._service_availability = service_availability

    @property
    def time_accepted(self):
        """
        Gets the time_accepted of this ScheduledActivitySummary.
        The time the scheduled activity record was created. An RFC3339 formatted datetime string.


        :return: The time_accepted of this ScheduledActivitySummary.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this ScheduledActivitySummary.
        The time the scheduled activity record was created. An RFC3339 formatted datetime string.


        :param time_accepted: The time_accepted of this ScheduledActivitySummary.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ScheduledActivitySummary.
        The time the scheduled activity record was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this ScheduledActivitySummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ScheduledActivitySummary.
        The time the scheduled activity record was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this ScheduledActivitySummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ScheduledActivitySummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this ScheduledActivitySummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ScheduledActivitySummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this ScheduledActivitySummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ScheduledActivitySummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ScheduledActivitySummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ScheduledActivitySummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ScheduledActivitySummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ScheduledActivitySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ScheduledActivitySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ScheduledActivitySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ScheduledActivitySummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
