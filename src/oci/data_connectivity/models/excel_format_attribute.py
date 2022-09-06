# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_format_attribute import AbstractFormatAttribute
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExcelFormatAttribute(AbstractFormatAttribute):
    """
    The Excel format attribute.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExcelFormatAttribute object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.ExcelFormatAttribute.model_type` attribute
        of this class is ``EXCEL_FORMAT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this ExcelFormatAttribute.
            Allowed values for this property are: "JSON_FORMAT", "CSV_FORMAT", "AVRO_FORMAT", "PARQUET_FORMAT"
        :type model_type: str

        :param data_address:
            The value to assign to the data_address property of this ExcelFormatAttribute.
        :type data_address: str

        :param header:
            The value to assign to the header property of this ExcelFormatAttribute.
        :type header: bool

        :param password:
            The value to assign to the password property of this ExcelFormatAttribute.
        :type password: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'data_address': 'str',
            'header': 'bool',
            'password': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'data_address': 'dataAddress',
            'header': 'header',
            'password': 'password'
        }

        self._model_type = None
        self._data_address = None
        self._header = None
        self._password = None
        self._model_type = 'EXCEL_FORMAT'

    @property
    def data_address(self):
        """
        Gets the data_address of this ExcelFormatAttribute.
        Range of the data. For example, \"'My Sheet'!B3:C35\"


        :return: The data_address of this ExcelFormatAttribute.
        :rtype: str
        """
        return self._data_address

    @data_address.setter
    def data_address(self, data_address):
        """
        Sets the data_address of this ExcelFormatAttribute.
        Range of the data. For example, \"'My Sheet'!B3:C35\"


        :param data_address: The data_address of this ExcelFormatAttribute.
        :type: str
        """
        self._data_address = data_address

    @property
    def header(self):
        """
        Gets the header of this ExcelFormatAttribute.
        Whether the dataAddress contains the header with column names. If false - column names fill be generated.


        :return: The header of this ExcelFormatAttribute.
        :rtype: bool
        """
        return self._header

    @header.setter
    def header(self, header):
        """
        Sets the header of this ExcelFormatAttribute.
        Whether the dataAddress contains the header with column names. If false - column names fill be generated.


        :param header: The header of this ExcelFormatAttribute.
        :type: bool
        """
        self._header = header

    @property
    def password(self):
        """
        Gets the password of this ExcelFormatAttribute.
        Workbook password if it is password protected.


        :return: The password of this ExcelFormatAttribute.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this ExcelFormatAttribute.
        Workbook password if it is password protected.


        :param password: The password of this ExcelFormatAttribute.
        :type: str
        """
        self._password = password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
