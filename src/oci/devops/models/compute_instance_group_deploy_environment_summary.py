# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_environment_summary import DeployEnvironmentSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeInstanceGroupDeployEnvironmentSummary(DeployEnvironmentSummary):
    """
    Specifies the Compute instance group environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeInstanceGroupDeployEnvironmentSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.ComputeInstanceGroupDeployEnvironmentSummary.deploy_environment_type` attribute
        of this class is ``COMPUTE_INSTANCE_GROUP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ComputeInstanceGroupDeployEnvironmentSummary.
        :type id: str

        :param description:
            The value to assign to the description property of this ComputeInstanceGroupDeployEnvironmentSummary.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this ComputeInstanceGroupDeployEnvironmentSummary.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this ComputeInstanceGroupDeployEnvironmentSummary.
        :type project_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ComputeInstanceGroupDeployEnvironmentSummary.
        :type compartment_id: str

        :param deploy_environment_type:
            The value to assign to the deploy_environment_type property of this ComputeInstanceGroupDeployEnvironmentSummary.
        :type deploy_environment_type: str

        :param time_created:
            The value to assign to the time_created property of this ComputeInstanceGroupDeployEnvironmentSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ComputeInstanceGroupDeployEnvironmentSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ComputeInstanceGroupDeployEnvironmentSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ComputeInstanceGroupDeployEnvironmentSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ComputeInstanceGroupDeployEnvironmentSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ComputeInstanceGroupDeployEnvironmentSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ComputeInstanceGroupDeployEnvironmentSummary.
        :type system_tags: dict(str, dict(str, object))

        :param compute_instance_group_selectors:
            The value to assign to the compute_instance_group_selectors property of this ComputeInstanceGroupDeployEnvironmentSummary.
        :type compute_instance_group_selectors: oci.devops.models.ComputeInstanceGroupSelectorCollection

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'compartment_id': 'str',
            'deploy_environment_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'compute_instance_group_selectors': 'ComputeInstanceGroupSelectorCollection'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'compartment_id': 'compartmentId',
            'deploy_environment_type': 'deployEnvironmentType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'compute_instance_group_selectors': 'computeInstanceGroupSelectors'
        }

        self._id = None
        self._description = None
        self._display_name = None
        self._project_id = None
        self._compartment_id = None
        self._deploy_environment_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._compute_instance_group_selectors = None
        self._deploy_environment_type = 'COMPUTE_INSTANCE_GROUP'

    @property
    def compute_instance_group_selectors(self):
        """
        **[Required]** Gets the compute_instance_group_selectors of this ComputeInstanceGroupDeployEnvironmentSummary.

        :return: The compute_instance_group_selectors of this ComputeInstanceGroupDeployEnvironmentSummary.
        :rtype: oci.devops.models.ComputeInstanceGroupSelectorCollection
        """
        return self._compute_instance_group_selectors

    @compute_instance_group_selectors.setter
    def compute_instance_group_selectors(self, compute_instance_group_selectors):
        """
        Sets the compute_instance_group_selectors of this ComputeInstanceGroupDeployEnvironmentSummary.

        :param compute_instance_group_selectors: The compute_instance_group_selectors of this ComputeInstanceGroupDeployEnvironmentSummary.
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
