# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .instance_configuration_instance_details import InstanceConfigurationInstanceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeInstanceDetails(InstanceConfigurationInstanceDetails):
    """
    Compute Instance Configuration instance details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeInstanceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.ComputeInstanceDetails.instance_type` attribute
        of this class is ``compute`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param instance_type:
            The value to assign to the instance_type property of this ComputeInstanceDetails.
        :type instance_type: str

        :param block_volumes:
            The value to assign to the block_volumes property of this ComputeInstanceDetails.
        :type block_volumes: list[InstanceConfigurationBlockVolumeDetails]

        :param launch_details:
            The value to assign to the launch_details property of this ComputeInstanceDetails.
        :type launch_details: InstanceConfigurationLaunchInstanceDetails

        :param secondary_vnics:
            The value to assign to the secondary_vnics property of this ComputeInstanceDetails.
        :type secondary_vnics: list[InstanceConfigurationAttachVnicDetails]

        """
        self.swagger_types = {
            'instance_type': 'str',
            'block_volumes': 'list[InstanceConfigurationBlockVolumeDetails]',
            'launch_details': 'InstanceConfigurationLaunchInstanceDetails',
            'secondary_vnics': 'list[InstanceConfigurationAttachVnicDetails]'
        }

        self.attribute_map = {
            'instance_type': 'instanceType',
            'block_volumes': 'blockVolumes',
            'launch_details': 'launchDetails',
            'secondary_vnics': 'secondaryVnics'
        }

        self._instance_type = None
        self._block_volumes = None
        self._launch_details = None
        self._secondary_vnics = None
        self._instance_type = 'compute'

    @property
    def block_volumes(self):
        """
        Gets the block_volumes of this ComputeInstanceDetails.

        :return: The block_volumes of this ComputeInstanceDetails.
        :rtype: list[InstanceConfigurationBlockVolumeDetails]
        """
        return self._block_volumes

    @block_volumes.setter
    def block_volumes(self, block_volumes):
        """
        Sets the block_volumes of this ComputeInstanceDetails.

        :param block_volumes: The block_volumes of this ComputeInstanceDetails.
        :type: list[InstanceConfigurationBlockVolumeDetails]
        """
        self._block_volumes = block_volumes

    @property
    def launch_details(self):
        """
        Gets the launch_details of this ComputeInstanceDetails.

        :return: The launch_details of this ComputeInstanceDetails.
        :rtype: InstanceConfigurationLaunchInstanceDetails
        """
        return self._launch_details

    @launch_details.setter
    def launch_details(self, launch_details):
        """
        Sets the launch_details of this ComputeInstanceDetails.

        :param launch_details: The launch_details of this ComputeInstanceDetails.
        :type: InstanceConfigurationLaunchInstanceDetails
        """
        self._launch_details = launch_details

    @property
    def secondary_vnics(self):
        """
        Gets the secondary_vnics of this ComputeInstanceDetails.

        :return: The secondary_vnics of this ComputeInstanceDetails.
        :rtype: list[InstanceConfigurationAttachVnicDetails]
        """
        return self._secondary_vnics

    @secondary_vnics.setter
    def secondary_vnics(self, secondary_vnics):
        """
        Sets the secondary_vnics of this ComputeInstanceDetails.

        :param secondary_vnics: The secondary_vnics of this ComputeInstanceDetails.
        :type: list[InstanceConfigurationAttachVnicDetails]
        """
        self._secondary_vnics = secondary_vnics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
