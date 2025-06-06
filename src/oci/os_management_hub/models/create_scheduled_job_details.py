# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateScheduledJobDetails(object):
    """
    Provides the information used to create a scheduled job.
    """

    #: A constant which can be used with the schedule_type property of a CreateScheduledJobDetails.
    #: This constant has a value of "ONETIME"
    SCHEDULE_TYPE_ONETIME = "ONETIME"

    #: A constant which can be used with the schedule_type property of a CreateScheduledJobDetails.
    #: This constant has a value of "RECURRING"
    SCHEDULE_TYPE_RECURRING = "RECURRING"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateScheduledJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateScheduledJobDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateScheduledJobDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateScheduledJobDetails.
        :type description: str

        :param schedule_type:
            The value to assign to the schedule_type property of this CreateScheduledJobDetails.
            Allowed values for this property are: "ONETIME", "RECURRING"
        :type schedule_type: str

        :param locations:
            The value to assign to the locations property of this CreateScheduledJobDetails.
        :type locations: list[oci.os_management_hub.models.ManagedInstanceLocation]

        :param time_next_execution:
            The value to assign to the time_next_execution property of this CreateScheduledJobDetails.
        :type time_next_execution: datetime

        :param recurring_rule:
            The value to assign to the recurring_rule property of this CreateScheduledJobDetails.
        :type recurring_rule: str

        :param managed_instance_ids:
            The value to assign to the managed_instance_ids property of this CreateScheduledJobDetails.
        :type managed_instance_ids: list[str]

        :param managed_instance_group_ids:
            The value to assign to the managed_instance_group_ids property of this CreateScheduledJobDetails.
        :type managed_instance_group_ids: list[str]

        :param managed_compartment_ids:
            The value to assign to the managed_compartment_ids property of this CreateScheduledJobDetails.
        :type managed_compartment_ids: list[str]

        :param lifecycle_stage_ids:
            The value to assign to the lifecycle_stage_ids property of this CreateScheduledJobDetails.
        :type lifecycle_stage_ids: list[str]

        :param is_subcompartment_included:
            The value to assign to the is_subcompartment_included property of this CreateScheduledJobDetails.
        :type is_subcompartment_included: bool

        :param operations:
            The value to assign to the operations property of this CreateScheduledJobDetails.
        :type operations: list[oci.os_management_hub.models.ScheduledJobOperation]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateScheduledJobDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateScheduledJobDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param retry_intervals:
            The value to assign to the retry_intervals property of this CreateScheduledJobDetails.
        :type retry_intervals: list[int]

        :param is_managed_by_autonomous_linux:
            The value to assign to the is_managed_by_autonomous_linux property of this CreateScheduledJobDetails.
        :type is_managed_by_autonomous_linux: bool

        :param work_request_id:
            The value to assign to the work_request_id property of this CreateScheduledJobDetails.
        :type work_request_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'schedule_type': 'str',
            'locations': 'list[ManagedInstanceLocation]',
            'time_next_execution': 'datetime',
            'recurring_rule': 'str',
            'managed_instance_ids': 'list[str]',
            'managed_instance_group_ids': 'list[str]',
            'managed_compartment_ids': 'list[str]',
            'lifecycle_stage_ids': 'list[str]',
            'is_subcompartment_included': 'bool',
            'operations': 'list[ScheduledJobOperation]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'retry_intervals': 'list[int]',
            'is_managed_by_autonomous_linux': 'bool',
            'work_request_id': 'str'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'schedule_type': 'scheduleType',
            'locations': 'locations',
            'time_next_execution': 'timeNextExecution',
            'recurring_rule': 'recurringRule',
            'managed_instance_ids': 'managedInstanceIds',
            'managed_instance_group_ids': 'managedInstanceGroupIds',
            'managed_compartment_ids': 'managedCompartmentIds',
            'lifecycle_stage_ids': 'lifecycleStageIds',
            'is_subcompartment_included': 'isSubcompartmentIncluded',
            'operations': 'operations',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'retry_intervals': 'retryIntervals',
            'is_managed_by_autonomous_linux': 'isManagedByAutonomousLinux',
            'work_request_id': 'workRequestId'
        }
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._schedule_type = None
        self._locations = None
        self._time_next_execution = None
        self._recurring_rule = None
        self._managed_instance_ids = None
        self._managed_instance_group_ids = None
        self._managed_compartment_ids = None
        self._lifecycle_stage_ids = None
        self._is_subcompartment_included = None
        self._operations = None
        self._freeform_tags = None
        self._defined_tags = None
        self._retry_intervals = None
        self._is_managed_by_autonomous_linux = None
        self._work_request_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateScheduledJobDetails.
        The `OCID`__ of the compartment that contains the scheduled job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateScheduledJobDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateScheduledJobDetails.
        The `OCID`__ of the compartment that contains the scheduled job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateScheduledJobDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateScheduledJobDetails.
        User-friendly name for the scheduled job. Does not have to be unique and you can change the name later. Avoid entering confidential information.


        :return: The display_name of this CreateScheduledJobDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateScheduledJobDetails.
        User-friendly name for the scheduled job. Does not have to be unique and you can change the name later. Avoid entering confidential information.


        :param display_name: The display_name of this CreateScheduledJobDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateScheduledJobDetails.
        User-specified description of the scheduled job. Avoid entering confidential information.


        :return: The description of this CreateScheduledJobDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateScheduledJobDetails.
        User-specified description of the scheduled job. Avoid entering confidential information.


        :param description: The description of this CreateScheduledJobDetails.
        :type: str
        """
        self._description = description

    @property
    def schedule_type(self):
        """
        **[Required]** Gets the schedule_type of this CreateScheduledJobDetails.
        The type of scheduling frequency for the scheduled job.

        Allowed values for this property are: "ONETIME", "RECURRING"


        :return: The schedule_type of this CreateScheduledJobDetails.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """
        Sets the schedule_type of this CreateScheduledJobDetails.
        The type of scheduling frequency for the scheduled job.


        :param schedule_type: The schedule_type of this CreateScheduledJobDetails.
        :type: str
        """
        allowed_values = ["ONETIME", "RECURRING"]
        if not value_allowed_none_or_none_sentinel(schedule_type, allowed_values):
            raise ValueError(
                f"Invalid value for `schedule_type`, must be None or one of {allowed_values}"
            )
        self._schedule_type = schedule_type

    @property
    def locations(self):
        """
        Gets the locations of this CreateScheduledJobDetails.
        The list of locations this scheduled job should operate on for a job targeting on compartments. (Empty list means apply to all locations). This can only be set when managedCompartmentIds is not empty.


        :return: The locations of this CreateScheduledJobDetails.
        :rtype: list[oci.os_management_hub.models.ManagedInstanceLocation]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """
        Sets the locations of this CreateScheduledJobDetails.
        The list of locations this scheduled job should operate on for a job targeting on compartments. (Empty list means apply to all locations). This can only be set when managedCompartmentIds is not empty.


        :param locations: The locations of this CreateScheduledJobDetails.
        :type: list[oci.os_management_hub.models.ManagedInstanceLocation]
        """
        self._locations = locations

    @property
    def time_next_execution(self):
        """
        **[Required]** Gets the time_next_execution of this CreateScheduledJobDetails.
        The desired time of the next execution of this scheduled job (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_next_execution of this CreateScheduledJobDetails.
        :rtype: datetime
        """
        return self._time_next_execution

    @time_next_execution.setter
    def time_next_execution(self, time_next_execution):
        """
        Sets the time_next_execution of this CreateScheduledJobDetails.
        The desired time of the next execution of this scheduled job (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_next_execution: The time_next_execution of this CreateScheduledJobDetails.
        :type: datetime
        """
        self._time_next_execution = time_next_execution

    @property
    def recurring_rule(self):
        """
        Gets the recurring_rule of this CreateScheduledJobDetails.
        The frequency schedule for a recurring scheduled job.


        :return: The recurring_rule of this CreateScheduledJobDetails.
        :rtype: str
        """
        return self._recurring_rule

    @recurring_rule.setter
    def recurring_rule(self, recurring_rule):
        """
        Sets the recurring_rule of this CreateScheduledJobDetails.
        The frequency schedule for a recurring scheduled job.


        :param recurring_rule: The recurring_rule of this CreateScheduledJobDetails.
        :type: str
        """
        self._recurring_rule = recurring_rule

    @property
    def managed_instance_ids(self):
        """
        Gets the managed_instance_ids of this CreateScheduledJobDetails.
        The managed instance `OCIDs`__ that this scheduled job operates on.
        A scheduled job can only operate on one type of target, therefore you must supply either this or
        managedInstanceGroupIds, or managedCompartmentIds, or lifecycleStageIds.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The managed_instance_ids of this CreateScheduledJobDetails.
        :rtype: list[str]
        """
        return self._managed_instance_ids

    @managed_instance_ids.setter
    def managed_instance_ids(self, managed_instance_ids):
        """
        Sets the managed_instance_ids of this CreateScheduledJobDetails.
        The managed instance `OCIDs`__ that this scheduled job operates on.
        A scheduled job can only operate on one type of target, therefore you must supply either this or
        managedInstanceGroupIds, or managedCompartmentIds, or lifecycleStageIds.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param managed_instance_ids: The managed_instance_ids of this CreateScheduledJobDetails.
        :type: list[str]
        """
        self._managed_instance_ids = managed_instance_ids

    @property
    def managed_instance_group_ids(self):
        """
        Gets the managed_instance_group_ids of this CreateScheduledJobDetails.
        The managed instance group `OCIDs`__ that this scheduled job operates on.
        A scheduled job can only operate on one type of target, therefore you must supply either this or managedInstanceIds,
        or managedCompartmentIds, or lifecycleStageIds.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The managed_instance_group_ids of this CreateScheduledJobDetails.
        :rtype: list[str]
        """
        return self._managed_instance_group_ids

    @managed_instance_group_ids.setter
    def managed_instance_group_ids(self, managed_instance_group_ids):
        """
        Sets the managed_instance_group_ids of this CreateScheduledJobDetails.
        The managed instance group `OCIDs`__ that this scheduled job operates on.
        A scheduled job can only operate on one type of target, therefore you must supply either this or managedInstanceIds,
        or managedCompartmentIds, or lifecycleStageIds.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param managed_instance_group_ids: The managed_instance_group_ids of this CreateScheduledJobDetails.
        :type: list[str]
        """
        self._managed_instance_group_ids = managed_instance_group_ids

    @property
    def managed_compartment_ids(self):
        """
        Gets the managed_compartment_ids of this CreateScheduledJobDetails.
        The compartment `OCIDs`__ that this scheduled job operates on.
        To apply the job to all compartments in the tenancy, set this to the tenancy OCID (root compartment) and set
        isSubcompartmentIncluded to true. A scheduled job can only operate on one type of target, therefore you must
        supply either this or managedInstanceIds, or managedInstanceGroupIds, or lifecycleStageIds.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The managed_compartment_ids of this CreateScheduledJobDetails.
        :rtype: list[str]
        """
        return self._managed_compartment_ids

    @managed_compartment_ids.setter
    def managed_compartment_ids(self, managed_compartment_ids):
        """
        Sets the managed_compartment_ids of this CreateScheduledJobDetails.
        The compartment `OCIDs`__ that this scheduled job operates on.
        To apply the job to all compartments in the tenancy, set this to the tenancy OCID (root compartment) and set
        isSubcompartmentIncluded to true. A scheduled job can only operate on one type of target, therefore you must
        supply either this or managedInstanceIds, or managedInstanceGroupIds, or lifecycleStageIds.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param managed_compartment_ids: The managed_compartment_ids of this CreateScheduledJobDetails.
        :type: list[str]
        """
        self._managed_compartment_ids = managed_compartment_ids

    @property
    def lifecycle_stage_ids(self):
        """
        Gets the lifecycle_stage_ids of this CreateScheduledJobDetails.
        The lifecycle stage `OCIDs`__ that this scheduled job operates on.
        A scheduled job can only operate on one type of target, therefore you must supply either this or managedInstanceIds,
        or managedInstanceGroupIds, or managedCompartmentIds.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The lifecycle_stage_ids of this CreateScheduledJobDetails.
        :rtype: list[str]
        """
        return self._lifecycle_stage_ids

    @lifecycle_stage_ids.setter
    def lifecycle_stage_ids(self, lifecycle_stage_ids):
        """
        Sets the lifecycle_stage_ids of this CreateScheduledJobDetails.
        The lifecycle stage `OCIDs`__ that this scheduled job operates on.
        A scheduled job can only operate on one type of target, therefore you must supply either this or managedInstanceIds,
        or managedInstanceGroupIds, or managedCompartmentIds.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param lifecycle_stage_ids: The lifecycle_stage_ids of this CreateScheduledJobDetails.
        :type: list[str]
        """
        self._lifecycle_stage_ids = lifecycle_stage_ids

    @property
    def is_subcompartment_included(self):
        """
        Gets the is_subcompartment_included of this CreateScheduledJobDetails.
        Indicates whether to apply the scheduled job to all compartments in the tenancy when managedCompartmentIds specifies
        the tenancy `OCID`__ (root compartment).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The is_subcompartment_included of this CreateScheduledJobDetails.
        :rtype: bool
        """
        return self._is_subcompartment_included

    @is_subcompartment_included.setter
    def is_subcompartment_included(self, is_subcompartment_included):
        """
        Sets the is_subcompartment_included of this CreateScheduledJobDetails.
        Indicates whether to apply the scheduled job to all compartments in the tenancy when managedCompartmentIds specifies
        the tenancy `OCID`__ (root compartment).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param is_subcompartment_included: The is_subcompartment_included of this CreateScheduledJobDetails.
        :type: bool
        """
        self._is_subcompartment_included = is_subcompartment_included

    @property
    def operations(self):
        """
        **[Required]** Gets the operations of this CreateScheduledJobDetails.
        The list of operations this scheduled job needs to perform.
        A scheduled job supports only one operation type, unless it is one of the following:
        * UPDATE_PACKAGES
        * UPDATE_ALL
        * UPDATE_SECURITY
        * UPDATE_BUGFIX
        * UPDATE_ENHANCEMENT
        * UPDATE_OTHER
        * UPDATE_KSPLICE_USERSPACE
        * UPDATE_KSPLICE_KERNEL


        :return: The operations of this CreateScheduledJobDetails.
        :rtype: list[oci.os_management_hub.models.ScheduledJobOperation]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """
        Sets the operations of this CreateScheduledJobDetails.
        The list of operations this scheduled job needs to perform.
        A scheduled job supports only one operation type, unless it is one of the following:
        * UPDATE_PACKAGES
        * UPDATE_ALL
        * UPDATE_SECURITY
        * UPDATE_BUGFIX
        * UPDATE_ENHANCEMENT
        * UPDATE_OTHER
        * UPDATE_KSPLICE_USERSPACE
        * UPDATE_KSPLICE_KERNEL


        :param operations: The operations of this CreateScheduledJobDetails.
        :type: list[oci.os_management_hub.models.ScheduledJobOperation]
        """
        self._operations = operations

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateScheduledJobDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateScheduledJobDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateScheduledJobDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateScheduledJobDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateScheduledJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateScheduledJobDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateScheduledJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateScheduledJobDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def retry_intervals(self):
        """
        Gets the retry_intervals of this CreateScheduledJobDetails.
        The amount of time in minutes to wait until retrying the scheduled job. If set, the service will automatically
        retry a failed scheduled job after the interval. For example, you could set the interval to [2,5,10]. If the
        initial execution of the job fails, the service waits 2 minutes and then retries. If that fails, the service
        waits 5 minutes and then retries. If that fails, the service waits 10 minutes and then retries.


        :return: The retry_intervals of this CreateScheduledJobDetails.
        :rtype: list[int]
        """
        return self._retry_intervals

    @retry_intervals.setter
    def retry_intervals(self, retry_intervals):
        """
        Sets the retry_intervals of this CreateScheduledJobDetails.
        The amount of time in minutes to wait until retrying the scheduled job. If set, the service will automatically
        retry a failed scheduled job after the interval. For example, you could set the interval to [2,5,10]. If the
        initial execution of the job fails, the service waits 2 minutes and then retries. If that fails, the service
        waits 5 minutes and then retries. If that fails, the service waits 10 minutes and then retries.


        :param retry_intervals: The retry_intervals of this CreateScheduledJobDetails.
        :type: list[int]
        """
        self._retry_intervals = retry_intervals

    @property
    def is_managed_by_autonomous_linux(self):
        """
        Gets the is_managed_by_autonomous_linux of this CreateScheduledJobDetails.
        Indicates whether this scheduled job is managed by the Autonomous Linux service.


        :return: The is_managed_by_autonomous_linux of this CreateScheduledJobDetails.
        :rtype: bool
        """
        return self._is_managed_by_autonomous_linux

    @is_managed_by_autonomous_linux.setter
    def is_managed_by_autonomous_linux(self, is_managed_by_autonomous_linux):
        """
        Sets the is_managed_by_autonomous_linux of this CreateScheduledJobDetails.
        Indicates whether this scheduled job is managed by the Autonomous Linux service.


        :param is_managed_by_autonomous_linux: The is_managed_by_autonomous_linux of this CreateScheduledJobDetails.
        :type: bool
        """
        self._is_managed_by_autonomous_linux = is_managed_by_autonomous_linux

    @property
    def work_request_id(self):
        """
        Gets the work_request_id of this CreateScheduledJobDetails.
        The `OCID`__ for the work request that will be rerun.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The work_request_id of this CreateScheduledJobDetails.
        :rtype: str
        """
        return self._work_request_id

    @work_request_id.setter
    def work_request_id(self, work_request_id):
        """
        Sets the work_request_id of this CreateScheduledJobDetails.
        The `OCID`__ for the work request that will be rerun.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param work_request_id: The work_request_id of this CreateScheduledJobDetails.
        :type: str
        """
        self._work_request_id = work_request_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
