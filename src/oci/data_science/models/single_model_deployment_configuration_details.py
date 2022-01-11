# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .model_deployment_configuration_details import ModelDeploymentConfigurationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SingleModelDeploymentConfigurationDetails(ModelDeploymentConfigurationDetails):
    """
    The single model type deployment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SingleModelDeploymentConfigurationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.SingleModelDeploymentConfigurationDetails.deployment_type` attribute
        of this class is ``SINGLE_MODEL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deployment_type:
            The value to assign to the deployment_type property of this SingleModelDeploymentConfigurationDetails.
            Allowed values for this property are: "SINGLE_MODEL"
        :type deployment_type: str

        :param model_configuration_details:
            The value to assign to the model_configuration_details property of this SingleModelDeploymentConfigurationDetails.
        :type model_configuration_details: oci.data_science.models.ModelConfigurationDetails

        """
        self.swagger_types = {
            'deployment_type': 'str',
            'model_configuration_details': 'ModelConfigurationDetails'
        }

        self.attribute_map = {
            'deployment_type': 'deploymentType',
            'model_configuration_details': 'modelConfigurationDetails'
        }

        self._deployment_type = None
        self._model_configuration_details = None
        self._deployment_type = 'SINGLE_MODEL'

    @property
    def model_configuration_details(self):
        """
        **[Required]** Gets the model_configuration_details of this SingleModelDeploymentConfigurationDetails.

        :return: The model_configuration_details of this SingleModelDeploymentConfigurationDetails.
        :rtype: oci.data_science.models.ModelConfigurationDetails
        """
        return self._model_configuration_details

    @model_configuration_details.setter
    def model_configuration_details(self, model_configuration_details):
        """
        Sets the model_configuration_details of this SingleModelDeploymentConfigurationDetails.

        :param model_configuration_details: The model_configuration_details of this SingleModelDeploymentConfigurationDetails.
        :type: oci.data_science.models.ModelConfigurationDetails
        """
        self._model_configuration_details = model_configuration_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
