# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PipelineStepOverrideDetails(object):
    """
    Override details of the step. Only Step Configuration is allowed to be overridden.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PipelineStepOverrideDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param step_name:
            The value to assign to the step_name property of this PipelineStepOverrideDetails.
        :type step_name: str

        :param step_configuration_details:
            The value to assign to the step_configuration_details property of this PipelineStepOverrideDetails.
        :type step_configuration_details: oci.data_science.models.PipelineStepConfigurationDetails

        :param step_container_configuration_details:
            The value to assign to the step_container_configuration_details property of this PipelineStepOverrideDetails.
        :type step_container_configuration_details: oci.data_science.models.PipelineContainerConfigurationDetails

        :param step_dataflow_configuration_details:
            The value to assign to the step_dataflow_configuration_details property of this PipelineStepOverrideDetails.
        :type step_dataflow_configuration_details: oci.data_science.models.PipelineDataflowConfigurationDetails

        """
        self.swagger_types = {
            'step_name': 'str',
            'step_configuration_details': 'PipelineStepConfigurationDetails',
            'step_container_configuration_details': 'PipelineContainerConfigurationDetails',
            'step_dataflow_configuration_details': 'PipelineDataflowConfigurationDetails'
        }
        self.attribute_map = {
            'step_name': 'stepName',
            'step_configuration_details': 'stepConfigurationDetails',
            'step_container_configuration_details': 'stepContainerConfigurationDetails',
            'step_dataflow_configuration_details': 'stepDataflowConfigurationDetails'
        }
        self._step_name = None
        self._step_configuration_details = None
        self._step_container_configuration_details = None
        self._step_dataflow_configuration_details = None

    @property
    def step_name(self):
        """
        **[Required]** Gets the step_name of this PipelineStepOverrideDetails.
        The name of the step.


        :return: The step_name of this PipelineStepOverrideDetails.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """
        Sets the step_name of this PipelineStepOverrideDetails.
        The name of the step.


        :param step_name: The step_name of this PipelineStepOverrideDetails.
        :type: str
        """
        self._step_name = step_name

    @property
    def step_configuration_details(self):
        """
        **[Required]** Gets the step_configuration_details of this PipelineStepOverrideDetails.

        :return: The step_configuration_details of this PipelineStepOverrideDetails.
        :rtype: oci.data_science.models.PipelineStepConfigurationDetails
        """
        return self._step_configuration_details

    @step_configuration_details.setter
    def step_configuration_details(self, step_configuration_details):
        """
        Sets the step_configuration_details of this PipelineStepOverrideDetails.

        :param step_configuration_details: The step_configuration_details of this PipelineStepOverrideDetails.
        :type: oci.data_science.models.PipelineStepConfigurationDetails
        """
        self._step_configuration_details = step_configuration_details

    @property
    def step_container_configuration_details(self):
        """
        Gets the step_container_configuration_details of this PipelineStepOverrideDetails.

        :return: The step_container_configuration_details of this PipelineStepOverrideDetails.
        :rtype: oci.data_science.models.PipelineContainerConfigurationDetails
        """
        return self._step_container_configuration_details

    @step_container_configuration_details.setter
    def step_container_configuration_details(self, step_container_configuration_details):
        """
        Sets the step_container_configuration_details of this PipelineStepOverrideDetails.

        :param step_container_configuration_details: The step_container_configuration_details of this PipelineStepOverrideDetails.
        :type: oci.data_science.models.PipelineContainerConfigurationDetails
        """
        self._step_container_configuration_details = step_container_configuration_details

    @property
    def step_dataflow_configuration_details(self):
        """
        Gets the step_dataflow_configuration_details of this PipelineStepOverrideDetails.

        :return: The step_dataflow_configuration_details of this PipelineStepOverrideDetails.
        :rtype: oci.data_science.models.PipelineDataflowConfigurationDetails
        """
        return self._step_dataflow_configuration_details

    @step_dataflow_configuration_details.setter
    def step_dataflow_configuration_details(self, step_dataflow_configuration_details):
        """
        Sets the step_dataflow_configuration_details of this PipelineStepOverrideDetails.

        :param step_dataflow_configuration_details: The step_dataflow_configuration_details of this PipelineStepOverrideDetails.
        :type: oci.data_science.models.PipelineDataflowConfigurationDetails
        """
        self._step_dataflow_configuration_details = step_dataflow_configuration_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
