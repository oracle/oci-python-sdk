# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .data_source_details import DataSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataSourceDetailsObjectStorage(DataSourceDetails):
    """
    Data Source details for object storage
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataSourceDetailsObjectStorage object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_anomaly_detection.models.DataSourceDetailsObjectStorage.data_source_type` attribute
        of this class is ``ORACLE_OBJECT_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_source_type:
            The value to assign to the data_source_type property of this DataSourceDetailsObjectStorage.
            Allowed values for this property are: "ORACLE_OBJECT_STORAGE", "ORACLE_ATP", "INFLUX"
        :type data_source_type: str

        :param namespace:
            The value to assign to the namespace property of this DataSourceDetailsObjectStorage.
        :type namespace: str

        :param bucket_name:
            The value to assign to the bucket_name property of this DataSourceDetailsObjectStorage.
        :type bucket_name: str

        :param object_name:
            The value to assign to the object_name property of this DataSourceDetailsObjectStorage.
        :type object_name: str

        """
        self.swagger_types = {
            'data_source_type': 'str',
            'namespace': 'str',
            'bucket_name': 'str',
            'object_name': 'str'
        }

        self.attribute_map = {
            'data_source_type': 'dataSourceType',
            'namespace': 'namespace',
            'bucket_name': 'bucketName',
            'object_name': 'objectName'
        }

        self._data_source_type = None
        self._namespace = None
        self._bucket_name = None
        self._object_name = None
        self._data_source_type = 'ORACLE_OBJECT_STORAGE'

    @property
    def namespace(self):
        """
        Gets the namespace of this DataSourceDetailsObjectStorage.
        Object storage namespace


        :return: The namespace of this DataSourceDetailsObjectStorage.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this DataSourceDetailsObjectStorage.
        Object storage namespace


        :param namespace: The namespace of this DataSourceDetailsObjectStorage.
        :type: str
        """
        self._namespace = namespace

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this DataSourceDetailsObjectStorage.
        Object storage bucket name


        :return: The bucket_name of this DataSourceDetailsObjectStorage.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this DataSourceDetailsObjectStorage.
        Object storage bucket name


        :param bucket_name: The bucket_name of this DataSourceDetailsObjectStorage.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def object_name(self):
        """
        Gets the object_name of this DataSourceDetailsObjectStorage.
        File name


        :return: The object_name of this DataSourceDetailsObjectStorage.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this DataSourceDetailsObjectStorage.
        File name


        :param object_name: The object_name of this DataSourceDetailsObjectStorage.
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
