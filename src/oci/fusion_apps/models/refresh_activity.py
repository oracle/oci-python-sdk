# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RefreshActivity(object):
    """
    An environment refresh copies data from a source environment to a target environment, making a copy of the source environment onto the target environment. For more information, see `Refreshing an Environment`__.

    __ https://docs.cloud.oracle.com/iaas/Content/fusion-applications/refresh-environment.htm
    """

    #: A constant which can be used with the lifecycle_state property of a RefreshActivity.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a RefreshActivity.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a RefreshActivity.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a RefreshActivity.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a RefreshActivity.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the service_availability property of a RefreshActivity.
    #: This constant has a value of "AVAILABLE"
    SERVICE_AVAILABILITY_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the service_availability property of a RefreshActivity.
    #: This constant has a value of "UNAVAILABLE"
    SERVICE_AVAILABILITY_UNAVAILABLE = "UNAVAILABLE"

    #: A constant which can be used with the lifecycle_details property of a RefreshActivity.
    #: This constant has a value of "NONE"
    LIFECYCLE_DETAILS_NONE = "NONE"

    #: A constant which can be used with the lifecycle_details property of a RefreshActivity.
    #: This constant has a value of "ROLLBACKACCEPTED"
    LIFECYCLE_DETAILS_ROLLBACKACCEPTED = "ROLLBACKACCEPTED"

    #: A constant which can be used with the lifecycle_details property of a RefreshActivity.
    #: This constant has a value of "ROLLBACKINPROGRESS"
    LIFECYCLE_DETAILS_ROLLBACKINPROGRESS = "ROLLBACKINPROGRESS"

    #: A constant which can be used with the lifecycle_details property of a RefreshActivity.
    #: This constant has a value of "ROLLBACKSUCCEEDED"
    LIFECYCLE_DETAILS_ROLLBACKSUCCEEDED = "ROLLBACKSUCCEEDED"

    #: A constant which can be used with the lifecycle_details property of a RefreshActivity.
    #: This constant has a value of "ROLLBACKFAILED"
    LIFECYCLE_DETAILS_ROLLBACKFAILED = "ROLLBACKFAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new RefreshActivity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RefreshActivity.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this RefreshActivity.
        :type display_name: str

        :param source_fusion_environment_id:
            The value to assign to the source_fusion_environment_id property of this RefreshActivity.
        :type source_fusion_environment_id: str

        :param time_of_restoration_point:
            The value to assign to the time_of_restoration_point property of this RefreshActivity.
        :type time_of_restoration_point: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RefreshActivity.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param service_availability:
            The value to assign to the service_availability property of this RefreshActivity.
            Allowed values for this property are: "AVAILABLE", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type service_availability: str

        :param time_scheduled_start:
            The value to assign to the time_scheduled_start property of this RefreshActivity.
        :type time_scheduled_start: datetime

        :param time_expected_finish:
            The value to assign to the time_expected_finish property of this RefreshActivity.
        :type time_expected_finish: datetime

        :param time_finished:
            The value to assign to the time_finished property of this RefreshActivity.
        :type time_finished: datetime

        :param time_accepted:
            The value to assign to the time_accepted property of this RefreshActivity.
        :type time_accepted: datetime

        :param time_updated:
            The value to assign to the time_updated property of this RefreshActivity.
        :type time_updated: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this RefreshActivity.
            Allowed values for this property are: "NONE", "ROLLBACKACCEPTED", "ROLLBACKINPROGRESS", "ROLLBACKSUCCEEDED", "ROLLBACKFAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'source_fusion_environment_id': 'str',
            'time_of_restoration_point': 'datetime',
            'lifecycle_state': 'str',
            'service_availability': 'str',
            'time_scheduled_start': 'datetime',
            'time_expected_finish': 'datetime',
            'time_finished': 'datetime',
            'time_accepted': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'source_fusion_environment_id': 'sourceFusionEnvironmentId',
            'time_of_restoration_point': 'timeOfRestorationPoint',
            'lifecycle_state': 'lifecycleState',
            'service_availability': 'serviceAvailability',
            'time_scheduled_start': 'timeScheduledStart',
            'time_expected_finish': 'timeExpectedFinish',
            'time_finished': 'timeFinished',
            'time_accepted': 'timeAccepted',
            'time_updated': 'timeUpdated',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._id = None
        self._display_name = None
        self._source_fusion_environment_id = None
        self._time_of_restoration_point = None
        self._lifecycle_state = None
        self._service_availability = None
        self._time_scheduled_start = None
        self._time_expected_finish = None
        self._time_finished = None
        self._time_accepted = None
        self._time_updated = None
        self._lifecycle_details = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RefreshActivity.
        The unique identifier (OCID) of the refresh activity. Can't be changed after creation.


        :return: The id of this RefreshActivity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RefreshActivity.
        The unique identifier (OCID) of the refresh activity. Can't be changed after creation.


        :param id: The id of this RefreshActivity.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this RefreshActivity.
        A friendly name for the refresh activity. Can be changed later.


        :return: The display_name of this RefreshActivity.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RefreshActivity.
        A friendly name for the refresh activity. Can be changed later.


        :param display_name: The display_name of this RefreshActivity.
        :type: str
        """
        self._display_name = display_name

    @property
    def source_fusion_environment_id(self):
        """
        **[Required]** Gets the source_fusion_environment_id of this RefreshActivity.
        The OCID of the Fusion environment that is the source environment for the refresh.


        :return: The source_fusion_environment_id of this RefreshActivity.
        :rtype: str
        """
        return self._source_fusion_environment_id

    @source_fusion_environment_id.setter
    def source_fusion_environment_id(self, source_fusion_environment_id):
        """
        Sets the source_fusion_environment_id of this RefreshActivity.
        The OCID of the Fusion environment that is the source environment for the refresh.


        :param source_fusion_environment_id: The source_fusion_environment_id of this RefreshActivity.
        :type: str
        """
        self._source_fusion_environment_id = source_fusion_environment_id

    @property
    def time_of_restoration_point(self):
        """
        Gets the time_of_restoration_point of this RefreshActivity.
        The date and time of the most recent source environment backup used for the environment refresh.


        :return: The time_of_restoration_point of this RefreshActivity.
        :rtype: datetime
        """
        return self._time_of_restoration_point

    @time_of_restoration_point.setter
    def time_of_restoration_point(self, time_of_restoration_point):
        """
        Sets the time_of_restoration_point of this RefreshActivity.
        The date and time of the most recent source environment backup used for the environment refresh.


        :param time_of_restoration_point: The time_of_restoration_point of this RefreshActivity.
        :type: datetime
        """
        self._time_of_restoration_point = time_of_restoration_point

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this RefreshActivity.
        The current state of the refreshActivity.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this RefreshActivity.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RefreshActivity.
        The current state of the refreshActivity.


        :param lifecycle_state: The lifecycle_state of this RefreshActivity.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def service_availability(self):
        """
        **[Required]** Gets the service_availability of this RefreshActivity.
        Service availability / impact during refresh activity execution up down

        Allowed values for this property are: "AVAILABLE", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The service_availability of this RefreshActivity.
        :rtype: str
        """
        return self._service_availability

    @service_availability.setter
    def service_availability(self, service_availability):
        """
        Sets the service_availability of this RefreshActivity.
        Service availability / impact during refresh activity execution up down


        :param service_availability: The service_availability of this RefreshActivity.
        :type: str
        """
        allowed_values = ["AVAILABLE", "UNAVAILABLE"]
        if not value_allowed_none_or_none_sentinel(service_availability, allowed_values):
            service_availability = 'UNKNOWN_ENUM_VALUE'
        self._service_availability = service_availability

    @property
    def time_scheduled_start(self):
        """
        **[Required]** Gets the time_scheduled_start of this RefreshActivity.
        The time the refresh activity is scheduled to start. An RFC3339 formatted datetime string.


        :return: The time_scheduled_start of this RefreshActivity.
        :rtype: datetime
        """
        return self._time_scheduled_start

    @time_scheduled_start.setter
    def time_scheduled_start(self, time_scheduled_start):
        """
        Sets the time_scheduled_start of this RefreshActivity.
        The time the refresh activity is scheduled to start. An RFC3339 formatted datetime string.


        :param time_scheduled_start: The time_scheduled_start of this RefreshActivity.
        :type: datetime
        """
        self._time_scheduled_start = time_scheduled_start

    @property
    def time_expected_finish(self):
        """
        **[Required]** Gets the time_expected_finish of this RefreshActivity.
        The time the refresh activity is scheduled to end. An RFC3339 formatted datetime string.


        :return: The time_expected_finish of this RefreshActivity.
        :rtype: datetime
        """
        return self._time_expected_finish

    @time_expected_finish.setter
    def time_expected_finish(self, time_expected_finish):
        """
        Sets the time_expected_finish of this RefreshActivity.
        The time the refresh activity is scheduled to end. An RFC3339 formatted datetime string.


        :param time_expected_finish: The time_expected_finish of this RefreshActivity.
        :type: datetime
        """
        self._time_expected_finish = time_expected_finish

    @property
    def time_finished(self):
        """
        Gets the time_finished of this RefreshActivity.
        The time the refresh activity actually completed / cancelled / failed. An RFC3339 formatted datetime string.


        :return: The time_finished of this RefreshActivity.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this RefreshActivity.
        The time the refresh activity actually completed / cancelled / failed. An RFC3339 formatted datetime string.


        :param time_finished: The time_finished of this RefreshActivity.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def time_accepted(self):
        """
        Gets the time_accepted of this RefreshActivity.
        The time the refresh activity record was created. An RFC3339 formatted datetime string.


        :return: The time_accepted of this RefreshActivity.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this RefreshActivity.
        The time the refresh activity record was created. An RFC3339 formatted datetime string.


        :param time_accepted: The time_accepted of this RefreshActivity.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_updated(self):
        """
        Gets the time_updated of this RefreshActivity.
        The time the refresh activity record was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this RefreshActivity.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this RefreshActivity.
        The time the refresh activity record was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this RefreshActivity.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this RefreshActivity.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.

        Allowed values for this property are: "NONE", "ROLLBACKACCEPTED", "ROLLBACKINPROGRESS", "ROLLBACKSUCCEEDED", "ROLLBACKFAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_details of this RefreshActivity.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this RefreshActivity.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this RefreshActivity.
        :type: str
        """
        allowed_values = ["NONE", "ROLLBACKACCEPTED", "ROLLBACKINPROGRESS", "ROLLBACKSUCCEEDED", "ROLLBACKFAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_details, allowed_values):
            lifecycle_details = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
