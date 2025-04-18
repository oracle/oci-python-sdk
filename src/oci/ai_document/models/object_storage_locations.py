# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221109

from .input_location import InputLocation
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectStorageLocations(InputLocation):
    """
    A list of object locations in Object Storage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectStorageLocations object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_document.models.ObjectStorageLocations.source_type` attribute
        of this class is ``OBJECT_STORAGE_LOCATIONS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this ObjectStorageLocations.
            Allowed values for this property are: "OBJECT_STORAGE_LOCATIONS", "INLINE_DOCUMENT_CONTENT"
        :type source_type: str

        :param object_locations:
            The value to assign to the object_locations property of this ObjectStorageLocations.
        :type object_locations: list[oci.ai_document.models.ObjectLocation]

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
        self._source_type = 'OBJECT_STORAGE_LOCATIONS'

    @property
    def object_locations(self):
        """
        **[Required]** Gets the object_locations of this ObjectStorageLocations.
        The list of ObjectLocations.


        :return: The object_locations of this ObjectStorageLocations.
        :rtype: list[oci.ai_document.models.ObjectLocation]
        """
        return self._object_locations

    @object_locations.setter
    def object_locations(self, object_locations):
        """
        Sets the object_locations of this ObjectStorageLocations.
        The list of ObjectLocations.


        :param object_locations: The object_locations of this ObjectStorageLocations.
        :type: list[oci.ai_document.models.ObjectLocation]
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
