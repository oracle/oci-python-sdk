# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .image_details import ImageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectStorageImageDetails(ImageDetails):
    """
    The image residing in OCI Object Storage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectStorageImageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_vision.models.ObjectStorageImageDetails.source` attribute
        of this class is ``OBJECT_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source:
            The value to assign to the source property of this ObjectStorageImageDetails.
            Allowed values for this property are: "INLINE", "OBJECT_STORAGE"
        :type source: str

        :param namespace_name:
            The value to assign to the namespace_name property of this ObjectStorageImageDetails.
        :type namespace_name: str

        :param bucket_name:
            The value to assign to the bucket_name property of this ObjectStorageImageDetails.
        :type bucket_name: str

        :param object_name:
            The value to assign to the object_name property of this ObjectStorageImageDetails.
        :type object_name: str

        """
        self.swagger_types = {
            'source': 'str',
            'namespace_name': 'str',
            'bucket_name': 'str',
            'object_name': 'str'
        }

        self.attribute_map = {
            'source': 'source',
            'namespace_name': 'namespaceName',
            'bucket_name': 'bucketName',
            'object_name': 'objectName'
        }

        self._source = None
        self._namespace_name = None
        self._bucket_name = None
        self._object_name = None
        self._source = 'OBJECT_STORAGE'

    @property
    def namespace_name(self):
        """
        **[Required]** Gets the namespace_name of this ObjectStorageImageDetails.
        The Object Storage namespace.


        :return: The namespace_name of this ObjectStorageImageDetails.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this ObjectStorageImageDetails.
        The Object Storage namespace.


        :param namespace_name: The namespace_name of this ObjectStorageImageDetails.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this ObjectStorageImageDetails.
        The Object Storage bucket name.


        :return: The bucket_name of this ObjectStorageImageDetails.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ObjectStorageImageDetails.
        The Object Storage bucket name.


        :param bucket_name: The bucket_name of this ObjectStorageImageDetails.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this ObjectStorageImageDetails.
        The Object Storage object name.


        :return: The object_name of this ObjectStorageImageDetails.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this ObjectStorageImageDetails.
        The Object Storage object name.


        :param object_name: The object_name of this ObjectStorageImageDetails.
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
