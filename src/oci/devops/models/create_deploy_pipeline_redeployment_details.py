# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_deployment_details import CreateDeploymentDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDeployPipelineRedeploymentDetails(CreateDeploymentDetails):
    """
    Details of the new deployment to be created based on a previously executed deployment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDeployPipelineRedeploymentDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CreateDeployPipelineRedeploymentDetails.deployment_type` attribute
        of this class is ``PIPELINE_REDEPLOYMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this CreateDeployPipelineRedeploymentDetails.
        :type deploy_pipeline_id: str

        :param deployment_type:
            The value to assign to the deployment_type property of this CreateDeployPipelineRedeploymentDetails.
        :type deployment_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateDeployPipelineRedeploymentDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDeployPipelineRedeploymentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDeployPipelineRedeploymentDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param previous_deployment_id:
            The value to assign to the previous_deployment_id property of this CreateDeployPipelineRedeploymentDetails.
        :type previous_deployment_id: str

        """
        self.swagger_types = {
            'deploy_pipeline_id': 'str',
            'deployment_type': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'previous_deployment_id': 'str'
        }

        self.attribute_map = {
            'deploy_pipeline_id': 'deployPipelineId',
            'deployment_type': 'deploymentType',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'previous_deployment_id': 'previousDeploymentId'
        }

        self._deploy_pipeline_id = None
        self._deployment_type = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._previous_deployment_id = None
        self._deployment_type = 'PIPELINE_REDEPLOYMENT'

    @property
    def previous_deployment_id(self):
        """
        Gets the previous_deployment_id of this CreateDeployPipelineRedeploymentDetails.
        Specifies the OCID of the previous deployment to be redeployed.


        :return: The previous_deployment_id of this CreateDeployPipelineRedeploymentDetails.
        :rtype: str
        """
        return self._previous_deployment_id

    @previous_deployment_id.setter
    def previous_deployment_id(self, previous_deployment_id):
        """
        Sets the previous_deployment_id of this CreateDeployPipelineRedeploymentDetails.
        Specifies the OCID of the previous deployment to be redeployed.


        :param previous_deployment_id: The previous_deployment_id of this CreateDeployPipelineRedeploymentDetails.
        :type: str
        """
        self._previous_deployment_id = previous_deployment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
