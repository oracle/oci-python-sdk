# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .config_source_record import ConfigSourceRecord
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectStorageConfigSourceRecord(ConfigSourceRecord):
    """
    Metadata about the Object Storage configuration source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectStorageConfigSourceRecord object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.ObjectStorageConfigSourceRecord.config_source_record_type` attribute
        of this class is ``OBJECT_STORAGE_CONFIG_SOURCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_source_record_type:
            The value to assign to the config_source_record_type property of this ObjectStorageConfigSourceRecord.
            Allowed values for this property are: "ZIP_UPLOAD", "GIT_CONFIG_SOURCE", "OBJECT_STORAGE_CONFIG_SOURCE"
        :type config_source_record_type: str

        :param region:
            The value to assign to the region property of this ObjectStorageConfigSourceRecord.
        :type region: str

        :param namespace:
            The value to assign to the namespace property of this ObjectStorageConfigSourceRecord.
        :type namespace: str

        :param bucket_name:
            The value to assign to the bucket_name property of this ObjectStorageConfigSourceRecord.
        :type bucket_name: str

        """
        self.swagger_types = {
            'config_source_record_type': 'str',
            'region': 'str',
            'namespace': 'str',
            'bucket_name': 'str'
        }

        self.attribute_map = {
            'config_source_record_type': 'configSourceRecordType',
            'region': 'region',
            'namespace': 'namespace',
            'bucket_name': 'bucketName'
        }

        self._config_source_record_type = None
        self._region = None
        self._namespace = None
        self._bucket_name = None
        self._config_source_record_type = 'OBJECT_STORAGE_CONFIG_SOURCE'

    @property
    def region(self):
        """
        **[Required]** Gets the region of this ObjectStorageConfigSourceRecord.
        The name of the bucket's region.
        Example: `us-phoenix-1`


        :return: The region of this ObjectStorageConfigSourceRecord.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this ObjectStorageConfigSourceRecord.
        The name of the bucket's region.
        Example: `us-phoenix-1`


        :param region: The region of this ObjectStorageConfigSourceRecord.
        :type: str
        """
        self._region = region

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this ObjectStorageConfigSourceRecord.
        The Object Storage namespace that contains the bucket.


        :return: The namespace of this ObjectStorageConfigSourceRecord.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this ObjectStorageConfigSourceRecord.
        The Object Storage namespace that contains the bucket.


        :param namespace: The namespace of this ObjectStorageConfigSourceRecord.
        :type: str
        """
        self._namespace = namespace

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this ObjectStorageConfigSourceRecord.
        The name of the bucket that contains the Terraform configuration files.


        :return: The bucket_name of this ObjectStorageConfigSourceRecord.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ObjectStorageConfigSourceRecord.
        The name of the bucket that contains the Terraform configuration files.


        :param bucket_name: The bucket_name of this ObjectStorageConfigSourceRecord.
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
