# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .result_location import ResultLocation
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectStorageLocation(ResultLocation):
    """
    The object storage location where usage/cost CSVs will be uploaded
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectStorageLocation object with values from keyword arguments. The default value of the :py:attr:`~oci.usage_api.models.ObjectStorageLocation.location_type` attribute
        of this class is ``OBJECT_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param location_type:
            The value to assign to the location_type property of this ObjectStorageLocation.
            Allowed values for this property are: "OBJECT_STORAGE"
        :type location_type: str

        :param region:
            The value to assign to the region property of this ObjectStorageLocation.
        :type region: str

        :param namespace:
            The value to assign to the namespace property of this ObjectStorageLocation.
        :type namespace: str

        :param bucket_name:
            The value to assign to the bucket_name property of this ObjectStorageLocation.
        :type bucket_name: str

        """
        self.swagger_types = {
            'location_type': 'str',
            'region': 'str',
            'namespace': 'str',
            'bucket_name': 'str'
        }

        self.attribute_map = {
            'location_type': 'locationType',
            'region': 'region',
            'namespace': 'namespace',
            'bucket_name': 'bucketName'
        }

        self._location_type = None
        self._region = None
        self._namespace = None
        self._bucket_name = None
        self._location_type = 'OBJECT_STORAGE'

    @property
    def region(self):
        """
        **[Required]** Gets the region of this ObjectStorageLocation.
        The destination Object Store Region specified by customer


        :return: The region of this ObjectStorageLocation.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this ObjectStorageLocation.
        The destination Object Store Region specified by customer


        :param region: The region of this ObjectStorageLocation.
        :type: str
        """
        self._region = region

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this ObjectStorageLocation.
        The namespace needed to determine object storage bucket.


        :return: The namespace of this ObjectStorageLocation.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this ObjectStorageLocation.
        The namespace needed to determine object storage bucket.


        :param namespace: The namespace of this ObjectStorageLocation.
        :type: str
        """
        self._namespace = namespace

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this ObjectStorageLocation.
        The bucket name where usage/cost CSVs will be uploaded


        :return: The bucket_name of this ObjectStorageLocation.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ObjectStorageLocation.
        The bucket name where usage/cost CSVs will be uploaded


        :param bucket_name: The bucket_name of this ObjectStorageLocation.
        :type: str
        """
        self._bucket_name = bucket_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
