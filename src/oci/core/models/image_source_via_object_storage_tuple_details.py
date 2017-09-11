# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .image_source_details import ImageSourceDetails
from ...util import formatted_flat_dict


class ImageSourceViaObjectStorageTupleDetails(ImageSourceDetails):

    def __init__(self):

        self.swagger_types = {
            'source_type': 'str',
            'bucket_name': 'str',
            'namespace_name': 'str',
            'object_name': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'bucket_name': 'bucketName',
            'namespace_name': 'namespaceName',
            'object_name': 'objectName'
        }

        self._source_type = None
        self._bucket_name = None
        self._namespace_name = None
        self._object_name = None
        self._source_type = 'objectStorageTuple'

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage Service bucket for the image.


        :return: The bucket_name of this ImageSourceViaObjectStorageTupleDetails.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage Service bucket for the image.


        :param bucket_name: The bucket_name of this ImageSourceViaObjectStorageTupleDetails.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def namespace_name(self):
        """
        Gets the namespace_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage Service namespace for the image.


        :return: The namespace_name of this ImageSourceViaObjectStorageTupleDetails.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage Service namespace for the image.


        :param namespace_name: The namespace_name of this ImageSourceViaObjectStorageTupleDetails.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def object_name(self):
        """
        Gets the object_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage Service name for the image.


        :return: The object_name of this ImageSourceViaObjectStorageTupleDetails.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage Service name for the image.


        :param object_name: The object_name of this ImageSourceViaObjectStorageTupleDetails.
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
