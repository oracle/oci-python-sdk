# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_environment_summary import DeployEnvironmentSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OkeClusterDeployEnvironmentSummary(DeployEnvironmentSummary):
    """
    Specifies the Kubernetes cluster environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OkeClusterDeployEnvironmentSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.OkeClusterDeployEnvironmentSummary.deploy_environment_type` attribute
        of this class is ``OKE_CLUSTER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OkeClusterDeployEnvironmentSummary.
        :type id: str

        :param description:
            The value to assign to the description property of this OkeClusterDeployEnvironmentSummary.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this OkeClusterDeployEnvironmentSummary.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this OkeClusterDeployEnvironmentSummary.
        :type project_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OkeClusterDeployEnvironmentSummary.
        :type compartment_id: str

        :param deploy_environment_type:
            The value to assign to the deploy_environment_type property of this OkeClusterDeployEnvironmentSummary.
        :type deploy_environment_type: str

        :param time_created:
            The value to assign to the time_created property of this OkeClusterDeployEnvironmentSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OkeClusterDeployEnvironmentSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OkeClusterDeployEnvironmentSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OkeClusterDeployEnvironmentSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OkeClusterDeployEnvironmentSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OkeClusterDeployEnvironmentSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OkeClusterDeployEnvironmentSummary.
        :type system_tags: dict(str, dict(str, object))

        :param cluster_id:
            The value to assign to the cluster_id property of this OkeClusterDeployEnvironmentSummary.
        :type cluster_id: str

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
            'cluster_id': 'str'
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
            'cluster_id': 'clusterId'
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
        self._cluster_id = None
        self._deploy_environment_type = 'OKE_CLUSTER'

    @property
    def cluster_id(self):
        """
        **[Required]** Gets the cluster_id of this OkeClusterDeployEnvironmentSummary.
        The OCID of the Kubernetes cluster.


        :return: The cluster_id of this OkeClusterDeployEnvironmentSummary.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this OkeClusterDeployEnvironmentSummary.
        The OCID of the Kubernetes cluster.


        :param cluster_id: The cluster_id of this OkeClusterDeployEnvironmentSummary.
        :type: str
        """
        self._cluster_id = cluster_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
