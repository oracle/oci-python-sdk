# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_deployment_details import UpdateDeploymentDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSingleDeployStageDeploymentDetails(UpdateDeploymentDetails):
    """
    Update details for a single stage deployment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSingleDeployStageDeploymentDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.UpdateSingleDeployStageDeploymentDetails.deployment_type` attribute
        of this class is ``SINGLE_STAGE_DEPLOYMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deployment_type:
            The value to assign to the deployment_type property of this UpdateSingleDeployStageDeploymentDetails.
        :type deployment_type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateSingleDeployStageDeploymentDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateSingleDeployStageDeploymentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateSingleDeployStageDeploymentDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'deployment_type': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'deployment_type': 'deploymentType',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._deployment_type = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._deployment_type = 'SINGLE_STAGE_DEPLOYMENT'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
