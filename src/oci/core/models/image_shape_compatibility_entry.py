# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageShapeCompatibilityEntry(object):
    """
    An image and shape that are compatible.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImageShapeCompatibilityEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param image_id:
            The value to assign to the image_id property of this ImageShapeCompatibilityEntry.
        :type image_id: str

        :param shape:
            The value to assign to the shape property of this ImageShapeCompatibilityEntry.
        :type shape: str

        :param ocpu_constraints:
            The value to assign to the ocpu_constraints property of this ImageShapeCompatibilityEntry.
        :type ocpu_constraints: ImageOcpuConstraints

        """
        self.swagger_types = {
            'image_id': 'str',
            'shape': 'str',
            'ocpu_constraints': 'ImageOcpuConstraints'
        }

        self.attribute_map = {
            'image_id': 'imageId',
            'shape': 'shape',
            'ocpu_constraints': 'ocpuConstraints'
        }

        self._image_id = None
        self._shape = None
        self._ocpu_constraints = None

    @property
    def image_id(self):
        """
        **[Required]** Gets the image_id of this ImageShapeCompatibilityEntry.
        The image OCID.


        :return: The image_id of this ImageShapeCompatibilityEntry.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this ImageShapeCompatibilityEntry.
        The image OCID.


        :param image_id: The image_id of this ImageShapeCompatibilityEntry.
        :type: str
        """
        self._image_id = image_id

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this ImageShapeCompatibilityEntry.
        The shape name.


        :return: The shape of this ImageShapeCompatibilityEntry.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this ImageShapeCompatibilityEntry.
        The shape name.


        :param shape: The shape of this ImageShapeCompatibilityEntry.
        :type: str
        """
        self._shape = shape

    @property
    def ocpu_constraints(self):
        """
        Gets the ocpu_constraints of this ImageShapeCompatibilityEntry.

        :return: The ocpu_constraints of this ImageShapeCompatibilityEntry.
        :rtype: ImageOcpuConstraints
        """
        return self._ocpu_constraints

    @ocpu_constraints.setter
    def ocpu_constraints(self, ocpu_constraints):
        """
        Sets the ocpu_constraints of this ImageShapeCompatibilityEntry.

        :param ocpu_constraints: The ocpu_constraints of this ImageShapeCompatibilityEntry.
        :type: ImageOcpuConstraints
        """
        self._ocpu_constraints = ocpu_constraints

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
