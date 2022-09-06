# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OperationInputRecord(object):
    """
    Holder for IN/INOUT parameter values.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OperationInputRecord object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param field_values:
            The value to assign to the field_values property of this OperationInputRecord.
        :type field_values: list[object]

        """
        self.swagger_types = {
            'field_values': 'list[object]'
        }

        self.attribute_map = {
            'field_values': 'fieldValues'
        }

        self._field_values = None

    @property
    def field_values(self):
        """
        Gets the field_values of this OperationInputRecord.
        Values of IN/INOUT parameter.


        :return: The field_values of this OperationInputRecord.
        :rtype: list[object]
        """
        return self._field_values

    @field_values.setter
    def field_values(self, field_values):
        """
        Sets the field_values of this OperationInputRecord.
        Values of IN/INOUT parameter.


        :param field_values: The field_values of this OperationInputRecord.
        :type: list[object]
        """
        self._field_values = field_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
