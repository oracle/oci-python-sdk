# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PipelineInfrastructureConfigurationDetails(object):
    """
    The infrastructure configuration details of a pipeline or a step.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PipelineInfrastructureConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param shape_name:
            The value to assign to the shape_name property of this PipelineInfrastructureConfigurationDetails.
        :type shape_name: str

        :param block_storage_size_in_gbs:
            The value to assign to the block_storage_size_in_gbs property of this PipelineInfrastructureConfigurationDetails.
        :type block_storage_size_in_gbs: int

        :param subnet_id:
            The value to assign to the subnet_id property of this PipelineInfrastructureConfigurationDetails.
        :type subnet_id: str

        :param shape_config_details:
            The value to assign to the shape_config_details property of this PipelineInfrastructureConfigurationDetails.
        :type shape_config_details: oci.data_science.models.PipelineShapeConfigDetails

        """
        self.swagger_types = {
            'shape_name': 'str',
            'block_storage_size_in_gbs': 'int',
            'subnet_id': 'str',
            'shape_config_details': 'PipelineShapeConfigDetails'
        }
        self.attribute_map = {
            'shape_name': 'shapeName',
            'block_storage_size_in_gbs': 'blockStorageSizeInGBs',
            'subnet_id': 'subnetId',
            'shape_config_details': 'shapeConfigDetails'
        }
        self._shape_name = None
        self._block_storage_size_in_gbs = None
        self._subnet_id = None
        self._shape_config_details = None

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this PipelineInfrastructureConfigurationDetails.
        The shape used to launch the instance for all step runs in the pipeline.


        :return: The shape_name of this PipelineInfrastructureConfigurationDetails.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this PipelineInfrastructureConfigurationDetails.
        The shape used to launch the instance for all step runs in the pipeline.


        :param shape_name: The shape_name of this PipelineInfrastructureConfigurationDetails.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def block_storage_size_in_gbs(self):
        """
        **[Required]** Gets the block_storage_size_in_gbs of this PipelineInfrastructureConfigurationDetails.
        The size of the block storage volume to attach to the instance.


        :return: The block_storage_size_in_gbs of this PipelineInfrastructureConfigurationDetails.
        :rtype: int
        """
        return self._block_storage_size_in_gbs

    @block_storage_size_in_gbs.setter
    def block_storage_size_in_gbs(self, block_storage_size_in_gbs):
        """
        Sets the block_storage_size_in_gbs of this PipelineInfrastructureConfigurationDetails.
        The size of the block storage volume to attach to the instance.


        :param block_storage_size_in_gbs: The block_storage_size_in_gbs of this PipelineInfrastructureConfigurationDetails.
        :type: int
        """
        self._block_storage_size_in_gbs = block_storage_size_in_gbs

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this PipelineInfrastructureConfigurationDetails.
        The subnet to create a secondary vnic in to attach to the instance running the pipeline step.


        :return: The subnet_id of this PipelineInfrastructureConfigurationDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this PipelineInfrastructureConfigurationDetails.
        The subnet to create a secondary vnic in to attach to the instance running the pipeline step.


        :param subnet_id: The subnet_id of this PipelineInfrastructureConfigurationDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def shape_config_details(self):
        """
        Gets the shape_config_details of this PipelineInfrastructureConfigurationDetails.

        :return: The shape_config_details of this PipelineInfrastructureConfigurationDetails.
        :rtype: oci.data_science.models.PipelineShapeConfigDetails
        """
        return self._shape_config_details

    @shape_config_details.setter
    def shape_config_details(self, shape_config_details):
        """
        Sets the shape_config_details of this PipelineInfrastructureConfigurationDetails.

        :param shape_config_details: The shape_config_details of this PipelineInfrastructureConfigurationDetails.
        :type: oci.data_science.models.PipelineShapeConfigDetails
        """
        self._shape_config_details = shape_config_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
