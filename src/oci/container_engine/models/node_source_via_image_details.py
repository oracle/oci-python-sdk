# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .node_source_details import NodeSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodeSourceViaImageDetails(NodeSourceDetails):
    """
    Details of the image running on the node.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NodeSourceViaImageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.container_engine.models.NodeSourceViaImageDetails.source_type` attribute
        of this class is ``IMAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this NodeSourceViaImageDetails.
            Allowed values for this property are: "IMAGE"
        :type source_type: str

        :param image_id:
            The value to assign to the image_id property of this NodeSourceViaImageDetails.
        :type image_id: str

        :param boot_volume_size_in_gbs:
            The value to assign to the boot_volume_size_in_gbs property of this NodeSourceViaImageDetails.
        :type boot_volume_size_in_gbs: int

        """
        self.swagger_types = {
            'source_type': 'str',
            'image_id': 'str',
            'boot_volume_size_in_gbs': 'int'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'image_id': 'imageId',
            'boot_volume_size_in_gbs': 'bootVolumeSizeInGBs'
        }

        self._source_type = None
        self._image_id = None
        self._boot_volume_size_in_gbs = None
        self._source_type = 'IMAGE'

    @property
    def image_id(self):
        """
        **[Required]** Gets the image_id of this NodeSourceViaImageDetails.
        The OCID of the image used to boot the node.


        :return: The image_id of this NodeSourceViaImageDetails.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this NodeSourceViaImageDetails.
        The OCID of the image used to boot the node.


        :param image_id: The image_id of this NodeSourceViaImageDetails.
        :type: str
        """
        self._image_id = image_id

    @property
    def boot_volume_size_in_gbs(self):
        """
        Gets the boot_volume_size_in_gbs of this NodeSourceViaImageDetails.
        The size of the boot volume in GBs. Minimum value is 50 GB. See `here`__ for max custom boot volume sizing and OS-specific requirements.

        __ https://docs.cloud.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumes.htm


        :return: The boot_volume_size_in_gbs of this NodeSourceViaImageDetails.
        :rtype: int
        """
        return self._boot_volume_size_in_gbs

    @boot_volume_size_in_gbs.setter
    def boot_volume_size_in_gbs(self, boot_volume_size_in_gbs):
        """
        Sets the boot_volume_size_in_gbs of this NodeSourceViaImageDetails.
        The size of the boot volume in GBs. Minimum value is 50 GB. See `here`__ for max custom boot volume sizing and OS-specific requirements.

        __ https://docs.cloud.oracle.com/en-us/iaas/Content/Block/Concepts/bootvolumes.htm


        :param boot_volume_size_in_gbs: The boot_volume_size_in_gbs of this NodeSourceViaImageDetails.
        :type: int
        """
        self._boot_volume_size_in_gbs = boot_volume_size_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
