# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .data_object_column_unit import DataObjectColumnUnit
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataObjectCustomColumnUnit(DataObjectColumnUnit):
    """
    Unit details of a data object column of CUSTOM unit category.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataObjectCustomColumnUnit object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.DataObjectCustomColumnUnit.unit_category` attribute
        of this class is ``CUSTOM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param unit_category:
            The value to assign to the unit_category property of this DataObjectCustomColumnUnit.
            Allowed values for this property are: "DATA_SIZE", "TIME", "POWER", "TEMPERATURE", "CORE", "RATE", "FREQUENCY", "OTHER_STANDARD", "CUSTOM"
        :type unit_category: str

        :param display_name:
            The value to assign to the display_name property of this DataObjectCustomColumnUnit.
        :type display_name: str

        :param unit:
            The value to assign to the unit property of this DataObjectCustomColumnUnit.
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
        self._unit_category = 'CUSTOM'

    @property
    def unit(self):
        """
        Gets the unit of this DataObjectCustomColumnUnit.
        Custom column unit.


        :return: The unit of this DataObjectCustomColumnUnit.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this DataObjectCustomColumnUnit.
        Custom column unit.


        :param unit: The unit of this DataObjectCustomColumnUnit.
        :type: str
        """
        self._unit = unit

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
