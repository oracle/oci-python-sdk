# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .partition_config import PartitionConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KeyRangePartitionConfig(PartitionConfig):
    """
    The information about key range.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KeyRangePartitionConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.KeyRangePartitionConfig.model_type` attribute
        of this class is ``KEYRANGEPARTITIONCONFIG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this KeyRangePartitionConfig.
            Allowed values for this property are: "KEYRANGEPARTITIONCONFIG"
        :type model_type: str

        :param partition_number:
            The value to assign to the partition_number property of this KeyRangePartitionConfig.
        :type partition_number: int

        :param key_range:
            The value to assign to the key_range property of this KeyRangePartitionConfig.
        :type key_range: oci.data_integration.models.KeyRange

        """
        self.swagger_types = {
            'model_type': 'str',
            'partition_number': 'int',
            'key_range': 'KeyRange'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'partition_number': 'partitionNumber',
            'key_range': 'keyRange'
        }

        self._model_type = None
        self._partition_number = None
        self._key_range = None
        self._model_type = 'KEYRANGEPARTITIONCONFIG'

    @property
    def partition_number(self):
        """
        Gets the partition_number of this KeyRangePartitionConfig.
        The partition number for the key range.


        :return: The partition_number of this KeyRangePartitionConfig.
        :rtype: int
        """
        return self._partition_number

    @partition_number.setter
    def partition_number(self, partition_number):
        """
        Sets the partition_number of this KeyRangePartitionConfig.
        The partition number for the key range.


        :param partition_number: The partition_number of this KeyRangePartitionConfig.
        :type: int
        """
        self._partition_number = partition_number

    @property
    def key_range(self):
        """
        Gets the key_range of this KeyRangePartitionConfig.

        :return: The key_range of this KeyRangePartitionConfig.
        :rtype: oci.data_integration.models.KeyRange
        """
        return self._key_range

    @key_range.setter
    def key_range(self, key_range):
        """
        Sets the key_range of this KeyRangePartitionConfig.

        :param key_range: The key_range of this KeyRangePartitionConfig.
        :type: oci.data_integration.models.KeyRange
        """
        self._key_range = key_range

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
