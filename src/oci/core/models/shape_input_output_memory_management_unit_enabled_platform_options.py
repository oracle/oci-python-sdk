# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ShapeInputOutputMemoryManagementUnitEnabledPlatformOptions(object):
    """
    Configuration options for the input-output memory management unit (IOMMU).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ShapeInputOutputMemoryManagementUnitEnabledPlatformOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param allowed_values:
            The value to assign to the allowed_values property of this ShapeInputOutputMemoryManagementUnitEnabledPlatformOptions.
        :type allowed_values: list[bool]

        :param is_default_enabled:
            The value to assign to the is_default_enabled property of this ShapeInputOutputMemoryManagementUnitEnabledPlatformOptions.
        :type is_default_enabled: bool

        """
        self.swagger_types = {
            'allowed_values': 'list[bool]',
            'is_default_enabled': 'bool'
        }

        self.attribute_map = {
            'allowed_values': 'allowedValues',
            'is_default_enabled': 'isDefaultEnabled'
        }

        self._allowed_values = None
        self._is_default_enabled = None

    @property
    def allowed_values(self):
        """
        Gets the allowed_values of this ShapeInputOutputMemoryManagementUnitEnabledPlatformOptions.
        Whether the input-output memory management unit can be enabled.


        :return: The allowed_values of this ShapeInputOutputMemoryManagementUnitEnabledPlatformOptions.
        :rtype: list[bool]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """
        Sets the allowed_values of this ShapeInputOutputMemoryManagementUnitEnabledPlatformOptions.
        Whether the input-output memory management unit can be enabled.


        :param allowed_values: The allowed_values of this ShapeInputOutputMemoryManagementUnitEnabledPlatformOptions.
        :type: list[bool]
        """
        self._allowed_values = allowed_values

    @property
    def is_default_enabled(self):
        """
        Gets the is_default_enabled of this ShapeInputOutputMemoryManagementUnitEnabledPlatformOptions.
        Whether the input-output memory management unit is enabled by default.


        :return: The is_default_enabled of this ShapeInputOutputMemoryManagementUnitEnabledPlatformOptions.
        :rtype: bool
        """
        return self._is_default_enabled

    @is_default_enabled.setter
    def is_default_enabled(self, is_default_enabled):
        """
        Sets the is_default_enabled of this ShapeInputOutputMemoryManagementUnitEnabledPlatformOptions.
        Whether the input-output memory management unit is enabled by default.


        :param is_default_enabled: The is_default_enabled of this ShapeInputOutputMemoryManagementUnitEnabledPlatformOptions.
        :type: bool
        """
        self._is_default_enabled = is_default_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
