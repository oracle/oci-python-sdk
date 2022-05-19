# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceTypeMetadata(object):
    """
    Describes resources of a given type within a package.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceTypeMetadata object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_type:
            The value to assign to the resource_type property of this ResourceTypeMetadata.
        :type resource_type: str

        :param properties:
            The value to assign to the properties property of this ResourceTypeMetadata.
        :type properties: list[oci.oda.models.MetadataProperty]

        """
        self.swagger_types = {
            'resource_type': 'str',
            'properties': 'list[MetadataProperty]'
        }

        self.attribute_map = {
            'resource_type': 'resourceType',
            'properties': 'properties'
        }

        self._resource_type = None
        self._properties = None

    @property
    def resource_type(self):
        """
        Gets the resource_type of this ResourceTypeMetadata.
        The type of the resource described by this metadata object.


        :return: The resource_type of this ResourceTypeMetadata.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this ResourceTypeMetadata.
        The type of the resource described by this metadata object.


        :param resource_type: The resource_type of this ResourceTypeMetadata.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def properties(self):
        """
        Gets the properties of this ResourceTypeMetadata.
        Any properties needed to describe the content and its usage for this resource type, and within the containing package.


        :return: The properties of this ResourceTypeMetadata.
        :rtype: list[oci.oda.models.MetadataProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this ResourceTypeMetadata.
        Any properties needed to describe the content and its usage for this resource type, and within the containing package.


        :param properties: The properties of this ResourceTypeMetadata.
        :type: list[oci.oda.models.MetadataProperty]
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
