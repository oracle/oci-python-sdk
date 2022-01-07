# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateJobDetails(object):
    """
    Defines the requirements and properties of a job to create and run against the specified stack.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param stack_id:
            The value to assign to the stack_id property of this CreateJobDetails.
        :type stack_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateJobDetails.
        :type display_name: str

        :param operation:
            The value to assign to the operation property of this CreateJobDetails.
        :type operation: str

        :param job_operation_details:
            The value to assign to the job_operation_details property of this CreateJobDetails.
        :type job_operation_details: oci.resource_manager.models.CreateJobOperationDetails

        :param apply_job_plan_resolution:
            The value to assign to the apply_job_plan_resolution property of this CreateJobDetails.
        :type apply_job_plan_resolution: oci.resource_manager.models.ApplyJobPlanResolution

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateJobDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateJobDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'stack_id': 'str',
            'display_name': 'str',
            'operation': 'str',
            'job_operation_details': 'CreateJobOperationDetails',
            'apply_job_plan_resolution': 'ApplyJobPlanResolution',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'stack_id': 'stackId',
            'display_name': 'displayName',
            'operation': 'operation',
            'job_operation_details': 'jobOperationDetails',
            'apply_job_plan_resolution': 'applyJobPlanResolution',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._stack_id = None
        self._display_name = None
        self._operation = None
        self._job_operation_details = None
        self._apply_job_plan_resolution = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def stack_id(self):
        """
        **[Required]** Gets the stack_id of this CreateJobDetails.
        The `OCID`__ of the stack that is associated with the current job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The stack_id of this CreateJobDetails.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """
        Sets the stack_id of this CreateJobDetails.
        The `OCID`__ of the stack that is associated with the current job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param stack_id: The stack_id of this CreateJobDetails.
        :type: str
        """
        self._stack_id = stack_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateJobDetails.
        Description of the job.


        :return: The display_name of this CreateJobDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateJobDetails.
        Description of the job.


        :param display_name: The display_name of this CreateJobDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def operation(self):
        """
        Gets the operation of this CreateJobDetails.
        Terraform-specific operation to execute.


        :return: The operation of this CreateJobDetails.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this CreateJobDetails.
        Terraform-specific operation to execute.


        :param operation: The operation of this CreateJobDetails.
        :type: str
        """
        self._operation = operation

    @property
    def job_operation_details(self):
        """
        Gets the job_operation_details of this CreateJobDetails.

        :return: The job_operation_details of this CreateJobDetails.
        :rtype: oci.resource_manager.models.CreateJobOperationDetails
        """
        return self._job_operation_details

    @job_operation_details.setter
    def job_operation_details(self, job_operation_details):
        """
        Sets the job_operation_details of this CreateJobDetails.

        :param job_operation_details: The job_operation_details of this CreateJobDetails.
        :type: oci.resource_manager.models.CreateJobOperationDetails
        """
        self._job_operation_details = job_operation_details

    @property
    def apply_job_plan_resolution(self):
        """
        Gets the apply_job_plan_resolution of this CreateJobDetails.

        :return: The apply_job_plan_resolution of this CreateJobDetails.
        :rtype: oci.resource_manager.models.ApplyJobPlanResolution
        """
        return self._apply_job_plan_resolution

    @apply_job_plan_resolution.setter
    def apply_job_plan_resolution(self, apply_job_plan_resolution):
        """
        Sets the apply_job_plan_resolution of this CreateJobDetails.

        :param apply_job_plan_resolution: The apply_job_plan_resolution of this CreateJobDetails.
        :type: oci.resource_manager.models.ApplyJobPlanResolution
        """
        self._apply_job_plan_resolution = apply_job_plan_resolution

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateJobDetails.
        Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateJobDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateJobDetails.
        Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateJobDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateJobDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateJobDetails.
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
