# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataObjectColumnUnit(object):
    """
    Unit details of a data object column.
    """

    #: A constant which can be used with the unit_category property of a DataObjectColumnUnit.
    #: This constant has a value of "DATA_SIZE"
    UNIT_CATEGORY_DATA_SIZE = "DATA_SIZE"

    #: A constant which can be used with the unit_category property of a DataObjectColumnUnit.
    #: This constant has a value of "TIME"
    UNIT_CATEGORY_TIME = "TIME"

    #: A constant which can be used with the unit_category property of a DataObjectColumnUnit.
    #: This constant has a value of "POWER"
    UNIT_CATEGORY_POWER = "POWER"

    #: A constant which can be used with the unit_category property of a DataObjectColumnUnit.
    #: This constant has a value of "TEMPERATURE"
    UNIT_CATEGORY_TEMPERATURE = "TEMPERATURE"

    #: A constant which can be used with the unit_category property of a DataObjectColumnUnit.
    #: This constant has a value of "CORE"
    UNIT_CATEGORY_CORE = "CORE"

    #: A constant which can be used with the unit_category property of a DataObjectColumnUnit.
    #: This constant has a value of "RATE"
    UNIT_CATEGORY_RATE = "RATE"

    #: A constant which can be used with the unit_category property of a DataObjectColumnUnit.
    #: This constant has a value of "FREQUENCY"
    UNIT_CATEGORY_FREQUENCY = "FREQUENCY"

    #: A constant which can be used with the unit_category property of a DataObjectColumnUnit.
    #: This constant has a value of "OTHER_STANDARD"
    UNIT_CATEGORY_OTHER_STANDARD = "OTHER_STANDARD"

    #: A constant which can be used with the unit_category property of a DataObjectColumnUnit.
    #: This constant has a value of "CUSTOM"
    UNIT_CATEGORY_CUSTOM = "CUSTOM"

    def __init__(self, **kwargs):
        """
        Initializes a new DataObjectColumnUnit object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.DataObjectCoreColumnUnit`
        * :class:`~oci.opsi.models.DataObjectTimeColumnUnit`
        * :class:`~oci.opsi.models.DataObjectOtherStandardColumnUnit`
        * :class:`~oci.opsi.models.DataObjectCustomColumnUnit`
        * :class:`~oci.opsi.models.DataObjectTemperatureColumnUnit`
        * :class:`~oci.opsi.models.DataObjectPowerColumnUnit`
        * :class:`~oci.opsi.models.DataObjectRateColumnUnit`
        * :class:`~oci.opsi.models.DataObjectFrequencyColumnUnit`
        * :class:`~oci.opsi.models.DataObjectDataSizeColumnUnit`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param unit_category:
            The value to assign to the unit_category property of this DataObjectColumnUnit.
            Allowed values for this property are: "DATA_SIZE", "TIME", "POWER", "TEMPERATURE", "CORE", "RATE", "FREQUENCY", "OTHER_STANDARD", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type unit_category: str

        :param display_name:
            The value to assign to the display_name property of this DataObjectColumnUnit.
        :type display_name: str

        """
        self.swagger_types = {
            'unit_category': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'unit_category': 'unitCategory',
            'display_name': 'displayName'
        }

        self._unit_category = None
        self._display_name = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['unitCategory']

        if type == 'CORE':
            return 'DataObjectCoreColumnUnit'

        if type == 'TIME':
            return 'DataObjectTimeColumnUnit'

        if type == 'OTHER_STANDARD':
            return 'DataObjectOtherStandardColumnUnit'

        if type == 'CUSTOM':
            return 'DataObjectCustomColumnUnit'

        if type == 'TEMPERATURE':
            return 'DataObjectTemperatureColumnUnit'

        if type == 'POWER':
            return 'DataObjectPowerColumnUnit'

        if type == 'RATE':
            return 'DataObjectRateColumnUnit'

        if type == 'FREQUENCY':
            return 'DataObjectFrequencyColumnUnit'

        if type == 'DATA_SIZE':
            return 'DataObjectDataSizeColumnUnit'
        else:
            return 'DataObjectColumnUnit'

    @property
    def unit_category(self):
        """
        **[Required]** Gets the unit_category of this DataObjectColumnUnit.
        Category of the column's unit.

        Allowed values for this property are: "DATA_SIZE", "TIME", "POWER", "TEMPERATURE", "CORE", "RATE", "FREQUENCY", "OTHER_STANDARD", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The unit_category of this DataObjectColumnUnit.
        :rtype: str
        """
        return self._unit_category

    @unit_category.setter
    def unit_category(self, unit_category):
        """
        Sets the unit_category of this DataObjectColumnUnit.
        Category of the column's unit.


        :param unit_category: The unit_category of this DataObjectColumnUnit.
        :type: str
        """
        allowed_values = ["DATA_SIZE", "TIME", "POWER", "TEMPERATURE", "CORE", "RATE", "FREQUENCY", "OTHER_STANDARD", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(unit_category, allowed_values):
            unit_category = 'UNKNOWN_ENUM_VALUE'
        self._unit_category = unit_category

    @property
    def display_name(self):
        """
        Gets the display_name of this DataObjectColumnUnit.
        Display name of the column's unit.


        :return: The display_name of this DataObjectColumnUnit.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DataObjectColumnUnit.
        Display name of the column's unit.


        :param display_name: The display_name of this DataObjectColumnUnit.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
