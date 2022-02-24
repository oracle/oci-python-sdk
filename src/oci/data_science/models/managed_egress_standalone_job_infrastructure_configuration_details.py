# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .job_infrastructure_configuration_details import JobInfrastructureConfigurationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedEgressStandaloneJobInfrastructureConfigurationDetails(JobInfrastructureConfigurationDetails):
    """
    The standalone job infrastructure configuration with network egress settings preconfigured.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedEgressStandaloneJobInfrastructureConfigurationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.ManagedEgressStandaloneJobInfrastructureConfigurationDetails.job_infrastructure_type` attribute
        of this class is ``ME_STANDALONE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param job_infrastructure_type:
            The value to assign to the job_infrastructure_type property of this ManagedEgressStandaloneJobInfrastructureConfigurationDetails.
            Allowed values for this property are: "STANDALONE", "ME_STANDALONE"
        :type job_infrastructure_type: str

        :param shape_name:
            The value to assign to the shape_name property of this ManagedEgressStandaloneJobInfrastructureConfigurationDetails.
        :type shape_name: str

        :param block_storage_size_in_gbs:
            The value to assign to the block_storage_size_in_gbs property of this ManagedEgressStandaloneJobInfrastructureConfigurationDetails.
        :type block_storage_size_in_gbs: int

        """
        self.swagger_types = {
            'job_infrastructure_type': 'str',
            'shape_name': 'str',
            'block_storage_size_in_gbs': 'int'
        }

        self.attribute_map = {
            'job_infrastructure_type': 'jobInfrastructureType',
            'shape_name': 'shapeName',
            'block_storage_size_in_gbs': 'blockStorageSizeInGBs'
        }

        self._job_infrastructure_type = None
        self._shape_name = None
        self._block_storage_size_in_gbs = None
        self._job_infrastructure_type = 'ME_STANDALONE'

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this ManagedEgressStandaloneJobInfrastructureConfigurationDetails.
        The shape used to launch the job run instances.


        :return: The shape_name of this ManagedEgressStandaloneJobInfrastructureConfigurationDetails.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this ManagedEgressStandaloneJobInfrastructureConfigurationDetails.
        The shape used to launch the job run instances.


        :param shape_name: The shape_name of this ManagedEgressStandaloneJobInfrastructureConfigurationDetails.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def block_storage_size_in_gbs(self):
        """
        **[Required]** Gets the block_storage_size_in_gbs of this ManagedEgressStandaloneJobInfrastructureConfigurationDetails.
        The size of the block storage volume to attach to the instance running the job


        :return: The block_storage_size_in_gbs of this ManagedEgressStandaloneJobInfrastructureConfigurationDetails.
        :rtype: int
        """
        return self._block_storage_size_in_gbs

    @block_storage_size_in_gbs.setter
    def block_storage_size_in_gbs(self, block_storage_size_in_gbs):
        """
        Sets the block_storage_size_in_gbs of this ManagedEgressStandaloneJobInfrastructureConfigurationDetails.
        The size of the block storage volume to attach to the instance running the job


        :param block_storage_size_in_gbs: The block_storage_size_in_gbs of this ManagedEgressStandaloneJobInfrastructureConfigurationDetails.
        :type: int
        """
        self._block_storage_size_in_gbs = block_storage_size_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
