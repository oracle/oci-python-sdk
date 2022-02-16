# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_write_attribute import AbstractWriteAttribute
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectStorageWriteAttributes(AbstractWriteAttribute):
    """
    Properties to configure writing to Object Storage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectStorageWriteAttributes object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.ObjectStorageWriteAttributes.model_type` attribute
        of this class is ``OBJECT_STORAGE_WRITE_ATTRIBUTE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this ObjectStorageWriteAttributes.
            Allowed values for this property are: "ORACLE_WRITE_ATTRIBUTE", "ORACLE_ATP_WRITE_ATTRIBUTE", "ORACLE_ADWC_WRITE_ATTRIBUTE", "OBJECT_STORAGE_WRITE_ATTRIBUTE", "HDFS_WRITE_ATTRIBUTE"
        :type model_type: str

        :param write_to_single_file:
            The value to assign to the write_to_single_file property of this ObjectStorageWriteAttributes.
        :type write_to_single_file: bool

        """
        self.swagger_types = {
            'model_type': 'str',
            'write_to_single_file': 'bool'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'write_to_single_file': 'writeToSingleFile'
        }

        self._model_type = None
        self._write_to_single_file = None
        self._model_type = 'OBJECT_STORAGE_WRITE_ATTRIBUTE'

    @property
    def write_to_single_file(self):
        """
        Gets the write_to_single_file of this ObjectStorageWriteAttributes.
        Specifies whether to write output to single-file or not.


        :return: The write_to_single_file of this ObjectStorageWriteAttributes.
        :rtype: bool
        """
        return self._write_to_single_file

    @write_to_single_file.setter
    def write_to_single_file(self, write_to_single_file):
        """
        Sets the write_to_single_file of this ObjectStorageWriteAttributes.
        Specifies whether to write output to single-file or not.


        :param write_to_single_file: The write_to_single_file of this ObjectStorageWriteAttributes.
        :type: bool
        """
        self._write_to_single_file = write_to_single_file

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
