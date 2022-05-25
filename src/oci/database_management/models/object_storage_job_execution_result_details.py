# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .job_execution_result_details import JobExecutionResultDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectStorageJobExecutionResultDetails(JobExecutionResultDetails):
    """
    The details of the job execution result stored in Object Storage. The
    job execution result could be accessed using the Object Storage API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectStorageJobExecutionResultDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.ObjectStorageJobExecutionResultDetails.type` attribute
        of this class is ``OBJECT_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ObjectStorageJobExecutionResultDetails.
            Allowed values for this property are: "OBJECT_STORAGE"
        :type type: str

        :param namespace_name:
            The value to assign to the namespace_name property of this ObjectStorageJobExecutionResultDetails.
        :type namespace_name: str

        :param bucket_name:
            The value to assign to the bucket_name property of this ObjectStorageJobExecutionResultDetails.
        :type bucket_name: str

        :param object_name:
            The value to assign to the object_name property of this ObjectStorageJobExecutionResultDetails.
        :type object_name: str

        :param row_count:
            The value to assign to the row_count property of this ObjectStorageJobExecutionResultDetails.
        :type row_count: int

        """
        self.swagger_types = {
            'type': 'str',
            'namespace_name': 'str',
            'bucket_name': 'str',
            'object_name': 'str',
            'row_count': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'namespace_name': 'namespaceName',
            'bucket_name': 'bucketName',
            'object_name': 'objectName',
            'row_count': 'rowCount'
        }

        self._type = None
        self._namespace_name = None
        self._bucket_name = None
        self._object_name = None
        self._row_count = None
        self._type = 'OBJECT_STORAGE'

    @property
    def namespace_name(self):
        """
        Gets the namespace_name of this ObjectStorageJobExecutionResultDetails.
        The Object Storage namespace used for job execution result storage.


        :return: The namespace_name of this ObjectStorageJobExecutionResultDetails.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this ObjectStorageJobExecutionResultDetails.
        The Object Storage namespace used for job execution result storage.


        :param namespace_name: The namespace_name of this ObjectStorageJobExecutionResultDetails.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this ObjectStorageJobExecutionResultDetails.
        The name of the bucket used for job execution result storage.


        :return: The bucket_name of this ObjectStorageJobExecutionResultDetails.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ObjectStorageJobExecutionResultDetails.
        The name of the bucket used for job execution result storage.


        :param bucket_name: The bucket_name of this ObjectStorageJobExecutionResultDetails.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def object_name(self):
        """
        Gets the object_name of this ObjectStorageJobExecutionResultDetails.
        The name of the object containing the job execution result.


        :return: The object_name of this ObjectStorageJobExecutionResultDetails.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this ObjectStorageJobExecutionResultDetails.
        The name of the object containing the job execution result.


        :param object_name: The object_name of this ObjectStorageJobExecutionResultDetails.
        :type: str
        """
        self._object_name = object_name

    @property
    def row_count(self):
        """
        Gets the row_count of this ObjectStorageJobExecutionResultDetails.
        The number of rows returned in the result for the Query SqlType.


        :return: The row_count of this ObjectStorageJobExecutionResultDetails.
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """
        Sets the row_count of this ObjectStorageJobExecutionResultDetails.
        The number of rows returned in the result for the Query SqlType.


        :param row_count: The row_count of this ObjectStorageJobExecutionResultDetails.
        :type: int
        """
        self._row_count = row_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
