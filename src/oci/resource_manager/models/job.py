# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Job(object):
    """
    The properties that define a job. Jobs perform the actions that are defined in your configuration.
    - **Plan job**. A plan job takes your Terraform configuration, parses it, and creates an execution plan.
    - **Apply job**. The apply job takes your execution plan, applies it to the associated stack, then executes
    the configuration's instructions.
    - **Destroy job**. To clean up the infrastructure controlled by the stack, you run a destroy job.
    A destroy job does not delete the stack or associated job resources,
    but instead releases the resources managed by the stack.
    - **Import_TF_State job**. An import Terraform state job takes a Terraform state file and sets it as the current
    state of the stack. This is used to migrate local Terraform environments to Resource Manager.
    """

    #: A constant which can be used with the operation property of a Job.
    #: This constant has a value of "PLAN"
    OPERATION_PLAN = "PLAN"

    #: A constant which can be used with the operation property of a Job.
    #: This constant has a value of "APPLY"
    OPERATION_APPLY = "APPLY"

    #: A constant which can be used with the operation property of a Job.
    #: This constant has a value of "DESTROY"
    OPERATION_DESTROY = "DESTROY"

    #: A constant which can be used with the operation property of a Job.
    #: This constant has a value of "IMPORT_TF_STATE"
    OPERATION_IMPORT_TF_STATE = "IMPORT_TF_STATE"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new Job object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Job.
        :type id: str

        :param stack_id:
            The value to assign to the stack_id property of this Job.
        :type stack_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Job.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this Job.
        :type display_name: str

        :param operation:
            The value to assign to the operation property of this Job.
            Allowed values for this property are: "PLAN", "APPLY", "DESTROY", "IMPORT_TF_STATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation: str

        :param job_operation_details:
            The value to assign to the job_operation_details property of this Job.
        :type job_operation_details: oci.resource_manager.models.JobOperationDetails

        :param apply_job_plan_resolution:
            The value to assign to the apply_job_plan_resolution property of this Job.
        :type apply_job_plan_resolution: oci.resource_manager.models.ApplyJobPlanResolution

        :param resolved_plan_job_id:
            The value to assign to the resolved_plan_job_id property of this Job.
        :type resolved_plan_job_id: str

        :param time_created:
            The value to assign to the time_created property of this Job.
        :type time_created: datetime

        :param time_finished:
            The value to assign to the time_finished property of this Job.
        :type time_finished: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Job.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param failure_details:
            The value to assign to the failure_details property of this Job.
        :type failure_details: oci.resource_manager.models.FailureDetails

        :param cancellation_details:
            The value to assign to the cancellation_details property of this Job.
        :type cancellation_details: oci.resource_manager.models.CancellationDetails

        :param working_directory:
            The value to assign to the working_directory property of this Job.
        :type working_directory: str

        :param variables:
            The value to assign to the variables property of this Job.
        :type variables: dict(str, str)

        :param config_source:
            The value to assign to the config_source property of this Job.
        :type config_source: oci.resource_manager.models.ConfigSourceRecord

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Job.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Job.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'stack_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'operation': 'str',
            'job_operation_details': 'JobOperationDetails',
            'apply_job_plan_resolution': 'ApplyJobPlanResolution',
            'resolved_plan_job_id': 'str',
            'time_created': 'datetime',
            'time_finished': 'datetime',
            'lifecycle_state': 'str',
            'failure_details': 'FailureDetails',
            'cancellation_details': 'CancellationDetails',
            'working_directory': 'str',
            'variables': 'dict(str, str)',
            'config_source': 'ConfigSourceRecord',
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
            'failure_details': 'failureDetails',
            'cancellation_details': 'cancellationDetails',
            'working_directory': 'workingDirectory',
            'variables': 'variables',
            'config_source': 'configSource',
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
        self._failure_details = None
        self._cancellation_details = None
        self._working_directory = None
        self._variables = None
        self._config_source = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this Job.
        The `OCID`__ of the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Job.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Job.
        The `OCID`__ of the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this Job.
        :type: str
        """
        self._id = id

    @property
    def stack_id(self):
        """
        Gets the stack_id of this Job.
        The `OCID`__ of the stack that is associated with the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The stack_id of this Job.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """
        Sets the stack_id of this Job.
        The `OCID`__ of the stack that is associated with the job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param stack_id: The stack_id of this Job.
        :type: str
        """
        self._stack_id = stack_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Job.
        The `OCID`__ of the compartment in which the job's associated stack resides.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Job.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Job.
        The `OCID`__ of the compartment in which the job's associated stack resides.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Job.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Job.
        The job's display name.


        :return: The display_name of this Job.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Job.
        The job's display name.


        :param display_name: The display_name of this Job.
        :type: str
        """
        self._display_name = display_name

    @property
    def operation(self):
        """
        Gets the operation of this Job.
        The type of job executing.

        Allowed values for this property are: "PLAN", "APPLY", "DESTROY", "IMPORT_TF_STATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation of this Job.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this Job.
        The type of job executing.


        :param operation: The operation of this Job.
        :type: str
        """
        allowed_values = ["PLAN", "APPLY", "DESTROY", "IMPORT_TF_STATE"]
        if not value_allowed_none_or_none_sentinel(operation, allowed_values):
            operation = 'UNKNOWN_ENUM_VALUE'
        self._operation = operation

    @property
    def job_operation_details(self):
        """
        Gets the job_operation_details of this Job.

        :return: The job_operation_details of this Job.
        :rtype: oci.resource_manager.models.JobOperationDetails
        """
        return self._job_operation_details

    @job_operation_details.setter
    def job_operation_details(self, job_operation_details):
        """
        Sets the job_operation_details of this Job.

        :param job_operation_details: The job_operation_details of this Job.
        :type: oci.resource_manager.models.JobOperationDetails
        """
        self._job_operation_details = job_operation_details

    @property
    def apply_job_plan_resolution(self):
        """
        Gets the apply_job_plan_resolution of this Job.

        :return: The apply_job_plan_resolution of this Job.
        :rtype: oci.resource_manager.models.ApplyJobPlanResolution
        """
        return self._apply_job_plan_resolution

    @apply_job_plan_resolution.setter
    def apply_job_plan_resolution(self, apply_job_plan_resolution):
        """
        Sets the apply_job_plan_resolution of this Job.

        :param apply_job_plan_resolution: The apply_job_plan_resolution of this Job.
        :type: oci.resource_manager.models.ApplyJobPlanResolution
        """
        self._apply_job_plan_resolution = apply_job_plan_resolution

    @property
    def resolved_plan_job_id(self):
        """
        Gets the resolved_plan_job_id of this Job.
        Deprecated. Use the property `executionPlanJobId` in `jobOperationDetails` instead.
        The plan job `OCID`__ that was used (if this was an apply job and was not auto-approved).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The resolved_plan_job_id of this Job.
        :rtype: str
        """
        return self._resolved_plan_job_id

    @resolved_plan_job_id.setter
    def resolved_plan_job_id(self, resolved_plan_job_id):
        """
        Sets the resolved_plan_job_id of this Job.
        Deprecated. Use the property `executionPlanJobId` in `jobOperationDetails` instead.
        The plan job `OCID`__ that was used (if this was an apply job and was not auto-approved).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param resolved_plan_job_id: The resolved_plan_job_id of this Job.
        :type: str
        """
        self._resolved_plan_job_id = resolved_plan_job_id

    @property
    def time_created(self):
        """
        Gets the time_created of this Job.
        The date and time when the job was created.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :return: The time_created of this Job.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Job.
        The date and time when the job was created.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :param time_created: The time_created of this Job.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_finished(self):
        """
        Gets the time_finished of this Job.
        The date and time when the job stopped running, irrespective of whether the job ran successfully.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :return: The time_finished of this Job.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this Job.
        The date and time when the job stopped running, irrespective of whether the job ran successfully.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :param time_finished: The time_finished of this Job.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Job.
        Current state of the specified job.
        For more information about job lifecycle states in Resource Manager, see
        `Key Concepts`__.

        __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__JobStates

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Job.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Job.
        Current state of the specified job.
        For more information about job lifecycle states in Resource Manager, see
        `Key Concepts`__.

        __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__JobStates


        :param lifecycle_state: The lifecycle_state of this Job.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def failure_details(self):
        """
        Gets the failure_details of this Job.

        :return: The failure_details of this Job.
        :rtype: oci.resource_manager.models.FailureDetails
        """
        return self._failure_details

    @failure_details.setter
    def failure_details(self, failure_details):
        """
        Sets the failure_details of this Job.

        :param failure_details: The failure_details of this Job.
        :type: oci.resource_manager.models.FailureDetails
        """
        self._failure_details = failure_details

    @property
    def cancellation_details(self):
        """
        Gets the cancellation_details of this Job.

        :return: The cancellation_details of this Job.
        :rtype: oci.resource_manager.models.CancellationDetails
        """
        return self._cancellation_details

    @cancellation_details.setter
    def cancellation_details(self, cancellation_details):
        """
        Sets the cancellation_details of this Job.

        :param cancellation_details: The cancellation_details of this Job.
        :type: oci.resource_manager.models.CancellationDetails
        """
        self._cancellation_details = cancellation_details

    @property
    def working_directory(self):
        """
        Gets the working_directory of this Job.
        File path to the directory from which Terraform runs.
        If not specified, the root directory is used.
        This parameter is ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`.


        :return: The working_directory of this Job.
        :rtype: str
        """
        return self._working_directory

    @working_directory.setter
    def working_directory(self, working_directory):
        """
        Sets the working_directory of this Job.
        File path to the directory from which Terraform runs.
        If not specified, the root directory is used.
        This parameter is ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`.


        :param working_directory: The working_directory of this Job.
        :type: str
        """
        self._working_directory = working_directory

    @property
    def variables(self):
        """
        Gets the variables of this Job.
        Terraform variables associated with this resource.
        Maximum number of variables supported is 250.
        The maximum size of each variable, including both name and value, is 8192 bytes.
        Example: `{\"CompartmentId\": \"compartment-id-value\"}`


        :return: The variables of this Job.
        :rtype: dict(str, str)
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this Job.
        Terraform variables associated with this resource.
        Maximum number of variables supported is 250.
        The maximum size of each variable, including both name and value, is 8192 bytes.
        Example: `{\"CompartmentId\": \"compartment-id-value\"}`


        :param variables: The variables of this Job.
        :type: dict(str, str)
        """
        self._variables = variables

    @property
    def config_source(self):
        """
        Gets the config_source of this Job.

        :return: The config_source of this Job.
        :rtype: oci.resource_manager.models.ConfigSourceRecord
        """
        return self._config_source

    @config_source.setter
    def config_source(self, config_source):
        """
        Sets the config_source of this Job.

        :param config_source: The config_source of this Job.
        :type: oci.resource_manager.models.ConfigSourceRecord
        """
        self._config_source = config_source

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Job.
        Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Job.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Job.
        Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Job.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Job.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Job.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Job.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Job.
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
