# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobSummary(object):
    """
    Returns a listing of all of the specified job's properties and their values.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JobSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this JobSummary.
        :type id: str

        :param stack_id:
            The value to assign to the stack_id property of this JobSummary.
        :type stack_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this JobSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this JobSummary.
        :type display_name: str

        :param operation:
            The value to assign to the operation property of this JobSummary.
        :type operation: str

        :param job_operation_details:
            The value to assign to the job_operation_details property of this JobSummary.
        :type job_operation_details: oci.resource_manager.models.JobOperationDetailsSummary

        :param apply_job_plan_resolution:
            The value to assign to the apply_job_plan_resolution property of this JobSummary.
        :type apply_job_plan_resolution: oci.resource_manager.models.ApplyJobPlanResolution

        :param resolved_plan_job_id:
            The value to assign to the resolved_plan_job_id property of this JobSummary.
        :type resolved_plan_job_id: str

        :param time_created:
            The value to assign to the time_created property of this JobSummary.
        :type time_created: datetime

        :param time_finished:
            The value to assign to the time_finished property of this JobSummary.
        :type time_finished: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this JobSummary.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this JobSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this JobSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'stack_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'operation': 'str',
            'job_operation_details': 'JobOperationDetailsSummary',
            'apply_job_plan_resolution': 'ApplyJobPlanResolution',
            'resolved_plan_job_id': 'str',
            'time_created': 'datetime',
            'time_finished': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'stack_id': 'stackId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'operation': 'operation',
            'job_operation_details': 'jobOperationDetails',
            'apply_job_plan_resolution': 'applyJobPlanResolution',
            'resolved_plan_job_id': 'resolvedPlanJobId',
            'time_created': 'timeCreated',
            'time_finished': 'timeFinished',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._stack_id = None
        self._compartment_id = None
        self._display_name = None
        self._operation = None
        self._job_operation_details = None
        self._apply_job_plan_resolution = None
        self._resolved_plan_job_id = None
        self._time_created = None
        self._time_finished = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this JobSummary.
        The `OCID`__ of the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this JobSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this JobSummary.
        The `OCID`__ of the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this JobSummary.
        :type: str
        """
        self._id = id

    @property
    def stack_id(self):
        """
        Gets the stack_id of this JobSummary.
        The `OCID`__ of the stack that is associated with the specified job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The stack_id of this JobSummary.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """
        Sets the stack_id of this JobSummary.
        The `OCID`__ of the stack that is associated with the specified job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param stack_id: The stack_id of this JobSummary.
        :type: str
        """
        self._stack_id = stack_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this JobSummary.
        The `OCID`__ of the compartment where the stack of the associated job resides.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this JobSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this JobSummary.
        The `OCID`__ of the compartment where the stack of the associated job resides.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this JobSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this JobSummary.
        The job's display name.


        :return: The display_name of this JobSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this JobSummary.
        The job's display name.


        :param display_name: The display_name of this JobSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def operation(self):
        """
        Gets the operation of this JobSummary.
        The type of job executing


        :return: The operation of this JobSummary.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this JobSummary.
        The type of job executing


        :param operation: The operation of this JobSummary.
        :type: str
        """
        self._operation = operation

    @property
    def job_operation_details(self):
        """
        Gets the job_operation_details of this JobSummary.

        :return: The job_operation_details of this JobSummary.
        :rtype: oci.resource_manager.models.JobOperationDetailsSummary
        """
        return self._job_operation_details

    @job_operation_details.setter
    def job_operation_details(self, job_operation_details):
        """
        Sets the job_operation_details of this JobSummary.

        :param job_operation_details: The job_operation_details of this JobSummary.
        :type: oci.resource_manager.models.JobOperationDetailsSummary
        """
        self._job_operation_details = job_operation_details

    @property
    def apply_job_plan_resolution(self):
        """
        Gets the apply_job_plan_resolution of this JobSummary.

        :return: The apply_job_plan_resolution of this JobSummary.
        :rtype: oci.resource_manager.models.ApplyJobPlanResolution
        """
        return self._apply_job_plan_resolution

    @apply_job_plan_resolution.setter
    def apply_job_plan_resolution(self, apply_job_plan_resolution):
        """
        Sets the apply_job_plan_resolution of this JobSummary.

        :param apply_job_plan_resolution: The apply_job_plan_resolution of this JobSummary.
        :type: oci.resource_manager.models.ApplyJobPlanResolution
        """
        self._apply_job_plan_resolution = apply_job_plan_resolution

    @property
    def resolved_plan_job_id(self):
        """
        Gets the resolved_plan_job_id of this JobSummary.
        Deprecated. Use the property `executionPlanJobId` in `jobOperationDetails` instead.
        The plan job `OCID`__ that was used (if this was an apply job and was not auto-approved).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The resolved_plan_job_id of this JobSummary.
        :rtype: str
        """
        return self._resolved_plan_job_id

    @resolved_plan_job_id.setter
    def resolved_plan_job_id(self, resolved_plan_job_id):
        """
        Sets the resolved_plan_job_id of this JobSummary.
        Deprecated. Use the property `executionPlanJobId` in `jobOperationDetails` instead.
        The plan job `OCID`__ that was used (if this was an apply job and was not auto-approved).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param resolved_plan_job_id: The resolved_plan_job_id of this JobSummary.
        :type: str
        """
        self._resolved_plan_job_id = resolved_plan_job_id

    @property
    def time_created(self):
        """
        Gets the time_created of this JobSummary.
        The date and time the job was created.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :return: The time_created of this JobSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this JobSummary.
        The date and time the job was created.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :param time_created: The time_created of this JobSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_finished(self):
        """
        Gets the time_finished of this JobSummary.
        The date and time the job succeeded or failed.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :return: The time_finished of this JobSummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this JobSummary.
        The date and time the job succeeded or failed.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :param time_finished: The time_finished of this JobSummary.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this JobSummary.
        Current state of the specified job.
        For more information about job lifecycle states in Resource Manager, see
        `Key Concepts`__.

        Allowable values:
        - ACCEPTED
        - IN_PROGRESS
        - FAILED
        - SUCCEEDED
        - CANCELING
        - CANCELED

        __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#JobStates


        :return: The lifecycle_state of this JobSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this JobSummary.
        Current state of the specified job.
        For more information about job lifecycle states in Resource Manager, see
        `Key Concepts`__.

        Allowable values:
        - ACCEPTED
        - IN_PROGRESS
        - FAILED
        - SUCCEEDED
        - CANCELING
        - CANCELED

        __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#JobStates


        :param lifecycle_state: The lifecycle_state of this JobSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this JobSummary.
        Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this JobSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this JobSummary.
        Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this JobSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this JobSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this JobSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this JobSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this JobSummary.
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
