# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TableLimits(object):
    """
    Throughput and storage limits configuration of a table.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TableLimits object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param max_read_units:
            The value to assign to the max_read_units property of this TableLimits.
        :type max_read_units: int

        :param max_write_units:
            The value to assign to the max_write_units property of this TableLimits.
        :type max_write_units: int

        :param max_storage_in_g_bs:
            The value to assign to the max_storage_in_g_bs property of this TableLimits.
        :type max_storage_in_g_bs: int

        """
        self.swagger_types = {
            'max_read_units': 'int',
            'max_write_units': 'int',
            'max_storage_in_g_bs': 'int'
        }

        self.attribute_map = {
            'max_read_units': 'maxReadUnits',
            'max_write_units': 'maxWriteUnits',
            'max_storage_in_g_bs': 'maxStorageInGBs'
        }

        self._max_read_units = None
        self._max_write_units = None
        self._max_storage_in_g_bs = None

    @property
    def max_read_units(self):
        """
        **[Required]** Gets the max_read_units of this TableLimits.
        Maximum sustained read throughput limit for the table.


        :return: The max_read_units of this TableLimits.
        :rtype: int
        """
        return self._max_read_units

    @max_read_units.setter
    def max_read_units(self, max_read_units):
        """
        Sets the max_read_units of this TableLimits.
        Maximum sustained read throughput limit for the table.


        :param max_read_units: The max_read_units of this TableLimits.
        :type: int
        """
        self._max_read_units = max_read_units

    @property
    def max_write_units(self):
        """
        **[Required]** Gets the max_write_units of this TableLimits.
        Maximum sustained write throughput limit for the table.


        :return: The max_write_units of this TableLimits.
        :rtype: int
        """
        return self._max_write_units

    @max_write_units.setter
    def max_write_units(self, max_write_units):
        """
        Sets the max_write_units of this TableLimits.
        Maximum sustained write throughput limit for the table.


        :param max_write_units: The max_write_units of this TableLimits.
        :type: int
        """
        self._max_write_units = max_write_units

    @property
    def max_storage_in_g_bs(self):
        """
        **[Required]** Gets the max_storage_in_g_bs of this TableLimits.
        Maximum size of storage used by the table.


        :return: The max_storage_in_g_bs of this TableLimits.
        :rtype: int
        """
        return self._max_storage_in_g_bs

    @max_storage_in_g_bs.setter
    def max_storage_in_g_bs(self, max_storage_in_g_bs):
        """
        Sets the max_storage_in_g_bs of this TableLimits.
        Maximum size of storage used by the table.


        :param max_storage_in_g_bs: The max_storage_in_g_bs of this TableLimits.
        :type: int
        """
        self._max_storage_in_g_bs = max_storage_in_g_bs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
