# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkActionResource(object):
    """
    The bulk action resource entity.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BulkActionResource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param identifier:
            The value to assign to the identifier property of this BulkActionResource.
        :type identifier: str

        :param entity_type:
            The value to assign to the entity_type property of this BulkActionResource.
        :type entity_type: str

        :param metadata:
            The value to assign to the metadata property of this BulkActionResource.
        :type metadata: dict(str, str)

        """
        self.swagger_types = {
            'identifier': 'str',
            'entity_type': 'str',
            'metadata': 'dict(str, str)'
        }

        self.attribute_map = {
            'identifier': 'identifier',
            'entity_type': 'entityType',
            'metadata': 'metadata'
        }

        self._identifier = None
        self._entity_type = None
        self._metadata = None

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this BulkActionResource.
        The resource identifier.


        :return: The identifier of this BulkActionResource.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this BulkActionResource.
        The resource identifier.


        :param identifier: The identifier of this BulkActionResource.
        :type: str
        """
        self._identifier = identifier

    @property
    def entity_type(self):
        """
        **[Required]** Gets the entity_type of this BulkActionResource.
        The resource type.


        :return: The entity_type of this BulkActionResource.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this BulkActionResource.
        The resource type.


        :param entity_type: The entity_type of this BulkActionResource.
        :type: str
        """
        self._entity_type = entity_type

    @property
    def metadata(self):
        """
        Gets the metadata of this BulkActionResource.
        Additional information that helps to identity the resource for bulk action.

        DELETE and UPDATE APIs for most resource types only require the resource identifier(ocid).
        But additional metadata is required for some resource types.

        This information is provided in the resource's public API document. It is also
        available through the ListBulkActionResourceTypes API.


        :return: The metadata of this BulkActionResource.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this BulkActionResource.
        Additional information that helps to identity the resource for bulk action.

        DELETE and UPDATE APIs for most resource types only require the resource identifier(ocid).
        But additional metadata is required for some resource types.

        This information is provided in the resource's public API document. It is also
        available through the ListBulkActionResourceTypes API.


        :param metadata: The metadata of this BulkActionResource.
        :type: dict(str, str)
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
