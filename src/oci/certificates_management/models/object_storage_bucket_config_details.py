# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectStorageBucketConfigDetails(object):
    """
    The details of the Object Storage bucket configured to store the certificate revocation list (CRL).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectStorageBucketConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param object_storage_namespace:
            The value to assign to the object_storage_namespace property of this ObjectStorageBucketConfigDetails.
        :type object_storage_namespace: str

        :param object_storage_bucket_name:
            The value to assign to the object_storage_bucket_name property of this ObjectStorageBucketConfigDetails.
        :type object_storage_bucket_name: str

        :param object_storage_object_name_format:
            The value to assign to the object_storage_object_name_format property of this ObjectStorageBucketConfigDetails.
        :type object_storage_object_name_format: str

        """
        self.swagger_types = {
            'object_storage_namespace': 'str',
            'object_storage_bucket_name': 'str',
            'object_storage_object_name_format': 'str'
        }

        self.attribute_map = {
            'object_storage_namespace': 'objectStorageNamespace',
            'object_storage_bucket_name': 'objectStorageBucketName',
            'object_storage_object_name_format': 'objectStorageObjectNameFormat'
        }

        self._object_storage_namespace = None
        self._object_storage_bucket_name = None
        self._object_storage_object_name_format = None

    @property
    def object_storage_namespace(self):
        """
        Gets the object_storage_namespace of this ObjectStorageBucketConfigDetails.
        The tenancy of the bucket where the CRL is stored.


        :return: The object_storage_namespace of this ObjectStorageBucketConfigDetails.
        :rtype: str
        """
        return self._object_storage_namespace

    @object_storage_namespace.setter
    def object_storage_namespace(self, object_storage_namespace):
        """
        Sets the object_storage_namespace of this ObjectStorageBucketConfigDetails.
        The tenancy of the bucket where the CRL is stored.


        :param object_storage_namespace: The object_storage_namespace of this ObjectStorageBucketConfigDetails.
        :type: str
        """
        self._object_storage_namespace = object_storage_namespace

    @property
    def object_storage_bucket_name(self):
        """
        **[Required]** Gets the object_storage_bucket_name of this ObjectStorageBucketConfigDetails.
        The name of the bucket where the CRL is stored.


        :return: The object_storage_bucket_name of this ObjectStorageBucketConfigDetails.
        :rtype: str
        """
        return self._object_storage_bucket_name

    @object_storage_bucket_name.setter
    def object_storage_bucket_name(self, object_storage_bucket_name):
        """
        Sets the object_storage_bucket_name of this ObjectStorageBucketConfigDetails.
        The name of the bucket where the CRL is stored.


        :param object_storage_bucket_name: The object_storage_bucket_name of this ObjectStorageBucketConfigDetails.
        :type: str
        """
        self._object_storage_bucket_name = object_storage_bucket_name

    @property
    def object_storage_object_name_format(self):
        """
        **[Required]** Gets the object_storage_object_name_format of this ObjectStorageBucketConfigDetails.
        The object name in the bucket where the CRL is stored, expressed using a format where the version number of the issuing CA is inserted as part of the Object Storage object name wherever you include a pair of curly braces. This versioning scheme helps avoid collisions when new CA versions are created. For example, myCrlFileIssuedFromCAVersion{}.crl becomes myCrlFileIssuedFromCAVersion2.crl for CA version 2.


        :return: The object_storage_object_name_format of this ObjectStorageBucketConfigDetails.
        :rtype: str
        """
        return self._object_storage_object_name_format

    @object_storage_object_name_format.setter
    def object_storage_object_name_format(self, object_storage_object_name_format):
        """
        Sets the object_storage_object_name_format of this ObjectStorageBucketConfigDetails.
        The object name in the bucket where the CRL is stored, expressed using a format where the version number of the issuing CA is inserted as part of the Object Storage object name wherever you include a pair of curly braces. This versioning scheme helps avoid collisions when new CA versions are created. For example, myCrlFileIssuedFromCAVersion{}.crl becomes myCrlFileIssuedFromCAVersion2.crl for CA version 2.


        :param object_storage_object_name_format: The object_storage_object_name_format of this ObjectStorageBucketConfigDetails.
        :type: str
        """
        self._object_storage_object_name_format = object_storage_object_name_format

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
