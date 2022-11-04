# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .job_operation_details import JobOperationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PlanRollbackJobOperationDetails(JobOperationDetails):
    """
    Job details that are specific to a plan rollback job. For more information about plan rollback jobs,
    see `Creating a Plan Rollback Job`__.

    __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Tasks/create-job-plan-rollback.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PlanRollbackJobOperationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.PlanRollbackJobOperationDetails.operation` attribute
        of this class is ``PLAN_ROLLBACK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this PlanRollbackJobOperationDetails.
        :type operation: str

        :param terraform_advanced_options:
            The value to assign to the terraform_advanced_options property of this PlanRollbackJobOperationDetails.
        :type terraform_advanced_options: oci.resource_manager.models.TerraformAdvancedOptions

        :param target_rollback_job_id:
            The value to assign to the target_rollback_job_id property of this PlanRollbackJobOperationDetails.
        :type target_rollback_job_id: str

        """
        self.swagger_types = {
            'operation': 'str',
            'terraform_advanced_options': 'TerraformAdvancedOptions',
            'target_rollback_job_id': 'str'
        }

        self.attribute_map = {
            'operation': 'operation',
            'terraform_advanced_options': 'terraformAdvancedOptions',
            'target_rollback_job_id': 'targetRollbackJobId'
        }

        self._operation = None
        self._terraform_advanced_options = None
        self._target_rollback_job_id = None
        self._operation = 'PLAN_ROLLBACK'

    @property
    def terraform_advanced_options(self):
        """
        Gets the terraform_advanced_options of this PlanRollbackJobOperationDetails.

        :return: The terraform_advanced_options of this PlanRollbackJobOperationDetails.
        :rtype: oci.resource_manager.models.TerraformAdvancedOptions
        """
        return self._terraform_advanced_options

    @terraform_advanced_options.setter
    def terraform_advanced_options(self, terraform_advanced_options):
        """
        Sets the terraform_advanced_options of this PlanRollbackJobOperationDetails.

        :param terraform_advanced_options: The terraform_advanced_options of this PlanRollbackJobOperationDetails.
        :type: oci.resource_manager.models.TerraformAdvancedOptions
        """
        self._terraform_advanced_options = terraform_advanced_options

    @property
    def target_rollback_job_id(self):
        """
        **[Required]** Gets the target_rollback_job_id of this PlanRollbackJobOperationDetails.
        The `OCID`__ of a successful apply job to use for the plan rollback job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The target_rollback_job_id of this PlanRollbackJobOperationDetails.
        :rtype: str
        """
        return self._target_rollback_job_id

    @target_rollback_job_id.setter
    def target_rollback_job_id(self, target_rollback_job_id):
        """
        Sets the target_rollback_job_id of this PlanRollbackJobOperationDetails.
        The `OCID`__ of a successful apply job to use for the plan rollback job.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param target_rollback_job_id: The target_rollback_job_id of this PlanRollbackJobOperationDetails.
        :type: str
        """
        self._target_rollback_job_id = target_rollback_job_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
