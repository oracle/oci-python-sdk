# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_data_operation_config import AbstractDataOperationConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReadOperationConfig(AbstractDataOperationConfig):
    """
    The information about the read operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ReadOperationConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.ReadOperationConfig.model_type` attribute
        of this class is ``READ_OPERATION_CONFIG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this ReadOperationConfig.
            Allowed values for this property are: "READ_OPERATION_CONFIG", "WRITE_OPERATION_CONFIG"
        :type model_type: str

        :param key:
            The value to assign to the key property of this ReadOperationConfig.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this ReadOperationConfig.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this ReadOperationConfig.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param operations:
            The value to assign to the operations property of this ReadOperationConfig.
        :type operations: list[oci.data_connectivity.models.PushDownOperation]

        :param data_format:
            The value to assign to the data_format property of this ReadOperationConfig.
        :type data_format: oci.data_connectivity.models.DataFormat

        :param partition_config:
            The value to assign to the partition_config property of this ReadOperationConfig.
        :type partition_config: oci.data_connectivity.models.PartitionConfig

        :param read_attribute:
            The value to assign to the read_attribute property of this ReadOperationConfig.
        :type read_attribute: oci.data_connectivity.models.AbstractReadAttribute

        :param object_status:
            The value to assign to the object_status property of this ReadOperationConfig.
        :type object_status: int

        :param read_raw_data:
            The value to assign to the read_raw_data property of this ReadOperationConfig.
        :type read_raw_data: bool

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'operations': 'list[PushDownOperation]',
            'data_format': 'DataFormat',
            'partition_config': 'PartitionConfig',
            'read_attribute': 'AbstractReadAttribute',
            'object_status': 'int',
            'read_raw_data': 'bool'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'operations': 'operations',
            'data_format': 'dataFormat',
            'partition_config': 'partitionConfig',
            'read_attribute': 'readAttribute',
            'object_status': 'objectStatus',
            'read_raw_data': 'readRawData'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._operations = None
        self._data_format = None
        self._partition_config = None
        self._read_attribute = None
        self._object_status = None
        self._read_raw_data = None
        self._model_type = 'READ_OPERATION_CONFIG'

    @property
    def key(self):
        """
        Gets the key of this ReadOperationConfig.
        The object key.


        :return: The key of this ReadOperationConfig.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ReadOperationConfig.
        The object key.


        :param key: The key of this ReadOperationConfig.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this ReadOperationConfig.
        The object's model version.


        :return: The model_version of this ReadOperationConfig.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this ReadOperationConfig.
        The object's model version.


        :param model_version: The model_version of this ReadOperationConfig.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this ReadOperationConfig.

        :return: The parent_ref of this ReadOperationConfig.
        :rtype: oci.data_connectivity.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this ReadOperationConfig.

        :param parent_ref: The parent_ref of this ReadOperationConfig.
        :type: oci.data_connectivity.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def operations(self):
        """
        Gets the operations of this ReadOperationConfig.
        An array of operations.


        :return: The operations of this ReadOperationConfig.
        :rtype: list[oci.data_connectivity.models.PushDownOperation]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """
        Sets the operations of this ReadOperationConfig.
        An array of operations.


        :param operations: The operations of this ReadOperationConfig.
        :type: list[oci.data_connectivity.models.PushDownOperation]
        """
        self._operations = operations

    @property
    def data_format(self):
        """
        Gets the data_format of this ReadOperationConfig.

        :return: The data_format of this ReadOperationConfig.
        :rtype: oci.data_connectivity.models.DataFormat
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """
        Sets the data_format of this ReadOperationConfig.

        :param data_format: The data_format of this ReadOperationConfig.
        :type: oci.data_connectivity.models.DataFormat
        """
        self._data_format = data_format

    @property
    def partition_config(self):
        """
        Gets the partition_config of this ReadOperationConfig.

        :return: The partition_config of this ReadOperationConfig.
        :rtype: oci.data_connectivity.models.PartitionConfig
        """
        return self._partition_config

    @partition_config.setter
    def partition_config(self, partition_config):
        """
        Sets the partition_config of this ReadOperationConfig.

        :param partition_config: The partition_config of this ReadOperationConfig.
        :type: oci.data_connectivity.models.PartitionConfig
        """
        self._partition_config = partition_config

    @property
    def read_attribute(self):
        """
        Gets the read_attribute of this ReadOperationConfig.

        :return: The read_attribute of this ReadOperationConfig.
        :rtype: oci.data_connectivity.models.AbstractReadAttribute
        """
        return self._read_attribute

    @read_attribute.setter
    def read_attribute(self, read_attribute):
        """
        Sets the read_attribute of this ReadOperationConfig.

        :param read_attribute: The read_attribute of this ReadOperationConfig.
        :type: oci.data_connectivity.models.AbstractReadAttribute
        """
        self._read_attribute = read_attribute

    @property
    def object_status(self):
        """
        Gets the object_status of this ReadOperationConfig.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this ReadOperationConfig.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this ReadOperationConfig.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this ReadOperationConfig.
        :type: int
        """
        self._object_status = object_status

    @property
    def read_raw_data(self):
        """
        Gets the read_raw_data of this ReadOperationConfig.
        Specifies if this readOperationConfig operation should trigger raw data preview flow.


        :return: The read_raw_data of this ReadOperationConfig.
        :rtype: bool
        """
        return self._read_raw_data

    @read_raw_data.setter
    def read_raw_data(self, read_raw_data):
        """
        Sets the read_raw_data of this ReadOperationConfig.
        Specifies if this readOperationConfig operation should trigger raw data preview flow.


        :param read_raw_data: The read_raw_data of this ReadOperationConfig.
        :type: bool
        """
        self._read_raw_data = read_raw_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
