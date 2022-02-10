# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .patch_instruction import PatchInstruction
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchInsertInstruction(PatchInstruction):
    """
    An operation that inserts a value into an array, shifting array items as necessary and handling NOT_FOUND exceptions by creating the implied containing structure.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PatchInsertInstruction object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.PatchInsertInstruction.operation` attribute
        of this class is ``INSERT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this PatchInsertInstruction.
            Allowed values for this property are: "INSERT", "REMOVE", "MERGE"
        :type operation: str

        :param selection:
            The value to assign to the selection property of this PatchInsertInstruction.
        :type selection: str

        :param value:
            The value to assign to the value property of this PatchInsertInstruction.
        :type value: object

        """
        self.swagger_types = {
            'operation': 'str',
            'selection': 'str',
            'value': 'object'
        }

        self.attribute_map = {
            'operation': 'operation',
            'selection': 'selection',
            'value': 'value'
        }

        self._operation = None
        self._selection = None
        self._value = None
        self._operation = 'INSERT'

    @property
    def value(self):
        """
        **[Required]** Gets the value of this PatchInsertInstruction.
        A value to be inserted into the target.


        :return: The value of this PatchInsertInstruction.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this PatchInsertInstruction.
        A value to be inserted into the target.


        :param value: The value of this PatchInsertInstruction.
        :type: object
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
