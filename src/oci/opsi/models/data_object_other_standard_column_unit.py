# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .data_object_column_unit import DataObjectColumnUnit
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataObjectOtherStandardColumnUnit(DataObjectColumnUnit):
    """
    Unit details of a data object column of OTHER_STANDARD unit category.
    """

    #: A constant which can be used with the unit property of a DataObjectOtherStandardColumnUnit.
    #: This constant has a value of "PERCENTAGE"
    UNIT_PERCENTAGE = "PERCENTAGE"

    #: A constant which can be used with the unit property of a DataObjectOtherStandardColumnUnit.
    #: This constant has a value of "COUNT"
    UNIT_COUNT = "COUNT"

    #: A constant which can be used with the unit property of a DataObjectOtherStandardColumnUnit.
    #: This constant has a value of "IO"
    UNIT_IO = "IO"

    #: A constant which can be used with the unit property of a DataObjectOtherStandardColumnUnit.
    #: This constant has a value of "BOOLEAN"
    UNIT_BOOLEAN = "BOOLEAN"

    #: A constant which can be used with the unit property of a DataObjectOtherStandardColumnUnit.
    #: This constant has a value of "OPERATION"
    UNIT_OPERATION = "OPERATION"

    #: A constant which can be used with the unit property of a DataObjectOtherStandardColumnUnit.
    #: This constant has a value of "TRANSACTION"
    UNIT_TRANSACTION = "TRANSACTION"

    #: A constant which can be used with the unit property of a DataObjectOtherStandardColumnUnit.
    #: This constant has a value of "CONNECTION"
    UNIT_CONNECTION = "CONNECTION"

    #: A constant which can be used with the unit property of a DataObjectOtherStandardColumnUnit.
    #: This constant has a value of "ACCESS"
    UNIT_ACCESS = "ACCESS"

    #: A constant which can be used with the unit property of a DataObjectOtherStandardColumnUnit.
    #: This constant has a value of "REQUEST"
    UNIT_REQUEST = "REQUEST"

    #: A constant which can be used with the unit property of a DataObjectOtherStandardColumnUnit.
    #: This constant has a value of "MESSAGE"
    UNIT_MESSAGE = "MESSAGE"

    #: A constant which can be used with the unit property of a DataObjectOtherStandardColumnUnit.
    #: This constant has a value of "EXECUTION"
    UNIT_EXECUTION = "EXECUTION"

    #: A constant which can be used with the unit property of a DataObjectOtherStandardColumnUnit.
    #: This constant has a value of "LOGONS"
    UNIT_LOGONS = "LOGONS"

    #: A constant which can be used with the unit property of a DataObjectOtherStandardColumnUnit.
    #: This constant has a value of "THREAD"
    UNIT_THREAD = "THREAD"

    #: A constant which can be used with the unit property of a DataObjectOtherStandardColumnUnit.
    #: This constant has a value of "ERROR"
    UNIT_ERROR = "ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new DataObjectOtherStandardColumnUnit object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.DataObjectOtherStandardColumnUnit.unit_category` attribute
        of this class is ``OTHER_STANDARD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param unit_category:
            The value to assign to the unit_category property of this DataObjectOtherStandardColumnUnit.
            Allowed values for this property are: "DATA_SIZE", "TIME", "POWER", "TEMPERATURE", "CORE", "RATE", "FREQUENCY", "OTHER_STANDARD", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type unit_category: str

        :param display_name:
            The value to assign to the display_name property of this DataObjectOtherStandardColumnUnit.
        :type display_name: str

        :param unit:
            The value to assign to the unit property of this DataObjectOtherStandardColumnUnit.
            Allowed values for this property are: "PERCENTAGE", "COUNT", "IO", "BOOLEAN", "OPERATION", "TRANSACTION", "CONNECTION", "ACCESS", "REQUEST", "MESSAGE", "EXECUTION", "LOGONS", "THREAD", "ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type unit: str

        """
        self.swagger_types = {
            'unit_category': 'str',
            'display_name': 'str',
            'unit': 'str'
        }

        self.attribute_map = {
            'unit_category': 'unitCategory',
            'display_name': 'displayName',
            'unit': 'unit'
        }

        self._unit_category = None
        self._display_name = None
        self._unit = None
        self._unit_category = 'OTHER_STANDARD'

    @property
    def unit(self):
        """
        Gets the unit of this DataObjectOtherStandardColumnUnit.
        Other standard column unit.

        Allowed values for this property are: "PERCENTAGE", "COUNT", "IO", "BOOLEAN", "OPERATION", "TRANSACTION", "CONNECTION", "ACCESS", "REQUEST", "MESSAGE", "EXECUTION", "LOGONS", "THREAD", "ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The unit of this DataObjectOtherStandardColumnUnit.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this DataObjectOtherStandardColumnUnit.
        Other standard column unit.


        :param unit: The unit of this DataObjectOtherStandardColumnUnit.
        :type: str
        """
        allowed_values = ["PERCENTAGE", "COUNT", "IO", "BOOLEAN", "OPERATION", "TRANSACTION", "CONNECTION", "ACCESS", "REQUEST", "MESSAGE", "EXECUTION", "LOGONS", "THREAD", "ERROR"]
        if not value_allowed_none_or_none_sentinel(unit, allowed_values):
            unit = 'UNKNOWN_ENUM_VALUE'
        self._unit = unit

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
