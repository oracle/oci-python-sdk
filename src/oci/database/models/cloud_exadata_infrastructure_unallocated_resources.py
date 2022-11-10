# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloudExadataInfrastructureUnallocatedResources(object):
    """
    Unallocated resources details of the Cloud Exadata infrastructure. Applies to Cloud Exadata infrastructure instances only.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CloudExadataInfrastructureUnallocatedResources object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cloud_exadata_infrastructure_id:
            The value to assign to the cloud_exadata_infrastructure_id property of this CloudExadataInfrastructureUnallocatedResources.
        :type cloud_exadata_infrastructure_id: str

        :param cloud_exadata_infrastructure_display_name:
            The value to assign to the cloud_exadata_infrastructure_display_name property of this CloudExadataInfrastructureUnallocatedResources.
        :type cloud_exadata_infrastructure_display_name: str

        :param local_storage_in_gbs:
            The value to assign to the local_storage_in_gbs property of this CloudExadataInfrastructureUnallocatedResources.
        :type local_storage_in_gbs: int

        :param ocpus:
            The value to assign to the ocpus property of this CloudExadataInfrastructureUnallocatedResources.
        :type ocpus: int

        :param memory_in_gbs:
            The value to assign to the memory_in_gbs property of this CloudExadataInfrastructureUnallocatedResources.
        :type memory_in_gbs: int

        :param exadata_storage_in_tbs:
            The value to assign to the exadata_storage_in_tbs property of this CloudExadataInfrastructureUnallocatedResources.
        :type exadata_storage_in_tbs: float

        :param cloud_autonomous_vm_clusters:
            The value to assign to the cloud_autonomous_vm_clusters property of this CloudExadataInfrastructureUnallocatedResources.
        :type cloud_autonomous_vm_clusters: list[oci.database.models.CloudAutonomousVmClusterResourceDetails]

        """
        self.swagger_types = {
            'cloud_exadata_infrastructure_id': 'str',
            'cloud_exadata_infrastructure_display_name': 'str',
            'local_storage_in_gbs': 'int',
            'ocpus': 'int',
            'memory_in_gbs': 'int',
            'exadata_storage_in_tbs': 'float',
            'cloud_autonomous_vm_clusters': 'list[CloudAutonomousVmClusterResourceDetails]'
        }

        self.attribute_map = {
            'cloud_exadata_infrastructure_id': 'cloudExadataInfrastructureId',
            'cloud_exadata_infrastructure_display_name': 'cloudExadataInfrastructureDisplayName',
            'local_storage_in_gbs': 'localStorageInGbs',
            'ocpus': 'ocpus',
            'memory_in_gbs': 'memoryInGBs',
            'exadata_storage_in_tbs': 'exadataStorageInTBs',
            'cloud_autonomous_vm_clusters': 'cloudAutonomousVmClusters'
        }

        self._cloud_exadata_infrastructure_id = None
        self._cloud_exadata_infrastructure_display_name = None
        self._local_storage_in_gbs = None
        self._ocpus = None
        self._memory_in_gbs = None
        self._exadata_storage_in_tbs = None
        self._cloud_autonomous_vm_clusters = None

    @property
    def cloud_exadata_infrastructure_id(self):
        """
        **[Required]** Gets the cloud_exadata_infrastructure_id of this CloudExadataInfrastructureUnallocatedResources.
        The `OCID`__ of the Cloud Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The cloud_exadata_infrastructure_id of this CloudExadataInfrastructureUnallocatedResources.
        :rtype: str
        """
        return self._cloud_exadata_infrastructure_id

    @cloud_exadata_infrastructure_id.setter
    def cloud_exadata_infrastructure_id(self, cloud_exadata_infrastructure_id):
        """
        Sets the cloud_exadata_infrastructure_id of this CloudExadataInfrastructureUnallocatedResources.
        The `OCID`__ of the Cloud Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param cloud_exadata_infrastructure_id: The cloud_exadata_infrastructure_id of this CloudExadataInfrastructureUnallocatedResources.
        :type: str
        """
        self._cloud_exadata_infrastructure_id = cloud_exadata_infrastructure_id

    @property
    def cloud_exadata_infrastructure_display_name(self):
        """
        **[Required]** Gets the cloud_exadata_infrastructure_display_name of this CloudExadataInfrastructureUnallocatedResources.
        The user-friendly name for the Cloud Exadata infrastructure. The name does not need to be unique.


        :return: The cloud_exadata_infrastructure_display_name of this CloudExadataInfrastructureUnallocatedResources.
        :rtype: str
        """
        return self._cloud_exadata_infrastructure_display_name

    @cloud_exadata_infrastructure_display_name.setter
    def cloud_exadata_infrastructure_display_name(self, cloud_exadata_infrastructure_display_name):
        """
        Sets the cloud_exadata_infrastructure_display_name of this CloudExadataInfrastructureUnallocatedResources.
        The user-friendly name for the Cloud Exadata infrastructure. The name does not need to be unique.


        :param cloud_exadata_infrastructure_display_name: The cloud_exadata_infrastructure_display_name of this CloudExadataInfrastructureUnallocatedResources.
        :type: str
        """
        self._cloud_exadata_infrastructure_display_name = cloud_exadata_infrastructure_display_name

    @property
    def local_storage_in_gbs(self):
        """
        Gets the local_storage_in_gbs of this CloudExadataInfrastructureUnallocatedResources.
        The minimum amount of un allocated storage that is available across all nodes in the infrastructure.


        :return: The local_storage_in_gbs of this CloudExadataInfrastructureUnallocatedResources.
        :rtype: int
        """
        return self._local_storage_in_gbs

    @local_storage_in_gbs.setter
    def local_storage_in_gbs(self, local_storage_in_gbs):
        """
        Sets the local_storage_in_gbs of this CloudExadataInfrastructureUnallocatedResources.
        The minimum amount of un allocated storage that is available across all nodes in the infrastructure.


        :param local_storage_in_gbs: The local_storage_in_gbs of this CloudExadataInfrastructureUnallocatedResources.
        :type: int
        """
        self._local_storage_in_gbs = local_storage_in_gbs

    @property
    def ocpus(self):
        """
        Gets the ocpus of this CloudExadataInfrastructureUnallocatedResources.
        The minimum amount of un allocated ocpus that is available across all nodes in the infrastructure.


        :return: The ocpus of this CloudExadataInfrastructureUnallocatedResources.
        :rtype: int
        """
        return self._ocpus

    @ocpus.setter
    def ocpus(self, ocpus):
        """
        Sets the ocpus of this CloudExadataInfrastructureUnallocatedResources.
        The minimum amount of un allocated ocpus that is available across all nodes in the infrastructure.


        :param ocpus: The ocpus of this CloudExadataInfrastructureUnallocatedResources.
        :type: int
        """
        self._ocpus = ocpus

    @property
    def memory_in_gbs(self):
        """
        Gets the memory_in_gbs of this CloudExadataInfrastructureUnallocatedResources.
        The minimum amount of un allocated memory that is available across all nodes in the infrastructure.


        :return: The memory_in_gbs of this CloudExadataInfrastructureUnallocatedResources.
        :rtype: int
        """
        return self._memory_in_gbs

    @memory_in_gbs.setter
    def memory_in_gbs(self, memory_in_gbs):
        """
        Sets the memory_in_gbs of this CloudExadataInfrastructureUnallocatedResources.
        The minimum amount of un allocated memory that is available across all nodes in the infrastructure.


        :param memory_in_gbs: The memory_in_gbs of this CloudExadataInfrastructureUnallocatedResources.
        :type: int
        """
        self._memory_in_gbs = memory_in_gbs

    @property
    def exadata_storage_in_tbs(self):
        """
        Gets the exadata_storage_in_tbs of this CloudExadataInfrastructureUnallocatedResources.
        Total unallocated exadata storage in the infrastructure in TBs.


        :return: The exadata_storage_in_tbs of this CloudExadataInfrastructureUnallocatedResources.
        :rtype: float
        """
        return self._exadata_storage_in_tbs

    @exadata_storage_in_tbs.setter
    def exadata_storage_in_tbs(self, exadata_storage_in_tbs):
        """
        Sets the exadata_storage_in_tbs of this CloudExadataInfrastructureUnallocatedResources.
        Total unallocated exadata storage in the infrastructure in TBs.


        :param exadata_storage_in_tbs: The exadata_storage_in_tbs of this CloudExadataInfrastructureUnallocatedResources.
        :type: float
        """
        self._exadata_storage_in_tbs = exadata_storage_in_tbs

    @property
    def cloud_autonomous_vm_clusters(self):
        """
        Gets the cloud_autonomous_vm_clusters of this CloudExadataInfrastructureUnallocatedResources.
        The list of Cloud Autonomous VM Clusters on the Infra and their associated unallocated resources details


        :return: The cloud_autonomous_vm_clusters of this CloudExadataInfrastructureUnallocatedResources.
        :rtype: list[oci.database.models.CloudAutonomousVmClusterResourceDetails]
        """
        return self._cloud_autonomous_vm_clusters

    @cloud_autonomous_vm_clusters.setter
    def cloud_autonomous_vm_clusters(self, cloud_autonomous_vm_clusters):
        """
        Sets the cloud_autonomous_vm_clusters of this CloudExadataInfrastructureUnallocatedResources.
        The list of Cloud Autonomous VM Clusters on the Infra and their associated unallocated resources details


        :param cloud_autonomous_vm_clusters: The cloud_autonomous_vm_clusters of this CloudExadataInfrastructureUnallocatedResources.
        :type: list[oci.database.models.CloudAutonomousVmClusterResourceDetails]
        """
        self._cloud_autonomous_vm_clusters = cloud_autonomous_vm_clusters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
