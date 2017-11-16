# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .instance_source_details import InstanceSourceDetails
from ...util import formatted_flat_dict


class InstanceSourceViaImageDetails(InstanceSourceDetails):

    def __init__(self):

        self.swagger_types = {
            'source_type': 'str',
            'image_id': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'image_id': 'imageId'
        }

        self._source_type = None
        self._image_id = None
        self._source_type = 'image'

    @property
    def image_id(self):
        """
        Gets the image_id of this InstanceSourceViaImageDetails.
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
