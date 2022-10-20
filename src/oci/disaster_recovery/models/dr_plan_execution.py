# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrPlanExecution(object):
    """
    The details of a DR Plan Execution.
    """

    #: A constant which can be used with the plan_execution_type property of a DrPlanExecution.
    #: This constant has a value of "SWITCHOVER"
    PLAN_EXECUTION_TYPE_SWITCHOVER = "SWITCHOVER"

    #: A constant which can be used with the plan_execution_type property of a DrPlanExecution.
    #: This constant has a value of "SWITCHOVER_PRECHECK"
    PLAN_EXECUTION_TYPE_SWITCHOVER_PRECHECK = "SWITCHOVER_PRECHECK"

    #: A constant which can be used with the plan_execution_type property of a DrPlanExecution.
    #: This constant has a value of "FAILOVER"
    PLAN_EXECUTION_TYPE_FAILOVER = "FAILOVER"

    #: A constant which can be used with the plan_execution_type property of a DrPlanExecution.
    #: This constant has a value of "FAILOVER_PRECHECK"
    PLAN_EXECUTION_TYPE_FAILOVER_PRECHECK = "FAILOVER_PRECHECK"

    #: A constant which can be used with the lifecycle_state property of a DrPlanExecution.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a DrPlanExecution.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a DrPlanExecution.
    #: This constant has a value of "WAITING"
    LIFECYCLE_STATE_WAITING = "WAITING"

    #: A constant which can be used with the lifecycle_state property of a DrPlanExecution.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a DrPlanExecution.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a DrPlanExecution.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a DrPlanExecution.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a DrPlanExecution.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DrPlanExecution.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DrPlanExecution.
    #: This constant has a value of "PAUSING"
    LIFECYCLE_STATE_PAUSING = "PAUSING"

    #: A constant which can be used with the lifecycle_state property of a DrPlanExecution.
    #: This constant has a value of "PAUSED"
    LIFECYCLE_STATE_PAUSED = "PAUSED"

    #: A constant which can be used with the lifecycle_state property of a DrPlanExecution.
    #: This constant has a value of "RESUMING"
    LIFECYCLE_STATE_RESUMING = "RESUMING"

    def __init__(self, **kwargs):
        """
        Initializes a new DrPlanExecution object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DrPlanExecution.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DrPlanExecution.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this DrPlanExecution.
        :type display_name: str

        :param plan_id:
            The value to assign to the plan_id property of this DrPlanExecution.
        :type plan_id: str

        :param plan_execution_type:
            The value to assign to the plan_execution_type property of this DrPlanExecution.
            Allowed values for this property are: "SWITCHOVER", "SWITCHOVER_PRECHECK", "FAILOVER", "FAILOVER_PRECHECK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type plan_execution_type: str

        :param execution_options:
            The value to assign to the execution_options property of this DrPlanExecution.
        :type execution_options: oci.disaster_recovery.models.DrPlanExecutionOptions

        :param dr_protection_group_id:
            The value to assign to the dr_protection_group_id property of this DrPlanExecution.
        :type dr_protection_group_id: str

        :param peer_dr_protection_group_id:
            The value to assign to the peer_dr_protection_group_id property of this DrPlanExecution.
        :type peer_dr_protection_group_id: str

        :param peer_region:
            The value to assign to the peer_region property of this DrPlanExecution.
        :type peer_region: str

        :param log_location:
            The value to assign to the log_location property of this DrPlanExecution.
        :type log_location: oci.disaster_recovery.models.ObjectStorageLogLocation

        :param time_created:
            The value to assign to the time_created property of this DrPlanExecution.
        :type time_created: datetime

        :param time_started:
            The value to assign to the time_started property of this DrPlanExecution.
        :type time_started: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DrPlanExecution.
        :type time_updated: datetime

        :param time_ended:
            The value to assign to the time_ended property of this DrPlanExecution.
        :type time_ended: datetime

        :param execution_duration_in_sec:
            The value to assign to the execution_duration_in_sec property of this DrPlanExecution.
        :type execution_duration_in_sec: int

        :param group_executions:
            The value to assign to the group_executions property of this DrPlanExecution.
        :type group_executions: list[oci.disaster_recovery.models.DrPlanGroupExecution]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DrPlanExecution.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "DELETING", "DELETED", "PAUSING", "PAUSED", "RESUMING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param life_cycle_details:
            The value to assign to the life_cycle_details property of this DrPlanExecution.
        :type life_cycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DrPlanExecution.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DrPlanExecution.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DrPlanExecution.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'plan_id': 'str',
            'plan_execution_type': 'str',
            'execution_options': 'DrPlanExecutionOptions',
            'dr_protection_group_id': 'str',
            'peer_dr_protection_group_id': 'str',
            'peer_region': 'str',
            'log_location': 'ObjectStorageLogLocation',
            'time_created': 'datetime',
            'time_started': 'datetime',
            'time_updated': 'datetime',
            'time_ended': 'datetime',
            'execution_duration_in_sec': 'int',
            'group_executions': 'list[DrPlanGroupExecution]',
            'lifecycle_state': 'str',
            'life_cycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'plan_id': 'planId',
            'plan_execution_type': 'planExecutionType',
            'execution_options': 'executionOptions',
            'dr_protection_group_id': 'drProtectionGroupId',
            'peer_dr_protection_group_id': 'peerDrProtectionGroupId',
            'peer_region': 'peerRegion',
            'log_location': 'logLocation',
            'time_created': 'timeCreated',
            'time_started': 'timeStarted',
            'time_updated': 'timeUpdated',
            'time_ended': 'timeEnded',
            'execution_duration_in_sec': 'executionDurationInSec',
            'group_executions': 'groupExecutions',
            'lifecycle_state': 'lifecycleState',
            'life_cycle_details': 'lifeCycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._plan_id = None
        self._plan_execution_type = None
        self._execution_options = None
        self._dr_protection_group_id = None
        self._peer_dr_protection_group_id = None
        self._peer_region = None
        self._log_location = None
        self._time_created = None
        self._time_started = None
        self._time_updated = None
        self._time_ended = None
        self._execution_duration_in_sec = None
        self._group_executions = None
        self._lifecycle_state = None
        self._life_cycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DrPlanExecution.
        The OCID of the DR Plan Execution.

        Example: `ocid1.drplanexecution.oc1.iad.exampleocid2`


        :return: The id of this DrPlanExecution.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DrPlanExecution.
        The OCID of the DR Plan Execution.

        Example: `ocid1.drplanexecution.oc1.iad.exampleocid2`


        :param id: The id of this DrPlanExecution.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DrPlanExecution.
        The OCID of the compartment containing this DR Plan Execution.

        Example: `ocid1.compartment.oc1..exampleocid1`


        :return: The compartment_id of this DrPlanExecution.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DrPlanExecution.
        The OCID of the compartment containing this DR Plan Execution.

        Example: `ocid1.compartment.oc1..exampleocid1`


        :param compartment_id: The compartment_id of this DrPlanExecution.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DrPlanExecution.
        The display name of this DR Plan Execution.

        Example: `Execution - EBS Switchover PHX to IAD`


        :return: The display_name of this DrPlanExecution.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DrPlanExecution.
        The display name of this DR Plan Execution.

        Example: `Execution - EBS Switchover PHX to IAD`


        :param display_name: The display_name of this DrPlanExecution.
        :type: str
        """
        self._display_name = display_name

    @property
    def plan_id(self):
        """
        **[Required]** Gets the plan_id of this DrPlanExecution.
        The OCID of the DR Plan.

        Example: `ocid1.drplan.oc1.iad.exampleocid2`


        :return: The plan_id of this DrPlanExecution.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """
        Sets the plan_id of this DrPlanExecution.
        The OCID of the DR Plan.

        Example: `ocid1.drplan.oc1.iad.exampleocid2`


        :param plan_id: The plan_id of this DrPlanExecution.
        :type: str
        """
        self._plan_id = plan_id

    @property
    def plan_execution_type(self):
        """
        **[Required]** Gets the plan_execution_type of this DrPlanExecution.
        The type of the DR Plan executed.

        Allowed values for this property are: "SWITCHOVER", "SWITCHOVER_PRECHECK", "FAILOVER", "FAILOVER_PRECHECK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The plan_execution_type of this DrPlanExecution.
        :rtype: str
        """
        return self._plan_execution_type

    @plan_execution_type.setter
    def plan_execution_type(self, plan_execution_type):
        """
        Sets the plan_execution_type of this DrPlanExecution.
        The type of the DR Plan executed.


        :param plan_execution_type: The plan_execution_type of this DrPlanExecution.
        :type: str
        """
        allowed_values = ["SWITCHOVER", "SWITCHOVER_PRECHECK", "FAILOVER", "FAILOVER_PRECHECK"]
        if not value_allowed_none_or_none_sentinel(plan_execution_type, allowed_values):
            plan_execution_type = 'UNKNOWN_ENUM_VALUE'
        self._plan_execution_type = plan_execution_type

    @property
    def execution_options(self):
        """
        **[Required]** Gets the execution_options of this DrPlanExecution.

        :return: The execution_options of this DrPlanExecution.
        :rtype: oci.disaster_recovery.models.DrPlanExecutionOptions
        """
        return self._execution_options

    @execution_options.setter
    def execution_options(self, execution_options):
        """
        Sets the execution_options of this DrPlanExecution.

        :param execution_options: The execution_options of this DrPlanExecution.
        :type: oci.disaster_recovery.models.DrPlanExecutionOptions
        """
        self._execution_options = execution_options

    @property
    def dr_protection_group_id(self):
        """
        **[Required]** Gets the dr_protection_group_id of this DrPlanExecution.
        The OCID of the DR Protection Group to which this DR Plan Execution belongs.

        Example: `ocid1.drprotectiongroup.oc1.iad.exampleocid2`


        :return: The dr_protection_group_id of this DrPlanExecution.
        :rtype: str
        """
        return self._dr_protection_group_id

    @dr_protection_group_id.setter
    def dr_protection_group_id(self, dr_protection_group_id):
        """
        Sets the dr_protection_group_id of this DrPlanExecution.
        The OCID of the DR Protection Group to which this DR Plan Execution belongs.

        Example: `ocid1.drprotectiongroup.oc1.iad.exampleocid2`


        :param dr_protection_group_id: The dr_protection_group_id of this DrPlanExecution.
        :type: str
        """
        self._dr_protection_group_id = dr_protection_group_id

    @property
    def peer_dr_protection_group_id(self):
        """
        **[Required]** Gets the peer_dr_protection_group_id of this DrPlanExecution.
        The OCID of peer (remote) DR Protection Group associated with this plan's
        DR Protection Group.

        Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid1`


        :return: The peer_dr_protection_group_id of this DrPlanExecution.
        :rtype: str
        """
        return self._peer_dr_protection_group_id

    @peer_dr_protection_group_id.setter
    def peer_dr_protection_group_id(self, peer_dr_protection_group_id):
        """
        Sets the peer_dr_protection_group_id of this DrPlanExecution.
        The OCID of peer (remote) DR Protection Group associated with this plan's
        DR Protection Group.

        Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid1`


        :param peer_dr_protection_group_id: The peer_dr_protection_group_id of this DrPlanExecution.
        :type: str
        """
        self._peer_dr_protection_group_id = peer_dr_protection_group_id

    @property
    def peer_region(self):
        """
        **[Required]** Gets the peer_region of this DrPlanExecution.
        The region of the peer (remote) DR Protection Group.

        Example: `us-ashburn-1`


        :return: The peer_region of this DrPlanExecution.
        :rtype: str
        """
        return self._peer_region

    @peer_region.setter
    def peer_region(self, peer_region):
        """
        Sets the peer_region of this DrPlanExecution.
        The region of the peer (remote) DR Protection Group.

        Example: `us-ashburn-1`


        :param peer_region: The peer_region of this DrPlanExecution.
        :type: str
        """
        self._peer_region = peer_region

    @property
    def log_location(self):
        """
        **[Required]** Gets the log_location of this DrPlanExecution.

        :return: The log_location of this DrPlanExecution.
        :rtype: oci.disaster_recovery.models.ObjectStorageLogLocation
        """
        return self._log_location

    @log_location.setter
    def log_location(self, log_location):
        """
        Sets the log_location of this DrPlanExecution.

        :param log_location: The log_location of this DrPlanExecution.
        :type: oci.disaster_recovery.models.ObjectStorageLogLocation
        """
        self._log_location = log_location

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DrPlanExecution.
        The date and time at which DR Plan Execution was created. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :return: The time_created of this DrPlanExecution.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DrPlanExecution.
        The date and time at which DR Plan Execution was created. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :param time_created: The time_created of this DrPlanExecution.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_started(self):
        """
        Gets the time_started of this DrPlanExecution.
        The date and time at which DR Plan Execution began. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :return: The time_started of this DrPlanExecution.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this DrPlanExecution.
        The date and time at which DR Plan Execution began. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :param time_started: The time_started of this DrPlanExecution.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this DrPlanExecution.
        The time at which DR Plan Execution was last updated. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :return: The time_updated of this DrPlanExecution.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DrPlanExecution.
        The time at which DR Plan Execution was last updated. An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :param time_updated: The time_updated of this DrPlanExecution.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_ended(self):
        """
        Gets the time_ended of this DrPlanExecution.
        The date and time at which DR Plan Execution succeeded, failed, was paused, or was canceled.
        An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :return: The time_ended of this DrPlanExecution.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this DrPlanExecution.
        The date and time at which DR Plan Execution succeeded, failed, was paused, or was canceled.
        An RFC3339 formatted datetime string.

        Example: `2019-03-29T09:36:42Z`


        :param time_ended: The time_ended of this DrPlanExecution.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def execution_duration_in_sec(self):
        """
        Gets the execution_duration_in_sec of this DrPlanExecution.
        The total duration in seconds taken to complete the DR Plan Execution.

        Example: `750`


        :return: The execution_duration_in_sec of this DrPlanExecution.
        :rtype: int
        """
        return self._execution_duration_in_sec

    @execution_duration_in_sec.setter
    def execution_duration_in_sec(self, execution_duration_in_sec):
        """
        Sets the execution_duration_in_sec of this DrPlanExecution.
        The total duration in seconds taken to complete the DR Plan Execution.

        Example: `750`


        :param execution_duration_in_sec: The execution_duration_in_sec of this DrPlanExecution.
        :type: int
        """
        self._execution_duration_in_sec = execution_duration_in_sec

    @property
    def group_executions(self):
        """
        **[Required]** Gets the group_executions of this DrPlanExecution.
        A list of groups executed in this DR Plan Execution.


        :return: The group_executions of this DrPlanExecution.
        :rtype: list[oci.disaster_recovery.models.DrPlanGroupExecution]
        """
        return self._group_executions

    @group_executions.setter
    def group_executions(self, group_executions):
        """
        Sets the group_executions of this DrPlanExecution.
        A list of groups executed in this DR Plan Execution.


        :param group_executions: The group_executions of this DrPlanExecution.
        :type: list[oci.disaster_recovery.models.DrPlanGroupExecution]
        """
        self._group_executions = group_executions

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DrPlanExecution.
        The current state of the DR Plan Execution.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "DELETING", "DELETED", "PAUSING", "PAUSED", "RESUMING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DrPlanExecution.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DrPlanExecution.
        The current state of the DR Plan Execution.


        :param lifecycle_state: The lifecycle_state of this DrPlanExecution.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "DELETING", "DELETED", "PAUSING", "PAUSED", "RESUMING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def life_cycle_details(self):
        """
        Gets the life_cycle_details of this DrPlanExecution.
        A message describing the DR Plan Execution's current state in more detail.

        Example: `The DR Plan Execution [Execution - EBS Switchover PHX to IAD] is currently in progress`


        :return: The life_cycle_details of this DrPlanExecution.
        :rtype: str
        """
        return self._life_cycle_details

    @life_cycle_details.setter
    def life_cycle_details(self, life_cycle_details):
        """
        Sets the life_cycle_details of this DrPlanExecution.
        A message describing the DR Plan Execution's current state in more detail.

        Example: `The DR Plan Execution [Execution - EBS Switchover PHX to IAD] is currently in progress`


        :param life_cycle_details: The life_cycle_details of this DrPlanExecution.
        :type: str
        """
        self._life_cycle_details = life_cycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DrPlanExecution.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"Department\": \"Finance\"}`


        :return: The freeform_tags of this DrPlanExecution.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DrPlanExecution.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"Department\": \"Finance\"}`


        :param freeform_tags: The freeform_tags of this DrPlanExecution.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DrPlanExecution.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :return: The defined_tags of this DrPlanExecution.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DrPlanExecution.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :param defined_tags: The defined_tags of this DrPlanExecution.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DrPlanExecution.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this DrPlanExecution.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DrPlanExecution.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this DrPlanExecution.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
