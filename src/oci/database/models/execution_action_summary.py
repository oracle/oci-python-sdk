# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExecutionActionSummary(object):
    """
    Details of an execution action.
    """

    #: A constant which can be used with the lifecycle_state property of a ExecutionActionSummary.
    #: This constant has a value of "SCHEDULED"
    LIFECYCLE_STATE_SCHEDULED = "SCHEDULED"

    #: A constant which can be used with the lifecycle_state property of a ExecutionActionSummary.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a ExecutionActionSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a ExecutionActionSummary.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a ExecutionActionSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ExecutionActionSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ExecutionActionSummary.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a ExecutionActionSummary.
    #: This constant has a value of "PARTIAL_SUCCESS"
    LIFECYCLE_STATE_PARTIAL_SUCCESS = "PARTIAL_SUCCESS"

    #: A constant which can be used with the lifecycle_substate property of a ExecutionActionSummary.
    #: This constant has a value of "DURATION_EXCEEDED"
    LIFECYCLE_SUBSTATE_DURATION_EXCEEDED = "DURATION_EXCEEDED"

    #: A constant which can be used with the lifecycle_substate property of a ExecutionActionSummary.
    #: This constant has a value of "MAINTENANCE_IN_PROGRESS"
    LIFECYCLE_SUBSTATE_MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_substate property of a ExecutionActionSummary.
    #: This constant has a value of "WAITING"
    LIFECYCLE_SUBSTATE_WAITING = "WAITING"

    #: A constant which can be used with the lifecycle_substate property of a ExecutionActionSummary.
    #: This constant has a value of "RESCHEDULED"
    LIFECYCLE_SUBSTATE_RESCHEDULED = "RESCHEDULED"

    #: A constant which can be used with the action_type property of a ExecutionActionSummary.
    #: This constant has a value of "DB_SERVER_FULL_SOFTWARE_UPDATE"
    ACTION_TYPE_DB_SERVER_FULL_SOFTWARE_UPDATE = "DB_SERVER_FULL_SOFTWARE_UPDATE"

    #: A constant which can be used with the action_type property of a ExecutionActionSummary.
    #: This constant has a value of "STORAGE_SERVER_FULL_SOFTWARE_UPDATE"
    ACTION_TYPE_STORAGE_SERVER_FULL_SOFTWARE_UPDATE = "STORAGE_SERVER_FULL_SOFTWARE_UPDATE"

    #: A constant which can be used with the action_type property of a ExecutionActionSummary.
    #: This constant has a value of "NETWORK_SWITCH_FULL_SOFTWARE_UPDATE"
    ACTION_TYPE_NETWORK_SWITCH_FULL_SOFTWARE_UPDATE = "NETWORK_SWITCH_FULL_SOFTWARE_UPDATE"

    def __init__(self, **kwargs):
        """
        Initializes a new ExecutionActionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExecutionActionSummary.
        :type id: str

        :param execution_window_id:
            The value to assign to the execution_window_id property of this ExecutionActionSummary.
        :type execution_window_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExecutionActionSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ExecutionActionSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ExecutionActionSummary.
        :type description: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExecutionActionSummary.
            Allowed values for this property are: "SCHEDULED", "IN_PROGRESS", "FAILED", "CANCELED", "UPDATING", "DELETED", "SUCCEEDED", "PARTIAL_SUCCESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_substate:
            The value to assign to the lifecycle_substate property of this ExecutionActionSummary.
            Allowed values for this property are: "DURATION_EXCEEDED", "MAINTENANCE_IN_PROGRESS", "WAITING", "RESCHEDULED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_substate: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExecutionActionSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this ExecutionActionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ExecutionActionSummary.
        :type time_updated: datetime

        :param estimated_time_in_mins:
            The value to assign to the estimated_time_in_mins property of this ExecutionActionSummary.
        :type estimated_time_in_mins: int

        :param total_time_taken_in_mins:
            The value to assign to the total_time_taken_in_mins property of this ExecutionActionSummary.
        :type total_time_taken_in_mins: int

        :param execution_action_order:
            The value to assign to the execution_action_order property of this ExecutionActionSummary.
        :type execution_action_order: int

        :param action_type:
            The value to assign to the action_type property of this ExecutionActionSummary.
            Allowed values for this property are: "DB_SERVER_FULL_SOFTWARE_UPDATE", "STORAGE_SERVER_FULL_SOFTWARE_UPDATE", "NETWORK_SWITCH_FULL_SOFTWARE_UPDATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action_type: str

        :param action_params:
            The value to assign to the action_params property of this ExecutionActionSummary.
        :type action_params: dict(str, str)

        :param action_members:
            The value to assign to the action_members property of this ExecutionActionSummary.
        :type action_members: list[oci.database.models.ExecutionActionMember]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ExecutionActionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ExecutionActionSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'execution_window_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'lifecycle_state': 'str',
            'lifecycle_substate': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'estimated_time_in_mins': 'int',
            'total_time_taken_in_mins': 'int',
            'execution_action_order': 'int',
            'action_type': 'str',
            'action_params': 'dict(str, str)',
            'action_members': 'list[ExecutionActionMember]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'execution_window_id': 'executionWindowId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_substate': 'lifecycleSubstate',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'estimated_time_in_mins': 'estimatedTimeInMins',
            'total_time_taken_in_mins': 'totalTimeTakenInMins',
            'execution_action_order': 'executionActionOrder',
            'action_type': 'actionType',
            'action_params': 'actionParams',
            'action_members': 'actionMembers',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._execution_window_id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._lifecycle_state = None
        self._lifecycle_substate = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._estimated_time_in_mins = None
        self._total_time_taken_in_mins = None
        self._execution_action_order = None
        self._action_type = None
        self._action_params = None
        self._action_members = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExecutionActionSummary.
        The `OCID`__ of the execution action.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ExecutionActionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExecutionActionSummary.
        The `OCID`__ of the execution action.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExecutionActionSummary.
        :type: str
        """
        self._id = id

    @property
    def execution_window_id(self):
        """
        **[Required]** Gets the execution_window_id of this ExecutionActionSummary.
        The `OCID`__ of the execution window resource the execution action belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The execution_window_id of this ExecutionActionSummary.
        :rtype: str
        """
        return self._execution_window_id

    @execution_window_id.setter
    def execution_window_id(self, execution_window_id):
        """
        Sets the execution_window_id of this ExecutionActionSummary.
        The `OCID`__ of the execution window resource the execution action belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param execution_window_id: The execution_window_id of this ExecutionActionSummary.
        :type: str
        """
        self._execution_window_id = execution_window_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExecutionActionSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExecutionActionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExecutionActionSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExecutionActionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ExecutionActionSummary.
        The user-friendly name for the execution action. The name does not need to be unique.


        :return: The display_name of this ExecutionActionSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExecutionActionSummary.
        The user-friendly name for the execution action. The name does not need to be unique.


        :param display_name: The display_name of this ExecutionActionSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ExecutionActionSummary.
        Description of the execution action.


        :return: The description of this ExecutionActionSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ExecutionActionSummary.
        Description of the execution action.


        :param description: The description of this ExecutionActionSummary.
        :type: str
        """
        self._description = description

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ExecutionActionSummary.
        The current state of the execution action. Valid states are SCHEDULED, IN_PROGRESS, FAILED, CANCELED,
        UPDATING, DELETED, SUCCEEDED and PARTIAL_SUCCESS.

        Allowed values for this property are: "SCHEDULED", "IN_PROGRESS", "FAILED", "CANCELED", "UPDATING", "DELETED", "SUCCEEDED", "PARTIAL_SUCCESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ExecutionActionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ExecutionActionSummary.
        The current state of the execution action. Valid states are SCHEDULED, IN_PROGRESS, FAILED, CANCELED,
        UPDATING, DELETED, SUCCEEDED and PARTIAL_SUCCESS.


        :param lifecycle_state: The lifecycle_state of this ExecutionActionSummary.
        :type: str
        """
        allowed_values = ["SCHEDULED", "IN_PROGRESS", "FAILED", "CANCELED", "UPDATING", "DELETED", "SUCCEEDED", "PARTIAL_SUCCESS"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_substate(self):
        """
        Gets the lifecycle_substate of this ExecutionActionSummary.
        The current sub-state of the execution action. Valid states are DURATION_EXCEEDED, MAINTENANCE_IN_PROGRESS and WAITING.

        Allowed values for this property are: "DURATION_EXCEEDED", "MAINTENANCE_IN_PROGRESS", "WAITING", "RESCHEDULED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_substate of this ExecutionActionSummary.
        :rtype: str
        """
        return self._lifecycle_substate

    @lifecycle_substate.setter
    def lifecycle_substate(self, lifecycle_substate):
        """
        Sets the lifecycle_substate of this ExecutionActionSummary.
        The current sub-state of the execution action. Valid states are DURATION_EXCEEDED, MAINTENANCE_IN_PROGRESS and WAITING.


        :param lifecycle_substate: The lifecycle_substate of this ExecutionActionSummary.
        :type: str
        """
        allowed_values = ["DURATION_EXCEEDED", "MAINTENANCE_IN_PROGRESS", "WAITING", "RESCHEDULED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_substate, allowed_values):
            lifecycle_substate = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_substate = lifecycle_substate

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ExecutionActionSummary.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this ExecutionActionSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ExecutionActionSummary.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this ExecutionActionSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        Gets the time_created of this ExecutionActionSummary.
        The date and time the execution action was created.


        :return: The time_created of this ExecutionActionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ExecutionActionSummary.
        The date and time the execution action was created.


        :param time_created: The time_created of this ExecutionActionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ExecutionActionSummary.
        The last date and time that the execution action was updated.


        :return: The time_updated of this ExecutionActionSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ExecutionActionSummary.
        The last date and time that the execution action was updated.


        :param time_updated: The time_updated of this ExecutionActionSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def estimated_time_in_mins(self):
        """
        Gets the estimated_time_in_mins of this ExecutionActionSummary.
        The estimated time of the execution action in minutes.


        :return: The estimated_time_in_mins of this ExecutionActionSummary.
        :rtype: int
        """
        return self._estimated_time_in_mins

    @estimated_time_in_mins.setter
    def estimated_time_in_mins(self, estimated_time_in_mins):
        """
        Sets the estimated_time_in_mins of this ExecutionActionSummary.
        The estimated time of the execution action in minutes.


        :param estimated_time_in_mins: The estimated_time_in_mins of this ExecutionActionSummary.
        :type: int
        """
        self._estimated_time_in_mins = estimated_time_in_mins

    @property
    def total_time_taken_in_mins(self):
        """
        Gets the total_time_taken_in_mins of this ExecutionActionSummary.
        The total time taken by corresponding resource activity in minutes.


        :return: The total_time_taken_in_mins of this ExecutionActionSummary.
        :rtype: int
        """
        return self._total_time_taken_in_mins

    @total_time_taken_in_mins.setter
    def total_time_taken_in_mins(self, total_time_taken_in_mins):
        """
        Sets the total_time_taken_in_mins of this ExecutionActionSummary.
        The total time taken by corresponding resource activity in minutes.


        :param total_time_taken_in_mins: The total_time_taken_in_mins of this ExecutionActionSummary.
        :type: int
        """
        self._total_time_taken_in_mins = total_time_taken_in_mins

    @property
    def execution_action_order(self):
        """
        Gets the execution_action_order of this ExecutionActionSummary.
        The priority order of the execution action.


        :return: The execution_action_order of this ExecutionActionSummary.
        :rtype: int
        """
        return self._execution_action_order

    @execution_action_order.setter
    def execution_action_order(self, execution_action_order):
        """
        Sets the execution_action_order of this ExecutionActionSummary.
        The priority order of the execution action.


        :param execution_action_order: The execution_action_order of this ExecutionActionSummary.
        :type: int
        """
        self._execution_action_order = execution_action_order

    @property
    def action_type(self):
        """
        **[Required]** Gets the action_type of this ExecutionActionSummary.
        The action type of the execution action being performed

        Allowed values for this property are: "DB_SERVER_FULL_SOFTWARE_UPDATE", "STORAGE_SERVER_FULL_SOFTWARE_UPDATE", "NETWORK_SWITCH_FULL_SOFTWARE_UPDATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action_type of this ExecutionActionSummary.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """
        Sets the action_type of this ExecutionActionSummary.
        The action type of the execution action being performed


        :param action_type: The action_type of this ExecutionActionSummary.
        :type: str
        """
        allowed_values = ["DB_SERVER_FULL_SOFTWARE_UPDATE", "STORAGE_SERVER_FULL_SOFTWARE_UPDATE", "NETWORK_SWITCH_FULL_SOFTWARE_UPDATE"]
        if not value_allowed_none_or_none_sentinel(action_type, allowed_values):
            action_type = 'UNKNOWN_ENUM_VALUE'
        self._action_type = action_type

    @property
    def action_params(self):
        """
        **[Required]** Gets the action_params of this ExecutionActionSummary.
        Map<ParamName, ParamValue> where a key value pair describes the specific action parameter.
        Example: `{\"count\": \"3\"}`


        :return: The action_params of this ExecutionActionSummary.
        :rtype: dict(str, str)
        """
        return self._action_params

    @action_params.setter
    def action_params(self, action_params):
        """
        Sets the action_params of this ExecutionActionSummary.
        Map<ParamName, ParamValue> where a key value pair describes the specific action parameter.
        Example: `{\"count\": \"3\"}`


        :param action_params: The action_params of this ExecutionActionSummary.
        :type: dict(str, str)
        """
        self._action_params = action_params

    @property
    def action_members(self):
        """
        Gets the action_members of this ExecutionActionSummary.
        List of action members of this execution action.


        :return: The action_members of this ExecutionActionSummary.
        :rtype: list[oci.database.models.ExecutionActionMember]
        """
        return self._action_members

    @action_members.setter
    def action_members(self, action_members):
        """
        Sets the action_members of this ExecutionActionSummary.
        List of action members of this execution action.


        :param action_members: The action_members of this ExecutionActionSummary.
        :type: list[oci.database.models.ExecutionActionMember]
        """
        self._action_members = action_members

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ExecutionActionSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ExecutionActionSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ExecutionActionSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ExecutionActionSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ExecutionActionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ExecutionActionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ExecutionActionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ExecutionActionSummary.
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
