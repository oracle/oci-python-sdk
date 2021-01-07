# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .image_source_details import ImageSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageSourceViaObjectStorageTupleDetails(ImageSourceDetails):
    """
    ImageSourceViaObjectStorageTupleDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImageSourceViaObjectStorageTupleDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.ImageSourceViaObjectStorageTupleDetails.source_type` attribute
        of this class is ``objectStorageTuple`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operating_system:
            The value to assign to the operating_system property of this ImageSourceViaObjectStorageTupleDetails.
        :type operating_system: str

        :param operating_system_version:
            The value to assign to the operating_system_version property of this ImageSourceViaObjectStorageTupleDetails.
        :type operating_system_version: str

        :param source_image_type:
            The value to assign to the source_image_type property of this ImageSourceViaObjectStorageTupleDetails.
            Allowed values for this property are: "QCOW2", "VMDK"
        :type source_image_type: str

        :param source_type:
            The value to assign to the source_type property of this ImageSourceViaObjectStorageTupleDetails.
        :type source_type: str

        :param bucket_name:
            The value to assign to the bucket_name property of this ImageSourceViaObjectStorageTupleDetails.
        :type bucket_name: str

        :param namespace_name:
            The value to assign to the namespace_name property of this ImageSourceViaObjectStorageTupleDetails.
        :type namespace_name: str

        :param object_name:
            The value to assign to the object_name property of this ImageSourceViaObjectStorageTupleDetails.
        :type object_name: str

        """
        self.swagger_types = {
            'operating_system': 'str',
            'operating_system_version': 'str',
            'source_image_type': 'str',
            'source_type': 'str',
            'bucket_name': 'str',
            'namespace_name': 'str',
            'object_name': 'str'
        }

        self.attribute_map = {
            'operating_system': 'operatingSystem',
            'operating_system_version': 'operatingSystemVersion',
            'source_image_type': 'sourceImageType',
            'source_type': 'sourceType',
            'bucket_name': 'bucketName',
            'namespace_name': 'namespaceName',
            'object_name': 'objectName'
        }

        self._operating_system = None
        self._operating_system_version = None
        self._source_image_type = None
        self._source_type = None
        self._bucket_name = None
        self._namespace_name = None
        self._object_name = None
        self._source_type = 'objectStorageTuple'

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage bucket for the image.


        :return: The bucket_name of this ImageSourceViaObjectStorageTupleDetails.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage bucket for the image.


        :param bucket_name: The bucket_name of this ImageSourceViaObjectStorageTupleDetails.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def namespace_name(self):
        """
        **[Required]** Gets the namespace_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage namespace for the image.


        :return: The namespace_name of this ImageSourceViaObjectStorageTupleDetails.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage namespace for the image.


        :param namespace_name: The namespace_name of this ImageSourceViaObjectStorageTupleDetails.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage name for the image.


        :return: The object_name of this ImageSourceViaObjectStorageTupleDetails.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage name for the image.


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
