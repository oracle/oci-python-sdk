# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .instance_configuration_instance_source_details import InstanceConfigurationInstanceSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationInstanceSourceViaImageDetails(InstanceConfigurationInstanceSourceDetails):
    """
    InstanceConfigurationInstanceSourceViaImageDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationInstanceSourceViaImageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.InstanceConfigurationInstanceSourceViaImageDetails.source_type` attribute
        of this class is ``image`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this InstanceConfigurationInstanceSourceViaImageDetails.
        :type source_type: str

        :param boot_volume_size_in_gbs:
            The value to assign to the boot_volume_size_in_gbs property of this InstanceConfigurationInstanceSourceViaImageDetails.
        :type boot_volume_size_in_gbs: int

        :param image_id:
            The value to assign to the image_id property of this InstanceConfigurationInstanceSourceViaImageDetails.
        :type image_id: str

        :param boot_volume_vpus_per_gb:
            The value to assign to the boot_volume_vpus_per_gb property of this InstanceConfigurationInstanceSourceViaImageDetails.
        :type boot_volume_vpus_per_gb: int

        """
        self.swagger_types = {
            'source_type': 'str',
            'boot_volume_size_in_gbs': 'int',
            'image_id': 'str',
            'boot_volume_vpus_per_gb': 'int'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'boot_volume_size_in_gbs': 'bootVolumeSizeInGBs',
            'image_id': 'imageId',
            'boot_volume_vpus_per_gb': 'bootVolumeVpusPerGB'
        }

        self._source_type = None
        self._boot_volume_size_in_gbs = None
        self._image_id = None
        self._boot_volume_vpus_per_gb = None
        self._source_type = 'image'

    @property
    def boot_volume_size_in_gbs(self):
        """
        Gets the boot_volume_size_in_gbs of this InstanceConfigurationInstanceSourceViaImageDetails.
        The size of the boot volume in GBs. The minimum value is 50 GB and the maximum
        value is 32,768 GB (32 TB).


        :return: The boot_volume_size_in_gbs of this InstanceConfigurationInstanceSourceViaImageDetails.
        :rtype: int
        """
        return self._boot_volume_size_in_gbs

    @boot_volume_size_in_gbs.setter
    def boot_volume_size_in_gbs(self, boot_volume_size_in_gbs):
        """
        Sets the boot_volume_size_in_gbs of this InstanceConfigurationInstanceSourceViaImageDetails.
        The size of the boot volume in GBs. The minimum value is 50 GB and the maximum
        value is 32,768 GB (32 TB).


        :param boot_volume_size_in_gbs: The boot_volume_size_in_gbs of this InstanceConfigurationInstanceSourceViaImageDetails.
        :type: int
        """
        self._boot_volume_size_in_gbs = boot_volume_size_in_gbs

    @property
    def image_id(self):
        """
        Gets the image_id of this InstanceConfigurationInstanceSourceViaImageDetails.
        The OCID of the image used to boot the instance.


        :return: The image_id of this InstanceConfigurationInstanceSourceViaImageDetails.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this InstanceConfigurationInstanceSourceViaImageDetails.
        The OCID of the image used to boot the instance.


        :param image_id: The image_id of this InstanceConfigurationInstanceSourceViaImageDetails.
        :type: str
        """
        self._image_id = image_id

    @property
    def boot_volume_vpus_per_gb(self):
        """
        Gets the boot_volume_vpus_per_gb of this InstanceConfigurationInstanceSourceViaImageDetails.
        The number of volume performance units (VPUs) that will be applied to this volume per GB,
        representing the Block Volume service's elastic performance options.
        See `Block Volume Performance Levels`__ for more information.

        Allowed values:

          * `10`: Represents Balanced option.

          * `20`: Represents Higher Performance option.

          * `30`-`120`: Represents the Ultra High Performance option.

        For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels


        :return: The boot_volume_vpus_per_gb of this InstanceConfigurationInstanceSourceViaImageDetails.
        :rtype: int
        """
        return self._boot_volume_vpus_per_gb

    @boot_volume_vpus_per_gb.setter
    def boot_volume_vpus_per_gb(self, boot_volume_vpus_per_gb):
        """
        Sets the boot_volume_vpus_per_gb of this InstanceConfigurationInstanceSourceViaImageDetails.
        The number of volume performance units (VPUs) that will be applied to this volume per GB,
        representing the Block Volume service's elastic performance options.
        See `Block Volume Performance Levels`__ for more information.

        Allowed values:

          * `10`: Represents Balanced option.

          * `20`: Represents Higher Performance option.

          * `30`-`120`: Represents the Ultra High Performance option.

        For performance autotune enabled volumes, it would be the Default(Minimum) VPUs/GB.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels


        :param boot_volume_vpus_per_gb: The boot_volume_vpus_per_gb of this InstanceConfigurationInstanceSourceViaImageDetails.
        :type: int
        """
        self._boot_volume_vpus_per_gb = boot_volume_vpus_per_gb

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
