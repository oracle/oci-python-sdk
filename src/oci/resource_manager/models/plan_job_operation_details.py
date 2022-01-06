# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .job_operation_details import JobOperationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PlanJobOperationDetails(JobOperationDetails):
    """
    Job details that are specific to plan operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PlanJobOperationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.PlanJobOperationDetails.operation` attribute
        of this class is ``PLAN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this PlanJobOperationDetails.
        :type operation: str

        :param terraform_advanced_options:
            The value to assign to the terraform_advanced_options property of this PlanJobOperationDetails.
        :type terraform_advanced_options: oci.resource_manager.models.TerraformAdvancedOptions

        """
        self.swagger_types = {
            'operation': 'str',
            'terraform_advanced_options': 'TerraformAdvancedOptions'
        }

        self.attribute_map = {
            'operation': 'operation',
            'terraform_advanced_options': 'terraformAdvancedOptions'
        }

        self._operation = None
        self._terraform_advanced_options = None
        self._operation = 'PLAN'

    @property
    def terraform_advanced_options(self):
        """
        Gets the terraform_advanced_options of this PlanJobOperationDetails.

        :return: The terraform_advanced_options of this PlanJobOperationDetails.
        :rtype: oci.resource_manager.models.TerraformAdvancedOptions
        """
        return self._terraform_advanced_options

    @terraform_advanced_options.setter
    def terraform_advanced_options(self, terraform_advanced_options):
        """
        Sets the terraform_advanced_options of this PlanJobOperationDetails.

        :param terraform_advanced_options: The terraform_advanced_options of this PlanJobOperationDetails.
        :type: oci.resource_manager.models.TerraformAdvancedOptions
        """
        self._terraform_advanced_options = terraform_advanced_options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
