# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .job_execution_result_location import JobExecutionResultLocation
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectStorageJobExecutionResultLocation(JobExecutionResultLocation):
    """
    The details about Object Storage job execution result location type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectStorageJobExecutionResultLocation object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.ObjectStorageJobExecutionResultLocation.type` attribute
        of this class is ``OBJECT_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ObjectStorageJobExecutionResultLocation.
            Allowed values for this property are: "OBJECT_STORAGE"
        :type type: str

        :param namespace_name:
            The value to assign to the namespace_name property of this ObjectStorageJobExecutionResultLocation.
        :type namespace_name: str

        :param bucket_name:
            The value to assign to the bucket_name property of this ObjectStorageJobExecutionResultLocation.
        :type bucket_name: str

        """
        self.swagger_types = {
            'type': 'str',
            'namespace_name': 'str',
            'bucket_name': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'namespace_name': 'namespaceName',
            'bucket_name': 'bucketName'
        }

        self._type = None
        self._namespace_name = None
        self._bucket_name = None
        self._type = 'OBJECT_STORAGE'

    @property
    def namespace_name(self):
        """
        Gets the namespace_name of this ObjectStorageJobExecutionResultLocation.
        The Object Storage namespace used for job execution result storage.


        :return: The namespace_name of this ObjectStorageJobExecutionResultLocation.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this ObjectStorageJobExecutionResultLocation.
        The Object Storage namespace used for job execution result storage.


        :param namespace_name: The namespace_name of this ObjectStorageJobExecutionResultLocation.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this ObjectStorageJobExecutionResultLocation.
        The name of the bucket used for job execution result storage.


        :return: The bucket_name of this ObjectStorageJobExecutionResultLocation.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ObjectStorageJobExecutionResultLocation.
        The name of the bucket used for job execution result storage.


        :param bucket_name: The bucket_name of this ObjectStorageJobExecutionResultLocation.
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
