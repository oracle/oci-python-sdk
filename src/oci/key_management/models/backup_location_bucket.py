# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .backup_location import BackupLocation
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackupLocationBucket(BackupLocation):
    """
    Object storage bucket details to upload or download the backup
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BackupLocationBucket object with values from keyword arguments. The default value of the :py:attr:`~oci.key_management.models.BackupLocationBucket.destination` attribute
        of this class is ``BUCKET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param destination:
            The value to assign to the destination property of this BackupLocationBucket.
            Allowed values for this property are: "BUCKET", "PRE_AUTHENTICATED_REQUEST_URI"
        :type destination: str

        :param namespace:
            The value to assign to the namespace property of this BackupLocationBucket.
        :type namespace: str

        :param bucket_name:
            The value to assign to the bucket_name property of this BackupLocationBucket.
        :type bucket_name: str

        :param object_name:
            The value to assign to the object_name property of this BackupLocationBucket.
        :type object_name: str

        """
        self.swagger_types = {
            'destination': 'str',
            'namespace': 'str',
            'bucket_name': 'str',
            'object_name': 'str'
        }

        self.attribute_map = {
            'destination': 'destination',
            'namespace': 'namespace',
            'bucket_name': 'bucketName',
            'object_name': 'objectName'
        }

        self._destination = None
        self._namespace = None
        self._bucket_name = None
        self._object_name = None
        self._destination = 'BUCKET'

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this BackupLocationBucket.

        :return: The namespace of this BackupLocationBucket.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this BackupLocationBucket.

        :param namespace: The namespace of this BackupLocationBucket.
        :type: str
        """
        self._namespace = namespace

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this BackupLocationBucket.

        :return: The bucket_name of this BackupLocationBucket.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this BackupLocationBucket.

        :param bucket_name: The bucket_name of this BackupLocationBucket.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this BackupLocationBucket.

        :return: The object_name of this BackupLocationBucket.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this BackupLocationBucket.

        :param object_name: The object_name of this BackupLocationBucket.
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
