# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_deploy_environment_details import UpdateDeployEnvironmentDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOkeClusterDeployEnvironmentDetails(UpdateDeployEnvironmentDetails):
    """
    Specifies the Kubernetes cluster environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOkeClusterDeployEnvironmentDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.UpdateOkeClusterDeployEnvironmentDetails.deploy_environment_type` attribute
        of this class is ``OKE_CLUSTER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateOkeClusterDeployEnvironmentDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateOkeClusterDeployEnvironmentDetails.
        :type display_name: str

        :param deploy_environment_type:
            The value to assign to the deploy_environment_type property of this UpdateOkeClusterDeployEnvironmentDetails.
        :type deploy_environment_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateOkeClusterDeployEnvironmentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateOkeClusterDeployEnvironmentDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param cluster_id:
            The value to assign to the cluster_id property of this UpdateOkeClusterDeployEnvironmentDetails.
        :type cluster_id: str

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_environment_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'cluster_id': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_environment_type': 'deployEnvironmentType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'cluster_id': 'clusterId'
        }

        self._description = None
        self._display_name = None
        self._deploy_environment_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._cluster_id = None
        self._deploy_environment_type = 'OKE_CLUSTER'

    @property
    def cluster_id(self):
        """
        Gets the cluster_id of this UpdateOkeClusterDeployEnvironmentDetails.
        The OCID of the Kubernetes cluster.


        :return: The cluster_id of this UpdateOkeClusterDeployEnvironmentDetails.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this UpdateOkeClusterDeployEnvironmentDetails.
        The OCID of the Kubernetes cluster.


        :param cluster_id: The cluster_id of this UpdateOkeClusterDeployEnvironmentDetails.
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
