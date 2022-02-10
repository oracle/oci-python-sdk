# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .patch_instruction import PatchInstruction
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchMergeInstruction(PatchInstruction):
    """
    An operation that recursively updates items of the selection, or adding the value if the selection is empty. If the value is not an object, it is used directly, otherwise each key-value member is used to create or update a member of the same name in the target and the same process is applied recursively for each object-typed value (similar to `RFC 7396`__ JSON Merge Patch, except that null values are copied rather than transformed into deletions). NOT_FOUND exceptions are handled by creating the implied containing structure. To avoid referential errors if an item's descendant is also in the selection, items of the selection are processed in order of decreasing depth.

    __ https://tools.ietf.org/html/rfc7396#section-2
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PatchMergeInstruction object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.PatchMergeInstruction.operation` attribute
        of this class is ``MERGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this PatchMergeInstruction.
            Allowed values for this property are: "INSERT", "REMOVE", "MERGE"
        :type operation: str

        :param selection:
            The value to assign to the selection property of this PatchMergeInstruction.
        :type selection: str

        :param value:
            The value to assign to the value property of this PatchMergeInstruction.
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
        self._operation = 'MERGE'

    @property
    def value(self):
        """
        Gets the value of this PatchMergeInstruction.
        A value to be merged into the target.


        :return: The value of this PatchMergeInstruction.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this PatchMergeInstruction.
        A value to be merged into the target.


        :param value: The value of this PatchMergeInstruction.
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
