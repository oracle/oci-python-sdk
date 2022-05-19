# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StorageLocation(object):
    """
    Properties that point to a specific object in Object Storage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StorageLocation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param region_id:
            The value to assign to the region_id property of this StorageLocation.
        :type region_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this StorageLocation.
        :type compartment_id: str

        :param namespace_name:
            The value to assign to the namespace_name property of this StorageLocation.
        :type namespace_name: str

        :param bucket_name:
            The value to assign to the bucket_name property of this StorageLocation.
        :type bucket_name: str

        :param object_name:
            The value to assign to the object_name property of this StorageLocation.
        :type object_name: str

        """
        self.swagger_types = {
            'region_id': 'str',
            'compartment_id': 'str',
            'namespace_name': 'str',
            'bucket_name': 'str',
            'object_name': 'str'
        }

        self.attribute_map = {
            'region_id': 'regionId',
            'compartment_id': 'compartmentId',
            'namespace_name': 'namespaceName',
            'bucket_name': 'bucketName',
            'object_name': 'objectName'
        }

        self._region_id = None
        self._compartment_id = None
        self._namespace_name = None
        self._bucket_name = None
        self._object_name = None

    @property
    def region_id(self):
        """
        **[Required]** Gets the region_id of this StorageLocation.
        The region id.


        :return: The region_id of this StorageLocation.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """
        Sets the region_id of this StorageLocation.
        The region id.


        :param region_id: The region_id of this StorageLocation.
        :type: str
        """
        self._region_id = region_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this StorageLocation.
        The unique identifier for the compartment.


        :return: The compartment_id of this StorageLocation.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this StorageLocation.
        The unique identifier for the compartment.


        :param compartment_id: The compartment_id of this StorageLocation.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def namespace_name(self):
        """
        **[Required]** Gets the namespace_name of this StorageLocation.
        The Object Storage namespace.


        :return: The namespace_name of this StorageLocation.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this StorageLocation.
        The Object Storage namespace.


        :param namespace_name: The namespace_name of this StorageLocation.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this StorageLocation.
        The name of the bucket.


        :return: The bucket_name of this StorageLocation.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this StorageLocation.
        The name of the bucket.


        :param bucket_name: The bucket_name of this StorageLocation.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this StorageLocation.
        The name of the object.


        :return: The object_name of this StorageLocation.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this StorageLocation.
        The name of the object.


        :param object_name: The object_name of this StorageLocation.
        :type: str
        """
        self._object_name = object_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
