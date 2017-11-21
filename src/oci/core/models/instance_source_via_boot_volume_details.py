# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .instance_source_details import InstanceSourceDetails
from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceSourceViaBootVolumeDetails(InstanceSourceDetails):

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceSourceViaBootVolumeDetails object with values from values from keyword arguments. The default value of the :py:attr:`~oci.core.models.InstanceSourceViaBootVolumeDetails.source_type` attribute
        of this class is ``bootVolume`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this InstanceSourceViaBootVolumeDetails.
        :type source_type: str

        :param boot_volume_id:
            The value to assign to the boot_volume_id property of this InstanceSourceViaBootVolumeDetails.
        :type boot_volume_id: str

        """
        self.swagger_types = {
            'source_type': 'str',
            'boot_volume_id': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'boot_volume_id': 'bootVolumeId'
        }

        self._source_type = None
        self._boot_volume_id = None
        self._source_type = 'bootVolume'

    @property
    def boot_volume_id(self):
        """
        Gets the boot_volume_id of this InstanceSourceViaBootVolumeDetails.
        The OCID of the boot volume used to boot the instance.


        :return: The boot_volume_id of this InstanceSourceViaBootVolumeDetails.
        :rtype: str
        """
        return self._boot_volume_id

    @boot_volume_id.setter
    def boot_volume_id(self, boot_volume_id):
        """
        Sets the boot_volume_id of this InstanceSourceViaBootVolumeDetails.
        The OCID of the boot volume used to boot the instance.


        :param boot_volume_id: The boot_volume_id of this InstanceSourceViaBootVolumeDetails.
        :type: str
        """
        self._boot_volume_id = boot_volume_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
