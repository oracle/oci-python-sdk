# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RequestUsage(object):
    """
    The usage metrics for a request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RequestUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param read_units_consumed:
            The value to assign to the read_units_consumed property of this RequestUsage.
        :type read_units_consumed: int

        :param write_units_consumed:
            The value to assign to the write_units_consumed property of this RequestUsage.
        :type write_units_consumed: int

        """
        self.swagger_types = {
            'read_units_consumed': 'int',
            'write_units_consumed': 'int'
        }

        self.attribute_map = {
            'read_units_consumed': 'readUnitsConsumed',
            'write_units_consumed': 'writeUnitsConsumed'
        }

        self._read_units_consumed = None
        self._write_units_consumed = None

    @property
    def read_units_consumed(self):
        """
        Gets the read_units_consumed of this RequestUsage.
        Read Units consumed by this operation.


        :return: The read_units_consumed of this RequestUsage.
        :rtype: int
        """
        return self._read_units_consumed

    @read_units_consumed.setter
    def read_units_consumed(self, read_units_consumed):
        """
        Sets the read_units_consumed of this RequestUsage.
        Read Units consumed by this operation.


        :param read_units_consumed: The read_units_consumed of this RequestUsage.
        :type: int
        """
        self._read_units_consumed = read_units_consumed

    @property
    def write_units_consumed(self):
        """
        Gets the write_units_consumed of this RequestUsage.
        Write Units consumed by this operation.


        :return: The write_units_consumed of this RequestUsage.
        :rtype: int
        """
        return self._write_units_consumed

    @write_units_consumed.setter
    def write_units_consumed(self, write_units_consumed):
        """
        Sets the write_units_consumed of this RequestUsage.
        Write Units consumed by this operation.


        :param write_units_consumed: The write_units_consumed of this RequestUsage.
        :type: int
        """
        self._write_units_consumed = write_units_consumed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
