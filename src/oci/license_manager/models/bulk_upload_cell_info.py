# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkUploadCellInfo(object):
    """
    Error information corresponding to each column that was required but was invalid.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BulkUploadCellInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param column_index:
            The value to assign to the column_index property of this BulkUploadCellInfo.
        :type column_index: str

        :param error_info:
            The value to assign to the error_info property of this BulkUploadCellInfo.
        :type error_info: str

        """
        self.swagger_types = {
            'column_index': 'str',
            'error_info': 'str'
        }

        self.attribute_map = {
            'column_index': 'columnIndex',
            'error_info': 'errorInfo'
        }

        self._column_index = None
        self._error_info = None

    @property
    def column_index(self):
        """
        **[Required]** Gets the column_index of this BulkUploadCellInfo.
        Column index as in the given bulk upload file.


        :return: The column_index of this BulkUploadCellInfo.
        :rtype: str
        """
        return self._column_index

    @column_index.setter
    def column_index(self, column_index):
        """
        Sets the column_index of this BulkUploadCellInfo.
        Column index as in the given bulk upload file.


        :param column_index: The column_index of this BulkUploadCellInfo.
        :type: str
        """
        self._column_index = column_index

    @property
    def error_info(self):
        """
        **[Required]** Gets the error_info of this BulkUploadCellInfo.
        Error information corresponding to a particular column.


        :return: The error_info of this BulkUploadCellInfo.
        :rtype: str
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """
        Sets the error_info of this BulkUploadCellInfo.
        Error information corresponding to a particular column.


        :param error_info: The error_info of this BulkUploadCellInfo.
        :type: str
        """
        self._error_info = error_info

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
