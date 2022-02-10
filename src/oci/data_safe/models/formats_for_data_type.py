# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FormatsForDataType(object):
    """
    A list of basic masking formats compatible with a supported data type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FormatsForDataType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_type:
            The value to assign to the data_type property of this FormatsForDataType.
        :type data_type: str

        :param masking_formats:
            The value to assign to the masking_formats property of this FormatsForDataType.
        :type masking_formats: list[oci.data_safe.models.FormatSummary]

        """
        self.swagger_types = {
            'data_type': 'str',
            'masking_formats': 'list[FormatSummary]'
        }

        self.attribute_map = {
            'data_type': 'dataType',
            'masking_formats': 'maskingFormats'
        }

        self._data_type = None
        self._masking_formats = None

    @property
    def data_type(self):
        """
        **[Required]** Gets the data_type of this FormatsForDataType.
        The data type category, which can be one of the following -
          Character - Includes CHAR, NCHAR, VARCHAR2, and NVARCHAR2
          Numeric - Includes NUMBER, FLOAT, RAW, BINARY_FLOAT, and BINARY_DOUBLE
          Date - Includes DATE and TIMESTAMP
          LOB - Includes BLOB, CLOB, and NCLOB
          All - Includes all the supported data types


        :return: The data_type of this FormatsForDataType.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this FormatsForDataType.
        The data type category, which can be one of the following -
          Character - Includes CHAR, NCHAR, VARCHAR2, and NVARCHAR2
          Numeric - Includes NUMBER, FLOAT, RAW, BINARY_FLOAT, and BINARY_DOUBLE
          Date - Includes DATE and TIMESTAMP
          LOB - Includes BLOB, CLOB, and NCLOB
          All - Includes all the supported data types


        :param data_type: The data_type of this FormatsForDataType.
        :type: str
        """
        self._data_type = data_type

    @property
    def masking_formats(self):
        """
        Gets the masking_formats of this FormatsForDataType.
        An array of the basic masking formats compatible with the data type category.


        :return: The masking_formats of this FormatsForDataType.
        :rtype: list[oci.data_safe.models.FormatSummary]
        """
        return self._masking_formats

    @masking_formats.setter
    def masking_formats(self, masking_formats):
        """
        Sets the masking_formats of this FormatsForDataType.
        An array of the basic masking formats compatible with the data type category.


        :param masking_formats: The masking_formats of this FormatsForDataType.
        :type: list[oci.data_safe.models.FormatSummary]
        """
        self._masking_formats = masking_formats

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
