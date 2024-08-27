# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExecutionWindow(object):
    """
    Details of an execution window.
    """

    #: A constant which can be used with the lifecycle_state property of a ExecutionWindow.
    #: This constant has a value of "CREATED"
    LIFECYCLE_STATE_CREATED = "CREATED"

    #: A constant which can be used with the lifecycle_state property of a ExecutionWindow.
    #: This constant has a value of "SCHEDULED"
    LIFECYCLE_STATE_SCHEDULED = "SCHEDULED"

    #: A constant which can be used with the lifecycle_state property of a ExecutionWindow.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a ExecutionWindow.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a ExecutionWindow.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a ExecutionWindow.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ExecutionWindow.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ExecutionWindow.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a ExecutionWindow.
    #: This constant has a value of "PARTIAL_SUCCESS"
    LIFECYCLE_STATE_PARTIAL_SUCCESS = "PARTIAL_SUCCESS"

    #: A constant which can be used with the lifecycle_state property of a ExecutionWindow.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ExecutionWindow.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_substate property of a ExecutionWindow.
    #: This constant has a value of "DURATION_EXCEEDED"
    LIFECYCLE_SUBSTATE_DURATION_EXCEEDED = "DURATION_EXCEEDED"

    #: A constant which can be used with the lifecycle_substate property of a ExecutionWindow.
    #: This constant has a value of "MAINTENANCE_IN_PROGRESS"
    LIFECYCLE_SUBSTATE_MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_substate property of a ExecutionWindow.
    #: This constant has a value of "WAITING"
    LIFECYCLE_SUBSTATE_WAITING = "WAITING"

    #: A constant which can be used with the lifecycle_substate property of a ExecutionWindow.
    #: This constant has a value of "RESCHEDULED"
    LIFECYCLE_SUBSTATE_RESCHEDULED = "RESCHEDULED"

    #: A constant which can be used with the window_type property of a ExecutionWindow.
    #: This constant has a value of "PLANNED"
    WINDOW_TYPE_PLANNED = "PLANNED"

    #: A constant which can be used with the window_type property of a ExecutionWindow.
    #: This constant has a value of "UNPLANNED"
    WINDOW_TYPE_UNPLANNED = "UNPLANNED"

    def __init__(self, **kwargs):
        """
        Initializes a new ExecutionWindow object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExecutionWindow.
        :type id: str

        :param execution_resource_id:
            The value to assign to the execution_resource_id property of this ExecutionWindow.
        :type execution_resource_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExecutionWindow.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ExecutionWindow.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ExecutionWindow.
        :type description: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExecutionWindow.
            Allowed values for this property are: "CREATED", "SCHEDULED", "IN_PROGRESS", "FAILED", "CANCELED", "UPDATING", "DELETED", "SUCCEEDED", "PARTIAL_SUCCESS", "CREATING", "DELETING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_substate:
            The value to assign to the lifecycle_substate property of this ExecutionWindow.
            Allowed values for this property are: "DURATION_EXCEEDED", "MAINTENANCE_IN_PROGRESS", "WAITING", "RESCHEDULED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_substate: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExecutionWindow.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this ExecutionWindow.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ExecutionWindow.
        :type time_updated: datetime

        :param time_started:
            The value to assign to the time_started property of this ExecutionWindow.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this ExecutionWindow.
        :type time_ended: datetime

        :param time_scheduled:
            The value to assign to the time_scheduled property of this ExecutionWindow.
        :type time_scheduled: datetime

        :param window_duration_in_mins:
            The value to assign to the window_duration_in_mins property of this ExecutionWindow.
        :type window_duration_in_mins: int

        :param is_enforced_duration:
            The value to assign to the is_enforced_duration property of this ExecutionWindow.
        :type is_enforced_duration: bool

        :param estimated_time_in_mins:
            The value to assign to the estimated_time_in_mins property of this ExecutionWindow.
        :type estimated_time_in_mins: int

        :param total_time_taken_in_mins:
            The value to assign to the total_time_taken_in_mins property of this ExecutionWindow.
        :type total_time_taken_in_mins: int

        :param window_type:
            The value to assign to the window_type property of this ExecutionWindow.
            Allowed values for this property are: "PLANNED", "UNPLANNED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type window_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ExecutionWindow.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ExecutionWindow.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'execution_resource_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'lifecycle_state': 'str',
            'lifecycle_substate': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'time_scheduled': 'datetime',
            'window_duration_in_mins': 'int',
            'is_enforced_duration': 'bool',
            'estimated_time_in_mins': 'int',
            'total_time_taken_in_mins': 'int',
            'window_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'execution_resource_id': 'executionResourceId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_substate': 'lifecycleSubstate',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'time_scheduled': 'timeScheduled',
            'window_duration_in_mins': 'windowDurationInMins',
            'is_enforced_duration': 'isEnforcedDuration',
            'estimated_time_in_mins': 'estimatedTimeInMins',
            'total_time_taken_in_mins': 'totalTimeTakenInMins',
            'window_type': 'windowType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._execution_resource_id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._lifecycle_state = None
        self._lifecycle_substate = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._time_started = None
        self._time_ended = None
        self._time_scheduled = None
        self._window_duration_in_mins = None
        self._is_enforced_duration = None
        self._estimated_time_in_mins = None
        self._total_time_taken_in_mins = None
        self._window_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExecutionWindow.
        The `OCID`__ of the execution window.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ExecutionWindow.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExecutionWindow.
        The `OCID`__ of the execution window.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExecutionWindow.
        :type: str
        """
        self._id = id

    @property
    def execution_resource_id(self):
        """
        **[Required]** Gets the execution_resource_id of this ExecutionWindow.
        The `OCID`__ of the execution resource the execution window belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The execution_resource_id of this ExecutionWindow.
        :rtype: str
        """
        return self._execution_resource_id

    @execution_resource_id.setter
    def execution_resource_id(self, execution_resource_id):
        """
        Sets the execution_resource_id of this ExecutionWindow.
        The `OCID`__ of the execution resource the execution window belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param execution_resource_id: The execution_resource_id of this ExecutionWindow.
        :type: str
        """
        self._execution_resource_id = execution_resource_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExecutionWindow.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExecutionWindow.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExecutionWindow.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExecutionWindow.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ExecutionWindow.
        The user-friendly name for the execution window. The name does not need to be unique.


        :return: The display_name of this ExecutionWindow.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExecutionWindow.
        The user-friendly name for the execution window. The name does not need to be unique.


        :param display_name: The display_name of this ExecutionWindow.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ExecutionWindow.
        Description of the execution window.


        :return: The description of this ExecutionWindow.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ExecutionWindow.
        Description of the execution window.


        :param description: The description of this ExecutionWindow.
        :type: str
        """
        self._description = description

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ExecutionWindow.
        The current state of the Schedule Policy. Valid states are CREATED, SCHEDULED, IN_PROGRESS, FAILED, CANCELED,
        UPDATING, DELETED, SUCCEEDED and PARTIAL_SUCCESS.

        Allowed values for this property are: "CREATED", "SCHEDULED", "IN_PROGRESS", "FAILED", "CANCELED", "UPDATING", "DELETED", "SUCCEEDED", "PARTIAL_SUCCESS", "CREATING", "DELETING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ExecutionWindow.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ExecutionWindow.
        The current state of the Schedule Policy. Valid states are CREATED, SCHEDULED, IN_PROGRESS, FAILED, CANCELED,
        UPDATING, DELETED, SUCCEEDED and PARTIAL_SUCCESS.


        :param lifecycle_state: The lifecycle_state of this ExecutionWindow.
        :type: str
        """
        allowed_values = ["CREATED", "SCHEDULED", "IN_PROGRESS", "FAILED", "CANCELED", "UPDATING", "DELETED", "SUCCEEDED", "PARTIAL_SUCCESS", "CREATING", "DELETING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_substate(self):
        """
        Gets the lifecycle_substate of this ExecutionWindow.
        The current sub-state of the execution window. Valid states are DURATION_EXCEEDED, MAINTENANCE_IN_PROGRESS and WAITING.

        Allowed values for this property are: "DURATION_EXCEEDED", "MAINTENANCE_IN_PROGRESS", "WAITING", "RESCHEDULED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_substate of this ExecutionWindow.
        :rtype: str
        """
        return self._lifecycle_substate

    @lifecycle_substate.setter
    def lifecycle_substate(self, lifecycle_substate):
        """
        Sets the lifecycle_substate of this ExecutionWindow.
        The current sub-state of the execution window. Valid states are DURATION_EXCEEDED, MAINTENANCE_IN_PROGRESS and WAITING.


        :param lifecycle_substate: The lifecycle_substate of this ExecutionWindow.
        :type: str
        """
        allowed_values = ["DURATION_EXCEEDED", "MAINTENANCE_IN_PROGRESS", "WAITING", "RESCHEDULED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_substate, allowed_values):
            lifecycle_substate = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_substate = lifecycle_substate

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ExecutionWindow.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this ExecutionWindow.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ExecutionWindow.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this ExecutionWindow.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        Gets the time_created of this ExecutionWindow.
        The date and time the execution window was created.


        :return: The time_created of this ExecutionWindow.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ExecutionWindow.
        The date and time the execution window was created.


        :param time_created: The time_created of this ExecutionWindow.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ExecutionWindow.
        The last date and time that the execution window was updated.


        :return: The time_updated of this ExecutionWindow.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ExecutionWindow.
        The last date and time that the execution window was updated.


        :param time_updated: The time_updated of this ExecutionWindow.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_started(self):
        """
        Gets the time_started of this ExecutionWindow.
        The date and time that the execution window was started.


        :return: The time_started of this ExecutionWindow.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this ExecutionWindow.
        The date and time that the execution window was started.


        :param time_started: The time_started of this ExecutionWindow.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this ExecutionWindow.
        The date and time that the execution window ended.


        :return: The time_ended of this ExecutionWindow.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this ExecutionWindow.
        The date and time that the execution window ended.


        :param time_ended: The time_ended of this ExecutionWindow.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def time_scheduled(self):
        """
        **[Required]** Gets the time_scheduled of this ExecutionWindow.
        The scheduled start date and time of the execution window.


        :return: The time_scheduled of this ExecutionWindow.
        :rtype: datetime
        """
        return self._time_scheduled

    @time_scheduled.setter
    def time_scheduled(self, time_scheduled):
        """
        Sets the time_scheduled of this ExecutionWindow.
        The scheduled start date and time of the execution window.


        :param time_scheduled: The time_scheduled of this ExecutionWindow.
        :type: datetime
        """
        self._time_scheduled = time_scheduled

    @property
    def window_duration_in_mins(self):
        """
        **[Required]** Gets the window_duration_in_mins of this ExecutionWindow.
        Duration window allows user to set a duration they plan to allocate for Scheduling window. The duration is in minutes.


        :return: The window_duration_in_mins of this ExecutionWindow.
        :rtype: int
        """
        return self._window_duration_in_mins

    @window_duration_in_mins.setter
    def window_duration_in_mins(self, window_duration_in_mins):
        """
        Sets the window_duration_in_mins of this ExecutionWindow.
        Duration window allows user to set a duration they plan to allocate for Scheduling window. The duration is in minutes.


        :param window_duration_in_mins: The window_duration_in_mins of this ExecutionWindow.
        :type: int
        """
        self._window_duration_in_mins = window_duration_in_mins

    @property
    def is_enforced_duration(self):
        """
        Gets the is_enforced_duration of this ExecutionWindow.
        Indicates if duration the user plans to allocate for scheduling window is strictly enforced. The default value is `FALSE`.


        :return: The is_enforced_duration of this ExecutionWindow.
        :rtype: bool
        """
        return self._is_enforced_duration

    @is_enforced_duration.setter
    def is_enforced_duration(self, is_enforced_duration):
        """
        Sets the is_enforced_duration of this ExecutionWindow.
        Indicates if duration the user plans to allocate for scheduling window is strictly enforced. The default value is `FALSE`.


        :param is_enforced_duration: The is_enforced_duration of this ExecutionWindow.
        :type: bool
        """
        self._is_enforced_duration = is_enforced_duration

    @property
    def estimated_time_in_mins(self):
        """
        Gets the estimated_time_in_mins of this ExecutionWindow.
        The estimated time of the execution window in minutes.


        :return: The estimated_time_in_mins of this ExecutionWindow.
        :rtype: int
        """
        return self._estimated_time_in_mins

    @estimated_time_in_mins.setter
    def estimated_time_in_mins(self, estimated_time_in_mins):
        """
        Sets the estimated_time_in_mins of this ExecutionWindow.
        The estimated time of the execution window in minutes.


        :param estimated_time_in_mins: The estimated_time_in_mins of this ExecutionWindow.
        :type: int
        """
        self._estimated_time_in_mins = estimated_time_in_mins

    @property
    def total_time_taken_in_mins(self):
        """
        Gets the total_time_taken_in_mins of this ExecutionWindow.
        The total time taken by corresponding resource activity in minutes.


        :return: The total_time_taken_in_mins of this ExecutionWindow.
        :rtype: int
        """
        return self._total_time_taken_in_mins

    @total_time_taken_in_mins.setter
    def total_time_taken_in_mins(self, total_time_taken_in_mins):
        """
        Sets the total_time_taken_in_mins of this ExecutionWindow.
        The total time taken by corresponding resource activity in minutes.


        :param total_time_taken_in_mins: The total_time_taken_in_mins of this ExecutionWindow.
        :type: int
        """
        self._total_time_taken_in_mins = total_time_taken_in_mins

    @property
    def window_type(self):
        """
        Gets the window_type of this ExecutionWindow.
        The execution window is of PLANNED or UNPLANNED type.

        Allowed values for this property are: "PLANNED", "UNPLANNED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The window_type of this ExecutionWindow.
        :rtype: str
        """
        return self._window_type

    @window_type.setter
    def window_type(self, window_type):
        """
        Sets the window_type of this ExecutionWindow.
        The execution window is of PLANNED or UNPLANNED type.


        :param window_type: The window_type of this ExecutionWindow.
        :type: str
        """
        allowed_values = ["PLANNED", "UNPLANNED"]
        if not value_allowed_none_or_none_sentinel(window_type, allowed_values):
            window_type = 'UNKNOWN_ENUM_VALUE'
        self._window_type = window_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ExecutionWindow.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ExecutionWindow.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ExecutionWindow.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ExecutionWindow.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ExecutionWindow.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ExecutionWindow.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ExecutionWindow.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ExecutionWindow.
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
