# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ShapeMaxVnicAttachmentOptions(object):
    """
    The possible configurations for the number of VNIC attachments available to an instance of this shape. If this field is null, then all instances of this shape have a fixed maximum number of VNIC attachments equal to `maxVnicAttachments`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ShapeMaxVnicAttachmentOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param min:
            The value to assign to the min property of this ShapeMaxVnicAttachmentOptions.
        :type min: int

        :param max:
            The value to assign to the max property of this ShapeMaxVnicAttachmentOptions.
        :type max: float

        :param default_per_ocpu:
            The value to assign to the default_per_ocpu property of this ShapeMaxVnicAttachmentOptions.
        :type default_per_ocpu: float

        """
        self.swagger_types = {
            'min': 'int',
            'max': 'float',
            'default_per_ocpu': 'float'
        }

        self.attribute_map = {
            'min': 'min',
            'max': 'max',
            'default_per_ocpu': 'defaultPerOcpu'
        }

        self._min = None
        self._max = None
        self._default_per_ocpu = None

    @property
    def min(self):
        """
        Gets the min of this ShapeMaxVnicAttachmentOptions.
        The lowest maximum value of VNIC attachments.


        :return: The min of this ShapeMaxVnicAttachmentOptions.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this ShapeMaxVnicAttachmentOptions.
        The lowest maximum value of VNIC attachments.


        :param min: The min of this ShapeMaxVnicAttachmentOptions.
        :type: int
        """
        self._min = min

    @property
    def max(self):
        """
        Gets the max of this ShapeMaxVnicAttachmentOptions.
        The highest maximum value of VNIC attachments.


        :return: The max of this ShapeMaxVnicAttachmentOptions.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this ShapeMaxVnicAttachmentOptions.
        The highest maximum value of VNIC attachments.


        :param max: The max of this ShapeMaxVnicAttachmentOptions.
        :type: float
        """
        self._max = max

    @property
    def default_per_ocpu(self):
        """
        Gets the default_per_ocpu of this ShapeMaxVnicAttachmentOptions.
        The default number of VNIC attachments allowed per OCPU.


        :return: The default_per_ocpu of this ShapeMaxVnicAttachmentOptions.
        :rtype: float
        """
        return self._default_per_ocpu

    @default_per_ocpu.setter
    def default_per_ocpu(self, default_per_ocpu):
        """
        Sets the default_per_ocpu of this ShapeMaxVnicAttachmentOptions.
        The default number of VNIC attachments allowed per OCPU.


        :param default_per_ocpu: The default_per_ocpu of this ShapeMaxVnicAttachmentOptions.
        :type: float
        """
        self._default_per_ocpu = default_per_ocpu

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
