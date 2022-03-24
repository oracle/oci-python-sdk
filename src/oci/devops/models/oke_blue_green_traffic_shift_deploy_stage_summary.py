# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_stage_summary import DeployStageSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OkeBlueGreenTrafficShiftDeployStageSummary(DeployStageSummary):
    """
    Specifies the Container Engine for Kubernetes (OKE) cluster blue-green deployment traffic shift stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OkeBlueGreenTrafficShiftDeployStageSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.OkeBlueGreenTrafficShiftDeployStageSummary.deploy_stage_type` attribute
        of this class is ``OKE_BLUE_GREEN_TRAFFIC_SHIFT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :type id: str

        :param description:
            The value to assign to the description property of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :type project_id: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :type deploy_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :type compartment_id: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :type deploy_stage_type: str

        :param time_created:
            The value to assign to the time_created property of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :type lifecycle_details: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :type system_tags: dict(str, dict(str, object))

        :param oke_blue_green_deploy_stage_id:
            The value to assign to the oke_blue_green_deploy_stage_id property of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :type oke_blue_green_deploy_stage_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'deploy_pipeline_id': 'str',
            'compartment_id': 'str',
            'deploy_stage_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'oke_blue_green_deploy_stage_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'deploy_pipeline_id': 'deployPipelineId',
            'compartment_id': 'compartmentId',
            'deploy_stage_type': 'deployStageType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'oke_blue_green_deploy_stage_id': 'okeBlueGreenDeployStageId'
        }

        self._id = None
        self._description = None
        self._display_name = None
        self._project_id = None
        self._deploy_pipeline_id = None
        self._compartment_id = None
        self._deploy_stage_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._oke_blue_green_deploy_stage_id = None
        self._deploy_stage_type = 'OKE_BLUE_GREEN_TRAFFIC_SHIFT'

    @property
    def oke_blue_green_deploy_stage_id(self):
        """
        **[Required]** Gets the oke_blue_green_deploy_stage_id of this OkeBlueGreenTrafficShiftDeployStageSummary.
        The OCID of the upstream OKE blue-green deployment stage in this pipeline.


        :return: The oke_blue_green_deploy_stage_id of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :rtype: str
        """
        return self._oke_blue_green_deploy_stage_id

    @oke_blue_green_deploy_stage_id.setter
    def oke_blue_green_deploy_stage_id(self, oke_blue_green_deploy_stage_id):
        """
        Sets the oke_blue_green_deploy_stage_id of this OkeBlueGreenTrafficShiftDeployStageSummary.
        The OCID of the upstream OKE blue-green deployment stage in this pipeline.


        :param oke_blue_green_deploy_stage_id: The oke_blue_green_deploy_stage_id of this OkeBlueGreenTrafficShiftDeployStageSummary.
        :type: str
        """
        self._oke_blue_green_deploy_stage_id = oke_blue_green_deploy_stage_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
