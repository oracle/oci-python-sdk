# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .input_location import InputLocation
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectListInlineInputLocation(InputLocation):
    """
    A list of object locations in Object Storage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectListInlineInputLocation object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_vision.models.ObjectListInlineInputLocation.source_type` attribute
        of this class is ``OBJECT_LIST_INLINE_INPUT_LOCATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this ObjectListInlineInputLocation.
            Allowed values for this property are: "OBJECT_LIST_INLINE_INPUT_LOCATION"
        :type source_type: str

        :param object_locations:
            The value to assign to the object_locations property of this ObjectListInlineInputLocation.
        :type object_locations: list[oci.ai_vision.models.ObjectLocation]

        """
        self.swagger_types = {
            'source_type': 'str',
            'object_locations': 'list[ObjectLocation]'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'object_locations': 'objectLocations'
        }

        self._source_type = None
        self._object_locations = None
        self._source_type = 'OBJECT_LIST_INLINE_INPUT_LOCATION'

    @property
    def object_locations(self):
        """
        **[Required]** Gets the object_locations of this ObjectListInlineInputLocation.
        List of ObjectLocations.


        :return: The object_locations of this ObjectListInlineInputLocation.
        :rtype: list[oci.ai_vision.models.ObjectLocation]
        """
        return self._object_locations

    @object_locations.setter
    def object_locations(self, object_locations):
        """
        Sets the object_locations of this ObjectListInlineInputLocation.
        List of ObjectLocations.


        :param object_locations: The object_locations of this ObjectListInlineInputLocation.
        :type: list[oci.ai_vision.models.ObjectLocation]
        """
        self._object_locations = object_locations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
