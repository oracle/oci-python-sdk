# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .instance_source_details import InstanceSourceDetails
from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceSourceViaImageDetails(InstanceSourceDetails):

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceSourceViaImageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.InstanceSourceViaImageDetails.source_type` attribute
        of this class is ``image`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this InstanceSourceViaImageDetails.
        :type source_type: str

        :param boot_volume_size_in_gbs:
            The value to assign to the boot_volume_size_in_gbs property of this InstanceSourceViaImageDetails.
        :type boot_volume_size_in_gbs: int

        :param image_id:
            The value to assign to the image_id property of this InstanceSourceViaImageDetails.
        :type image_id: str

        """
        self.swagger_types = {
            'source_type': 'str',
            'boot_volume_size_in_gbs': 'int',
            'image_id': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'boot_volume_size_in_gbs': 'bootVolumeSizeInGBs',
            'image_id': 'imageId'
        }

        self._source_type = None
        self._boot_volume_size_in_gbs = None
        self._image_id = None
        self._source_type = 'image'

    @property
    def boot_volume_size_in_gbs(self):
        """
        Gets the boot_volume_size_in_gbs of this InstanceSourceViaImageDetails.
        The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is 16384 GB (16TB).


        :return: The boot_volume_size_in_gbs of this InstanceSourceViaImageDetails.
        :rtype: int
        """
        return self._boot_volume_size_in_gbs

    @boot_volume_size_in_gbs.setter
    def boot_volume_size_in_gbs(self, boot_volume_size_in_gbs):
        """
        Sets the boot_volume_size_in_gbs of this InstanceSourceViaImageDetails.
        The size of the boot volume in GBs. Minimum value is 50 GB and maximum value is 16384 GB (16TB).


        :param boot_volume_size_in_gbs: The boot_volume_size_in_gbs of this InstanceSourceViaImageDetails.
        :type: int
        """
        self._boot_volume_size_in_gbs = boot_volume_size_in_gbs

    @property
    def image_id(self):
        """
        **[Required]** Gets the image_id of this InstanceSourceViaImageDetails.
        The OCID of the image used to boot the instance.


        :return: The image_id of this InstanceSourceViaImageDetails.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this InstanceSourceViaImageDetails.
        The OCID of the image used to boot the instance.


        :param image_id: The image_id of this InstanceSourceViaImageDetails.
        :type: str
        """
        self._image_id = image_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
