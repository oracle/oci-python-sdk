# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_write_attribute import AbstractWriteAttribute
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OracleWriteAttribute(AbstractWriteAttribute):
    """
    The Oracle write attribute.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OracleWriteAttribute object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.OracleWriteAttribute.model_type` attribute
        of this class is ``ORACLEWRITEATTRIBUTE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this OracleWriteAttribute.
            Allowed values for this property are: "ORACLEWRITEATTRIBUTE", "ORACLEATPWRITEATTRIBUTE", "ORACLEADWCWRITEATTRIBUTE", "OBJECTSTORAGEWRITEATTRIBUTE", "ORACLE_WRITE_ATTRIBUTE", "ORACLE_ATP_WRITE_ATTRIBUTE", "ORACLE_ADWC_WRITE_ATTRIBUTE", "OBJECT_STORAGE_WRITE_ATTRIBUTE"
        :type model_type: str

        :param batch_size:
            The value to assign to the batch_size property of this OracleWriteAttribute.
        :type batch_size: int

        :param is_truncate:
            The value to assign to the is_truncate property of this OracleWriteAttribute.
        :type is_truncate: bool

        :param isolation_level:
            The value to assign to the isolation_level property of this OracleWriteAttribute.
        :type isolation_level: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'batch_size': 'int',
            'is_truncate': 'bool',
            'isolation_level': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'batch_size': 'batchSize',
            'is_truncate': 'isTruncate',
            'isolation_level': 'isolationLevel'
        }

        self._model_type = None
        self._batch_size = None
        self._is_truncate = None
        self._isolation_level = None
        self._model_type = 'ORACLEWRITEATTRIBUTE'

    @property
    def batch_size(self):
        """
        Gets the batch_size of this OracleWriteAttribute.
        The batch size for writing.


        :return: The batch_size of this OracleWriteAttribute.
        :rtype: int
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        """
        Sets the batch_size of this OracleWriteAttribute.
        The batch size for writing.


        :param batch_size: The batch_size of this OracleWriteAttribute.
        :type: int
        """
        self._batch_size = batch_size

    @property
    def is_truncate(self):
        """
        Gets the is_truncate of this OracleWriteAttribute.
        Specifies whether to truncate.


        :return: The is_truncate of this OracleWriteAttribute.
        :rtype: bool
        """
        return self._is_truncate

    @is_truncate.setter
    def is_truncate(self, is_truncate):
        """
        Sets the is_truncate of this OracleWriteAttribute.
        Specifies whether to truncate.


        :param is_truncate: The is_truncate of this OracleWriteAttribute.
        :type: bool
        """
        self._is_truncate = is_truncate

    @property
    def isolation_level(self):
        """
        Gets the isolation_level of this OracleWriteAttribute.
        Specifies the isolation level.


        :return: The isolation_level of this OracleWriteAttribute.
        :rtype: str
        """
        return self._isolation_level

    @isolation_level.setter
    def isolation_level(self, isolation_level):
        """
        Sets the isolation_level of this OracleWriteAttribute.
        Specifies the isolation level.


        :param isolation_level: The isolation_level of this OracleWriteAttribute.
        :type: str
        """
        self._isolation_level = isolation_level

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
