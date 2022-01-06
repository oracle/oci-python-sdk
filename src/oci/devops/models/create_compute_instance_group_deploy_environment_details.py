# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_deploy_environment_details import CreateDeployEnvironmentDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateComputeInstanceGroupDeployEnvironmentDetails(CreateDeployEnvironmentDetails):
    """
    Specifies the Compute instance group environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateComputeInstanceGroupDeployEnvironmentDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CreateComputeInstanceGroupDeployEnvironmentDetails.deploy_environment_type` attribute
        of this class is ``COMPUTE_INSTANCE_GROUP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CreateComputeInstanceGroupDeployEnvironmentDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateComputeInstanceGroupDeployEnvironmentDetails.
        :type display_name: str

        :param deploy_environment_type:
            The value to assign to the deploy_environment_type property of this CreateComputeInstanceGroupDeployEnvironmentDetails.
        :type deploy_environment_type: str

        :param project_id:
            The value to assign to the project_id property of this CreateComputeInstanceGroupDeployEnvironmentDetails.
        :type project_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateComputeInstanceGroupDeployEnvironmentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateComputeInstanceGroupDeployEnvironmentDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param compute_instance_group_selectors:
            The value to assign to the compute_instance_group_selectors property of this CreateComputeInstanceGroupDeployEnvironmentDetails.
        :type compute_instance_group_selectors: oci.devops.models.ComputeInstanceGroupSelectorCollection

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_environment_type': 'str',
            'project_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'compute_instance_group_selectors': 'ComputeInstanceGroupSelectorCollection'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_environment_type': 'deployEnvironmentType',
            'project_id': 'projectId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'compute_instance_group_selectors': 'computeInstanceGroupSelectors'
        }

        self._description = None
        self._display_name = None
        self._deploy_environment_type = None
        self._project_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._compute_instance_group_selectors = None
        self._deploy_environment_type = 'COMPUTE_INSTANCE_GROUP'

    @property
    def compute_instance_group_selectors(self):
        """
        **[Required]** Gets the compute_instance_group_selectors of this CreateComputeInstanceGroupDeployEnvironmentDetails.

        :return: The compute_instance_group_selectors of this CreateComputeInstanceGroupDeployEnvironmentDetails.
        :rtype: oci.devops.models.ComputeInstanceGroupSelectorCollection
        """
        return self._compute_instance_group_selectors

    @compute_instance_group_selectors.setter
    def compute_instance_group_selectors(self, compute_instance_group_selectors):
        """
        Sets the compute_instance_group_selectors of this CreateComputeInstanceGroupDeployEnvironmentDetails.

        :param compute_instance_group_selectors: The compute_instance_group_selectors of this CreateComputeInstanceGroupDeployEnvironmentDetails.
        :type: oci.devops.models.ComputeInstanceGroupSelectorCollection
        """
        self._compute_instance_group_selectors = compute_instance_group_selectors

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
