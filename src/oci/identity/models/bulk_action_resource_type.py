# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkActionResourceType(object):
    """
    BulkActionResourceType model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BulkActionResourceType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this BulkActionResourceType.
        :type name: str

        :param metadata_keys:
            The value to assign to the metadata_keys property of this BulkActionResourceType.
        :type metadata_keys: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'metadata_keys': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'metadata_keys': 'metadataKeys'
        }

        self._name = None
        self._metadata_keys = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this BulkActionResourceType.
        The unique name of the resource-type.


        :return: The name of this BulkActionResourceType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BulkActionResourceType.
        The unique name of the resource-type.


        :param name: The name of this BulkActionResourceType.
        :type: str
        """
        self._name = name

    @property
    def metadata_keys(self):
        """
        Gets the metadata_keys of this BulkActionResourceType.
        List of metadata keys required to identify a specific resource. Some resource-types require information besides an OCID to identify
        a specific resource. For example, the resource-type `buckets` requires metadataKeys :func:`delete_bucket`.


        :return: The metadata_keys of this BulkActionResourceType.
        :rtype: list[str]
        """
        return self._metadata_keys

    @metadata_keys.setter
    def metadata_keys(self, metadata_keys):
        """
        Sets the metadata_keys of this BulkActionResourceType.
        List of metadata keys required to identify a specific resource. Some resource-types require information besides an OCID to identify
        a specific resource. For example, the resource-type `buckets` requires metadataKeys :func:`delete_bucket`.


        :param metadata_keys: The metadata_keys of this BulkActionResourceType.
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
