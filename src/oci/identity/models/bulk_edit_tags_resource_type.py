# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkEditTagsResourceType(object):
    """
    BulkEditTagsResourceType model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BulkEditTagsResourceType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_type:
            The value to assign to the resource_type property of this BulkEditTagsResourceType.
        :type resource_type: str

        :param metadata_keys:
            The value to assign to the metadata_keys property of this BulkEditTagsResourceType.
        :type metadata_keys: list[str]

        """
        self.swagger_types = {
            'resource_type': 'str',
            'metadata_keys': 'list[str]'
        }

        self.attribute_map = {
            'resource_type': 'resourceType',
            'metadata_keys': 'metadataKeys'
        }

        self._resource_type = None
        self._metadata_keys = None

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this BulkEditTagsResourceType.
        The unique name of the resource type.


        :return: The resource_type of this BulkEditTagsResourceType.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this BulkEditTagsResourceType.
        The unique name of the resource type.


        :param resource_type: The resource_type of this BulkEditTagsResourceType.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def metadata_keys(self):
        """
        Gets the metadata_keys of this BulkEditTagsResourceType.
        The metadata keys required to identify the resource.

        For example, for a bucket, the value of `metadataKeys` will be `\"namespaceName\", \"bucketName\"].
        This information will match the API documentation.
        See [UpdateBucket`__ and
        `DeleteBucket`__.

        __ https://docs.cloud.oracle.com/api/#/en/objectstorage/latest/Bucket/UpdateBucket
        __ https://docs.cloud.oracle.com/api/#/en/objectstorage/latest/Bucket/DeleteBucket


        :return: The metadata_keys of this BulkEditTagsResourceType.
        :rtype: list[str]
        """
        return self._metadata_keys

    @metadata_keys.setter
    def metadata_keys(self, metadata_keys):
        """
        Sets the metadata_keys of this BulkEditTagsResourceType.
        The metadata keys required to identify the resource.

        For example, for a bucket, the value of `metadataKeys` will be `\"namespaceName\", \"bucketName\"].
        This information will match the API documentation.
        See [UpdateBucket`__ and
        `DeleteBucket`__.

        __ https://docs.cloud.oracle.com/api/#/en/objectstorage/latest/Bucket/UpdateBucket
        __ https://docs.cloud.oracle.com/api/#/en/objectstorage/latest/Bucket/DeleteBucket


        :param metadata_keys: The metadata_keys of this BulkEditTagsResourceType.
        :type: list[str]
        """
        self._metadata_keys = metadata_keys

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
