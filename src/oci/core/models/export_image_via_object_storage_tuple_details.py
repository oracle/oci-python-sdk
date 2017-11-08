# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .export_image_details import ExportImageDetails
from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExportImageViaObjectStorageTupleDetails(ExportImageDetails):

    def __init__(self, **kwargs):
        """
        Initializes a new ExportImageViaObjectStorageTupleDetails object with values from values from keyword arguments. The
        following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bucket_name:
            The value to assign to the bucket_name property of this ExportImageViaObjectStorageTupleDetails.
        :type bucket_name: str

        :param namespace_name:
            The value to assign to the namespace_name property of this ExportImageViaObjectStorageTupleDetails.
        :type namespace_name: str

        :param object_name:
            The value to assign to the object_name property of this ExportImageViaObjectStorageTupleDetails.
        :type object_name: str

        """
        self.swagger_types = {
            'destination_type': 'str',
            'bucket_name': 'str',
            'namespace_name': 'str',
            'object_name': 'str'
        }

        self.attribute_map = {
            'destination_type': 'destinationType',
            'bucket_name': 'bucketName',
            'namespace_name': 'namespaceName',
            'object_name': 'objectName'
        }

        self._destination_type = None
        self._bucket_name = None
        self._namespace_name = None
        self._object_name = None
        self._destination_type = 'objectStorageTuple'

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this ExportImageViaObjectStorageTupleDetails.
        The Object Storage bucket to export the image to.


        :return: The bucket_name of this ExportImageViaObjectStorageTupleDetails.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ExportImageViaObjectStorageTupleDetails.
        The Object Storage bucket to export the image to.


        :param bucket_name: The bucket_name of this ExportImageViaObjectStorageTupleDetails.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def namespace_name(self):
        """
        Gets the namespace_name of this ExportImageViaObjectStorageTupleDetails.
        The Object Storage namespace to export the image to.


        :return: The namespace_name of this ExportImageViaObjectStorageTupleDetails.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this ExportImageViaObjectStorageTupleDetails.
        The Object Storage namespace to export the image to.


        :param namespace_name: The namespace_name of this ExportImageViaObjectStorageTupleDetails.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def object_name(self):
        """
        Gets the object_name of this ExportImageViaObjectStorageTupleDetails.
        The Object Storage object name for the exported image.


        :return: The object_name of this ExportImageViaObjectStorageTupleDetails.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this ExportImageViaObjectStorageTupleDetails.
        The Object Storage object name for the exported image.


        :param object_name: The object_name of this ExportImageViaObjectStorageTupleDetails.
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
